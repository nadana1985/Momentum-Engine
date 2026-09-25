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

from momentum_v10.config import ROOT, TAPE_DIR
from momentum_v10.logger import get_logger, check_disk_space

logger = get_logger("system")


def render_report(status: dict) -> tuple[str, str]:
    flag = "" if status.get("ok") else " FAILED"
    subject = (
        f"V10 hourly{flag}: {status.get('open', 0)} open, "
        f"{status.get('closed', 0)} closed ({status.get('closed_this_hour', 0)} new)"
    )
    lines = [
        f"Open trades: {status.get('open', 0)}",
        "Closed trades: "
        f"{status.get('closed', 0)} (open_at_end marks excluded)",
        f"Closed this hour: {status.get('closed_this_hour', 0)}",
        f"Ingest updated: {status.get('ingest_updated', 0)}  failed: {status.get('ingest_failed', 0)}",
        f"Assets: {status.get('assets', 0)}  failed: {status.get('assets_failed', 0)}",
        f"Started UTC: {status.get('started_utc', '')}",
        f"Finished UTC: {status.get('finished_utc', '')}",
    ]
    if status.get("error"):
        lines.append(f"Error: {status['error']}")
    return subject, "\n".join(lines) + "\n"


def send_report(status: dict) -> bool:
    from_addr = os.environ.get("V10_SES_FROM", "").strip()
    to_raw = os.environ.get("V10_ALERT_TO", "").strip()
    subject, body = render_report(status)
    if not from_addr or not to_raw:
        logger.warning("[hourly] Email not sent. V10_SES_FROM and V10_ALERT_TO not set in environment.")
        return False
    tos = [item.strip() for item in to_raw.split(",") if item.strip()]
    region = os.environ.get("AWS_DEFAULT_REGION") or os.environ.get("AWS_REGION") or "us-east-1"
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
    os.chdir(ROOT)
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))

    t_run_start = time.perf_counter()
    started = datetime.now(timezone.utc)
    logger.info(f"========== Kronos V10 Hourly Clock Started ({started.strftime('%Y-%m-%d %H:%M:%S UTC')}) ==========")

    # Host diagnostics: check disk space before execution
    disk = check_disk_space(ROOT / "data")
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
    }
    try:
        from config.ingestion.live_bridger import run_bridger
        from momentum_v10.build_csv import write_all_trades_view
        from momentum_v10.live_runner import run as run_live

        # Phase 1: Ingestion
        t_ingest_start = time.perf_counter()
        ingest = run_bridger()
        t_ingest = time.perf_counter() - t_ingest_start
        status["ingest_updated"] = int(ingest.get("updated", 0))
        status["ingest_failed"] = int(ingest.get("failed", 0))
        logger.info(f"[hourly] Phase 1 (Ingestion) completed in {t_ingest:.1f}s | Updated={status['ingest_updated']} Failed={status['ingest_failed']}")

        # Phase 2: Live Runner & State Update
        t_live_start = time.perf_counter()
        live = run_live()
        t_live = time.perf_counter() - t_live_start
        for key in ("open", "closed", "closed_this_hour", "assets", "assets_failed"):
            status[key] = int(live[key])
        logger.info(f"[hourly] Phase 2 (Live Compute) completed in {t_live:.1f}s | Open={status['open']} Closed={status['closed']} NewClosed={status['closed_this_hour']}")

        write_all_trades_view()
        if live["assets"] <= 0:
            status["error"] = "no assets discovered"
            logger.error("[hourly] Error: no assets discovered in shard directory.")
        elif live["assets_failed"] >= live["assets"]:
            status["error"] = "live runner failed every asset"
            logger.critical("[hourly] Critical: live runner failed on every asset.")
        else:
            status["ok"] = True
    except Exception as e:
        status["error"] = f"{type(e).__name__}: {e}"
        logger.error(f"[hourly] Pipeline exception: {status['error']}", exc_info=True)

    status["finished_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    TAPE_DIR.mkdir(parents=True, exist_ok=True)
    (TAPE_DIR / "hourly_status.json").write_text(json.dumps(status, indent=2), encoding="utf-8")

    sent = send_report(status)

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

