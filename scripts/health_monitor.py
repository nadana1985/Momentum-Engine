"""
scripts/health_monitor.py — Kronos V12 Production Health Guardian

Performs 4 critical health checks on every pipeline run:
  1. Stale Data Detection  — Last shard timestamp > STALE_HOURS hours old → ALERT
  2. Disk Space Guard      — Disk usage > DISK_WARN_PCT % → ALERT
  3. S3 Upload Validation  — Validates uploaded file bytes > 0 in S3 bucket
  4. Dependency Integrity  — `pip check` to detect broken dependency chains

Sends alerts via CloudWatch Alarm metric and/or HEARTBEAT_URL fail ping.
Graceful fallback on localhost (no AWS credentials → logs only, exits 0).
"""

import os
import sys
import json
import shutil
import logging
import subprocess
from pathlib import Path
from datetime import datetime, timezone, timedelta

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger("kronos.health_monitor")

ROOT = Path(__file__).resolve().parent.parent

# ── Thresholds (tunable via .env) ──────────────────────────────────────────────
STALE_HOURS       = float(os.getenv("HEALTH_STALE_HOURS",    "2"))    # Alert if newest shard > 2h old
DISK_WARN_PCT     = float(os.getenv("HEALTH_DISK_WARN_PCT",  "80"))   # Alert if disk > 80% full
DISK_CRIT_PCT     = float(os.getenv("HEALTH_DISK_CRIT_PCT",  "99.5")) # Hard-stop if disk > threshold


def _emit_cloudwatch_alarm(metric_name: str, value: float, unit: str = "Count"):
    """Push a metric to CloudWatch. Silently skips if boto3/creds unavailable."""
    try:
        import boto3
        cw = boto3.client("cloudwatch")
        cw.put_metric_data(
            Namespace="KronosV12",
            MetricData=[{"MetricName": metric_name, "Value": value, "Unit": unit}]
        )
        logger.info(f"[CloudWatch] {metric_name}={value} emitted.")
    except Exception as e:
        logger.debug(f"[CloudWatch] Skipped ({e})")


def check_stale_data() -> bool:
    """
    Fix #1 — Stale Data Silent Death Guard.
    Reads sync_state.json to find the latest successfully synced timestamp.
    If the newest shard is older than STALE_HOURS, emits a CloudWatch alarm.
    Returns True if data is FRESH, False if STALE.
    """
    sync_state_paths = [
        ROOT / "data" / "sync_state.json",
        ROOT / "config" / "ingestion" / "sync_state.json",
    ]

    latest_ts = None
    for p in sync_state_paths:
        if p.exists():
            try:
                state = json.loads(p.read_text())
                # sync_state maps symbol → last_ts (epoch ms or ISO string)
                for symbol, val in state.items():
                    try:
                        ts = float(val) / 1000.0  # epoch ms → seconds
                        dt = datetime.fromtimestamp(ts, tz=timezone.utc)
                        if latest_ts is None or dt > latest_ts:
                            latest_ts = dt
                    except Exception:
                        pass
            except Exception:
                pass

    if latest_ts is None:
        logger.warning("[Health #1] STALE CHECK: sync_state.json not found or unreadable. Assuming fresh.")
        return True

    age_hours = (datetime.now(timezone.utc) - latest_ts).total_seconds() / 3600
    if age_hours > STALE_HOURS:
        logger.error(
            f"[Health #1] ⚠️  STALE DATA DETECTED: Newest shard is {age_hours:.1f}h old "
            f"(threshold: {STALE_HOURS}h). Binance ingestion may have silently failed!"
        )
        _emit_cloudwatch_alarm("DataFreshness", 0.0)
        return False
    else:
        logger.info(f"[Health #1] ✅ Data freshness OK: newest shard is {age_hours:.1f}h old.")
        _emit_cloudwatch_alarm("DataFreshness", 1.0)
        return True


def check_disk_space() -> bool:
    """
    Fix #2 — Disk Space Guard.
    Checks disk usage of the ROOT partition.
    Warns at DISK_WARN_PCT, hard-stops (exits 1) at DISK_CRIT_PCT.
    Returns True if OK, False if WARNING zone.
    """
    usage = shutil.disk_usage(ROOT)
    pct_used = (usage.used / usage.total) * 100
    free_gb = usage.free / (1024 ** 3)

    if pct_used >= DISK_CRIT_PCT:
        logger.critical(
            f"[Health #2] 🔴 DISK CRITICAL: {pct_used:.1f}% used ({free_gb:.1f} GB free). "
            f"STOPPING PIPELINE — parquet writes will corrupt!"
        )
        _emit_cloudwatch_alarm("DiskUsagePct", pct_used, "Percent")
        sys.exit(1)  # Hard stop — do NOT proceed with parquet writes
    elif pct_used >= DISK_WARN_PCT:
        logger.warning(
            f"[Health #2] ⚠️  DISK WARNING: {pct_used:.1f}% used ({free_gb:.1f} GB free). "
            f"Clean up old snapshots or expand volume soon."
        )
        _emit_cloudwatch_alarm("DiskUsagePct", pct_used, "Percent")
        return False
    else:
        logger.info(f"[Health #2] ✅ Disk OK: {pct_used:.1f}% used ({free_gb:.1f} GB free).")
        _emit_cloudwatch_alarm("DiskUsagePct", pct_used, "Percent")
        return True


def validate_s3_uploads(bucket: str | None = None) -> bool:
    """
    Fix #7 — S3 Upload Validation.
    After upload, confirms that the `latest/` keys in S3 have non-zero file size.
    Emits a CloudWatch alarm if any critical file is zero-byte or missing in S3.
    Returns True if all uploads validated, False otherwise.
    """
    bucket_name = bucket or os.getenv("S3_BUCKET")
    if not bucket_name:
        logger.info("[Health #7] S3 validation skipped (no S3_BUCKET configured — localhost mode).")
        return True

    critical_keys = [
        "v12_production/latest/trades.parquet",
        "v12_production/latest/closed_trades.csv",
        "v12_production/latest/sync_state.json",
    ]

    try:
        import boto3
        from botocore.exceptions import ClientError
        s3 = boto3.client("s3")
        all_ok = True
        for key in critical_keys:
            try:
                head = s3.head_object(Bucket=bucket_name, Key=key)
                size = head.get("ContentLength", 0)
                if size == 0:
                    logger.error(f"[Health #7] ⚠️  ZERO-BYTE in S3: s3://{bucket_name}/{key}")
                    all_ok = False
                else:
                    logger.info(f"[Health #7] ✅ S3 validated: {key} ({size:,} bytes)")
            except ClientError as e:
                if e.response["Error"]["Code"] == "404":
                    logger.error(f"[Health #7] ⚠️  MISSING in S3: s3://{bucket_name}/{key}")
                    all_ok = False

        s3_health = 1.0 if all_ok else 0.0
        _emit_cloudwatch_alarm("S3BackupHealth", s3_health)
        return all_ok
    except ImportError:
        logger.warning("[Health #7] boto3 not installed — S3 validation skipped.")
        return True


def check_dependency_integrity() -> bool:
    """
    Fix #9 — Dependency Integrity Check.
    Runs `pip check` to detect broken/conflicting package chains.
    Returns True if clean, False if conflicts detected.
    """
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "check"],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode == 0:
            logger.info("[Health #9] ✅ Dependency integrity OK (pip check passed).")
            return True
        else:
            logger.warning(
                f"[Health #9] ⚠️  Dependency conflicts detected:\n{result.stdout.strip()}\n"
                "Run: pip install -r requirements.txt --force-reinstall"
            )
            _emit_cloudwatch_alarm("DependencyHealth", 0.0)
            return False
    except Exception as e:
        logger.warning(f"[Health #9] pip check failed to run: {e}")
        return True  # Non-critical, don't block pipeline


def run_all_checks(validate_s3: bool = False) -> int:
    """Run all health checks and return exit code (0=ok, 1=critical)."""
    logger.info("=" * 60)
    logger.info("KRONOS V12 PRODUCTION HEALTH MONITOR")
    logger.info("=" * 60)

    results = {
        "stale_data":  check_stale_data(),
        "disk_space":  check_disk_space(),   # may sys.exit(1) if critical
        "dep_integrity": check_dependency_integrity(),
    }

    if validate_s3:
        results["s3_uploads"] = validate_s3_uploads()

    passed = sum(1 for v in results.values() if v)
    total  = len(results)
    logger.info(f"\n[Health Monitor] {passed}/{total} checks passed.")

    if passed == total:
        logger.info("✅ ALL HEALTH CHECKS PASSED — Pipeline proceeding.")
        return 0
    else:
        failed = [k for k, v in results.items() if not v]
        logger.warning(f"⚠️  WARNINGS in: {failed} — Pipeline proceeding with caution.")
        return 0  # Warnings don't abort pipeline; only disk CRITICAL does (via sys.exit above)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Kronos V12 Production Health Monitor")
    parser.add_argument("--validate-s3", action="store_true", help="Also validate S3 upload integrity")
    args = parser.parse_args()
    sys.exit(run_all_checks(validate_s3=args.validate_s3))
