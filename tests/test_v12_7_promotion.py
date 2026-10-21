"""
Unit & Integration Tests for Kronos V12.7 Production Promotion
Verifies:
1. Book 2 Sub-200d EMA Specialization Gate (Study S-BC)
2. Unified Compensatory Squeeze & Momentum Index (CSMI) Sizing Overlay (Study S-BD)
3. Anti-Chop Defensive Firewall (Study S-BD)
4. Config Invariants & Default Parameters for V12.7
5. End-to-End Engine Integration with CSMI Sizing
"""

import dataclasses
import sys
from pathlib import Path
import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from momentum_v15.config import V12Config, MicrostructureConfig, SizingConfig, TierConfig, EntryConfig
from momentum_v15.sizing_v12 import compute_csmi_metrics
from momentum_v15.engine_v12 import run_v12_engine
from momentum_v15.telemetry_v12 import TelemetryCollector


def test_v12_7_config_invariants():
    """Verify V12.7 configuration fields and their empirical default values."""
    cfg = V12Config()
    
    # Study S-BC & S-BD Microstructure settings
    assert hasattr(cfg.micro, "book2_sub_200d_only")
    assert cfg.micro.book2_sub_200d_only is True
    assert hasattr(cfg.micro, "enable_csmi_anti_chop")
    assert cfg.micro.enable_csmi_anti_chop is True
    assert hasattr(cfg.micro, "csmi_anti_chop_threshold")
    assert cfg.micro.csmi_anti_chop_threshold == -1.25

    # Study S-BD CSMI Sizing settings
    assert hasattr(cfg.sizing, "enable_csmi_sizing")
    assert cfg.sizing.enable_csmi_sizing is True
    assert cfg.sizing.csmi_base_weight == 0.50
    assert cfg.sizing.csmi_slope_weight == 1.00
    assert cfg.sizing.csmi_min_weight == 0.50
    assert cfg.sizing.csmi_max_weight == 1.45


def test_csmi_mathematical_bounds_and_symmetry():
    """Verify CSMI mathematical properties: neutral baseline, bounds, and directional sensitivity."""
    cfg = SizingConfig()

    # 1. Neutral inputs must yield S = 0.0, prob = 0.50, and exactly 1.00x sizing weight
    s_b2, prob_b2, w_b2 = compute_csmi_metrics(
        book='Book 2', rank_ts=0.50, pct_lam=0.50, dist_ema=0.0, config=cfg
    )
    assert np.isclose(s_b2, 0.0, atol=1e-6)
    assert np.isclose(prob_b2, 0.50, atol=1e-6)
    assert np.isclose(w_b2, 1.00, atol=1e-6)

    s_b1, prob_b1, w_b1 = compute_csmi_metrics(
        book='Book 1', rank_ts=0.50, pct_lam=0.50, dist_ema=0.0, config=cfg
    )
    assert np.isclose(s_b1, 0.0, atol=1e-6)
    assert np.isclose(prob_b1, 0.50, atol=1e-6)
    assert np.isclose(w_b1, 1.00, atol=1e-6)

    # 2. Maximum institutional conviction must scale up toward 1.45x
    # For Book 2: deep sub-200d (dist_ema = -0.30), high whale ticket size (1.0), low slippage impact (0.0)
    s_high, prob_high, w_high = compute_csmi_metrics(
        book='Book 2', rank_ts=1.00, pct_lam=0.00, dist_ema=-0.30, config=cfg
    )
    assert s_high > 0.0
    assert prob_high > 0.50
    assert w_high > 1.00
    assert w_high <= 1.45

    # 3. Severe friction / retail chop must scale down toward 0.50x
    s_low, prob_low, w_low = compute_csmi_metrics(
        book='Book 2', rank_ts=0.00, pct_lam=1.00, dist_ema=0.20, config=cfg
    )
    assert s_low < 0.0
    assert prob_low < 0.50
    assert w_low < 1.00
    assert w_low >= 0.50

    # 4. Asymptotic extreme inputs must clamp cleanly within [0.50, 1.45]
    _, prob_ext, w_ext = compute_csmi_metrics(
        book='Book 1', rank_ts=10.0, pct_lam=-10.0, dist_ema=10.0, config=cfg
    )
    assert prob_ext <= 1.0
    assert np.isclose(w_ext, 1.45, atol=1e-5)

    _, prob_neg, w_neg = compute_csmi_metrics(
        book='Book 1', rank_ts=-10.0, pct_lam=10.0, dist_ema=-10.0, config=cfg
    )
    assert prob_neg >= 0.0
    assert np.isclose(w_neg, 0.50, atol=1e-5)


def test_csmi_vectorized_series():
    """Verify compute_csmi_metrics operates cleanly on pandas Series inputs."""
    cfg = SizingConfig()
    ts_series = pd.Series([0.50, 1.00, 0.00])
    lam_series = pd.Series([0.50, 0.00, 1.00])
    ema_series = pd.Series([0.00, -0.20, 0.20])

    s, prob, w = compute_csmi_metrics('Book 2', ts_series, lam_series, ema_series, config=cfg)
    assert isinstance(s, pd.Series)
    assert isinstance(prob, pd.Series)
    assert isinstance(w, pd.Series)
    assert np.isclose(w.iloc[0], 1.00, atol=1e-5)
    assert w.iloc[1] > 1.00
    assert w.iloc[2] < 1.00


def test_book2_sub_200d_gate_veto():
    """
    Verify Book 2 Sub-200d Specialization Gate:
    1. If close >= ema200_1d, setup must be vetoed with 'Core 4: Book 2 Above-200d Squeeze Stall' when enabled.
    2. If close < ema200_1d, setup is accepted.
    3. If book2_sub_200d_only = False, above-200d setup is NOT vetoed.
    """
    n = 200
    dates = pd.date_range("2025-06-01", periods=n, freq="1h")
    
    # Construct base DataFrame satisfying Book 2 pre-conditions
    df = pd.DataFrame(index=dates)
    df['tier'] = 'Tier 2'
    df['open'] = 100.0
    df['high'] = 101.0
    df['low'] = 98.0
    df['close'] = 100.0
    df['volume'] = 50000.0
    df['quote_volume'] = 5000000.0
    df['oi_usd'] = 8000000.0
    df['toptrader_ls'] = 0.70  # Squeeze candidate (L/S < 0.85)
    df['funding_rate'] = 0.0001
    df['btc_macro_bull'] = True
    df['btc_ath_pct'] = 0.50
    df['vol_shock'] = 3.0
    df['turnover_24h'] = 2.0
    df['shelf_range_72h'] = 0.04   # Tight shelf <= 0.25
    df['dist_from_72h_low'] = 0.04 # Unextended <= 0.25
    df['high_72h'] = 99.0          # c (100.0) > high_72h (99.0)
    df['low_72h'] = 98.0
    df['taker_ratio'] = 0.45       # Passive absorption <= 0.52
    df['ret_7d'] = 0.03            # Unextended base <= 0.30
    df['d_oi_usd_24h'] = 0.05
    df['pct_lambda'] = 0.50
    df['rank_ts_168h'] = 0.50
    df['rank_ema_168h'] = 0.50
    df['is_leading'] = True
    df['sma200_1d'] = 100.0
    df['nov25_low'] = 90.0

    # Test Case 1: Above 200d EMA with book2_sub_200d_only = True -> Must be VETOED
    df_above = df.copy()
    df_above['ema200_1d'] = 90.0  # close (100.0) >= ema200_1d (90.0)
    cfg_enabled = V12Config(
        micro=dataclasses.replace(MicrostructureConfig(), book2_sub_200d_only=True),
        tier=dataclasses.replace(TierConfig(), tier3_enable_book2=True),
        entry=dataclasses.replace(EntryConfig(), cooldown_hours=0)
    )
    telemetry_above = TelemetryCollector()
    trades_above = run_v12_engine(df_above, 'TEST_TOKEN', cfg=cfg_enabled, telemetry=telemetry_above)
    
    # Check that it was vetoed with the exact gate name
    veto_records = [r for r in telemetry_above.records if r.status == 'VETOED' and r.veto_gate == 'Core 4: Book 2 Above-200d Squeeze Stall']
    assert len(veto_records) > 0, "Expected Book 2 Above-200d Squeeze Stall veto"
    if not trades_above.empty:
        assert len(trades_above[trades_above['book'] == 'Book 2']) == 0

    # Test Case 2: Sub 200d EMA with book2_sub_200d_only = True -> Allowed
    df_below = df.copy()
    df_below['ema200_1d'] = 110.0  # close (100.0) < ema200_1d (110.0)
    telemetry_below = TelemetryCollector()
    trades_below = run_v12_engine(df_below, 'TEST_TOKEN', cfg=cfg_enabled, telemetry=telemetry_below)
    assert not trades_below.empty
    b2_trades = trades_below[trades_below['book'] == 'Book 2']
    assert len(b2_trades) > 0, "Expected Book 2 trade to execute sub-200d EMA"

    # Test Case 3: Above 200d EMA with book2_sub_200d_only = False -> Not vetoed
    cfg_disabled = V12Config(
        micro=dataclasses.replace(MicrostructureConfig(), book2_sub_200d_only=False),
        tier=dataclasses.replace(TierConfig(), tier3_enable_book2=True),
        entry=dataclasses.replace(EntryConfig(), cooldown_hours=0)
    )
    telemetry_disabled = TelemetryCollector()
    trades_disabled = run_v12_engine(df_above, 'TEST_TOKEN', cfg=cfg_disabled, telemetry=telemetry_disabled)
    veto_records_disabled = [r for r in telemetry_disabled.records if r.veto_gate == 'Core 4: Book 2 Above-200d Squeeze Stall']
    assert len(veto_records_disabled) == 0, "Did not expect stall veto when book2_sub_200d_only is False"


def test_csmi_anti_chop_firewall():
    """
    Verify CSMI Anti-Chop Firewall:
    If S <= -1.25, setup is vetoed with 'Core 4: CSMI Anti-Chop Firewall'.
    """
    n = 200
    dates = pd.date_range("2025-06-01", periods=n, freq="1h")
    
    df = pd.DataFrame(index=dates)
    df['tier'] = 'Tier 2'
    df['open'] = 100.0
    df['high'] = 101.0
    df['low'] = 98.0
    df['close'] = 100.0
    df['volume'] = 50000.0
    df['quote_volume'] = 5000000.0
    df['oi_usd'] = 8000000.0
    df['toptrader_ls'] = 0.70  # Squeeze candidate
    df['funding_rate'] = 0.0001
    df['btc_macro_bull'] = True
    df['btc_ath_pct'] = 0.50
    df['vol_shock'] = 3.0
    df['turnover_24h'] = 2.0
    df['shelf_range_72h'] = 0.04
    df['dist_from_72h_low'] = 0.04
    df['high_72h'] = 99.0
    df['low_72h'] = 98.0
    df['taker_ratio'] = 0.45
    df['ret_7d'] = 0.03
    df['d_oi_usd_24h'] = 0.05
    df['is_leading'] = True
    df['sma200_1d'] = 100.0
    df['nov25_low'] = 90.0

    # Ensure it's sub-200d EMA (100 < 105)
    df['ema200_1d'] = 105.0

    # Set parameters to force S <= -1.25
    # rank_ts = 0.0, pct_lambda = 1.0, dist_ema = 0.0
    df['pct_lambda'] = 1.00
    df['rank_ts_168h'] = 0.00
    df['rank_ema_168h'] = 0.00

    cfg = V12Config(
        micro=dataclasses.replace(
            MicrostructureConfig(),
            book2_sub_200d_only=True,
            enable_csmi_anti_chop=True,
            csmi_anti_chop_threshold=-0.70,
        ),
        tier=dataclasses.replace(TierConfig(), tier3_enable_book2=True),
        entry=dataclasses.replace(EntryConfig(), cooldown_hours=0),
    )
    telemetry = TelemetryCollector()

    trades = run_v12_engine(df, 'CHOP_TOKEN', cfg=cfg, telemetry=telemetry)
    anti_chop_vetoes = [r for r in telemetry.records if r.status == 'VETOED' and r.veto_gate == 'Core 4: CSMI Anti-Chop Firewall']
    assert len(anti_chop_vetoes) > 0, "Expected setup to be vetoed by CSMI Anti-Chop Firewall"
    if not trades.empty:
        assert len(trades[trades['book'] == 'Book 2']) == 0


def test_v12_7_engine_csmi_sizing_weights():
    """Verify that trades executed by engine_v12 have their sizing_weight driven by CSMI."""
    n = 200
    dates = pd.date_range("2025-06-01", periods=n, freq="1h")
    
    df = pd.DataFrame(index=dates)
    df['tier'] = 'Tier 2'
    df['open'] = 100.0
    df['high'] = 101.0
    df['low'] = 98.0
    df['close'] = 100.0
    df['volume'] = 50000.0
    df['quote_volume'] = 5000000.0
    df['oi_usd'] = 8000000.0
    df['toptrader_ls'] = 0.70  # Squeeze candidate
    df['funding_rate'] = 0.0001
    df['btc_macro_bull'] = True
    df['btc_ath_pct'] = 0.50
    df['vol_shock'] = 3.0
    df['turnover_24h'] = 2.0
    df['shelf_range_72h'] = 0.04
    df['dist_from_72h_low'] = 0.04
    df['high_72h'] = 99.0
    df['low_72h'] = 98.0
    df['taker_ratio'] = 0.45
    df['ret_7d'] = 0.03
    df['d_oi_usd_24h'] = 0.05
    df['is_leading'] = True
    df['sma200_1d'] = 100.0
    df['nov25_low'] = 90.0
    df['ema200_1d'] = 110.0  # sub-200d

    # Setup strong institutional sponsorship
    df['pct_lambda'] = 0.20
    df['rank_ts_168h'] = 0.85
    df['rank_ema_168h'] = 0.80

    cfg = V12Config(
        micro=dataclasses.replace(MicrostructureConfig(), book2_sub_200d_only=True),
        tier=dataclasses.replace(TierConfig(), tier3_enable_book2=True),
        entry=dataclasses.replace(EntryConfig(), cooldown_hours=0),
        sizing=dataclasses.replace(SizingConfig(), enable_csmi_sizing=True)
    )

    trades = run_v12_engine(df, 'SIZING_TOKEN', cfg=cfg)
    assert not trades.empty, "Expected executed trades"
    b2_trades = trades[trades['book'] == 'Book 2']
    assert not b2_trades.empty, "Expected executed Book 2 trades"

    # Sizing weight should be strictly above 1.00x given strong institutional conviction
    trade_w = b2_trades.iloc[0]['sizing_weight']
    assert trade_w > 1.00, f"Expected sizing weight > 1.0, got {trade_w}"
    assert trade_w <= 1.45, f"Expected sizing weight <= 1.45, got {trade_w}"

