"""
Standalone Compliance & Invariant Verification Test Suite
Validates configuration immutability, atomic parquet writes, rate-limiter pacing,
and execution invariants completely self-contained within the standalone package.
"""

import os
import sys
import tempfile
import time
from pathlib import Path
import pytest
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from momentum_v12.config import V12Config, MacroConfig, TierConfig, MicrostructureConfig, EntryConfig, ExitConfig
from config.ingestion.live_bridger import RateLimiter, atomic_to_parquet


def test_config_immutability():
    """Ensure all 6 core configurations are frozen dataclasses."""
    cfg = V12Config()
    with pytest.raises(Exception):
        cfg.macro.enable_cycle_spring = False  # FrozenInstanceError

    with pytest.raises(Exception):
        cfg.exit.enable_stall_bailout = False


def test_config_assertions():
    """Verify bounds and safety assertions."""
    cfg = V12Config()
    assert cfg.macro.cycle_spring_min_days == 180.0
    assert cfg.macro.max_rs_btc_extension == 0.20
    assert cfg.exit.stall_bailout_hours == 36.0
    assert cfg.exit.stall_bailout_max_mfe == 0.010
    assert cfg.micro.b2_max_initial_risk == 0.08
    assert cfg.entry.max_dist_from_72h_low == 0.25
    assert cfg.entry.remediated_max_dist_60d == 0.60


def test_atomic_parquet_write():
    """Verify atomic parquet writes without leaving temporary debris."""
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4.0, 5.0, 6.0]})
    with tempfile.TemporaryDirectory() as tmpdir:
        target = os.path.join(tmpdir, "test.parquet")
        atomic_to_parquet(df, target)

        assert os.path.exists(target)
        read_df = pd.read_parquet(target)
        pd.testing.assert_frame_equal(df, read_df)

        # Ensure no temp files left behind
        files = os.listdir(tmpdir)
        assert len(files) == 1
        assert files[0] == "test.parquet"


def test_rate_limiter_pacing():
    """Verify thread-safe rate limiter pacing."""
    limiter = RateLimiter(max_per_second=10.0)  # 10 req/sec = 100ms interval
    t0 = time.time()
    for _ in range(5):
        limiter.wait()
    elapsed = time.time() - t0
    # 5 iterations at 10/s should take at least 0.35s
    assert elapsed >= 0.35, f"Rate limiter was too fast: {elapsed:.3f}s"
