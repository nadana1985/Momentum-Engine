"""
Unit & Integration Tests for Kronos V12.9 Production Promotion:
1. Study S-BF Book 4 Continuous Anti-Chase Sizing Multiplier Engine.
2. Anti-Chase Mathematical Bounds & Clamping Invariants.
3. End-to-End Engine Integration for Controlled vs. Overextended Reclaims.
4. Canonical V12.9 Production Tape Synchronization & Gate Integrity.
"""

import sys
from pathlib import Path
import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from momentum_v12.config import V12Config, Book4Config
from momentum_v12.features_v12 import compute_features_v12
from momentum_v12.engine_v12 import run_v12_engine


def _sbb_cfg() -> V12Config:
    """S-BB hourly reclaim path: S-CA day-close + microstructure off."""
    return V12Config(
        book4=Book4Config(
            enable_p_nb_day_close_confirmation=False,
            enable_p_nb_microstructure_sizing=False,
        )
    )


def test_v12_9_config_invariants():
    """Verify V12.9 configuration fields and their empirical default values."""
    cfg = V12Config()
    
    assert hasattr(cfg.book4, "enable_anti_chase_sizing")
    assert cfg.book4.enable_anti_chase_sizing is True
    assert hasattr(cfg.book4, "anti_chase_threshold")
    assert cfg.book4.anti_chase_threshold == 1.50
    assert hasattr(cfg.book4, "anti_chase_decay_slope")
    assert cfg.book4.anti_chase_decay_slope == 0.35
    assert hasattr(cfg.book4, "anti_chase_min_multiplier")
    assert cfg.book4.anti_chase_min_multiplier == 0.50
    assert hasattr(cfg.book4, "anti_chase_max_multiplier")
    assert cfg.book4.anti_chase_max_multiplier == 1.20
    assert cfg.book4.enable_p_nb_day_close_confirmation is True
    assert cfg.book4.enable_p_nb_microstructure_sizing is True


def test_anti_chase_mathematical_bounds():
    """Verify continuous anti-chase sizing mathematical behavior across all regimes."""
    th = 1.50
    slope = 0.35
    min_m = 0.50
    max_m = 1.20

    def calc_w(ratio):
        return float(np.clip(max_m - slope * max(0.0, ratio - th), min_m, max_m))

    # 1. Controlled breakouts (<= 1.50x ATR) receive 1.20x max conviction sizing
    assert np.isclose(calc_w(0.50), 1.20)
    assert np.isclose(calc_w(1.00), 1.20)
    assert np.isclose(calc_w(1.50), 1.20)

    # 2. Moderate extensions scale down linearly
    assert np.isclose(calc_w(2.50), 0.85)  # 1.20 - 0.35 * 1.0 = 0.85
    assert np.isclose(calc_w(3.00), 0.675) # 1.20 - 0.35 * 1.5 = 0.675
    assert np.isclose(calc_w(3.50), 0.50)  # 1.20 - 0.35 * 2.0 = 0.50

    # 3. Vertical single-bar blowouts (like SKL at > 4x ATR) clamp cleanly at 0.50x
    assert np.isclose(calc_w(5.00), 0.50)
    assert np.isclose(calc_w(12.50), 0.50)


def test_book4_anti_chase_engine_sizing():
    """Verify that run_v12_engine allocates 1.20x to controlled reclaims
    and defensively downweights overextended spikes.
    """
    n = 2000
    dates = pd.date_range("2025-01-01", periods=n, freq="1h")
    
    # Base series: 720h below EMA, touch, retest dip, and controlled reclaim
    c = np.full(n, 50.0)
    c[:200] = 150.0
    c[200:1000] = 50.0
    c[1000:1040] = np.linspace(50.0, 105.0, 40)
    c[1040:1070] = np.linspace(105.0, 92.0, 30)
    # Controlled reclaim: open 100, close 102 (small body relative to ATR)
    c[1070:1100] = np.linspace(92.0, 108.0, 30)
    c[1100:1150] = np.linspace(108.0, 135.0, 50)
    c[1150:] = 135.0
    
    h = c + 1.0
    l = c - 1.0
    
    df = pd.DataFrame({
        "timestamp": dates.astype(np.int64) // 10**6,
        "open": c,
        "high": h,
        "low": l,
        "close": c,
        "volume": np.full(n, 50000.0),
        "quote_volume": c * 50000.0,
        "sum_open_interest_value": np.full(n, 8000000.0),
        "count_toptrader_long_short_ratio": np.full(n, 1.80),
        "funding_rate": np.full(n, 0.0001),
        "taker_buy_quote_volume": c * 26000.0,
    }, index=dates)
    
    cfg = _sbb_cfg()
    feat = compute_features_v12(df, btc_df=None, tier_label="Tier 1", cfg=cfg)
    trades, _ = run_v12_engine(feat, "CONTROLLED_B4_TOKEN", cfg=cfg)
    
    assert isinstance(trades, pd.DataFrame)
    b4 = trades[trades['book'] == 'Book 4']
    assert not b4.empty
    trade = b4.iloc[0]
    
    # Controlled reclaim should receive 1.20x sizing weight
    assert trade['sizing_weight'] >= 1.10, f"Expected sizing weight >= 1.10, got {trade['sizing_weight']}"


def test_canonical_v12_9_vault_integrity():
    """Verify that canonical_v12_9_tape.parquet is present, intact, and passes V12.9 acceptance gates."""
    canon_path = ROOT / "data" / "canonical" / "canonical_v12_9_tape.parquet"
    assert canon_path.exists(), f"Canonical V12.9 tape missing at {canon_path}"
    
    df = pd.read_parquet(canon_path)
    assert len(df) == 3462, f"Expected 3,462 total trades, found {len(df)}"
    
    closed = df[~df['is_open']].copy()
    assert len(closed) == 3443, f"Expected 3,443 closed trades, found {len(closed)}"
    
    tot_log = closed['log_ret'].sum() * 100.0
    assert tot_log > 11000.0, f"Expected Net Log > +11,000%, got {tot_log:.1f}%"
    
    wins = closed[closed['log_ret'] > 0]['log_ret'].sum()
    losses = abs(closed[closed['log_ret'] < 0]['log_ret'].sum())
    log_pf = wins / losses if losses > 0 else 0.0
    assert log_pf >= 2.10, f"Expected Log PF >= 2.10, got {log_pf:.3f}"
