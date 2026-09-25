# Version 10
"""Shared causal feature core — the single enrichment used by every consumer.

All baseline windows terminate at t-1 (shift(1) everywhere); the only bar-t
reads are the bar's own OHLCV/taker values. Forward bars are never touched
here — they live exclusively in outcomes.py.

This replaces the copy-pasted ~40-line block that existed in 6+ files with one
implementation. Verified by scratch/causal_proof.py's truncation test.
"""
from __future__ import annotations

import pandas as pd

from .config import BARS_1YR, BARS_24H, BARS_30D, FeatureConfig


def load_asset(path) -> pd.DataFrame:
    """Load a 1h shard, converting epoch-ms timestamps, sorted ascending."""
    df = pd.read_parquet(path)
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df = df.set_index('timestamp')
    elif not pd.api.types.is_datetime64_any_dtype(df.index):
        df.index = pd.to_datetime(df.index, unit='ms')
    return df.sort_index()


def enrich(df: pd.DataFrame, cfg: FeatureConfig) -> pd.DataFrame:
    """Compute all causal ignition features. Returns a copy with columns added.

    Feature columns produced:
      notional_vol, p50_30d, p50_1yr, vol_24h_avg, shock_mult,
      price_24h_high, price_24h_low, breakout, breakdown, taker_ratio,
      p50_taker_30d, is_aggressive_flow, shock_thresh, is_dormant_book,
      hyper_ignition (shock gate + dormant + breakout), strict_ignition
      (adds aggressive taker flow), ignition_signal (first-of-run variant).
    """
    out = df.copy()

    # --- baselines: all windows terminate at t-1 ---
    out['notional_vol'] = out['volume'] * out['close']
    out['p50_30d'] = out['notional_vol'].shift(1).rolling(BARS_30D, min_periods=BARS_30D).median()
    out['p50_1yr'] = out['notional_vol'].shift(1).rolling(
        BARS_1YR, min_periods=cfg.year_min_periods).median()

    # FIXED: shift(1) must precede rolling() so bar-t's own volume never contaminates
    # its own baseline. Pattern is consistent with every other baseline in this file.
    out['vol_24h_avg'] = out['volume'].shift(1).rolling(BARS_24H, min_periods=1).mean()
    out['shock_mult'] = out['volume'] / out['vol_24h_avg']
    out['price_24h_high'] = out['high'].shift(1).rolling(BARS_24H, min_periods=1).max()
    out['price_24h_low'] = out['low'].shift(1).rolling(BARS_24H, min_periods=1).min()
    out['breakout'] = out['close'] > out['price_24h_high']
    out['breakdown'] = out['close'] < out['price_24h_low']

    # --- taker flow (own 30d median baseline + buffer) ---
    out['taker_ratio'] = out['taker_buy_base_volume'] / out['volume']
    out['p50_taker_30d'] = out['taker_ratio'].shift(1).rolling(
        BARS_30D, min_periods=BARS_30D).median()
    out['is_aggressive_flow'] = out['taker_ratio'] > (out['p50_taker_30d'] + cfg.taker_buffer)

    # --- dormant book (one implementation, named modes) ---
    if cfg.dormant_mode == 'relative':
        out['is_dormant_book'] = out['p50_30d'] < out['p50_1yr']
    elif cfg.dormant_mode == 'abs_usd':
        out['is_dormant_book'] = out['p50_30d'] < cfg.max_notional_usd
    elif cfg.dormant_mode == 'volume':
        vol_p50_30d = out['volume'].shift(1).rolling(BARS_30D, min_periods=BARS_30D).median()
        out['is_dormant_book'] = out['vol_24h_avg'] < vol_p50_30d
    else:
        raise ValueError(f"unknown dormant_mode '{cfg.dormant_mode}'")

    # --- shock gate: trailing-1yr percentile of own shock_mult, or fixed ---
    if cfg.shock_mult is not None:
        out['shock_thresh'] = float(cfg.shock_mult)
    else:
        out['shock_thresh'] = out['shock_mult'].shift(1).rolling(
            BARS_1YR, min_periods=cfg.year_min_periods).quantile(cfg.shock_percentile / 100.0)

    shock_hit = (out['shock_mult'] > out['shock_thresh']) & (out['volume'] > 0)
    out['hyper_ignition'] = shock_hit & out['is_dormant_book'] & out['breakout']
    out['strict_ignition'] = out['hyper_ignition'] & out['is_aggressive_flow']

    # which flag column consumers treat as the ignition depends on require_taker
    out['_ignition'] = out['strict_ignition'] if cfg.require_taker else out['hyper_ignition']

    # first-of-run dedup of consecutive hourly flags (uses only the PREVIOUS bar)
    if cfg.first_of_run:
        out['ignition_signal'] = out['_ignition'] & (~out['_ignition'].shift(1).fillna(False))
    else:
        out['ignition_signal'] = out['_ignition']
    return out




