"""
Test Suite: Study S-R Microstructure De-Guillotining (test_remediation_v12.py)
Validates immutability, zero-regression backward compatibility,
and opt-in activation of funding squeeze & turnover scaling exceptions.
"""

import sys
from pathlib import Path
import pytest
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from momentum_v12.config import V12Config, MicrostructureConfig, SizingConfig
from momentum_v12.engine_v12 import run_v12_engine
from momentum_v12.telemetry_v12 import TelemetryCollector


def test_micro_config_immutability_and_assertions():
    """Verify S-R flags are frozen and asserted."""
    cfg = MicrostructureConfig()
    with pytest.raises(Exception):
        cfg.enable_funding_sqz_exception = True

    with pytest.raises(AssertionError):
        MicrostructureConfig(funding_sqz_max_ls=-0.1)

    with pytest.raises(AssertionError):
        MicrostructureConfig(funding_sqz_max_ls=2.5)


def test_default_flags_backward_compatibility():
    """Verify default V12Config defaults to Canonical Production (Remediated + S-Q Sizing active)."""
    cfg = V12Config()
    assert cfg.micro.enable_funding_sqz_exception is True
    assert cfg.micro.funding_sqz_max_ls == 0.95
    assert cfg.micro.enable_turnover_scaling is True
    assert cfg.sizing.enable_lambda_sizing is True
    assert cfg.shadow_reclaim.enable_bear_shadow_reclaims is False

    # Verify legacy baseline can be explicitly configured
    legacy_cfg = V12Config(
        micro=MicrostructureConfig(enable_funding_sqz_exception=False, enable_turnover_scaling=False),
        sizing=SizingConfig(enable_lambda_sizing=False)
    )
    assert legacy_cfg.micro.enable_funding_sqz_exception is False
    assert legacy_cfg.micro.enable_turnover_scaling is False
    assert legacy_cfg.sizing.enable_lambda_sizing is False


def _create_mock_breakout_df(fr=0.00010, turnover=2.0, ls_ratio=1.10):
    """Generates synthetic feature dataframe qualifying for breakout."""
    n = 600
    dates = pd.date_range("2024-01-01", periods=n, freq="h")
    base_px = 100.0
    closes = np.full(n, base_px)
    highs = np.full(n, base_px * 1.01)
    lows = np.full(n, base_px * 0.99)
    opens = np.full(n, base_px)

    df = pd.DataFrame({
        "open": opens,
        "high": highs,
        "low": lows,
        "close": closes,
        "volume": np.full(n, 10000.0),
        "quote_volume": np.full(n, 1000000.0),
        "oi_usd": np.full(n, 50000000.0),
        "toptrader_ls": np.full(n, ls_ratio),
        "funding_rate": np.full(n, fr),
        "turnover_24h": np.full(n, turnover),
        "breakout_21d": np.full(n, True),
        "ret_14d": np.full(n, 0.20),
        "rs_vs_btc": np.full(n, 0.15),
        "dist_from_60d_low": np.full(n, 0.20),
        "btc_macro_bull": np.full(n, True),
        "btc_ath_pct": np.full(n, 0.70),
        "ema_168": np.full(n, 50.0), # below price
        "low_14d": np.full(n, 90.0),
        "low_7d": np.full(n, 92.0),
        "vol_shock": np.full(n, 2.5),
        "taker_ratio": np.full(n, 0.50),
        "d_oi_tokens_24h": np.full(n, 0.10),
        "tier": ["Tier 1"] * n
    }, index=dates)
    return df


def test_funding_sqz_exception_activation():
    """Verify funding squeeze exception bypasses veto when whales are net short."""
    # fr = 0.00045 (exceeds 0.00030 cap), ls_ratio = 0.90 (whales short <= 0.95, but >= 0.85 firewall)
    df = _create_mock_breakout_df(fr=0.00045, turnover=2.0, ls_ratio=0.90)

    # 1. Disabled mode -> must be vetoed
    cfg_disabled = V12Config(micro=MicrostructureConfig(enable_funding_sqz_exception=False))
    tel_disabled = TelemetryCollector()
    trades_disabled = run_v12_engine(df, "TEST", cfg=cfg_disabled, telemetry=tel_disabled)
    assert len(trades_disabled) == 0
    records_disabled = tel_disabled.records
    assert any(r.veto_gate == "Core 4: Funding Rate Cap" for r in records_disabled)

    # 2. Production Default (True) -> exception triggers, trade is taken
    cfg_prod = V12Config()
    tel_prod = TelemetryCollector()
    trades_prod = run_v12_engine(df, "TEST", cfg=cfg_prod, telemetry=tel_prod)
    assert len(trades_prod) >= 1
    assert trades_prod.iloc[0]["asset"] == "TEST"


def test_turnover_scaling_activation():
    """Verify turnover scaling bypasses 15.0x hard veto."""
    # turnover = 18.5 (exceeds 15.0x ceiling)
    df = _create_mock_breakout_df(fr=0.00010, turnover=18.5, ls_ratio=1.10)

    # 1. Disabled mode -> must be vetoed
    cfg_disabled = V12Config(micro=MicrostructureConfig(enable_turnover_scaling=False))
    tel_disabled = TelemetryCollector()
    trades_disabled = run_v12_engine(df, "TEST", cfg=cfg_disabled, telemetry=tel_disabled)
    assert len(trades_disabled) == 0
    records_disabled = tel_disabled.records
    assert any(r.veto_gate == "Core 3: Max Turnover Velocity" for r in records_disabled)

    # 2. Production Default (True) -> turnover scaling allows trade
    cfg_prod = V12Config()
    tel_prod = TelemetryCollector()
    trades_prod = run_v12_engine(df, "TEST", cfg=cfg_prod, telemetry=tel_prod)
    assert len(trades_prod) >= 1
    assert trades_prod.iloc[0]["asset"] == "TEST"
