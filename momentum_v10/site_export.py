"""Static dashboard export.

Writes the dashboard's data files next to a copy of dashboard_v10.html so the
same UI can be hosted from S3 + CloudFront with no server running.

    <DATA_ROOT>/site/index.html
    <DATA_ROOT>/site/robots.txt
    <DATA_ROOT>/site/data/trades.json         every open + closed trade (see dashboard_data)
    <DATA_ROOT>/site/data/meta.json           freshness, counts, last hourly status + history
    <DATA_ROOT>/site/data/config.json         engine thresholds
    <DATA_ROOT>/site/data/asset_dna.json      {"ASSET": alpha|null, ...}
"""
from __future__ import annotations

import json
import math
from datetime import datetime, timezone
from pathlib import Path

from momentum_v10.config import DATA_ROOT, SHARD_DIR
from momentum_v10.io_utils import atomic_write_text
from momentum_v10.logger import get_logger

logger = get_logger("system")
SITE_DIR = DATA_ROOT / "site"
HTML_SRC = Path(__file__).parent / "dashboard_v10.html"


def _clean(obj):
    """JSON-safe: NaN/inf -> null, numpy scalars -> python."""
    if isinstance(obj, dict):
        return {str(k): _clean(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_clean(v) for v in obj]
    if hasattr(obj, "item") and not isinstance(obj, (str, bytes)):
        try:
            obj = obj.item()
        except Exception:
            pass
    if isinstance(obj, float) and not math.isfinite(obj):
        return None
    return obj


def _dump(path: Path, obj) -> None:
    atomic_write_text(path, json.dumps(_clean(obj), allow_nan=False, separators=(",", ":")))


def patched_html(src: str) -> str:
    """The page already reads data/*.json; only add a noindex hint for hosting."""
    if "<head>" not in src:
        raise ValueError("dashboard_v10.html has no <head>")
    return src.replace("<head>", '<head>\n    <meta name="robots" content="noindex, nofollow">', 1)


def dna_map() -> dict:
    from momentum_v10 import dashboard_server as ds
    dna = {}
    for p in sorted(SHARD_DIR.glob("*_USDT_1h.parquet")):
        asset = p.name[: -len("_USDT_1h.parquet")]
        if asset.isascii() and asset.replace("_", "").isalnum():
            dna[asset] = ds.calc_point_72(asset)
    return dna


def export_site(site_dir: Path | None = None) -> dict:
    from momentum_v10 import dashboard_data as dd

    site = Path(site_dir) if site_dir else SITE_DIR
    data_dir = site / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    trades = dd.build_trades()
    _dump(data_dir / "trades.json", trades)
    meta = dd.build_meta(trades)
    dna = dna_map()
    meta["assets_with_dna"] = sum(v is not None for v in dna.values())
    _dump(data_dir / "meta.json", meta)
    _dump(data_dir / "config.json", dd.build_config())
    _dump(data_dir / "asset_dna.json", dna)
    for old in ("open.json", "closed.json", "all.json"):      # superseded by trades.json
        (data_dir / old).unlink(missing_ok=True)
    atomic_write_text(site / "index.html", patched_html(HTML_SRC.read_text(encoding="utf-8")))
    atomic_write_text(site / "robots.txt", "User-agent: *\nDisallow: /\n")
    logger.info(f"[site] exported {meta['counts']} + {len(dna)} asset DNA values to {site}")
    return {"generated_utc": meta["generated_utc"], "counts": meta["counts"],
            "assets_with_dna": meta["assets_with_dna"]}


if __name__ == "__main__":
    print(export_site())
