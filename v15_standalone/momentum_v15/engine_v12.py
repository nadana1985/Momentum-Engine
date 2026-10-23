"""
Kronos V12: Pure 6-Core Execution Kernel (engine_v12.py)
Executes Macro Gating, Dynamic Tier Floors, Whale Firewalling, Bear Trap Reclaims,
and Climax Top Harvesting.
"""

from typing import Dict, List, Optional
import numpy as np
import pandas as pd

from momentum_v15.config import V12Config
from momentum_v15.telemetry_v12 import TelemetryCollector, TelemetryRecord
from momentum_v15.sizing_v12 import compute_csmi_metrics
from momentum_v15.features_v12 import extract_p_nb_high
from momentum_v15.oms_fills import limit_fill_price


def compute_exit_urgency_score(row, c: float, h: float, l: float, o: float, shock: float, mfe: float, cfg_exit=None) -> int:
    """Study S-CE & S-CG: Computes the 6 Climax Exhaustion Signatures score in [0, 100]."""
    score = 0

    # Sig 1: Climax Pinbar & Upper Wick Rejection (Max 20 pts)
    wick = float(row.get('upper_wick_ratio', (h - max(o, c)) / max(1e-6, h - l)))
    ema200_1h = float(row.get('ema200_1h', c))
    atr_24 = float(row.get('atr_24h', c * 0.02))
    is_extended = (c >= ema200_1h + 2.0 * atr_24) or (mfe >= 0.20)
    if is_extended:
        if wick >= 0.75:
            score += 20
        elif wick >= 0.55:
            score += 14
        elif wick >= 0.45 and shock >= 4.0:
            score += 12

    # Sig 2: Volume Contraction from 24h Peak (Max 20 pts)
    d_vol = float(row.get('d_vol_peak_24h', 0.0))
    if d_vol <= -0.50:
        score += 15
        if shock < 1.2:
            score += 5

    # Sig 3: Token Open Interest Unwind from 24h Peak (Max 20 pts - Rule 7 Dynamic vs Static)
    use_studentized = getattr(cfg_exit, 'enable_studentized_oi_firewall', False) if cfg_exit is not None else False
    if use_studentized:
        z_oi_peak = float(row.get('z_delta_oi_24h', 0.0))
        if z_oi_peak <= -2.00:
            score += 20 # Extreme statistical liquidation waterfall (<= -2.0 sigma)
        elif z_oi_peak <= -1.25:
            score += 14 # Significant orderflow deceleration (<= -1.25 sigma)
    else:
        d_oi = float(row.get('d_oi_tok_peak_24h', 0.0))
        if d_oi <= -0.15:
            score += 20
        elif d_oi <= -0.04:
            score += 14

    # Sig 4: Funding Rate Snap or Euphoria Flip (Max 15 pts)
    fr_curr = float(row.get('funding_rate', 0.0))
    fr_min = float(row.get('funding_min_24h', fr_curr))
    if fr_min <= -0.0003 and fr_curr >= -0.00005:
        score += 15
    elif fr_curr >= 0.00020:
        score += 12

    # Sig 5: Taker Buy Breakdown (Max 15 pts)
    taker = float(row.get('taker_ratio', 0.50))
    if taker < 0.46:
        score += 15
    elif taker < 0.495 and shock <= 1.25:
        score += 12

    # Sig 6: Whale L/S Floor Inflection (Max 10 pts)
    ls_min = float(row.get('ls_min_24h', 1.0))
    d_ls_6h = float(row.get('d_ls_6h', 0.0))
    d_oi = float(row.get('d_oi_tok_peak_24h', 0.0))
    if ls_min <= 0.85 and d_ls_6h >= 0.05 and d_oi <= -0.04:
        score += 10

    return score


def check_whale_squeeze_immunity(row, ls_ratio: Optional[float], cfg_exit) -> bool:
    """Study S-CE / Study S-BK: Overrides climax exit when whales are trapped net short."""
    if not getattr(cfg_exit, 'enable_whale_squeeze_immunity', True):
        return False
    z_ls_val = float(row.get('z_ls_30d', 0.0))
    imm_z = getattr(cfg_exit, 'immunity_z_ls', -2.0)
    imm_ls = getattr(cfg_exit, 'immunity_max_ls', 0.95)
    return (z_ls_val <= imm_z) or (ls_ratio is not None and pd.notna(ls_ratio) and ls_ratio <= imm_ls)


def check_macro_wave1_genesis(row, c: float, cfg_exit) -> bool:
    """Study S-CG: Identifies Genesis of Macro Impulse Wave 1 to grant unconstrained Donchian trail."""
    if not getattr(cfg_exit, 'enable_dynamic_wave1_convexity_guard', False):
        return False
    ema200_1d_val = float(row.get('ema200_1d', c))
    c_dist_200d = (c - ema200_1d_val) / max(1e-8, ema200_1d_val)
    btc_dist_200d = float(row.get('btc_dist_ema_200d', 0.0))
    max_dist = getattr(cfg_exit, 'wave1_max_asset_dist_200d', 0.15)
    min_btc = getattr(cfg_exit, 'wave1_min_btc_dist_200d', 0.15)
    return (c_dist_200d <= max_dist) and (c_dist_200d >= -0.05) and (btc_dist_200d >= min_btc)


def run_v12_engine(
    df: pd.DataFrame,
    asset: str,
    cfg: V12Config = V12Config(),
    telemetry: Optional[TelemetryCollector] = None
) -> pd.DataFrame:
    """
    Executes the Clean 6-Core Execution Kernel on an enriched shard.
    Returns DataFrame of executed trades (closed and open).
    """
    if df.empty:
        return pd.DataFrame()

    trades: List[Dict] = []
    active_positions: Dict[str, Optional[Dict]] = {
        'Book 1': None,
        'Book 2': None,
        'Book 3': None,
        'Book 4': None,
        'Book 5': None,
        'Book 6': None,
        'Book 7': None,
    }
    last_exit_ts_by_book: Dict[str, Optional[pd.Timestamp]] = {
        'Book 1': None,
        'Book 2': None,
        'Book 3': None,
        'Book 4': None,
        'Book 5': None,
        'Book 6': None,
        'Book 7': None,
    }
    last_exit_reason_b1: Optional[str] = None
    last_exit_pnl_b1: float = 0.0
    last_entry_price_b1: float = 0.0
    flush_low_since_exit_b1: float = float('inf')

    last_exit_ts: Optional[pd.Timestamp] = None
    last_exit_reason: Optional[str] = None
    last_exit_pnl: float = 0.0
    last_entry_price: float = 0.0
    flush_low_since_exit: float = float('inf')
    active_shadow_anchor: Optional[Dict] = None
    active_flush_bid: Optional[Dict] = None
    active_b4_setup: Optional[Dict] = None
    active_b1_anchor: Optional[Dict] = None
    active_b5_bid: Optional[Dict] = None
    last_b5_arm_ts: Optional[pd.Timestamp] = None
    active_b6_setup: Optional[Dict] = None
    active_b2_delayed: Optional[Dict] = None
    active_b4_reentry: Optional[Dict] = None
    active_b7_setup: Optional[Dict] = None

    tier = str(df['tier'].iloc[0]) if 'tier' in df.columns else 'Tier 1'
    is_tier1 = (tier == 'Tier 1')

    # Study S-BZ: Extract precomputed daily DataFrame from attrs or calculate once
    daily_df = df.attrs.get('daily_df')
    if daily_df is None:
        try:
            d_c = df['close'].resample('1D').last().dropna()
            d_o = df['open'].resample('1D').first().dropna()
            d_h = df['high'].resample('1D').max().dropna()
            d_l = df['low'].resample('1D').min().dropna()
            daily_df = pd.DataFrame({'open': d_o, 'high': d_h, 'low': d_l, 'close': d_c})
        except Exception:
            daily_df = None

    # Precompute rolling series for speed
    ls_series = df.get('toptrader_ls', pd.Series(1.0, index=df.index)).ffill()
    max_ls_7d_series = ls_series.shift(1).rolling(168, min_periods=24).max()

    slippage = cfg.entry.slippage

    # Precompute arrays and caching for Two-Tier Volume Profile Shelf Absorption (Study S-AN / S-AO)
    c_arr = df['close'].to_numpy(float)
    h_arr = df['high'].to_numpy(float)
    l_arr = df['low'].to_numpy(float)
    v_arr = df['volume'].to_numpy(float) if 'volume' in df.columns else np.ones(len(df), dtype=float)
    if 'quote_volume' in df.columns:
        qv_arr = df['quote_volume'].fillna(0.0).to_numpy(float)
    elif 'volume' in df.columns:
        qv_arr = (df['close'] * df['volume']).fillna(0.0).to_numpy(float)
    else:
        qv_arr = df['close'].fillna(0.0).to_numpy(float)

    _vp_cache = {}
    vp_lookback = getattr(cfg.book3_flush, 'vp_lookback_bars', 2160)
    vp_bins = getattr(cfg.book3_flush, 'vp_bins', 35)

    def _get_vp(i: int):
        """Point-in-time volume profile over bars [i-vp_lookback, i-1] strictly excluding bar i."""
        if i in _vp_cache:
            return _vp_cache[i]
        s = max(0, i - vp_lookback)
        res = None
        if i - s >= 24 * 7:  # require >= 7 days of history to form profile
            lo_v = float(np.min(l_arr[s:i]))
            hi_v = float(np.max(h_arr[s:i]))
            if hi_v > lo_v > 0:
                edges = np.linspace(lo_v, hi_v, vp_bins + 1)
                vols, _ = np.histogram(c_arr[s:i], bins=edges, weights=qv_arr[s:i])
                tot = float(vols.sum())
                if tot > 0:
                    res = {
                        'lows': edges[:-1],
                        'highs': edges[1:],
                        'mids': 0.5 * (edges[:-1] + edges[1:]),
                        'vols': vols,
                        'mean': tot / vp_bins
                    }
        _vp_cache[i] = res
        return res

    for _bar_i, (ts, row) in enumerate(df.iterrows()):
        c = float(row['close'])
        h = float(row['high'])
        l = float(row['low'])
        o = float(row['open']) if 'open' in row else c
        fr = float(row.get('funding_rate')) if pd.notna(row.get('funding_rate')) else np.nan
        dist_60d = float(row.get('dist_from_60d_low', 999.0))
        current_oi = float(row.get('oi_usd')) if pd.notna(row.get('oi_usd')) else 0.0
        ls_ratio = float(ls_series.loc[ts]) if pd.notna(ls_series.loc[ts]) else np.nan
        max_ls_7d = float(max_ls_7d_series.loc[ts]) if pd.notna(max_ls_7d_series.loc[ts]) else 1.0
        d_ls_24h = float(row.get('d_ls_24h', 0.0))
        d_oi_tok = float(row.get('d_oi_tokens_24h', 0.0))
        d_c_24h = float(row.get('d_close_24h', 0.0))
        turnover = float(row.get('turnover_24h')) if pd.notna(row.get('turnover_24h')) else np.nan
        wick = float(row.get('upper_wick', 0.0))
        shock = float(row.get('vol_shock', 1.0))
        btc_bull = bool(row.get('btc_macro_bull', True))
        vol = float(row.get('volume', 1.0))

        if active_positions['Book 1'] is None and last_exit_ts_by_book['Book 1'] is not None:
            flush_low_since_exit_b1 = min(flush_low_since_exit_b1, l)
        if all(pos is None for pos in active_positions.values()) and last_exit_ts is not None:
            flush_low_since_exit = min(flush_low_since_exit, l)

        # Study S-BR & S-BS: Book 1 AVWAP_tau Anchor Accumulator Tracking
        if getattr(cfg, 'book1', None) and getattr(cfg.book1, 'enable_avwap_reclaim', True):
            is_b1_breakout_bar = bool(row.get('breakout_21d', False))
            dorm_score_72 = float(row.get('dorm_72h_mean', row.get('dormancy_score', 0.50)))
            cusum_usd_val = float(row.get('cusum_usd', 1.0))

            if is_b1_breakout_bar and btc_bull and (dorm_score_72 >= cfg.book1.min_dormancy_72h) and (cusum_usd_val >= 1.0):
                pre_start = max(0, _bar_i - 504)
                base_l = float(l_arr[pre_start : _bar_i].min()) if _bar_i > 0 else l
                active_b1_anchor = {
                    'tau_bar': _bar_i,
                    'base_low': base_l,
                    'cum_pv': c * qv_arr[_bar_i],
                    'cum_v': qv_arr[_bar_i],
                    'retest_low': l,
                    'peak_h': h,
                    'tau_midpoint': (h + l) / 2.0,
                    'tau_low': l,
                    'consolidation_bars': 0,
                    'consolidation_passed': not getattr(cfg.book1, 'enable_3bar_consolidation_hold', True),
                }
            elif active_b1_anchor is not None:
                active_b1_anchor['cum_pv'] += c * qv_arr[_bar_i]
                active_b1_anchor['cum_v'] += qv_arr[_bar_i]
                bars_since_tau = _bar_i - active_b1_anchor['tau_bar']
                if l < active_b1_anchor['retest_low']:
                    active_b1_anchor['retest_low'] = l
                if h > active_b1_anchor['peak_h']:
                    active_b1_anchor['peak_h'] = h

                # Study S-BU: 3-Bar Consolidation Hold Tracking
                if not active_b1_anchor['consolidation_passed']:
                    req_bars = getattr(cfg.book1, 'min_consolidation_bars', 3)
                    if bars_since_tau <= req_bars:
                        if l >= active_b1_anchor['tau_midpoint'] and c >= active_b1_anchor['tau_low']:
                            active_b1_anchor['consolidation_bars'] += 1
                            if active_b1_anchor['consolidation_bars'] >= req_bars:
                                active_b1_anchor['consolidation_passed'] = True
                        else:
                            # Failed consolidation hold: discard false sweep anchor
                            active_b1_anchor = None
                    else:
                        if not active_b1_anchor['consolidation_passed']:
                            active_b1_anchor = None

                # Anchor expiry: retest exceeding max hours or breaching base low
                if (
                    active_b1_anchor is not None and (
                        bars_since_tau > getattr(cfg.book1, 'max_retest_hours', 120) or
                        active_b1_anchor['retest_low'] <= active_b1_anchor['base_low']
                    )
                ):
                    active_b1_anchor = None

        # Study S-BP: Book 6 3-SARE CUSUM-Anchored Base AVWAP Tracking (Tier 2 Mid-Caps only)
        if getattr(cfg, 'book6', None) and getattr(cfg.book6, 'enable_book6', True) and (tier == 'Tier 2'):
            is_b6_breakout = bool(row.get('is_b6_breakout', False))
            cusum_val = float(row.get('cusum_usdt', 0.0))
            if is_b6_breakout and (cusum_val >= cfg.book6.cusum_threshold) and (_bar_i >= 720):
                base_low_30d = float(l_arr[max(0, _bar_i - 720) : _bar_i].min())
                active_b6_setup = {
                    'tau_bar': _bar_i,
                    'tau_ts': ts,
                    'base_low_30d': base_low_30d,
                    'cum_pv': c * qv_arr[_bar_i],
                    'cum_v': qv_arr[_bar_i],
                    'retest_low': l,
                    'retest_bar': _bar_i,
                    'retest_found': False,
                    'peak_h': h,
                }
            elif active_b6_setup is not None:
                active_b6_setup['cum_pv'] += c * qv_arr[_bar_i]
                active_b6_setup['cum_v'] += qv_arr[_bar_i]
                bars_since_b6_tau = _bar_i - active_b6_setup['tau_bar']
                cur_b6_avwap = active_b6_setup['cum_pv'] / max(1e-5, active_b6_setup['cum_v'])

                # Check retest corridor [0.90, 1.03] of AVWAP
                if (bars_since_b6_tau >= cfg.book6.retest_min_hours) and (bars_since_b6_tau <= cfg.book6.retest_max_hours):
                    if (l <= cur_b6_avwap * cfg.book6.avwap_tolerance_high) and (l >= cur_b6_avwap * cfg.book6.avwap_tolerance_low):
                        if l > active_b6_setup['base_low_30d']:
                            active_b6_setup['retest_found'] = True
                            if l < active_b6_setup['retest_low']:
                                active_b6_setup['retest_low'] = l
                                active_b6_setup['retest_bar'] = _bar_i

                # Retest floor breach or timeout invalidation
                if (
                    bars_since_b6_tau > cfg.book6.retest_max_hours or
                    l <= active_b6_setup['base_low_30d']
                ):
                    active_b6_setup = None

        # Study S-BX: Book 2 Sunday 7-Day High Break Trigger Evaluation
        cal_cfg = getattr(cfg, 'calendar', None)
        if cal_cfg and cal_cfg.enable_calendar_firewall and cal_cfg.book2_require_sunday_high_break:
            if active_b2_delayed is not None and active_positions['Book 2'] is None:
                # Check expiration (> 168 hours or past Sunday week)
                age_h = (ts - active_b2_delayed['trigger_ts']).total_seconds() / 3600.0
                if age_h > cal_cfg.sunday_high_break_window_hours or age_h > 168:
                    active_b2_delayed = None
                elif h > active_b2_delayed['sun_high']:
                    # Triggered! Enter at Sunday High breakout
                    break_px = max(active_b2_delayed['sun_high'] * 1.001, o) * (1 + slippage)
                    stop_px = max(active_b2_delayed['stop_px'], break_px * 0.92) # 8% stop clamp
                    active_positions['Book 2'] = {
                        'entry_time': ts,
                        'entry_price': break_px,
                        'stop': stop_px,
                        'max_high': h,
                        'min_low': l,
                        'book': 'Book 2',
                        'is_reclaim': False,
                        'entry_oi': current_oi,
                        'pct_lam': active_b2_delayed.get('pct_lam', 0.50),
                        'turnover_at_entry': turnover if pd.notna(turnover) else 1.0,
                        'rank_ts': active_b2_delayed.get('rank_ts', 0.50),
                        'dist_ema': active_b2_delayed.get('dist_ema', 0.0),
                        'w_btc': 1.0,
                        'w_conviction': active_b2_delayed.get('w_conviction', 1.0),
                    }
                    active_b2_delayed = None
                    if telemetry:
                        telemetry.log_signal(TelemetryRecord(
                            timestamp=ts, asset=asset, tier=tier, status="ACTIVE",
                            veto_gate="None", candidate_setup="Book 2 Sunday High Break",
                            price=break_px, turnover=turnover if pd.notna(turnover) else 1.0,
                            ls_ratio=ls_ratio if pd.notna(ls_ratio) else 1.0,
                            funding_rate=fr if pd.notna(fr) else 0.0,
                            btc_macro_bull=btc_bull
                        ))
                    continue

        # Check Book 3: Active resting flush bid fill or expiry
        if getattr(cfg.book3_flush, 'enable_book3_flush_reclaim', False):
            if active_flush_bid is not None and active_positions['Book 3'] is None:
                bid_age_h = (ts - active_flush_bid['armed_ts']).total_seconds() / 3600.0
                if bid_age_h > active_flush_bid['ttl_bars']:
                    active_flush_bid = None # Expired
                else:
                    fill_mode = getattr(getattr(cfg, 'execution', None), 'mode', 'paper_limit')
                    entry_px = limit_fill_price(
                        float(active_flush_bid['bid_px']), o, l, fill_mode
                    )
                    if entry_px is not None:
                        # Study S-BX: Calendar Firewall on Limit Fills
                        cal_cfg = getattr(cfg, 'calendar', None)
                        is_mon = (ts.dayofweek == 0)
                        is_mstart = ts.is_month_start
                        is_mend = ts.is_month_end
                        skip_fill = False
                        if cal_cfg and cal_cfg.enable_calendar_firewall and (candidate_setup != "200d EMA Reclaim"):
                            if (cal_cfg.veto_monday and is_mon) or (cal_cfg.veto_month_start and is_mstart) or (cal_cfg.veto_month_end and is_mend):
                                skip_fill = True

                        if not skip_fill:
                            stop_px = float(active_flush_bid['stop_px'])
                            if fill_mode == 'live_limit':
                                stop_px = entry_px * (1.0 - float(cfg.book3_flush.max_initial_risk))
                            active_positions['Book 3'] = {
                                'entry_time': ts,
                                'entry_price': entry_px,
                                'stop': stop_px,
                                'target': active_flush_bid['target_px'],
                                'max_high': h,
                                'min_low': l,
                                'book': 'Book 3',
                                'is_reclaim': False,
                                'is_continuation': False,
                                'is_book3': True,
                                'entry_oi': current_oi,
                                'pct_lam': 0.50,
                                'turnover_at_entry': turnover if pd.notna(turnover) else 1.0,
                                'veto_gate': active_flush_bid['veto_gate'],
                            }
                            active_flush_bid = None
                            if telemetry:
                                telemetry.log_signal(TelemetryRecord(
                                    timestamp=ts, asset=asset, tier=tier, status="ACTIVE",
                                    veto_gate="Book 3: Flush Limit Filled", candidate_setup="Book 3 Flush Reclaim",
                                    price=entry_px, turnover=turnover if pd.notna(turnover) else 1.0,
                                    ls_ratio=ls_ratio if pd.notna(ls_ratio) else 1.0,
                                    funding_rate=fr if pd.notna(fr) else 0.0,
                                    btc_macro_bull=btc_bull
                                ))
                            continue

        # Study S-BI Pillar 1: Book 5 Trapped-Whale Shelf Absorption (resting limit bid lifecycle - Tier 1 & 2 only)
        if getattr(cfg.book5, 'enable_book5', False) and (tier in ('Tier 1', 'Tier 2')):
            if active_b5_bid is not None and active_positions['Book 5'] is None:
                b5_age_h = (ts - active_b5_bid['armed_ts']).total_seconds() / 3600.0
                if b5_age_h > active_b5_bid['ttl_bars']:
                    active_b5_bid = None
                elif l <= active_b5_bid['bid_px']:
                    cal_cfg = getattr(cfg, 'calendar', None)
                    is_mon = (ts.dayofweek == 0)
                    is_mstart = ts.is_month_start
                    is_mend = ts.is_month_end
                    skip_b5 = False
                    if cal_cfg and cal_cfg.enable_calendar_firewall:
                        if (cal_cfg.veto_monday and is_mon) or (cal_cfg.veto_month_start and is_mstart) or (cal_cfg.veto_month_end and is_mend):
                            skip_b5 = True
                    if not skip_b5:
                        fill_mode = getattr(getattr(cfg, 'execution', None), 'mode', 'paper_limit')
                        if fill_mode == 'live_limit':
                            entry_px = limit_fill_price(
                                float(active_b5_bid['bid_px']), o, l, fill_mode
                            )
                        else:
                            entry_px = min(o, active_b5_bid['bid_px'])
                        if entry_px is not None:
                            active_positions['Book 5'] = {
                                'entry_time': ts,
                                'entry_price': entry_px,
                                'stop': entry_px * (1.0 - cfg.book5.max_initial_risk),
                                'target': active_b5_bid['target_px'],
                                'max_high': h,
                                'min_low': l,
                                'book': 'Book 5',
                                'is_reclaim': False,
                                'is_continuation': False,
                                'entry_oi': current_oi,
                                'pct_lam': 0.50,
                                'turnover_at_entry': turnover if pd.notna(turnover) else 1.0,
                            }
                            active_b5_bid = None
                            if telemetry:
                                telemetry.log_signal(TelemetryRecord(
                                    timestamp=ts, asset=asset, tier=tier, status="ACTIVE",
                                    veto_gate="Book 5: Shelf Squeeze Limit Filled", candidate_setup="Book 5 Trapped-Whale Shelf",
                                    price=entry_px, turnover=turnover if pd.notna(turnover) else 1.0,
                                    ls_ratio=ls_ratio if pd.notna(ls_ratio) else 1.0,
                                    funding_rate=fr if pd.notna(fr) else 0.0,
                                    btc_macro_bull=btc_bull
                                ))
                            continue
            # Arm a new bid using only information available at this bar's close (institutional liquidity only)
            if (tier in ('Tier 1', 'Tier 2')) and active_positions['Book 5'] is None and active_b5_bid is None and pd.notna(ls_ratio):
                since_arm = (ts - last_b5_arm_ts).total_seconds() / 3600.0 if last_b5_arm_ts is not None else 1e9
                if (since_arm >= cfg.book5.cooldown_hours and
                        ls_ratio <= cfg.book5.max_ls and
                        d_oi_tok >= cfg.book5.min_d_oi_tokens and
                        (d_c_24h > 0.0 or not cfg.book5.require_price_up_24h)):
                    active_b5_bid = {
                        'bid_px': c * (1.0 - cfg.book5.discount_pct),
                        'target_px': c,
                        'armed_ts': ts,
                        'ttl_bars': cfg.book5.ttl_hours,
                    }
                    last_b5_arm_ts = ts

        # -------------------------------------------------------------
        # 1. ACTIVE POSITION MANAGEMENT & CLIMAX HARVESTING (PER-BOOK SLEEVES)
        # -------------------------------------------------------------
        for book_name in list(active_positions.keys()):
            active = active_positions[book_name]
            if active is None:
                continue

            active['max_high'] = max(active['max_high'], h)
            active['min_low'] = min(active['min_low'], l)
            dur_hours = (ts - active['entry_time']).total_seconds() / 3600.0
            mfe = (active['max_high'] - active['entry_price']) / active['entry_price']
            mae = (active['min_low'] - active['entry_price']) / active['entry_price']

            active['max_vol'] = max(active.get('max_vol', vol), vol)
            entry_oi = active.get('entry_oi', current_oi)
            oi_change = (current_oi - entry_oi) / entry_oi if entry_oi > 0 else 0.0
            book_type = active.get('book', 'Book 1')

            # Trailing Floor & Ratchets
            if book_type in ('Book 3', 'Book 5'):
                pass # Fixed target reclaim & stop floor
            elif book_type == 'Book 2':
                mode = getattr(cfg.exit, 'be_ratchet_mode', 'baseline')
                if mode == "baseline":
                    if mfe >= 0.15:
                        active['stop'] = max(active['stop'], active['entry_price'] * 1.005)
                elif mode == "cushion_3pct":
                    if mfe >= 0.15:
                        active['stop'] = max(active['stop'], active['entry_price'] * (1.0 - 0.03))
                elif mode == "cushion_1_5pct":
                    if mfe >= 0.15:
                        active['stop'] = max(active['stop'], active['entry_price'] * (1.0 - 0.015))
                elif mode == "delayed_30pct":
                    if mfe >= 0.30:
                        active['stop'] = max(active['stop'], active['entry_price'] * 1.005)
                elif mode == "volume_gated":
                    if mfe >= 0.15:
                        ema168 = float(row.get('ema_168', 0.0))
                        is_dry_hl = (vol <= 0.65 * active.get('max_vol', vol)) and (c >= ema168)
                        if not is_dry_hl:
                            active['stop'] = max(active['stop'], active['entry_price'] * 1.005)
                elif mode == "no_be_ratchet":
                    pass

                if mfe >= 0.35:
                    active['stop'] = max(active['stop'], active['max_high'] * 0.85)
                if mfe >= 0.70:
                    active['stop'] = max(active['stop'], active['max_high'] * 0.80)
            elif book_type == 'Book 6':
                # Study S-BP: Book 6 3-SARE Trailing Floor & Ratchets
                # S-TX-2: do not ratchet stop to BE or 72h low; trail is a close-break in the exit block.
                if not getattr(cfg.book6, 'stx2_hold', False):
                    if active.get('t_b_hit', False):
                        floor_val = float(row.get('low_72h', active['stop']))
                        active['stop'] = max(active['stop'], floor_val)
                    elif active.get('t_a_hit', False):
                        active['stop'] = max(active['stop'], active['entry_price'] * 0.998)
            elif book_type == 'Book 7':
                # Study S-CH & S-CK: Book 7 Snug Stop & Breakeven Cushion Ratchet
                b7_cfg = getattr(cfg, 'book7', None)
                be_trigger = getattr(b7_cfg, 'breakeven_mfe_trigger', 0.05) if b7_cfg is not None else 0.05
                be_cush = getattr(b7_cfg, 'breakeven_cushion_pct', 0.005) if b7_cfg is not None else 0.005
                if active.get('is_clean_runner', False):
                    be_cush = getattr(b7_cfg, 'runner_cushion_pct', 0.030)
                if mfe >= be_trigger:
                    active['stop'] = max(active['stop'], active['entry_price'] * (1.0 - be_cush))
            elif book_type == 'Book 4':
                # Study S-BZ: resting stop stays static (breakeven cushion for Tranche B, structural
                # stop for re-entries). The 72h Donchian trail is a CLOSE-break exit, handled in the
                # Book 4 exit block below — not an intraday ratchet.
                pass
            elif active.get('is_b1_twotranche', False):
                # Study S-BR & S-BS: Book 1 Two-Tranche Trailing Floor (72h Donchian)
                if active.get('t1_a_hit', False) or active.get('arm_donchian', False):
                    floor_val = float(row.get('low_72h', active['stop']))
                    if pd.notna(floor_val) and floor_val > active['stop']:
                        active['stop'] = floor_val
                elif mfe >= 0.08:
                    active['arm_donchian'] = True
                    floor_val = float(row.get('low_72h', active['stop']))
                    if pd.notna(floor_val) and floor_val > active['stop']:
                        active['stop'] = floor_val
            elif active.get('is_continuation', False):
                # Study S-U Continuation Trailing Architecture
                if mfe >= cfg.exit.continuation_be_ratchet_mfe:
                    active['stop'] = max(active['stop'], active['entry_price'] * 1.005)
                floor_7d = float(row.get('low_7d', active['stop']))
                if pd.notna(floor_7d) and floor_7d > active['stop']:
                    active['stop'] = floor_7d
                if mfe >= cfg.exit.continuation_trail_mfe:
                    active['stop'] = max(active['stop'], active['max_high'] * cfg.exit.continuation_trail_floor_pct)
            else: # Book 1 Clean 6-Core Trailing Architecture
                mode = getattr(cfg.exit, 'be_ratchet_mode', 'baseline')
                if is_tier1:
                    floor_14d = float(row.get('low_14d', active['stop']))
                    if pd.notna(floor_14d) and floor_14d > active['stop']:
                        active['stop'] = floor_14d
                    if mode == "baseline":
                        if mfe >= cfg.exit.tier1_be_ratchet_mfe:
                            active['stop'] = max(active['stop'], active['entry_price'] * 1.005)
                    elif mode == "cushion_3pct":
                        if mfe >= cfg.exit.tier1_be_ratchet_mfe:
                            active['stop'] = max(active['stop'], active['entry_price'] * (1.0 - 0.03))
                    elif mode == "cushion_1_5pct":
                        if mfe >= cfg.exit.tier1_be_ratchet_mfe:
                            active['stop'] = max(active['stop'], active['entry_price'] * (1.0 - 0.015))
                    elif mode == "delayed_30pct":
                        if mfe >= 0.30:
                            active['stop'] = max(active['stop'], active['entry_price'] * 1.005)
                    elif mode == "volume_gated":
                        if mfe >= cfg.exit.tier1_be_ratchet_mfe:
                            ema168 = float(row.get('ema_168', 0.0))
                            is_dry_hl = (vol <= 0.65 * active.get('max_vol', vol)) and (c >= ema168)
                            if not is_dry_hl:
                                active['stop'] = max(active['stop'], active['entry_price'] * 1.005)
                    elif mode == "no_be_ratchet":
                        pass

                    if mfe >= cfg.exit.tier1_trail_ratchet_mfe:
                        active['stop'] = max(active['stop'], active['max_high'] * cfg.exit.tier1_trail_floor_pct)
                else: # Tier 2 (Calibrated 7d Floor)
                    floor_7d = float(row.get('low_7d', active['stop']))
                    if pd.notna(floor_7d) and floor_7d > active['stop']:
                        active['stop'] = floor_7d
                    if mode == "baseline":
                        if mfe >= cfg.exit.tier2_be_ratchet_mfe:
                            active['stop'] = max(active['stop'], active['entry_price'] * 1.005)
                    elif mode == "cushion_3pct":
                        if mfe >= cfg.exit.tier2_be_ratchet_mfe:
                            active['stop'] = max(active['stop'], active['entry_price'] * (1.0 - 0.03))
                    elif mode == "cushion_1_5pct":
                        if mfe >= cfg.exit.tier2_be_ratchet_mfe:
                            active['stop'] = max(active['stop'], active['entry_price'] * (1.0 - 0.015))
                    elif mode == "delayed_30pct":
                        if mfe >= 0.30:
                            active['stop'] = max(active['stop'], active['entry_price'] * 1.005)
                    elif mode == "volume_gated":
                        if mfe >= cfg.exit.tier2_be_ratchet_mfe:
                            ema168 = float(row.get('ema_168', 0.0))
                            is_dry_hl = (vol <= 0.65 * active.get('max_vol', vol)) and (c >= ema168)
                            if not is_dry_hl:
                                active['stop'] = max(active['stop'], active['entry_price'] * 1.005)
                    elif mode == "no_be_ratchet":
                        pass

                    if mfe >= cfg.exit.tier2_trail_ratchet_mfe:
                        active['stop'] = max(active['stop'], active['max_high'] * cfg.exit.tier2_trail_floor_pct)

            exit_triggered = False
            exit_price = 0.0
            exit_reason = ""

            # Core 6 Exits: Climax Air-Pocket Harvest & Fast Decay Cuts
            if book_type in ('Book 3', 'Book 5'):
                if l <= active['stop']:
                    exit_price = min(float(row.get('open', active['stop'])), active['stop']) * (1 - slippage)
                    exit_triggered = True
                    exit_reason = "stop_loss"
                elif h >= active.get('target', float('inf')):
                    exit_price = active['target']
                    exit_triggered = True
                    exit_reason = "target_reclaim"
                elif dur_hours >= cfg.book3_flush.ttl_hours:
                    exit_price = c * (1 - slippage)
                    exit_triggered = True
                    exit_reason = "time_expiry"
            elif book_type == 'Book 4':
                # Book 4 200d EMA Reclaim Exit Mechanics (Study S-BB, S-BE & S-BZ)
                # 1. Study S-BZ: Intraday Catastrophe Stop (-12%) — ONLY intraday stop before Tranche A
                # 1. Study S-BZ: Lower wicks NEVER trigger stop loss.
                #    Stops are evaluated strictly on 00:00 UTC daily close below P_NB_High.
                if not exit_triggered and not active.get('t1_a_hit', False):
                    catastrophe_pct = getattr(cfg.book4, 'catastrophe_stop_pct', 0.0)
                    if catastrophe_pct > 0.0 and not getattr(cfg.book4, 'enable_daily_close_stop', True):
                        catastrophe_floor = active['entry_price'] * (1.0 - catastrophe_pct)
                        if l <= catastrophe_floor:
                            exit_price = catastrophe_floor * (1 - slippage)
                            exit_triggered = True
                            exit_reason = "catastrophe_stop_12pct"

                # 2. Study S-BZ: Daily Close Support Stop Loss (Evaluated strictly at 00:00 UTC)
                if not exit_triggered and getattr(cfg.book4, 'enable_daily_close_stop', True) and not active.get('t1_a_hit', False):
                    anchor_mode = getattr(cfg.book4, 'daily_close_stop_anchor', 'structural_base')
                    p_nb_lvl = active.get('p_nb_high')
                    if anchor_mode == 'structural_base':
                        # Structural Stop: Daily close below 30d base floor or below initial structural stop
                        stop_ref = active.get('initial_stop', active['entry_price'] * 0.85)
                    elif anchor_mode == 'trough_stop':
                        stop_ref = active.get('initial_stop', active.get('stop'))
                    elif anchor_mode == 'p_nb_buffered':
                        stop_ref = (p_nb_lvl * 0.98) if (p_nb_lvl is not None and p_nb_lvl > 0) else active.get('initial_stop', active.get('stop'))
                    else:
                        stop_ref = p_nb_lvl if (p_nb_lvl is not None and p_nb_lvl > 0) else active.get('stop')

                    is_daily_close_bar = (ts.hour == 0)
                    if is_daily_close_bar and stop_ref is not None and c < stop_ref:
                        exit_price = c * (1 - slippage)
                        exit_triggered = True
                        exit_reason = "structural_daily_close_stop" if anchor_mode == 'structural_base' else "daily_close_below_p_nb"

                # 3. Study S-BZ: Tranche B / Re-Entry Derivatives Climax Harvest
                is_reentry = active.get('is_b4_reentry', False)
                if not exit_triggered and getattr(cfg.book4, 'enable_derivatives_climax_exit', True) and active.get('t1_a_hit', False):
                    oi_90d_peak = float(row.get('oi_rolling_90d_high', 1.0))
                    cur_oi_usd = float(current_oi)
                    is_oi_peak = (cur_oi_usd >= 0.98 * oi_90d_peak) if oi_90d_peak > 0 else False
                    is_climax_pin = (wick >= 0.50)
                    climax_mfe = 0.20 if is_reentry else 0.30
                    if mfe >= climax_mfe and is_oi_peak and is_climax_pin:
                        active['t1_b_exit_px'] = c * (1 - slippage)
                        exit_price = active['t1_b_exit_px'] if is_reentry else 0.50 * active['t1_a_exit_px'] + 0.50 * active['t1_b_exit_px']
                        exit_triggered = True
                        exit_reason = "wave3_climax_harvest" if is_reentry else "derivatives_climax_harvest"

                # Study S-CG: Studentized Orderflow Liquidation Firewall & Dynamic Macro Wave 1 Guard (Book 4 Tranche B)
                if not exit_triggered and getattr(cfg.book4, 'enable_studentized_oi_firewall', False) and active.get('t1_a_hit', False):
                    is_wave1 = check_macro_wave1_genesis(row, c, cfg.exit)
                    if not is_wave1 and mfe >= getattr(cfg.exit, 'climax_min_mfe', 0.20):
                        z_delta_oi = float(row.get('z_delta_oi_24h', 0.0))
                        is_immune = check_whale_squeeze_immunity(row, ls_ratio, cfg.exit)
                        waterfall_z = getattr(cfg.exit, 'studentized_oi_waterfall_z', -2.00)

                        if z_delta_oi <= waterfall_z and not is_immune:
                            active['t1_b_exit_px'] = c * (1 - slippage)
                            exit_price = active['t1_b_exit_px'] if is_reentry else 0.50 * active['t1_a_exit_px'] + 0.50 * active['t1_b_exit_px']
                            exit_triggered = True
                            exit_reason = "studentized_oi_waterfall"

                # Study S-CF: 4-Stage Tactical Flight Alarm & Exit Escalation Architecture (Book 4 Tranche B)
                elif not exit_triggered and getattr(cfg.book4, 'enable_4stage_tactical_exit', False) and active.get('t1_a_hit', False):
                    if mfe >= getattr(cfg.exit, 'climax_min_mfe', 0.20):
                        urg_score = compute_exit_urgency_score(row, c, h, l, o, shock, mfe)
                        is_immune = check_whale_squeeze_immunity(row, ls_ratio, cfg.exit)
                        d_oi_tok = float(row.get('d_oi_tok_peak_24h', 0.0))

                        # Stage 4: Red Alarm Terminal Air Pocket Collapse (Score >= 75 or Delta OI <= -15%)
                        if (d_oi_tok <= getattr(cfg.exit, 'post_climax_unwind_oi_drop', -0.15) or urg_score >= getattr(cfg.exit, 'stage4_terminal_urgency', 75)) and not is_immune:
                            t1_b_final_px = c * (1 - slippage)
                            if active.get('t1_b_harvest_hit', False):
                                ratio = getattr(cfg.exit, 'stage3_harvest_ratio', 0.3333333333333333)
                                t1_b_blended = ratio * active['t1_b_harvest_px'] + (1.0 - ratio) * t1_b_final_px
                            else:
                                t1_b_blended = t1_b_final_px
                            active['t1_b_exit_px'] = t1_b_blended
                            exit_price = active['t1_b_exit_px'] if is_reentry else 0.50 * active['t1_a_exit_px'] + 0.50 * active['t1_b_exit_px']
                            exit_triggered = True
                            exit_reason = "post_climax_unwind" if d_oi_tok <= getattr(cfg.exit, 'post_climax_unwind_oi_drop', -0.15) else "climax_terminal_harvest"

                        # Stage 3: Orange Alarm Partial Scale-Out (Score 55 - 74)
                        elif urg_score >= getattr(cfg.exit, 'climax_harvest_urgency', 55) and not is_immune:
                            if not active.get('t1_b_harvest_hit', False):
                                active['t1_b_harvest_hit'] = True
                                active['t1_b_harvest_px'] = c * (1 - slippage)
                                active['t1_b_harvest_ts'] = ts
                            vwap_stop = float(row.get('vwap_24h', active['stop'])) * 0.985
                            active['stop'] = max(active['stop'], vwap_stop)

                        # Stage 2: Yellow Alarm Tactical Defense Ratchet (Score 35 - 54)
                        elif urg_score >= getattr(cfg.exit, 'climax_ratchet_urgency', 35):
                            vwap_stop = float(row.get('vwap_24h', active['stop'])) * 0.985
                            active['stop'] = max(active['stop'], vwap_stop)

                # Study S-CE: Dynamic Multi-Signature Climax Harvest & Whale Squeeze Immunity (Book 4 Tranche B - Full Binary)
                elif not exit_triggered and getattr(cfg.book4, 'enable_climax_scoring_harvest', False) and active.get('t1_a_hit', False):
                    if mfe >= getattr(cfg.exit, 'climax_min_mfe', 0.20):
                        urg_score = compute_exit_urgency_score(row, c, h, l, o, shock, mfe)
                        is_immune = check_whale_squeeze_immunity(row, ls_ratio, cfg.exit)
                        d_oi_tok = float(row.get('d_oi_tok_peak_24h', 0.0))

                        if d_oi_tok <= getattr(cfg.exit, 'post_climax_unwind_oi_drop', -0.15) and not is_immune:
                            active['t1_b_exit_px'] = c * (1 - slippage)
                            exit_price = active['t1_b_exit_px'] if is_reentry else 0.50 * active['t1_a_exit_px'] + 0.50 * active['t1_b_exit_px']
                            exit_triggered = True
                            exit_reason = "post_climax_unwind"
                        elif urg_score >= getattr(cfg.exit, 'climax_harvest_urgency', 55) and not is_immune:
                            active['t1_b_exit_px'] = c * (1 - slippage)
                            exit_price = active['t1_b_exit_px'] if is_reentry else 0.50 * active['t1_a_exit_px'] + 0.50 * active['t1_b_exit_px']
                            exit_triggered = True
                            exit_reason = "climax_top_harvest"
                        elif urg_score >= getattr(cfg.exit, 'climax_ratchet_urgency', 35):
                            vwap_stop = float(row.get('vwap_24h', active['stop'])) * 0.985
                            active['stop'] = max(active['stop'], vwap_stop)

                # 3b. Study S-BZ: 72h Donchian CLOSE-break trail (Tranche B / Re-Entry)
                if not exit_triggered and active.get('t1_a_hit', False):
                    don_floor = float(row.get('low_72h', np.nan))
                    arm_level = active['entry_price'] * (1.05 if is_reentry else 1.005)
                    stx_trail_ok = True
                    if getattr(cfg.book4, 'stx_trail_after_arm_mfe', False):
                        arm_mfe = float(getattr(cfg.book4, 'donchian_arm_mfe', 0.50))
                        stx_trail_ok = mfe >= arm_mfe
                    if stx_trail_ok and pd.notna(don_floor) and don_floor > arm_level and c < don_floor:
                        t1_b_final_px = c * (1 - slippage)
                        if active.get('t1_b_harvest_hit', False):
                            ratio = getattr(cfg.exit, 'stage3_harvest_ratio', 0.3333333333333333)
                            active['t1_b_exit_px'] = ratio * active['t1_b_harvest_px'] + (1.0 - ratio) * t1_b_final_px
                        else:
                            active['t1_b_exit_px'] = t1_b_final_px

                        if getattr(cfg.book4, 'stx_real_fill', False) or is_reentry:
                            exit_price = active['t1_b_exit_px']
                        else:
                            exit_price = 0.50 * active['t1_a_exit_px'] + 0.50 * active['t1_b_exit_px']
                        exit_triggered = True
                        exit_reason = "wave3_donchian_trail" if is_reentry else "donchian_floor_break"

                # 4. Stagnation Cut
                if not exit_triggered and not is_reentry and dur_hours >= getattr(cfg.book4, 'stagnation_cut_hours', 168) and mfe < 0.05 and c < active['entry_price']:
                    exit_price = c * (1 - slippage)
                    exit_triggered = True
                    exit_reason = "stagnation_cut"
            elif book_type == 'Book 7':
                # Study S-CH & S-CK: Dedicated Book 7 Micro-Cap Supernova Exits
                b7_cfg = getattr(cfg, 'book7', None)
                if not exit_triggered and active.get('t1_a_hit', False):
                    # Study S-CK: Climax Runner Harvest
                    if getattr(b7_cfg, 'enable_climax_runner_harvest', False) and mfe >= getattr(b7_cfg, 'climax_min_mfe', 0.20):
                        urg_score = compute_exit_urgency_score(row, c, h, l, o, shock, mfe)
                        if urg_score >= getattr(b7_cfg, 'climax_harvest_urgency', 55.0):
                            active['t1_b_exit_px'] = c * (1 - slippage)
                            exit_price = 0.50 * active['t1_a_exit_px'] + 0.50 * active['t1_b_exit_px']
                            exit_triggered = True
                            exit_reason = "climax_top_harvest"

                    if not exit_triggered:
                        don_floor = float(row.get('low_72h', np.nan))
                        be_cush = getattr(b7_cfg, 'breakeven_cushion_pct', 0.005) if b7_cfg is not None else 0.005
                        if active.get('is_clean_runner', False):
                            be_cush = getattr(b7_cfg, 'runner_cushion_pct', 0.030)
                        arm_level = active['entry_price'] * (1.0 - be_cush)
                        if pd.notna(don_floor) and don_floor >= arm_level and c < don_floor:
                            active['t1_b_exit_px'] = c * (1 - slippage)
                            exit_price = 0.50 * active['t1_a_exit_px'] + 0.50 * active['t1_b_exit_px']
                            exit_triggered = True
                            exit_reason = "donchian_floor_break"
            elif book_type == 'Book 2':
                if mfe >= cfg.exit.b2_climax_mfe and wick >= cfg.exit.b2_climax_wick and shock >= cfg.exit.b2_climax_shock:
                    exit_price = c * (1 - slippage)
                    exit_triggered = True
                    exit_reason = "climax_top_harvest"
                elif not is_tier1 and dur_hours >= 48.0 and mfe < 0.08 and c < active['entry_price']:
                    exit_price = c * (1 - slippage)
                    exit_triggered = True
                    exit_reason = "fast_decay_cut"
                elif dur_hours >= cfg.exit.stagnation_hours and mfe < 0.04 and c < active['entry_price']:
                    exit_price = c * (1 - slippage)
                    exit_triggered = True
                    exit_reason = "stagnation_cut"
            elif active.get('is_continuation', False):
                # Study S-U Continuation Climax Top Harvest
                if mfe >= cfg.exit.continuation_climax_mfe and wick >= cfg.exit.continuation_climax_wick and shock >= cfg.exit.continuation_climax_shock:
                    exit_price = c * (1 - slippage)
                    exit_triggered = True
                    exit_reason = "climax_top_harvest"
                elif dur_hours >= cfg.exit.stagnation_hours and mfe < cfg.exit.stagnation_max_mfe and c < active['entry_price']:
                    exit_price = c * (1 - slippage)
                    exit_triggered = True
                    exit_reason = "stagnation_bailout"
            else:
                climax_mfe_threshold = cfg.exit.tier1_climax_mfe if is_tier1 else cfg.exit.tier2_climax_mfe
                is_climax_wick = (wick >= cfg.exit.climax_min_upper_wick) and (shock >= cfg.exit.climax_min_vol_shock)
                is_whale_dumping = (d_ls_24h <= cfg.exit.climax_whale_dump_d_ls) or (fr >= cfg.exit.climax_whale_dump_funding)

                if mfe >= climax_mfe_threshold and is_climax_wick and is_whale_dumping:
                    exit_price = c * (1 - slippage)
                    exit_triggered = True
                    exit_reason = "climax_top_harvest"
                # Velocity & Fast OI Decay Bailouts (Bypassed for Two-Tranche trades)
                elif not active.get('is_b1_twotranche', False):
                    if not is_tier1 and dur_hours >= cfg.exit.tier2_fast_decay_hours and oi_change <= cfg.exit.tier2_fast_decay_oi_leak and c < active['entry_price']:
                        exit_price = c * (1 - slippage)
                        exit_triggered = True
                        exit_reason = "fast_decay_cut"
                    elif is_tier1 and dur_hours >= cfg.exit.tier1_fast_decay_hours and oi_change <= cfg.exit.tier1_fast_decay_oi_leak and c < active['entry_price']:
                        exit_price = c * (1 - slippage)
                        exit_triggered = True
                        exit_reason = "fast_decay_cut"
                    elif dur_hours >= cfg.exit.stagnation_hours and mfe < cfg.exit.stagnation_max_mfe and c < active['entry_price']:
                        exit_price = c * (1 - slippage)
                        exit_triggered = True
                        exit_reason = "stagnation_bailout"

            # Study S-BI Pillar 3: Whale Euphoria Climax Harvest (point-in-time L/S on the current bar)
            if (not exit_triggered and getattr(cfg.exit, 'enable_euphoria_climax_harvest', False)
                    and book_type in ('Book 1', 'Book 2', 'Continuation')
                    and mfe >= getattr(cfg.exit, 'euphoria_min_mfe', 0.20)
                    and pd.notna(ls_ratio) and ls_ratio >= getattr(cfg.exit, 'euphoria_min_ls', 2.50)):
                exit_price = c * (1 - slippage)
                exit_triggered = True
                exit_reason = "euphoria_climax_harvest"

            # Study S-CE: Dynamic Multi-Signature Climax Harvest (Book 1, Book 2, Continuation)
            if not exit_triggered and getattr(cfg.exit, 'enable_climax_scoring_engine', False) and book_type in ('Book 1', 'Book 2', 'Continuation'):
                if mfe >= getattr(cfg.exit, 'climax_min_mfe', 0.20):
                    urg_score = compute_exit_urgency_score(row, c, h, l, o, shock, mfe)
                    is_immune = check_whale_squeeze_immunity(row, ls_ratio, cfg.exit)
                    d_oi_tok = float(row.get('d_oi_tok_peak_24h', 0.0))

                    if d_oi_tok <= getattr(cfg.exit, 'post_climax_unwind_oi_drop', -0.15) and not is_immune:
                        exit_price = c * (1 - slippage)
                        exit_triggered = True
                        exit_reason = "post_climax_unwind"
                    elif urg_score >= getattr(cfg.exit, 'climax_harvest_urgency', 55) and not is_immune:
                        exit_price = c * (1 - slippage)
                        exit_triggered = True
                        exit_reason = "climax_top_harvest"
                    elif urg_score >= getattr(cfg.exit, 'climax_ratchet_urgency', 35):
                        vwap_stop = float(row.get('vwap_24h', active['stop'])) * 0.985
                        active['stop'] = max(active['stop'], vwap_stop)

            # Study S-AA: 36-Hour Stagnation Stall-Out Bailout (Zero-Runner Loss Checkpoint)
            if not exit_triggered and cfg.exit.enable_stall_bailout and not active.get('is_b1_twotranche', False) and book_type not in ('Book 4', 'Book 7'):
                if dur_hours >= cfg.exit.stall_bailout_hours and mfe < cfg.exit.stall_bailout_max_mfe and c < active['entry_price']:
                    exit_price = c * (1 - slippage)
                    exit_triggered = True
                    exit_reason = "stall_bailout"

            # Study S-BP: Book 6 3-SARE 3-Stage Asymmetric Reclaim Engine Exits
            if not exit_triggered and book_type == 'Book 6':
                if getattr(cfg.book6, 'stx2_hold', False):
                    # S-TX-2 T5–T7: structural stop until large arm, then 72h Donchian on close.
                    arm_mfe = float(getattr(cfg.book6, 'stx2_arm_mfe', 0.50))
                    if mfe >= arm_mfe:
                        don_floor = float(row.get('low_72h', np.nan))
                        arm_level = active['entry_price'] * 1.005
                        if pd.notna(don_floor) and don_floor > arm_level and c < don_floor:
                            exit_price = c * (1 - slippage)
                            exit_triggered = True
                            exit_reason = "donchian_floor"
                else:
                    t_a_hit = active.get('t_a_hit', False)
                    t_b_hit = active.get('t_b_hit', False)

                    # Tranche A (+8.0% Fast Breakeven Lock)
                    if not t_a_hit and (mfe >= getattr(cfg.book6, 'tranche_a_mfe', 0.08) or h >= active['entry_price'] * (1.0 + getattr(cfg.book6, 'tranche_a_mfe', 0.08))):
                        active['t_a_hit'] = True
                        active['t_a_exit_px'] = active['entry_price'] * (1.0 + getattr(cfg.book6, 'tranche_a_mfe', 0.08))
                        active['stop'] = max(active['stop'], active['entry_price'] * (1.0 - getattr(cfg.book6, 'tranche_a_cushion', 0.002)))

                    # Tranche B (+25.0% Swing Target Cap)
                    if active.get('t_a_hit', False) and not t_b_hit and (mfe >= getattr(cfg.book6, 'tranche_b_mfe', 0.25) or h >= active['entry_price'] * (1.0 + getattr(cfg.book6, 'tranche_b_mfe', 0.25))):
                        active['t_b_hit'] = True
                        active['t_b_exit_px'] = active['entry_price'] * (1.0 + getattr(cfg.book6, 'tranche_b_mfe', 0.25))
                        active['stop'] = max(active['stop'], active['entry_price'] * (1.0 + getattr(cfg.book6, 'tranche_b_floor', 0.08)))
                        active['arm_donchian'] = True

                    # Study S-CG: Studentized Orderflow Liquidation Firewall for Book 6
                    if not exit_triggered and getattr(cfg.book6, 'enable_studentized_oi_firewall', False) and active.get('t_a_hit', False):
                        is_wave1 = check_macro_wave1_genesis(row, c, cfg.exit)
                        if not is_wave1 and mfe >= getattr(cfg.exit, 'climax_min_mfe', 0.20):
                            z_delta_oi = float(row.get('z_delta_oi_24h', 0.0))
                            is_immune = check_whale_squeeze_immunity(row, ls_ratio, cfg.exit)
                            waterfall_z = getattr(cfg.exit, 'studentized_oi_waterfall_z', -2.00)

                            if z_delta_oi <= waterfall_z and not is_immune:
                                t_a_px = active.get('t_a_exit_px', c)
                                t_b_px = active.get('t_b_exit_px', c)
                                harvest_px = c * (1 - slippage)
                                if active.get('t_b_hit', False):
                                    exit_price = (1.0/3.0) * t_a_px + (1.0/3.0) * t_b_px + (1.0/3.0) * harvest_px
                                else:
                                    exit_price = 0.50 * t_a_px + 0.50 * harvest_px
                                exit_triggered = True
                                exit_reason = "studentized_oi_waterfall"

                    # Study S-CE: Dynamic Multi-Signature Climax Harvest & Whale Squeeze Immunity (Book 6 Tranches B & C)
                    elif not exit_triggered and getattr(cfg.book6, 'enable_climax_scoring_harvest', False) and active.get('t_a_hit', False):
                        if mfe >= getattr(cfg.exit, 'climax_min_mfe', 0.20):
                            urg_score = compute_exit_urgency_score(row, c, h, l, o, shock, mfe)
                            is_immune = check_whale_squeeze_immunity(row, ls_ratio, cfg.exit)
                            d_oi_tok = float(row.get('d_oi_tok_peak_24h', 0.0))

                            t_a_px = active.get('t_a_exit_px', c)
                            t_b_px = active.get('t_b_exit_px', c)
                            harvest_px = c * (1 - slippage)

                            if d_oi_tok <= getattr(cfg.exit, 'post_climax_unwind_oi_drop', -0.15) and not is_immune:
                                if active.get('t_b_hit', False):
                                    exit_price = (1.0/3.0) * t_a_px + (1.0/3.0) * t_b_px + (1.0/3.0) * harvest_px
                                else:
                                    exit_price = 0.50 * t_a_px + 0.50 * harvest_px
                                exit_triggered = True
                                exit_reason = "post_climax_unwind"
                            elif urg_score >= getattr(cfg.exit, 'climax_harvest_urgency', 55) and not is_immune:
                                if active.get('t_b_hit', False):
                                    exit_price = (1.0/3.0) * t_a_px + (1.0/3.0) * t_b_px + (1.0/3.0) * harvest_px
                                else:
                                    exit_price = 0.50 * t_a_px + 0.50 * harvest_px
                                exit_triggered = True
                                exit_reason = "climax_top_harvest"
                            elif urg_score >= getattr(cfg.exit, 'climax_ratchet_urgency', 35):
                                vwap_stop = float(row.get('vwap_24h', active['stop'])) * 0.985
                                active['stop'] = max(active['stop'], vwap_stop)

                # Panic Liquidation Bailout: volume >= 3.0x breaking retest floor
                if not exit_triggered:
                    retest_floor = active.get('retest_bot_low', active['entry_price'] * 0.90)
                    if (l < retest_floor * getattr(cfg.book6, 'stop_retest_floor_buffer', 0.995)) and (shock >= getattr(cfg.book6, 'panic_bailout_vol_mult', 3.0)):
                        bailout_px = max(l, retest_floor * 0.98) * (1 - slippage)
                        exit_price = bailout_px
                        exit_triggered = True
                        exit_reason = "panic_liquidation_bailout"

            # Study S-BE & Study S-BR/S-BS: Two-Tranche Target Cap Trigger for Book 4 and Book 1
            if not exit_triggered and book_type == 'Book 1' and active.get('is_b1_twotranche', False) and not active.get('t1_a_hit', False):
                if active.get('target') is not None and h >= active['target']:
                    active['t1_a_hit'] = True
                    active['t1_a_exit_px'] = active['target']
                    cush_pct = getattr(cfg.book1, 'tranche_b_cushion_pct', 0.005) if getattr(cfg, 'book1', None) else 0.005
                    active['stop'] = max(active['stop'], active['entry_price'] * (1.0 - cush_pct)) # Tight -0.5% ratchet cushion
                    active['arm_donchian'] = True
            elif not exit_triggered and book_type == 'Book 4' and not active.get('t1_a_hit', False):
                # Study S-BZ Dynamic Overhead Ceilings & Microstructure Volume Shock
                target_hit = False
                target_px = active.get('target')

                if getattr(cfg.book4, 'enable_dynamic_overhead_targets', True):
                    ema500 = float(row.get('ema500_1d', 1e9))
                    dyn_atr = active.get('target_dynamic_atr')
                    # 1. EMA_500d overhead ceiling in profit >= +5.0%
                    if ema500 >= active['entry_price'] * 1.05 and h >= ema500:
                        target_hit = True
                        target_px = ema500
                    # 2. Dynamic ATR volatility target
                    elif dyn_atr is not None and h >= dyn_atr:
                        target_hit = True
                        target_px = dyn_atr
                    # 3. Microstructure Volume Rejection Shock
                    elif shock >= 2.50 and wick >= 0.33 and c >= active['entry_price'] + 3.0 * float(row.get('atr_24h', 0.0)):
                        target_hit = True
                        target_px = c
                    # 4. Standard structural target fallback
                    elif target_px is not None and h >= target_px:
                        target_hit = True
                else:
                    if target_px is not None and h >= target_px:
                        target_hit = True

                if target_hit:
                    # Tranche A (50%) locks in target
                    active['t1_a_hit'] = True
                    active['t1_a_exit_px'] = target_px
                    # Tranche B (50%) ratchets stop to breakeven cushion (+0.5%) and arms Donchian trail
                    active['stop'] = max(active['stop'], active['entry_price'] * 1.005)
                    active['arm_donchian'] = True
            elif not exit_triggered and book_type == 'Book 7' and not active.get('t1_a_hit', False):
                if active.get('target') is not None and h >= active['target']:
                    active['t1_a_hit'] = True
                    active['t1_a_exit_px'] = active['target']
                    b7_cfg = getattr(cfg, 'book7', None)
                    be_cush = getattr(b7_cfg, 'breakeven_cushion_pct', 0.005) if b7_cfg is not None else 0.005
                    
                    if getattr(b7_cfg, 'enable_microstructure_conditioned_exit', False):
                        # Study S-CK: Check upper wick rejection on trigger bar
                        wick_ratio = (h - max(o, c)) / (h - l + 1e-9) if (h - l) > 1e-9 else 0.0
                        stall_wick = getattr(b7_cfg, 'stall_wick_threshold', 0.40)
                        if wick_ratio >= stall_wick:
                            # Micro-Stall Air Pocket: snug ratchet to save from -48% collapse
                            active['stop'] = max(active['stop'], active['entry_price'] * (1.0 - be_cush))
                            active['is_micro_stall'] = True
                        else:
                            # Clean structural continuation: wide cushion to allow runner breathing room
                            runner_cush = getattr(b7_cfg, 'runner_cushion_pct', 0.030)
                            active['stop'] = max(active['initial_stop'], active['entry_price'] * (1.0 - runner_cush))
                            active['is_clean_runner'] = True
                    else:
                        active['stop'] = max(active['stop'], active['entry_price'] * (1.0 - be_cush))
                    active['arm_donchian'] = True
            elif (
                not exit_triggered
                and not active.get('arm_donchian', False)
                and active.get('target') is not None
                and h >= active['target']
                and not (
                    book_type == 'Book 6'
                    and getattr(cfg.book6, 'stx_skip_a_full_exit', False)
                )
            ):
                # Study S-AY Law 5 / Study S-BB: Two-Tier Target Cap Exit
                # S-TX T1: Book 6 3-SARE must not full-exit at tranche A +8%.
                exit_price = active['target']
                exit_triggered = True
                exit_reason = "target_reclaim"

            # Native Resting Stop-Market Order Execution
            if not exit_triggered:
                if l <= active['stop']:
                    if book_type == 'Book 6':
                        if getattr(cfg.book6, 'stx_real_fill', False):
                            exit_price = min(float(row.get('open', active['stop'])), active['stop']) * (1 - slippage)
                        else:
                            t_a_px = active.get('t_a_exit_px') or active['stop']
                            t_b_px = active.get('t_b_exit_px') or active['stop']
                            t_c_px = active['stop']
                            exit_price = (1.0/3.0) * t_a_px + (1.0/3.0) * t_b_px + (1.0/3.0) * t_c_px
                        exit_triggered = True
                        if active.get('t_b_hit', False):
                            exit_reason = "donchian_floor"
                        elif active.get('t_a_hit', False):
                            exit_reason = "breakeven_ratchet"
                        else:
                            exit_reason = "initial_stop"
                    elif book_type == 'Book 4' and not active.get('t1_a_hit', False):
                        # Hourly catastrophic barrier: If intraday low breaches structural base stop floor,
                        # exit at stop price to prevent catastrophic -25% to -40% tail crashes.
                        exit_price = min(float(row.get('open', active['stop'])), active['stop']) * (1 - slippage)
                        exit_triggered = True
                        exit_reason = "structural_base_stop"
                    elif book_type == 'Book 4' and active.get('is_b4_reentry', False):
                        exit_price = min(o, active['stop'])
                        exit_triggered = True
                        exit_reason = "shakeout_trough_stop"
                    elif book_type == 'Book 4' and active.get('t1_a_hit', False):
                        # Study S-BZ: Tranche B intraday stop is the static breakeven cushion
                        final_stop_px = active['stop']
                        if active.get('t1_b_harvest_hit', False):
                            ratio = getattr(cfg.exit, 'stage3_harvest_ratio', 0.3333333333333333)
                            active['t1_b_exit_px'] = ratio * active['t1_b_harvest_px'] + (1.0 - ratio) * final_stop_px
                        else:
                            active['t1_b_exit_px'] = final_stop_px
                        if getattr(cfg.book4, 'stx_real_fill', False):
                            exit_price = min(float(row.get('open', active['stop'])), active['stop']) * (1 - slippage)
                        else:
                            exit_price = 0.50 * active['t1_a_exit_px'] + 0.50 * active['t1_b_exit_px']
                        exit_triggered = True
                        exit_reason = "breakeven_cushion"
                    elif book_type == 'Book 7':
                        if active.get('t1_a_hit', False):
                            active['t1_b_exit_px'] = active['stop']
                            exit_price = 0.50 * active['t1_a_exit_px'] + 0.50 * active['t1_b_exit_px']
                            exit_triggered = True
                            exit_reason = "breakeven_cushion"
                        else:
                            exit_price = min(float(row.get('open', active['stop'])), active['stop']) * (1 - slippage)
                            exit_triggered = True
                            exit_reason = "initial_stop"
                    elif book_type == 'Book 1' and active.get('t1_a_hit', False):
                        active['t1_b_exit_px'] = active['stop']
                        exit_price = 0.50 * active['t1_a_exit_px'] + 0.50 * active['t1_b_exit_px']
                        exit_triggered = True
                        if active['stop'] >= active['entry_price'] * 1.005:
                            exit_reason = "donchian_floor"
                        elif active['stop'] >= active['entry_price'] * 0.985:
                            exit_reason = "breakeven_ratchet"
                        else:
                            exit_reason = "target_reclaim"
                    else:
                        exit_price = min(float(row.get('open', active['stop'])), active['stop']) * (1 - slippage)
                        exit_triggered = True
                        if active['stop'] >= active['entry_price'] * 1.015:
                            exit_reason = "trail_stop"
                        elif active['stop'] >= active['entry_price'] * 0.965:
                            exit_reason = "breakeven_ratchet"
                        else:
                            exit_reason = "initial_stop"
            # Maximum Holding Duration Time Cap
            if not exit_triggered:
                max_dur = getattr(cfg.book7, 'max_duration_hours', 720) if book_type == 'Book 7' else (getattr(cfg.book6, 'max_duration_hours', 720) if book_type == 'Book 6' else (getattr(cfg.book4, 'max_duration_hours', 720) if book_type == 'Book 4' else (cfg.exit.b2_time_cap_hours if book_type == 'Book 2' else (cfg.exit.time_cap_hours_t1 if is_tier1 else cfg.exit.time_cap_hours_t2))))
                if dur_hours >= max_dur:
                    if book_type == 'Book 6':
                        t_a_px = active.get('t_a_exit_px') or (c * (1 - slippage))
                        t_b_px = active.get('t_b_exit_px') or (c * (1 - slippage))
                        t_c_px = c * (1 - slippage)
                        exit_price = (1.0/3.0) * t_a_px + (1.0/3.0) * t_b_px + (1.0/3.0) * t_c_px
                        exit_triggered = True
                        exit_reason = "time_cap"
                    elif book_type == 'Book 4' and active.get('is_b4_reentry', False):
                        exit_price = c * (1 - slippage)
                        exit_triggered = True
                        exit_reason = "time_cap"
                    elif (book_type in ('Book 4', 'Book 1', 'Book 7')) and active.get('t1_a_hit', False):
                        final_cap_px = c * (1 - slippage)
                        if active.get('t1_b_harvest_hit', False):
                            ratio = getattr(cfg.exit, 'stage3_harvest_ratio', 0.3333333333333333)
                            active['t1_b_exit_px'] = ratio * active['t1_b_harvest_px'] + (1.0 - ratio) * final_cap_px
                        else:
                            active['t1_b_exit_px'] = final_cap_px
                        exit_price = 0.50 * active['t1_a_exit_px'] + 0.50 * active['t1_b_exit_px']
                        exit_triggered = True
                        exit_reason = "time_cap"
                    else:
                        exit_price = c * (1 - slippage)
                        exit_triggered = True
                        exit_reason = "time_cap"

            if exit_triggered:
                if book_type == 'Book 6':
                    t_a_px = active.get('t_a_exit_px') or exit_price
                    t_b_px = active.get('t_b_exit_px') or exit_price
                    t_c_px = exit_price
                    pnl_a = (t_a_px - active['entry_price']) / active['entry_price'] - 0.0010
                    pnl_b = (t_b_px - active['entry_price']) / active['entry_price'] - 0.0010
                    pnl_c = (t_c_px - active['entry_price']) / active['entry_price'] - 0.0010
                    raw_pnl = (1.0/3.0) * pnl_a + (1.0/3.0) * pnl_b + (1.0/3.0) * pnl_c
                elif book_type == 'Book 4' and active.get('is_b4_reentry', False):
                    # Study S-BZ re-entry: single full-size runner, PnL from the actual exit price
                    raw_pnl = (exit_price - active['entry_price']) / active['entry_price'] - 0.0010
                elif (book_type in ('Book 4', 'Book 1', 'Book 7')) and active.get('t1_a_hit', False) and active.get('t1_b_exit_px') is not None:
                    pnl_a = (active['t1_a_exit_px'] - active['entry_price']) / active['entry_price'] - 0.0010
                    pnl_b = (active['t1_b_exit_px'] - active['entry_price']) / active['entry_price'] - 0.0010
                    raw_pnl = 0.50 * pnl_a + 0.50 * pnl_b
                else:
                    raw_pnl = (exit_price - active['entry_price']) / active['entry_price']
                if book_type in ('Book 3', 'Book 5'):
                    w = 1.0
                elif book_type == 'Book 6':
                    # Study S-BP: Continuous Anti-Chase Volatility & Macro Sizing for Book 6
                    w = float(active.get('sizing_weight', 1.0))
                else:
                    w_to = float(np.minimum(1.0, 15.0 / max(1e-4, active.get('turnover_at_entry', 1.0)))) if getattr(cfg.micro, 'enable_turnover_scaling', False) else 1.0
                    w_btc = float(active.get('w_btc', 1.0))

                    if book_type in ('Book 4', 'Book 7'):
                        # Study S-BF & S-CH: Sizing Overlay for Book 4 and Book 7
                        w_vol = active.get('w_vol', 1.0)
                        w = float(np.clip(w_vol * w_btc, 0.10, 1.50))
                    elif book_type in ('Book 1', 'Book 2') and getattr(cfg.sizing, 'enable_csmi_sizing', False):
                        # Study S-BD: Unified Compensatory Squeeze & Momentum Index (CSMI) Sizing Overlay
                        _, _, w_csmi = compute_csmi_metrics(
                            book_type,
                            active.get('rank_ts', 0.50),
                            active.get('pct_lam', 0.50),
                            active.get('dist_ema', 0.0),
                            cfg.sizing
                        )
                        w_conv = float(active.get('w_conviction', 1.0))
                        w = float(np.clip(w_to * w_csmi * w_btc * w_conv, 0.10, 1.50))
                    else:
                        w_lam = float(np.clip(cfg.sizing.base_weight - active.get('pct_lam', 0.50), cfg.sizing.min_weight, cfg.sizing.max_weight)) if cfg.sizing.enable_lambda_sizing else 1.0
                        if book_type == 'Book 1' and getattr(cfg.sizing, 'enable_ticket_size_sizing', False):
                            ts_base = getattr(cfg.sizing, 'ts_base_multiplier', 0.75)
                            ts_slope = getattr(cfg.sizing, 'ts_slope_multiplier', 0.50)
                            ts_min = getattr(cfg.sizing, 'ts_min_multiplier', 0.75)
                            ts_max = getattr(cfg.sizing, 'ts_max_multiplier', 1.25)
                            w_ts = float(np.clip(ts_base + ts_slope * active.get('rank_ts', 0.50), ts_min, ts_max))
                        else:
                            w_ts = 1.0

                        if book_type in ('Book 1', 'Book 4') and getattr(cfg.sizing, 'enable_ema_sizing', False):
                            ema_base = getattr(cfg.sizing, 'ema_base_multiplier', 0.75)
                            ema_slope = getattr(cfg.sizing, 'ema_slope_multiplier', 0.50)
                            ema_min = getattr(cfg.sizing, 'ema_min_multiplier', 0.75)
                            ema_max = getattr(cfg.sizing, 'ema_max_multiplier', 1.25)
                            w_ema = float(np.clip(ema_base + ema_slope * active.get('rank_ema', 0.50), ema_min, ema_max))
                        else:
                            w_ema = 1.0

                        w_conv = float(active.get('w_conviction', 1.0))
                        w = float(np.clip(w_lam * w_to * w_ts * w_ema * w_btc * w_conv, 0.10, 1.50))
                pnl = w * raw_pnl
                log_ret = float(np.log(max(1e-6, 1.0 + pnl)))
                trades.append({
                    'asset': asset,
                    'tier': tier,
                    'book': book_type,
                    'entry': active['entry_time'],
                    'exit': ts,
                    'duration_hours': dur_hours,
                    'entry_price': active['entry_price'],
                    'exit_price': exit_price,
                    'stop_price': active['stop'],
                    'initial_stop': active.get('initial_stop', active['stop']),
                    'raw_pnl': raw_pnl,
                    'pnl': pnl,
                    'sizing_weight': w,
                    'log_ret': log_ret,
                    'mfe': mfe,
                    'mae': mae,
                    'reason': exit_reason,
                    'is_open': False,
                    'is_reclaim': active.get('is_reclaim', False),
                    'is_continuation': active.get('is_continuation', False),
                    'is_book3': active.get('is_book3', False),
                    'pct_lam': active.get('pct_lam', 0.50),
                    'turnover_at_entry': active.get('turnover_at_entry', 1.0),
                    'rank_ts': active.get('rank_ts', 0.50),
                    # MEDIUM-3: entry OI saved for post-trade OI expansion analysis
                    'entry_oi_usd': active.get('entry_oi', 0.0),
                    'w_vol': active.get('w_vol', 1.0),
                    'body_atr_mult': active.get('body_atr_mult', np.nan),
                })
                last_exit_reason = exit_reason
                last_exit_pnl = pnl
                last_entry_price = active['entry_price']
                last_exit_ts = ts
                flush_low_since_exit = l
                sleeve_key = 'Book 1' if book_type in ('Book 1', 'Continuation') else book_type
                last_exit_ts_by_book[sleeve_key] = ts
                if sleeve_key == 'Book 1':
                    last_exit_reason_b1 = exit_reason
                    last_exit_pnl_b1 = pnl
                    last_entry_price_b1 = active['entry_price']
                    flush_low_since_exit_b1 = l

                # Study S-BZ & S-CA: Multi-Day Base CUSUM Re-Entry Engine — arm on breakeven cushion OR shakeout stop
                allow_stopped_reentry = getattr(cfg.book4, 'reentry_allow_stopped_trades', True)
                valid_reentry_exit = (exit_reason == 'breakeven_cushion' and active.get('t1_a_hit', False)) or (
                    allow_stopped_reentry and exit_reason in ('daily_close_below_p_nb', 'structural_daily_close_stop', 'shakeout_trough_stop', 'structural_base_stop')
                )
                if (
                    book_type == 'Book 4' and
                    getattr(cfg.book4, 'enable_multiday_cusum_reentry', True) and
                    valid_reentry_exit and
                    not active.get('is_b4_reentry', False)
                ):
                    scan_dur = getattr(cfg.book4, 'reentry_max_scan_hours', 168)
                    # Arm re-entry queue: track shakeout trough, base low, and the exact structural stop price
                    active_b4_reentry = {
                        'armed_ts': ts,
                        'stop_px': exit_price,
                        'shakeout_trough': l,
                        'consecutive_bars_above_ema200': 0,
                        'avwap_ref': active.get('avwap_tau', active['entry_price']),  # setup AVWAP_tau (frozen at entry)
                        'max_scan_ts': ts + pd.Timedelta(hours=scan_dur),
                        'initial_entry_price': active['entry_price'],
                        'base_low_30d': active.get('base_low_30d', active['stop'] * 0.85),
                        'p_nb_high': active.get('p_nb_high'),
                        'w_confluence': active.get('w_confluence', 1.0),
                        'w_btc': active.get('w_btc', 1.0),
                        'body_atr_mult': active.get('body_atr_mult', 1.0),
                        'stopped_reentry': (exit_reason != 'breakeven_cushion')
                    }
                active_positions[book_name] = None

        # Study S-BZ: Multi-Day Base CUSUM Re-Entry Scanner (runs each bar when armed, Book 4 sleeve is free)
        reentry_tier_ok = (tier == 'Tier 1') or (tier == 'Tier 2' and getattr(cfg.tier, 'tier2_enable_book4', False)) or (tier == 'Tier 3' and getattr(cfg.tier, 'tier3_enable_book4', False))
        if (
            active_b4_reentry is not None and
            active_positions['Book 4'] is None and
            getattr(cfg.book4, 'enable_multiday_cusum_reentry', True) and
            reentry_tier_ok
        ):
            re_ema200 = float(row.get('ema200_1d', c))
            # Update shakeout trough
            if l < active_b4_reentry['shakeout_trough']:
                active_b4_reentry['shakeout_trough'] = l

            # Invalidation: price dumps below 30d base floor or timeout
            base_floor_re = active_b4_reentry.get('base_low_30d', active_b4_reentry['shakeout_trough'] * 0.80)
            if l < base_floor_re:
                active_b4_reentry = None
            elif ts > active_b4_reentry['max_scan_ts']:
                active_b4_reentry = None  # Timeout after scan window
            else:
                # Track consecutive hours holding >= EMA200
                if c >= re_ema200:
                    active_b4_reentry['consecutive_bars_above_ema200'] += 1
                else:
                    active_b4_reentry['consecutive_bars_above_ema200'] = 0

                atr_24 = float(row.get('atr_24h', row.get('atr_24', c * 0.02)))
                if atr_24 <= 0.0:
                    atr_24 = float(row.get('atr', c * 0.02))
                atr_168 = float(row.get('atr_168h', atr_24)) if pd.notna(row.get('atr_168h')) else atr_24
                vol_comp = (atr_24 / max(1e-5, atr_168)) if atr_168 > 0 else 1.0

                # =========================================================================
                # SOVEREIGN CONTINUOUS FAVOURABILITY ENGINE (Study S-BZ)
                # Eliminates the "same old binary gates" (no hard cliffs on time, CUSUM, L/S, RS)
                # Physical condition: Price pushes past the structural stop (c > stop_ref) or AVWAP
                # while holding above the 30-day base low.
                # All other factors continuously modulate Favourability Index (Phi_t in [0.25, 1.50])
                # =========================================================================
                avwap_ref = active_b4_reentry['avwap_ref']
                initial_px = active_b4_reentry.get('initial_entry_price', avwap_ref)
                stop_ref = active_b4_reentry.get('stop_px', initial_px)

                # Physical Reclaim Event: Price must physically push past the structural stop or AVWAP
                has_gone_past_stop = (c > stop_ref)
                has_reclaim = (c >= avwap_ref) or (c >= initial_px) or has_gone_past_stop

                # 1. Continuous Base Maturity Factor (S_time):
                # Tier-Specific dynamic reference duration: Tier 1: 96h, Tier 2: 72h, Tier 3: 48h
                h_ref = 96.0 if tier == 'Tier 1' else (72.0 if tier == 'Tier 2' else 48.0)
                h_base = float(np.clip(h_ref * vol_comp, 36.0, 120.0))
                hours_since_exit = (ts - active_b4_reentry['armed_ts']).total_seconds() / 3600.0
                tau_base = hours_since_exit / max(1.0, h_base)
                s_time = float(np.clip(0.35 + 0.65 * min(1.5, tau_base), 0.35, 1.15))

                # 2. Continuous CUSUM Orderflow Momentum Factor (Psi_cusum):
                s_pos_72 = float(row.get('cusum_pos_72', 0.0))
                psi_cusum = float(np.clip(0.70 + 0.35 * (s_pos_72 / 1.50), 0.60, 1.35))

                # 3. Continuous Whale Positioning & Squeeze Factor (Omega_whale):
                ls_r = float(ls_ratio) if pd.notna(ls_ratio) else 1.0
                omega_whale = float(np.clip(1.0 + 0.45 * (1.0 - ls_r), 0.65, 1.35))

                # 4. Continuous Relative Strength vs BTC Factor (Gamma_rs):
                rs_val = float(row.get('rs_vs_btc', 0.0))
                gamma_rs = float(np.clip(1.0 + 0.75 * rs_val, 0.65, 1.35))

                # Composite Sovereign Favourability Index (Phi_t):
                # Smooth continuous interaction of all 4 dimensions
                phi_t = float(np.clip(s_time * psi_cusum * omega_whale * gamma_rs, 0.25, 1.50))

                is_stopped = active_b4_reentry.get('stopped_reentry', False)
                p_nb_re_ok = True
                if getattr(cfg.book4, 'enable_p_nb_day_close_confirmation', False):
                    p_nb_re_ref = active_b4_reentry.get('p_nb_high')
                    if p_nb_re_ref is not None and p_nb_re_ref > 0:
                        is_day_close_bar = (ts.hour == 23)
                        p_nb_re_ok = is_day_close_bar and (c >= p_nb_re_ref)

                if is_stopped:
                    # Physical trigger: must push past the structural stop or AVWAP, with net positive composite favourability
                    reentry_triggered = has_reclaim and p_nb_re_ok and (phi_t >= 0.95)
                else:
                    reentry_triggered = (active_b4_reentry['consecutive_bars_above_ema200'] >= 24) and has_reclaim and p_nb_re_ok and (phi_t >= 0.85)

                if reentry_triggered:
                    cal_cfg = getattr(cfg, 'calendar', None)
                    skip_reentry = False
                    if cal_cfg and cal_cfg.enable_calendar_firewall:
                        is_mon = (ts.dayofweek == 0)
                        is_mstart = ts.is_month_start
                        is_mend = ts.is_month_end
                        if (cal_cfg.veto_monday and is_mon) or (cal_cfg.veto_month_start and is_mstart) or (cal_cfg.veto_month_end and is_mend):
                            skip_reentry = True
                    if not skip_reentry:
                        # Execute re-entry: Tranche B only (full position, standalone)
                        shakeout_trough = active_b4_reentry['shakeout_trough']
                        market_px = c * (1 + slippage)
                        avwap_ref = active_b4_reentry.get('avwap_ref')
                        if getattr(cfg.book4, 'enable_staged_avwap_entry', True) and avwap_ref is not None and l <= avwap_ref:
                            fill_px = 0.50 * avwap_ref + 0.50 * market_px
                        else:
                            fill_px = market_px

                        # Volatility-Adaptive Retest Stop: ATR-proportional buffer below trough
                        atr_norm_re = (atr_24 / fill_px) if fill_px > 0 else 0.02
                        re_buf = 0.50 * atr_norm_re if tier == 'Tier 1' else (0.75 * atr_norm_re if tier == 'Tier 2' else 1.00 * atr_norm_re)
                        re_buf = float(np.clip(re_buf, 0.005, 0.025))
                        re_max_risk = 0.10 if tier == 'Tier 1' else (0.14 if tier == 'Tier 2' else 0.18)
                        reentry_stop = max(shakeout_trough * (1.0 - re_buf), fill_px * (1.0 - re_max_risk))

                        w_btc_re = 1.0 if btc_bull else getattr(cfg.book4, 'bear_sizing_mult', 0.50)
                        w_conf_re = active_b4_reentry.get('w_confluence', 1.0)
                        body_atr_re = 1.0
                        w_vol_re = 1.0
                        if getattr(cfg.book4, 'enable_anti_chase_sizing', True):
                            bar_body = abs(c - o)
                            body_atr_re = bar_body / atr_24 if atr_24 > 0.0 else 1.0
                            th = getattr(cfg.book4, 'anti_chase_threshold', 1.50)
                            slope = getattr(cfg.book4, 'anti_chase_decay_slope', 0.35)
                            min_m = getattr(cfg.book4, 'anti_chase_min_multiplier', 0.50)
                            max_m = getattr(cfg.book4, 'anti_chase_max_multiplier', 1.20)
                            w_vol_re = float(np.clip(max_m - slope * max(0.0, body_atr_re - th), min_m, max_m))

                        # Continuous Dynamic Liquidity Multiplier (w_liq)
                        to_val_re = float(turnover) if pd.notna(turnover) else 1.0
                        to_ref_re = 15.0 if tier == 'Tier 1' else (5.0 if tier == 'Tier 2' else 1.5)
                        v_t_re = to_val_re / max(0.1, to_ref_re)
                        w_liq_re = float(np.clip(0.85 + 0.35 * (v_t_re - 1.0), 0.35, 1.25))

                        # Continuous Dynamic Favourability Scaling (Phi_t & w_liq)
                        w_vol_re = float(np.clip(w_vol_re * w_liq_re * phi_t, 0.20, 1.50))

                        active_positions['Book 4'] = {
                            'entry_time': ts,
                            'entry_price': fill_px,
                            'stop': reentry_stop,
                            'initial_stop': reentry_stop,
                            'target': None,  # Tranche B: unconstrained runner
                            'max_high': h,
                            'min_low': l,
                            'book': 'Book 4',
                            'is_reclaim': True,
                            'is_continuation': False,
                            'is_b4_reentry': True,  # Flag for telemetry
                            'entry_oi': current_oi,
                            'pct_lam': float(row.get('pct_lambda', 0.50)),
                            'turnover_at_entry': float(turnover) if pd.notna(turnover) else 1.0,
                            'rank_ts': float(row.get('rank_ts_168h', 0.50)),
                            'rank_ema': float(row.get('rank_ema_168h', 0.50)),
                            'w_btc': w_btc_re,
                            'w_vol': w_vol_re,
                            'w_confluence': w_conf_re,
                            'body_atr_mult': body_atr_re,
                            't1_a_hit': True,  # Re-entry is Tranche B equivalent — skip Tranche A target
                            't1_a_exit_px': fill_px,  # Placeholder: blended PnL effectively 100% Tranche B
                            't1_b_exit_px': None,
                            'arm_donchian': True,  # Immediately arm 72h Donchian trailing floor
                            'p_nb_high': active_b4_reentry.get('p_nb_high'),
                            'target_dynamic_atr': fill_px + getattr(cfg.book4, 'atr_target_multiple', 6.0) * atr_24,
                        }
                        active_b4_reentry = None
                        if telemetry:
                            telemetry.log_signal(TelemetryRecord(
                                timestamp=ts, asset=asset, tier=tier, status="ACTIVE",
                                veto_gate="None", candidate_setup="Book 4 S-BZ Multi-Day CUSUM Re-Entry",
                                price=fill_px, turnover=float(turnover) if pd.notna(turnover) else 1.0,
                                ls_ratio=float(ls_ratio) if pd.notna(ls_ratio) else 1.0,
                                funding_rate=float(fr) if pd.notna(fr) else 0.0,
                                btc_macro_bull=btc_bull
                            ))
                        continue

        # -------------------------------------------------------------
        # 2. ENTRY EVALUATION & SLEEVE DISPATCHING
        # -------------------------------------------------------------
        if any(pos is None for pos in active_positions.values()):
            time_since_exit_b1 = (ts - last_exit_ts_by_book['Book 1']).total_seconds() / 3600.0 if last_exit_ts_by_book['Book 1'] is not None else 9999.0
            time_since_exit_b2 = (ts - last_exit_ts_by_book['Book 2']).total_seconds() / 3600.0 if last_exit_ts_by_book['Book 2'] is not None else 9999.0
            time_since_exit_b4 = (ts - last_exit_ts_by_book['Book 4']).total_seconds() / 3600.0 if last_exit_ts_by_book['Book 4'] is not None else 9999.0
            time_since_exit = (ts - last_exit_ts).total_seconds() / 3600.0 if last_exit_ts is not None else 9999.0
            time_since_exit = (ts - last_exit_ts).total_seconds() / 3600.0 if last_exit_ts is not None else 9999.0

            # Study S-P: Point-in-Time Shadow Anchor Tracking
            can_shadow_reclaim = False
            if getattr(cfg.shadow_reclaim, 'enable_bear_shadow_reclaims', False) and active_shadow_anchor is not None:
                elapsed_h = (ts - active_shadow_anchor['armed_ts']).total_seconds() / 3600.0
                if elapsed_h > cfg.shadow_reclaim.reclaim_max_hours:
                    active_shadow_anchor = None  # Expired zombie breakdown
                else:
                    active_shadow_anchor['flush_low'] = min(active_shadow_anchor['flush_low'], l)
                    if (elapsed_h >= cfg.shadow_reclaim.reclaim_min_hours) and (c >= active_shadow_anchor['anchor_px']) and (c > float(row.get('ema_168', 0.0))):
                        can_shadow_reclaim = True

            # Candidate Pattern Detection
            is_breakout = bool(row.get('breakout_21d', False))
            ret_14d = float(row.get('ret_14d', 0.0))
            rs_btc = float(row.get('rs_vs_btc', 0.0))
            is_above_ma = c > float(row.get('ema_168', 0.0))
            oi_14d = float(row.get('oi_change_14d', 0.0))

            # Book 2 Coiled Squeeze Breakout Candidate (Reverse-Engineered from Pure Shards)
            is_b2_candidate = False
            if cfg.micro.enable_book2:
                is_b2_stressed = (ls_ratio < cfg.micro.b2_max_ls) or (fr <= 0.0)
                shelf_rng_72 = float(row.get('shelf_range_72h', 1.0))
                dist_72_low = float(row.get('dist_from_72h_low', 1.0))
                ret_7d = float(row.get('ret_7d', 0.0))
                d_oi_usd = float(row.get('d_oi_usd_24h', 0.0))
                taker = float(row.get('taker_ratio', 0.50))
                high_72 = float(row.get('high_72h', c))

                is_b2_candidate = (
                    is_b2_stressed and
                    (shelf_rng_72 <= cfg.micro.b2_max_shelf_range) and
                    (ret_7d <= cfg.micro.b2_max_ret_7d) and
                    (d_oi_usd <= cfg.micro.b2_max_d_oi_usd_24h) and
                    (time_since_exit_b2 >= cfg.micro.b2_cooldown_hours) and
                    (c > high_72) and
                    (dist_72_low <= cfg.micro.b2_max_dist_72h_low) and
                    (taker <= cfg.micro.b2_max_taker_ratio) and
                    (shock >= cfg.micro.b2_min_vol_shock) and
                    (turnover >= cfg.micro.min_turnover_velocity) and (turnover <= cfg.micro.b2_max_turnover_velocity)
                )

            # Bear Trap V-Reclaim Candidate (Study S-P)
            can_reclaim = (
                time_since_exit_b1 >= cfg.entry.reclaim_min_hours and
                time_since_exit_b1 <= cfg.entry.reclaim_max_hours and
                last_exit_reason_b1 in ['initial_stop', 'trail_stop'] and
                (last_exit_pnl_b1 < 0.0 and last_exit_pnl_b1 >= cfg.entry.reclaim_max_pnl_loss) and
                (c >= last_entry_price_b1 or is_breakout) and
                is_above_ma
            )

            # Study S-U High-Shelf Continuation Candidate (with Relative Strength Primacy)
            shelf_range = float(row.get('shelf_range_14d', 999.0))
            high_14d = float(row.get('high_14d', 0.0))
            low_14d = float(row.get('low_14d', 0.0))
            is_continuation_candidate = False
            if cfg.entry.enable_continuation and is_above_ma:
                is_continuation_candidate = (
                    (shelf_range <= cfg.entry.continuation_max_shelf_range) and
                    (c > high_14d) and
                    (shock >= cfg.entry.continuation_min_vol_shock) and
                    (turnover >= cfg.entry.continuation_min_turnover) and
                    (ls_ratio >= cfg.entry.continuation_min_toptrader_ls) and
                    (time_since_exit_b1 >= cfg.entry.continuation_cooldown_hours) and
                    (dist_60d >= cfg.entry.continuation_min_dist_60d) and
                    (rs_btc >= cfg.entry.continuation_min_rs_btc) and
                    (ret_14d >= cfg.entry.continuation_min_14d_ret)
                )

            # Study S-BY & S-BZ: Causal Point-in-Time Higher-Low Retest & Reclaim State Machine (Book 4 Engine)
            ema200 = float(row.get('ema200_1d', c))
            is_b4_touch = bool(row.get('is_200d_touch', False))
            b4_cfg = getattr(cfg, 'book4', None)
            b4_enabled = getattr(b4_cfg, 'enable_book4', True) if b4_cfg is not None else True

            # State 1: Armed on Canary Touch & AVWAP Anchor (with 120h post-exit cooldown & Tier gates)
            b4_last_exit = last_exit_ts_by_book.get('Book 4')
            b4_cd_hours = getattr(b4_cfg, 'cooldown_hours', 120) if b4_cfg is not None else 120
            b4_cooldown_ok = (b4_last_exit is None) or ((ts - b4_last_exit).total_seconds() >= b4_cd_hours * 3600)
            tier2_b4_ok = getattr(cfg.tier, 'tier2_enable_book4', False) if tier == 'Tier 2' else True
            tier3_b4_ok = getattr(cfg.tier, 'tier3_enable_book4', False) if tier == 'Tier 3' else True
            is_tier_b4_ok = (tier == 'Tier 1') or (tier == 'Tier 2' and tier2_b4_ok) or (tier == 'Tier 3' and tier3_b4_ok)
            if is_b4_touch and b4_enabled and is_tier_b4_ok and (active_positions['Book 4'] is None) and b4_cooldown_ok:
                pre_start = max(0, _bar_i - getattr(b4_cfg, 'min_bars_below', 720))
                base_low_30d = float(l_arr[pre_start : _bar_i].min()) if _bar_i > 0 else l
                if active_b4_setup is None:
                    daily_df = getattr(df, 'attrs', {}).get('daily_df', None)
                    p_nb_high = None
                    if daily_df is not None:
                        canary_date = pd.Timestamp(ts).floor('D')
                        p_nb_val, _, _ = extract_p_nb_high(daily_df, canary_date, c)
                        if p_nb_val is not None and p_nb_val > 0:
                            p_nb_high = p_nb_val
                    if p_nb_high is None or p_nb_high <= 0:
                        p_nb_high = float(np.max(h_arr[pre_start : _bar_i])) if _bar_i > 0 else h

                    active_b4_setup = {
                        'tau_bar': _bar_i,
                        'tau_ts': ts,
                        'p0': c,
                        'p_nb_high': p_nb_high,
                        'peak_high': h,
                        'base_low_30d': base_low_30d,
                        'cum_pv': c * qv_arr[_bar_i],
                        'cum_v': qv_arr[_bar_i],
                        'retest_low': l,
                        'retest_bar': _bar_i,
                        'retest_found': False,
                    }
                else:
                    if h > active_b4_setup.get('peak_high', h):
                        active_b4_setup['peak_high'] = h

            is_b4_candidate = False
            if active_b4_setup is not None and (_bar_i > active_b4_setup['tau_bar']):
                active_b4_setup['cum_pv'] += c * qv_arr[_bar_i]
                active_b4_setup['cum_v'] += qv_arr[_bar_i]
                avwap_tau = active_b4_setup['cum_pv'] / max(1e-5, active_b4_setup['cum_v'])
                bars_since_touch = _bar_i - active_b4_setup['tau_bar']

                if h > active_b4_setup.get('peak_high', h):
                    active_b4_setup['peak_high'] = h

                # Book 6 Style Retest Corridor: Price pulls back into [0.90, 1.03] of AVWAP_tau
                if (bars_since_touch >= 4) and (bars_since_touch <= 168):
                    if (l <= avwap_tau * 1.03) and (l >= avwap_tau * 0.90):
                        if l > active_b4_setup['base_low_30d']:
                            active_b4_setup['retest_found'] = True
                            if l < active_b4_setup['retest_low']:
                                active_b4_setup['retest_low'] = l
                                active_b4_setup['retest_bar'] = _bar_i

                # Invalidation checks: breaks 30d base floor or retest timeout > 168h (7 days)
                if (
                    l <= active_b4_setup['base_low_30d'] or
                    bars_since_touch > 168
                ):
                    active_b4_setup = None
                else:
                    # Buy Trigger: Price reclaims AVWAP_tau directly from the retest corridor!
                    reclaimed_b4 = (c > avwap_tau) and (c >= ema200 * 0.98)
                    p_nb_ok = True
                    if getattr(cfg.book4, 'enable_p_nb_day_close_confirmation', False):
                        p_nb_ref = active_b4_setup.get('p_nb_high')
                        if p_nb_ref is not None and p_nb_ref > 0:
                            is_day_close_bar = (ts.hour == 23)
                            p_nb_ok = is_day_close_bar and (c >= p_nb_ref)

                    # Study S-CD: Dynamic Toxic Whale Long Trap Firewall (Rule 7)
                    toxic_long_b4 = False
                    if getattr(cfg.book4, 'enable_toxic_long_firewall', False):
                        pct_ls_b4 = float(row.get('pct_ls_30d', 50.0))
                        z_ls_b4 = float(row.get('z_ls_30d', 0.0))
                        if (pct_ls_b4 >= getattr(cfg.book4, 'toxic_long_pct_ls', 80.0)) and (z_ls_b4 >= getattr(cfg.book4, 'toxic_long_z_ls', 0.80)):
                            toxic_long_b4 = True

                    if (
                        active_b4_setup['retest_found'] and
                        reclaimed_b4 and
                        p_nb_ok and
                        not toxic_long_b4 and
                        b4_enabled and
                        is_tier_b4_ok
                    ):
                        is_b4_candidate = True

            # Study S-BR & S-BS: Book 1 AVWAP Retest Reclaim Candidate Check
            is_b1_avwap_candidate = False
            if (
                getattr(cfg, 'book1', None) and
                getattr(cfg.book1, 'enable_avwap_reclaim', True) and
                active_b1_anchor is not None and
                (_bar_i > active_b1_anchor['tau_bar'])
            ):
                avwap_val = active_b1_anchor['cum_pv'] / max(1e-5, active_b1_anchor['cum_v'])
                tol = getattr(cfg.book1, 'avwap_corridor_tolerance', 0.05)
                held_retest = (active_b1_anchor['retest_low'] >= active_b1_anchor['base_low']) and (active_b1_anchor['retest_low'] <= avwap_val * (1.0 + tol))
                reclaimed = (c >= avwap_val) and is_above_ma

                # Derivatives Quality Filters
                fr_z = float(row.get('funding_z', 0.0))
                fr_z_ok = fr_z <= getattr(cfg.book1, 'max_funding_z', 1.0)
                tok_oi_ok = d_oi_tok <= getattr(cfg.book1, 'max_token_oi_expansion', 0.30)
                is_passed = active_b1_anchor.get('consolidation_passed', True)
                if held_retest and reclaimed and fr_z_ok and tok_oi_ok and whales_not_dumping and is_passed:
                    is_b1_avwap_candidate = True

            # Study S-BP: Book 6 3-SARE Orderflow Base Reclaim Candidate Check (Tier 2 only)
            is_b6_candidate = False
            if (
                getattr(cfg, 'book6', None) and
                getattr(cfg.book6, 'enable_book6', True) and
                (tier == 'Tier 2') and
                active_b6_setup is not None and
                active_b6_setup.get('retest_found', False) and
                (_bar_i > active_b6_setup['retest_bar'])
            ):
                cur_b6_avwap = active_b6_setup['cum_pv'] / max(1e-5, active_b6_setup['cum_v'])
                reclaimed_b6 = (c > cur_b6_avwap)
                whale_frontrun = (d_ls_24h >= cfg.book6.whale_frontrun_veto_delta)

                # Study S-CD: Dynamic Toxic Whale Long Trap Firewall (Rule 7)
                toxic_long_b6 = False
                if getattr(cfg.book6, 'enable_toxic_long_firewall', False):
                    pct_ls_b6 = float(row.get('pct_ls_30d', 50.0))
                    z_ls_b6 = float(row.get('z_ls_30d', 0.0))
                    if (pct_ls_b6 >= getattr(cfg.book6, 'toxic_long_pct_ls', 80.0)) and (z_ls_b6 >= getattr(cfg.book6, 'toxic_long_z_ls', 0.80)):
                        toxic_long_b6 = True

                # Study S-CD: Studentized OI Absorption Gate at Retest
                oi_abs_ok = True
                if getattr(cfg.book6, 'enable_oi_absorption_filter', False):
                    z_oi_b6 = float(row.get('z_oi_12h', 0.0))
                    if z_oi_b6 < 0.0:
                        oi_abs_ok = False

                if reclaimed_b6 and not whale_frontrun and not toxic_long_b6 and oi_abs_ok:
                    is_b6_candidate = True

            # Study S-CH: Book 7 Micro-Cap Supernova & Base Squeeze Candidate Check (Tier 3 only)
            is_b7_candidate = False
            b7_cfg = getattr(cfg, 'book7', None)
            if (
                b7_cfg and
                b7_cfg.enable_book7 and
                (tier == 'Tier 3')
            ):
                b7_last_exit = last_exit_ts_by_book.get('Book 7')
                b7_cd_hours = getattr(b7_cfg, 'cooldown_hours', 120)
                b7_cooldown_ok = (b7_last_exit is None) or ((ts - b7_last_exit).total_seconds() >= b7_cd_hours * 3600)
                touch_tol_b7 = getattr(b7_cfg, 'touch_tolerance_pct', 0.015)
                min_bel_b7 = getattr(b7_cfg, 'min_bars_below', 720)
                ema200_val_b7 = float(row.get('ema200_1d', c))
                is_b7_touch = (h >= ema200_val_b7 * (1.0 - touch_tol_b7)) and (float(row.get('bars_below_ema200_1d', 0)) >= min_bel_b7)

                if is_b7_touch and (active_positions['Book 7'] is None) and b7_cooldown_ok:
                    pre_start_b7 = max(0, _bar_i - getattr(b7_cfg, 'min_bars_below', 720))
                    base_low_b7 = float(l_arr[pre_start_b7 : _bar_i].min()) if _bar_i > 0 else l
                    if active_b7_setup is None:
                        active_b7_setup = {
                            'tau_bar': _bar_i,
                            'tau_ts': ts,
                            'p0': c,
                            'peak_high': h,
                            'base_low_30d': base_low_b7,
                            'cum_pv': c * qv_arr[_bar_i],
                            'cum_v': qv_arr[_bar_i],
                            'retest_low': l,
                            'retest_bar': _bar_i,
                            'retest_found': False,
                        }
                    else:
                        if h > active_b7_setup.get('peak_high', h):
                            active_b7_setup['peak_high'] = h

                if active_b7_setup is not None and (_bar_i > active_b7_setup['tau_bar']):
                    active_b7_setup['cum_pv'] += c * qv_arr[_bar_i]
                    active_b7_setup['cum_v'] += qv_arr[_bar_i]
                    avwap_tau_b7 = active_b7_setup['cum_pv'] / max(1e-5, active_b7_setup['cum_v'])
                    bars_since_b7 = _bar_i - active_b7_setup['tau_bar']
                    if h > active_b7_setup.get('peak_high', h):
                        active_b7_setup['peak_high'] = h

                    if (bars_since_b7 >= 4) and (bars_since_b7 <= b7_cfg.max_retest_hours):
                        if (l <= avwap_tau_b7 * 1.03) and (l >= avwap_tau_b7 * 0.90):
                            if l > active_b7_setup['base_low_30d']:
                                active_b7_setup['retest_found'] = True
                                if l < active_b7_setup['retest_low']:
                                    active_b7_setup['retest_low'] = l
                                    active_b7_setup['retest_bar'] = _bar_i

                    if (l <= active_b7_setup['base_low_30d']) or (bars_since_b7 > b7_cfg.max_retest_hours):
                        active_b7_setup = None
                    else:
                        reclaimed_b7 = (c > avwap_tau_b7)

                        # 4 Sovereign Micro-Cap Safeguards:
                        # 1. Over-Extension Clamp: Entry within [-5%, +12%] of 200d EMA
                        ema200 = float(row.get('ema200_1d', c))
                        dist_200d = (c - ema200) / (ema200 + 1e-8)
                        ext_ok = (dist_200d >= b7_cfg.min_dist_200d) and (dist_200d <= b7_cfg.max_dist_200d)

                        # 2. Whale Squeeze Fuel Gate: pct_ls <= 15% or z_ls <= -1.25 sigma
                        pct_ls_b7 = float(row.get('pct_ls_30d', 50.0))
                        z_ls_b7 = float(row.get('z_ls_30d', 0.0))
                        squeeze_fuel_ok = (pct_ls_b7 <= b7_cfg.max_pct_ls) or (z_ls_b7 <= b7_cfg.max_z_ls)

                        # 3. Leverage Bubble Firewall: Dynamic Heuristic (Rule 7) vs Legacy Static
                        if getattr(b7_cfg, 'enable_studentized_oi_bubble', False):
                            z_oi_val = float(row.get('z_oi_12h', 0.0))
                            leverage_ok = (z_oi_val <= getattr(b7_cfg, 'max_z_oi', 2.00))
                        elif getattr(b7_cfg, 'enable_percentile_oi_bubble', False):
                            pct_oi_val = float(row.get('pct_doi_30d', 50.0))
                            leverage_ok = (pct_oi_val <= getattr(b7_cfg, 'max_pct_oi', 90.0))
                        else:
                            d_oi_tok_b7 = float(row.get('d_oi_tokens_24h', 0.0))
                            leverage_ok = (d_oi_tok_b7 <= b7_cfg.max_d_oi_tokens)

                        # 4. Minimum Turnover
                        to_val_b7 = float(turnover) if pd.notna(turnover) else 0.0
                        to_ok = (to_val_b7 >= b7_cfg.min_turnover)

                        # 5. Negative Carry Inverted Squeeze Gate (Study S-CI & S-CJ Studentized Carry)
                        carry_ok = True
                        if getattr(b7_cfg, 'require_negative_carry', False):
                            fr_b7 = float(row.get('funding_rate', 0.0))
                            fr_z = float(row.get('funding_z', 0.0))
                            if getattr(b7_cfg, 'enable_studentized_carry', False):
                                max_z_fnd = getattr(b7_cfg, 'max_z_funding', 0.25)
                                if getattr(b7_cfg, 'enable_whale_carry_override', False):
                                    ov_z_ls = getattr(b7_cfg, 'whale_override_max_z_ls', -1.50)
                                    ov_z_fnd = getattr(b7_cfg, 'whale_override_max_z_fnd', 0.50)
                                    if z_ls_b7 <= ov_z_ls:
                                        max_z_fnd = max(max_z_fnd, ov_z_fnd)
                                carry_ok = (fr_b7 <= getattr(b7_cfg, 'max_funding_rate', 0.0)) or (fr_z <= max_z_fnd)
                            else:
                                carry_ok = (fr_b7 <= getattr(b7_cfg, 'max_funding_rate', 0.0))

                        # Calendar Firewall
                        cal_ok = True
                        cal_cfg = getattr(cfg, 'calendar', None)
                        if cal_cfg and cal_cfg.enable_calendar_firewall:
                            if (cal_cfg.veto_monday and ts.dayofweek == 0) or (cal_cfg.veto_month_start and ts.is_month_start) or (cal_cfg.veto_month_end and ts.is_month_end):
                                cal_ok = False

                        # Study S-CL: Direct Breakout Mode (Zero Retest Delay under Extreme Whale Squeeze Conviction)
                        direct_ok = False
                        if getattr(b7_cfg, 'enable_direct_breakout', False):
                            direct_z_ls = getattr(b7_cfg, 'direct_breakout_max_z_ls', -1.50)
                            if (z_ls_b7 <= direct_z_ls) and (c >= ema200):
                                direct_ok = True

                        if (
                            (active_b7_setup['retest_found'] or direct_ok) and
                            reclaimed_b7 and
                            ext_ok and
                            squeeze_fuel_ok and
                            leverage_ok and
                            to_ok and
                            carry_ok and
                            cal_ok
                        ):
                            is_b7_candidate = True

            use_avwap_mode = getattr(cfg, 'book1', None) and getattr(cfg.book1, 'enable_avwap_reclaim', True)
            b1_cand = is_b1_avwap_candidate if use_avwap_mode else is_breakout

            is_candidate = is_b4_candidate or is_b6_candidate or is_b7_candidate or is_b2_candidate or can_reclaim or can_shadow_reclaim or b1_cand or is_continuation_candidate
            if not is_candidate:
                continue

            if is_b4_candidate:
                candidate_setup = "200d EMA Reclaim"
            elif is_b6_candidate:
                candidate_setup = "3-SARE Base Reclaim"
            elif is_b7_candidate:
                candidate_setup = "MSSR Supernova Squeeze"
            elif is_b2_candidate:
                candidate_setup = "Squeeze Hunter"
            elif is_b1_avwap_candidate:
                candidate_setup = "Dormant AVWAP Reclaim"
            elif can_shadow_reclaim:
                candidate_setup = "Bear-Trap S-P Reclaim"
            elif can_reclaim:
                candidate_setup = "Bear-Trap V-Reclaim"
            elif is_continuation_candidate:
                candidate_setup = "High-Shelf Continuation"
            else:
                candidate_setup = "Continuation Breakout"

            def _try_arm_flush_bid(gate_name: str):
                nonlocal active_flush_bid
                if (
                    getattr(cfg.book3_flush, 'enable_book3_flush_reclaim', False) and
                    btc_bull and
                    (active_positions['Book 3'] is None) and
                    (active_flush_bid is None)
                ):
                    # Dynamic Tier Filtering for Book 3 (Study S-AC V12.2 Optimization)
                    if tier == 'Tier 1' and not getattr(cfg.book3_flush, 'enable_tier1', True):
                        return
                    t2_whitelisted = (tier == 'Tier 2') and (gate_name in getattr(cfg.book3_flush, 'tier2_gate_whitelist', ()))
                    if tier == 'Tier 2' and not getattr(cfg.book3_flush, 'enable_tier2', False) and not t2_whitelisted:
                        return
                    if tier == 'Tier 3' and not getattr(cfg.book3_flush, 'enable_tier3', True):
                        return

                    discount = (
                        cfg.book3_flush.tier2_flush_discount_pct
                        if (tier == 'Tier 2' and not t2_whitelisted)
                        else cfg.book3_flush.flush_discount_pct
                    )
                    base_bid = c * (1.0 - discount)
                    bid_p = base_bid
                    target_p = c
                    stop_p = bid_p * (1.0 - cfg.book3_flush.max_initial_risk)
                    ttl_bars = cfg.book3_flush.ttl_hours

                    # Canonical V12.3 (Study S-AN / S-AO): Two-Tier Volume Profile Shelf Absorption with Static Fallback
                    shelf_mode = getattr(cfg.book3_flush, 'book3_shelf_mode', 'shelf_fallback')
                    if shelf_mode == 'shelf_fallback':
                        vp = _get_vp(_bar_i)
                        if vp is not None:
                            lo_px = cfg.book3_flush.corridor_lo * c
                            hi_px = cfg.book3_flush.corridor_hi * c
                            in_corr = (vp['highs'] >= lo_px) & (vp['lows'] <= hi_px)
                            hvn = in_corr & (vp['vols'] >= cfg.book3_flush.hvn_mult_support * vp['mean'])
                            if hvn.any():
                                idx = np.flatnonzero(hvn)
                                best = idx[np.argmax(vp['vols'][idx])]
                                bid_p = float(np.clip(vp['highs'][best], lo_px, hi_px))
                                stop_p = bid_p * (1.0 - cfg.book3_flush.max_initial_risk)

                    active_flush_bid = {
                        'trigger_px': c,
                        'bid_px': bid_p,
                        'stop_px': stop_p,
                        'target_px': target_p,
                        'armed_ts': ts,
                        'ttl_bars': ttl_bars,
                        'veto_gate': gate_name,
                        'candidate_setup': candidate_setup
                    }

            # --- GATE AUDITING & DEFENSIVE VETO CHECKS ---
            # 0. Zero-Tolerance Data Quality Firewall (Core 0)
            # Strictly forbids entry if Open Interest (< $100k), Top Trader L/S, or Funding Rate is missing/NaN
            has_valid_oi = (current_oi >= 1e5)
            has_valid_ls = pd.notna(ls_ratio) and (ls_ratio > 0.0)
            has_valid_fr = pd.notna(fr)
            has_valid_turnover = pd.notna(turnover) and (turnover > 0.0)

            if not (has_valid_oi and has_valid_ls and has_valid_fr and has_valid_turnover):
                if telemetry:
                    telemetry.log_signal(TelemetryRecord(
                        timestamp=ts, asset=asset, tier=tier, status="VETOED",
                        veto_gate="Core 0: Zero-Tolerance Data Firewall", candidate_setup=candidate_setup,
                        price=c, turnover=turnover if pd.notna(turnover) else 0.0,
                        ls_ratio=ls_ratio if pd.notna(ls_ratio) else 1.0,
                        funding_rate=fr if pd.notna(fr) else 0.0,
                        btc_macro_bull=btc_bull
                    ))
                continue

            # Core 5: Temporal Calendar Boundary Firewall (Study S-BV & S-BX V13.3)
            cal_cfg = getattr(cfg, 'calendar', None)
            if cal_cfg and cal_cfg.enable_calendar_firewall:
                is_mon = (ts.dayofweek == 0)
                is_sun = (ts.dayofweek == 6)
                is_mstart = ts.is_month_start
                is_mend = ts.is_month_end

                cal_veto_reason = None
                if cal_cfg.veto_monday and is_mon:
                    cal_veto_reason = "Core 5: Monday Opening Firewall"
                elif cal_cfg.veto_month_start and is_mstart:
                    cal_veto_reason = "Core 5: Month-Start Firewall"
                elif cal_cfg.veto_month_end and is_mend:
                    cal_veto_reason = "Core 5: Month-End Firewall"

                if cal_veto_reason is not None:
                    if telemetry:
                        telemetry.log_signal(TelemetryRecord(
                            timestamp=ts, asset=asset, tier=tier, status="VETOED",
                            veto_gate=cal_veto_reason, candidate_setup=candidate_setup,
                            price=c, turnover=turnover, ls_ratio=ls_ratio, funding_rate=fr,
                            btc_macro_bull=btc_bull
                        ))
                    continue

            # Route A0: Book 4 200-Day EMA Retest & Reclaim Execution (Study S-BY Causal Engine)
            if is_b4_candidate and (active_positions['Book 4'] is None):
                # Book 4 Macro Regime Gate (Options A, B & Synthesis)
                b4_regime_mode = getattr(b4_cfg, 'bear_regime_mode', 'open') if b4_cfg is not None else 'open'
                if not btc_bull:
                    if b4_regime_mode == 'bull_only':
                        continue
                    elif b4_regime_mode == 'option_a_zone4':
                        days_below = float(row.get('days_below_ema', 0.0))
                        b_ret30 = float(row.get('btc_ret_30d', 0.0))
                        is_zone4 = (days_below >= 180.0) and (b_ret30 > 0.0)
                        if not is_zone4:
                            continue
                    elif b4_regime_mode == 'option_b_decoupling':
                        ls_r = float(ls_ratio) if pd.notna(ls_ratio) else 1.0
                        doi_24 = float(row.get('d_oi_tokens_24h', 0.0))
                        rs_val = float(row.get('rs_vs_btc', 0.0))
                        to_val = float(turnover) if pd.notna(turnover) else 0.0
                        is_decoupling = (
                            (ls_r <= getattr(b4_cfg, 'decoupling_max_ls', 1.05)) and
                            (doi_24 >= getattr(b4_cfg, 'decoupling_min_doi_24h', 0.35)) and
                            (rs_val >= getattr(b4_cfg, 'decoupling_min_rs_btc', 0.25)) and
                            (to_val >= getattr(b4_cfg, 'decoupling_min_turnover', 4.0))
                        )
                        if not is_decoupling:
                            continue
                    elif b4_regime_mode == 'synthesis_a_b':
                        days_below = float(row.get('days_below_ema', 0.0))
                        b_ret30 = float(row.get('btc_ret_30d', 0.0))
                        is_zone4 = (days_below >= 180.0) and (b_ret30 > 0.0)

                        ls_r = float(ls_ratio) if pd.notna(ls_ratio) else 1.0
                        doi_24 = float(row.get('d_oi_tokens_24h', 0.0))
                        rs_val = float(row.get('rs_vs_btc', 0.0))
                        to_val = float(turnover) if pd.notna(turnover) else 0.0
                        is_decoupling = (
                            (ls_r <= getattr(b4_cfg, 'decoupling_max_ls', 1.05)) and
                            (doi_24 >= getattr(b4_cfg, 'decoupling_min_doi_24h', 0.35)) and
                            (rs_val >= getattr(b4_cfg, 'decoupling_min_rs_btc', 0.25)) and
                            (to_val >= getattr(b4_cfg, 'decoupling_min_turnover', 4.0))
                        )
                        if not (is_zone4 or is_decoupling):
                            continue

                market_px = c * (1 + slippage)
                cur_b4_avwap = active_b4_setup['cum_pv'] / max(1e-5, active_b4_setup['cum_v']) if active_b4_setup is not None else market_px
                retest_low_b4 = active_b4_setup['retest_low'] if active_b4_setup is not None else l
                base_floor = active_b4_setup.get('base_low_30d', market_px * 0.85) if active_b4_setup is not None else market_px * 0.85

                # Book 6 Staged Limit Absorption: 50% resting limit bid at AVWAP_tau, 50% reclaim close
                target_limit_bid = cur_b4_avwap
                filled_limit = (retest_low_b4 <= target_limit_bid)
                if getattr(b4_cfg, 'enable_staged_avwap_entry', True) and filled_limit:
                    fill_px = 0.50 * target_limit_bid + 0.50 * market_px
                else:
                    fill_px = market_px

                # 2D Sovereign Stop Governance Matrix: Mathematical Market Phase x Liquidity Tier
                days_below_ema = float(row.get('days_below_ema', 0.0))
                b_ret30 = float(row.get('btc_ret_30d', 0.0))
                s_pos_btc = float(row.get('cusum_pos_btc', 0.0))

                if days_below_ema >= 180.0 and b_ret30 > 0.0:
                    math_phase = 'early_bull'
                elif btc_bull and s_pos_btc >= 2.50:
                    math_phase = 'late_bull_exhaustion'
                elif btc_bull:
                    math_phase = 'mature_markup'
                else:
                    math_phase = 'bear_markdown'

                atr_24 = float(row.get('atr_24h', row.get('atr_24', 0.0)))
                if atr_24 <= 0.0:
                    atr_24 = float(row.get('atr', c * 0.02))
                atr_norm = (atr_24 / fill_px) if fill_px > 0 else 0.02

                if math_phase == 'early_bull':
                    trough_buf = float(np.clip(0.60 * atr_norm if tier == 'Tier 1' else (0.90 * atr_norm if tier == 'Tier 2' else 1.20 * atr_norm), 0.010, 0.035))
                    b4_max_risk = 0.100 if tier == 'Tier 1' else (0.140 if tier == 'Tier 2' else 0.180)
                    b4_target_cap_pct = 0.20 if tier == 'Tier 1' else (0.25 if tier == 'Tier 2' else 0.35)
                elif math_phase == 'mature_markup':
                    trough_buf = float(np.clip(0.40 * atr_norm if tier == 'Tier 1' else (0.60 * atr_norm if tier == 'Tier 2' else 0.80 * atr_norm), 0.005, 0.020))
                    b4_max_risk = 0.080 if tier == 'Tier 1' else (0.100 if tier == 'Tier 2' else 0.120)
                    b4_target_cap_pct = 0.20 if tier == 'Tier 1' else (0.25 if tier == 'Tier 2' else 0.30)
                elif math_phase == 'late_bull_exhaustion':
                    trough_buf = float(np.clip(0.30 * atr_norm if tier == 'Tier 1' else (0.50 * atr_norm if tier == 'Tier 2' else 0.60 * atr_norm), 0.003, 0.015))
                    b4_max_risk = 0.050 if tier == 'Tier 1' else (0.070 if tier == 'Tier 2' else 0.090)
                    b4_target_cap_pct = 0.15 if tier == 'Tier 1' else (0.20 if tier == 'Tier 2' else 0.25)
                else: # bear_markdown
                    trough_buf = 0.005
                    b4_max_risk = 0.050 if tier == 'Tier 1' else (0.070 if tier == 'Tier 2' else 0.080)
                    b4_target_cap_pct = 0.15

                # Snug structural stop directly below the retest trough, clamped by tier-specific risk budget
                floor_stop_px = retest_low_b4 * (1.0 - trough_buf)
                max_stop_px = fill_px * (1.0 - b4_max_risk)
                clamped_stop = max(floor_stop_px, max_stop_px)

                # Law 5 Two-Tier Target Cap (Tier-Adaptive)
                nov25 = float(row.get('nov25_low', 0.0))
                target_cap = min(fill_px * (1.0 + b4_target_cap_pct), max(fill_px * 1.15, nov25))

                w_btc = 1.0 if btc_bull else getattr(cfg.book4, 'bear_sizing_mult', 0.50)
                pct_lam_val = float(row.get('pct_lambda', 0.50))
                to_val = float(turnover) if pd.notna(turnover) else 1.0

                # Study S-BF: Continuous Anti-Chase Sizing Multiplier
                if getattr(cfg.book4, 'enable_anti_chase_sizing', True):
                    bar_body = abs(c - o)
                    body_atr_mult = bar_body / atr_24 if atr_24 > 0.0 else 1.0
                    th = getattr(cfg.book4, 'anti_chase_threshold', 1.50)
                    slope = getattr(cfg.book4, 'anti_chase_decay_slope', 0.35)
                    min_m = getattr(cfg.book4, 'anti_chase_min_multiplier', 0.50)
                    max_m = getattr(cfg.book4, 'anti_chase_max_multiplier', 1.20)
                    w_vol = float(np.clip(max_m - slope * max(0.0, body_atr_mult - th), min_m, max_m))
                else:
                    body_atr_mult = 1.0
                    w_vol = 1.0

                # Continuous Dynamic Liquidity Velocity Multiplier (w_liq)
                to_ref = 15.0 if tier == 'Tier 1' else (5.0 if tier == 'Tier 2' else 1.5)
                v_t = to_val / max(0.1, to_ref)
                w_liq = float(np.clip(0.85 + 0.35 * (v_t - 1.0), 0.35, 1.25))

                # Continuous Dynamic Relative Strength Multiplier (w_rs)
                rs_val = float(row.get('rs_vs_btc', 0.0))
                w_rs = float(np.clip(1.0 + 0.80 * rs_val, 0.50, 1.35))
                w_vol = float(np.clip(w_vol * w_liq * w_rs, 0.25, 1.50))

                # Study S-CA: Continuous Microstructure & Funding Governor
                if getattr(cfg.book4, 'enable_p_nb_microstructure_sizing', False):
                    p_nb_val = active_b4_setup.get('p_nb_high') if active_b4_setup is not None else None
                    if p_nb_val is not None and p_nb_val > 0:
                        dist_pnb = (c - p_nb_val) / p_nb_val
                        w_pnb = float(np.clip(1.0 + 0.35 * dist_pnb, 0.65, 1.35))
                        fr_z_val = float(row.get('funding_z', 0.0))
                        w_fr = float(np.clip(1.0 - 0.20 * fr_z_val, 0.70, 1.25))
                        w_vol = float(np.clip(w_vol * w_pnb * w_fr, 0.20, 1.50))

                # Study S-CD: Dynamic Whale Squeeze Sizing Multiplier (Rule 7)
                if getattr(cfg.book4, 'enable_dynamic_whale_sizing', False):
                    z_ls_val = float(row.get('z_ls_30d', 0.0))
                    w_whale = float(np.clip(1.0 - 0.25 * z_ls_val, 0.65, 1.35))
                    w_vol = float(np.clip(w_vol * w_whale, 0.20, 1.50))

                # Study S-BK & S-BY Arm 6: ALT/BTC Confluence Multiplier (1.35x)
                w_confluence = 1.0
                if getattr(cfg.book4, 'enable_dual_confluence_sizing', True):
                    alt_btc_px = float(row.get('alt_btc', 1.0))
                    ema200_btc_px = float(row.get('ema200_btc', 1.0))
                    s_pos_btc = float(row.get('cusum_pos_btc', 0.0))
                    if (alt_btc_px >= ema200_btc_px) or (s_pos_btc >= getattr(cfg.book4, 'cusum_btc_min', 1.50)):
                        w_confluence = getattr(cfg.book4, 'confluence_conviction_mult', 1.35)

                active_positions['Book 4'] = {
                    'entry_time': ts,
                    'entry_price': fill_px,
                    'stop': clamped_stop,
                    'initial_stop': clamped_stop,
                    'target': target_cap,
                    'max_high': h,
                    'min_low': l,
                    'book': 'Book 4',
                    'is_reclaim': True,
                    'is_continuation': False,
                    'entry_oi': current_oi,
                    'pct_lam': pct_lam_val,
                    'turnover_at_entry': to_val,
                    'rank_ts': float(row.get('rank_ts_168h', 0.50)),
                    'rank_ema': float(row.get('rank_ema_168h', 0.50)),
                    'p_nb_high': active_b4_setup.get('p_nb_high') if active_b4_setup is not None else None,
                    'w_btc': w_btc,
                    'w_vol': w_vol,
                    'w_confluence': w_confluence,
                    'body_atr_mult': body_atr_mult,
                    't1_a_hit': False,
                    't1_a_exit_px': None,
                    't1_b_exit_px': None,
                    'arm_donchian': False,
                    'p_nb_high': active_b4_setup.get('p_nb_high') if active_b4_setup is not None else None,
                    'avwap_tau': (active_b4_setup['cum_pv'] / max(1e-5, active_b4_setup['cum_v'])) if active_b4_setup is not None else fill_px,
                    'target_dynamic_atr': fill_px + getattr(cfg.book4, 'atr_target_multiple', 6.0) * (float(row.get('atr_24h', 0.0)) if float(row.get('atr_24h', 0.0)) > 0 else fill_px * 0.02),
                }
                active_b4_setup = None
                if telemetry:
                    telemetry.log_signal(TelemetryRecord(
                        timestamp=ts, asset=asset, tier=tier, status="ACTIVE",
                        veto_gate="None", candidate_setup="Book 4 200d Reclaim",
                        price=fill_px, turnover=turnover, ls_ratio=ls_ratio, funding_rate=fr,
                        btc_macro_bull=btc_bull
                    ))
                continue

            # Route A0.5: Book 6 3-SARE Orderflow Base Reclaim Execution (Study S-BP Canonical V13.2)
            if is_b6_candidate and (active_positions['Book 6'] is None):
                market_px = c * (1 + slippage)
                cur_b6_avwap = active_b6_setup['cum_pv'] / max(1e-5, active_b6_setup['cum_v'])
                retest_low_b6 = active_b6_setup['retest_low']

                # Staged Limit Absorption: 50% resting limit bid at AVWAP_tau, 50% reclaim close
                target_limit_bid = cur_b6_avwap
                filled_limit = (retest_low_b6 <= target_limit_bid)
                if filled_limit:
                    fill_px = 0.50 * target_limit_bid + 0.50 * market_px
                else:
                    fill_px = market_px

                # Dual-Barrier Invalidating Stop
                max_stop_px = fill_px * (1.0 - getattr(cfg.book6, 'max_stop_pct', 0.105))
                floor_stop_px = retest_low_b6 * getattr(cfg.book6, 'stop_retest_floor_buffer', 0.995)
                clamped_stop = max(floor_stop_px, max_stop_px)

                # Continuous Anti-Chase Volatility Sizing Multiplier
                atr_24 = float(row.get('atr_24h', row.get('atr_24', c * 0.02)))
                if atr_24 <= 0.0:
                    atr_24 = float(c * 0.02)
                bar_body = abs(c - o)
                body_atr_mult = bar_body / atr_24 if atr_24 > 0.0 else 1.0
                w_vol = float(np.clip(1.20 - 0.35 * max(0.0, body_atr_mult - 1.50), 0.50, 1.20))

                # Study S-CD: Dynamic Funding Carry Governor & Dynamic Whale Squeeze Multiplier (Rule 7)
                if getattr(cfg.book6, 'enable_dynamic_funding_sizing', False):
                    z_fnd_val = float(row.get('z_fnd_30d', 0.0))
                    w_fnd = float(np.clip(1.0 - 0.20 * z_fnd_val, 0.70, 1.30))
                    w_vol = float(np.clip(w_vol * w_fnd, 0.35, 1.50))
                if getattr(cfg.book6, 'enable_dynamic_whale_sizing', False):
                    z_ls_val = float(row.get('z_ls_30d', 0.0))
                    w_whale = float(np.clip(1.0 - 0.25 * z_ls_val, 0.65, 1.35))
                    w_vol = float(np.clip(w_vol * w_whale, 0.35, 1.50))

                w_btc = 1.00 if btc_bull else 0.50
                w_total = float(np.clip(w_vol * w_btc, 0.35, 1.35))

                active_positions['Book 6'] = {
                    'entry_time': ts,
                    'entry_price': fill_px,
                    'stop': clamped_stop,
                    'initial_stop': clamped_stop,
                    'target': fill_px * (1.0 + getattr(cfg.book6, 'tranche_a_mfe', 0.08)),
                    'max_high': h,
                    'min_low': l,
                    'book': 'Book 6',
                    'is_reclaim': True,
                    'is_continuation': False,
                    'is_b6_3sare': True,
                    'entry_oi': current_oi,
                    'pct_lam': float(row.get('pct_lambda', 0.50)),
                    'turnover_at_entry': float(turnover) if pd.notna(turnover) else 1.0,
                    'rank_ts': float(row.get('rank_ts_168h', 0.50)),
                    'rank_ema': float(row.get('rank_ema_168h', 0.50)),
                    'w_btc': w_btc,
                    'w_vol': w_vol,
                    'sizing_weight': w_total,
                    'body_atr_mult': body_atr_mult,
                    't_a_hit': False,
                    't_a_exit_px': None,
                    't_b_hit': False,
                    't_b_exit_px': None,
                    't_c_exit_px': None,
                    'arm_donchian': False,
                    'retest_bot_low': retest_low_b6,
                }
                active_b6_setup = None
                if telemetry:
                    telemetry.log_signal(TelemetryRecord(
                        timestamp=ts, asset=asset, tier=tier, status="ACTIVE",
                        veto_gate="None", candidate_setup="Book 6 3-SARE Base Reclaim",
                        price=fill_px, turnover=turnover, ls_ratio=ls_ratio, funding_rate=fr,
                        btc_macro_bull=btc_bull
                    ))
                continue

            # Route A0.7: Book 7 Micro-Cap Supernova & Base Squeeze Engine Execution (Study S-CH)
            if is_b7_candidate and (active_positions['Book 7'] is None):
                market_px = c * (1 + slippage)
                cur_b7_avwap = (active_b7_setup['cum_pv'] / max(1e-5, active_b7_setup['cum_v'])) if active_b7_setup is not None else market_px
                retest_low_b7 = active_b7_setup['retest_low'] if active_b7_setup is not None else l

                target_limit_bid = cur_b7_avwap
                filled_limit = (retest_low_b7 <= target_limit_bid)
                fill_px = (0.50 * target_limit_bid + 0.50 * market_px) if filled_limit else market_px

                atr_24 = float(row.get('atr_24h', row.get('atr_24', c * 0.03)))
                atr_norm = (atr_24 / fill_px) if fill_px > 0 else 0.03
                trough_buf = float(np.clip(1.00 * atr_norm, 0.010, 0.030))
                floor_stop_px = retest_low_b7 * (1.0 - trough_buf)
                max_stop_px = fill_px * (1.0 - b7_cfg.max_initial_risk)
                entry_stop = max(floor_stop_px, max_stop_px)

                # Continuous Dynamic Whale Squeeze Multiplier
                z_ls_val = float(row.get('z_ls_30d', 0.0))
                w_whale = float(np.clip(1.0 - 0.25 * z_ls_val, 0.65, 1.35))
                fr_z_val = float(row.get('funding_z', 0.0))
                w_fr = float(np.clip(1.0 - 0.20 * fr_z_val, 0.70, 1.25))
                w_btc = 1.0 if btc_bull else getattr(cfg.book4, 'bear_sizing_mult', 0.50)
                w_vol = float(np.clip(w_whale * w_fr, 0.35, 1.35))

                to_val = float(turnover) if pd.notna(turnover) else 1.0
                active_positions['Book 7'] = {
                    'entry_time': ts,
                    'entry_price': fill_px,
                    'stop': entry_stop,
                    'initial_stop': entry_stop,
                    'stop_price': entry_stop,
                    'highest_price': fill_px,
                    'max_high': fill_px,
                    'min_low': fill_px,
                    'lowest_price': fill_px,
                    'size': 1.0,
                    'book': 'Book 7',
                    'bar_count': 0,
                    'target': fill_px * (1.0 + b7_cfg.tranche_a_target_pct),
                    'entry_oi': current_oi,
                    'pct_lam': float(row.get('pct_lambda', 0.50)),
                    'turnover_at_entry': to_val,
                    'w_btc': w_btc,
                    'w_vol': w_vol,
                    't1_a_hit': False,
                    't1_a_exit_px': None,
                    't1_b_exit_px': None,
                    'arm_donchian': False,
                    'avwap_tau': cur_b7_avwap,
                }
                active_b7_setup = None
                if telemetry:
                    telemetry.log_signal(TelemetryRecord(
                        timestamp=ts, asset=asset, tier=tier, status="ACTIVE",
                        veto_gate="None", candidate_setup="Book 7 Micro-Cap Supernova",
                        price=fill_px, turnover=turnover, ls_ratio=ls_ratio, funding_rate=fr,
                        btc_macro_bull=btc_bull
                    ))
                continue

            # 1. Macro Bear Veto (Core 1) with Study S-Y Cycle Bottom Spring & Decoupling Override
            btc_ath_pct = float(row.get('btc_ath_pct', 1.0))
            vol_shock = float(row.get('vol_shock', 1.0))
            dist_60d = float(row.get('dist_from_60d_low', 0.0))
            days_below_ema = float(row.get('days_below_ema', 0.0))
            btc_ret_30d = float(row.get('btc_ret_30d', 0.0))

            # Study S-Y: Cycle Bottom Spring Module (BTC >= 180d below EMA and 30d base stabilization)
            is_cycle_spring = (
                cfg.macro.enable_cycle_spring and
                (not btc_bull) and
                (days_below_ema >= cfg.macro.cycle_spring_min_days) and
                (btc_ret_30d > 0.0 if cfg.macro.cycle_spring_require_base else True)
            )

            is_decoupling_override = False
            if cfg.macro.enable_decoupling_override and not btc_bull and tier in ['Tier 1', 'Tier 2']:
                is_decoupling_override = (
                    (ls_ratio <= cfg.macro.decoupling_max_ls) and
                    (turnover >= cfg.macro.decoupling_min_turnover) and
                    (vol_shock >= cfg.macro.decoupling_min_vol_shock) and
                    (rs_btc >= cfg.macro.decoupling_min_rs_btc)
                )

            macro_passed = btc_bull or is_cycle_spring or is_decoupling_override or can_shadow_reclaim
            if not macro_passed:
                # Study S-P: Check for new Shadow Anchor registration ($0 risk)
                if (
                    getattr(cfg.shadow_reclaim, 'enable_bear_shadow_reclaims', False) and
                    (active_shadow_anchor is None) and
                    (ls_ratio <= cfg.shadow_reclaim.max_toptrader_ls) and
                    (turnover >= cfg.shadow_reclaim.min_turnover_velocity) and
                    (fr <= cfg.shadow_reclaim.max_funding_rate) and
                    (shock >= cfg.shadow_reclaim.min_vol_shock)
                ):
                    active_shadow_anchor = {
                        'anchor_px': c,
                        'flush_low': l,
                        'armed_ts': ts,
                        'ls_ratio': ls_ratio,
                        'turnover': turnover
                    }
                    if telemetry:
                        telemetry.log_signal(TelemetryRecord(
                            timestamp=ts, asset=asset, tier=tier, status="SHADOW_ARMED",
                            veto_gate="Core 1: S-P Shadow Anchor Registered", candidate_setup=candidate_setup,
                            price=c, turnover=turnover, ls_ratio=ls_ratio, funding_rate=fr,
                            btc_macro_bull=btc_bull
                        ))
                    continue

                if telemetry:
                    telemetry.log_signal(TelemetryRecord(
                        timestamp=ts, asset=asset, tier=tier, status="VETOED",
                        veto_gate="Core 1: Macro Bear Veto", candidate_setup=candidate_setup,
                        price=c, turnover=turnover, ls_ratio=ls_ratio, funding_rate=fr,
                        btc_macro_bull=btc_bull
                    ))
                continue

            # ATH Tier 2 Protection Clamp: Veto mid-caps when BTC is near ATH (>= 85%)
            if (not is_tier1) and (btc_ath_pct >= cfg.macro.ath_tier2_protection_pct):
                if telemetry:
                    telemetry.log_signal(TelemetryRecord(
                        timestamp=ts, asset=asset, tier=tier, status="VETOED",
                        veto_gate="Core 1: ATH Tier-2 Protection Clamp", candidate_setup=candidate_setup,
                        price=c, turnover=turnover, ls_ratio=ls_ratio, funding_rate=fr,
                        btc_macro_bull=btc_bull
                    ))
                _try_arm_flush_bid("Core 1: ATH Tier-2 Protection Clamp")
                continue

            # Study S-Z (Calibrated): Tier-Differentiated RS_BTC Over-Extension Climax Clamp
            # Tier 1 & Tier 2 momentum leaders naturally exhibit strong relative strength vs BTC.
            # Micro-Caps (Tier 3) suffer illiquid blow-off traps when excessively overextended.
            is_rs_clamped_tier = (tier == 'Tier 3')
            if cfg.macro.enable_rs_btc_extension_veto and is_rs_clamped_tier and (rs_btc > cfg.macro.max_rs_btc_extension):
                if telemetry:
                    telemetry.log_signal(TelemetryRecord(
                        timestamp=ts, asset=asset, tier=tier, status="VETOED",
                        veto_gate="Core 4: RS_BTC Over-Extension Climax Clamp", candidate_setup=candidate_setup,
                        price=c, turnover=turnover, ls_ratio=ls_ratio, funding_rate=fr,
                        btc_macro_bull=btc_bull
                    ))
                _try_arm_flush_bid("Core 4: RS_BTC Over-Extension Climax Clamp")
                continue

            # 2. Orderbook Turnover Gate (Core 3)
            # Universal Min Turnover Floor
            if pd.notna(turnover) and turnover < cfg.micro.min_turnover_velocity:
                if telemetry:
                    telemetry.log_signal(TelemetryRecord(
                        timestamp=ts, asset=asset, tier=tier, status="VETOED",
                        veto_gate="Core 3: Min Turnover Velocity", candidate_setup=candidate_setup,
                        price=c, turnover=turnover, ls_ratio=ls_ratio, funding_rate=fr,
                        btc_macro_bull=btc_bull
                    ))
                _try_arm_flush_bid("Core 3: Min Turnover Velocity")
                continue

            # Trapped-Short Squeeze Override (Study S-Z2)
            is_sqz_override = (
                cfg.micro.enable_sqz_turnover_override and
                (fr <= cfg.micro.sqz_override_max_funding) and
                (ls_ratio <= cfg.micro.sqz_override_max_ls)
            )

            # Book 2 Squeeze Hunter Turnover Firewall (Retail Euphoria Protection: turnover <= 5.0x)
            if is_b2_candidate and pd.notna(turnover) and turnover > cfg.micro.b2_max_turnover_velocity and not is_sqz_override:
                is_b2_candidate = False

            # Book 1 / Continuation Max Turnover Ceiling (P98: turnover <= 15.0x)
            if pd.notna(turnover) and turnover > cfg.micro.max_turnover_velocity and not is_sqz_override:
                if getattr(cfg.micro, 'enable_turnover_scaling', False):
                    # Study S-R: Allow high turnover with continuous scaled sizing
                    pass
                else:
                    if telemetry:
                        telemetry.log_signal(TelemetryRecord(
                            timestamp=ts, asset=asset, tier=tier, status="VETOED",
                            veto_gate="Core 3: Max Turnover Velocity", candidate_setup=candidate_setup,
                            price=c, turnover=turnover, ls_ratio=ls_ratio, funding_rate=fr,
                            btc_macro_bull=btc_bull
                        ))
                    _try_arm_flush_bid("Core 3: Max Turnover Velocity")
                    continue

            # Whale Short-Trap Exception (Study S-Z3: QNT / High-Turnover Squeeze Trap)
            is_whale_sqz_trap = (
                getattr(cfg.micro, 'enable_whale_trap_override', True) and
                pd.notna(turnover) and (turnover >= getattr(cfg.micro, 'whale_trap_min_turnover', 5.0)) and
                (fr <= getattr(cfg.micro, 'whale_trap_max_funding', 0.00005))
            )

            # 3. Defensible Whale Dump Veto
            is_defensible_whale_dump = (ls_ratio < cfg.micro.min_toptrader_ls) and (d_oi_tok <= 0.15)
            if is_defensible_whale_dump and not is_b2_candidate and not is_decoupling_override and not is_sqz_override and not is_whale_sqz_trap and not can_shadow_reclaim:
                if telemetry:
                    telemetry.log_signal(TelemetryRecord(
                        timestamp=ts, asset=asset, tier=tier, status="VETOED",
                        veto_gate="Core 4: Defensible Whale Dump", candidate_setup=candidate_setup,
                        price=c, turnover=turnover, ls_ratio=ls_ratio, funding_rate=fr,
                        btc_macro_bull=btc_bull
                    ))
                _try_arm_flush_bid("Core 4: Defensible Whale Dump")
                continue

            # Route A: Book 2 Squeeze Execution
            if is_b2_candidate:
                if tier == "Tier 3" and not cfg.tier.tier3_enable_book2:
                    is_b2_candidate = False
                
                # Study S-BC: Coiled Squeezes restricted strictly to Sub-200d EMA (PF 2.281, +1,479.7% Log)
                if is_b2_candidate and getattr(cfg.micro, 'book2_sub_200d_only', True) and pd.notna(row.get('ema200_1d')) and c >= float(row.get('ema200_1d')):
                    if telemetry:
                        telemetry.log_signal(TelemetryRecord(
                            timestamp=ts, asset=asset, tier=tier, status="VETOED",
                            veto_gate="Core 4: Book 2 Above-200d Squeeze Stall", candidate_setup=candidate_setup,
                            price=c, turnover=turnover, ls_ratio=ls_ratio, funding_rate=fr,
                            btc_macro_bull=btc_bull
                        ))
                    is_b2_candidate = False

                # Study S-BD: Compensatory Anti-Chop Firewall for Book 2
                if is_b2_candidate and getattr(cfg.micro, 'enable_csmi_anti_chop', True):
                    d_ema_chk = (c - float(row.get('ema200_1d', c))) / (float(row.get('ema200_1d', c)) + 1e-8) if pd.notna(row.get('ema200_1d')) else 0.0
                    s_score, _, _ = compute_csmi_metrics('Book 2', float(row.get('rank_ts_168h', 0.50)), float(row.get('pct_lambda', 0.50)), d_ema_chk, cfg.sizing)
                    if s_score <= getattr(cfg.micro, 'csmi_anti_chop_threshold', -1.25):
                        if telemetry:
                            telemetry.log_signal(TelemetryRecord(
                                timestamp=ts, asset=asset, tier=tier, status="VETOED",
                                veto_gate="Core 4: CSMI Anti-Chop Firewall", candidate_setup=candidate_setup,
                                price=c, turnover=turnover, ls_ratio=ls_ratio, funding_rate=fr,
                                btc_macro_bull=btc_bull
                            ))
                        is_b2_candidate = False

                # Study S-BI Pillar 2: Whale Front-Running Purge (clean veto; never arms Book 3)
                if is_b2_candidate and getattr(cfg.micro, 'enable_front_running_purge', False) and d_ls_24h >= getattr(cfg.micro, 'front_run_min_d_ls_24h', 0.25):
                    if telemetry:
                        telemetry.log_signal(TelemetryRecord(
                            timestamp=ts, asset=asset, tier=tier, status="VETOED",
                            veto_gate="Core 4: Book 2 Whale Front-Running Purge", candidate_setup=candidate_setup,
                            price=c, turnover=turnover, ls_ratio=ls_ratio, funding_rate=fr,
                            btc_macro_bull=btc_bull
                        ))
                    is_b2_candidate = False

            if is_b2_candidate and (active_positions['Book 2'] is None):
                # Study S-BX: Sunday 7-Day High Break Protocol for Book 2
                if cal_cfg and cal_cfg.enable_calendar_firewall and cal_cfg.book2_require_sunday_high_break and (ts.dayofweek == 6):
                    # Register conditional trigger tracking Sunday's High
                    low_72 = float(row.get('low_72h', l))
                    clamped_stop = max(low_72 * (1 - slippage), c * (1 - cfg.micro.b2_max_initial_risk))
                    d_ema_val = (c - float(row.get('ema200_1d', c))) / (float(row.get('ema200_1d', c)) + 1e-8) if pd.notna(row.get('ema200_1d')) else 0.0
                    w_b2_carry = 1.0
                    if getattr(cfg.micro, 'enable_b2_inverted_carry_sizing', True):
                        if (fr <= 0.0) and (pd.isna(ls_ratio) or ls_ratio <= getattr(cfg.micro, 'b2_inverted_carry_max_ls', 1.05) or d_ls_24h <= -0.10):
                            w_b2_carry = getattr(cfg.micro, 'b2_inverted_carry_multiplier', 1.25)
                    active_b2_delayed = {
                        'trigger_ts': ts,
                        'sun_high': h,
                        'stop_px': clamped_stop,
                        'pct_lam': float(row.get('pct_lambda', 0.50)),
                        'rank_ts': float(row.get('rank_ts_168h', 0.50)),
                        'dist_ema': d_ema_val,
                        'w_conviction': w_b2_carry,
                    }
                    if telemetry:
                        telemetry.log_signal(TelemetryRecord(
                            timestamp=ts, asset=asset, tier=tier, status="VETOED",
                            veto_gate="Core 5: Book 2 Sunday Break Armed", candidate_setup=candidate_setup,
                            price=c, turnover=turnover, ls_ratio=ls_ratio, funding_rate=fr,
                            btc_macro_bull=btc_bull
                        ))
                    continue

                fill_px = c * (1 + slippage)
                low_72 = float(row.get('low_72h', l))
                raw_floor = max(low_72 * (1 - slippage), fill_px * (1 - cfg.micro.b2_max_initial_risk))
                clamped_stop = max(raw_floor, fill_px * (1 - cfg.micro.b2_max_initial_risk))
                d_ema_val = (fill_px - float(row.get('ema200_1d', fill_px))) / (float(row.get('ema200_1d', fill_px)) + 1e-8) if pd.notna(row.get('ema200_1d')) else 0.0

                w_b2_carry = 1.0
                if getattr(cfg.micro, 'enable_b2_inverted_carry_sizing', True):
                    if (fr <= 0.0) and (pd.isna(ls_ratio) or ls_ratio <= getattr(cfg.micro, 'b2_inverted_carry_max_ls', 1.05) or d_ls_24h <= -0.10):
                        w_b2_carry = getattr(cfg.micro, 'b2_inverted_carry_multiplier', 1.25)

                active_positions['Book 2'] = {
                    'entry_time': ts,
                    'entry_price': fill_px,
                    'stop': clamped_stop,
                    'max_high': h,           # use bar high for immediate MFE tracking
                    'min_low': l,            # HIGH-2 FIX: use bar low (not fill_px) for accurate MAE
                    'book': 'Book 2',
                    'is_reclaim': False,
                    'entry_oi': current_oi,
                    'pct_lam': float(row.get('pct_lambda', 0.50)),
                    'turnover_at_entry': float(turnover) if pd.notna(turnover) else 1.0,
                    'rank_ts': float(row.get('rank_ts_168h', 0.50)),
                    'dist_ema': d_ema_val,
                    'w_btc': 1.0,
                    'w_conviction': w_b2_carry,
                }
                if telemetry:
                    telemetry.log_signal(TelemetryRecord(
                        timestamp=ts, asset=asset, tier=tier, status="ACTIVE",
                        veto_gate="None", candidate_setup=candidate_setup,
                        price=fill_px, turnover=turnover, ls_ratio=ls_ratio, funding_rate=fr,
                        btc_macro_bull=btc_bull
                    ))
                continue


            # Route B: Book 1 Trend Continuation & Bear-Trap Reclaim
            # Tier 3 Gate: Book 1 is strictly prohibited on micro-caps (avoids -380% log trend bleed)
            if (tier == "Tier 3" and not cfg.tier.tier3_enable_book1) and not can_shadow_reclaim:
                if telemetry:
                    telemetry.log_signal(TelemetryRecord(
                        timestamp=ts, asset=asset, tier=tier, status="VETOED",
                        veto_gate="Core 2c: Tier 3 Book 1 Prohibition", candidate_setup=candidate_setup,
                        price=c, turnover=turnover, ls_ratio=ls_ratio, funding_rate=fr,
                        btc_macro_bull=btc_bull
                    ))
                _try_arm_flush_bid("Core 2c: Tier 3 Book 1 Prohibition")
                continue

            # 4. Whale Alignment for Book 1
            if ls_ratio < cfg.micro.min_toptrader_ls and not is_decoupling_override and not is_sqz_override and not is_whale_sqz_trap and not can_shadow_reclaim:
                if telemetry:
                    telemetry.log_signal(TelemetryRecord(
                        timestamp=ts, asset=asset, tier=tier, status="VETOED",
                        veto_gate="Core 4: Whale Firewall", candidate_setup=candidate_setup,
                        price=c, turnover=turnover, ls_ratio=ls_ratio, funding_rate=fr,
                        btc_macro_bull=btc_bull
                    ))
                _try_arm_flush_bid("Core 4: Whale Firewall")
                continue

            # 5. Funding Rate Reset Gate
            max_funding = cfg.micro.tier1_max_funding if is_tier1 else cfg.micro.tier2_max_funding
            is_sqz_funding_exception = False
            if fr > max_funding:
                is_sqz_funding_exception = (
                    getattr(cfg.micro, 'enable_funding_sqz_exception', False) and
                    pd.notna(ls_ratio) and
                    (ls_ratio < getattr(cfg.micro, 'funding_sqz_max_ls', 0.95))
                )
                if not is_sqz_funding_exception:
                    if telemetry:
                        telemetry.log_signal(TelemetryRecord(
                            timestamp=ts, asset=asset, tier=tier, status="VETOED",
                            veto_gate="Core 4: Funding Rate Cap", candidate_setup=candidate_setup,
                            price=c, turnover=turnover, ls_ratio=ls_ratio, funding_rate=fr,
                            btc_macro_bull=btc_bull
                        ))
                    _try_arm_flush_bid("Core 4: Funding Rate Cap")
                    continue

            # 6. Qualification for Reclaim vs Continuation vs Breakout
            if can_shadow_reclaim and active_shadow_anchor is not None:
                is_reclaim = True
                is_continuation = False
                reclaim_floor = active_shadow_anchor['flush_low']
                valid_b1 = True
            elif can_reclaim:
                is_reclaim = True
                is_continuation = False
                reclaim_floor = flush_low_since_exit
                max_dist = cfg.entry.reclaim_max_dist_60d_t1 if is_tier1 else cfg.entry.reclaim_max_dist_60d_t2
                valid_b1 = is_above_ma and (ret_14d >= cfg.entry.reclaim_min_ret_14d) and (dist_60d <= max_dist)
            elif is_continuation_candidate:
                is_reclaim = False
                is_continuation = True
                reclaim_floor = None
                valid_b1 = True
            elif is_b1_avwap_candidate:
                is_reclaim = True
                is_continuation = False
                reclaim_floor = active_b1_anchor['retest_low']
                valid_b1 = True
            else:
                is_reclaim = False
                is_continuation = False
                reclaim_floor = None
                # If Book 1 is operating under AVWAP Retest Reclaim mode, raw breakouts cannot enter directly
                if getattr(cfg, 'book1', None) and getattr(cfg.book1, 'enable_avwap_reclaim', True):
                    valid_b1 = False
                else:
                    if time_since_exit_b1 < cfg.entry.cooldown_hours:
                        continue
                    is_turnover_scaled_breakout = (
                        getattr(cfg.micro, 'enable_turnover_scaling', False) and
                        pd.notna(turnover) and
                        (turnover > cfg.micro.max_turnover_velocity)
                    )
                    is_remediated_override = is_sqz_override or is_sqz_funding_exception or is_turnover_scaled_breakout
                    max_dist = getattr(cfg.entry, 'remediated_max_dist_60d', 0.60) if is_remediated_override else (0.75 if is_decoupling_override else cfg.entry.max_dist_from_60d_low)
                    dist_72_low = float(row.get('dist_from_72h_low', 0.0))
                    max_dist_72 = getattr(cfg.entry, 'max_dist_from_72h_low', 0.25)
                    valid_b1 = (
                        is_breakout and
                        (ret_14d >= cfg.entry.min_14d_ret) and
                        (is_remediated_override or rs_btc >= cfg.entry.min_rs_btc) and
                        is_above_ma and
                        (dist_60d <= max_dist) and
                        (dist_72_low <= max_dist_72) and
                        (is_remediated_override or is_decoupling_override or pd.isna(oi_14d) or oi_14d <= cfg.entry.max_oi_expansion_14d)
                    )

            if valid_b1:
                # Study S-BV / S-BX: Book 1 Sunday Firewall
                if cal_cfg and cal_cfg.enable_calendar_firewall and cal_cfg.book1_veto_sunday and (ts.dayofweek == 6):
                    if telemetry:
                        telemetry.log_signal(TelemetryRecord(
                            timestamp=ts, asset=asset, tier=tier, status="VETOED",
                            veto_gate="Core 5: Book 1 Sunday Firewall", candidate_setup=candidate_setup,
                            price=c, turnover=turnover, ls_ratio=ls_ratio, funding_rate=fr,
                            btc_macro_bull=btc_bull
                        ))
                    valid_b1 = False

            if valid_b1:
                # Study S-BD: Compensatory Anti-Chop Firewall for Book 1
                if getattr(cfg.micro, 'enable_csmi_anti_chop', True):
                    d_ema_chk = (c - float(row.get('ema200_1d', c))) / (float(row.get('ema200_1d', c)) + 1e-8) if pd.notna(row.get('ema200_1d')) else 0.0
                    s_score, _, _ = compute_csmi_metrics('Book 1', float(row.get('rank_ts_168h', 0.50)), float(row.get('pct_lambda', 0.50)), d_ema_chk, cfg.sizing)
                    if s_score <= getattr(cfg.micro, 'csmi_anti_chop_threshold', -1.25):
                        if telemetry:
                            telemetry.log_signal(TelemetryRecord(
                                timestamp=ts, asset=asset, tier=tier, status="VETOED",
                                veto_gate="Core 4: CSMI Anti-Chop Firewall", candidate_setup=candidate_setup,
                                price=c, turnover=turnover, ls_ratio=ls_ratio, funding_rate=fr,
                                btc_macro_bull=btc_bull
                            ))
                        valid_b1 = False

            if valid_b1 and (active_positions['Book 1'] is None):
                fill_px = c * (1 + slippage)
                is_twotranche_b1 = False
                w_conviction = 1.0

                if is_continuation:
                    max_initial_risk = cfg.entry.continuation_max_initial_risk
                    raw_floor = max(low_14d * (1 - slippage), fill_px * (1.0 - max_initial_risk))
                    clamped_stop = max(raw_floor, fill_px * (1.0 - max_initial_risk))
                    book_label = 'Continuation'
                elif is_b1_avwap_candidate:
                    # Study S-BR & S-BS: Book 1 AVWAP Retest Reclaim Execution
                    max_initial_risk = 0.10
                    raw_floor = max(reclaim_floor * (1 - slippage), fill_px * (1.0 - max_initial_risk))
                    clamped_stop = max(raw_floor, fill_px * (1.0 - max_initial_risk))
                    book_label = 'Book 1'
                    is_twotranche_b1 = True
                    # Spot Absorption Multiplier (Study S-BP): when Token OI is flat/falling (Delta OI <= 0)
                    if getattr(cfg, 'book1', None) and d_oi_tok <= 0.0:
                        w_conviction = getattr(cfg.book1, 'spot_absorption_mult', 1.35)
                elif is_reclaim and reclaim_floor is not None and reclaim_floor > 0:
                    max_initial_risk = cfg.shadow_reclaim.max_initial_risk if can_shadow_reclaim else (cfg.exit.tier1_max_initial_risk if is_tier1 else cfg.exit.tier2_max_initial_risk)
                    raw_floor = max(reclaim_floor * (1 - slippage), fill_px * (1.0 - max_initial_risk))
                    clamped_stop = max(raw_floor, fill_px * (1.0 - max_initial_risk))
                    book_label = 'Book 2' if can_shadow_reclaim else 'Book 1'
                else:
                    is_turnover_scaled_breakout = (
                        getattr(cfg.micro, 'enable_turnover_scaling', False) and
                        pd.notna(turnover) and
                        (turnover > cfg.micro.max_turnover_velocity)
                    )
                    is_remediated_override = is_sqz_override or is_sqz_funding_exception or is_turnover_scaled_breakout
                    max_initial_risk = 0.08 if is_remediated_override else (cfg.exit.tier1_max_initial_risk if is_tier1 else cfg.exit.tier2_max_initial_risk)
                    floor_col = 'low_14d' if is_tier1 else 'low_7d'
                    raw_floor = float(row.get(floor_col, fill_px * (1 - max_initial_risk)))
                    clamped_stop = max(raw_floor, fill_px * (1.0 - max_initial_risk))
                    book_label = 'Book 2' if (is_remediated_override or is_whale_sqz_trap) else 'Book 1'

                entry_target = None
                if is_twotranche_b1:
                    target_pct = getattr(cfg.book1, 'tranche_a_target_pct', 0.08)
                    entry_target = fill_px * (1.0 + target_pct)
                elif getattr(cfg.exit, 'enable_two_tier_targets', True):
                    is_lead = bool(row.get('is_leading', True))
                    if not is_lead:
                        nov25 = float(row.get('nov25_low', 0.0))
                        sma200 = float(row.get('sma200_1d', 0.0))
                        cap = max(nov25, sma200)
                        if cap > fill_px * 1.03:
                            entry_target = min(fill_px * (1.0 + getattr(cfg.exit, 'max_lagging_target_pct', 0.20)), cap)
                        else:
                            entry_target = fill_px * (1.0 + getattr(cfg.exit, 'min_lagging_target_pct', 0.15))

                pct_lam_val = float(row.get('pct_lambda', 0.50))
                to_val = float(turnover) if pd.notna(turnover) else 1.0
                d_ema_b1 = (fill_px - float(row.get('ema200_1d', fill_px))) / (float(row.get('ema200_1d', fill_px)) + 1e-8) if pd.notna(row.get('ema200_1d')) else 0.0
                active_positions['Book 1'] = {
                    'entry_time': ts,
                    'entry_price': fill_px,
                    'stop': clamped_stop,
                    'target': entry_target,
                    'max_high': h,           # use bar high for immediate MFE tracking
                    'min_low': l,            # HIGH-2 FIX: use bar low (not fill_px) for accurate MAE
                    'book': book_label,
                    'is_reclaim': is_reclaim,
                    'is_continuation': is_continuation,
                    'is_b1_twotranche': is_twotranche_b1,
                    't1_a_hit': False,
                    't1_a_exit_px': None,
                    't1_b_exit_px': None,
                    'arm_donchian': False,
                    'entry_oi': current_oi,
                    'pct_lam': pct_lam_val,
                    'turnover_at_entry': to_val,
                    'rank_ts': float(row.get('rank_ts_168h', 0.50)),
                    'rank_ema': float(row.get('rank_ema_168h', 0.50)),
                    'dist_ema': d_ema_b1,
                    'w_btc': 1.0,
                    'w_conviction': w_conviction,
                }

                if can_shadow_reclaim:
                    active_shadow_anchor = None

                if telemetry:
                    telemetry.log_signal(TelemetryRecord(
                        timestamp=ts, asset=asset, tier=tier, status="ACTIVE",
                        veto_gate="None", candidate_setup=candidate_setup,
                        price=fill_px, turnover=turnover, ls_ratio=ls_ratio, funding_rate=fr,
                        btc_macro_bull=btc_bull
                    ))

    # Mark active positions as open at end of tape across all independent sleeves
    for book_name, active in active_positions.items():
        if active is not None:
            last_c = float(df.iloc[-1]['close'])
            book_type = active.get('book', 'Book 1')
            if book_type == 'Book 6':
                t_a_px = active.get('t_a_exit_px') or last_c
                t_b_px = active.get('t_b_exit_px') or last_c
                t_c_px = last_c
                pnl_a = (t_a_px - active['entry_price']) / active['entry_price'] - 0.0010
                pnl_b = (t_b_px - active['entry_price']) / active['entry_price'] - 0.0010
                pnl_c = (t_c_px - active['entry_price']) / active['entry_price'] - 0.0010
                raw_pnl = (1.0/3.0) * pnl_a + (1.0/3.0) * pnl_b + (1.0/3.0) * pnl_c
            elif (book_type in ('Book 4', 'Book 1', 'Book 7')) and active.get('t1_a_hit', False) and active.get('t1_a_exit_px') is not None:
                pnl_a = (active['t1_a_exit_px'] - active['entry_price']) / active['entry_price'] - 0.0010
                pnl_b = (last_c - active['entry_price']) / active['entry_price'] - 0.0010
                raw_pnl = 0.50 * pnl_a + 0.50 * pnl_b
            else:
                raw_pnl = (last_c - active['entry_price']) / active['entry_price']
            if book_type in ('Book 3', 'Book 5'):
                w = 1.0
            elif book_type == 'Book 6':
                w = float(active.get('sizing_weight', 1.0))
            else:
                w_to = float(np.minimum(1.0, 15.0 / max(1e-4, active.get('turnover_at_entry', 1.0)))) if getattr(cfg.micro, 'enable_turnover_scaling', False) else 1.0
                w_btc = float(active.get('w_btc', 1.0))

                if book_type in ('Book 4', 'Book 7'):
                    # Study S-BF & S-CH: Sizing Overlay for Book 4 and Book 7
                    w_vol = active.get('w_vol', 1.0)
                    w = float(np.clip(w_vol * w_btc, 0.10, 1.50))
                elif book_type in ('Book 1', 'Book 2') and getattr(cfg.sizing, 'enable_csmi_sizing', False):
                    # Study S-BD: Unified Compensatory Squeeze & Momentum Index (CSMI) Sizing Overlay
                    _, _, w_csmi = compute_csmi_metrics(
                        book_type,
                        active.get('rank_ts', 0.50),
                        active.get('pct_lam', 0.50),
                        active.get('dist_ema', 0.0),
                        cfg.sizing
                    )
                    w_conv = float(active.get('w_conviction', 1.0))
                    w = float(np.clip(w_to * w_csmi * w_btc * w_conv, 0.10, 1.50))
                else:
                    w_lam = float(np.clip(cfg.sizing.base_weight - active.get('pct_lam', 0.50), cfg.sizing.min_weight, cfg.sizing.max_weight)) if cfg.sizing.enable_lambda_sizing else 1.0
                    if book_type == 'Book 1' and getattr(cfg.sizing, 'enable_ticket_size_sizing', False):
                        ts_base = getattr(cfg.sizing, 'ts_base_multiplier', 0.75)
                        ts_slope = getattr(cfg.sizing, 'ts_slope_multiplier', 0.50)
                        ts_min = getattr(cfg.sizing, 'ts_min_multiplier', 0.75)
                        ts_max = getattr(cfg.sizing, 'ts_max_multiplier', 1.25)
                        w_ts = float(np.clip(ts_base + ts_slope * active.get('rank_ts', 0.50), ts_min, ts_max))
                    else:
                        w_ts = 1.0

                    if book_type in ('Book 1', 'Book 4') and getattr(cfg.sizing, 'enable_ema_sizing', False):
                        ema_base = getattr(cfg.sizing, 'ema_base_multiplier', 0.75)
                        ema_slope = getattr(cfg.sizing, 'ema_slope_multiplier', 0.50)
                        ema_min = getattr(cfg.sizing, 'ema_min_multiplier', 0.75)
                        ema_max = getattr(cfg.sizing, 'ema_max_multiplier', 1.25)
                        w_ema = float(np.clip(ema_base + ema_slope * active.get('rank_ema', 0.50), ema_min, ema_max))
                    else:
                        w_ema = 1.0

                    w_conv = float(active.get('w_conviction', 1.0))
                    w = float(np.clip(w_lam * w_to * w_ts * w_ema * w_btc * w_conv, 0.10, 1.50))
            pnl = w * raw_pnl
            log_ret = float(np.log(max(1e-6, 1.0 + pnl)))
            dur_hours = (df.index[-1] - active['entry_time']).total_seconds() / 3600.0
            mfe = (active['max_high'] - active['entry_price']) / active['entry_price']
            mae = (active['min_low'] - active['entry_price']) / active['entry_price']
            trades.append({
                'asset': asset,
                'tier': tier,
                'book': active.get('book', 'Book 1'),
                'entry': active['entry_time'],
                'exit': df.index[-1],
                'duration_hours': dur_hours,
                'entry_price': active['entry_price'],
                # HIGH-3: label clearly — this is the last tape snapshot close, not a live exchange price
                'exit_price': last_c,
                'stop_price': active['stop'],
                'initial_stop': active.get('initial_stop', active['stop']),
                'raw_pnl': raw_pnl,
                'pnl': pnl,
                'sizing_weight': w,
                'log_ret': log_ret,
                'mfe': mfe,
                'mae': mae,
                'reason': 'open_at_end',
                'is_open': True,
                'is_reclaim': active.get('is_reclaim', False),
                'is_continuation': active.get('is_continuation', False),
                'is_book3': active.get('is_book3', False),
                'pct_lam': active.get('pct_lam', 0.50),
                'turnover_at_entry': active.get('turnover_at_entry', 1.0),
                'rank_ts': active.get('rank_ts', 0.50),
                # MEDIUM-3: entry OI for post-trade OI expansion analysis
                'entry_oi_usd': active.get('entry_oi', 0.0),
                'w_vol': active.get('w_vol', 1.0),
                'body_atr_mult': active.get('body_atr_mult', np.nan),
            })

    return pd.DataFrame(trades)
