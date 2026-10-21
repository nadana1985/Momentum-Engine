"""
Production tape path and canonical-MTM fail-closed helpers (Momentum V15).

Default ledger is data/all_tapes/v15_0_production. A live hour must not
MTM-open data/canonical/canonical_*. Cold engine replay is
KRONOS_FULL_REBUILD=1 (or profile fresh/full_rebuild/rebuild/scratch).
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

DEFAULT_TAPE_SLUG = "v15_0_production"
DEFAULT_TAPE_DIR = f"data/all_tapes/{DEFAULT_TAPE_SLUG}"

CANONICAL_TAPE_NAMES = (
    "canonical_v15_0_tape.parquet",
    "canonical_v14_tape.parquet",
    "canonical_v13_3_tape.parquet",
    "canonical_v13_2_tape.parquet",
    "canonical_v13_tape.parquet",
)

LIVE_MTM_PROFILES = frozenset({
    "production",
    "v15_production",
    "v15_0_production",
    "v14",
    "v13_production",
    "v13",
    "v13_cached",
    "cached",
    "v14_cached",
})

REBUILD_PROFILES = frozenset({"fresh", "full_rebuild", "rebuild", "scratch"})

PROFILE_TAPE_MAP = {
    "v15_0_production": DEFAULT_TAPE_DIR,
    "v15_production": DEFAULT_TAPE_DIR,
    "production": DEFAULT_TAPE_DIR,
    "fresh": DEFAULT_TAPE_DIR,
    "v14": "data/all_tapes/v14_production",
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
    if raw.is_absolute():
        return raw
    # Check v15_standalone directory if tape lives there
    v15_cand = Path(root) / "v15_standalone" / raw
    if v15_cand.exists():
        return v15_cand
    return Path(root) / raw


def resolve_telemetry_dir(root: Path, tape_dir: Path) -> Path:
    slug = tape_dir.name
    base = Path(root)
    if "v15_standalone" in str(tape_dir):
        base = Path(root) / "v15_standalone"
    if slug in ("v15_0_production", "v15_production", "v13_production", "v12_production"):
        return base / "telemetry"
    return base / "telemetry" / slug


def find_canonical_tape(root: Path) -> Optional[Path]:
    for cand in [Path(root) / "data" / "canonical", Path(root) / "v15_standalone" / "data" / "canonical"]:
        for name in CANONICAL_TAPE_NAMES:
            p = cand / name
            if p.exists():
                return p
    return None


find_canonical_v13 = find_canonical_tape


def refuse_canonical_mtm_on_live_hour(
    root: Path,
    profile: Optional[str] = None,
    full_rebuild: Optional[bool] = None,
) -> None:
    """Raise SystemExit if a live hour would MTM-open a canonical tape."""
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
    hit = find_canonical_tape(root)
    if hit is None:
        return
    raise SystemExit(
        f"Refusing to MTM-open {hit.name} on a live hour. "
        "Cold engine replay only: KRONOS_FULL_REBUILD=1. "
        "Do not copy canonical_* into a production tape."
    )
