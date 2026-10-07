"""
scripts/restore_from_s3.py — 1-Click Disaster Recovery & Fresh Host Seeder
Downloads the latest production trade ledgers, scorecards, sync state,
and optionally raw/exotic shards from AWS S3 onto a blank EC2 host.

Usage:
  python scripts/restore_from_s3.py --bucket my-kronos-bucket
  python scripts/restore_from_s3.py --bucket my-kronos-bucket --include-shards
"""

import os
import sys
import argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger("kronos.restore_s3")

ROOT = Path(__file__).resolve().parent.parent


def restore_from_s3(
    bucket_name: str | None = None,
    prefix: str = "v12_production",
    include_shards: bool = False,
    region: str | None = None,
) -> int:
    bucket = bucket_name or os.environ.get("S3_BUCKET")
    if not bucket:
        logger.error("[S3 Restore] Error: No bucket specified. Set S3_BUCKET env var or pass --bucket.")
        return 1

    try:
        import boto3
        from botocore.exceptions import BotoCoreError, ClientError
    except ImportError:
        logger.error("[S3 Restore] Error: 'boto3' is not installed. Run 'pip install boto3' to enable S3 restore.")
        return 1

    region_name = region or os.environ.get("AWS_DEFAULT_REGION", "eu-central-1")
    s3 = boto3.client("s3", region_name=region_name)

    logger.info(f"==========================================================")
    logger.info(f"   KRONOS V12 1-CLICK DISASTER RECOVERY (AWS S3)          ")
    logger.info(f"   Bucket: s3://{bucket}/{prefix}/ | Region: {region_name} ")
    logger.info(f"==========================================================")

    # 1. Define target mapping for latest ledger and state files
    ledger_dir = ROOT / "data" / "all_tapes" / "v12_production"
    ledger_dir.mkdir(parents=True, exist_ok=True)
    (ROOT / "config" / "ingestion").mkdir(parents=True, exist_ok=True)
    (ROOT / "data").mkdir(parents=True, exist_ok=True)

    files_to_restore = [
        ("trades.parquet", ledger_dir / "trades.parquet"),
        ("scorecard.parquet", ledger_dir / "scorecard.parquet"),
        ("closed_trades.csv", ledger_dir / "closed_trades.csv"),
        ("open_trades.csv", ledger_dir / "open_trades.csv"),
        ("sync_state.json", ROOT / "config" / "ingestion" / "sync_state.json"),
        ("sync_state.json", ROOT / "data" / "sync_state.json"),
        ("v12_tear_tape.md", ROOT / "v12_tear_tape.md"),
        ("v12_open_trades.md", ROOT / "v12_open_trades.md"),
    ]

    restored = 0
    for file_name, dest_path in files_to_restore:
        s3_key = f"{prefix}/latest/{file_name}"
        try:
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            s3.download_file(bucket, s3_key, str(dest_path))
            size = dest_path.stat().st_size
            if size > 0:
                logger.info(f"✓ Restored {file_name} -> {dest_path.relative_to(ROOT)} ({size:,} bytes)")
                restored += 1
            else:
                logger.warning(f"⚠ Warning: Restored file {file_name} is 0 bytes.")
        except ClientError as e:
            err_code = e.response.get("Error", {}).get("Code")
            if err_code == "404" or err_code == "NoSuchKey":
                logger.warning(f"- Key not found in S3 (skipping): s3://{bucket}/{s3_key}")
            else:
                logger.error(f"Failed to restore {file_name}: {e}")
        except Exception as e:
            logger.error(f"Unexpected error restoring {file_name}: {e}")

    # 2. Optional: Restore raw_shards and exotic_shards
    if include_shards:
        logger.info(f"\n[Shard Restore] Scanning S3 for historical shards under s3://{bucket}/{prefix}/data/...")
        paginator = s3.get_paginator("list_objects_v2")
        shard_keys = []
        shard_prefix = f"{prefix}/data/"

        try:
            for page in paginator.paginate(Bucket=bucket, Prefix=shard_prefix):
                for obj in page.get("Contents", []):
                    k = obj["Key"]
                    if k.endswith(".parquet"):
                        shard_keys.append(k)
        except Exception as e:
            logger.error(f"Failed to list shard objects: {e}")

        if not shard_keys:
            # Fallback check under data/
            fallback_prefix = "data/"
            logger.info(f"No shards found under {shard_prefix}. Trying fallback prefix '{fallback_prefix}'...")
            try:
                for page in paginator.paginate(Bucket=bucket, Prefix=fallback_prefix):
                    for obj in page.get("Contents", []):
                        k = obj["Key"]
                        if k.endswith(".parquet"):
                            shard_keys.append(k)
                shard_prefix = fallback_prefix
            except Exception as e:
                logger.error(f"Failed to list fallback shards: {e}")

        if shard_keys:
            logger.info(f"Found {len(shard_keys)} shards to download. Starting 10-worker pool...")
            (ROOT / "data" / "raw_shards").mkdir(parents=True, exist_ok=True)
            (ROOT / "data" / "exotic_shards").mkdir(parents=True, exist_ok=True)

            shards_done = 0

            def _download_shard(k):
                rel_path = k.replace(shard_prefix, "data/")
                dest = ROOT / rel_path
                dest.parent.mkdir(parents=True, exist_ok=True)
                try:
                    s3.download_file(bucket, k, str(dest))
                    return True
                except Exception as ex:
                    logger.error(f"Failed to download {k}: {ex}")
                    return False

            with ThreadPoolExecutor(max_workers=10) as pool:
                futures = [pool.submit(_download_shard, k) for k in shard_keys]
                for fut in as_completed(futures):
                    if fut.result():
                        shards_done += 1
                    if shards_done % 100 == 0:
                        logger.info(f"Shard restore progress: {shards_done}/{len(shard_keys)} downloaded.")

            logger.info(f"✓ Shard download complete: {shards_done}/{len(shard_keys)} shards restored.")
        else:
            logger.warning("[Shard Restore] No .parquet shard files discovered in S3.")

    logger.info("==========================================================")
    logger.info(f"   DISASTER RECOVERY COMPLETE: {restored} STATE FILES RESTORED")
    logger.info("   System is ready for immediate live execution: ./pipeline_v12.sh")
    logger.info("==========================================================")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Restore Kronos V12 state & ledgers from AWS S3")
    parser.add_argument("--bucket", type=str, default=None, help="Source S3 bucket name")
    parser.add_argument("--prefix", type=str, default="v12_production", help="S3 key prefix (default: v12_production)")
    parser.add_argument("--include-shards", action="store_true", help="Also restore all raw and exotic shard parquets")
    parser.add_argument("--region", type=str, default=None, help="AWS Region (default: eu-central-1 or AWS_DEFAULT_REGION)")
    args = parser.parse_args()
    sys.exit(restore_from_s3(args.bucket, args.prefix, args.include_shards, args.region))
