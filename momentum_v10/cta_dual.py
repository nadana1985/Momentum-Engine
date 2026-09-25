# -*- coding: utf-8 -*-
import argparse
from pathlib import Path
import pandas as pd
import numpy as np

from momentum_v10.features import load_asset, enrich
from momentum_v10.config import (
    CtaConfig,
    FeatureConfig,
    ROOT,
    SHARD_DIR,
    DONCHIAN_ARM_MFE,
    DONCHIAN_BARS,
    DONCHIAN_COL,
    DONCHIAN_ENGINE,
)
from momentum_v10.fd_ofi import compute_fd_ofi_kernel

SLIPPAGE = 0.0020
MAX_CONCURRENT = 1
_BTC_CACHE = None
_L5_CACHE = None

def get_hill_estimator(rets):
    pos_rets = rets[rets > 0].dropna()
    if len(pos_rets) < 10: return 5.0
    k = max(int(len(pos_rets) * 0.10), 3)
    sorted_rets = np.sort(pos_rets.values)[::-1]
    tail = sorted_rets[:k]
    u = sorted_rets[k]
    if u <= 0: return 5.0
    log_ratios = np.log(tail / u)
    if np.sum(log_ratios) == 0: return 5.0
    return k / np.sum(log_ratios)

def compute_features(df: pd.DataFrame, fcfg: FeatureConfig, asset: str = '') -> pd.DataFrame:
    global _BTC_CACHE
    if _BTC_CACHE is None:
        try:
            btc_path = SHARD_DIR / 'BTC_USDT_1h.parquet'
            if btc_path.exists():
                _BTC_CACHE = pd.read_parquet(btc_path, columns=['timestamp', 'close'])
                _BTC_CACHE['timestamp'] = pd.to_datetime(_BTC_CACHE['timestamp'], unit='ms')
                _BTC_CACHE.set_index('timestamp', inplace=True)
                _BTC_CACHE['btc_ret'] = _BTC_CACHE['close'].pct_change()
                _BTC_CACHE = _BTC_CACHE[['btc_ret']]
            else:
                _BTC_CACHE = pd.DataFrame()
        except Exception:
            _BTC_CACHE = pd.DataFrame()
    out = enrich(df, fcfg)
    if 'taker_ratio' in out.columns:
        out['taker_ratio_mean'] = out['taker_ratio'].rolling(720, min_periods=24).mean()
        out['taker_ratio_std'] = out['taker_ratio'].rolling(720, min_periods=24).std()
        out['is_3sigma_taker'] = out['taker_ratio'] > (out['taker_ratio_mean'] + 3 * out['taker_ratio_std'])
    else:
        out['is_3sigma_taker'] = False

    global _L5_CACHE
    if _L5_CACHE is None:
        l5_path = None if fcfg.l5_ranking_path is None else Path(fcfg.l5_ranking_path)
        if l5_path is not None and not l5_path.is_absolute():
            l5_path = ROOT / l5_path
        if l5_path is None or not l5_path.exists():
            _L5_CACHE = pd.DataFrame()
        else:
            try:
                _L5_CACHE = pd.read_parquet(l5_path)
                _L5_CACHE['date_dt'] = pd.to_datetime(_L5_CACHE['date'])
                _L5_CACHE['asset_norm'] = _L5_CACHE['symbol'].str.replace('USDT', '')
                _L5_CACHE = _L5_CACHE.sort_values('date_dt')
                _L5_CACHE['rank_pctile'] = _L5_CACHE.groupby('date_dt')['rank'].rank(pct=True)
            except Exception:
                _L5_CACHE = pd.DataFrame()

    out['l5_rank_pctile'] = np.nan
    if _L5_CACHE is not None and not _L5_CACHE.empty and asset:
        asset_norm = asset.replace("1000000", "").replace("1000", "")
        asset_ranks = _L5_CACHE[_L5_CACHE['asset_norm'] == asset_norm].copy()
        if not asset_ranks.empty:
            out_dates = pd.DataFrame({'timestamp': out.index})
            out_dates['timestamp'] = out_dates['timestamp'].astype('datetime64[ns]')
            asset_ranks['date_dt'] = asset_ranks['date_dt'].astype('datetime64[ns]')
            merged = pd.merge_asof(out_dates, asset_ranks[['date_dt', 'rank_pctile']], left_on='timestamp', right_on='date_dt', direction='backward')
            merged.index = out.index
            out['l5_rank_pctile'] = merged['rank_pctile']
            

    out['asset_ret'] = out['close'].pct_change()
    if _BTC_CACHE is not None and not _BTC_CACHE.empty:
        joined = out[['asset_ret']].join(_BTC_CACHE, how='left')
        out['btc_corr'] = joined['asset_ret'].rolling(window=720, min_periods=300).corr(joined['btc_ret'])
    else:
        out['btc_corr'] = 0.0
    out['is_idiosyncratic'] = out['btc_corr'].fillna(0.0) < 0.50

    # --- FDOFI ---
    if 'taker_buy_base_volume' in out.columns and 'volume' in out.columns:
        tbv = out['taker_buy_base_volume'].fillna(0).values
        tsv = out['volume'].fillna(0).values - tbv
        ofi = tbv - tsv
        W_t = np.full(len(ofi), 100, dtype=np.float64)
        eps = np.full(len(ofi), 1e-8, dtype=np.float64)
        out['fd_ofi'] = compute_fd_ofi_kernel(ofi.astype(np.float64), W_t, eps, 0.45)
        out['has_long_memory_accumulation'] = out['fd_ofi'] > 0
    else:
        out['has_long_memory_accumulation'] = True

    
    out['sma_200'] = out['close'].shift(1).rolling(200, min_periods=24).mean()
    out['is_uptrend'] = out['close'] > out['sma_200']
    
    # True Dynamic Fix: Strictly Shifted for Causality
    out['avg_candle_size'] = ((out['high'] - out['low']) / out['close']).shift(1).rolling(720, min_periods=24).mean()
    out['oi_change_p90'] = out['oi_change'].shift(1).rolling(720, min_periods=24).quantile(0.90)
    
    current_candle_size = (out['high'] - out['low']) / out['low']
    
    # Pre-move extension normalized by 24h ATR (strictly causal shifted)
    out['ret_4h_pre'] = (out['close'].shift(1) - out['close'].shift(5)) / out['close'].shift(5)
    tr = np.maximum(
        out['high'] - out['low'],
        np.maximum(
            abs(out['high'] - out['close'].shift(1)),
            abs(out['low'] - out['close'].shift(1))
        )
    )
    out['atr_24h_pct'] = tr.shift(1).rolling(24, min_periods=24).mean() / out['close'].shift(1)
    out['ext_mult'] = out['ret_4h_pre'] / out['atr_24h_pct'].replace(0, np.nan)
    
    if 'topLongShortAccountRatio' in out.columns:
        ls_p05 = out['topLongShortAccountRatio'].shift(1).rolling(720, min_periods=24).quantile(0.05)
        is_dropping = out['topLongShortAccountRatio'].diff(1) < 0
        out['whale_trap'] = (out['topLongShortAccountRatio'] < ls_p05) & is_dropping
    else:
        out['whale_trap'] = False
        
    if 'funding_rate' in out.columns:
        out['funding_p99'] = out['funding_rate'].shift(1).rolling(720, min_periods=24).quantile(0.99)
        out['is_overheated'] = (out['funding_rate'] > out['funding_p99']) & (out['funding_rate'] > 0.0001)
        out['funding_delta'] = out['funding_rate'].diff()
        out['funding_accelerating_negative'] = (out['funding_rate'] < 0) & (out['funding_delta'] < 0)
    else:
        out['funding_p99'] = 0.0
        out['is_overheated'] = False
        out['funding_delta'] = 0.0
        out['funding_accelerating_negative'] = False

    # --- Signal 1: Institutional Flow (trade count → avg trade size > P90 baseline) ---
    # Filters out retail FOMO shocks. A 25x volume spike from 12 whale blocks
    # is categorically different from 200,000 retail market orders.
    if 'count' in out.columns:
        count_safe = out['count'].replace(0, float('nan'))
        out['avg_trade_size'] = out['volume'] / count_safe
        out['avg_trade_size_p90_30d'] = (
            out['avg_trade_size'].shift(1).rolling(720, min_periods=24).quantile(0.90)
        )
        out['is_institutional_flow'] = out['avg_trade_size'] > out['avg_trade_size_p90_30d']
    else:
        out['is_institutional_flow'] = True  # count absent → gate disabled (graceful)

    # --- Signal 2: USD-denominated OI change (cross-asset normalised exhaustion) ---
    # sum_open_interest_value is in USD, making the blow-off exit comparable across
    # low-cap and high-cap assets without being distorted by contract sizing.
    if 'sum_open_interest_value' in out.columns:
        out['oi_value_change'] = out['sum_open_interest_value'].pct_change()
    else:
        out['oi_value_change'] = out.get('oi_change', pd.Series(0.0, index=out.index))

    # --- Signal 3: Quote-denominated taker aggression (USD taker flow) ---
    # taker_buy_quote_volume / quote_volume is more stable across assets of different
    # price scales than the base-token ratio. OR logic: either measure firing is enough.
    if 'taker_buy_quote_volume' in out.columns and 'quote_volume' in out.columns:
        quote_vol_safe = out['quote_volume'].replace(0, float('nan'))
        out['taker_quote_ratio'] = out['taker_buy_quote_volume'] / quote_vol_safe
        out['p50_taker_quote_30d'] = (
            out['taker_quote_ratio'].shift(1).rolling(720, min_periods=720).median()
        )
        out['is_aggressive_flow_quote'] = (
            out['taker_quote_ratio'] > (out['p50_taker_quote_30d'] + fcfg.taker_buffer)
        )
    else:
        out['is_aggressive_flow_quote'] = out['is_aggressive_flow']

    # --- Macro Toxicity Z-Score (The Rubber Band) ---
    if 'fd_ofi' in out.columns:
        # Calculate 30-day (720h) rolling sum to represent 'monthly flow'
        out['rolling_30d_fdofi'] = out['fd_ofi'].rolling(720, min_periods=720).sum()
        # Historical Mean and Std of monthly flow
        out['hist_mean_30d'] = out['rolling_30d_fdofi'].expanding().mean()
        out['hist_std_30d'] = out['rolling_30d_fdofi'].expanding().std()
        
        # 90-day (2160h) average monthly flow
        out['recent_3m_avg_monthly'] = out['fd_ofi'].rolling(2160, min_periods=720).mean() * 720
        
        # Z-Score of current 3-month flow vs historical 30-day norm
        out['macro_z_score'] = (out['recent_3m_avg_monthly'] - out['hist_mean_30d']) / out['hist_std_30d'].replace(0, np.nan)
        out['is_toxic_distribution'] = out['macro_z_score'].fillna(0.0) < -1.5
    else:
        out['is_toxic_distribution'] = False

    out['continuation_long'] = (
        out['is_uptrend'] &
        out['breakout'] &
        (out['is_aggressive_flow'] | out['is_aggressive_flow_quote']) &  # Signal 3: OR (more fills)
        out['is_institutional_flow'] &                                    # Signal 1: whale confirmation
        (current_candle_size > (out['avg_candle_size'] * 2.5)) &
        (out['oi_change'] > out['oi_change_p90']) &
        (~out['whale_trap']) &
        (~out['is_overheated'])
    )

    if 'topLongShortAccountRatio' in out.columns:
        out['retail_squeeze_long'] = (
            out['is_uptrend'] &
            out['breakout'] &
            (out['is_aggressive_flow'] | out['is_aggressive_flow_quote']) & 
            (~out['is_institutional_flow']) &  # Proves it is retail, not whales
            (out['topLongShortAccountRatio'] < 1.0) &  # Top traders are net short
            (out['oi_change'] < -0.05) &  # >5% OI destruction (Liquidations)
            (~out['is_overheated'])
        )
    else:
        out['retail_squeeze_long'] = False

    # V10.2 freeze: 21d causal floor. Column name kept for live-state compatibility.
    out[DONCHIAN_COL] = out['low'].shift(1).rolling(DONCHIAN_BARS, min_periods=24).min()
    out['hill_estimator'] = 5.0
    idx_retail = out[out['retail_squeeze_long'] == True].index
    for idx in idx_retail:
        pos = out.index.get_loc(idx)
        start = max(0, pos - 720)
        if start < pos:
            rets = out['asset_ret'].iloc[start:pos]
            out.loc[idx, 'hill_estimator'] = get_hill_estimator(rets)
    out['retail_squeeze_long'] = out['retail_squeeze_long'] & (out['hill_estimator'] <= 2.5)

    # --- OVERSOLD SQUEEZE TRIGGER ---
    if 'fd_ofi' in out.columns:
        out['fd_ofi_168_mean'] = out['fd_ofi'].rolling(168, min_periods=24).mean()
        out['fd_ofi_168_std'] = out['fd_ofi'].rolling(168, min_periods=24).std()
        
        out['oversold_squeeze_long'] = (
            out['is_toxic_distribution'] &
            (out['fd_ofi'] > (out['fd_ofi_168_mean'] + 3.0 * out['fd_ofi_168_std'])) &
            (~out['is_overheated'])
        )
    else:
        out['oversold_squeeze_long'] = False

    # --- Macro Base Context (Strictly Causal Shifted 90d Baseline) ---
    base_bars = 2160
    low_90d = out['low'].shift(1).rolling(base_bars, min_periods=720).min()
    high_90d = out['high'].shift(1).rolling(base_bars, min_periods=720).max()
    out['macro_low_mult'] = np.where(
        low_90d.isna() | (low_90d <= 0),
        1.0,
        out['close'] / low_90d
    )
    denom = high_90d - low_90d
    out['base_percentile'] = np.where(
        denom.isna() | (denom <= 0),
        0.5,
        (out['close'] - low_90d) / denom
    )
    out['is_early_stage'] = (out['macro_low_mult'] <= 2.0) | (out['base_percentile'] <= 0.60)

    return out
    

def _as_timestamp(value):
    """JSON state stores times as text. Subtraction needs a timestamp."""
    if isinstance(value, str):
        return pd.to_datetime(value)
    return value


def step_cta(ts, row, state_dict, cfg, asset=""):
    SLIPPAGE = getattr(cfg, 'slippage', 0.0020)
    MAX_CONCURRENT = 1
    
    completed_trades = []
    active = state_dict.get("active_trades", [])
    pw = state_dict.get("phoenix_watch", [])
    armed_countdown = state_dict.get("armed_countdown", 0)
    armed_shock = state_dict.get("armed_shock", 0.0)
    armed_hard_stop = state_dict.get("armed_hard_stop", 0.0)
    
    curr_close = float(row["close"])
    curr_high = float(row["high"])
    curr_low = float(row["low"])
    curr_shock = float(row.get("shock_mult", 0.0))
    upper_wick = float(row.get("upper_wick_ratio", 0.0))
    curr_oi_val = float(row.get("oi_value_change", float("nan")))
    
    is_idio = bool(row.get("is_idiosyncratic", False))
    is_inst = bool(row.get("is_institutional_flow", False))
    is_accum = bool(row.get("has_long_memory_accumulation", False))
    is_early = bool(row.get("is_early_stage", False))
    is_parabolic = bool(row.get("funding_rate", 0.0) > row.get("funding_p99", 999.0))
    is_toxic = bool(row.get("is_toxic_distribution", False))
    is_deadcat = bool(row.get("regime_dead_cat", False))

    still_active = []
    for t in active:
        exit_triggered = False
        exit_price = 0.0
        exit_reason = ""
        
        t["trade_max_high"] = max(t["trade_max_high"], curr_high)
        t["trade_min_low"] = min(t["trade_min_low"], curr_low)
        
        if "SQZ" in t["engine"] or "SQUEEZE" in t["engine"]:
            if is_toxic or is_deadcat:
                exit_price = curr_close * (1 - SLIPPAGE); exit_triggered = True; exit_reason = "regime_bailout"
            elif curr_close < t["entry_price"] * 0.80:
                exit_price = curr_close * (1 - SLIPPAGE); exit_triggered = True; exit_reason = "20pct_hard_stop"
            elif t["trade_max_high"] > t["entry_price"] * 1.05 and curr_close < t["trade_max_high"] * 0.75:
                exit_price = curr_close * (1 - SLIPPAGE); exit_triggered = True; exit_reason = "25pct_trailing_stop"
        else:
            # Donchian 21d floor: CONTINUATION only. pit_study 2026-09-20: rise-veto
            # and early-path flatten both failed validation. Do not extend to
            # IGNITION / PHOENIX. Do not replace with a peak-% trail.
            donchian_engine = getattr(cfg, 'donchian_engine', DONCHIAN_ENGINE)
            donchian_arm = getattr(cfg, 'donchian_arm_mfe', DONCHIAN_ARM_MFE)
            if t["engine"] == donchian_engine:
                mfe = (t["trade_max_high"] - t["entry_price"]) / t["entry_price"]
                working_stop = t["hard_stop"]
                t["donchian_stop"] = t.get("donchian_stop", 0.0)
                
                if mfe >= donchian_arm:
                    donchian = float(row.get(DONCHIAN_COL, 0.0))
                    if pd.notna(donchian) and donchian > 0:
                        t["donchian_stop"] = max(t["donchian_stop"], donchian)
                        
                working_stop = max(working_stop, t["donchian_stop"])
                
                if curr_close < working_stop and not is_parabolic:
                    exit_price = curr_close * (1 - SLIPPAGE)
                    exit_triggered = True
                    exit_reason = "donchian_trail" if working_stop == t["donchian_stop"] and t["donchian_stop"] > t["hard_stop"] else "structural_stop"
                
                can_exhaust = (mfe >= 0.15) or (not is_early)
                if not exit_triggered and can_exhaust and curr_shock > 3.0 and upper_wick > 0.40 and curr_oi_val < 0.0:
                    exit_price = curr_close * (1 - SLIPPAGE)
                    exit_triggered = True
                    exit_reason = "exhaustion"
            else:
                if is_toxic:
                    if t["trade_max_high"] > t["entry_price"] * 1.05 and curr_close < t["trade_max_high"] * 0.75:
                        exit_price = t["trade_max_high"] * 0.75; exit_triggered = True; exit_reason = "toxic_trail"
                    elif curr_close < t["entry_price"] * 0.80:
                        exit_price = curr_close * (1 - SLIPPAGE); exit_triggered = True; exit_reason = "toxic_hard"
                else:
                    if curr_close < t["hard_stop"] and not is_parabolic:
                        exit_price = curr_close * (1 - SLIPPAGE); exit_triggered = True; exit_reason = "structural_stop"
                    mfe = (t["trade_max_high"] - t["entry_price"]) / t["entry_price"]
                    can_exhaust = (mfe >= 0.15) or (not is_early)
                    if not exit_triggered and can_exhaust and curr_shock > 3.0 and upper_wick > 0.40 and curr_oi_val < 0.0:
                        exit_price = curr_close * (1 - SLIPPAGE); exit_triggered = True; exit_reason = "exhaustion"
                
        if exit_triggered:
            pnl = (exit_price - t["entry_price"]) / t["entry_price"]
            dur = (ts - _as_timestamp(t["entry_time"])).total_seconds() / 3600.0
            completed_trades.append(dict(asset=asset, entry=t["entry_time"], exit=ts, duration_hours=dur,
                entry_price=t["entry_price"], exit_price=exit_price, pnl=pnl,
                mae=(t["trade_min_low"] - t["entry_price"]) / t["entry_price"],
                mfe=(t["trade_max_high"] - t["entry_price"]) / t["entry_price"],
                reason=exit_reason, engine=t["engine"]))
                
            if exit_reason == 'structural_stop' and not t['engine'].startswith('PHOENIX_'):
                pw.append({
                    'original_entry_price': t['entry_price'],
                    'exit_ts': ts,
                    'original_engine': t['engine']
                })
        else:
            still_active.append(t)
            
    active = still_active
    
    still_watching = []
    for w in pw:
        if (ts - _as_timestamp(w['exit_ts'])).total_seconds() <= (336 * 3600):
            still_watching.append(w)
    pw = still_watching

    if armed_countdown > 0:
        if curr_close < armed_hard_stop: armed_countdown = 0
        else: armed_countdown -= 1
        
    if bool(row.get("hyper_ignition", False)):
        armed_countdown = 12; armed_shock = curr_shock; armed_hard_stop = curr_low

    entry_exec = curr_close * (1 + SLIPPAGE)
    is_whale_trap = bool(row.get("whale_trap", False))
    is_squeeze = float(row.get("funding_rate", 0.0)) < 0.0

    regime_is_trap = (
        bool(row.get("is_toxic_distribution", False)) or
        bool(row.get("regime_euphoria", False)) or
        bool(row.get("regime_dead_cat", False))
    )

    oi_p90 = row.get("oi_change_p90", np.nan)
    curr_oi_change = float(row.get("oi_change", float("nan")))
    is_ext = float(row.get("ext_mult", 0.0)) > 2.0
    is_conf = True
    if pd.notna(curr_oi_change) and pd.notna(oi_p90) and oi_p90 > 0:
        is_conf = curr_oi_change >= (oi_p90 * 0.8)
    is_exhaust_trap = is_ext and not is_conf

    if not regime_is_trap and len(active) < MAX_CONCURRENT:
        phoenix_triggered = False
        for w in list(pw):
            if curr_close > w['original_entry_price']:
                if bool(row.get('is_aggressive_flow', False)) and is_idio and is_accum:
                    hs = entry_exec * 0.80 if ("SQZ" in w['original_engine'] or "SQUEEZE" in w['original_engine']) else curr_low
                    active.append({
                        'entry_time': ts, 'entry_price': entry_exec, 'hard_stop': hs,
                        'trade_max_high': entry_exec, 'trade_min_low': entry_exec,
                        'engine': f"PHOENIX_{w['original_engine']}"
                    })
                    pw.remove(w)
                    phoenix_triggered = True
                    break
                    
        if not phoenix_triggered:
            if (armed_countdown > 0 and bool(row.get("is_aggressive_flow", False))
                    and not is_whale_trap and not is_exhaust_trap
                    and is_inst and is_idio and is_accum
                    and upper_wick <= 0.65 and not is_squeeze):
                active.append({"entry_time": ts, "entry_price": entry_exec, "hard_stop": armed_hard_stop,
                    "trade_max_high": entry_exec, "trade_min_low": entry_exec, "engine": "IGNITION"})
                armed_countdown = 0

            if (armed_countdown > 0 and bool(row.get("is_aggressive_flow", False))
                    and not is_whale_trap and not is_exhaust_trap
                    and is_inst and is_idio and is_accum
                    and upper_wick <= 0.65 and is_squeeze):
                if bool(row.get("funding_accelerating_negative", False)) or bool(row.get("is_3sigma_taker", False)):
                    active.append({"entry_time": ts, "entry_price": entry_exec, "hard_stop": entry_exec * 0.80,
                        "trade_max_high": entry_exec, "trade_min_low": entry_exec, "engine": "SQUEEZE_IGN"})
                    armed_countdown = 0

            if (bool(row.get("continuation_long", False)) and is_idio and is_accum):
                active.append({"entry_time": ts, "entry_price": entry_exec, "hard_stop": curr_low,
                    "trade_max_high": entry_exec, "trade_min_low": entry_exec, "engine": "CONTINUATION"})

            if (bool(row.get("retail_squeeze_long", False)) and is_idio and is_accum):
                active.append({"entry_time": ts, "entry_price": entry_exec, "hard_stop": entry_exec * 0.80,
                    "trade_max_high": entry_exec, "trade_min_low": entry_exec, "engine": "RETAIL_SQZ"})

    state_dict["active_trades"] = active
    state_dict["phoenix_watch"] = pw
    state_dict["armed_countdown"] = armed_countdown
    state_dict["armed_shock"] = armed_shock
    state_dict["armed_hard_stop"] = armed_hard_stop

    return completed_trades

def run_cta(df: pd.DataFrame, cfg: CtaConfig, asset: str = "") -> pd.DataFrame:
    completed_trades = []
    state_dict = {
        'active_trades': [],
        'phoenix_watch': [],
        'armed_countdown': 0,
        'armed_shock': 0.0,
        'armed_hard_stop': 0.0
    }

    for ts, row in df.iterrows():
        new_completed = step_cta(ts, row, state_dict, cfg, asset)
        completed_trades.extend(new_completed)

    curr_close = df.iloc[-1]['close'] if not df.empty else 0.0
    ts = df.index[-1] if not df.empty else None

    for t in state_dict['active_trades']:
        pnl = (curr_close - t['entry_price']) / t['entry_price']
        dur = (ts - t['entry_time']).total_seconds() / 3600.0 if ts and t['entry_time'] else 0.0
        completed_trades.append(dict(
            asset=asset,
            side='LONG', entry=t['entry_time'], exit=ts, duration_hours=dur,
            entry_price=t['entry_price'], exit_price=curr_close,
            pnl=pnl, shock=t.get('entry_shock', 0.0),
            mae=(t['trade_min_low'] - t['entry_price']) / t['entry_price'],
            mfe=(t['trade_max_high'] - t['entry_price']) / t['entry_price'],
            reason='open_at_end',
            engine=t['engine']
        ))
                           
    return pd.DataFrame(completed_trades)

