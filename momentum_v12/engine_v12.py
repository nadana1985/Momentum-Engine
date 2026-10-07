"""
Kronos V12: Pure 6-Core Execution Kernel (engine_v12.py)
Executes Macro Gating, Dynamic Tier Floors, Whale Firewalling, Bear Trap Reclaims,
and Climax Top Harvesting.
"""

from typing import Dict, List, Optional
import numpy as np
import pandas as pd

from momentum_v12.config import V12Config
from momentum_v12.telemetry_v12 import TelemetryCollector, TelemetryRecord


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
    active: Optional[Dict] = None

    last_exit_ts: Optional[pd.Timestamp] = None
    last_exit_reason: Optional[str] = None
    last_exit_pnl: float = 0.0
    last_entry_price: float = 0.0
    flush_low_since_exit: float = float('inf')
    active_shadow_anchor: Optional[Dict] = None
    active_flush_bid: Optional[Dict] = None

    tier = str(df['tier'].iloc[0]) if 'tier' in df.columns else 'Tier 1'
    is_tier1 = (tier == 'Tier 1')

    # Precompute rolling series for speed
    ls_series = df.get('toptrader_ls', pd.Series(1.0, index=df.index)).ffill()
    max_ls_7d_series = ls_series.shift(1).rolling(168, min_periods=24).max()

    slippage = cfg.entry.slippage

    for ts, row in df.iterrows():
        c = float(row['close'])
        h = float(row['high'])
        l = float(row['low'])
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

        if active is None and last_exit_ts is not None:
            flush_low_since_exit = min(flush_low_since_exit, l)

        # Check Book 3: Active resting flush bid fill or expiry
        if getattr(cfg.book3_flush, 'enable_book3_flush_reclaim', False):
            if active_flush_bid is not None and active is None:
                bid_age_h = (ts - active_flush_bid['armed_ts']).total_seconds() / 3600.0
                if bid_age_h > active_flush_bid['ttl_bars']:
                    active_flush_bid = None # Expired
                elif l <= active_flush_bid['bid_px']: # Filled at limit!
                    entry_px = active_flush_bid['bid_px']
                    active = {
                        'entry_time': ts,
                        'entry_price': entry_px,
                        'stop': active_flush_bid['stop_px'],
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

        # -------------------------------------------------------------
        # 1. ACTIVE POSITION MANAGEMENT & CLIMAX HARVESTING
        # -------------------------------------------------------------
        if active is not None:
            active['max_high'] = max(active['max_high'], h)
            active['min_low'] = min(active['min_low'], l)
            dur_hours = (ts - active['entry_time']).total_seconds() / 3600.0
            mfe = (active['max_high'] - active['entry_price']) / active['entry_price']
            mae = (active['min_low'] - active['entry_price']) / active['entry_price']

            entry_oi = active.get('entry_oi', current_oi)
            oi_change = (current_oi - entry_oi) / entry_oi if entry_oi > 0 else 0.0
            book_type = active.get('book', 'Book 1')

            # Trailing Floor & Ratchets
            if book_type == 'Book 3':
                pass # Fixed target reclaim & stop floor
            elif book_type == 'Book 2':
                if mfe >= 0.15:
                    active['stop'] = max(active['stop'], active['entry_price'] * 1.005)
                if mfe >= 0.35:
                    active['stop'] = max(active['stop'], active['max_high'] * 0.85)
                if mfe >= 0.70:
                    active['stop'] = max(active['stop'], active['max_high'] * 0.80)
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
                if is_tier1:
                    floor_14d = float(row.get('low_14d', active['stop']))
                    if pd.notna(floor_14d) and floor_14d > active['stop']:
                        active['stop'] = floor_14d
                    if mfe >= cfg.exit.tier1_be_ratchet_mfe:
                        active['stop'] = max(active['stop'], active['entry_price'] * 1.005)
                    if mfe >= cfg.exit.tier1_trail_ratchet_mfe:
                        active['stop'] = max(active['stop'], active['max_high'] * cfg.exit.tier1_trail_floor_pct)
                else: # Tier 2 (Calibrated 7d Floor)
                    floor_7d = float(row.get('low_7d', active['stop']))
                    if pd.notna(floor_7d) and floor_7d > active['stop']:
                        active['stop'] = floor_7d
                    if mfe >= cfg.exit.tier2_be_ratchet_mfe:
                        active['stop'] = max(active['stop'], active['entry_price'] * 1.005)
                    if mfe >= cfg.exit.tier2_trail_ratchet_mfe:
                        active['stop'] = max(active['stop'], active['max_high'] * cfg.exit.tier2_trail_floor_pct)

            exit_triggered = False
            exit_price = 0.0
            exit_reason = ""

            # Core 6 Exits: Climax Air-Pocket Harvest & Fast Decay Cuts
            if book_type == 'Book 3':
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
                # Velocity & Fast OI Decay Bailouts
                elif not is_tier1 and dur_hours >= cfg.exit.tier2_fast_decay_hours and oi_change <= cfg.exit.tier2_fast_decay_oi_leak and c < active['entry_price']:
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

            # Study S-AA: 36-Hour Stagnation Stall-Out Bailout (Zero-Runner Loss Checkpoint)
            if not exit_triggered and cfg.exit.enable_stall_bailout:
                if dur_hours >= cfg.exit.stall_bailout_hours and mfe < cfg.exit.stall_bailout_max_mfe and c < active['entry_price']:
                    exit_price = c * (1 - slippage)
                    exit_triggered = True
                    exit_reason = "stall_bailout"

            # Native Resting Stop-Market Order Execution
            if not exit_triggered:
                if l <= active['stop']:
                    exit_price = min(float(row.get('open', active['stop'])), active['stop']) * (1 - slippage)
                    exit_triggered = True
                    if active['stop'] >= active['entry_price'] * 1.015:
                        exit_reason = "trail_stop"
                    elif active['stop'] >= active['entry_price'] * 1.005:
                        exit_reason = "breakeven_ratchet"
                    else:
                        exit_reason = "initial_stop"
                elif dur_hours >= (cfg.exit.b2_time_cap_hours if book_type == 'Book 2' else (cfg.exit.time_cap_hours_t1 if is_tier1 else cfg.exit.time_cap_hours_t2)):
                    exit_price = c * (1 - slippage)
                    exit_triggered = True
                    exit_reason = "time_cap"

            if exit_triggered:
                raw_pnl = (exit_price - active['entry_price']) / active['entry_price']
                if book_type == 'Book 3':
                    w = 1.0
                else:
                    w_lam = float(np.clip(cfg.sizing.base_weight - active.get('pct_lam', 0.50), cfg.sizing.min_weight, cfg.sizing.max_weight)) if cfg.sizing.enable_lambda_sizing else 1.0
                    w_to = float(np.minimum(1.0, 15.0 / max(1e-4, active.get('turnover_at_entry', 1.0)))) if getattr(cfg.micro, 'enable_turnover_scaling', False) else 1.0
                    w = float(np.clip(w_lam * w_to, 0.10, 1.50))
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
                    # MEDIUM-3: entry OI saved for post-trade OI expansion analysis
                    'entry_oi_usd': active.get('entry_oi', 0.0),
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

            is_candidate = is_b2_candidate or can_reclaim or can_shadow_reclaim or is_breakout or is_continuation_candidate
            if not is_candidate:
                continue

            if is_b2_candidate:
                candidate_setup = "Squeeze Hunter"
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
                    if tier == 'Tier 2' and not getattr(cfg.book3_flush, 'enable_tier2', False):
                        return
                    if tier == 'Tier 3' and not getattr(cfg.book3_flush, 'enable_tier3', True):
                        return

                    discount = (
                        cfg.book3_flush.tier2_flush_discount_pct
                        if tier == 'Tier 2'
                        else cfg.book3_flush.flush_discount_pct
                    )
                    bid_p = c * (1.0 - discount)
                    active_flush_bid = {
                        'trigger_px': c,
                        'bid_px': bid_p,
                        'stop_px': bid_p * (1.0 - cfg.book3_flush.max_initial_risk),
                        'target_px': c,
                        'armed_ts': ts,
                        'ttl_bars': cfg.book3_flush.ttl_hours,
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
                    continue
                fill_px = c * (1 + slippage)
                low_72 = float(row.get('low_72h', l))
                raw_floor = max(low_72 * (1 - slippage), fill_px * (1 - cfg.micro.b2_max_initial_risk))
                clamped_stop = max(raw_floor, fill_px * (1 - cfg.micro.b2_max_initial_risk))
                active = {
                    'entry_time': ts,
                    'entry_price': fill_px,
                    'stop': clamped_stop,
                    'max_high': h,           # use bar high for immediate MFE tracking
                    'min_low': l,            # HIGH-2 FIX: use bar low (not fill_px) for accurate MAE
                    'book': 'Book 2',
                    'is_reclaim': False,
                    'entry_oi': current_oi
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
            else:
                is_reclaim = False
                is_continuation = False
                reclaim_floor = None
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
                fill_px = c * (1 + slippage)
                if is_continuation:
                    max_initial_risk = cfg.entry.continuation_max_initial_risk
                    raw_floor = max(low_14d * (1 - slippage), fill_px * (1.0 - max_initial_risk))
                    clamped_stop = max(raw_floor, fill_px * (1.0 - max_initial_risk))
                    book_label = 'Continuation'
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

                pct_lam_val = float(row.get('pct_lambda', 0.50))
                to_val = float(turnover) if pd.notna(turnover) else 1.0
                active = {
                    'entry_time': ts,
                    'entry_price': fill_px,
                    'stop': clamped_stop,
                    'max_high': h,           # use bar high for immediate MFE tracking
                    'min_low': l,            # HIGH-2 FIX: use bar low (not fill_px) for accurate MAE
                    'book': book_label,
                    'is_reclaim': is_reclaim,
                    'is_continuation': is_continuation,
                    'entry_oi': current_oi,
                    'pct_lam': pct_lam_val,
                    'turnover_at_entry': to_val
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

    # Mark active position as open at end of tape
    if active is not None:
        last_c = float(df.iloc[-1]['close'])
        raw_pnl = (last_c - active['entry_price']) / active['entry_price']
        if active.get('book') == 'Book 3':
            w = 1.0
        else:
            w_lam = float(np.clip(cfg.sizing.base_weight - active.get('pct_lam', 0.50), cfg.sizing.min_weight, cfg.sizing.max_weight)) if cfg.sizing.enable_lambda_sizing else 1.0
            w_to = float(np.minimum(1.0, 15.0 / max(1e-4, active.get('turnover_at_entry', 1.0)))) if getattr(cfg.micro, 'enable_turnover_scaling', False) else 1.0
            w = float(np.clip(w_lam * w_to, 0.10, 1.50))
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
            # MEDIUM-3: entry OI for post-trade OI expansion analysis
            'entry_oi_usd': active.get('entry_oi', 0.0),
        })

    return pd.DataFrame(trades)
