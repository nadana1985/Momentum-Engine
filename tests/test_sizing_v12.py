"""
Test Suite: Kyle-Lambda Dynamic Position Sizing Overlay (test_sizing_v12.py)
Validates immutability, mathematical purity, golden snapshot equivalence,
and non-regression invariants for Study S-Q / Section 8 Adoption Bridge.
"""

import os
import sys
from pathlib import Path
import pytest
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from momentum_v12.config import V12Config, SizingConfig
from momentum_v12.sizing_v12 import (
    compute_kyle_lambda_series,
    compute_pit_lambda_percentile,
    get_position_weight,
    apply_sizing_overlay_to_trades,
)


def test_sizing_config_immutability():
    """Verify SizingConfig is strictly frozen."""
    cfg = SizingConfig()
    with pytest.raises(Exception):
        cfg.enable_lambda_sizing = True

    with pytest.raises(Exception):
        cfg.min_weight = 0.10


def test_sizing_config_bounds_assertions():
    """Verify parameter bounds assertions."""
    # min_weight must be positive
    with pytest.raises(AssertionError):
        SizingConfig(min_weight=-0.1)

    # max_weight must be >= min_weight
    with pytest.raises(AssertionError):
        SizingConfig(min_weight=1.5, max_weight=1.0)

    # lookback must be >= 12
    with pytest.raises(AssertionError):
        SizingConfig(lookback_bars=5)

    # history_max must exceed history_min
    with pytest.raises(AssertionError):
        SizingConfig(history_min_bars=5000, history_max_bars=4000)


def test_kyle_lambda_pure_math_golden_snapshot():
    """Golden snapshot verification of Kyle-lambda calculation."""
    np.random.seed(42)
    n = 100
    prices = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0, 0.01, n))))
    volumes = pd.Series(np.random.uniform(1000, 5000, n))
    taker_buy = pd.Series(volumes * np.random.uniform(0.3, 0.7, n))

    lam = compute_kyle_lambda_series(prices, volumes, taker_buy, lookback_bars=24)
    assert len(lam) == n
    assert np.isnan(lam.iloc[0])  # Lookback warmup must be NaN
    assert not np.isnan(lam.iloc[-1])

    # Manual verification at bar 50 using exact trailing window of length 24
    r_series = np.log(prices).diff()
    qv_mean = volumes.rolling(24).mean()
    q_series = (2.0 * taker_buy - volumes) / qv_mean

    r_window = r_series.iloc[27:51]  # 24 observations ending at index 50
    q_window = q_series.iloc[27:51]  # 24 observations ending at index 50

    cov_manual = np.cov(r_window, q_window)[0, 1]
    var_manual = np.var(q_window, ddof=1)
    expected_lam = cov_manual / var_manual

    assert np.isclose(lam.iloc[50], expected_lam, rtol=1e-5)


def test_position_weight_clamping_and_fallbacks():
    """Verify position weights under active and disabled modes."""
    # 1. Disabled mode (Default) -> must always yield exactly 1.0
    disabled_cfg = SizingConfig(enable_lambda_sizing=False)
    assert get_position_weight(0.10, disabled_cfg) == 1.0
    assert get_position_weight(0.90, disabled_cfg) == 1.0
    assert get_position_weight(np.nan, disabled_cfg) == 1.0

    arr = np.array([0.1, 0.5, 0.9, np.nan])
    weights_disabled = get_position_weight(arr, disabled_cfg)
    assert np.all(weights_disabled == 1.0)

    # 2. Active mode
    active_cfg = SizingConfig(enable_lambda_sizing=True, min_weight=0.50, max_weight=1.50)
    # pct = 0.0 -> 1.5
    assert np.isclose(get_position_weight(0.0, active_cfg), 1.50)
    # pct = 0.2 -> 1.3
    assert np.isclose(get_position_weight(0.2, active_cfg), 1.30)
    # pct = 0.5 -> 1.0
    assert np.isclose(get_position_weight(0.5, active_cfg), 1.00)
    # pct = 0.8 -> 0.7
    assert np.isclose(get_position_weight(0.8, active_cfg), 0.70)
    # pct = 1.0 -> 0.5
    assert np.isclose(get_position_weight(1.0, active_cfg), 0.50)

    # Bounds clipping
    assert np.isclose(get_position_weight(-0.5, active_cfg), 1.50)
    assert np.isclose(get_position_weight(1.5, active_cfg), 0.50)

    # NaN fallback to neutral 0.5 -> weight 1.0
    assert np.isclose(get_position_weight(np.nan, active_cfg), 1.00)


def test_v12_config_integration():
    """Verify integration into unified V12Config without breaking existing cores."""
    cfg = V12Config()
    assert hasattr(cfg, "sizing")
    assert cfg.sizing.enable_lambda_sizing is True
    assert cfg.sizing.min_weight == 0.50
    assert cfg.sizing.max_weight == 1.50


def test_apply_sizing_overlay_non_regression():
    """Verify exact non-regression when disabled, and alpha expansion when enabled."""
    sq_path = Path(ROOT).parent / "clean_room" / "S-Q_trade_features.parquet"
    if not sq_path.exists():
        pytest.skip("S-Q_trade_features.parquet not present")

    df = pd.read_parquet(sq_path)
    
    # 1. Disabled (Default) -> weighted_log_ret sum must be identical to unweighted log_ret
    cfg_disabled = SizingConfig(enable_lambda_sizing=False)
    out_disabled = apply_sizing_overlay_to_trades(df, cfg_disabled)
    assert np.all(out_disabled["sizing_weight"] == 1.0)
    assert np.isclose(out_disabled["weighted_log_ret"].sum(), df["log_ret"].sum(), rtol=1e-5)

    # 2. Enabled -> weighted_log_ret sum must match Study S-Q verified total (+18.69 log with fee haircut)
    cfg_enabled = SizingConfig(enable_lambda_sizing=True, fee_haircut_bps=10.0)
    out_enabled = apply_sizing_overlay_to_trades(df, cfg_enabled)
    total_log = out_enabled["weighted_log_ret"].sum()
    assert total_log > df["log_ret"].sum()
    assert np.isclose(total_log, 18.69259, rtol=1e-3)

