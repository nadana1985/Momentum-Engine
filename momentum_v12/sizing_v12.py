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
