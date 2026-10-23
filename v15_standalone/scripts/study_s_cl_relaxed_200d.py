"""
Study S-CL: Clean-Room Evaluation of Relaxed 200-Day EMA Dormancy & Direct Breakout in Micro-Caps (Book 7)
Rule 7 & Clean-Room Sovereign Protocol Certified (.agents/AGENTS.md & .agents/KNOWLEDGE.md)
Multi-Core Parallel Architecture (10 Worker Processes) with Real-Time Shard Progress Streaming.

Hypothesis: In Tier 3 micro-caps, market cycles move 3x faster than in large-caps. A 30-day (720 bars)
pre-dormancy requirement blinds the system to secondary Wave 2 supernovas (like JCT Oct 20).
Testing relaxed dormancy (10d, 7d) and Direct Breakout Ignition under extreme Whale Conviction (z_ls <= -1.50).

Models Evaluated across all 384 Tier 3 Shards:
- Model 0: Baseline V15.1 (min_bars_below = 720 / 30 days, Retest Required)
- Model 1: Relaxed Dormancy 10 Days (min_bars_below = 240 / 10 days, Retest Required)
- Model 2: Relaxed Dormancy 7 Days (min_bars_below = 168 / 7 days, Retest Required)
- Model 3: 7-Day Dormancy + Direct Breakout Ignition (min_bars_below = 168, direct_breakout if z_ls <= -1.50)
- Model 4: 7-Day Dormancy + Direct Breakout + Extended Ceiling (max_dist_200d = 0.20)
"""

import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import time
import numpy as np
import pandas as pd
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import Dict, List, Tuple
from momentum_v15.config import V12Config, Book7Config
from momentum_v15.features_v12 import load_shard, compute_features_v12, get_btc_macro
from momentum_v15.engine_v12 import run_v12_engine
from momentum_v15.tier_classifier import get_all_universe_tiers

def format_eta(seconds: float) -> str:
    if seconds < 60:
        return f"{seconds:.0f}s"
    elif seconds < 3600:
        mins = int(seconds // 60)
        secs = int(seconds % 60)
        return f"{mins}m {secs}s"
    else:
        hrs = int(seconds // 3600)
        mins = int((seconds % 3600) // 60)
        return f"{hrs}h {mins}m"

def process_single_shard(args):
    sym, raw_dir_str, exotic_dir_str, btc_df = args
    raw_dir = Path(raw_dir_str)
    exotic_dir = Path(exotic_dir_str)
    cfg_base = V12Config()
    
    models = {
        "Model 0": Book7Config(
            enable_book7=True,
            enable_studentized_carry=True,
            max_z_funding=0.25,
            min_bars_below=720,
            max_dist_200d=0.12,
            enable_direct_breakout=False,
        ),
        "Model 1": Book7Config(
            enable_book7=True,
            enable_studentized_carry=True,
            max_z_funding=0.25,
            min_bars_below=240, # 10 days
            max_dist_200d=0.12,
            enable_direct_breakout=False,
        ),
        "Model 2": Book7Config(
            enable_book7=True,
            enable_studentized_carry=True,
            max_z_funding=0.25,
            min_bars_below=168, # 7 days
            max_dist_200d=0.12,
            enable_direct_breakout=False,
        ),
        "Model 3": Book7Config(
            enable_book7=True,
            enable_studentized_carry=True,
            max_z_funding=0.25,
            min_bars_below=168, # 7 days
            max_dist_200d=0.12,
            enable_direct_breakout=True,
            direct_breakout_max_z_ls=-1.50,
        ),
        "Model 4": Book7Config(
            enable_book7=True,
            enable_studentized_carry=True,
            max_z_funding=0.25,
            min_bars_below=168, # 7 days
            max_dist_200d=0.20, # +20% ceiling
            enable_direct_breakout=True,
            direct_breakout_max_z_ls=-1.50,
        )
    }

    shard_df = load_shard(sym, raw_dir, exotic_dir)
    if shard_df is None or shard_df.empty:
        return sym, {}
        
    f_df = compute_features_v12(shard_df, btc_df, tier_label="Tier 3", cfg=cfg_base)
    if f_df.empty:
        return sym, {}

    shard_results = {}
    for m_name, b7_cfg in models.items():
        cfg_variant = V12Config(book7=b7_cfg)
        trades_df = run_v12_engine(f_df, sym, cfg=cfg_variant)
        if not trades_df.empty:
            b7_t = trades_df[trades_df['book'] == 'Book 7']
            shard_results[m_name] = b7_t
        else:
            shard_results[m_name] = pd.DataFrame()

    return sym, shard_results

def run_study_s_cl():
    t_start = time.time()
    print("=" * 85, flush=True)
    print("  STUDY S-CL: RELAXED 200d EMA DORMANCY & DIRECT BREAKOUT ENGINE (TIER 3 MICRO-CAPS)", flush=True)
    print("  Universe: All 384 Tier 3 Micro-Cap Shards | 10 Parallel Worker Cores", flush=True)
    print("=" * 85 + "\n", flush=True)

    t1, t2, t3, _ = get_all_universe_tiers()
    raw_dir = Path("data/raw_shards")
    exotic_dir = Path("data/exotic_shards")
    btc_df = get_btc_macro(raw_dir=raw_dir)
    
    tier3_symbols = [s for s in t3 if (raw_dir / f"{s}_USDT_1h.parquet").exists() or (raw_dir / f"1000{s}_USDT_1h.parquet").exists()]
    total_shards = len(tier3_symbols)
    print(f"Total Active Tier 3 Shards on Disk: {total_shards}", flush=True)
    print("Launching 10 Parallel Workers to compute features & evaluate all 5 models...\n", flush=True)

    tasks_args = [(sym, str(raw_dir), str(exotic_dir), btc_df) for sym in tier3_symbols]

    all_model_trades = {
        "Model 0": [],
        "Model 1": [],
        "Model 2": [],
        "Model 3": [],
        "Model 4": []
    }
    
    jct_results = {}
    dood_results = {}

    completed = 0
    with ProcessPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(process_single_shard, arg): arg[0] for arg in tasks_args}
        
        for future in as_completed(futures):
            sym = futures[future]
            try:
                ret_sym, shard_res = future.result()
                completed += 1
                
                n_m0 = len(shard_res.get("Model 0", []))
                n_m1 = len(shard_res.get("Model 1", []))
                n_m2 = len(shard_res.get("Model 2", []))
                n_m3 = len(shard_res.get("Model 3", []))
                n_m4 = len(shard_res.get("Model 4", []))
                
                for m_key in ["Model 0", "Model 1", "Model 2", "Model 3", "Model 4"]:
                    df_t = shard_res.get(m_key)
                    if df_t is not None and not df_t.empty:
                        all_model_trades[m_key].append(df_t)
                        if sym == "JCT":
                            jct_results.setdefault(m_key, []).append(df_t)
                        elif sym == "DOOD":
                            dood_results.setdefault(m_key, []).append(df_t)

                elapsed = time.time() - t_start
                rate = completed / elapsed if elapsed > 0 else 1.0
                eta = (total_shards - completed) / rate
                pct = (completed / total_shards) * 100.0

                print(f"  [{completed:3d}/{total_shards}] ({pct:5.1f}%) | Shard: {sym:12s} | B7: [M0:{n_m0} M1:{n_m1} M2:{n_m2} M3:{n_m3} M4:{n_m4}] | Elapsed: {format_eta(elapsed)} | ETA: {format_eta(eta)}", flush=True)

            except Exception as e:
                print(f"  [ERROR] Shard {sym} failed: {e}", flush=True)

    t_total = time.time() - t_start
    print("\n" + "=" * 85, flush=True)
    print(f"  STUDY S-CL COMPLETED ACROSS 384 SHARDS IN {format_eta(t_total)}", flush=True)
    print("=" * 85 + "\n", flush=True)

    model_labels = {
        "Model 0": "Model 0 (Baseline V15.1: 30d Dormancy, Retest Req)",
        "Model 1": "Model 1 (10d Dormancy / 240 bars, Retest Req)",
        "Model 2": "Model 2 (7d Dormancy / 168 bars, Retest Req)",
        "Model 3": "Model 3 (7d Dormancy + Direct Breakout if z_ls<=-1.50)",
        "Model 4": "Model 4 (7d Dormancy + Direct Breakout + +20% Ceiling)"
    }

    summary_rows = []
    for m_key in ["Model 0", "Model 1", "Model 2", "Model 3", "Model 4"]:
        t_list = all_model_trades[m_key]
        if t_list:
            all_t = pd.concat(t_list, ignore_index=True)
            # Filter to closed trades for win rate and profit factor
            is_open_bool = all_t['is_open'].fillna(False).astype(bool) if 'is_open' in all_t.columns else pd.Series(False, index=all_t.index)
            closed_t = all_t[~is_open_bool]
            n_closed = len(closed_t)
            n_tot = len(all_t)
            wr = (closed_t['pnl'] > 0).mean() * 100.0 if n_closed > 0 else 0.0
            net_log = all_t['log_ret'].sum() * 100.0
            mean_mfe = all_t['mfe'].mean() * 100.0 if 'mfe' in all_t.columns else 0.0
            gains = closed_t.loc[closed_t['log_ret'] > 0, 'log_ret'].sum()
            losses = abs(closed_t.loc[closed_t['log_ret'] < 0, 'log_ret'].sum())
            pf = gains / losses if losses > 0 else np.nan
        else:
            n_tot, n_closed, wr, net_log, mean_mfe, pf = 0, 0, 0.0, 0.0, 0.0, 0.0
            
        n_jct = sum(len(x) for x in jct_results.get(m_key, []))
        n_dood = sum(len(x) for x in dood_results.get(m_key, []))

        summary_rows.append({
            "model_name": model_labels[m_key],
            "n_total": n_tot,
            "n_closed": n_closed,
            "win_rate": wr,
            "profit_factor": pf,
            "net_log": net_log,
            "mean_mfe": mean_mfe,
            "jct_count": n_jct,
            "dood_count": n_dood
        })

    print(f"{'Dormancy & Breakout Model':<55} | {'Trades':<7} | {'Win Rate':<9} | {'Log PF':<8} | {'Net Log':<10} | {'Mean MFE':<9} | {'JCT':<5} | {'DOOD':<5}")
    print("-" * 120)
    for r in summary_rows:
        print(f"{r['model_name']:<55} | {r['n_closed']:<7d} | {r['win_rate']:<8.2f}% | {r['profit_factor']:<8.3f} | {r['net_log']:<+9.1f}% | {r['mean_mfe']:<8.1f}% | {r['jct_count']:<5d} | {r['dood_count']:<5d}")
    print("-" * 120)

    print("\n>>> FORENSIC JCT TRADES PER MODEL:")
    for m_key in ["Model 0", "Model 1", "Model 2", "Model 3", "Model 4"]:
        t_list = jct_results.get(m_key, [])
        print(f"\n[{m_key} - {model_labels[m_key]}]:")
        if t_list:
            j_df = pd.concat(t_list, ignore_index=True)
            for _, tr in j_df.iterrows():
                print(f"  Entry: {tr['entry']} @ {tr['entry_price']:.6f} -> Exit: {tr['exit']} @ {tr['exit_price']:.6f} | PnL: {tr['pnl']*100:+.2f}% | Log: {tr['log_ret']*100:+.2f}% | MFE: {tr['mfe']*100:.1f}% | Reason: {tr['reason']}")
        else:
            print("  No JCT trades")

    return summary_rows

if __name__ == "__main__":
    run_study_s_cl()
