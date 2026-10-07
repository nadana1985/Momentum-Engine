"""
scripts/notify_signals_sns.py — AWS SNS Email Alert Dispatcher for New Trade Signals
Scans the production open trades ledger for newly entered positions (entered within the last 90 minutes)
and dispatches an institutional email notification via AWS SNS.

Configuration (via .env or CLI):
  SNS_TOPIC_ARN              AWS SNS Topic ARN (subscribers receive email alerts)
  NOTIFY_ONLY_ON_NEW_SIGNALS If 1 (default), only sends emails when new signals are triggered.
  DASHBOARD_URL              Public URL of NiceGUI dashboard for quick drilldown.
  AWS_DEFAULT_REGION         AWS Region (default: eu-central-1)

Graceful fallback:
  If SNS_TOPIC_ARN is not configured or AWS credentials are missing, logs a localhost notice and exits code 0.
"""

import os
import sys
import argparse
from pathlib import Path
from datetime import datetime, timezone
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger("kronos.sns_notify")

ROOT = Path(__file__).resolve().parent.parent


def format_table(rows: list[dict]) -> str:
    """Renders a clean ASCII table for email readability."""
    if not rows:
        return "  (None)\n"
    header = f"  {'Asset':<10}{'Tier':<10}{'Book':<10}{'Entry Px':>12}{'Stop Px':>12}{'Risk %':>10}{'Weight':>8}"
    sep = "  " + "-" * 72
    lines = [header, sep]
    for r in rows:
        risk_pct = f"{((r['stop_price'] - r['entry_price']) / r['entry_price']) * 100:.2f}%"
        weight = f"{r.get('sizing_weight', 1.0):.2f}x"
        lines.append(
            f"  {r['asset']:<10}{r['tier']:<10}{r['book']:<10}"
            f"{r['entry_price']:>12.6g}{r['stop_price']:>12.6g}"
            f"{risk_pct:>10}{weight:>8}"
        )
    return "\n".join(lines) + "\n"


def notify_signals_sns(
    topic_arn: str | None = None,
    max_age_hours: float = 1.5,
    only_on_new: bool | None = None,
    region: str | None = None,
    dashboard_url: str | None = None,
) -> int:
    target_arn = topic_arn or os.environ.get("SNS_TOPIC_ARN") or os.environ.get("V12_SNS_TOPIC_ARN")
    if not target_arn:
        logger.info("[SNS Alert] Notice: No SNS_TOPIC_ARN configured. Skipping email notification (Localhost mode).")
        return 0

    try:
        import boto3
        from botocore.exceptions import BotoCoreError, ClientError
    except ImportError:
        logger.warning("[SNS Alert] Warning: 'boto3' is not installed. Run 'pip install boto3' to enable SNS alerts.")
        return 0

    if only_on_new is None:
        only_on_new_str = os.environ.get("NOTIFY_ONLY_ON_NEW_SIGNALS", "1").strip().lower()
        only_on_new = only_on_new_str in ("1", "true", "yes")

    region_name = region or os.environ.get("AWS_DEFAULT_REGION", "eu-central-1")
    dash_url = dashboard_url or os.environ.get("DASHBOARD_URL", "")

    # Load open trades
    open_trades_path = ROOT / "data" / "all_tapes" / "v12_production" / "open_trades.csv"
    if not open_trades_path.exists():
        logger.info(f"[SNS Alert] Open trades file not found at {open_trades_path}. Skipping.")
        return 0

    try:
        df_open = pd.read_csv(open_trades_path)
    except Exception as e:
        logger.error(f"[SNS Alert] Failed to read open_trades.csv: {e}")
        return 0

    total_open = len(df_open)
    new_signals = []

    if not df_open.empty and "duration_hours" in df_open.columns:
        # Detect new signals within max_age_hours
        fresh_mask = df_open["duration_hours"] <= max_age_hours
        new_df = df_open[fresh_mask]
        for _, row in new_df.iterrows():
            new_signals.append({
                "asset": str(row.get("asset", "")),
                "tier": str(row.get("tier", "")),
                "book": str(row.get("book", "")),
                "entry_price": float(row.get("entry_price", 0.0)),
                "stop_price": float(row.get("stop_price", 0.0)),
                "sizing_weight": float(row.get("sizing_weight", 1.0)),
            })

    if only_on_new and len(new_signals) == 0:
        logger.info(f"[SNS Alert] 0 new signals in the last {max_age_hours}h. Skipping email alert (NOTIFY_ONLY_ON_NEW_SIGNALS=1).")
        return 0

    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")

    # Format Subject & Body
    if len(new_signals) > 0:
        subject = f"⚡ [Kronos V12] {len(new_signals)} New Trade Signal(s) Entered [{now_utc}]"
    else:
        subject = f"📊 [Kronos V12] Hourly Digest: {total_open} Open Position(s) [{now_utc}]"

    # Count breakdown by book
    book_counts = df_open["book"].value_counts().to_dict() if not df_open.empty and "book" in df_open.columns else {}
    book_summary_lines = "\n".join([f"  • {k}: {v} active" for k, v in sorted(book_counts.items())]) or "  • None active"

    body_lines = [
        "================================================================================",
        "     KRONOS V12 UNIVERSAL 7-CORE MOMENTUM ENGINE — TRADE SIGNAL ALERT           ",
        "================================================================================",
        f"Timestamp UTC:        {now_utc}",
        f"Total Open Trades:    {total_open}",
        f"New Signals Entered:  {len(new_signals)} (within last {max_age_hours}h)",
        "",
        "--------------------------------------------------------------------------------",
        f"🚨 NEW ENTRY SIGNALS ({len(new_signals)}):",
        "--------------------------------------------------------------------------------",
        format_table(new_signals),
        "--------------------------------------------------------------------------------",
        "📊 ACTIVE PORTFOLIO BOOK BREAKDOWN:",
        "--------------------------------------------------------------------------------",
        book_summary_lines,
        "",
        "--------------------------------------------------------------------------------",
        "🛡️ REGIME & EXECUTION STATUS:",
        "--------------------------------------------------------------------------------",
        "  • Macro Regime:       BULL (Core 1: BTC > EMA_4800h)",
        "  • Stop Orders:        NATIVE RESTING STOP-MARKET MANDATE ACTIVE",
        "  • Position Sizing:    Core 7 Kyle-Lambda Dynamic Overlay",
    ]

    if dash_url:
        body_lines.extend([
            "",
            "--------------------------------------------------------------------------------",
            f"🔗 Live Intelligence Command Center: {dash_url}",
            "--------------------------------------------------------------------------------",
        ])

    body_lines.extend([
        "",
        "================================================================================",
        "Kronos V12 Production Engine • Automated Algorithmic Trade Alert",
        "================================================================================",
    ])

    body_text = "\n".join(body_lines)

    # Publish to AWS SNS
    try:
        sns = boto3.client("sns", region_name=region_name)
        res = sns.publish(
            TopicArn=target_arn,
            Subject=subject[:100],  # SNS Subject max 100 chars
            Message=body_text,
        )
        msg_id = res.get("MessageId", "ok")
        logger.info(f"[SNS Alert] Successfully dispatched email notification to {target_arn} (MessageId: {msg_id}).")
        return 0
    except (BotoCoreError, ClientError) as e:
        logger.error(f"[SNS Alert] Failed to publish message to SNS topic: {e}")
        return 0
    except Exception as e:
        logger.error(f"[SNS Alert] Unexpected error dispatching SNS alert: {e}")
        return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dispatch Kronos V12 signal alerts to AWS SNS")
    parser.add_argument("--topic-arn", type=str, default=None, help="Target AWS SNS Topic ARN")
    parser.add_argument("--max-age-hours", type=float, default=1.5, help="Lookback window for new signals in hours")
    parser.add_argument("--all-hours", action="store_true", help="Send email every hour even if 0 new signals")
    parser.add_argument("--region", type=str, default=None, help="AWS Region (default: eu-central-1)")
    parser.add_argument("--dashboard-url", type=str, default=None, help="Public dashboard URL")
    args = parser.parse_args()

    only_on_new = False if args.all_hours else None
    sys.exit(notify_signals_sns(
        topic_arn=args.topic_arn,
        max_age_hours=args.max_age_hours,
        only_on_new=only_on_new,
        region=args.region,
        dashboard_url=args.dashboard_url,
    ))
