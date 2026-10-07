"""
backup_to_s3.py — Offsite Ledger & State Backup to AWS S3
Automatically synchronizes canonical trades, scorecards, sync state, and tear sheets
to an S3 bucket after every pipeline execution.

Graceful fallback: If no S3_BUCKET environment variable or credentials exist,
it gracefully logs a localhost notice and exits with code 0.
"""

import os
import sys
import argparse
from pathlib import Path
from datetime import datetime, timezone
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')
logger = logging.getLogger("kronos.s3_backup")

ROOT = Path(__file__).resolve().parent.parent

def backup_to_s3(bucket_name: str | None = None, prefix: str = "v12_production", include_shards: bool = False):
    bucket = bucket_name or os.environ.get("S3_BUCKET")
    if not bucket:
        logger.info("[S3 Backup] Notice: No S3_BUCKET configured. Skipping offsite backup (Localhost mode).")
        return 0

    try:
        import boto3
        from botocore.exceptions import BotoCoreError, ClientError
    except ImportError:
        logger.warning("[S3 Backup] Warning: 'boto3' is not installed. Run 'pip install boto3' to enable S3 backups.")
        return 0

    s3 = boto3.client("s3")
    now_str = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%SZ")

    # Critical ledger & state files to preserve
    files_to_sync = [
        ROOT / "data" / "all_tapes" / "v12_production" / "trades.parquet",
        ROOT / "data" / "all_tapes" / "v12_production" / "scorecard.parquet",
        ROOT / "data" / "all_tapes" / "v12_production" / "closed_trades.csv",
        ROOT / "data" / "all_tapes" / "v12_production" / "open_trades.csv",
        ROOT / "config" / "ingestion" / "sync_state.json",
        ROOT / "data" / "sync_state.json",
        ROOT / "v12_tear_tape.md",
        ROOT / "v12_open_trades.md",
    ]

    uploaded = 0
    for file_path in files_to_sync:
        if not file_path.exists():
            continue

        file_name = file_path.name
        # 1. Upload to latest pointer
        latest_key = f"{prefix}/latest/{file_name}"
        # 2. Upload to immutable historical snapshot
        snapshot_key = f"{prefix}/snapshots/{now_str}/{file_name}"

        try:
            s3.upload_file(str(file_path), bucket, latest_key)
            s3.upload_file(str(file_path), bucket, snapshot_key)
            uploaded += 1
            logger.info(f"Uploaded {file_name} -> s3://{bucket}/{latest_key}")
        except (BotoCoreError, ClientError) as e:
            logger.error(f"Failed to upload {file_name} to S3: {e}")

    # Optional: Full Shard Mirror (raw_shards and exotic_shards)
    if include_shards:
        from concurrent.futures import ThreadPoolExecutor, as_completed
        logger.info(f"[S3 Backup] Initiating full shard mirror to s3://{bucket}/{prefix}/data/...")
        shard_files = []
        for d in ["raw_shards", "exotic_shards"]:
            s_dir = ROOT / "data" / d
            if s_dir.exists():
                for p in s_dir.glob("*.parquet"):
                    rel = f"data/{d}/{p.name}"
                    s3_k = f"{prefix}/{rel}"
                    shard_files.append((p, s3_k))

        logger.info(f"[S3 Backup] Mirroring {len(shard_files)} shards with 10 parallel upload workers...")
        shards_uploaded = 0
        def _upload_shard(pair):
            p, s3_k = pair
            try:
                s3.upload_file(str(p), bucket, s3_k)
                return True
            except Exception as e:
                logger.error(f"Failed to upload shard {p.name}: {e}")
                return False

        with ThreadPoolExecutor(max_workers=10) as pool:
            futures = [pool.submit(_upload_shard, item) for item in shard_files]
            for fut in as_completed(futures):
                if fut.result():
                    shards_uploaded += 1

        logger.info(f"[S3 Backup] Shard mirror complete: {shards_uploaded}/{len(shard_files)} shards uploaded.")

    logger.info(f"[S3 Backup] Complete: {uploaded} ledger/state files backed up to s3://{bucket}/{prefix}/.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Backup Kronos V12 state to S3")
    parser.add_argument("--bucket", type=str, default=None, help="Target S3 bucket name")
    parser.add_argument("--prefix", type=str, default="v12_production", help="S3 key prefix")
    parser.add_argument("--include-shards", action="store_true", help="Also mirror all raw & exotic shards to S3")
    args = parser.parse_args()
    sys.exit(backup_to_s3(args.bucket, args.prefix, args.include_shards))
