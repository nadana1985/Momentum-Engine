"""
scripts/disk_cleanup.py — Kronos V12 Automated Disk Housekeeping

Safely removes old S3 snapshot ledger copies that are older than RETENTION_DAYS
from the LOCAL data directory to prevent disk exhaustion.

Rules:
  - NEVER deletes raw_shards/ (source of truth for all backtests)
  - NEVER deletes the latest/ production parquet tapes
  - Only cleans: data/all_tapes/*/  older than RETENTION_DAYS (arm experiment snapshots)
  - Logs every deletion for audit trail

Run manually or add to a weekly cron job.
"""

import os
import sys
import logging
import shutil
from pathlib import Path
from datetime import datetime, timezone, timedelta

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger("kronos.disk_cleanup")

ROOT = Path(__file__).resolve().parent.parent

RETENTION_DAYS = int(os.getenv("CLEANUP_RETENTION_DAYS", "90"))  # Keep 90 days of arm experiments
PROTECTED_ARMS = {"v12_production"}                                # Never touch production arm


def cleanup_old_arm_experiments() -> int:
    """Remove arm experiment folders older than RETENTION_DAYS. Returns freed bytes."""
    tapes_dir = ROOT / "data" / "all_tapes"
    if not tapes_dir.exists():
        logger.info("No all_tapes directory found. Nothing to clean.")
        return 0

    cutoff = datetime.now(timezone.utc) - timedelta(days=RETENTION_DAYS)
    freed_bytes = 0

    for arm_dir in tapes_dir.iterdir():
        if not arm_dir.is_dir():
            continue
        if arm_dir.name in PROTECTED_ARMS:
            logger.info(f"[Cleanup] ⛔ Protected arm skipped: {arm_dir.name}")
            continue

        # Check modification time
        mtime = datetime.fromtimestamp(arm_dir.stat().st_mtime, tz=timezone.utc)
        if mtime < cutoff:
            size = sum(f.stat().st_size for f in arm_dir.rglob("*") if f.is_file())
            shutil.rmtree(arm_dir)
            freed_bytes += size
            logger.info(f"[Cleanup] 🗑️  Removed old arm: {arm_dir.name} (mtime={mtime.date()}, freed={size/(1024**2):.1f} MB)")
        else:
            logger.info(f"[Cleanup] ✅ Kept recent arm: {arm_dir.name} (mtime={mtime.date()})")

    return freed_bytes


def cleanup_old_log_entries():
    """
    Fix #4 — Journald size enforcement via logrotate config.
    This function just reports the current journal disk usage;
    the actual journald limit is enforced in /etc/systemd/journald.conf by setup_ec2.sh.
    """
    try:
        import subprocess
        result = subprocess.run(
            ["journalctl", "--disk-usage"],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            logger.info(f"[Cleanup] journald usage: {result.stdout.strip()}")
        # Vacuum logs older than 30 days
        subprocess.run(
            ["journalctl", "--vacuum-time=30d"],
            capture_output=True, timeout=30
        )
        logger.info("[Cleanup] journald vacuumed: entries older than 30 days removed.")
    except Exception as e:
        logger.debug(f"[Cleanup] journald vacuum skipped (Windows or permission): {e}")


def report_disk_usage():
    """Print a disk usage summary."""
    import shutil as _shutil
    usage = _shutil.disk_usage(ROOT)
    total_gb  = usage.total / (1024 ** 3)
    used_gb   = usage.used  / (1024 ** 3)
    free_gb   = usage.free  / (1024 ** 3)
    pct_used  = (usage.used / usage.total) * 100
    logger.info(f"[Disk] Total: {total_gb:.1f} GB | Used: {used_gb:.1f} GB ({pct_used:.1f}%) | Free: {free_gb:.1f} GB")


if __name__ == "__main__":
    logger.info("=" * 60)
    logger.info("KRONOS V12 DISK HOUSEKEEPING")
    logger.info("=" * 60)
    report_disk_usage()
    freed = cleanup_old_arm_experiments()
    cleanup_old_log_entries()
    logger.info(f"[Cleanup] Total freed: {freed / (1024**2):.1f} MB")
    report_disk_usage()
    sys.exit(0)
