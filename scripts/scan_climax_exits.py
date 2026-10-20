#!/usr/bin/env python3
"""
Kronos Quantitative Engine: 6-Signature Climax Exit & Position Hold Scanner
Evaluates active momentum runners and short squeezes (both OGN-type and MAGIC-type)
across the 6 verified Climax Exhaustion Signatures + Study S-N & BTR Air-Pocket Laws
to determine whether to:
  • HOLD_STRONG / ADD_ON_DIP (Mid-run shakeout where shorts are piling in)
  • RATCHET_STOP / TRAIL     (Early momentum deceleration)
  • CLIMAX_HARVEST_NOW       (Peak blow-off exhaustion: >=3/6 Exit Alarms firing)
  • POST_CLIMAX_DISTRIBUTION (Move over: OI unwinding & whales covering top-shorts)

The 6 Quantitative Climax Exit Signatures (0 to 100 Exit Urgency Score):
  [Sig 1] Climax Pinbar Upper Wick Rejection (Max 20 pts): Upper wick >= 75% at cycle high
  [Sig 2] Volume & Trade Count Bearish Divergence (Max 20 pts): >= 50% drop vs 24h peak + Ticket Size contraction
  [Sig 3] Token Open Interest Divergence & Unwind (Max 20 pts): Token OI drops below 24h peak (-4% to -35%)
  [Sig 4] 10x Funding Rate Collapse / Euphoria Flip (Max 15 pts): Extreme negative carry snaps to 0% or flips >+0.05%
  [Sig 5] Taker Buy Breakdown & Velocity Stall (Max 15 pts): Taker Buy < 49.5% + Vol Shock drops <= 1.25x
  [Sig 6] Whale L/S Floor Inflection (Max 10 pts): Whale L/S bottoms (<0.85) and turns UP while OI bleeds

Usage:
  python scripts/scan_climax_exits.py --symbol ERA
  python scripts/scan_climax_exits.py --symbol OGN --as-of "2026-10-08 20:00:00"
  python scripts/scan_climax_exits.py --watchlist "ERA,MAGIC,CTSI,OGN,C98,KAIA"
  python scripts/scan_climax_exits.py --scan
"""

import os
import sys
import glob
import argparse
import json
import pandas as pd
import numpy as np

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')


def resolve_symbol_shards(sym):
    clean = sym.upper().replace('USDT', '').replace('PERP', '').replace('_', '').strip()
    raw_candidates = [
        f"data/raw_shards/{clean}_USDT_1h.parquet",
        f"data/raw_shards/{clean}USDT_1h.parquet",
        f"data/raw_shards/{clean}_1h.parquet",
        f"data/raw_shards/*{clean}*_1h.parquet"
    ]
    raw_file = None
    for pat in raw_candidates:
        matches = glob.glob(pat)
        if matches:
            raw_file = matches[0]
            break

    met_candidates = [
        f"data/exotic_shards/{clean}USDT_metrics.parquet",
        f"data/exotic_shards/{clean}_USDT_metrics.parquet",
        f"data/exotic_shards/*{clean}*metrics.parquet"
    ]
    met_file = None
    for pat in met_candidates:
        matches = glob.glob(pat)
        if matches:
            met_file = matches[0]
            break

    fund_candidates = [
        f"data/exotic_shards/{clean}USDT_funding.parquet",
        f"data/exotic_shards/{clean}_USDT_funding.parquet",
        f"data/exotic_shards/*{clean}*funding.parquet"
    ]
    fund_file = None
    for pat in fund_candidates:
        matches = glob.glob(pat)
        if matches:
            fund_file = matches[0]
            break

    return clean, raw_file, met_file, fund_file


def evaluate_exit_signature(sym, as_of=None):
    clean, raw_file, met_file, fund_file = resolve_symbol_shards(sym)
    if not raw_file or not os.path.exists(raw_file):
        return None, f"Raw shard not found for {sym}"

    try:
        ohlc = pd.read_parquet(raw_file)
        tcol = 'open_time' if 'open_time' in ohlc.columns else ('timestamp' if 'timestamp' in ohlc.columns else None)
        if tcol:
            ohlc['dt'] = pd.to_datetime(ohlc[tcol], unit='ms')
        elif isinstance(ohlc.index, pd.DatetimeIndex):
            ohlc['dt'] = ohlc.index
            ohlc = ohlc.reset_index(drop=True)
        else:
            return None, "Timestamp not found"

        df = ohlc.sort_values('dt').reset_index(drop=True)

        if met_file and os.path.exists(met_file):
            met = pd.read_parquet(met_file)
            if 'timestamp' in met.columns:
                met['dt'] = pd.to_datetime(met['timestamp'], unit='ms')
            df = pd.merge_asof(df, met.sort_values('dt'), on='dt', direction='backward')
        else:
            df['sum_open_interest'] = np.nan
            df['sum_open_interest_value'] = np.nan
            df['count_toptrader_long_short_ratio'] = np.nan

        if fund_file and os.path.exists(fund_file):
            fund = pd.read_parquet(fund_file)
            if 'timestamp' in fund.columns:
                fund['dt'] = pd.to_datetime(fund['timestamp'], unit='ms')
            df = pd.merge_asof(df, fund[['dt', 'funding_rate']].sort_values('dt'), on='dt', direction='backward')
        else:
            df['funding_rate'] = np.nan

        if as_of is not None:
            as_of_dt = pd.to_datetime(as_of)
            df = df[df['dt'] <= as_of_dt].copy()

        if len(df) < 72:
            return None, f"Insufficient history ({len(df)} bars)"

        # Macro Breakdown Targets (Sep 2025 Low & Nov 2025 Low)
        sep25_sub = df[(df['dt'] >= '2025-09-01') & (df['dt'] < '2025-10-01')]
        nov25_sub = df[(df['dt'] >= '2025-11-01') & (df['dt'] < '2025-12-01')]
        sep25_low = float(sep25_sub['low'].min()) if len(sep25_sub) > 0 else np.nan
        nov25_low = float(nov25_sub['low'].min()) if len(nov25_sub) > 0 else np.nan

        # Multi-Timeframe 200 EMA Convergence Law (1h, 4h, 1D EMA200 & 1D SMA200)
        ema200_1h = float(df['close'].ewm(span=200, adjust=False).mean().iloc[-1])
        df_4h = df.set_index('dt')[['close']].resample('4h').last().dropna()
        ema200_4h = float(df_4h['close'].ewm(span=200, adjust=False).mean().iloc[-1]) if len(df_4h) > 0 else ema200_1h
        df_1d = df.set_index('dt')[['close']].resample('1D').last().dropna()
        ema200_1d = float(df_1d['close'].ewm(span=200, adjust=False).mean().iloc[-1]) if len(df_1d) > 0 else ema200_4h
        sma200_1d = float(df_1d['close'].rolling(200).mean().iloc[-1]) if len(df_1d) >= 200 else ema200_1d

        w72 = df.tail(72).copy()
        w24 = df.tail(24).copy()
        cur_row = df.iloc[-1]

        cur_price = float(cur_row['close'])
        high_72h = float(w72['high'].max())
        low_72h = float(w72['low'].min())
        high_24h = float(w24['high'].max())
        low_24h = float(w24['low'].min())

        price_vs_ema200_1d_pct = ((cur_price / max(ema200_1d, 1e-12)) - 1.0) * 100.0
        ema_1h_vs_1d_gap_pct = ((ema200_1h / max(ema200_1d, 1e-12)) - 1.0) * 100.0
        candidate_tier = "LEADING" if (price_vs_ema200_1d_pct >= -3.0 and ema_1h_vs_1d_gap_pct >= -15.0) else "LAGGING"

        sep25_high_diff_pct = (((high_72h - sep25_low) / max(sep25_low, 1e-12)) * 100.0) if pd.notna(sep25_low) else np.nan
        sep25_cur_upside_pct = (((sep25_low - cur_price) / max(cur_price, 1e-12)) * 100.0) if pd.notna(sep25_low) else np.nan
        nov25_cur_upside_pct = (((nov25_low - cur_price) / max(cur_price, 1e-12)) * 100.0) if pd.notna(nov25_low) else np.nan

        mfe_72h_pct = ((high_72h - low_72h) / max(low_72h, 1e-12)) * 100.0
        gain_from_72h_low_pct = ((cur_price - low_72h) / max(low_72h, 1e-12)) * 100.0
        drawdown_from_72h_high_pct = ((cur_price - high_72h) / max(high_72h, 1e-12)) * 100.0

        ret_1h = ((cur_price - float(cur_row['open'])) / max(float(cur_row['open']), 1e-12)) * 100.0
        ret_24h = ((cur_price - float(w24['open'].iloc[0])) / max(float(w24['open'].iloc[0]), 1e-12)) * 100.0

        # Upper wick of current bar and max upper wick in last 3 bars near high
        cur_upper_wick_pct = ((float(cur_row['high']) - max(float(cur_row['open']), float(cur_row['close']))) / max(float(cur_row['high']) - float(cur_row['low']), 1e-12)) * 100.0

        # Volume & Trade Count metrics
        cur_count = float(cur_row['count']) if ('count' in cur_row and pd.notna(cur_row['count'])) else 0.0
        median_count_24h = float(w24['count'].median()) if ('count' in w24 and pd.notna(w24['count'].median())) else 1.0
        tc_velocity = (cur_count / max(median_count_24h, 1.0)) if median_count_24h > 0 else 1.0
        peak_count_24h = float(w24['count'].max()) if ('count' in w24 and pd.notna(w24['count'].max())) else cur_count
        tc_div_pct = (((cur_count - peak_count_24h) / max(peak_count_24h, 1.0)) * 100.0) if peak_count_24h > 0 else 0.0

        cur_vol_usd = float(cur_row['quote_volume']) if ('quote_volume' in cur_row and pd.notna(cur_row['quote_volume'])) else float(cur_row['volume'] * cur_price)
        median_vol_24h = float(w24['quote_volume'].median()) if 'quote_volume' in w24 else float((w24['volume'] * w24['close']).median())
        vol_shock = (cur_vol_usd / max(median_vol_24h, 1.0)) if median_vol_24h > 0 else 1.0
        peak_vol_24h_usd = float(w24['quote_volume'].max()) if 'quote_volume' in w24 else cur_vol_usd
        vol_div_pct = (((cur_vol_usd - peak_vol_24h_usd) / max(peak_vol_24h_usd, 1.0)) * 100.0) if peak_vol_24h_usd > 0 else 0.0

        avg_ticket_usd = (cur_vol_usd / max(cur_count, 1.0)) if cur_count > 0 else 0.0
        med_ticket_24h_usd = float((w24['quote_volume'] / w24['count'].replace(0, np.nan)).median()) if ('quote_volume' in w24 and 'count' in w24) else avg_ticket_usd
        ticket_ratio = (avg_ticket_usd / max(med_ticket_24h_usd, 1e-6)) if med_ticket_24h_usd > 0 else 1.0

        cur_taker_buy_usd = float(cur_row['taker_buy_quote_volume']) if ('taker_buy_quote_volume' in cur_row and pd.notna(cur_row['taker_buy_quote_volume'])) else (float(cur_row.get('taker_buy_base_volume', 0.0)) * cur_price)
        cur_taker_ratio = (cur_taker_buy_usd / max(cur_vol_usd, 1.0)) if cur_vol_usd > 0 else 0.50

        # Open Interest & BTR Air-Pocket Ratio
        cur_oi_usd = float(cur_row['sum_open_interest_value']) if pd.notna(cur_row.get('sum_open_interest_value')) else 0.0
        cur_oi_tokens = float(cur_row['sum_open_interest']) if pd.notna(cur_row.get('sum_open_interest')) else 0.0
        peak_oi_tokens_24h = float(w24['sum_open_interest'].max()) if pd.notna(w24['sum_open_interest'].max()) else cur_oi_tokens
        oi_div_pct = (((cur_oi_tokens - peak_oi_tokens_24h) / max(peak_oi_tokens_24h, 1.0)) * 100.0) if peak_oi_tokens_24h > 0 else 0.0
        air_pocket_ratio = (cur_oi_usd / max(cur_vol_usd, 1.0)) if cur_vol_usd > 0 else 0.0

        # Funding & Whale L/S
        cur_funding = float(cur_row['funding_rate']) if pd.notna(cur_row.get('funding_rate')) else 0.0
        min_funding_24h = float(w24['funding_rate'].min()) if pd.notna(w24['funding_rate'].min()) else cur_funding

        cur_whale_ls = float(cur_row['count_toptrader_long_short_ratio']) if pd.notna(cur_row.get('count_toptrader_long_short_ratio')) else np.nan
        min_whale_ls_24h = float(w24['count_toptrader_long_short_ratio'].min()) if pd.notna(w24['count_toptrader_long_short_ratio'].min()) else cur_whale_ls
        whale_ls_rebound = (cur_whale_ls - min_whale_ls_24h) if (pd.notna(cur_whale_ls) and pd.notna(min_whale_ls_24h)) else 0.0

        # Asset-Specific Quantile for Whale L/S Floor
        valid_hist_ls = df['count_toptrader_long_short_ratio'].dropna().tail(2160)
        pct_min_whale_ls = float((valid_hist_ls < min_whale_ls_24h).mean() * 100.0) if (len(valid_hist_ls) >= 24 and pd.notna(min_whale_ls_24h)) else np.nan
        pct_cur_whale_ls = float((valid_hist_ls < cur_whale_ls).mean() * 100.0) if (len(valid_hist_ls) >= 24 and pd.notna(cur_whale_ls)) else np.nan

        # =====================================================================
        # 6-SIGNATURE CLIMAX EXIT & EXHAUSTION SCORING ENGINE (0 TO 100 PTS)
        # =====================================================================
        is_extended = (gain_from_72h_low_pct >= 25.0) or (mfe_72h_pct >= 30.0)

        # [Sig 1] Climax Pinbar Upper Wick Rejection (Max 20 pts)
        score_wick = 0
        if cur_upper_wick_pct >= 75.0:
            score_wick = 20
        elif cur_upper_wick_pct >= 55.0:
            score_wick = 14
        elif cur_upper_wick_pct >= 45.0 and vol_shock >= 4.0:
            score_wick = 12
        sig1_alarm = bool(is_extended and cur_upper_wick_pct >= 70.0)

        # [Sig 2] Volume & Trade Count Bearish Divergence (Max 20 pts)
        score_div = 0
        if vol_div_pct <= -60.0 and tc_div_pct <= -50.0:
            score_div = 15
        elif vol_div_pct <= -45.0 or tc_div_pct <= -45.0:
            score_div = 10
        if ticket_ratio < 0.75:
            score_div += 5  # Institutional ticket contraction
        score_div = min(score_div, 20)
        sig2_alarm = bool(is_extended and (vol_div_pct <= -50.0 or tc_div_pct <= -50.0))

        # [Sig 3] Token OI Bearish Divergence & Unwind (Max 20 pts)
        score_oi_div = 0
        if oi_div_pct <= -15.0:
            score_oi_div = 20  # Heavy post-climax unwind
        elif oi_div_pct <= -4.0:
            score_oi_div = 14  # Peak OI divergence (OGN @ $0.0536)
        elif oi_div_pct < -1.5:
            score_oi_div = 6
        sig3_alarm = bool(is_extended and oi_div_pct <= -4.0)

        # [Sig 4] 10x Funding Rate Collapse / Long Euphoria (Max 15 pts)
        score_fund_exit = 0
        if min_funding_24h <= -0.0030 and cur_funding >= -0.0005:
            score_fund_exit = 15  # 10x negative carry collapse (OGN -0.89% -> -0.037%)
        elif min_funding_24h <= -0.0010 and cur_funding >= -0.0001:
            score_fund_exit = 10
        elif cur_funding >= 0.0005:
            score_fund_exit = 12  # Crowded retail long euphoria (>+0.05% / 8h)
        sig4_alarm = bool(score_fund_exit >= 10)

        # [Sig 5] Taker Buy Breakdown & Velocity Stall (Max 15 pts)
        score_flow_stall = 0
        if cur_taker_ratio < 0.46:
            score_flow_stall = 15
        elif cur_taker_ratio < 0.495 and vol_shock <= 1.25:
            score_flow_stall = 12
        elif cur_taker_ratio < 0.495:
            score_flow_stall = 7
        sig5_alarm = bool(is_extended and score_flow_stall >= 12)

        # [Sig 6] Whale L/S Floor Inflection (Top-Shorts Covering) (Max 10 pts)
        # Dynamic check: Whale L/S touched an asset-specific floor (<= 5th percentile or absolute <= 0.85) and rebounds while OI bleeds
        score_whale_exit = 0
        is_hard_floor = (pd.notna(pct_min_whale_ls) and pct_min_whale_ls <= 5.0) or (pd.notna(min_whale_ls_24h) and min_whale_ls_24h <= 0.85)
        is_mild_floor = (pd.notna(pct_min_whale_ls) and pct_min_whale_ls <= 12.0) or (pd.notna(min_whale_ls_24h) and min_whale_ls_24h <= 1.30)
        if is_hard_floor and whale_ls_rebound >= 0.05 and oi_div_pct <= -4.0:
            score_whale_exit = 10
        elif is_mild_floor and whale_ls_rebound >= 0.12 and oi_div_pct <= -4.0:
            score_whale_exit = 7
        sig6_alarm = bool(score_whale_exit >= 7)

        exit_alarms = [sig1_alarm, sig2_alarm, sig3_alarm, sig4_alarm, sig5_alarm, sig6_alarm]
        alarm_count = sum(1 for x in exit_alarms if x)
        exit_score = score_wick + score_div + score_oi_div + score_fund_exit + score_flow_stall + score_whale_exit

        # Action Decision Classification
        if not is_extended and mfe_72h_pct < 25.0:
            action = "NOT_EXTENDED (BASE / COIL PHASE)"
        elif oi_div_pct <= -15.0 and (whale_ls_rebound >= 0.08 or drawdown_from_72h_high_pct <= -15.0):
            action = "POST_CLIMAX_UNWIND (EXIT_ALL / AVOID_LONGS)"
        elif alarm_count >= 3 or (exit_score >= 55 and is_extended):
            action = "CLIMAX_HARVEST_NOW (TAKE_PROFIT_100%)"
        elif alarm_count == 2 or exit_score >= 38:
            action = "RATCHET_STOP / PARTIAL_TP (CAUTION)"
        else:
            action = "HOLD_STRONG / ADD_DIP (SQUEEZE_FUEL_INTACT)"

        # Trailing Stop Reference Coordinates
        bar1_floor_stop = float(df.iloc[-2]['low']) * 0.985  # -1.5% Cushion below prior bar low
        vwap_24h = float((w24['quote_volume'] * w24['close']).sum() / max(w24['quote_volume'].sum(), 1.0)) if 'quote_volume' in w24 else low_24h

        return {
            'symbol': clean,
            'timestamp': str(cur_row['dt']),
            'current_price': cur_price,
            'ret_1h_pct': ret_1h,
            'ret_24h_pct': ret_24h,
            'mfe_72h_pct': mfe_72h_pct,
            'gain_from_72h_low_pct': gain_from_72h_low_pct,
            'drawdown_from_72h_high_pct': drawdown_from_72h_high_pct,
            'exit_score': exit_score,
            'alarm_count': alarm_count,
            'action': action,
            'upper_wick_pct': cur_upper_wick_pct,
            'vol_1h_usd': cur_vol_usd,
            'vol_shock': vol_shock,
            'vol_div_pct': vol_div_pct,
            'cur_count': cur_count,
            'tc_velocity': tc_velocity,
            'tc_div_pct': tc_div_pct,
            'avg_ticket_usd': avg_ticket_usd,
            'med_ticket_24h_usd': med_ticket_24h_usd,
            'taker_buy_pct': cur_taker_ratio * 100.0,
            'oi_usd': cur_oi_usd,
            'oi_tokens': cur_oi_tokens,
            'peak_oi_tokens_24h': peak_oi_tokens_24h,
            'oi_div_pct': oi_div_pct,
            'air_pocket_ratio': air_pocket_ratio,
            'funding_rate': cur_funding,
            'min_funding_24h': min_funding_24h,
            'whale_ls': cur_whale_ls,
            'min_whale_ls_24h': min_whale_ls_24h,
            'pct_whale_ls': pct_cur_whale_ls,
            'pct_min_whale_ls': pct_min_whale_ls,
            'whale_ls_rebound': whale_ls_rebound,
            'bar1_cushion_stop': bar1_floor_stop,
            'vwap_24h': vwap_24h,
            'sep25_low': sep25_low,
            'nov25_low': nov25_low,
            'sep25_high_diff_pct': sep25_high_diff_pct,
            'sep25_cur_upside_pct': sep25_cur_upside_pct,
            'nov25_cur_upside_pct': nov25_cur_upside_pct,
            'candidate_tier': candidate_tier,
            'ema200_1h': ema200_1h,
            'ema200_4h': ema200_4h,
            'ema200_1d': ema200_1d,
            'sma200_1d': sma200_1d,
            'price_vs_ema200_1d_pct': price_vs_ema200_1d_pct,
            'ema_1h_vs_1d_gap_pct': ema_1h_vs_1d_gap_pct,
            'alarms': {
                'sig1_wick': sig1_alarm,
                'sig2_vol_tc_div': sig2_alarm,
                'sig3_oi_div': sig3_alarm,
                'sig4_fund_collapse': sig4_alarm,
                'sig5_taker_stall': sig5_alarm,
                'sig6_whale_inflection': sig6_alarm
            },
            'scores': {
                'wick': score_wick,
                'div': score_div,
                'oi_div': score_oi_div,
                'fund': score_fund_exit,
                'flow': score_flow_stall,
                'whale': score_whale_exit
            }
        }, None

    except Exception as e:
        return None, f"Exit analysis error on {sym}: {e}"


def print_exit_tear_sheet(r):
    a = r['alarms']
    s = r['scores']
    print("=" * 108)
    print(f"  KRONOS 6-SIGNATURE CLIMAX EXIT & POSITION HOLD TEAR SHEET: {r['symbol']}/USDT")
    print(f"  AS-OF: {r['timestamp']} | EXIT URGENCY SCORE: {r['exit_score']}/100 | ALARMS: {r['alarm_count']}/6 | TIER: [{r.get('candidate_tier','N/A')}]")
    print(f"  TACTICAL DECISION: >> {r['action']} <<")
    print("=" * 108)
    print(f"\n  [1] EXTENSION, 200-EMA CONVERGENCE, MACRO BREAKDOWN MAGNETS & TRAILING STOPS:")
    print(f"      • Current Price:         ${r['current_price']:.5f} (1h: {r['ret_1h_pct']:+.2f}% | 24h: {r['ret_24h_pct']:+.2f}%)")
    print(f"      • 72h Run Extension:     +{r['gain_from_72h_low_pct']:.1f}% from 72h Low (72h Peak Drawdown: {r['drawdown_from_72h_high_pct']:+.1f}%)")
    print(f"      • 200-EMA Convergence:   1h: ${r.get('ema200_1h',0):.5f} | 4h: ${r.get('ema200_4h',0):.5f} | 1D EMA200: ${r.get('ema200_1d',0):.5f} ({r.get('price_vs_ema200_1d_pct',0):+.1f}%) | 1D SMA200: ${r.get('sma200_1d',0):.5f}")
    if pd.notna(r.get('sep25_low')):
        s25_tag = " [EXACT SEP-2025 MAGNET HIT!]" if abs(r['sep25_high_diff_pct']) <= 6.0 else ""
        n25_str = f" | Nov 2025 Gateway: ${r['nov25_low']:.5f} ({r['nov25_cur_upside_pct']:+.1f}%)" if pd.notna(r.get('nov25_low')) else ""
        print(f"      • Macro Breakdown Zone:  Sep 2025 Low: ${r['sep25_low']:.5f} (72h High vs Sep25: {r['sep25_high_diff_pct']:+.1f}%{s25_tag}){n25_str}")
    print(f"      • -1.5% Cushion Stop:    ${r['bar1_cushion_stop']:.5f} | 24h Dynamic VWAP Floor: ${r['vwap_24h']:.5f}")
    print(f"      • Air-Pocket Fragility:  {r['air_pocket_ratio']:.2f}x (OI/1h Vol — {'[HIGH WATERFALL RISK >=3x]' if r['air_pocket_ratio'] >= 3.0 else '[LIQUID BOOK <3x]'})")

    print(f"\n  [2] THE 6 CLIMAX EXIT SIGNATURES (Breakdown: {r['exit_score']}/100):")
    print(f"      • [Sig 1] Climax Pinbar Wick ({s['wick']:>2}/20):   {'[ALARM]' if a['sig1_wick'] else '[CLEAR]'}  1h Upper Wick = {r['upper_wick_pct']:.1f}% (Threshold: >=70%)")
    print(f"      • [Sig 2] Vol & Trade Cnt Div ({s['div']:>2}/20):  {'[ALARM]' if a['sig2_vol_tc_div'] else '[CLEAR]'}  Vol Div: {r['vol_div_pct']:+.1f}% | Trade Cnt Div: {r['tc_div_pct']:+.1f}% | Ticket: ${r['avg_ticket_usd']:,.1f} (Med: ${r['med_ticket_24h_usd']:,.1f})")
    print(f"      • [Sig 3] Token OI Divergence ({s['oi_div']:>2}/20):  {'[ALARM]' if a['sig3_oi_div'] else '[CLEAR]'}  Token OI: {r['oi_tokens']:,.0f} vs 24h Peak {r['peak_oi_tokens_24h']:,.0f} ({r['oi_div_pct']:+.1f}%)")
    print(f"      • [Sig 4] Funding Snap/Euph   ({s['fund']:>2}/15):  {'[ALARM]' if a['sig4_fund_collapse'] else '[CLEAR]'}  24h Min: {r['min_funding_24h']*100:+.4f}% -> Current: {r['funding_rate']*100:+.4f}%")
    print(f"      • [Sig 5] Taker/Vol Stall     ({s['flow']:>2}/15):  {'[ALARM]' if a['sig5_taker_stall'] else '[CLEAR]'}  Taker Buy: {r['taker_buy_pct']:.1f}% | Vol Shock: {r['vol_shock']:.1f}x | Trade Vel: {r['tc_velocity']:.1f}x")
    wls_str = f"{r['whale_ls']:.2f}" if pd.notna(r['whale_ls']) else "N/A"
    min_wls_str = f"{r['min_whale_ls_24h']:.2f}" if pd.notna(r['min_whale_ls_24h']) else "N/A"
    pct_info = f" [Floor P{r['pct_min_whale_ls']:.1f}% -> Now P{r['pct_whale_ls']:.1f}%]" if pd.notna(r.get('pct_min_whale_ls')) else ""
    print(f"      • [Sig 6] Whale L/S Rebound   ({s['whale']:>2}/10):  {'[ALARM]' if a['sig6_whale_inflection'] else '[CLEAR]'}  24h Floor: {min_wls_str} -> Current: {wls_str}{pct_info} (Rebound: {r['whale_ls_rebound']:+.2f})")
    print("=" * 108 + "\n")


def print_exit_table(results, title="LIVE RUNNER EXIT & HOLD MATRIX"):
    if not results:
        print("\n[INFO] No active runners matched the criteria.\n")
        return

    print("=" * 158)
    print(f"  {title}")
    print("=" * 158)
    print(f"{'Symbol':<8} | {'Tier':<7} | {'vs 1D EMA':<9} | {'ExitScore':<9} | {'Alarms':<6} | {'Tactical Decision':<43} | {'24h Ret':<8} | {'OI vs Peak':<10} | {'Whale L/S':<12} | {'Funding':<9}")
    print("-" * 158)
    for r in results[:30]:
        wls_s = f"{r['whale_ls']:.2f} ({r['whale_ls_rebound']:+.2f})" if pd.notna(r['whale_ls']) else "N/A"
        tier_s = r.get('candidate_tier', 'N/A')
        vs_1d = f"{r.get('price_vs_ema200_1d_pct', 0.0):>+7.1f}%"
        print(
            f"{r['symbol']:<8} | {tier_s:<7} | {vs_1d:<9} | {r['exit_score']:>4}/100  | {r['alarm_count']}/6    | "
            f"{r['action']:<43} | {r['ret_24h_pct']:>+6.1f}% | "
            f"{r['oi_div_pct']:>+8.1f}%  | {wls_s:<12} | {r['funding_rate']*100:>+7.3f}%"
        )
    print("=" * 158 + "\n")


def main():
    parser = argparse.ArgumentParser(description="Kronos 6-Signature Climax Exit & Position Hold Scanner")
    parser.add_argument("--symbol", type=str, help="Single symbol to evaluate for Exit vs Hold (e.g. ERA, MAGIC, OGN)")
    parser.add_argument("--watchlist", type=str, help="Comma-separated list of active tickers (e.g. 'ERA,MAGIC,CTSI,OGN,C98')")
    parser.add_argument("--scan", action="store_true", help="Scan all active runners in universe (72h MFE >= 25% or 24h Ret >= 10%)")
    parser.add_argument("--as-of", type=str, default=None, help="Historical point-in-time timestamp")
    parser.add_argument("--json", action="store_true", help="JSON output")
    args = parser.parse_args()

    if args.symbol:
        res, err = evaluate_exit_signature(args.symbol, as_of=args.as_of)
        if err:
            print(f"[ERROR] {err}")
            return
        if args.json:
            print(json.dumps(res, indent=2))
        else:
            print_exit_tear_sheet(res)
    elif args.watchlist:
        syms = [s.strip() for s in args.watchlist.split(",") if s.strip()]
        results = []
        for s in syms:
            res, err = evaluate_exit_signature(s, as_of=args.as_of)
            if res:
                results.append(res)
        results.sort(key=lambda x: x['exit_score'], reverse=True)
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print_exit_table(results, title=f"WATCHLIST EXIT & HOLD MATRIX (AS-OF: {args.as_of or 'LATEST'})")
    elif args.scan:
        raw_files = glob.glob("data/raw_shards/*_USDT_1h.parquet")
        if not raw_files:
            raw_files = glob.glob("data/raw_shards/*_1h.parquet")
        symbols = [os.path.basename(f).split('_')[0] for f in raw_files]
        results = []
        print(f"\n[EXIT SCANNER] Auditing {len(symbols)} shards for extended runners & climax exits...\n")
        for s in symbols:
            res, err = evaluate_exit_signature(s, as_of=args.as_of)
            if res and (res['gain_from_72h_low_pct'] >= 20.0 or res['ret_24h_pct'] >= 10.0) and res['oi_usd'] >= 1.0e6:
                results.append(res)
        results.sort(key=lambda x: x['exit_score'], reverse=True)
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print_exit_table(results, title="UNIVERSE ACTIVE RUNNERS: CLIMAX EXIT VS. HOLD MATRIX")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
