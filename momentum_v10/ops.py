"""Operational side-effects for the hourly job: S3 backup/restore and a
CloudWatch heartbeat.

Environment:
  V10_BACKUP_BUCKET     S3 bucket for backups (unset = backups disabled)
  V10_BACKUP_PREFIX     key prefix, default "v10"
  V10_DATA_BACKUP_HOUR  UTC hour for the once-a-day shard mirror (default 2)
  V10_CW_NAMESPACE      CloudWatch namespace for the heartbeat (unset = off)

Layout in the bucket:
  <prefix>/latest/...              ledger + state, overwritten every hour
  <prefix>/daily/YYYY-MM-DD/...    ledger + state copy at 00 UTC
                                   (expire with a 35-day lifecycle rule)
  <prefix>/data/...                full shard mirror, overwritten daily

Restore on a fresh host:
  python -m momentum_v10.ops restore
"""
from __future__ import annotations

import argparse
import os
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

from momentum_v10.config import DATA_ROOT, TAPE_DIR
from momentum_v10.logger import get_logger

logger = get_logger("system")
DATA_DIR = DATA_ROOT

STATE_FILES = ("engine_state.json", "sync_state.json")
SHARD_DIRS = ("raw_shards", "exotic_shards")


def _region() -> str:
    return os.environ.get("AWS_DEFAULT_REGION") or os.environ.get("AWS_REGION") or "eu-west-2"


def _s3():
    import boto3
    return boto3.client("s3", region_name=_region())


def _bucket_prefix():
    bucket = os.environ.get("V10_BACKUP_BUCKET", "").strip()
    prefix = os.environ.get("V10_BACKUP_PREFIX", "v10").strip().strip("/")
    return bucket, prefix


def ledger_files() -> list[tuple[Path, str]]:
    """(local path, key relative to data/) for state + tape files."""
    out = []
    for name in STATE_FILES:
        p = DATA_DIR / name
        if p.exists():
            out.append((p, name))
    if TAPE_DIR.exists():
        for p in sorted(TAPE_DIR.iterdir()):
            if p.is_file() and not p.name.startswith("."):
                out.append((p, f"all_tapes/v10_production/{p.name}"))
    return out


def shard_files() -> list[tuple[Path, str]]:
    out = []
    for d in SHARD_DIRS:
        base = DATA_DIR / d
        if base.exists():
            for p in sorted(base.glob("*.parquet")):
                out.append((p, f"{d}/{p.name}"))
    return out


def _upload_many(client, bucket: str, items: list[tuple[Path, str]], workers: int = 16) -> int:
    def put(item):
        path, key = item
        client.upload_file(str(path), bucket, key)
        return 1
    with ThreadPoolExecutor(max_workers=workers) as pool:
        return sum(pool.map(put, items))


def backup(now: datetime | None = None, client=None) -> dict:
    """Hourly: ledger/state to latest/. 00 UTC: also daily/<date>/.
    V10_DATA_BACKUP_HOUR: also mirror all shards to data/."""
    bucket, prefix = _bucket_prefix()
    if not bucket:
        logger.info("[backup] V10_BACKUP_BUCKET not set; skipping S3 backup.")
        return {"enabled": False}
    now = now or datetime.now(timezone.utc)
    client = client or _s3()
    ledger = ledger_files()
    result = {"enabled": True, "latest": 0, "daily": 0, "shards": 0}
    result["latest"] = _upload_many(client, bucket, [(p, f"{prefix}/latest/{k}") for p, k in ledger])
    if now.hour == 0:
        day = now.strftime("%Y-%m-%d")
        result["daily"] = _upload_many(client, bucket, [(p, f"{prefix}/daily/{day}/{k}") for p, k in ledger])
    if now.hour == int(os.environ.get("V10_DATA_BACKUP_HOUR", "2")):
        result["shards"] = _upload_many(client, bucket, [(p, f"{prefix}/data/{k}") for p, k in shard_files()])
    logger.info(f"[backup] s3://{bucket}/{prefix}: {result}")
    return result


_SITE_TYPES = {".html": ("text/html; charset=utf-8", "max-age=300"),
               ".json": ("application/json", "max-age=60"),
               ".txt": ("text/plain; charset=utf-8", "max-age=3600")}


def publish_site(client=None) -> dict:
    """Export the static dashboard and upload it to s3://<bucket>/site/.

    CloudFront (./deploy.sh dashboard) serves that prefix. Off when
    V10_SITE_ENABLED=0 or no bucket is configured.
    """
    bucket, _prefix = _bucket_prefix()
    if not bucket or os.environ.get("V10_SITE_ENABLED", "1") == "0":
        return {"enabled": False}
    from momentum_v10.site_export import SITE_DIR, export_site
    meta = export_site()
    client = client or _s3()
    n = 0
    for p in sorted(SITE_DIR.rglob("*")):
        if not p.is_file() or p.name.startswith("."):
            continue
        ctype, cache = _SITE_TYPES.get(p.suffix, ("application/octet-stream", "max-age=60"))
        key = "site/" + p.relative_to(SITE_DIR).as_posix()
        client.upload_file(str(p), bucket, key, ExtraArgs={"ContentType": ctype, "CacheControl": cache})
        n += 1
    logger.info(f"[site] published {n} files to s3://{bucket}/site/")
    return {"enabled": True, "files": n, "generated_utc": meta["generated_utc"]}


def restore(client=None, overwrite: bool = False) -> dict:
    """Pull shard mirror + latest ledger/state into data/. Seeds a new host."""
    bucket, prefix = _bucket_prefix()
    if not bucket:
        raise SystemExit("V10_BACKUP_BUCKET is not set")
    client = client or _s3()
    todo = []
    paginator = client.get_paginator("list_objects_v2")
    for sub in ("data/", "latest/"):
        for page in paginator.paginate(Bucket=bucket, Prefix=f"{prefix}/{sub}"):
            for obj in page.get("Contents", []):
                rel = obj["Key"][len(f"{prefix}/{sub}"):]
                if not rel or rel.endswith("/"):
                    continue
                dest = DATA_DIR / rel
                if dest.exists() and not overwrite:
                    continue
                todo.append((obj["Key"], dest))

    def get(item):
        key, dest = item
        dest.parent.mkdir(parents=True, exist_ok=True)
        tmp = dest.with_name(dest.name + ".part")
        client.download_file(bucket, key, str(tmp))
        os.replace(tmp, dest)
        return 1

    with ThreadPoolExecutor(max_workers=16) as pool:
        n = sum(pool.map(get, todo))
    logger.info(f"[restore] {n} files restored from s3://{bucket}/{prefix}")
    return {"restored": n}


def heartbeat(status: dict, client=None) -> bool:
    """Publish run health to CloudWatch. An alarm on missing HourlyOK data
    catches a dead host, which the per-run email cannot."""
    ns = os.environ.get("V10_CW_NAMESPACE", "").strip()
    if not ns:
        return False
    try:
        if client is None:
            import boto3
            client = boto3.client("cloudwatch", region_name=_region())
        metrics = [
            ("HourlyOK", 1.0 if status.get("ok") else 0.0, "Count"),
            ("OpenTrades", float(status.get("open", 0)), "Count"),
            ("IngestFailed", float(status.get("ingest_failed", 0)), "Count"),
            ("AssetsFailed", float(status.get("assets_failed", 0)), "Count"),
            ("RunSeconds", float(status.get("run_seconds", 0)), "Seconds"),
        ]
        client.put_metric_data(
            Namespace=ns,
            MetricData=[{"MetricName": n, "Value": v, "Unit": u} for n, v, u in metrics],
        )
        return True
    except Exception as e:
        logger.error(f"[heartbeat] CloudWatch put_metric_data failed: {e}")
        return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("action", choices=["backup", "restore", "backup-all", "publish-site"])
    ap.add_argument("--overwrite", action="store_true")
    a = ap.parse_args()
    if a.action == "publish-site":
        print(publish_site())
    elif a.action == "restore":
        print(restore(overwrite=a.overwrite))
    elif a.action == "backup-all":
        bucket, prefix = _bucket_prefix()
        c = _s3()
        n1 = _upload_many(c, bucket, [(p, f"{prefix}/latest/{k}") for p, k in ledger_files()])
        n2 = _upload_many(c, bucket, [(p, f"{prefix}/data/{k}") for p, k in shard_files()])
        print({"latest": n1, "shards": n2})
    else:
        print(backup())


if __name__ == "__main__":
    main()
