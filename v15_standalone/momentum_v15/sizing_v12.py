"""
Kronos V12: Kyle-Lambda Dynamic Position Sizing Overlay (sizing_v12.py)
Implements Clean-Room Study S-Q / Section 8 Adoption Bridge.

Pure side-effect-free mathematical estimators for orderbook price impact (Kyle's lambda),
point-in-time percentile ranking, and continuous allocation weights.
"""

from typing import Optional, Union
import numpy as np
import pandas as pd

from .config import SizingConfig


def compute_kyle_lambda_series(
    close: pd.Series,
    quote_volume: pd.Series,
    taker_buy_quote_volume: pd.Series,
    lookback_bars: int = 72,
) -> pd.Series:
    """
    Pure mathematical estimator for rolling Kyle's price impact lambda:
        lambda = Cov(r, q) / Var(q)
    where:
        r = ln(close_t / close_{t-1})
        q = (2 * taker_buy_quote_volume - quote_volume) / rolling_mean(quote_volume, lookback)
    """
    if len(close) < lookback_bars:
        return pd.Series(np.nan, index=close.index)

    # 1. Log returns
    r = np.log(close).diff()

    # 2. Normalized signed order flow
    qv_mean = quote_volume.rolling(lookback_bars, min_periods=lookback_bars).mean()
    flow_imb = 2.0 * taker_buy_quote_volume - quote_volume
    q = flow_imb / qv_mean.replace(0.0, np.nan)

    # 3. Rolling covariance & variance
    cov_rq = r.rolling(lookback_bars, min_periods=lookback_bars).cov(q)
    var_q = q.rolling(lookback_bars, min_periods=lookback_bars).var().replace(0.0, np.nan)

    lambda_series = cov_rq / var_q
    return lambda_series


def compute_pit_lambda_percentile(
    lambda_series: pd.Series,
    min_bars: int = 2160,
    max_bars: int = 8760,
) -> pd.Series:
    """
    Computes Point-in-Time percentile rank of Kyle's lambda relative to the asset's
    own trailing history (e.g. 1 year = 8760h, minimum 90d = 2160h).
    Returns values strictly in [0.0, 1.0].
    """
    if len(lambda_series) < min_bars:
        return pd.Series(np.nan, index=lambda_series.index)

    return lambda_series.rolling(max_bars, min_periods=min_bars).rank(pct=True)


def get_position_weight(
    pct_lambda: Union[float, np.ndarray, pd.Series],
    config: Optional[SizingConfig] = None,
) -> Union[float, np.ndarray, pd.Series]:
    """
    Calculates dynamic position sizing weight according to Study S-Q:
        w = clip(base_weight - pct_lambda, min_weight, max_weight)

    If sizing is disabled or pct_lambda is uncalibrated / NaN:
    - Disabled: returns 1.0 (exact production baseline reproduction)
    - Uncalibrated / NaN: defaults to pct_lambda = 0.50 -> w = 1.0
    """
    if config is None:
        config = SizingConfig()

    if not config.enable_lambda_sizing:
        if isinstance(pct_lambda, (pd.Series, np.ndarray)):
            return np.ones_like(pct_lambda, dtype=float)
        return 1.0

    if isinstance(pct_lambda, (float, int, np.floating)):
        val = 0.50 if np.isnan(pct_lambda) else float(pct_lambda)
        raw_w = config.base_weight - val
        return float(np.clip(raw_w, config.min_weight, config.max_weight))

    # Array / Series input
    arr = np.asarray(pct_lambda, dtype=float)
    clean_arr = np.where(np.isnan(arr), 0.50, arr)
    raw_w = config.base_weight - clean_arr
    res = np.clip(raw_w, config.min_weight, config.max_weight)
    if isinstance(pct_lambda, pd.Series):
        return pd.Series(res, index=pct_lambda.index)
    return res


def apply_sizing_overlay_to_trades(
    trades_df: pd.DataFrame,
    config: Optional[SizingConfig] = None,
) -> pd.DataFrame:
    """
    Applies the sizing overlay to a closed trades dataframe.
    Calculates weighted returns, log returns, and fee haircuts.
    """
    if config is None:
        config = SizingConfig()

    df = trades_df.copy()
    col = "pct_lam_a" if "pct_lam_a" in df.columns else ("pct_lam" if "pct_lam" in df.columns else None)
    
    if col is not None:
        pcts = df[col]
    else:
        pcts = pd.Series(0.50, index=df.index)

    weights = get_position_weight(pcts, config)
    df["sizing_weight"] = weights

    # Arithmetic return R = exp(log_ret) - 1
    if "log_ret" in df.columns:
        r_raw = np.expm1(df["log_ret"].values)
    elif "pnl" in df.columns:
        r_raw = df["pnl"].values
    else:
        r_raw = np.zeros(len(df))

    # Apply weight
    w_vals = df["sizing_weight"].values
    if config.enable_lambda_sizing and config.fee_haircut_bps > 0.0:
        excess = np.maximum(0.0, w_vals - 1.0)
        fee_penalty = 2.0 * (config.fee_haircut_bps / 10000.0) * excess
        weighted_r = w_vals * r_raw - fee_penalty
    else:
        weighted_r = w_vals * r_raw

    df["weighted_pnl"] = weighted_r
    df["weighted_log_ret"] = np.log1p(weighted_r)
    return df


def get_ema_position_weight(
    rank_ema: Union[float, np.ndarray, pd.Series],
    config: Optional[SizingConfig] = None,
) -> Union[float, np.ndarray, pd.Series]:
    """
    Study S-AY: Continuous 200-EMA Sizing Overlay:
        w_ema = clip(ema_base + ema_slope * rank_ema, ema_min, ema_max)
    """
    if config is None:
        config = SizingConfig()

    if not getattr(config, 'enable_ema_sizing', True):
        if isinstance(rank_ema, (pd.Series, np.ndarray)):
            return np.ones_like(rank_ema, dtype=float)
        return 1.0

    base = getattr(config, 'ema_base_multiplier', 0.75)
    slope = getattr(config, 'ema_slope_multiplier', 0.50)
    w_min = getattr(config, 'ema_min_multiplier', 0.75)
    w_max = getattr(config, 'ema_max_multiplier', 1.25)

    if isinstance(rank_ema, (float, int, np.floating)):
        val = 0.50 if np.isnan(rank_ema) else float(rank_ema)
        return float(np.clip(base + slope * val, w_min, w_max))

    arr = np.asarray(rank_ema, dtype=float)
    clean_arr = np.where(np.isnan(arr), 0.50, arr)
    res = np.clip(base + slope * clean_arr, w_min, w_max)
    if isinstance(rank_ema, pd.Series):
        return pd.Series(res, index=rank_ema.index)
    return res


def get_btc_macro_multiplier(
    btc_above_200d: Union[bool, np.ndarray, pd.Series],
    bear_mult: float = 0.50,
) -> Union[float, np.ndarray, pd.Series]:
    """
    Study S-BB Arm 2: Continuous BTC Macro Sizing:
        1.0x when BTC > 200d EMA (Bull Confluence)
        0.50x when BTC <= 200d EMA (Bear Defense)
    """
    if isinstance(btc_above_200d, (bool, int, np.bool_)):
        return 1.0 if bool(btc_above_200d) else bear_mult

    arr = np.asarray(btc_above_200d, dtype=bool)
    res = np.where(arr, 1.0, bear_mult)
    if isinstance(btc_above_200d, pd.Series):
        return pd.Series(res, index=btc_above_200d.index)
    return res


def compute_csmi_metrics(
    book: str,
    rank_ts: Union[float, pd.Series, np.ndarray],
    pct_lam: Union[float, pd.Series, np.ndarray],
    dist_ema: Union[float, pd.Series, np.ndarray],
    config: Optional[SizingConfig] = None,
) -> tuple[Union[float, pd.Series, np.ndarray], Union[float, pd.Series, np.ndarray], Union[float, pd.Series, np.ndarray]]:
    """
    Study S-BD: Computes the Compensatory Squeeze & Momentum Index (CSMI):
    Returns (csmi_score, csmi_prob, w_csmi).
    Supports both scalar and vectorized (pd.Series / np.ndarray) inputs.
    """
    if config is None:
        config = SizingConfig()

    is_series = isinstance(rank_ts, pd.Series) or isinstance(pct_lam, pd.Series) or isinstance(dist_ema, pd.Series)
    is_array = isinstance(rank_ts, np.ndarray) or isinstance(pct_lam, np.ndarray) or isinstance(dist_ema, np.ndarray)

    base = getattr(config, 'csmi_base_weight', 0.50)
    slope = getattr(config, 'csmi_slope_weight', 1.00)
    w_min = getattr(config, 'csmi_min_weight', 0.50)
    w_max = getattr(config, 'csmi_max_weight', 1.45)
    enable_sizing = getattr(config, 'enable_csmi_sizing', True)

    if not (is_series or is_array):
        r_ts = 0.50 if (rank_ts is None or pd.isna(rank_ts)) else float(rank_ts)
        r_lam = 0.50 if (pct_lam is None or pd.isna(pct_lam)) else float(pct_lam)
        d_ema = 0.0 if (dist_ema is None or pd.isna(dist_ema)) else float(dist_ema)

        z_ts = (r_ts - 0.50) / 0.288
        z_lam = (0.50 - r_lam) / 0.288

        if book == 'Book 1':
            z_ema = float(np.clip(d_ema / 0.20, -2.0, 2.0))
            s = 0.45 * z_ts + 0.35 * z_ema + 0.20 * z_lam
        elif book == 'Book 2':
            z_ema = float(np.clip(-d_ema / 0.20, -2.0, 2.0))
            s = 0.50 * z_ema + 0.35 * z_ts + 0.15 * z_lam
        else:
            s = 0.0

        prob = float(1.0 / (1.0 + np.exp(-s)))
        w_csmi = float(np.clip(base + slope * prob, w_min, w_max)) if enable_sizing else 1.0
        return s, prob, w_csmi

    # Vectorized path
    r_ts_arr = np.where(pd.isna(rank_ts), 0.50, np.asarray(rank_ts, dtype=float))
    r_lam_arr = np.where(pd.isna(pct_lam), 0.50, np.asarray(pct_lam, dtype=float))
    d_ema_arr = np.where(pd.isna(dist_ema), 0.0, np.asarray(dist_ema, dtype=float))

    z_ts = (r_ts_arr - 0.50) / 0.288
    z_lam = (0.50 - r_lam_arr) / 0.288

    if book == 'Book 1':
        z_ema = np.clip(d_ema_arr / 0.20, -2.0, 2.0)
        s = 0.45 * z_ts + 0.35 * z_ema + 0.20 * z_lam
    elif book == 'Book 2':
        z_ema = np.clip(-d_ema_arr / 0.20, -2.0, 2.0)
        s = 0.50 * z_ema + 0.35 * z_ts + 0.15 * z_lam
    else:
        s = np.zeros_like(r_ts_arr)

    prob = 1.0 / (1.0 + np.exp(-s))
    w_csmi = np.clip(base + slope * prob, w_min, w_max) if enable_sizing else np.ones_like(prob)

    if is_series:
        idx = rank_ts.index if isinstance(rank_ts, pd.Series) else (pct_lam.index if isinstance(pct_lam, pd.Series) else dist_ema.index)
        return pd.Series(s, index=idx), pd.Series(prob, index=idx), pd.Series(w_csmi, index=idx)

    return s, prob, w_csmi


