"""
Study S-CK: Clean-Room Microstructure-Conditioned Dynamic Exit & Peak Harvest Engine
Rule 7 & Clean-Room Sovereign Protocol Certified (.agents/AGENTS.md & .agents/KNOWLEDGE.md)

Evaluates whether conditioning Book 7 stop ratchets on bar acceptance quality
(Air-Pocket Stall vs Clean Structural Continuation) and adding tactical climax harvesting
allows micro-cap runners to capture peak supernovas without degrading portfolio win rate.

Models Tested across all 393 Tier 3 Shards:
- Model 0: Baseline V15.0 + S-CJ Studentized Carry (Static -0.5% BE Cushion, 72h Donchian)
- Model 1: Microstructure-Conditioned Cushion (-0.5% if Wick >= 40%, -3.0% if Wick < 40%)
- Model 2: Microstructure-Conditioned Cushion + Climax Runner Harvest (Urgency >= 55)
- Model 3: Preserved Structural Floor for Clean Runners (Initial Stop if Wick < 40%)
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

def run_study_s_ck():
    t_start = time.time()
    print("=" * 80, flush=True)
    print("  STUDY S-CK: MICROSTRUCTURE-CONDITIONED DYNAMIC EXIT & PEAK HARVEST ENGINE", flush=True)
    print("  Universe: All Available Tier 3 Micro-Cap Shards | Clean-Room Single-Kernel", flush=True)
    print("=" * 80 + "\n", flush=True)

    t1, t2, t3, _ = get_all_universe_tiers()
    raw_dir = Path("data/raw_shards")
    exotic_dir = Path("data/exotic_shards")
    btc_df = get_btc_macro(raw_dir=raw_dir)
    
    tier3_symbols = [s for s in t3 if (raw_dir / f"{s}_USDT_1h.parquet").exists() or (raw_dir / f"1000{s}_USDT_1h.parquet").exists()]
    total_shards = len(tier3_symbols)
    print(f"Total Active Tier 3 Shards on Disk: {total_shards}", flush=True)
    
    # Stage 1: Pre-compute and cache features with real-time progress logging
    print("\n>>> Stage 1: Pre-computing and Caching Features across Tier 3 Shards...", flush=True)
    feature_cache = {}
    cfg_base = V12Config()
    t_feat_start = time.time()
    
    for i, sym in enumerate(tier3_symbols, 1):
        t0 = time.time()
        shard_df = load_shard(sym, raw_dir, exotic_dir)
        if shard_df is not None and not shard_df.empty:
            f_df = compute_features_v12(shard_df, btc_df, tier_label="Tier 3", cfg=cfg_base)
            feature_cache[sym] = f_df
        
        elapsed = time.time() - t_feat_start
        rate = i / elapsed if elapsed > 0 else 1.0
        eta = (total_shards - i) / rate
        
        if i % 10 == 0 or i == total_shards:
            pct = (i / total_shards) * 100.0
            print(f"  [Features: {i:3d}/{total_shards}] ({pct:5.1f}%) | Cached: {sym:12s} | Elapsed: {format_eta(elapsed)} | ETA: {format_eta(eta)}", flush=True)

    cached_shards = len(feature_cache)
    print(f"\nSuccessfully cached {cached_shards} Tier 3 feature frames in {format_eta(time.time() - t_feat_start)}.\n", flush=True)
    
    # 4 Exit Architecture Models
    # Base Book 7 configuration uses Promoted Model 1 from Study S-CJ (Studentized Carry z_fnd <= +0.25s)
    models = {
        "Model 0 (Baseline V15.0 - Static -0.5% BE Cushion)": Book7Config(
            enable_book7=True,
            require_negative_carry=True,
            max_funding_rate=0.0,
            enable_studentized_carry=True,
            max_z_funding=0.25,
            enable_microstructure_conditioned_exit=False,
            enable_climax_runner_harvest=False,
        ),
        "Model 1 (Microstructure-Conditioned -3.0% Cushion)": Book7Config(
            enable_book7=True,
            require_negative_carry=True,
            max_funding_rate=0.0,
            enable_studentized_carry=True,
            max_z_funding=0.25,
            enable_microstructure_conditioned_exit=True,
            stall_wick_threshold=0.40,
            breakeven_cushion_pct=0.005,
            runner_cushion_pct=0.030,
            enable_climax_runner_harvest=False,
        ),
        "Model 2 (Conditioned Cushion + Climax Top Harvest)": Book7Config(
            enable_book7=True,
            require_negative_carry=True,
            max_funding_rate=0.0,
            enable_studentized_carry=True,
            max_z_funding=0.25,
            enable_microstructure_conditioned_exit=True,
            stall_wick_threshold=0.40,
            breakeven_cushion_pct=0.005,
            runner_cushion_pct=0.030,
            enable_climax_runner_harvest=True,
            climax_min_mfe=0.20,
            climax_harvest_urgency=55.0,
        ),
        "Model 3 (Preserved Structural Stop for Clean Runners)": Book7Config(
            enable_book7=True,
            require_negative_carry=True,
            max_funding_rate=0.0,
            enable_studentized_carry=True,
            max_z_funding=0.25,
            enable_microstructure_conditioned_exit=True,
            stall_wick_threshold=0.40,
            breakeven_cushion_pct=0.005,
            runner_cushion_pct=0.080, # Wide 8% structural breathing room
            enable_climax_runner_harvest=True,
            climax_min_mfe=0.20,
            climax_harvest_urgency=55.0,
        )
    }

    results = {}
    
    # Stage 2: Simulation Loop across Models with granular progress logging
    print(">>> Stage 2: Running Clean-Room Simulations across Exit Models...", flush=True)
    
    for m_idx, (m_name, b7_cfg) in enumerate(models.items(), 1):
        print(f"\n" + "-" * 75, flush=True)
        print(f"  [Model {m_idx}/4] Simulating: {m_name}", flush=True)
        print("-" * 75, flush=True)
        
        cfg_variant = V12Config(book7=b7_cfg)
        b7_trades_list = []
        jct_trades = []
        dood_trades = []
        
        t_model_start = time.time()
        
        for i, (sym, feat_df) in enumerate(feature_cache.items(), 1):
            trades_df = run_v12_engine(feat_df, sym, cfg=cfg_variant)
            if not trades_df.empty:
                b7_t = trades_df[trades_df['book'] == 'Book 7']
                if not b7_t.empty:
                    b7_trades_list.append(b7_t)
                    if sym == "JCT":
                        jct_trades.append(b7_t)
                    elif sym == "DOOD":
                        dood_trades.append(b7_t)
            
            elapsed = time.time() - t_model_start
            rate = i / elapsed if elapsed > 0 else 1.0
            eta = (cached_shards - i) / rate
            
            if i % 25 == 0 or i == cached_shards:
                pct = (i / cached_shards) * 100.0
                curr_b7_count = sum(len(x) for x in b7_trades_list)
                print(f"    [{i:3d}/{cached_shards}] ({pct:5.1f}%) | Shard: {sym:12s} | B7 Trades So Far: {curr_b7_count:3d} | Elapsed: {format_eta(elapsed)} | ETA: {format_eta(eta)}", flush=True)

        if b7_trades_list:
            all_b7 = pd.concat(b7_trades_list, ignore_index=True)
            n_trades = len(all_b7)
            wr = (all_b7['pnl'] > 0).mean() * 100.0
            net_log = all_b7['log_ret'].sum() * 100.0
            mean_mfe = all_b7['mfe'].mean() * 100.0 if 'mfe' in all_b7.columns else 0.0
            
            # Profit Factor
            gains = all_b7.loc[all_b7['log_ret'] > 0, 'log_ret'].sum()
            losses = abs(all_b7.loc[all_b7['log_ret'] < 0, 'log_ret'].sum())
            pf = gains / losses if losses > 0 else np.nan
        else:
            all_b7 = pd.DataFrame()
            n_trades = 0
            wr = 0.0
            net_log = 0.0
            mean_mfe = 0.0
            pf = 0.0

        jct_count = sum(len(x) for x in jct_trades)
        dood_count = sum(len(x) for x in dood_trades)
        
        jct_summary = []
        if jct_trades:
            j_df = pd.concat(jct_trades, ignore_index=True)
            for _, r in j_df.iterrows():
                jct_summary.append(f"Entry {r['entry']} -> Exit {r['exit']} | PnL: {r['pnl']*100:+.2f}% | Log: {r['log_ret']*100:+.2f}% | MFE: {r['mfe']*100:.1f}% | Reason: {r['reason']}")

        results[m_name] = {
            "n_trades": n_trades,
            "win_rate": wr,
            "net_log": net_log,
            "profit_factor": pf,
            "mean_mfe": mean_mfe,
            "jct_trades": jct_count,
            "dood_trades": dood_count,
            "jct_details": jct_summary,
            "trades_df": all_b7
        }
        
        print(f"\n  >>> Model Summary: {n_trades} trades | Win Rate: {wr:.2f}% | Log PF: {pf:.3f} | Net Log: {net_log:+.1f}% | Mean MFE: {mean_mfe:.1f}% | JCT: {jct_count} | DOOD: {dood_count}", flush=True)
        if jct_summary:
            for s in jct_summary:
                print(f"      JCT: {s}", flush=True)

    t_total = time.time() - t_start
    print("\n" + "=" * 80, flush=True)
    print(f"  STUDY S-CK COMPLETED IN {format_eta(t_total)}", flush=True)
    print("=" * 80, flush=True)

    # Print Comparative Matrix
    print("\n### FINAL COMPARATIVE PERFORMANCE MATRIX (STUDY S-CK)\n")
    print(f"{'Exit Architecture Model':<50} | {'Trades':<7} | {'Win Rate':<9} | {'Log PF':<8} | {'Net Log':<10} | {'Mean MFE':<9} | {'JCT':<5} | {'DOOD':<5}")
    print("-" * 115)
    for m_name, res in results.items():
        print(f"{m_name:<50} | {res['n_trades']:<7d} | {res['win_rate']:<8.2f}% | {res['profit_factor']:<8.3f} | {res['net_log']:<+9.1f}% | {res['mean_mfe']:<8.1f}% | {res['jct_trades']:<5d} | {res['dood_trades']:<5d}")
    print("-" * 115)

    return results

if __name__ == "__main__":
    run_study_s_ck()
