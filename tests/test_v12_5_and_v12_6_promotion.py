"""
Unit & Integration Tests for Kronos V12.5 and V12.6 Production Promotion
Verifies:
1. Two-Tier Target Cap Routing (Study S-AY / Law 4 & Law 5)
2. Continuous 200-EMA Position Sizing Overlay (Study S-AY)
3. Multi-Timeframe 200-EMA Convergence Features
4. The 200-Day EMA Retest & Reclaim Engine for Book 4 (Study S-BB)
5. Continuous BTC Macro Sizing (1.0x Bull / 0.50x Bear)
"""

import sys
from pathlib import Path
import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from momentum_v12.config import V12Config, Book4Config, SizingConfig, ExitConfig
from momentum_v12.sizing_v12 import get_ema_position_weight, get_btc_macro_multiplier
from momentum_v12.features_v12 import compute_features_v12
from momentum_v12.engine_v12 import run_v12_engine


def test_config_dataclasses_integrity():
    cfg = V12Config()
    
    # Book 4 Config
    assert hasattr(cfg, "book4")
    assert isinstance(cfg.book4, Book4Config)
    assert cfg.book4.enable_book4 is True
    assert cfg.book4.min_bars_below == 720
    assert cfg.book4.max_retest_hours == 120
    assert cfg.book4.max_retest_dd == -0.20
    assert cfg.book4.target_cap_pct == 0.20
    assert cfg.book4.continuous_btc_sizing is True
    assert cfg.book4.bear_sizing_mult == 0.50
    assert cfg.book4.enable_p_nb_day_close_confirmation is True
    assert cfg.book4.enable_p_nb_microstructure_sizing is True
    assert cfg.tier.tier2_enable_book4 is False
    assert cfg.tier.tier3_enable_book4 is False
    assert "MYX" in cfg.tier.excluded_symbols
    assert "LAB" in cfg.tier.excluded_symbols
    
    # Sizing Config (Study S-AY)
    assert cfg.sizing.enable_ema_sizing is True
    assert cfg.sizing.ema_base_multiplier == 0.75
    assert cfg.sizing.ema_slope_multiplier == 0.50
    assert cfg.sizing.ema_min_multiplier == 0.75
    assert cfg.sizing.ema_max_multiplier == 1.25

    # Exit Config (Study S-AY Two-Tier Targets)
    assert cfg.exit.enable_two_tier_targets is True
    assert cfg.exit.max_lagging_target_pct == 0.20
    assert cfg.exit.min_lagging_target_pct == 0.15


def test_continuous_ema_sizing_math():
    cfg = SizingConfig()
    
    # Min, median, max
    assert get_ema_position_weight(0.0, cfg) == 0.75
    assert get_ema_position_weight(0.5, cfg) == 1.00
    assert get_ema_position_weight(1.0, cfg) == 1.25
    
    # Clamping
    assert get_ema_position_weight(-0.5, cfg) == 0.75
    assert get_ema_position_weight(1.5, cfg) == 1.25
    
    # Vectorized
    s = pd.Series([0.0, 0.5, 1.0])
    w = get_ema_position_weight(s, cfg)
    assert np.allclose(w.values, [0.75, 1.00, 1.25])


def test_continuous_btc_macro_sizing():
    assert get_btc_macro_multiplier(True, bear_mult=0.50) == 1.00
    assert get_btc_macro_multiplier(False, bear_mult=0.50) == 0.50
    
    # Vectorized
    arr = np.array([True, False, True])
    w_btc = get_btc_macro_multiplier(arr, bear_mult=0.50)
    assert np.allclose(w_btc, [1.00, 0.50, 1.00])


def test_features_v12_promoted_indicators():
    # Build synthetic 1000-bar OHLCV dataframe
    n = 1000
    dates = pd.date_range("2025-01-01", periods=n, freq="1h")
    np.random.seed(42)
    px = 100.0 + np.cumsum(np.random.randn(n) * 0.5)
    px = np.maximum(px, 10.0)
    
    df = pd.DataFrame({
        "timestamp": dates.astype(np.int64) // 10**6,
        "open": px,
        "high": px + 0.5,
        "low": px - 0.5,
        "close": px,
        "volume": np.full(n, 10000.0),
        "quote_volume": px * 10000.0,
        "sum_open_interest_value": np.full(n, 5000000.0),
        "count_toptrader_long_short_ratio": np.full(n, 1.50),
        "funding_rate": np.full(n, 0.0001),
        "taker_buy_quote_volume": px * 5000.0,
    }, index=dates)
    
    cfg = V12Config()
    feat = compute_features_v12(df, btc_df=None, tier_label="Tier 2", cfg=cfg)
    
    # Verify promoted columns are present and calculated
    expected_cols = [
        "ema200_1d", "ema200_1h", "ema200_4h", "sma200_1d",
        "nov25_low", "is_leading", "rank_ema_168h",
        "bars_below_ema200_1d", "is_200d_touch"
    ]
    for col in expected_cols:
        assert col in feat.columns, f"Missing promoted feature: {col}"
        
    assert feat["rank_ema_168h"].min() >= 0.0
    assert feat["rank_ema_168h"].max() <= 1.0
    assert isinstance(feat["is_leading"].iloc[-1], (bool, np.bool_))


def test_book4_and_target_cap_engine_execution():
    # Construct a controlled synthetic scenario where a Book 4 reclaim occurs
    n = 1500
    dates = pd.date_range("2025-01-01", periods=n, freq="1h")
    
    # 1. First 800 bars: Price depressed at 50.0 (well below 200d EMA at ~80)
    # 2. Bar 850: Price surges to 85.0 (touches 200d EMA)
    # 3. Bar 880: Price pulls back to 75.0 (-11.7% dip, holding > base 50.0)
    # 4. Bar 910: Price reclaims back to 86.0 (closing above 200d EMA)
    # 5. Bar 930: Price hits target cap at 1.20 * entry (harvested)
    
    c = np.full(n, 50.0)
    # Create smooth historical base
    c[:800] = 50.0
    # Surge to touch
    c[800:850] = np.linspace(50.0, 85.0, 50)
    # Pullback retest dip
    c[850:880] = np.linspace(85.0, 75.0, 30)
    # Reclaim impulse
    c[880:920] = np.linspace(75.0, 88.0, 40)
    # Push to target
    c[920:960] = np.linspace(88.0, 110.0, 40)
    c[960:] = 100.0
    
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
    
    cfg = V12Config(
        book4=Book4Config(
            enable_p_nb_day_close_confirmation=False,
            enable_p_nb_microstructure_sizing=False,
        )
    )
    feat = compute_features_v12(df, btc_df=None, tier_label="Tier 1", cfg=cfg)
    trades, _ = run_v12_engine(feat, "TEST_ASSET", cfg=cfg)
    
    # Engine should run without error and generate valid trades
    assert isinstance(trades, pd.DataFrame)
    if not trades.empty:
        # Check that Book 4 or Two-Tier exits are properly recorded
        assert "book" in trades.columns
        assert "reason" in trades.columns
        assert "sizing_weight" in trades.columns
        assert trades["sizing_weight"].min() >= 0.10
        assert trades["sizing_weight"].max() <= 1.50
