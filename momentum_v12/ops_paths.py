"""
Production tape path and canonical-MTM fail-closed helpers.

Default ledger is data/all_tapes/v14_production. A live hour must not
MTM-open data/canonical/canonical_v13_*. Cold engine replay is
KRONOS_FULL_REBUILD=1 (or profile fresh/full_rebuild/rebuild/scratch).
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

DEFAULT_TAPE_SLUG = "v14_production"
DEFAULT_TAPE_DIR = f"data/all_tapes/{DEFAULT_TAPE_SLUG}"

CANONICAL_V13_NAMES = (
    "canonical_v13_3_tape.parquet",
    "canonical_v13_2_tape.parquet",
    "canonical_v13_tape.parquet",
)

LIVE_MTM_PROFILES = frozenset({
    "production",
    "v14_production",
    "v14",
    "v13_production",
    "v13",
    "v13_cached",
    "cached",
    "v14_cached",
})

REBUILD_PROFILES = frozenset({"fresh", "full_rebuild", "rebuild", "scratch"})

PROFILE_TAPE_MAP = {
    "v14_production": DEFAULT_TAPE_DIR,
    "v14": DEFAULT_TAPE_DIR,
    "production": DEFAULT_TAPE_DIR,
    "fresh": DEFAULT_TAPE_DIR,
    "v13_production": "data/all_tapes/v13_production",
    "v13": "data/all_tapes/v13_production",
    "legacy": "data/all_tapes/v12_legacy_baseline",
    "baseline": "data/all_tapes/v12_legacy_baseline",
    "v12_legacy": "data/all_tapes/v12_legacy_baseline",
    "shadow_reclaim": "data/all_tapes/v12_shadow_reclaim_arm",
    "s_p": "data/all_tapes/v12_shadow_reclaim_arm",
    "shadow": "data/all_tapes/v12_shadow_reclaim_arm",
    "book3_flush": "data/all_tapes/v12_book3_flush_reclaim_arm",
    "flush_reclaim": "data/all_tapes/v12_book3_flush_reclaim_arm",
    "s_ac": "data/all_tapes/v12_book3_flush_reclaim_arm",
    "book3": "data/all_tapes/v12_book3_flush_reclaim_arm",
}


def resolve_tape_dir_env(
    env_tape: Optional[str] = None,
    profile: Optional[str] = None,
) -> str:
    tape = env_tape if env_tape is not None else os.environ.get("KRONOS_TAPE_DIR")
    if tape:
        return tape
    prof = (profile if profile is not None else os.environ.get("KRONOS_PROFILE", "production")).lower()
    if prof in PROFILE_TAPE_MAP:
        return PROFILE_TAPE_MAP[prof]
    if prof in ("engine_baseline", "s_bi", "s_bj", "s_bi_bj"):
        return f"data/all_tapes/retest_{prof}"
    return DEFAULT_TAPE_DIR


def resolve_tape_dir(
    root: Path,
    env_tape: Optional[str] = None,
    profile: Optional[str] = None,
) -> Path:
    raw = Path(resolve_tape_dir_env(env_tape, profile))
    return raw if raw.is_absolute() else Path(root) / raw


def resolve_telemetry_dir(root: Path, tape_dir: Path) -> Path:
    slug = tape_dir.name
    if slug in ("v13_production", "v12_production"):
        return Path(root) / "telemetry"
    return Path(root) / "telemetry" / slug


def find_canonical_v13(root: Path) -> Optional[Path]:
    canon = Path(root) / "data" / "canonical"
    for name in CANONICAL_V13_NAMES:
        p = canon / name
        if p.exists():
            return p
    return None


def refuse_canonical_mtm_on_live_hour(
    root: Path,
    profile: Optional[str] = None,
    full_rebuild: Optional[bool] = None,
) -> None:
    """Raise SystemExit if a live hour would MTM-open a canonical v13 tape."""
    prof = (profile if profile is not None else os.environ.get("KRONOS_PROFILE", "production")).lower()
    if full_rebuild is None:
        full_rebuild = (
            os.environ.get("KRONOS_FULL_REBUILD", "0") == "1"
            or prof in REBUILD_PROFILES
        )
    if full_rebuild:
        return
    if prof not in LIVE_MTM_PROFILES:
        return
    hit = find_canonical_v13(root)
    if hit is None:
        return
    raise SystemExit(
        f"Refusing to MTM-open {hit.name} on a live hour. "
        "Cold engine replay only: KRONOS_FULL_REBUILD=1. "
        "Do not copy canonical_v13_* into a production tape."
    )
