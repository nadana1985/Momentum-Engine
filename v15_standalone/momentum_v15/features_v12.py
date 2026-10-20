"""
Kronos V12: Feature Engineering & Context Synthesis Kernel
Calculates candlestick anatomy, orderbook turnover, exotic derivatives tape,
and 200-day BTC macro regime features.
"""

from pathlib import Path
from typing import Optional
import numpy as np
import pandas as pd

from momentum_v15.config import V12Config

_BTC_CACHE: Optional[pd.DataFrame] = None


def extract_p_nb_high(daily_df: pd.DataFrame, canary_date: pd.Timestamp, canary_close: float) -> tuple:
    """Study S-BZ: Extract P_NB_High point-in-time from daily green candles prior to canary date."""
    past_days = daily_df.loc[: canary_date - pd.Timedelta(days=1)]
    if len(past_days) < 10:
        return None, None, 0

    green_days = past_days[past_days['close'] > past_days['open']]
    macro_candidates = green_days[green_days['high'] > canary_close]
    if macro_candidates.empty:
        return None, None, 0

    macro_date = macro_candidates.index[-1]
    win_start = macro_date + pd.Timedelta(days=1)
    win_end = canary_date - pd.Timedelta(days=1)
    if win_start > win_end:
        return None, None, 0

    window_green = green_days.loc[win_start:win_end]
    if window_green.empty:
        return None, None, 0

    p_nb_high = float(window_green['high'].max())
    window_len = (win_end - win_start).days + 1
    return p_nb_high, macro_date, window_len


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
            # FIX: Use pyarrow schema read (zero data deserialization) instead of
            # loading the full parquet just to check column names. This eliminates
            # 652 redundant full-file reads per hourly run (~600 MB wasted I/O).
            try:
                import pyarrow.parquet as pq
                met_schema_names = pq.read_schema(str(met_path)).names
            except Exception:
                met_schema_names = list(pd.read_parquet(met_path, columns=['timestamp']).columns)
            if 'sum_open_interest' in met_schema_names:
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
    out['atr_24h'] = out['atr_24']
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

    # Dynamic Heuristic Pillars (Study S-CD / Rule 7)
    # Pillar 2: Whale L/S studentized log-odds Z-score and empirical percentile (rolling 720h)
    log_ls = np.log(np.maximum(1e-4, ls))
    ls_mean_720 = log_ls.rolling(720, min_periods=72).mean()
    ls_std_720 = log_ls.rolling(720, min_periods=72).std().replace(0, np.nan)
    out['z_ls_30d'] = ((log_ls - ls_mean_720) / ls_std_720).fillna(0.0)
    out['pct_ls_30d'] = (ls.rolling(720, min_periods=72).rank(pct=True) * 100.0).fillna(50.0)

    # Pillar 3: Funding rate 30d studentized Z-score and empirical percentile (rolling 720h)
    funding_ann = fr * 3 * 365 * 100.0
    fnd_mean_720 = funding_ann.rolling(720, min_periods=72).mean()
    fnd_std_720 = funding_ann.rolling(720, min_periods=72).std().replace(0, np.nan)
    out['z_fnd_30d'] = ((funding_ann - fnd_mean_720) / fnd_std_720).fillna(0.0)
    out['pct_fnd_30d'] = (funding_ann.rolling(720, min_periods=72).rank(pct=True) * 100.0).fillna(50.0)

    # Pillar 4: Studentized Token Open Interest Absorption (rolling 168h vol)
    d_oi = oi_tok.pct_change().fillna(0.0)
    oi_std_168 = d_oi.rolling(168, min_periods=24).std().replace(0, np.nan)
    oi_exp_12h = (oi_tok / oi_tok.shift(12) - 1.0).fillna(0.0) * 100.0
    out['z_oi_12h'] = (oi_exp_12h / (oi_std_168 * 100.0 * np.sqrt(12.0) + 1e-8)).fillna(0.0)

    # Study S-CE: The 6 Climax Exhaustion Signatures & Dynamic 24h VWAP
    body_top = np.maximum(o, c)
    upper_wick = ((h - body_top) / np.maximum(1e-6, h - l)).fillna(0.0)
    out['upper_wick_ratio'] = upper_wick

    vol_quote = out['quote_volume'] if 'quote_volume' in out.columns else (c * v)
    vol_peak_24h = vol_quote.rolling(24, min_periods=12).max()
    out['d_vol_peak_24h'] = ((vol_quote - vol_peak_24h) / np.maximum(1e-5, vol_peak_24h)).fillna(0.0)

    oi_tok_peak_24h = oi_tok.rolling(24, min_periods=12).max()
    d_oi_nominal = ((oi_tok - oi_tok_peak_24h) / np.maximum(1e-5, oi_tok_peak_24h)).fillna(0.0)
    out['d_oi_tok_peak_24h'] = d_oi_nominal

    # Study S-CG: Studentized Orderflow Volatility and Peak Drawdown (Rule 7 Certified)
    sigma_oi_168h = d_oi.rolling(168, min_periods=24).std().replace(0, np.nan)
    sigma_oi_24h = (sigma_oi_168h * np.sqrt(24.0)).replace(0, np.nan)
    out['z_delta_oi_24h'] = (d_oi_nominal / sigma_oi_24h).fillna(0.0)
    out['sigma_oi_168h'] = sigma_oi_168h.fillna(0.01)

    out['funding_min_24h'] = fr.rolling(24, min_periods=12).min().fillna(0.0)
    out['ls_min_24h'] = ls.rolling(24, min_periods=12).min().fillna(1.0)
    out['d_ls_6h'] = (ls - ls.shift(6)).fillna(0.0)

    pv_24h = (c * vol_quote).rolling(24, min_periods=12).sum()
    v_24h = vol_quote.rolling(24, min_periods=12).sum()
    out['vwap_24h'] = (pv_24h / np.maximum(1e-5, v_24h)).fillna(c)

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

    # Study S-AW / S-AX: Point-in-Time Institutional Ticket Size & Percentile Rank (Canonical Production V12.4)
    qv = out['quote_volume'] if 'quote_volume' in out.columns else (c * v)
    cnt = out['count'] if 'count' in out.columns else pd.Series(1.0, index=out.index)
    ts_s = qv / np.maximum(1.0, cnt)
    out['ticket_size'] = ts_s
    ts_lookback = getattr(cfg.sizing, 'ts_lookback_bars', 168) if hasattr(cfg, 'sizing') else 168
    out['rank_ts_168h'] = ts_s.rolling(ts_lookback + 1, min_periods=24).rank(pct=True).fillna(0.50)

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

    # 5. Study S-AY & S-BB & S-BZ: Multi-Timeframe EMA Convergence & Two-Tier Reference Levels
    ema200_1d = c.ewm(span=4800, adjust=False).mean()
    out['ema200_1d'] = ema200_1d
    out['ema500_1d'] = c.ewm(span=12000, adjust=False).mean() # Study S-BZ: 500-Day EMA Overhead Target Ceiling
    out['oi_rolling_90d_high'] = oi_usd.rolling(2160, min_periods=168).max() # Study S-BZ: Peak OI Saturation
    out['ema200_1h'] = c.ewm(span=200, adjust=False).mean()
    out['ema200_4h'] = c.ewm(span=800, adjust=False).mean()
    out['sma200_1d'] = c.rolling(4800, min_periods=720).mean()
    out['nov25_low'] = l.shift(1).rolling(4800, min_periods=720).min()
    out['is_leading'] = (c >= ema200_1d) & (out['ema200_1h'] >= out['ema200_4h'])

    # Study S-AY: Continuous 200-EMA Sizing Rank (Percentile Rank over trailing 168h)
    ema_gap = (c - ema200_1d) / (ema200_1d + 1e-8)
    out['rank_ema_168h'] = ema_gap.rolling(168 + 1, min_periods=24).rank(pct=True).fillna(0.50)

    # Study S-BB: 200-Day EMA Touch & Retest Tracking Features
    below_ema_int = (c < ema200_1d).astype(int)
    grp_id = (below_ema_int == 0).cumsum()
    bars_bel = below_ema_int.groupby(grp_id).cumsum()
    out['bars_below_ema200_1d'] = bars_bel
    touch_tol = getattr(cfg.book4, 'touch_tolerance_pct', 0.015) if hasattr(cfg, 'book4') else 0.015
    min_bel = getattr(cfg.book4, 'min_bars_below', 720) if hasattr(cfg, 'book4') else 720
    out['is_200d_touch'] = (h >= ema200_1d * (1.0 - touch_tol)) & (bars_bel.shift(1) >= min_bel)

    # 6. V13.0 / Study S-BR: Regime Dormancy Engine Features
    log_c_f = np.log(np.maximum(1e-8, c))
    r_1h_f = log_c_f.diff().fillna(0.0)
    rv_24_f = (np.sqrt(24.0) * r_1h_f.rolling(24, min_periods=12).std()).fillna(0.0)
    max_h_24_f = h.rolling(24, min_periods=12).max()
    min_l_24_f = l.rolling(24, min_periods=12).min()
    r_24_f = ((max_h_24_f - min_l_24_f) / (c + 1e-8)).fillna(0.0)
    q_log_f = np.log(1.0 + np.maximum(0.0, out['quote_volume'] if 'quote_volume' in out.columns else (c * v)))

    dorm_lookback = min(4320, len(df))
    p_rv_f = rv_24_f.rolling(dorm_lookback, min_periods=96).rank(pct=True).fillna(0.50)
    p_r_f = r_24_f.rolling(dorm_lookback, min_periods=96).rank(pct=True).fillna(0.50)
    p_q_f = q_log_f.rolling(dorm_lookback, min_periods=96).rank(pct=True).fillna(0.50)

    dorm_score = 1.0 - (0.45 * p_rv_f + 0.35 * p_r_f + 0.20 * p_q_f)
    out['dormancy_score'] = dorm_score
    out['dorm_72h_mean'] = dorm_score.shift(1).rolling(72, min_periods=24).mean().fillna(0.50)

    # Funding 90d rolling z-score for microstructure protection
    fr_mean_f = fr.rolling(2160, min_periods=168).mean()
    fr_std_f = fr.rolling(2160, min_periods=168).std().replace(0, np.nan).fillna(1e-5)
    out['funding_z'] = ((fr - fr_mean_f) / fr_std_f).fillna(0.0)

    # 7. V13.2 / Study S-BP & Study S-BY: CUSUM & Base Features
    # CUSUM accumulation series (window=168, k=0.5)
    r_series = r_1h_f.values
    r_mean = pd.Series(r_series).rolling(168, min_periods=84).mean().values
    r_std = pd.Series(r_series).rolling(168, min_periods=84).std().values
    r_std = np.where(r_std < 1e-6, 1e-6, r_std)
    z_ret = np.nan_to_num((r_series - r_mean) / r_std, nan=0.0)
    s_pos = np.zeros(len(r_series), dtype=np.float64)
    s_neg_168 = np.zeros(len(r_series), dtype=np.float64)
    for i in range(1, len(r_series)):
        s_pos[i] = max(0.0, s_pos[i-1] + (z_ret[i] - 0.50))
        s_neg_168[i] = max(0.0, s_neg_168[i-1] - z_ret[i] - 0.50)
    out['cusum_usdt'] = s_pos
    out['cusum_neg_168'] = s_neg_168

    # Study S-BY: Upside Ignition CUSUM (72h window, k=0.5)
    r_mean_72 = pd.Series(r_series).rolling(72, min_periods=36).mean().values
    r_std_72 = pd.Series(r_series).rolling(72, min_periods=36).std().values
    r_std_72 = np.where(r_std_72 < 1e-6, 1e-6, r_std_72)
    z_ret_72 = np.nan_to_num((r_series - r_mean_72) / r_std_72, nan=0.0)
    s_pos_72 = np.zeros(len(r_series), dtype=np.float64)
    for i in range(1, len(r_series)):
        s_pos_72[i] = max(0.0, s_pos_72[i-1] + (z_ret_72[i] - 0.50))
    out['cusum_pos_72'] = s_pos_72

    # Study S-BY: ALT/BTC Price, 200d EMA, and CUSUM Momentum
    if btc_df is not None and not btc_df.empty:
        btc_c_s = btc_df['close'].reindex(out.index).ffill()
        alt_btc_s = (c / np.maximum(1e-8, btc_c_s)).fillna(0.0)
        out['alt_btc'] = alt_btc_s
        out['ema200_btc'] = alt_btc_s.ewm(span=4800, adjust=False).mean()

        r_btc_s = np.log(np.maximum(1e-8, alt_btc_s)).diff().fillna(0.0).values
        r_mean_btc = pd.Series(r_btc_s).rolling(168, min_periods=84).mean().values
        r_std_btc = pd.Series(r_btc_s).rolling(168, min_periods=84).std().values
        r_std_btc = np.where(r_std_btc < 1e-6, 1e-6, r_std_btc)
        z_btc = np.nan_to_num((r_btc_s - r_mean_btc) / r_std_btc, nan=0.0)
        s_pos_btc = np.zeros(len(r_btc_s), dtype=np.float64)
        for i in range(1, len(r_btc_s)):
            s_pos_btc[i] = max(0.0, s_pos_btc[i-1] + (z_btc[i] - 0.50))
        out['cusum_pos_btc'] = s_pos_btc
    else:
        out['alt_btc'] = 1.0
        out['ema200_btc'] = 1.0
        out['cusum_pos_btc'] = s_pos

    # 30-day base in 90-day cycle low
    low_90d = l.rolling(2160, min_periods=720).min()
    dist_to_90d_low = ((c - low_90d) / np.maximum(low_90d, 1e-6)).fillna(1.0)
    out['dist_to_90d_low'] = dist_to_90d_low
    is_base = dist_to_90d_low < getattr(cfg.book6, 'cycle_base_max_dist', 0.40)
    out['base_30d'] = is_base.rolling(720, min_periods=720).min() == 1.0
    out['high_30d'] = h.shift(1).rolling(720, min_periods=720).max()
    out['is_b6_breakout'] = (h >= out['high_30d']) & out['base_30d'].shift(1).fillna(False)

    # Study S-BZ: Pre-calculate daily candles for causal P_NB_High extraction
    try:
        daily_c = c.resample('1D').last().dropna()
        daily_o = o.resample('1D').first().dropna()
        daily_h = h.resample('1D').max().dropna()
        daily_l = l.resample('1D').min().dropna()
        out.attrs['daily_df'] = pd.DataFrame({'open': daily_o, 'high': daily_h, 'low': daily_l, 'close': daily_c})
    except Exception:
        out.attrs['daily_df'] = None

    out['tier'] = tier_label
    return out
