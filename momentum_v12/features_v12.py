"""
Kronos V12: Feature Engineering & Context Synthesis Kernel
Calculates candlestick anatomy, orderbook turnover, exotic derivatives tape,
and 200-day BTC macro regime features.
"""

from pathlib import Path
from typing import Optional
import numpy as np
import pandas as pd

from momentum_v12.config import V12Config

_BTC_CACHE: Optional[pd.DataFrame] = None


def get_btc_macro(
    raw_dir: Optional[Path] = None,
    ema_hours: int = 4800,
    return_hours: int = 720
) -> Optional[pd.DataFrame]:
    """Loads BTC/USDT 1h shard and calculates 200-day EMA and 30-day return."""
    global _BTC_CACHE
    if _BTC_CACHE is not None:
        return _BTC_CACHE

    if raw_dir is None:
        # Fallback candidate search
        candidates = [
            Path("data/raw_shards"),
            Path(__file__).resolve().parent.parent / "data" / "raw_shards",
            Path(__file__).resolve().parent.parent.parent / "data" / "raw_shards",
        ]
        for c in candidates:
            if c.exists() and (c / "BTC_USDT_1h.parquet").exists():
                raw_dir = c
                break

    if raw_dir is None:
        return None

    btc_path = raw_dir / "BTC_USDT_1h.parquet"
    if not btc_path.exists():
        return None

    df = pd.read_parquet(btc_path)
    df['dt'] = pd.to_datetime(df['timestamp'], unit='ms')
    df = df.dropna(subset=['dt']).sort_values('dt').set_index('dt')

    # Core 1 Macro indicators: 200-day EMA (4800h) and 30-day return (720h)
    df['ema_200d'] = df['close'].ewm(span=ema_hours, adjust=False).mean()
    df['ret_30d'] = df['close'] / df['close'].shift(return_hours) - 1.0
    df['ret_14d'] = df['close'] / df['close'].shift(336) - 1.0
    df['btc_ath'] = df['close'].cummax()
    df['btc_ath_pct'] = (df['close'] / df['btc_ath']).fillna(1.0)

    # Study S-Y: Consecutive duration below 200-day EMA for Cycle Bottom Spring Module
    # Robust implementation: cast to int, group by above-EMA transitions,
    # cumsum within each bear episode, then reset cleanly to 0 on every above-EMA bar.
    below_ema_int = (df['close'] < df['ema_200d']).astype(int)
    # Each time price crosses ABOVE the EMA, create a new group ID
    group_id = (below_ema_int == 0).cumsum()
    # Within each group: cumulative bars spent below EMA
    bars_below = below_ema_int.groupby(group_id).cumsum()
    df['days_below_ema'] = bars_below / 24.0

    _BTC_CACHE = df
    return _BTC_CACHE


def load_shard(
    asset: str,
    raw_dir: Path,
    exotic_dir: Optional[Path] = None
) -> Optional[pd.DataFrame]:
    """
    Robust loader for 1h OHLCV shard merged backward as-of with
    funding rate and top trader L/S + Open Interest derivatives.
    """
    raw_path = raw_dir / f"{asset}_USDT_1h.parquet"
    if not raw_path.exists():
        raw_path = raw_dir / f"1000{asset}_USDT_1h.parquet"
    if not raw_path.exists():
        return None

    try:
        raw = pd.read_parquet(raw_path)
        raw = raw.dropna(subset=['timestamp']).sort_values('timestamp')

        if exotic_dir is None:
            exotic_dir = raw_dir.parent / "exotic_shards"

        # 1. Merge Funding Rates
        fund_path = exotic_dir / f"{asset}USDT_funding.parquet"
        if not fund_path.exists():
            fund_path = exotic_dir / f"1000{asset}USDT_funding.parquet"
        if fund_path.exists():
            fund = pd.read_parquet(fund_path, columns=['timestamp', 'funding_rate'])
            fund = fund.dropna(subset=['timestamp']).sort_values('timestamp')
            df = pd.merge_asof(raw, fund, on='timestamp', direction='backward')
            df['funding_rate'] = df['funding_rate'].ffill().fillna(0.0)
        else:
            df = raw.copy()
            df['funding_rate'] = 0.0

        # 2. Merge Metrics (OI & Top Trader L/S)
        met_path = exotic_dir / f"{asset}USDT_metrics.parquet"
        if not met_path.exists():
            met_path = exotic_dir / f"1000{asset}USDT_metrics.parquet"
        if met_path.exists():
            cols = ['timestamp', 'sum_open_interest_value', 'count_toptrader_long_short_ratio']
            # If token open interest exists, load it as well
            met_schema = pd.read_parquet(met_path).columns
            if 'sum_open_interest' in met_schema:
                cols.append('sum_open_interest')
            met = pd.read_parquet(met_path, columns=cols)
            met = met.dropna(subset=['timestamp']).sort_values('timestamp')
            df = pd.merge_asof(df, met, on='timestamp', direction='backward')
            df['sum_open_interest_value'] = df['sum_open_interest_value'].ffill()
            df['count_toptrader_long_short_ratio'] = df['count_toptrader_long_short_ratio'].ffill()
            if 'sum_open_interest' in df.columns:
                df['sum_open_interest'] = df['sum_open_interest'].ffill()
        else:
            df['sum_open_interest_value'] = np.nan
            df['count_toptrader_long_short_ratio'] = np.nan

        df['dt'] = pd.to_datetime(df['timestamp'], unit='ms')
        df = df.set_index('dt')
        return df
    except Exception:
        return None


def compute_features_v12(
    df: pd.DataFrame,
    btc_df: Optional[pd.DataFrame] = None,
    tier_label: str = "Tier 1",
    cfg: V12Config = V12Config()
) -> pd.DataFrame:
    """
    Computes all mathematical features across the 6-Core stack:
    - Candlestick anatomy (upper wick, volume shock, ATR)
    - Donchian channels (7d, 14d, 21d, 60d)
    - Moving averages & returns (EMA 168, ret 14d, dist from 60d base)
    - Orderbook turnover velocity (24h volume USD / max(1e5, OI USD))
    - Exotic metrics (d_ls_24h, max_ls_7d, d_oi_tokens_24h)
    - BTC 200-day macro trend & relative strength
    """
    out = df.copy()
    c = out['close']
    h = out['high']
    l = out['low']
    o = out['open']
    v = out['volume']

    # 1. Candlestick Anatomy
    rng = (h - l).replace(0, np.nan)
    out['upper_wick'] = ((h - np.maximum(o, c)) / rng).fillna(0.0)
    vol_ma168 = v.rolling(168, min_periods=24).mean()
    out['vol_shock'] = (v / vol_ma168).fillna(1.0)

    tr = h - l
    out['atr_24'] = tr.rolling(24, min_periods=12).mean()
    out['atr_168'] = tr.rolling(168, min_periods=24).mean()
    out['vol_comp'] = (out['atr_24'] / out['atr_168']).fillna(1.0)

    # 2. Donchian Extremes & Moving Averages
    out['high_21d'] = h.shift(1).rolling(cfg.entry.breakout_lookback_bars, min_periods=168).max()
    out['high_14d'] = h.shift(1).rolling(cfg.exit.tier1_donchian_bars, min_periods=96).max()
    out['low_7d'] = l.shift(1).rolling(cfg.exit.tier2_donchian_bars, min_periods=48).min()
    out['low_14d'] = l.shift(1).rolling(cfg.exit.tier1_donchian_bars, min_periods=96).min()
    out['low_60d'] = l.shift(1).rolling(1440, min_periods=336).min()
    out['ema_168'] = c.ewm(span=168, adjust=False).mean()

    # 72-Hour Coiled Squeeze Extremes (Core B)
    low_72h = l.shift(1).rolling(72, min_periods=24).min()
    high_72h = h.shift(1).rolling(72, min_periods=24).max()
    out['low_72h'] = low_72h
    out['high_72h'] = high_72h
    out['shelf_range_72h'] = (high_72h - low_72h) / (low_72h + 1e-8)
    out['dist_from_72h_low'] = (c - low_72h) / (low_72h + 1e-8)

    out['shelf_range_14d'] = (out['high_14d'] - out['low_14d']) / out['low_14d'].replace(0, np.nan)
    out['dist_from_60d_low'] = (c - out['low_60d']) / out['low_60d']
    out['ret_14d'] = c / c.shift(336) - 1.0
    out['ret_7d'] = c / c.shift(168) - 1.0
    out['breakout_21d'] = c > out['high_21d']

    # 3. Derivatives Tape & Turnover
    fr = out.get('funding_rate', pd.Series(0.0, index=out.index)).fillna(0.0)
    out['funding_rate'] = fr

    ls = out.get('count_toptrader_long_short_ratio', pd.Series(np.nan, index=out.index)).ffill()
    out['toptrader_ls'] = ls
    out['d_ls_24h'] = (ls / ls.shift(24) - 1.0).fillna(0.0)
    out['max_ls_7d'] = ls.shift(1).rolling(168, min_periods=24).max()

    oi_usd = out.get('sum_open_interest_value', pd.Series(np.nan, index=out.index)).ffill()
    out['oi_usd'] = oi_usd
    out['oi_change_14d'] = (oi_usd / oi_usd.shift(336) - 1.0).fillna(0.0)
    out['d_oi_usd_24h'] = (oi_usd / oi_usd.shift(24) - 1.0).fillna(0.0)

    # Token-Denominated Open Interest
    if 'sum_open_interest' in out.columns and out['sum_open_interest'].notna().any():
        oi_tok = out['sum_open_interest'].ffill()
    else:
        oi_tok = oi_usd / c
    out['oi_tokens'] = oi_tok
    out['d_oi_tokens_24h'] = (oi_tok / oi_tok.shift(24) - 1.0).fillna(0.0)
    out['d_close_24h'] = (c / c.shift(24) - 1.0).fillna(0.0)

    # Passive Absorption Taker Ratio
    if 'taker_buy_quote_volume' in out.columns and 'quote_volume' in out.columns:
        out['taker_ratio'] = (out['taker_buy_quote_volume'] / (out['quote_volume'] + 1e-6)).fillna(0.50)
    else:
        out['taker_ratio'] = 0.50

    # Core 3: Orderbook Turnover Velocity (24h volume USD / max(1e5, OI USD))
    vol_usd_24h = (v * c).rolling(24).sum()
    out['turnover_24h'] = vol_usd_24h / np.maximum(1e5, oi_usd)

    # Study S-Q: Point-in-Time Kyle-Lambda Price Impact & Percentile
    if 'taker_buy_quote_volume' in out.columns and 'quote_volume' in out.columns:
        from .sizing_v12 import compute_kyle_lambda_series, compute_pit_lambda_percentile
        lookback = getattr(cfg.sizing, 'lookback_bars', 72) if hasattr(cfg, 'sizing') else 72
        min_bars = getattr(cfg.sizing, 'history_min_bars', 2160) if hasattr(cfg, 'sizing') else 2160
        max_bars = getattr(cfg.sizing, 'history_max_bars', 8760) if hasattr(cfg, 'sizing') else 8760
        out['kyle_lambda'] = compute_kyle_lambda_series(c, out['quote_volume'], out['taker_buy_quote_volume'], lookback_bars=lookback)
        out['pct_lambda'] = compute_pit_lambda_percentile(out['kyle_lambda'], min_bars=min_bars, max_bars=max_bars).fillna(0.50)
    else:
        out['kyle_lambda'] = np.nan
        out['pct_lambda'] = 0.50

    # 4. Core 1: Macro Regime (BTC 200d EMA & 30d Return)
    if btc_df is not None and not btc_df.empty:
        btc_c = btc_df['close'].reindex(out.index).ffill()
        btc_ema_200d = btc_df['ema_200d'].reindex(out.index).ffill()
        btc_ret_30d = (btc_c / btc_c.shift(720) - 1.0).fillna(0.0)
        btc_ret_14d = (btc_c / btc_c.shift(336) - 1.0).fillna(0.0)

        out['btc_macro_bull'] = (btc_c > btc_ema_200d) & (btc_ret_30d > 0.0)
        out['rs_vs_btc'] = out['ret_14d'] - btc_ret_14d
        out['btc_dist_ema_200d'] = (btc_c - btc_ema_200d) / btc_ema_200d
        out['btc_ret_30d'] = btc_ret_30d
        out['btc_ath_pct'] = btc_df['btc_ath_pct'].reindex(out.index).ffill().fillna(1.0)
        out['days_below_ema'] = btc_df['days_below_ema'].reindex(out.index).ffill().fillna(0.0)
    else:
        out['btc_macro_bull'] = True
        out['rs_vs_btc'] = out['ret_14d']
        out['btc_dist_ema_200d'] = 0.0
        out['btc_ret_30d'] = 0.0
        out['btc_ath_pct'] = 1.0
        out['days_below_ema'] = 0.0

    out['tier'] = tier_label
    return out
