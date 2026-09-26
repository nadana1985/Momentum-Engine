"""Static dashboard export.

Renders what dashboard_server.py served live (/api/data?mode=..., /api/asset_dna)
into static JSON files next to a copy of dashboard_v10.html, so the same UI can
be hosted from S3 + CloudFront with no server running.

    <DATA_ROOT>/site/index.html
    <DATA_ROOT>/site/robots.txt
    <DATA_ROOT>/site/data/{open,closed,all}.json
    <DATA_ROOT>/site/data/asset_dna.json      {"ASSET": alpha|null, ...}
    <DATA_ROOT>/site/data/meta.json           generated_utc, counts
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
MODES = ("open", "closed", "all")


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
    """Point the two API calls at static files; refresh every 60 s, not 10 s."""
    replacements = [
        ("const res = await fetch(`/api/data?mode=${currentMode}`);",
         "const res = await fetch(`data/${currentMode}.json`, {cache: 'no-cache'});"),
        ("const res = await fetch(`/api/asset_dna?asset=${asset}`);\n                const data = await res.json();",
         "const res = await fetch('data/asset_dna.json', {cache: 'no-cache'});\n"
         "                const dna = await res.json();\n"
         "                const data = {asset: asset, alpha: (asset in dna) ? dna[asset] : null};"),
        ("setInterval(loadData, 10000);", "setInterval(loadData, 60000);"),
        ("<head>", '<head>\n    <meta name="robots" content="noindex, nofollow">'),
    ]
    out = src
    for old, new in replacements:
        if old not in out:
            raise ValueError(f"dashboard_v10.html changed; cannot patch: {old[:60]!r}")
        out = out.replace(old, new, 1)
    return out


def export_site(site_dir: Path | None = None) -> dict:
    from momentum_v10 import dashboard_server as ds

    site = Path(site_dir) if site_dir else SITE_DIR
    data_dir = site / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    ds._DATA_CACHE.update({"open_mtime": 0, "open_df": None, "all_mtime": 0, "all_df": None})

    counts = {}
    for mode in MODES:
        payload = ds.build_api_response(mode)
        counts[mode] = len(payload.get("open_positions", []))
        _dump(data_dir / f"{mode}.json", payload)

    dna = {}
    for p in sorted(SHARD_DIR.glob("*_USDT_1h.parquet")):
        asset = p.name[: -len("_USDT_1h.parquet")]
        if asset.isascii() and asset.replace("_", "").isalnum():
            dna[asset] = ds.calc_point_72(asset)
    _dump(data_dir / "asset_dna.json", dna)

    meta = {"generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
            "counts": counts, "assets_with_dna": sum(v is not None for v in dna.values())}
    _dump(data_dir / "meta.json", meta)
    atomic_write_text(site / "index.html", patched_html(HTML_SRC.read_text(encoding="utf-8")))
    atomic_write_text(site / "robots.txt", "User-agent: *\nDisallow: /\n")
    logger.info(f"[site] exported {counts} + {len(dna)} asset DNA values to {site}")
    return meta


if __name__ == "__main__":
    print(export_site())
