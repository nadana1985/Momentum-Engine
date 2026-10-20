"""Ops/tape: v14_production default, extra exclusions, canonical MTM fail-closed."""

import os
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from momentum_v12.config import V12Config
from momentum_v12.ops_paths import (
    DEFAULT_TAPE_DIR,
    DEFAULT_TAPE_SLUG,
    find_canonical_v13,
    refuse_canonical_mtm_on_live_hour,
    resolve_tape_dir_env,
    resolve_telemetry_dir,
)


def test_default_tape_is_v14_production(monkeypatch):
    monkeypatch.delenv("KRONOS_TAPE_DIR", raising=False)
    monkeypatch.delenv("KRONOS_PROFILE", raising=False)
    assert resolve_tape_dir_env() == DEFAULT_TAPE_DIR
    assert DEFAULT_TAPE_SLUG in ("v14_production", "v15_production")
    assert resolve_tape_dir_env(env_tape=None, profile="production") == DEFAULT_TAPE_DIR
    assert resolve_tape_dir_env(env_tape=None, profile="v14") == DEFAULT_TAPE_DIR
    assert (
        resolve_tape_dir_env(env_tape=None, profile="book3_flush")
        == "data/all_tapes/v12_book3_flush_reclaim_arm"
    )
    assert (
        resolve_tape_dir_env(env_tape="data/all_tapes/v13_production")
        == "data/all_tapes/v13_production"
    )


def test_v14_telemetry_is_namespaced(tmp_path):
    tape = tmp_path / "data" / "all_tapes" / "v14_production"
    tel = resolve_telemetry_dir(tmp_path, tape)
    assert tel == tmp_path / "telemetry" / "v14_production"


def test_extra_exclusions_include_lottery_and_levered():
    excluded = set(V12Config().tier.excluded_symbols)
    for sym in ("MYX", "LAB", "CRCL", "HD", "RDDT", "SQQQ", "TMF", "UVXY"):
        assert sym in excluded, f"{sym} must be excluded from the training universe"


def test_refuse_canonical_mtm_on_live_hour(tmp_path, monkeypatch):
    monkeypatch.delenv("KRONOS_FULL_REBUILD", raising=False)
    canon = tmp_path / "data" / "canonical"
    canon.mkdir(parents=True)
    vault = canon / "canonical_v13_3_tape.parquet"
    vault.write_bytes(b"not-a-live-tape")
    assert find_canonical_v13(tmp_path) == vault

    with pytest.raises(SystemExit, match="canonical_v13_3_tape.parquet"):
        refuse_canonical_mtm_on_live_hour(tmp_path, profile="production")

    refuse_canonical_mtm_on_live_hour(tmp_path, profile="production", full_rebuild=True)
    refuse_canonical_mtm_on_live_hour(tmp_path, profile="fresh")
    refuse_canonical_mtm_on_live_hour(tmp_path, profile="book3_flush")


def test_live_hour_without_canonical_vault_is_ok(tmp_path, monkeypatch):
    monkeypatch.delenv("KRONOS_FULL_REBUILD", raising=False)
    (tmp_path / "data" / "canonical").mkdir(parents=True)
    refuse_canonical_mtm_on_live_hour(tmp_path, profile="production")


def test_build_v12_tape_no_longer_mtm_opens_canonical():
    src = (ROOT / "build_v12_tape.py").read_text(encoding="utf-8")
    assert "refuse_canonical_mtm_on_live_hour" in src
    assert "Forward-evaluating active open positions" not in src
    assert "Activating Canonical V13.3 Master Tape" not in src
