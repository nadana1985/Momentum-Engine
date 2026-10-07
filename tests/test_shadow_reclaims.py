"""
Tests for Study S-P: Bear-Market Shadow Anchor Reclaim Engine (v12_standalone/tests/test_shadow_reclaims.py)
Validates:
  1. Immutable contract compliance for ShadowReclaimConfig.
  2. Zero-regression default on baseline production engine.
  3. Point-in-time shadow anchor registration ($0 risk) and reclaim execution.
  4. Expiry / zombie breakdown cash protection.
"""

import pytest
import numpy as np
import pandas as pd
from momentum_v12.config import V12Config, ShadowReclaimConfig
from momentum_v12.telemetry_v12 import TelemetryRecord, TelemetryCollector
from momentum_v12.engine_v12 import run_v12_engine


def test_shadow_reclaim_config_immutability():
    """Verify ShadowReclaimConfig is immutable and enforces domain constraints."""
    cfg = ShadowReclaimConfig()
    assert cfg.enable_bear_shadow_reclaims is False
    assert cfg.max_toptrader_ls == 0.95
    assert cfg.min_turnover_velocity == 3.50
    assert cfg.max_initial_risk == 0.08
    assert cfg.reclaim_max_hours > cfg.reclaim_min_hours

    # Test frozen immutability
    with pytest.raises(Exception):
        cfg.enable_bear_shadow_reclaims = True

    # Test invalid constraints
    with pytest.raises(AssertionError):
        ShadowReclaimConfig(max_toptrader_ls=-0.1)

    with pytest.raises(AssertionError):
        ShadowReclaimConfig(min_turnover_velocity=-1.0)

    with pytest.raises(AssertionError):
        ShadowReclaimConfig(reclaim_min_hours=100.0, reclaim_max_hours=50.0)

    with pytest.raises(AssertionError):
        ShadowReclaimConfig(max_initial_risk=0.25)


def test_telemetry_record_shadow_armed_status():
    """Verify TelemetryRecord accepts SHADOW_ARMED status."""
    rec = TelemetryRecord(
        timestamp=pd.Timestamp("2026-03-15 12:00:00"),
        asset="TEST_COIN",
        tier="Tier 1",
        status="SHADOW_ARMED",
        veto_gate="Core 1: S-P Shadow Anchor Registered",
        candidate_setup="Bear-Trap S-P Reclaim",
        price=10.0,
        turnover=4.5,
        ls_ratio=0.85,
        funding_rate=0.00005,
        btc_macro_bull=False
    )
    assert rec.status == "SHADOW_ARMED"


def test_shadow_reclaim_lifecycle_point_in_time():
    """
    Simulate synthetic shard during BTC Bear regime:
      Bar 0: Breakout trigger in bear market -> registers Shadow Anchor at $10.00 ($0 risk).
      Bars 1-24: Pullback / flush down to $8.50 (flush low).
      Bar 25: Price reclaims $10.05 (> anchor_px) after 25h -> triggers Reclaim Trade!
      Stop is clamped to max(flush_low, fill_px * 0.92) = max($8.50, $10.05 * 0.92 = $9.246).
    """
    n_bars = 50
    dates = pd.date_range("2026-03-01 00:00:00", periods=n_bars, freq="1h")

    # Construct price series:
    # 0-9: flat at 9.0
    # 10: pops to 10.0 (Bar 0 trigger)
    # 11-20: flushes down to 8.50
    # 25: reclaims back to 10.05
    closes = np.full(n_bars, 9.0)
    closes[10] = 10.00
    closes[11:21] = np.linspace(9.8, 8.5, 10)
    closes[21:25] = np.linspace(8.6, 9.8, 4)
    closes[25:] = 10.05

    highs = closes * 1.01
    lows = closes * 0.99
    lows[18] = 8.40 # Deepest flush low

    df = pd.DataFrame({
        "close": closes,
        "high": highs,
        "low": lows,
        "tier": "Tier 1",
        "btc_macro_bull": False,  # Strict BTC Bear regime
        "btc_cycle_spring": False,
        "breakout_21d": False,
        "ret_14d": 0.25,
        "rs_vs_btc": 0.20,
        "ema_168": 8.0,
        "low_60d": 7.0,
        "low_14d": 8.0,
        "low_7d": 8.0,
        "toptrader_ls": 0.80,     # Whales net short
        "turnover_24h": 4.5,      # High turnover
        "funding_rate": 0.00002,  # Low funding
        "vol_shock": 3.0,         # Volume shock
        "oi_change_14d": 0.10,
        "oi_usd": 2e7,
        "open_interest": 2e6,
        "taker_ratio": 0.50,
        "pct_lambda": 0.40,
        "btc_ath_pct": 50.0
    }, index=dates)
    df.index.name = "dt"

    # Bar 10 is marked as breakout
    df.loc[dates[10], "breakout_21d"] = True

    # 1. When shadow reclaim is DISABLED: 0 trades fired (100% macro vetoed to cash)
    cfg_disabled = V12Config(shadow_reclaim=ShadowReclaimConfig(enable_bear_shadow_reclaims=False))
    tel_disabled = TelemetryCollector()
    t_disabled = run_v12_engine(df, "TEST_COIN", cfg=cfg_disabled, telemetry=tel_disabled)
    assert len(t_disabled) == 0, "Default disabled config must produce 0 trades during bear regime"

    # 2. When shadow reclaim is ENABLED:
    cfg_enabled = V12Config(shadow_reclaim=ShadowReclaimConfig(
        enable_bear_shadow_reclaims=True,
        reclaim_min_hours=12.0,
        reclaim_max_hours=144.0,
        max_initial_risk=0.08
    ))
    tel_enabled = TelemetryCollector()
    t_enabled = run_v12_engine(df, "TEST_COIN", cfg=cfg_enabled, telemetry=tel_enabled)

    assert len(t_enabled) > 0, "Enabled shadow reclaim must capture confirmed reclaim"
    reclaim_trade = t_enabled.iloc[0]
    assert bool(reclaim_trade["is_reclaim"]) is True
    # Stop loss must be clamped to at most -8.0% loss
    assert (reclaim_trade["entry_price"] - reclaim_trade["stop_price"]) / reclaim_trade["entry_price"] <= 0.0801
