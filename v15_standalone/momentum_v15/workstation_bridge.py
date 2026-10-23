"""
Kronos V15.2: Quant Trading Workstation Data Bridge
Transforms raw market shards, exotic derivatives, canonical tape trades,
and flight-recorder veto telemetry into high-fidelity JSON payloads for
TradingView Lightweight Charts.
"""

import math
from pathlib import Path
from typing import Dict, Any, List, Optional
import numpy as np
import pandas as pd

from momentum_v15.features_v12 import load_shard, compute_features_v12, get_btc_macro
from momentum_v15.tier_classifier import get_all_universe_tiers
from momentum_v15.config import V12Config

_TIER_CACHE: Optional[Dict[str, str]] = None
_CANONICAL_TRADES_CACHE: Optional[pd.DataFrame] = None
_VETO_TELEMETRY_CACHE: Optional[pd.DataFrame] = None


def _get_tier_map() -> Dict[str, str]:
    global _TIER_CACHE
    if _TIER_CACHE is not None:
        return _TIER_CACHE

    t1, t2, t3, _ = get_all_universe_tiers()
    mapping = {}
    for s in t1:
        mapping[s] = 'Tier 1'
    for s in t2:
        mapping[s] = 'Tier 2'
    for s in t3:
        mapping[s] = 'Tier 3'
    _TIER_CACHE = mapping
    return _TIER_CACHE


def _get_canonical_trades(arm: str = 'v15_2_production') -> pd.DataFrame:
    global _CANONICAL_TRADES_CACHE
    if _CANONICAL_TRADES_CACHE is not None:
        return _CANONICAL_TRADES_CACHE

    candidates = [
        Path(f"v15_standalone/data/all_tapes/{arm}/trades.parquet"),
        Path("data/canonical/canonical_v15_2_tape.parquet"),
        Path(f"data/all_tapes/{arm}/trades.parquet"),
        Path("data/canonical/canonical_v15_1_tape.parquet"),
    ]
    for c in candidates:
        if c.exists():
            try:
                df = pd.read_parquet(c)
                if not df.empty:
                    df['entry'] = pd.to_datetime(df['entry'])
                    if 'exit' in df.columns:
                        df['exit'] = pd.to_datetime(df['exit'], errors='coerce')
                    _CANONICAL_TRADES_CACHE = df
                    return _CANONICAL_TRADES_CACHE
            except Exception:
                continue

    _CANONICAL_TRADES_CACHE = pd.DataFrame()
    return _CANONICAL_TRADES_CACHE


def _get_veto_telemetry(arm: str = 'v15_2_production') -> pd.DataFrame:
    global _VETO_TELEMETRY_CACHE
    if _VETO_TELEMETRY_CACHE is not None:
        return _VETO_TELEMETRY_CACHE

    candidates = [
        Path(f"v15_standalone/data/all_tapes/{arm}/veto_telemetry.parquet"),
        Path(f"data/all_tapes/{arm}/veto_telemetry.parquet"),
        Path("v15_standalone/data/all_tapes/v15_1_production/veto_telemetry.parquet"),
    ]
    for c in candidates:
        if c.exists():
            try:
                df = pd.read_parquet(c)
                if not df.empty:
                    df['timestamp'] = pd.to_datetime(df['timestamp'])
                    _VETO_TELEMETRY_CACHE = df
                    return _VETO_TELEMETRY_CACHE
            except Exception:
                continue

    _VETO_TELEMETRY_CACHE = pd.DataFrame()
    return _VETO_TELEMETRY_CACHE


def get_available_workstation_symbols() -> List[Dict[str, Any]]:
    """Returns list of symbols sorted by Tier and Trade count for UI selection."""
    tier_map = _get_tier_map()
    trades_df = _get_canonical_trades()

    trade_counts = {}
    if not trades_df.empty and 'asset' in trades_df.columns:
        counts = trades_df['asset'].value_counts()
        trade_counts = counts.to_dict()

    items = []
    for sym, tier in tier_map.items():
        cnt = trade_counts.get(sym, 0)
        items.append({
            'symbol': sym,
            'tier': tier,
            'trade_count': cnt,
            'display_label': f"{sym} ({tier} · {cnt} trades)" if cnt > 0 else f"{sym} ({tier})"
        })

    # Sort Tier 1 first, then Tier 2, then Tier 3, then by trade count descending
    tier_order = {'Tier 1': 1, 'Tier 2': 2, 'Tier 3': 3}
    items.sort(key=lambda x: (tier_order.get(x['tier'], 9), -x['trade_count'], x['symbol']))
    return items


def sanitize_val(val: Any, default: Any = 0.0) -> Any:
    """Replaces NaN, Inf, None with valid JSON-compliant values."""
    if val is None:
        return default
    if isinstance(val, (int, np.integer)):
        return int(val)
    if isinstance(val, (float, np.floating)):
        if math.isnan(val) or math.isinf(val):
            return default
        return round(float(val), 6)
    return val


def build_workstation_payload(
    symbol: str,
    arm: str = 'v15_2_production',
    lookback_bars: Optional[int] = 3000
) -> Dict[str, Any]:
    """
    Constructs high-fidelity JSON payload for TradingView Lightweight Charts
    containing candlesticks, volume, open interest, L/S, funding, step-line
    overlays, trade entry/exit pins, veto markers, and the point-in-time
    decision inspection index.
    """
    clean_sym = symbol.replace('USDT', '').replace('1000', '').replace('_', '').strip().upper()
    tier_map = _get_tier_map()
    tier = tier_map.get(clean_sym, 'Tier 3')

    # Candidate shard directory resolution
    raw_dir_candidates = [
        Path("data/raw_shards"),
        Path("v15_standalone/data/raw_shards"),
        Path("../data/raw_shards"),
    ]
    raw_dir = None
    for d in raw_dir_candidates:
        if d.exists() and d.is_dir():
            raw_dir = d
            break
    if raw_dir is None:
        raise FileNotFoundError("Could not find data/raw_shards directory")

    exotic_dir = raw_dir.parent / "exotic_shards"

    # Load Shard
    raw_df = load_shard(clean_sym, raw_dir, exotic_dir)
    if raw_df is None or raw_df.empty:
        # Try alternate asset spelling if needed
        raw_df = load_shard(clean_sym.replace('1000', ''), raw_dir, exotic_dir)
    if raw_df is None or raw_df.empty:
        raise FileNotFoundError(f"No candlestick shard found for asset {clean_sym}")

    # Compute Features causally
    btc_df = get_btc_macro(raw_dir=raw_dir)
    cfg = V12Config()
    feat_df = compute_features_v12(raw_df, btc_df=btc_df, tier_label=tier, cfg=cfg)

    # Optional slice to lookback_bars
    if lookback_bars is not None and len(feat_df) > lookback_bars:
        feat_df = feat_df.iloc[-lookback_bars:].copy()

    # Load trades and filter to this asset
    trades_all = _get_canonical_trades(arm)
    asset_trades = trades_all[trades_all['asset'] == clean_sym].copy() if not trades_all.empty else pd.DataFrame()

    # Load veto telemetry and filter to this asset
    veto_all = _get_veto_telemetry(arm)
    asset_veto = veto_all[veto_all['asset'] == clean_sym].copy() if not veto_all.empty else pd.DataFrame()

    # Pre-index trades by timestamp for fast lookup
    entry_trade_map = {}
    exit_trade_map = {}
    active_position_ranges = []

    if not asset_trades.empty:
        for _, tr in asset_trades.iterrows():
            entry_ts = pd.to_datetime(tr['entry'])
            exit_ts = pd.to_datetime(tr['exit']) if pd.notna(tr['exit']) else None
            entry_trade_map[entry_ts] = tr
            if exit_ts is not None and not tr.get('is_open', False):
                exit_trade_map[exit_ts] = tr
            active_position_ranges.append({
                'entry_ts': entry_ts,
                'exit_ts': exit_ts if exit_ts is not None else pd.Timestamp.max,
                'trade': tr
            })

    # Pre-index veto telemetry
    veto_map = {}
    if not asset_veto.empty:
        for _, vt in asset_veto.iterrows():
            vt_ts = pd.to_datetime(vt['timestamp'])
            veto_map[vt_ts] = vt

    # Prepare Lightweight Charts arrays
    candles_data = []
    volume_data = []
    oi_data = []
    ls_data = []
    funding_data = []
    donchian_data = []
    shelf_data = []
    resting_stop_data = []
    ema200_data = []

    markers_list = []
    events_list = []
    inspection_index = {}

    timestamps = feat_df.index
    n_rows = len(feat_df)

    # Compute trailing stop mapping for each open position
    for idx in range(n_rows):
        row = feat_df.iloc[idx]
        ts: pd.Timestamp = timestamps[idx]
        t_sec = int(ts.timestamp())

        o = sanitize_val(row.get('open', 0.0))
        h = sanitize_val(row.get('high', 0.0))
        l = sanitize_val(row.get('low', 0.0))
        c = sanitize_val(row.get('close', 0.0))
        v = sanitize_val(row.get('volume', 0.0))

        # Main Candle
        candles_data.append({
            'time': t_sec,
            'open': o,
            'high': h,
            'low': l,
            'close': c
        })

        # Volume histogram with green/red taker coloration
        vol_color = 'rgba(0, 255, 135, 0.65)' if c >= o else 'rgba(255, 70, 85, 0.65)'
        volume_data.append({
            'time': t_sec,
            'value': v,
            'color': vol_color
        })

        # Open Interest
        oi_val = sanitize_val(row.get('oi_tokens', row.get('oi_usd', 0.0)))
        oi_data.append({'time': t_sec, 'value': oi_val})

        # Top Trader Long/Short Ratio
        ls_val = sanitize_val(row.get('toptrader_ls', 1.0))
        ls_data.append({'time': t_sec, 'value': ls_val})

        # Funding Rate
        fr_raw = sanitize_val(row.get('funding_rate', 0.0))
        fr_color = 'rgba(0, 240, 255, 0.85)' if fr_raw >= 0 else 'rgba(255, 70, 85, 0.85)'
        funding_data.append({
            'time': t_sec,
            'value': fr_raw,
            'color': fr_color
        })

        # Overlays: Donchian 14d Floor / 72h Low
        d_floor = sanitize_val(row.get('low_14d', row.get('low_72h', l)))
        if d_floor > 0:
            donchian_data.append({'time': t_sec, 'value': d_floor})

        # Compression Shelf: 72h High
        c_shelf = sanitize_val(row.get('high_72h', h))
        if c_shelf > 0:
            shelf_data.append({'time': t_sec, 'value': c_shelf})

        # 200d EMA
        ema_val = sanitize_val(row.get('ema200_1d', row.get('ema_168', 0.0)))
        if ema_val > 0:
            ema200_data.append({'time': t_sec, 'value': ema_val})

        # Active trade evaluation & Resting Stop
        active_trade_here = None
        for pos in active_position_ranges:
            if pos['entry_ts'] <= ts <= pos['exit_ts']:
                active_trade_here = pos['trade']
                break

        current_stop_price = None
        if active_trade_here is not None:
            # Trailing stop ratchet logic: max of initial stop and donchian 72h low
            init_stop = sanitize_val(active_trade_here.get('initial_stop', 0.0))
            trail_stop = sanitize_val(row.get('low_72h', init_stop))
            current_stop_price = max(init_stop, trail_stop) if init_stop > 0 else trail_stop
            if current_stop_price > 0:
                resting_stop_data.append({'time': t_sec, 'value': current_stop_price})

        # Entry Marker Check
        is_entry = ts in entry_trade_map
        is_exit = ts in exit_trade_map
        is_veto = ts in veto_map

        if is_entry:
            trade_obj = entry_trade_map[ts]
            book_label = str(trade_obj.get('book', 'Entry'))
            entry_p = sanitize_val(trade_obj.get('entry_price', c))
            markers_list.append({
                'time': t_sec,
                'position': 'belowBar',
                'color': '#00ff87',
                'shape': 'arrowUp',
                'text': f"{book_label} @ ${entry_p:g}",
                'id': f"entry_{t_sec}"
            })
            events_list.append({
                'time': t_sec,
                'type': 'entry',
                'label': f"Entry: {book_label}",
                'price': entry_p,
                'ts_iso': str(ts)
            })

        if is_exit:
            trade_obj = exit_trade_map[ts]
            exit_p = sanitize_val(trade_obj.get('exit_price', c))
            raw_pnl = sanitize_val(trade_obj.get('raw_pnl', trade_obj.get('pnl', 0.0)))
            reason = str(trade_obj.get('reason', 'exit'))
            pnl_pct_str = f"{raw_pnl * 100:+.1f}%"
            exit_color = '#00ff87' if raw_pnl >= 0 else '#ff4655'
            markers_list.append({
                'time': t_sec,
                'position': 'aboveBar',
                'color': exit_color,
                'shape': 'arrowDown',
                'text': f"Exit: {reason} ({pnl_pct_str})",
                'id': f"exit_{t_sec}"
            })
            events_list.append({
                'time': t_sec,
                'type': 'exit',
                'label': f"Exit: {reason} ({pnl_pct_str})",
                'price': exit_p,
                'ts_iso': str(ts)
            })

        if is_veto:
            vt_obj = veto_map[ts]
            gate = str(vt_obj.get('veto_gate', 'Veto'))
            is_dodged = bool(vt_obj.get('is_dodged_bullet', False))
            veto_color = '#ff4655' if is_dodged else '#f59e0b'
            markers_list.append({
                'time': t_sec,
                'position': 'aboveBar',
                'color': veto_color,
                'shape': 'circle',
                'text': f"VETO: {gate}",
                'id': f"veto_{t_sec}"
            })
            events_list.append({
                'time': t_sec,
                'type': 'veto',
                'label': f"Veto: {gate}",
                'price': sanitize_val(vt_obj.get('price', c)),
                'ts_iso': str(ts)
            })

        # Build point-in-time causal decision inspection state
        z_ls = sanitize_val(row.get('z_ls_30d', 0.0))
        pct_ls = sanitize_val(row.get('pct_ls_30d', 50.0))
        z_fnd = sanitize_val(row.get('z_fnd_30d', 0.0))
        d_oi_24 = sanitize_val(row.get('d_oi_tokens_24h', 0.0)) * 100.0
        shelf_rng = sanitize_val(row.get('shelf_range_72h', 0.0)) * 100.0
        vol_comp = sanitize_val(row.get('vol_comp', 1.0))
        funding_apr = fr_raw * 3 * 365 * 100.0

        # Formulate Causal Checklist
        # 1. Trend Filter: close >= 200d EMA
        trend_pass = bool(c >= ema_val) if ema_val > 0 else True
        # 2. Volume Spike: vol_comp >= 1.2
        vol_pass = bool(vol_comp >= 1.2)
        # 3. Leverage Bubble Firewall: d_oi_tokens_24h <= 35%
        oi_pass = bool(d_oi_24 <= 35.0)
        # 4. Whale Positioning: z_ls <= -0.50 (whale squeeze) or retail not trapped long
        whale_pass = bool(pct_ls < 80.0 or z_ls < 0.80)
        # 5. Funding Carry: z_fnd <= +0.25
        carry_pass = bool(z_fnd <= 0.25)
        # 6. Coiled Shelf Compression: shelf_range <= 15%
        shelf_pass = bool(shelf_rng <= 15.0)

        conditions_list = [
            {
                'name': 'Trend Filter (200d EMA)',
                'status': 'pass' if trend_pass else 'fail',
                'value': f"${c:g} >= ${ema_val:g}" if ema_val > 0 else 'N/A',
                'desc': 'Price must hold structural acceptance above 200d EMA'
            },
            {
                'name': 'Volume Shock',
                'status': 'pass' if vol_pass else 'fail',
                'value': f"{vol_comp:.2f}x baseline",
                'desc': 'ATR24 / ATR168 expansion >= 1.20x'
            },
            {
                'name': 'Leverage Bubble Firewall',
                'status': 'pass' if oi_pass else 'fail',
                'value': f"{d_oi_24:+.1f}% in 24h",
                'desc': '24h Token OI expansion must not exceed +35% capacity ceiling'
            },
            {
                'name': 'Whale Squeeze Positioning',
                'status': 'pass' if whale_pass else 'fail',
                'value': f"z_ls={z_ls:+.2f}σ ({pct_ls:.0f}%ile)",
                'desc': 'Top Trader Whale counter-bias protected against toxic crowd traps'
            },
            {
                'name': 'Funding Carry Governor',
                'status': 'pass' if carry_pass else 'fail',
                'value': f"z_fnd={z_fnd:+.2f}σ ({funding_apr:+.1f}% APR)",
                'desc': 'Studentized 30d carry must stay below +0.25σ euphoria threshold'
            },
            {
                'name': 'Coiled Base Compression',
                'status': 'pass' if shelf_pass else 'skip',
                'value': f"Shelf={shelf_rng:.1f}%",
                'desc': '72-Hour price range tightly coiled prior to breakout ignition'
            }
        ]

        # Determine Banner State
        banner_type = 'neutral'
        banner_text = 'No Active Signal · Monitoring Tape'
        if is_entry:
            banner_type = 'entry'
            banner_text = f"ENTRY TRIGGERED: {entry_trade_map[ts].get('book', 'Long')}"
        elif is_veto:
            banner_type = 'veto'
            banner_text = f"VETO ENFORCED: {veto_map[ts].get('veto_gate', 'Gate Block')}"
        elif is_exit:
            raw_pnl = sanitize_val(exit_trade_map[ts].get('raw_pnl', exit_trade_map[ts].get('pnl', 0.0)))
            banner_type = 'entry' if raw_pnl >= 0 else 'veto'
            banner_text = f"POSITION CLOSED: {exit_trade_map[ts].get('reason', 'Exit')} ({raw_pnl * 100:+.1f}%)"
        elif active_trade_here is not None:
            entry_p = sanitize_val(active_trade_here.get('entry_price', c))
            curr_gain = ((c - entry_p) / entry_p) * 100.0 if entry_p > 0 else 0.0
            banner_type = 'entry'
            banner_text = f"ACTIVE LONG: {active_trade_here.get('book', 'Position')} ({curr_gain:+.1f}% MTM)"

        # Position Risk State
        risk_info = {}
        if active_trade_here is not None:
            init_stop = sanitize_val(active_trade_here.get('initial_stop', 0.0))
            entry_p = sanitize_val(active_trade_here.get('entry_price', c))
            dist_stop = ((c - current_stop_price) / c) * 100.0 if current_stop_price and c > 0 else 0.0
            risk_info = {
                'entry_price': f"${entry_p:g}",
                'initial_stop': f"${init_stop:g}",
                'current_stop': f"${current_stop_price:g}" if current_stop_price else 'N/A',
                'dist_to_stop': f"{dist_stop:.2f}%",
                'pnl_mtm': f"{((c - entry_p) / entry_p) * 100:+.2f}%" if entry_p > 0 else '0.0%',
                'book': str(active_trade_here.get('book', 'Book')),
                'sizing': f"{sanitize_val(active_trade_here.get('sizing_weight', 1.0)):.2f}x"
            }

        # Veto Details
        veto_info = {}
        if is_veto:
            vt = veto_map[ts]
            veto_info = {
                'gate': str(vt.get('veto_gate', 'Gate')),
                'setup': str(vt.get('candidate_setup', 'Setup')),
                'is_dodged': bool(vt.get('is_dodged_bullet', False)),
                'is_missed': bool(vt.get('is_missed_opportunity', False)),
                'mfe_72h': f"{sanitize_val(vt.get('mfe_72h_fwd', 0.0)) * 100:+.1f}%",
                'ret_24h': f"{sanitize_val(vt.get('ret_24h_fwd', 0.0)) * 100:+.1f}%",
            }

        # Monospace OHLC summary string
        ohlcv_summary = {
            'open': f"${o:g}",
            'high': f"${h:g}",
            'low': f"${l:g}",
            'close': f"${c:g}",
            'volume': f"{v:,.0f}",
            'oi': f"{oi_val:,.0f} ({d_oi_24:+.1f}%)",
            'funding': f"{fr_raw * 100:.4f}% ({funding_apr:+.1f}% APR)",
            'ls_ratio': f"{ls_val:.2f} (z={z_ls:+.2f}σ)"
        }

        inspection_index[str(t_sec)] = {
            'timestamp_iso': str(ts),
            'ohlcv': ohlcv_summary,
            'banner': {
                'type': banner_type,
                'text': banner_text
            },
            'conditions': conditions_list,
            'risk': risk_info,
            'veto': veto_info
        }

    # Summary Statistics for Ribbon
    last_row = feat_df.iloc[-1]
    last_close = sanitize_val(last_row.get('close', 0.0))
    first_close_24h = sanitize_val(feat_df.iloc[-25].get('close', last_close)) if len(feat_df) >= 25 else last_close
    chg_24h = ((last_close - first_close_24h) / first_close_24h) * 100.0 if first_close_24h > 0 else 0.0

    vol_24h = sanitize_val(feat_df.iloc[-24:]['volume'].sum()) if len(feat_df) >= 24 else sanitize_val(feat_df['volume'].sum())
    last_oi = sanitize_val(last_row.get('oi_tokens', last_row.get('oi_usd', 0.0)))
    last_ls = sanitize_val(last_row.get('toptrader_ls', 1.0))
    last_fr = sanitize_val(last_row.get('funding_rate', 0.0))

    tot_trades = len(asset_trades)
    win_cnt = len(asset_trades[asset_trades['pnl'] > 0]) if tot_trades > 0 else 0
    win_rate = (win_cnt / tot_trades) * 100.0 if tot_trades > 0 else 0.0
    tot_pnl = sanitize_val(asset_trades['pnl'].sum()) * 100.0 if tot_trades > 0 else 0.0

    summary = {
        'symbol': clean_sym,
        'tier': tier,
        'last_price': f"${last_close:g}",
        'chg_24h': f"{chg_24h:+.2f}%",
        'chg_24h_val': chg_24h,
        'vol_24h': f"{vol_24h:,.0f}",
        'open_interest': f"{last_oi:,.0f}",
        'ls_ratio': f"{last_ls:.2f}",
        'funding_apr': f"{last_fr * 3 * 365 * 100:+.1f}% APR",
        'trade_count': tot_trades,
        'win_rate': f"{win_rate:.1f}%",
        'total_pnl': f"{tot_pnl:+.1f}%",
    }

    return {
        'symbol': clean_sym,
        'tier': tier,
        'summary': summary,
        'candles': candles_data,
        'volume': volume_data,
        'open_interest': oi_data,
        'toptrader_ls': ls_data,
        'funding_rate': funding_data,
        'donchian_floor': donchian_data,
        'compression_shelf': shelf_data,
        'resting_stop': resting_stop_data,
        'ema200': ema200_data,
        'markers': markers_list,
        'events': events_list,
        'inspection_index': inspection_index
    }
