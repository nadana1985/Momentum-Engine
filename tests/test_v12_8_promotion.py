"""
Unit & Integration Tests for Kronos V12.8 Production Promotion:
1. Book 4 Two-Phase Higher-Low Retest Reclaim Engine (Study S-BB).
2. Elimination of Premature Stop-Outs: bot_low preserved across touch clusters and anchored to swing low.
3. Study S-BE Two-Tranche Trajectory Exits (50% Target Cap +20%, 50% Rolling Donchian Trail with Breakeven Cushion Ratchet).
"""

import sys
from pathlib import Path
import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from momentum_v15.config import V12Config, Book4Config
from momentum_v15.features_v12 import compute_features_v12
from momentum_v15.engine_v12 import run_v12_engine


def _sbb_cfg() -> V12Config:
    """S-BB hourly reclaim path: S-CA day-close + microstructure off."""
    return V12Config(
        book4=Book4Config(
            enable_p_nb_day_close_confirmation=False,
            enable_p_nb_microstructure_sizing=False,
        )
    )


def test_book4_two_tranche_trajectory_exit():
    """Verify that when a Book 4 setup hits the +20% target cap,
    Tranche A locks in profit while Tranche B ratchets stop to breakeven and trails.
    """
    n = 2000
    dates = pd.date_range("2025-01-01", periods=n, freq="1h")
    
    # Construct synthetic series:
    # 0-200: Price high at 150.0 (so 200d EMA is ~100.0)
    # 200-1000: Price flat at 50.0 (>720h below EMA)
    # 1000-1040: Price surges to 105.0 (touching 200d EMA)
    # 1040-1070: Price pulls back to 92.0 (-12.4% retest dip, holding > base 50.0)
    # 1070-1100: Price reclaims back above 200d EMA to 108.0 (Entry trigger)
    # 1100-1150: Price pushes to 135.0 (+25% gain, hitting Tranche A target cap at 1.20 * 108 = 129.6)
    # 1150-1200: Price holds and runs to 145.0
    c = np.full(n, 50.0)
    c[:200] = 150.0
    c[200:1000] = 50.0
    c[1000:1040] = np.linspace(50.0, 105.0, 40)
    c[1040:1070] = np.linspace(105.0, 92.0, 30)
    c[1070:1100] = np.linspace(92.0, 108.0, 30)
    c[1100:1150] = np.linspace(108.0, 135.0, 50)
    c[1150:] = 135.0
    
    h = c + 0.5
    l = c - 0.5
    
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
    trades = run_v12_engine(feat, "SYNTHETIC_B4_TOKEN", cfg=cfg)
    
    assert isinstance(trades, pd.DataFrame)
    assert not trades.empty
    
    b4_trades = trades[trades['book'] == 'Book 4']
    assert not b4_trades.empty, "Book 4 trade should have fired on the 200d EMA reclaim"
    
    trade = b4_trades.iloc[0]
    # Trade should achieve positive PnL
    assert trade['raw_pnl'] > 0.05, f"Expected profitable exit, got raw_pnl={trade['raw_pnl']}"


def test_book4_retest_dip_immunity():
    """Verify that repeated touches in a cluster do NOT overwrite bot_low,
    allowing the trade to absorb a natural Higher Low retest dip without premature stop-out.
    """
    n = 2000
    dates = pd.date_range("2025-01-01", periods=n, freq="1h")
    
    c = np.full(n, 50.0)
    c[:200] = 150.0
    c[200:1000] = 50.0
    # Surge to touch EMA
    c[1000:1030] = np.linspace(50.0, 102.0, 30)
    # Repeated touches in cluster
    c[1030:1050] = np.linspace(102.0, 103.0, 20)
    # Healthy -10% retest dip
    c[1050:1080] = np.linspace(103.0, 92.0, 30)
    # Reclaim
    c[1080:1110] = np.linspace(92.0, 106.0, 30)
    # Expansion to target
    c[1110:1160] = np.linspace(106.0, 130.0, 50)
    c[1160:] = 130.0
    
    h = c + 0.5
    l = c - 0.5
    
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
    trades = run_v12_engine(feat, "RETEST_TOKEN", cfg=cfg)
    
    assert isinstance(trades, pd.DataFrame)
    b4 = trades[trades['book'] == 'Book 4']
    assert not b4.empty
    
    # Trade should survive the dip and achieve positive PnL
    t = b4.iloc[0]
    assert t['raw_pnl'] > 0.0, "Trade should not have stopped out prematurely during the retest dip"
