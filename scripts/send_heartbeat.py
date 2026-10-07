"""
send_heartbeat.py — Dead-Man's Switch & CloudWatch Liveness Alert
Dispatches a heartbeat signal to an external monitoring endpoint (Healthchecks.io, Cronitor, etc.)
or AWS CloudWatch metrics after every successful hourly pipeline run.

Dead-host protection: If the EC2 host freezes, panics, or terminates, no heartbeat will be sent.
An alarm set for 2 hours of missing heartbeats will trigger an alert (SNS / Email / Telegram).

Graceful fallback: If neither HEARTBEAT_URL nor AWS credentials exist,
it gracefully logs a localhost notice and exits with code 0.
"""

import os
import sys
import argparse
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')
logger = logging.getLogger("kronos.heartbeat")

def send_heartbeat(url: str | None = None, enable_cloudwatch: bool = False):
    heartbeat_url = url or os.environ.get("HEARTBEAT_URL")
    cloudwatch_enabled = enable_cloudwatch or (os.environ.get("ENABLE_CLOUDWATCH_HEARTBEAT", "0") in ("1", "true", "True"))

    sent = False

    # 1. External Dead-Man's Switch (Healthchecks.io / Better Uptime / Cronitor)
    if heartbeat_url:
        try:
            res = requests.get(heartbeat_url, timeout=10)
            if res.status_code in (200, 202):
                logger.info(f"[Heartbeat] Ping dispatched successfully to {heartbeat_url}")
                sent = True
            else:
                logger.warning(f"[Heartbeat] Ping returned HTTP {res.status_code}")
        except Exception as e:
            logger.error(f"[Heartbeat] Failed to ping {heartbeat_url}: {e}")

    # 2. AWS CloudWatch Custom Metric
    if cloudwatch_enabled:
        try:
            import boto3
            cw = boto3.client("cloudwatch")
            cw.put_metric_data(
                Namespace="KronosV12",
                MetricData=[
                    {
                        "MetricName": "PipelineHeartbeat",
                        "Value": 1.0,
                        "Unit": "Count"
                    }
                ]
            )
            logger.info("[Heartbeat] CloudWatch metric 'PipelineHeartbeat=1' emitted.")
            sent = True
        except Exception as e:
            logger.warning(f"[Heartbeat] CloudWatch emission failed: {e}")

    if not sent:
        logger.info("[Heartbeat] Notice: No HEARTBEAT_URL or CloudWatch configured. Skipping (Localhost mode).")

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send pipeline heartbeat to monitoring service")
    parser.add_argument("--url", type=str, default=None, help="Heartbeat ping URL")
    parser.add_argument("--cloudwatch", action="store_true", help="Emit metric to AWS CloudWatch")
    args = parser.parse_args()
    sys.exit(send_heartbeat(args.url, args.cloudwatch))
