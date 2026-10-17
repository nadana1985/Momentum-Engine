"""
Kronos V12: Pure 6-Core Execution Kernel (engine_v12.py)
Executes Macro Gating, Dynamic Tier Floors, Whale Firewalling, Bear Trap Reclaims,
and Climax Top Harvesting.
"""

from typing import Dict, List, Optional, Tuple
import numpy as np
import pandas as pd

from momentum_v12.config import V12Config
from momentum_v12.telemetry_v12 import TelemetryCollector, TelemetryRecord
from momentum_v12.sizing_v12 import compute_csmi_metrics
from momentum_v12.features_v12 import extract_p_nb_high
from momentum_v12.oms_fills import limit_fill_price
from momentum_v12.engine_state import (
    _to_naive_ts,
    hydrate_engine_state,
    snapshot_engine_state,
)


def run_v12_engine(
    df: pd.DataFrame,
    asset: str,
    cfg: V12Config = V12Config(),
    telemetry: Optional[TelemetryCollector] = None,
    state: Optional[Dict] = None,
    start_after: Optional[pd.Timestamp] = None,
) -> Tuple[pd.DataFrame, Dict]:
    """
    Executes the Clean 6-Core Execution Kernel on an enriched shard.

    Returns (trades_df, state_out). `state` restores every sleeve (active
    position, cooldowns, flush bids, Book 4/6 anchors). `start_after` skips
    bars at or before that timestamp so an incremental hour can reuse a
    feature window for lookbacks while only stepping new closed bars.
    """
    if df.empty:
        return pd.DataFrame(), hydrate_engine_state(state, None)

    trades: List[Dict] = []
    st = hydrate_engine_state(state, df.index)
    active: Optional[Dict] = st['active']

    last_exit_ts: Optional[pd.Timestamp] = st['last_exit_ts']
    last_exit_reason: Optional[str] = st['last_exit_reason']
    last_exit_pnl: float = float(st['last_exit_pnl'])
    last_entry_price: float = float(st['last_entry_price'])
    flush_low_since_exit: float = float(st['flush_low_since_exit'])
    active_shadow_anchor: Optional[Dict] = st['active_shadow_anchor']
    active_flush_bid: Optional[Dict] = st['active_flush_bid']
    active_b4_setup: Optional[Dict] = st['active_b4_setup']
    active_b1_anchor: Optional[Dict] = st['active_b1_anchor']
    active_b5_bid: Optional[Dict] = st['active_b5_bid']
    last_b5_arm_ts: Optional[pd.Timestamp] = st['last_b5_arm_ts']
    active_b6_setup: Optional[Dict] = st['active_b6_setup']
    active_b2_delayed: Optional[Dict] = st['active_b2_delayed']
    n_processed = 0
    start_ts = _to_naive_ts(start_after) if start_after is not None else None

    tier = str(df['tier'].iloc[0]) if 'tier' in df.columns else 'Tier 1'
    is_tier1 = (tier == 'Tier 1')

    # Precompute rolling series for speed
    ls_series = df.get('toptrader_ls', pd.Series(1.0, index=df.index)).ffill()
    max_ls_7d_series = ls_series.shift(1).rolling(168, min_periods=24).max()

    slippage = cfg.entry.slippage

    # Precompute arrays and caching for Two-Tier Volume Profile Shelf Absorption (Study S-AN / S-AO)
    c_arr = df['close'].to_numpy(float)
    h_arr = df['high'].to_numpy(float)
    l_arr = df['low'].to_numpy(float)
    if 'quote_volume' in df.columns:
        qv_arr = df['quote_volume'].fillna(0.0).to_numpy(float)
    elif 'volume' in df.columns:
        qv_arr = (df['close'] * df['volume']).fillna(0.0).to_numpy(float)
    else:
        qv_arr = df['close'].fillna(0.0).to_numpy(float)

    daily_df = getattr(df, 'attrs', {}).get('daily_df', None)
    if daily_df is None:
        try:
            d_c = df['close'].resample('1D').last().dropna()
            d_o = df['open'].resample('1D').first().dropna()
            d_h = df['high'].resample('1D').max().dropna()
            d_l = df['low'].resample('1D').min().dropna()
            daily_df = pd.DataFrame({'open': d_o, 'high': d_h, 'low': d_l, 'close': d_c})
        except Exception:
            daily_df = None

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
        ts = _to_naive_ts(ts)
        if ts is None:
            continue
        if start_ts is not None and ts <= start_ts:
            continue
        n_processed += 1
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

        if active is None and last_exit_ts is not None:
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
                    'tau_ts': ts,
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

        # Study S-BP: Book 6 3-SARE CUSUM-Anchored Base AVWAP Tracking
        if getattr(cfg, 'book6', None) and getattr(cfg.book6, 'enable_book6', True):
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
            if active_b2_delayed is not None and active is None:
                # Check expiration (> 168 hours or past Sunday week)
                age_h = (ts - active_b2_delayed['trigger_ts']).total_seconds() / 3600.0
                if age_h > cal_cfg.sunday_high_break_window_hours or age_h > 168:
                    active_b2_delayed = None
                elif h > active_b2_delayed['sun_high']:
                    # Triggered! Enter at Sunday High breakout
                    break_px = max(active_b2_delayed['sun_high'] * 1.001, o) * (1 + slippage)
                    stop_px = max(active_b2_delayed['stop_px'], break_px * 0.92) # 8% stop clamp
                    active = {
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
            if active_flush_bid is not None and active is None:
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
                        if cal_cfg and cal_cfg.enable_calendar_firewall:
                            if (cal_cfg.veto_monday and is_mon) or (cal_cfg.veto_month_start and is_mstart) or (cal_cfg.veto_month_end and is_mend):
                                skip_fill = True

                        if not skip_fill:
                            stop_px = float(active_flush_bid['stop_px'])
                            if fill_mode == 'live_limit':
                                stop_px = entry_px * (1.0 - float(cfg.book3_flush.max_initial_risk))
                            active = {
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

        # Study S-BI Pillar 1: Book 5 Trapped-Whale Shelf Absorption (resting limit bid lifecycle)
        if getattr(cfg.book5, 'enable_book5', False):
            if active_b5_bid is not None and active is None:
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
                            active = {
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
            # Arm a new bid using only information available at this bar's close
            if active is None and active_b5_bid is None and pd.notna(ls_ratio):
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
        # 1. ACTIVE POSITION MANAGEMENT & CLIMAX HARVESTING
        # -------------------------------------------------------------
        if active is not None:
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
                if active.get('t_b_hit', False):
                    # Tranche C trails rolling 72h Donchian floor
                    floor_val = float(row.get('low_72h', active['stop']))
                    active['stop'] = max(active['stop'], floor_val)
                elif active.get('t_a_hit', False):
                    # Ratchet stop to Breakeven (-0.2% fee cushion)
                    active['stop'] = max(active['stop'], active['entry_price'] * 0.998)
            elif book_type == 'Book 4':
                # Study S-BE: Two-Tranche Trajectory Exit Floor
                if active.get('t1_a_hit', False) or active.get('arm_donchian', False):
                    col_floor = 'low_14d' if is_tier1 else ('low_7d' if tier == 'Tier 2' else 'low_72h')
                    floor_val = float(row.get(col_floor, active['stop']))
                    if pd.notna(floor_val) and floor_val > active['stop']:
                        active['stop'] = floor_val
                elif mfe >= getattr(cfg.book4, 'donchian_arm_mfe', 0.50):
                    active['arm_donchian'] = True
                    col_floor = 'low_14d' if is_tier1 else ('low_7d' if tier == 'Tier 2' else 'low_72h')
                    floor_val = float(row.get(col_floor, active['stop']))
                    if pd.notna(floor_val) and floor_val > active['stop']:
                        active['stop'] = floor_val
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
                # Book 4 200d EMA Reclaim Exit Mechanics (Study S-BB & S-BE Two-Tranche)
                if dur_hours >= getattr(cfg.book4, 'stagnation_cut_hours', 168) and mfe < 0.05 and c < active['entry_price']:
                    exit_price = c * (1 - slippage)
                    exit_triggered = True
                    exit_reason = "stagnation_cut"
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

            # Study S-AA: 36-Hour Stagnation Stall-Out Bailout (Zero-Runner Loss Checkpoint)
            if not exit_triggered and cfg.exit.enable_stall_bailout and not active.get('is_b1_twotranche', False):
                if dur_hours >= cfg.exit.stall_bailout_hours and mfe < cfg.exit.stall_bailout_max_mfe and c < active['entry_price']:
                    exit_price = c * (1 - slippage)
                    exit_triggered = True
                    exit_reason = "stall_bailout"

            # Study S-BP: Book 6 3-SARE 3-Stage Asymmetric Reclaim Engine Exits
            if not exit_triggered and book_type == 'Book 6':
                t_a_hit = active.get('t_a_hit', False)
                t_b_hit = active.get('t_b_hit', False)

                # Tranche A (+8.0% Fast Breakeven Lock)
                if not t_a_hit and (mfe >= getattr(cfg.book6, 'tranche_a_mfe', 0.08) or h >= active['entry_price'] * (1.0 + getattr(cfg.book6, 'tranche_a_mfe', 0.08))):
                    active['t_a_hit'] = True
                    active['t_a_exit_px'] = active['entry_price'] * (1.0 + getattr(cfg.book6, 'tranche_a_mfe', 0.08))
                    # Ratchet remaining stop to breakeven (-0.2% cushion)
                    active['stop'] = max(active['stop'], active['entry_price'] * (1.0 - getattr(cfg.book6, 'tranche_a_cushion', 0.002)))

                # Tranche B (+25.0% Swing Target Cap)
                if active.get('t_a_hit', False) and not t_b_hit and (mfe >= getattr(cfg.book6, 'tranche_b_mfe', 0.25) or h >= active['entry_price'] * (1.0 + getattr(cfg.book6, 'tranche_b_mfe', 0.25))):
                    active['t_b_hit'] = True
                    active['t_b_exit_px'] = active['entry_price'] * (1.0 + getattr(cfg.book6, 'tranche_b_mfe', 0.25))
                    # Ratchet Tranche C stop to +8.0% guaranteed floor
                    active['stop'] = max(active['stop'], active['entry_price'] * (1.0 + getattr(cfg.book6, 'tranche_b_floor', 0.08)))
                    active['arm_donchian'] = True

                # Panic Liquidation Bailout: volume >= 3.0x breaking retest floor
                retest_floor = active.get('retest_bot_low', active['entry_price'] * 0.90)
                if (l < retest_floor * getattr(cfg.book6, 'stop_retest_floor_buffer', 0.995)) and (shock >= getattr(cfg.book6, 'panic_bailout_vol_mult', 3.0)):
                    bailout_px = max(l, retest_floor * 0.98) * (1 - slippage)
                    exit_price = bailout_px
                    exit_triggered = True
                    exit_reason = "panic_liquidation_bailout"

            # Study S-BE & Study S-BR/S-BS: Two-Tranche Target Cap Trigger for Book 4 and Book 1
            if not exit_triggered and (book_type in ('Book 4', 'Book 1')) and active.get('is_b1_twotranche', False) and not active.get('t1_a_hit', False):
                if active.get('target') is not None and h >= active['target']:
                    active['t1_a_hit'] = True
                    active['t1_a_exit_px'] = active['target']
                    cush_pct = getattr(cfg.book1, 'tranche_b_cushion_pct', 0.005) if getattr(cfg, 'book1', None) else 0.005
                    active['stop'] = max(active['stop'], active['entry_price'] * (1.0 - cush_pct)) # Tight -0.5% ratchet cushion
                    active['arm_donchian'] = True
            elif not exit_triggered and book_type == 'Book 4' and not active.get('t1_a_hit', False):
                if active.get('target') is not None and h >= active['target']:
                    # Tranche A (50%) locks in target cap (+20%)
                    active['t1_a_hit'] = True
                    active['t1_a_exit_px'] = active['target']
                    # Tranche B (50%) ratchets stop to breakeven cushion and arms Donchian trail
                    active['stop'] = max(active['stop'], active['entry_price'] * 0.9985)
                    active['arm_donchian'] = True
            elif not exit_triggered and not active.get('arm_donchian', False) and active.get('target') is not None and h >= active['target']:
                # Study S-AY Law 5 / Study S-BB: Two-Tier Target Cap Exit
                exit_price = active['target']
                exit_triggered = True
                exit_reason = "target_reclaim"

            # Native Resting Stop-Market Order Execution
            if not exit_triggered:
                if l <= active['stop']:
                    if book_type == 'Book 6':
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
                    elif (book_type in ('Book 4', 'Book 1')) and active.get('t1_a_hit', False):
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
                elif dur_hours >= (getattr(cfg.book6, 'max_duration_hours', 720) if book_type == 'Book 6' else (getattr(cfg.book4, 'max_duration_hours', 720) if book_type == 'Book 4' else (cfg.exit.b2_time_cap_hours if book_type == 'Book 2' else (cfg.exit.time_cap_hours_t1 if is_tier1 else cfg.exit.time_cap_hours_t2)))):
                    if book_type == 'Book 6':
                        t_a_px = active.get('t_a_exit_px') or (c * (1 - slippage))
                        t_b_px = active.get('t_b_exit_px') or (c * (1 - slippage))
                        t_c_px = c * (1 - slippage)
                        exit_price = (1.0/3.0) * t_a_px + (1.0/3.0) * t_b_px + (1.0/3.0) * t_c_px
                        exit_triggered = True
                        exit_reason = "time_cap"
                    elif (book_type in ('Book 4', 'Book 1')) and active.get('t1_a_hit', False):
                        active['t1_b_exit_px'] = c * (1 - slippage)
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
                elif (book_type in ('Book 4', 'Book 1')) and active.get('t1_a_hit', False) and active.get('t1_b_exit_px') is not None:
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

                    if book_type == 'Book 4':
                        # Study S-BF: Continuous Anti-Chase Sizing Overlay for Book 4
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
                active = None

        # -------------------------------------------------------------
        # 2. ENTRY EVALUATION & DUAL-BOOK DISPATCHING
        # -------------------------------------------------------------
        if active is None:
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
                    (time_since_exit >= cfg.micro.b2_cooldown_hours) and
                    (c > high_72) and
                    (dist_72_low <= cfg.micro.b2_max_dist_72h_low) and
                    (taker <= cfg.micro.b2_max_taker_ratio) and
                    (shock >= cfg.micro.b2_min_vol_shock) and
                    (turnover >= cfg.micro.min_turnover_velocity) and (turnover <= cfg.micro.b2_max_turnover_velocity)
                )

            # Bear Trap V-Reclaim Candidate (Study S-P)
            can_reclaim = (
                time_since_exit >= cfg.entry.reclaim_min_hours and
                time_since_exit <= cfg.entry.reclaim_max_hours and
                last_exit_reason in ['initial_stop', 'trail_stop'] and
                (last_exit_pnl < 0.0 and last_exit_pnl >= cfg.entry.reclaim_max_pnl_loss) and
                (c >= last_entry_price or is_breakout) and
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
                    (time_since_exit >= cfg.entry.continuation_cooldown_hours) and
                    (dist_60d >= cfg.entry.continuation_min_dist_60d) and
                    (rs_btc >= cfg.entry.continuation_min_rs_btc) and
                    (ret_14d >= cfg.entry.continuation_min_14d_ret)
                )

            # Study S-BB & S-BE & S-CA: Book 4 200-Day EMA Touch & Retest Tracking
            ema200 = float(row.get('ema200_1d', c))
            b4_cfg = getattr(cfg, 'book4', None)
            b4_enabled = getattr(b4_cfg, 'enable_book4', True) if b4_cfg is not None else True
            tier2_b4_ok = getattr(cfg.tier, 'tier2_enable_book4', False) if tier == 'Tier 2' else True
            tier3_b4_ok = getattr(cfg.tier, 'tier3_enable_book4', False) if tier == 'Tier 3' else True
            is_tier_b4_ok = (
                (tier == 'Tier 1')
                or (tier == 'Tier 2' and tier2_b4_ok)
                or (tier == 'Tier 3' and tier3_b4_ok)
            )
            if bool(row.get('is_200d_touch', False)) and b4_enabled and is_tier_b4_ok:
                pre_start = max(0, _bar_i - getattr(cfg.book4, 'min_bars_below', 720))
                base_low_30d = float(l_arr[pre_start : _bar_i].min()) if _bar_i > 0 else l
                if active_b4_setup is None:
                    p_nb_high = None
                    if daily_df is not None:
                        canary_date = pd.Timestamp(ts).floor('D')
                        p_nb_val, _, _ = extract_p_nb_high(daily_df, canary_date, c)
                        if p_nb_val is not None and p_nb_val > 0:
                            p_nb_high = p_nb_val
                    if p_nb_high is None or p_nb_high <= 0:
                        p_nb_high = float(np.max(h_arr[pre_start : _bar_i])) if _bar_i > 0 else h
                    active_b4_setup = {
                        'touch_bar': _bar_i,
                        'touch_ts': ts,
                        'p0': c,
                        'p_nb_high': p_nb_high,
                        'peak_high': h,
                        'base_low_30d': base_low_30d,
                        'bot_low': l,
                        'bot_bar': _bar_i,
                    }
                else:
                    if h > active_b4_setup.get('peak_high', h):
                        active_b4_setup['peak_high'] = h
                    if l < active_b4_setup['bot_low']:
                        active_b4_setup['bot_low'] = l
                        active_b4_setup['bot_bar'] = _bar_i

            is_b4_candidate = False
            if active_b4_setup is not None:
                if l < active_b4_setup['bot_low']:
                    active_b4_setup['bot_low'] = l
                    active_b4_setup['bot_bar'] = _bar_i
                if h > active_b4_setup.get('peak_high', h):
                    active_b4_setup['peak_high'] = h

                p0 = active_b4_setup['p0']
                bot_l = active_b4_setup['bot_low']
                bot_hours = active_b4_setup['bot_bar'] - active_b4_setup['touch_bar']
                bars_since_touch = _bar_i - active_b4_setup['touch_bar']
                dd = (bot_l - p0) / p0 if p0 > 0 else 0.0

                if (
                    bot_l <= active_b4_setup['base_low_30d'] or
                    bot_hours > getattr(cfg.book4, 'max_retest_hours', 120) or
                    dd < getattr(cfg.book4, 'max_retest_dd', -0.20) or
                    bars_since_touch > 384
                ):
                    active_b4_setup = None
                elif (
                    _bar_i > active_b4_setup['touch_bar'] and
                    c >= ema200 and
                    b4_enabled and
                    is_tier_b4_ok
                ):
                    p_nb_ok = True
                    if getattr(cfg.book4, 'enable_p_nb_day_close_confirmation', False):
                        p_nb_ref = active_b4_setup.get('p_nb_high')
                        if p_nb_ref is not None and p_nb_ref > 0:
                            is_day_close_bar = (ts.hour == 23)
                            p_nb_ok = is_day_close_bar and (c >= p_nb_ref)
                    if p_nb_ok:
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

            # Study S-BP: Book 6 3-SARE Orderflow Base Reclaim Candidate Check
            is_b6_candidate = False
            if (
                getattr(cfg, 'book6', None) and
                getattr(cfg.book6, 'enable_book6', True) and
                active_b6_setup is not None and
                active_b6_setup.get('retest_found', False) and
                (_bar_i > active_b6_setup['retest_bar'])
            ):
                cur_b6_avwap = active_b6_setup['cum_pv'] / max(1e-5, active_b6_setup['cum_v'])
                reclaimed_b6 = (c > cur_b6_avwap)
                whale_frontrun = (d_ls_24h >= cfg.book6.whale_frontrun_veto_delta)
                if reclaimed_b6 and not whale_frontrun:
                    is_b6_candidate = True

            use_avwap_mode = getattr(cfg, 'book1', None) and getattr(cfg.book1, 'enable_avwap_reclaim', True)
            b1_cand = is_b1_avwap_candidate if use_avwap_mode else is_breakout

            is_candidate = is_b4_candidate or is_b6_candidate or is_b2_candidate or can_reclaim or can_shadow_reclaim or b1_cand or is_continuation_candidate
            if not is_candidate:
                continue

            if is_b4_candidate:
                candidate_setup = "200d EMA Reclaim"
            elif is_b6_candidate:
                candidate_setup = "3-SARE Base Reclaim"
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
                    (active is None) and
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

            # Route A0: Book 4 200-Day EMA Retest & Reclaim Execution (Study S-BB & S-BE & S-BF Canonical V12.9)
            if is_b4_candidate:
                fill_px = c * (1 + slippage)
                bot_low = active_b4_setup['bot_low'] if active_b4_setup is not None else l
                clamped_stop = max(bot_low * (1 - slippage), fill_px * 0.85)

                # Law 5 Two-Tier Target Cap
                nov25 = float(row.get('nov25_low', 0.0))
                target_cap = min(fill_px * (1.0 + getattr(cfg.book4, 'target_cap_pct', 0.20)), max(fill_px * 1.15, nov25))

                w_btc = 1.0 if btc_bull else getattr(cfg.book4, 'bear_sizing_mult', 0.50)
                pct_lam_val = float(row.get('pct_lambda', 0.50))
                to_val = float(turnover) if pd.notna(turnover) else 1.0

                # Study S-BF: Continuous Anti-Chase Sizing Multiplier
                if getattr(cfg.book4, 'enable_anti_chase_sizing', True):
                    atr_24 = float(row.get('atr_24h', row.get('atr_24', 0.0)))
                    if atr_24 <= 0.0:
                        atr_24 = float(row.get('atr', c * 0.02))
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

                # Study S-CA: Continuous Microstructure & Funding Governor
                if getattr(cfg.book4, 'enable_p_nb_microstructure_sizing', False):
                    p_nb_val = active_b4_setup.get('p_nb_high') if active_b4_setup is not None else None
                    if p_nb_val is not None and p_nb_val > 0:
                        dist_pnb = (c - p_nb_val) / p_nb_val
                        w_pnb = float(np.clip(1.0 + 0.35 * dist_pnb, 0.65, 1.35))
                        fr_z_val = float(row.get('funding_z', 0.0))
                        w_fr = float(np.clip(1.0 - 0.20 * fr_z_val, 0.70, 1.25))
                        w_vol = float(np.clip(w_vol * w_pnb * w_fr, 0.20, 1.50))

                active = {
                    'entry_time': ts,
                    'entry_price': fill_px,
                    'stop': clamped_stop,
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
                    'body_atr_mult': body_atr_mult,
                    't1_a_hit': False,
                    't1_a_exit_px': None,
                    't1_b_exit_px': None,
                    'arm_donchian': False,
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
            if is_b6_candidate:
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
                w_btc = 1.00 if btc_bull else 0.50
                w_total = float(np.clip(w_vol * w_btc, 0.35, 1.35))

                active = {
                    'entry_time': ts,
                    'entry_price': fill_px,
                    'stop': clamped_stop,
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

            if is_b2_candidate:
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

                active = {
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
                    if time_since_exit < cfg.entry.cooldown_hours:
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

            if valid_b1:
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
                active = {
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

    def _state_out() -> Dict:
        return snapshot_engine_state(
            {
                'active': active,
                'last_exit_ts': last_exit_ts,
                'last_exit_reason': last_exit_reason,
                'last_exit_pnl': last_exit_pnl,
                'last_entry_price': last_entry_price,
                'flush_low_since_exit': flush_low_since_exit,
                'active_shadow_anchor': active_shadow_anchor,
                'active_flush_bid': active_flush_bid,
                'active_b4_setup': active_b4_setup,
                'active_b1_anchor': active_b1_anchor,
                'active_b5_bid': active_b5_bid,
                'last_b5_arm_ts': last_b5_arm_ts,
                'active_b6_setup': active_b6_setup,
                'active_b2_delayed': active_b2_delayed,
            },
            df.index,
        )

    # Incremental hour with no new closed bars: keep sleeves, emit no tape rows.
    if n_processed == 0:
        return pd.DataFrame(), _state_out()

    # Mark active position as open at end of tape
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
        elif (book_type in ('Book 4', 'Book 1')) and active.get('t1_a_hit', False) and active.get('t1_a_exit_px') is not None:
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

            if book_type == 'Book 4':
                # Study S-BF: Continuous Anti-Chase Sizing Overlay for Book 4
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

    return pd.DataFrame(trades), _state_out()
