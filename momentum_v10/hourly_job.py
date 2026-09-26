"""Hourly production clock: REST ingest, live compute, SES trade-count email.

Does not run the research matrix (build_v10_tape) or the websocket daemon.
Those either rewrite the live ledger or append malformed candles.

Mail is Amazon SES. Set:
  V10_SES_FROM=alerts@your-domain
  V10_ALERT_TO=you@your-domain          (comma-separated is allowed)
  AWS_DEFAULT_REGION=us-east-1
The instance role or environment must be allowed ses:SendEmail, and the
from-address must be a verified SES identity.
"""
from __future__ import annotations

import json
import os
import sys
import time
from datetime import datetime, timezone

from momentum_v10.config import DATA_ROOT, ROOT, SHARD_DIR, TAPE_DIR
from momentum_v10.logger import get_logger, check_disk_space
from momentum_v10.io_utils import RunLockedError, atomic_write_text, run_lock

logger = get_logger("system")


def render_report(status: dict) -> tuple[str, str]:
    flag = "" if status.get("ok") else " FAILED"
    sigs = status.get("new_signals") or []
    fresh = [s for s in sigs if (s.get("age_hours") or 99) <= 1.5]
    subject = (
        f"V10 hourly{flag}: {status.get('open', 0)} open, "
        f"{status.get('closed', 0)} closed ({status.get('closed_this_hour', 0)} new)"
        + (f", {len(fresh)} new signal{'s' if len(fresh) != 1 else ''}" if fresh else "")
    )
    lines = [
        f"Open trades: {status.get('open', 0)}",
        "Closed trades: "
        f"{status.get('closed', 0)} (open_at_end marks excluded)",
        f"Closed this hour: {status.get('closed_this_hour', 0)}",
        f"Ingest updated: {status.get('ingest_updated', 0)}  failed: {status.get('ingest_failed', 0)}  "
        f"delisted (skipped): {status.get('ingest_delisted', 0)}",
        f"Assets: {status.get('assets', 0)}  failed: {status.get('assets_failed', 0)}",
        f"Ingest seconds: {status.get('ingest_seconds', 0)}  Run seconds: {status.get('run_seconds', 0)}",
        f"Fresh shards: {status.get('fresh_pct')}%   Data root: {status.get('data_root', '')}",
        f"Backup: {status.get('backup', 'n/a')}   Dashboard: {status.get('site', 'n/a')}",
        f"Started UTC: {status.get('started_utc', '')}",
        f"Finished UTC: {status.get('finished_utc', '')}",
    ]
    if status.get("error"):
        lines.append(f"Error: {status['error']}")
    lines += ["", f"New signals (last 24h): {len(sigs)}   (* = entered this hour)"]
    if sigs:
        lines.append(f"  {'Asset':<12}{'Engine':<22}{'Entry UTC':<18}{'Entry px':>12}{'Now':>12}{'Stop':>12}{'To stop':>9}{'PnL':>8}")
        def f(v):
            return "-" if v is None else f"{v:.6g}"
        for s in sigs[:30]:
            mark = "*" if (s.get("age_hours") or 99) <= 1.5 else " "
            to_stop = "-" if s.get("stop_pct") is None else f"{s['stop_pct']:+.1f}%"
            pnl = "-" if s.get("pnl_pct") is None else f"{s['pnl_pct']:+.1f}%"
            lines.append(f"{mark} {s['asset']:<12}{s['engine']:<22}{s['entry']:<18}"
                         f"{f(s.get('entry_price')):>12}{f(s.get('current_price')):>12}{f(s.get('stop')):>12}{to_stop:>9}{pnl:>8}")
        lines.append("  Stop = exit if an hourly candle closes below it. Paper signals, not advice.")
    return subject, "\n".join(lines) + "\n"


def raw_fresh_pct(now: datetime) -> float | None:
    """Share of raw shards whose last bar is the latest closed hour."""
    try:
        from config.ingestion.sync_state_manager import SYNC_STATE_PATH
        raw = json.loads(SYNC_STATE_PATH.read_text()).get("raw", {})
    except Exception as e:
        logger.warning(f"[hourly] Could not read sync state for freshness: {e}")
        return None
    names = [p.name[: -len("_1h.parquet")] for p in SHARD_DIR.glob("*_USDT_1h.parquet")
             if p.name.split("_")[0].isalnum() and p.name.split("_")[0].isascii()]
    if not names:
        return 0.0
    now_ms = int(now.timestamp() * 1000)
    expected = now_ms - now_ms % 3_600_000 - 3_600_000   # open time of last closed bar
    fresh = sum(1 for n in names if int(raw.get(n, 0) or 0) >= expected)
    return round(100.0 * fresh / len(names), 1)


def _aws_region() -> str:
    return os.environ.get("AWS_DEFAULT_REGION") or os.environ.get("AWS_REGION") or "eu-west-2"


def send_report_sns(topic_arn: str, status: dict) -> bool:
    """Publish the report to an SNS topic (email subscribers confirm once)."""
    subject, body = render_report(status)
    # SNS email subjects: ASCII, no newlines, <= 100 chars.
    subject = subject.encode("ascii", "replace").decode().replace("\n", " ")[:100]
    try:
        import boto3
        region = topic_arn.split(":")[3] if topic_arn.count(":") >= 5 else _aws_region()
        resp = boto3.client("sns", region_name=region).publish(
            TopicArn=topic_arn, Subject=subject, Message=body)
        logger.info(f"[hourly] SNS report published: MessageId={resp.get('MessageId', 'unknown')}")
        return True
    except Exception as e:
        logger.error(f"[hourly] SNS publish failed: {e}")
        return False


def send_report(status: dict) -> bool:
    topic_arn = os.environ.get("V10_SNS_TOPIC_ARN", "").strip()
    if topic_arn:
        return send_report_sns(topic_arn, status)
    from_addr = os.environ.get("V10_SES_FROM", "").strip()
    to_raw = os.environ.get("V10_ALERT_TO", "").strip()
    subject, body = render_report(status)
    if not from_addr or not to_raw:
        logger.warning("[hourly] Report not sent: set V10_SNS_TOPIC_ARN (or V10_SES_FROM + V10_ALERT_TO).")
        return False
    tos = [item.strip() for item in to_raw.split(",") if item.strip()]
    region = (os.environ.get("V10_SES_REGION") or os.environ.get("AWS_DEFAULT_REGION")
              or os.environ.get("AWS_REGION") or "eu-west-2")
    try:
        import boto3
        client = boto3.client("ses", region_name=region)
        resp = client.send_email(
            Source=from_addr,
            Destination={"ToAddresses": tos},
            Message={
                "Subject": {"Data": subject, "Charset": "UTF-8"},
                "Body": {"Text": {"Data": body, "Charset": "UTF-8"}},
            },
        )
        msg_id = resp.get("MessageId", "unknown")
        logger.info(f"[hourly] SES email successfully dispatched to {', '.join(tos)}: MessageId={msg_id}")
        return True
    except Exception as e:
        logger.error(f"[hourly] SES email dispatch failed: {e}")
        return False


def main() -> int:
    try:
        with run_lock(DATA_ROOT / ".hourly.lock"):
            return _run()
    except RunLockedError as e:
        logger.warning(f"[hourly] Previous run still active ({e}); skipping this hour.")
        return 3


def _run() -> int:
    os.chdir(ROOT)
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))

    t_run_start = time.perf_counter()
    started = datetime.now(timezone.utc)
    logger.info(f"========== Kronos V10 Hourly Clock Started ({started.strftime('%Y-%m-%d %H:%M:%S UTC')}) ==========")

    # Host diagnostics: check disk space before execution
    disk = check_disk_space(DATA_ROOT)
    if not disk.get("healthy", True):
        logger.warning(f"[hourly] Running with reduced free disk space: {disk.get('free_gb')} GB free ({disk.get('free_pct')}%)")

    status = {
        "started_utc": started.strftime("%Y-%m-%d %H:%M:%S"),
        "open": 0,
        "closed": 0,
        "closed_this_hour": 0,
        "ingest_updated": 0,
        "ingest_failed": 0,
        "assets": 0,
        "assets_failed": 0,
        "ok": False,
        "error": "",
        "data_root": str(DATA_ROOT),
        "fresh_pct": None,
    }
    try:
        # Fail closed on a wrong/empty data root instead of "succeeding" on nothing.
        n_shards = len(list(SHARD_DIR.glob("*_USDT_1h.parquet"))) if SHARD_DIR.exists() else 0
        min_shards = int(os.environ.get("V10_MIN_SHARDS", "100"))
        if n_shards < min_shards:
            raise RuntimeError(f"data root {DATA_ROOT} has {n_shards} raw shards (< {min_shards}); "
                               f"set V10_DATA_ROOT or restore data")

        from config.ingestion.live_bridger import run_bridger
        from momentum_v10.build_csv import write_all_trades_view
        from momentum_v10.live_runner import run as run_live

        # Phase 1: Ingestion
        t_ingest_start = time.perf_counter()
        ingest = run_bridger()
        t_ingest = time.perf_counter() - t_ingest_start
        status["ingest_updated"] = int(ingest.get("updated", 0))
        status["ingest_failed"] = int(ingest.get("failed", 0))
        status["ingest_delisted"] = int(ingest.get("delisted", 0))
        status["ingest_seconds"] = round(t_ingest, 1)
        if ingest.get("banned"):
            status["error"] = "Binance refused requests (418 ban or 451 region block); see logs"
        logger.info(f"[hourly] Phase 1 (Ingestion) completed in {t_ingest:.1f}s | Updated={status['ingest_updated']} Failed={status['ingest_failed']}")

        # Phase 2: Live Runner & State Update
        t_live_start = time.perf_counter()
        live = run_live()
        t_live = time.perf_counter() - t_live_start
        for key in ("open", "closed", "closed_this_hour", "assets", "assets_failed"):
            status[key] = int(live[key])
        logger.info(f"[hourly] Phase 2 (Live Compute) completed in {t_live:.1f}s | Open={status['open']} Closed={status['closed']} NewClosed={status['closed_this_hour']}")

        write_all_trades_view()
        try:
            import pandas as pd
            from momentum_v10.live_book import new_signals
            from momentum_v10.live_runner import OPEN_TRADES_FILE
            status["new_signals"] = new_signals(pd.read_csv(OPEN_TRADES_FILE)) if OPEN_TRADES_FILE.exists() else []
        except Exception as e:
            logger.warning(f"[hourly] could not build new-signal list: {e}")
            status["new_signals"] = []
        fresh_pct = raw_fresh_pct(started)
        status["fresh_pct"] = fresh_pct
        min_fresh = float(os.environ.get("V10_MIN_FRESH_PCT", "80"))
        max_fail = float(os.environ.get("V10_MAX_FAIL_PCT", "20"))
        n_sym = max(1, int(ingest.get("symbols", 0)) - status["ingest_delisted"])
        if live["assets"] <= 0:
            status["error"] = "no assets discovered"
            logger.error("[hourly] Error: no assets discovered in shard directory.")
        elif live["assets_failed"] >= live["assets"]:
            status["error"] = "live runner failed every asset"
            logger.critical("[hourly] Critical: live runner failed on every asset.")
        elif ingest.get("banned"):
            logger.critical("[hourly] Ingest halted by Binance; results use stale data.")
        elif fresh_pct is not None and fresh_pct < min_fresh:
            status["error"] = f"stale data: only {fresh_pct:.1f}% of raw shards hold the last closed bar (< {min_fresh:g}%)"
            logger.critical(f"[hourly] {status['error']}")
        elif 100.0 * live["assets_failed"] / live["assets"] > max_fail:
            status["error"] = f"{live['assets_failed']}/{live['assets']} assets failed (> {max_fail:g}%)"
            logger.critical(f"[hourly] {status['error']}")
        elif 100.0 * status["ingest_failed"] / n_sym > max_fail:
            status["error"] = f"{status['ingest_failed']}/{n_sym} symbols failed ingest (> {max_fail:g}%)"
            logger.critical(f"[hourly] {status['error']}")
        else:
            status["ok"] = True
    except Exception as e:
        status["error"] = f"{type(e).__name__}: {e}"
        logger.error(f"[hourly] Pipeline exception: {status['error']}", exc_info=True)

    status["finished_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    TAPE_DIR.mkdir(parents=True, exist_ok=True)
    status["run_seconds"] = round(time.perf_counter() - t_run_start, 1)
    atomic_write_text(TAPE_DIR / "hourly_status.json", json.dumps(status, indent=2))

    from momentum_v10 import ops
    try:
        b = ops.backup()
        status["backup"] = "off" if not b.get("enabled") else f"ok ({b['latest']} latest, {b['daily']} daily, {b['shards']} shards)"
    except Exception as e:
        status["backup"] = f"FAILED: {type(e).__name__}: {e}"
        logger.error(f"[hourly] S3 backup failed: {e}", exc_info=True)

    try:
        site = ops.publish_site()
        status["site"] = "off" if not site.get("enabled") else f"ok ({site['files']} files)"
    except Exception as e:
        status["site"] = f"FAILED: {type(e).__name__}: {e}"
        logger.error(f"[hourly] dashboard publish failed: {e}", exc_info=True)

    sent = send_report(status)
    ops.heartbeat(status)

    t_total = time.perf_counter() - t_run_start
    result_flag = "SUCCESS" if status["ok"] else "FAILED"
    logger.info(f"========== Kronos V10 Hourly Clock Finished in {t_total:.1f}s [{result_flag}] ==========")

    if not status["ok"]:
        return 1
    if not sent:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

