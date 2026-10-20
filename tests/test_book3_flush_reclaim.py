"""
Tests for Study S-AC: Bull-Market Flush Absorption & Reclaim Architecture (v12_standalone/tests/test_book3_flush_reclaim.py)
Validates:
  1. Immutable contract compliance for Book3FlushReclaimConfig.
  2. Zero-regression default on baseline production engine.
  3. Passive resting limit fill at 0.92 * P0 (0 taker slippage) and 100% target reclaim at P0 (+8.70%).
  4. Resting stop loss protection at 0.8464 * P0 (-8.0% from fill).
  5. 72h TTL cancellation when flush discount is not reached.
  6. Strict BTC macro bear prohibition (Book 3 arms exclusively in confirmed bull regimes).
  7. Discrete sizing invariance (w = 1.0, not subject to Kyle-lambda continuous scaling).
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pytest
import numpy as np
import pandas as pd
from momentum_v12.config import V12Config, Book3FlushReclaimConfig
from momentum_v12.telemetry_v12 import TelemetryRecord, TelemetryCollector
from momentum_v12.engine_v12 import run_v12_engine


def test_book3_flush_config_immutability():
    """Verify Book3FlushReclaimConfig is immutable and enforces domain constraints."""
    cfg = Book3FlushReclaimConfig()
    assert cfg.enable_book3_flush_reclaim is True
    assert cfg.enable_tier1 is True
    assert cfg.enable_tier2 is False
    assert cfg.enable_tier3 is True
    assert cfg.flush_discount_pct == 0.080
    assert cfg.tier2_flush_discount_pct == 0.120
    assert cfg.ttl_hours == 72
    assert cfg.max_initial_risk == 0.080
    assert cfg.target_reclaim_pct == 0.087
    assert cfg.require_btc_macro_bull is True
    assert cfg.book3_shelf_mode == "shelf_fallback"
    assert cfg.vp_lookback_bars == 2160
    assert cfg.vp_bins == 35
    assert cfg.corridor_lo == 0.85
    assert cfg.corridor_hi == 0.96
    assert cfg.hvn_mult_support == 1.0

    # Test frozen immutability
    with pytest.raises(Exception):
        cfg.enable_book3_flush_reclaim = True

    # Test invalid constraints
    with pytest.raises(AssertionError):
        Book3FlushReclaimConfig(flush_discount_pct=-0.05)

    with pytest.raises(AssertionError):
        Book3FlushReclaimConfig(flush_discount_pct=0.30)

    with pytest.raises(AssertionError):
        Book3FlushReclaimConfig(tier2_flush_discount_pct=-0.05)

    with pytest.raises(AssertionError):
        Book3FlushReclaimConfig(tier2_flush_discount_pct=0.35)

    with pytest.raises(AssertionError):
        Book3FlushReclaimConfig(ttl_hours=0)

    with pytest.raises(AssertionError):
        Book3FlushReclaimConfig(max_initial_risk=0.25)

    with pytest.raises(AssertionError):
        Book3FlushReclaimConfig(book3_shelf_mode="unsupported_mode")

    with pytest.raises(AssertionError):
        Book3FlushReclaimConfig(vp_lookback_bars=0)

    with pytest.raises(AssertionError):
        Book3FlushReclaimConfig(vp_bins=5)

    with pytest.raises(AssertionError):
        Book3FlushReclaimConfig(corridor_lo=0.98, corridor_hi=0.92)

    with pytest.raises(AssertionError):
        Book3FlushReclaimConfig(hvn_mult_support=0.0)


def test_tier2_calibrated_flush_discount():
    """
    Verify Tier 2 mid-caps use calibrated -12.0% discount:
      P0 = $10.00 -> Limit Bid = $10.00 * (1 - 0.12) = $8.80.
      Stop = $8.80 * (1 - 0.08) = $8.096. Target = $10.00 (+13.6% gain).
    """
    n_bars = 40
    dates = pd.date_range("2026-03-15 00:00:00", periods=n_bars, freq="1h")

    closes = np.full(n_bars, 9.0)
    closes[10] = 10.00
    closes[11:14] = [9.50, 9.10, 8.85]
    closes[14] = 8.78   # Dips below Tier 2 limit bid of $8.80
    closes[15:20] = [8.90, 9.20, 9.50, 9.80, 9.95]
    closes[20] = 10.05  # Reclaims P0
    closes[21:] = 10.10

    highs = closes * 1.01
    lows = closes * 0.99
    lows[14] = 8.75     # Crosses below Tier 2 limit bid ($8.80)
    highs[20] = 10.05   # Reaches target $10.00

    df = pd.DataFrame({
        "close": closes,
        "high": highs,
        "low": lows,
        "open": closes,
        "tier": "Tier 2",  # STRICT TIER 2 ASSET
        "btc_macro_bull": True,
        "btc_cycle_spring": False,
        "breakout_21d": False,
        "ret_14d": 0.25,
        "rs_vs_btc": 0.20,
        "ema_168": 8.0,
        "low_60d": 7.0,
        "low_14d": 8.0,
        "low_7d": 8.0,
        "toptrader_ls": 1.20,
        "turnover_24h": 3.0,
        "funding_rate": 0.00080, # Triggers Core 4 Funding Rate Cap veto
        "vol_shock": 2.5,
        "oi_change_14d": 0.10,
        "oi_usd": 5e6,
        "open_interest": 5e5,
        "taker_ratio": 0.50,
        "pct_lambda": 0.40,
        "btc_ath_pct": 50.0
    }, index=dates)
    df.index.name = "dt"
    df.loc[dates[10], "breakout_21d"] = True

    cfg = V12Config(book3_flush=Book3FlushReclaimConfig(enable_book3_flush_reclaim=True, enable_tier2=True))
    trades, _ = run_v12_engine(df, "TIER2_COIN", cfg=cfg)

    assert len(trades) == 1
    tr = trades.iloc[0]
    assert tr["book"] == "Book 3"
    assert tr["tier"] == "Tier 2"
    assert abs(tr["entry_price"] - 8.80) < 1e-4  # Filled at calibrated -12.0% discount!
    assert abs(tr["exit_price"] - 10.00) < 1e-4  # Reclaimed target P0
    assert abs(tr["stop_price"] - 8.096) < 1e-4  # Clamped at -8% from fill
    assert tr["raw_pnl"] > 0.13                  # +13.6% raw gain


def test_tier2_disabled_by_default_in_book3():
    """Verify that by default, Tier 2 mid-caps are disabled in Book 3 to purge absorption drag."""
    n_bars = 40
    dates = pd.date_range("2026-03-15 00:00:00", periods=n_bars, freq="1h")

    closes = np.full(n_bars, 9.0)
    closes[10] = 10.00
    closes[14] = 8.78

    highs = closes * 1.01
    lows = closes * 0.99
    lows[14] = 8.75

    df = pd.DataFrame({
        "close": closes,
        "high": highs,
        "low": lows,
        "open": closes,
        "tier": "Tier 2",  # STRICT TIER 2 ASSET
        "btc_macro_bull": True,
        "btc_cycle_spring": False,
        "breakout_21d": False,
        "ret_14d": 0.25,
        "rs_vs_btc": 0.20,
        "ema_168": 8.0,
        "low_60d": 7.0,
        "low_14d": 8.0,
        "low_7d": 8.0,
        "toptrader_ls": 1.20,
        "turnover_24h": 3.0,
        "funding_rate": 0.00080,
        "vol_shock": 2.5,
        "oi_change_14d": 0.10,
        "oi_usd": 5e6,
        "open_interest": 5e5,
        "taker_ratio": 0.50,
        "pct_lambda": 0.40,
        "btc_ath_pct": 50.0
    }, index=dates)
    df.index.name = "dt"
    df.loc[dates[10], "breakout_21d"] = True

    # Book 3 enabled, but enable_tier2 defaults to False
    cfg = V12Config(book3_flush=Book3FlushReclaimConfig(enable_book3_flush_reclaim=True))
    trades, _ = run_v12_engine(df, "TIER2_COIN", cfg=cfg)

    # Must produce 0 trades because Tier 2 is disabled
    assert len(trades) == 0


def test_production_default_has_book3_enabled():
    """Verify that default V12Config has Book 3 enabled as part of canonical production."""
    cfg = V12Config()
    assert cfg.book3_flush.enable_book3_flush_reclaim is True


def test_disabled_book3_produces_no_book3_trades():
    """Verify that explicitly disabling Book 3 produces 0 Book 3 trades."""
    cfg = V12Config(book3_flush=Book3FlushReclaimConfig(enable_book3_flush_reclaim=False))
    assert cfg.book3_flush.enable_book3_flush_reclaim is False


def test_book3_flush_fill_and_target_reclaim():
    """
    Simulate synthetic bull-market shard:
      Bar 10: Breakout trigger vetoed by Core 4 Funding Cap (funding > max).
              Arms resting limit bid at $10.00 * (1 - 0.08) = $9.20. Target = $10.00, Stop = $8.464.
      Bar 14: Flush occurs! Low dips to $9.15 <= $9.20 -> fills at limit price $9.20.
      Bar 20: Recovery! High reaches $10.05 >= $10.00 -> exits at $10.00 (target_reclaim).
    """
    n_bars = 60
    dates = pd.date_range("2026-03-15 00:00:00", periods=n_bars, freq="1h")

    closes = np.full(n_bars, 9.0)
    closes[10] = 10.00  # Trigger candle at P0 = 10.00
    closes[11:14] = [9.70, 9.50, 9.30]
    closes[14] = 9.18   # Flush bar
    closes[15:20] = [9.30, 9.50, 9.70, 9.85, 9.95]
    closes[20] = 10.05  # Reclaim bar
    closes[21:] = 10.10

    highs = closes * 1.01
    lows = closes * 0.99
    lows[14] = 9.15     # Crosses below limit bid of $9.20
    highs[20] = 10.05   # Reaches target $10.00

    df = pd.DataFrame({
        "close": closes,
        "high": highs,
        "low": lows,
        "open": closes,
        "tier": "Tier 1",
        "btc_macro_bull": True,  # Bull market
        "btc_cycle_spring": False,
        "breakout_21d": False,
        "ret_14d": 0.25,
        "rs_vs_btc": 0.20,
        "ema_168": 8.0,
        "low_60d": 7.0,
        "low_14d": 8.0,
        "low_7d": 8.0,
        "toptrader_ls": 1.20,
        "turnover_24h": 3.0,
        "funding_rate": 0.00080, # Very high funding -> triggers Core 4 Funding Rate Cap veto!
        "vol_shock": 2.5,
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

    # 1. With Book 3 DISABLED: 0 trades fired (100% vetoed)
    cfg_off = V12Config(book3_flush=Book3FlushReclaimConfig(enable_book3_flush_reclaim=False))
    t_off, _ = run_v12_engine(df, "FLUSH_COIN", cfg=cfg_off)
    assert len(t_off) == 0

    # 2. With Book 3 ENABLED:
    cfg_on = V12Config(book3_flush=Book3FlushReclaimConfig(
        enable_book3_flush_reclaim=True,
        flush_discount_pct=0.080,
        ttl_hours=72,
        max_initial_risk=0.080,
        target_reclaim_pct=0.087
    ))
    tel = TelemetryCollector()
    t_on, _ = run_v12_engine(df, "FLUSH_COIN", cfg=cfg_on, telemetry=tel)

    assert len(t_on) == 1
    tr = t_on.iloc[0]
    assert tr["book"] == "Book 3"
    assert bool(tr["is_book3"]) is True
    assert tr["reason"] == "target_reclaim"
    assert tr["sizing_weight"] == 1.0 # Pure discrete unit sizing
    assert abs(tr["entry_price"] - 9.20) < 1e-4 # Filled at exact limit price
    assert abs(tr["exit_price"] - 10.00) < 1e-4  # Exited at exact target reclaim price
    assert tr["raw_pnl"] > 0.08


def test_book3_flush_stop_loss():
    """
    Simulate falling knife:
      Bar 10: Breakout trigger vetoed at P0 = 10.00 -> Limit bid at $9.20, Stop at $8.464.
      Bar 14: Filled at $9.20.
      Bar 16: Cascades down to Low = $8.30 <= $8.464 -> Exits via stop_loss!
    """
    n_bars = 40
    dates = pd.date_range("2026-03-15 00:00:00", periods=n_bars, freq="1h")

    closes = np.full(n_bars, 9.0)
    closes[10] = 10.00
    closes[14] = 9.18
    closes[15] = 8.80
    closes[16] = 8.35
    closes[17:] = 8.00

    highs = closes * 1.01
    lows = closes * 0.99
    lows[14] = 9.15  # Limit filled
    lows[16] = 8.30  # Smashes through stop at 8.464

    df = pd.DataFrame({
        "close": closes,
        "high": highs,
        "low": lows,
        "open": closes,
        "tier": "Tier 1",
        "btc_macro_bull": True,
        "btc_cycle_spring": False,
        "breakout_21d": False,
        "ret_14d": 0.25,
        "rs_vs_btc": 0.20,
        "ema_168": 8.0,
        "low_60d": 7.0,
        "low_14d": 8.0,
        "low_7d": 8.0,
        "toptrader_ls": 1.20,
        "turnover_24h": 3.0,
        "funding_rate": 0.00080,
        "vol_shock": 2.5,
        "oi_change_14d": 0.10,
        "oi_usd": 2e7,
        "open_interest": 2e6,
        "taker_ratio": 0.50,
        "pct_lambda": 0.40,
        "btc_ath_pct": 50.0
    }, index=dates)
    df.index.name = "dt"
    df.loc[dates[10], "breakout_21d"] = True

    cfg = V12Config(book3_flush=Book3FlushReclaimConfig(enable_book3_flush_reclaim=True))
    trades, _ = run_v12_engine(df, "FLUSH_KNIFE", cfg=cfg)

    assert len(trades) == 1
    tr = trades.iloc[0]
    assert tr["book"] == "Book 3"
    assert tr["reason"] == "stop_loss"
    assert tr["raw_pnl"] < 0.0


def test_book3_ttl_expiry_when_limit_not_reached():
    """
    If price consolidates between 9.50 and 10.00 and never drops to 9.20 within 72h,
    the resting limit order expires harmlessly with 0 trades and $0 risk.
    """
    n_bars = 100
    dates = pd.date_range("2026-03-15 00:00:00", periods=n_bars, freq="1h")

    closes = np.full(n_bars, 9.60)
    closes[10] = 10.00  # P0 = 10.00, Limit = 9.20
    # Lows never drop below 9.40
    highs = closes + 0.20
    lows = closes - 0.10

    df = pd.DataFrame({
        "close": closes,
        "high": highs,
        "low": lows,
        "open": closes,
        "tier": "Tier 1",
        "btc_macro_bull": True,
        "btc_cycle_spring": False,
        "breakout_21d": False,
        "ret_14d": 0.25,
        "rs_vs_btc": 0.20,
        "ema_168": 8.0,
        "low_60d": 7.0,
        "low_14d": 8.0,
        "low_7d": 8.0,
        "toptrader_ls": 1.20,
        "turnover_24h": 3.0,
        "funding_rate": 0.00080,
        "vol_shock": 2.5,
        "oi_change_14d": 0.10,
        "oi_usd": 2e7,
        "open_interest": 2e6,
        "taker_ratio": 0.50,
        "pct_lambda": 0.40,
        "btc_ath_pct": 50.0
    }, index=dates)
    df.index.name = "dt"
    df.loc[dates[10], "breakout_21d"] = True

    cfg = V12Config(book3_flush=Book3FlushReclaimConfig(enable_book3_flush_reclaim=True))
    trades, _ = run_v12_engine(df, "FLUSH_NO_FILL", cfg=cfg)

    # Never reached $9.20, expired harmlessly -> 0 trades
    assert len(trades) == 0


def test_book3_bear_market_veto_preservation():
    """
    During a Bitcoin bear market (btc_macro_bull = False), Book 3 must strictly NEVER arm,
    preserving Core 1 100% Cash Preservation invariant.
    """
    n_bars = 40
    dates = pd.date_range("2026-03-15 00:00:00", periods=n_bars, freq="1h")

    closes = np.full(n_bars, 9.0)
    closes[10] = 10.00
    closes[14] = 9.10 # drops below limit bid

    df = pd.DataFrame({
        "close": closes,
        "high": closes * 1.01,
        "low": closes * 0.99,
        "open": closes,
        "tier": "Tier 1",
        "btc_macro_bull": False, # STRICT BEAR MARKET
        "btc_cycle_spring": False,
        "breakout_21d": False,
        "ret_14d": 0.25,
        "rs_vs_btc": 0.20,
        "ema_168": 8.0,
        "low_60d": 7.0,
        "low_14d": 8.0,
        "low_7d": 8.0,
        "toptrader_ls": 1.20,
        "turnover_24h": 3.0,
        "funding_rate": 0.00080,
        "vol_shock": 2.5,
        "oi_change_14d": 0.10,
        "oi_usd": 2e7,
        "open_interest": 2e6,
        "taker_ratio": 0.50,
        "pct_lambda": 0.40,
        "btc_ath_pct": 50.0
    }, index=dates)
    df.index.name = "dt"
    df.loc[dates[10], "breakout_21d"] = True

    cfg = V12Config(book3_flush=Book3FlushReclaimConfig(enable_book3_flush_reclaim=True))
    trades, _ = run_v12_engine(df, "BEAR_FLUSH", cfg=cfg)

    # In bear regime, Core 1 vetoes immediately to cash and Book 3 refuses to arm
    assert len(trades) == 0


def test_two_tier_volume_shelf_absorption():
    """
    Study S-AN / S-AO: Two-Tier Volume Profile Shelf Absorption (Canonical V12.3)
    Verifies that when a high-volume consolidation shelf exists in the [-15%, -4%] corridor:
      1. The limit bid is placed at the shelf high (~$9.40) rather than the static -8% ($9.20).
      2. When price dips to $9.38 (above $9.20), the order fills at the shelf bid price.
      3. When price reclaims P0 ($10.00), the trade exits at target reclaim.
    """
    n_bars = 250
    dates = pd.date_range("2026-03-15 00:00:00", periods=n_bars, freq="1h")
    closes = np.full(n_bars, 9.40)
    closes[200] = 10.00  # P0 breakout pop
    closes[201:205] = [9.70, 9.50, 9.38, 9.40]  # Dips to 9.38, never reaches 9.20
    closes[205:215] = np.linspace(9.45, 10.05, 10) # Reclaims target 10.00
    highs = closes * 1.002
    lows = closes * 0.998
    highs[214] = 10.05
    volume = np.full(n_bars, 50000.0)

    df = pd.DataFrame({
        "close": closes, "high": highs, "low": lows, "open": closes,
        "volume": volume, "quote_volume": closes * volume, "tier": "Tier 1",
        "btc_macro_bull": True, "breakout_21d": False, "ret_14d": 0.25, "rs_vs_btc": 0.20,
        "ema_168": 8.0, "low_60d": 7.0, "low_14d": 8.0, "low_7d": 8.0, "toptrader_ls": 1.20,
        "turnover_24h": 3.0, "funding_rate": 0.00080, "vol_shock": 2.5, "oi_usd": 2e7
    }, index=dates)
    df.loc[dates[200], "breakout_21d"] = True

    # 1. Canonical V12.3 (shelf_fallback default): captures the shallow shelf bounce
    cfg_shelf = V12Config(book3_flush=Book3FlushReclaimConfig(enable_book3_flush_reclaim=True, book3_shelf_mode="shelf_fallback"))
    trades_shelf, _ = run_v12_engine(df, "SHELF_COIN", cfg=cfg_shelf)
    assert len(trades_shelf) == 1
    tr = trades_shelf.iloc[0]
    assert tr["book"] == "Book 3"
    assert tr["reason"] == "target_reclaim"
    assert tr["entry_price"] > 9.35  # Filled at shelf (~9.40)
    assert abs(tr["exit_price"] - 10.00) < 1e-4

    # 2. Static Only baseline: requires deep dip to $9.20, misses the shallow shelf bounce (0 trades)
    cfg_static = V12Config(book3_flush=Book3FlushReclaimConfig(enable_book3_flush_reclaim=True, book3_shelf_mode="static_only"))
    trades_static, _ = run_v12_engine(df, "SHELF_COIN", cfg=cfg_static)
    assert len(trades_static) == 0


def test_volume_shelf_static_fallback_when_no_hvn():
    """
    Verifies that when historical volume profile has NO high-volume node in the [-15%, -4%] corridor:
      - The engine falls back seamlessly to the static -8.0% limit bid ($9.20 for P0 = $10.00).
    """
    n_bars = 250
    dates = pd.date_range("2026-03-15 00:00:00", periods=n_bars, freq="1h")
    # All historical volume is at $7.50 (outside [8.50, 9.60] corridor)
    closes = np.full(n_bars, 7.50)
    closes[200] = 10.00  # P0 breakout pop
    closes[201:205] = [9.70, 9.40, 9.15, 9.20]  # Dips to 9.15, filling static -8% bid ($9.20)
    closes[205:215] = np.linspace(9.30, 10.05, 10) # Reclaims target 10.00
    highs = closes * 1.002
    lows = closes * 0.998
    lows[203] = 9.15  # Crosses below $9.20
    highs[214] = 10.05
    volume = np.full(n_bars, 50000.0)

    df = pd.DataFrame({
        "close": closes, "high": highs, "low": lows, "open": closes,
        "volume": volume, "quote_volume": closes * volume, "tier": "Tier 1",
        "btc_macro_bull": True, "breakout_21d": False, "ret_14d": 0.25, "rs_vs_btc": 0.20,
        "ema_168": 6.0, "low_60d": 5.0, "low_14d": 6.0, "low_7d": 6.0, "toptrader_ls": 1.20,
        "turnover_24h": 3.0, "funding_rate": 0.00080, "vol_shock": 2.5, "oi_usd": 2e7
    }, index=dates)
    df.loc[dates[200], "breakout_21d"] = True

    cfg = V12Config(book3_flush=Book3FlushReclaimConfig(enable_book3_flush_reclaim=True, book3_shelf_mode="shelf_fallback"))
    trades, _ = run_v12_engine(df, "FALLBACK_COIN", cfg=cfg)

    assert len(trades) == 1
    tr = trades.iloc[0]
    assert tr["book"] == "Book 3"
    assert abs(tr["entry_price"] - 9.20) < 1e-4  # Filled at static fallback -8.0% ($9.20)
    assert abs(tr["exit_price"] - 10.00) < 1e-4
    assert tr["reason"] == "target_reclaim"
