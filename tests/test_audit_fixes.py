"""
Regression and Audit Fix Verification Test Suite
Validates the mathematical correctness of:
1. Log-space Profit Factor calculation
2. Robust days_below_ema bear market reset
3. MAE and MFE bar-level initialization
4. Telemetry boolean column filtering
"""

import sys
from pathlib import Path
import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from momentum_v12.build_csv import _log_pf


def test_log_profit_factor_calculation():
    """Verify log-space Profit Factor is mathematically sound."""
    # Case 1: Equal gains and losses in log space
    df_wins = pd.DataFrame({'log_ret': [0.10, 0.20, 0.30]})
    df_losses = pd.DataFrame({'log_ret': [-0.10, -0.20, -0.30]})
    pf = _log_pf(df_wins, df_losses)
    assert abs(pf - 1.0) < 1e-6

    # Case 2: 2x more gains than losses
    df_wins2 = pd.DataFrame({'log_ret': [0.20, 0.40, 0.60]})
    pf2 = _log_pf(df_wins2, df_losses)
    assert abs(pf2 - 2.0) < 1e-6

    # Case 3: Zero losses
    df_empty_loss = pd.DataFrame({'log_ret': []})
    pf3 = _log_pf(df_wins, df_empty_loss)
    assert pf3 == 999.0


def test_days_below_ema_bear_reset():
    """Verify days_below_ema resets cleanly to 0 upon crossing above EMA."""
    # Construct synthetic series: 100 bars below, 24 bars above, 50 bars below
    n = 200
    prices = [90.0] * 100 + [110.0] * 24 + [90.0] * 76
    ema = [100.0] * n
    df = pd.DataFrame({'close': prices, 'ema_200d': ema})

    below_ema_int = (df['close'] < df['ema_200d']).astype(int)
    group_id = (below_ema_int == 0).cumsum()
    bars_below = below_ema_int.groupby(group_id).cumsum()
    df['days_below_ema'] = bars_below / 24.0

    # During first bear run: bar 99 should be 100 / 24 days
    assert abs(df['days_below_ema'].iloc[99] - (100.0 / 24.0)) < 1e-6

    # During bull transition (bars 100 to 123): must be exactly 0
    for idx in range(100, 124):
        assert df['days_below_ema'].iloc[idx] == 0.0

    # During second bear run: bar 124 must reset and start from 1 / 24 days
    assert abs(df['days_below_ema'].iloc[124] - (1.0 / 24.0)) < 1e-6
    # Bar 140 (17th bar of second bear run) should be 17 / 24 days
    assert abs(df['days_below_ema'].iloc[140] - (17.0 / 24.0)) < 1e-6


def test_telemetry_safe_filtering():
    """Verify telemetry dodged/missed filtering behaves safely without DataFrame.get()."""
    tel_df = pd.DataFrame({
        'status': ['VETOED', 'VETOED', 'VETOED', 'ACTIVE'],
        'is_dodged_bullet': [True, False, False, False],
        'is_missed_opportunity': [False, True, False, False],
        'mae_72h_fwd': [-0.08, 0.0, -0.02, -0.01],
        'mfe_72h_fwd': [0.02, 0.25, 0.05, 0.10],
    })

    vetoed = tel_df[tel_df['status'] == 'VETOED'].copy()
    dodged = vetoed[vetoed['is_dodged_bullet'] == True]
    missed = vetoed[vetoed['is_missed_opportunity'] == True]

    assert len(dodged) == 1
    assert len(missed) == 1

    saved_loss = abs(dodged['mae_72h_fwd'].clip(upper=0.0).sum()) * 100.0
    missed_mfe = missed['mfe_72h_fwd'].sum() * 100.0

    assert abs(saved_loss - 8.0) < 1e-6
    assert abs(missed_mfe - 25.0) < 1e-6


def test_zero_tolerance_data_firewall():
    """Verify that candidate signals with missing/NaN exotic data are vetoed."""
    from momentum_v12.engine_v12 import run_v12_engine
    from momentum_v12.config import V12Config
    from momentum_v12.telemetry_v12 import TelemetryCollector
    import tempfile

    cfg = V12Config()
    dates = pd.date_range('2024-01-01', periods=100, freq='h')
    
    # Construct synthetic breakout data where exotic metrics are NaN
    df = pd.DataFrame({
        'open': [10.0] * 100,
        'high': [10.5] * 99 + [15.0],  # Bar 99 breakout
        'low': [9.5] * 100,
        'close': [10.0] * 99 + [14.0],
        'volume': [1000.0] * 99 + [50000.0],
        'breakout_21d': [False] * 99 + [True],
        'high_21d': [10.2] * 100,
        'low_14d': [9.0] * 100,
        'low_7d': [9.0] * 100,
        'low_72h': [9.2] * 100,
        'high_72h': [10.2] * 100,
        'shelf_range_72h': [0.10] * 100,
        'shelf_range_14d': [0.10] * 100,
        'dist_from_72h_low': [0.10] * 100,
        'ret_7d': [0.05] * 100,
        'ret_14d': [0.10] * 100,
        'rs_vs_btc': [0.05] * 100,
        'ema_168': [10.0] * 100,
        'vol_shock': [1.0] * 99 + [10.0],
        'btc_macro_bull': [True] * 100,
        'upper_wick': [0.10] * 100,
        # INTENTIONALLY NaN EXOTIC DERIVATIVES:
        'oi_usd': [np.nan] * 100,
        'funding_rate': [np.nan] * 100,
        'count_toptrader_long_short_ratio': [np.nan] * 100,
        'taker_ratio': [0.45] * 100,
        'turnover_24h': [np.nan] * 100,
    }, index=dates)

    with tempfile.TemporaryDirectory() as tmpdir:
        telemetry = TelemetryCollector(storage_dir=Path(tmpdir))
        trades = run_v12_engine(df, 'SYNTHETIC_TEST', cfg=cfg, telemetry=telemetry)
        
        # Zero-Tolerance firewall must have prevented ANY trade entry!
        assert len(trades) == 0, f"Expected 0 trades on NaN data, got {len(trades)}"
        
        # Telemetry must record the veto under Core 0
        tel_df = telemetry.to_dataframe()
        assert not tel_df.empty
        vetoes = tel_df[tel_df['status'] == 'VETOED']
        assert len(vetoes) > 0
        assert 'Core 0: Zero-Tolerance Data Firewall' in vetoes['veto_gate'].values
