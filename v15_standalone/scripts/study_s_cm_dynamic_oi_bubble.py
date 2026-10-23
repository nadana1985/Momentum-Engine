"""
Study S-CM: Clean-Room Evaluation of Dynamic Studentized vs. Empirical Percentile Orderflow Bubble Gate for Micro-Caps (Book 7)
Sovereign Rule 1, 2, 3 & 7 (The Dynamic Heuristic Law) Certified (.agents/AGENTS.md & .agents/KNOWLEDGE.md)
Multi-Core Parallel Architecture (10 Worker Processes) with Real-Time Shard Progress Streaming.

Hypothesis: In Tier 3 micro-caps, the legacy static leverage bubble firewall (max_d_oi_tokens = 0.35 / +35%)
is an arbitrary static constant that causes false-positive vetoes on high-beta coins with naturally volatile orderflow
(like GTC), while potentially failing to detect subtle retail leverage buildups on low-turnover coins.
Normalizing orderflow expansion dynamically via:
  - Model B: Studentized 12h orderflow z-score (z_oi_12h <= +2.00 sigma)
  - Model B2: Relaxed studentized 12h orderflow z-score (z_oi_12h <= +2.50 sigma)
  - Model C: 30-day empirical percentile of 24h token OI expansion (pct_doi_30d <= 90%)
  - Model C2: Relaxed 30-day empirical percentile (pct_doi_30d <= 95%)
eliminates arbitrary constants, satisfies Sovereign Rule 7, and tests whether dynamic orderflow gates expand alpha.

Models Evaluated across all 384 Tier 3 Shards:
- Model A: Baseline V15.2 (Static max_d_oi_tokens = 0.35)
- Model B: Dynamic Studentized (z_oi_12h <= +2.00 sigma)
- Model B2: Dynamic Studentized Relaxed (z_oi_12h <= +2.50 sigma)
- Model C: Dynamic Percentile (pct_doi_30d <= 90%)
- Model C2: Dynamic Percentile Relaxed (pct_doi_30d <= 95%)
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
from dataclasses import replace
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
    
    # Common V15.2 promoted foundation
    common_b7 = dict(
        enable_book7=True,
        enable_studentized_carry=True,
        max_z_funding=0.25,
        min_bars_below=168,
        max_dist_200d=0.20,
        enable_direct_breakout=True,
        direct_breakout_max_z_ls=-1.50,
    )
    
    models = {
        "Model A": Book7Config(
            **common_b7,
            enable_studentized_oi_bubble=False,
            enable_percentile_oi_bubble=False,
            max_d_oi_tokens=0.35, # Baseline V15.2 static constant
        ),
        "Model B": Book7Config(
            **common_b7,
            enable_studentized_oi_bubble=True,
            max_z_oi=2.00, # Studentized z_oi_12h <= +2.00 sigma
            enable_percentile_oi_bubble=False,
        ),
        "Model B2": Book7Config(
            **common_b7,
            enable_studentized_oi_bubble=True,
            max_z_oi=2.50, # Studentized z_oi_12h <= +2.50 sigma
            enable_percentile_oi_bubble=False,
        ),
        "Model C": Book7Config(
            **common_b7,
            enable_studentized_oi_bubble=False,
            enable_percentile_oi_bubble=True,
            max_pct_oi=90.0, # Empirical 30d percentile <= 90%
        ),
        "Model C2": Book7Config(
            **common_b7,
            enable_studentized_oi_bubble=False,
            enable_percentile_oi_bubble=True,
            max_pct_oi=95.0, # Empirical 30d percentile <= 95%
        )
    }

    try:
        shard = load_shard(sym, raw_dir=raw_dir, exotic_dir=exotic_dir)
        if shard is None or len(shard) < 720:
            return sym, {}

        # Compute features once per shard
        feat = compute_features_v12(shard, btc_df, tier_label="Tier 3", cfg=cfg_base)

        results = {}
        for m_name, b7_cfg in models.items():
            cfg_variant = replace(cfg_base, book7=b7_cfg)
            # Run engine causally
            trades_df = run_v12_engine(feat, sym, cfg=cfg_variant)
            if trades_df is not None and not trades_df.empty:
                b7_trades = trades_df[trades_df['book'] == 'Book 7'].copy()
                results[m_name] = b7_trades
            else:
                results[m_name] = pd.DataFrame()

        return sym, results
    except Exception as e:
        return sym, {"error": str(e)}

def run_study_s_cm():
    t_start = time.time()
    print("=" * 95, flush=True)
    print("  STUDY S-CM: CLEAN-ROOM EVALUATION OF DYNAMIC VS STATIC ORDERFLOW BUBBLE FIREWALL (BOOK 7)", flush=True)
    print("  Sovereign Rule 1, 2, 3 & 7 Certified | Universe: All 384 Tier 3 Shards | 10 Parallel Worker Cores", flush=True)
    print("=" * 95 + "\n", flush=True)

    t1, t2, t3, _ = get_all_universe_tiers()
    raw_dir = Path("data/raw_shards")
    exotic_dir = Path("data/exotic_shards")
    btc_df = get_btc_macro(raw_dir=raw_dir)
    
    tier3_symbols = [s for s in t3 if (raw_dir / f"{s}_USDT_1h.parquet").exists() or (raw_dir / f"1000{s}_USDT_1h.parquet").exists()]
    total_shards = len(tier3_symbols)
    print(f"Total Active Tier 3 Shards on Disk: {total_shards}", flush=True)
    print("Launching 10 Parallel Workers to compute features & evaluate all 5 models...\n", flush=True)

    tasks_args = [(sym, str(raw_dir), str(exotic_dir), btc_df) for sym in tier3_symbols]

    model_keys = ["Model A", "Model B", "Model B2", "Model C", "Model C2"]
    all_model_trades = {m: [] for m in model_keys}
    
    gtc_results = {}
    dood_results = {}
    jct_results = {}

    completed = 0
    with ProcessPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(process_single_shard, arg): arg[0] for arg in tasks_args}
        
        for future in as_completed(futures):
            sym = futures[future]
            try:
                ret_sym, shard_res = future.result()
                completed += 1
                
                counts = {}
                for m_key in model_keys:
                    df_t = shard_res.get(m_key)
                    n_t = len(df_t) if df_t is not None else 0
                    counts[m_key] = n_t
                    if df_t is not None and not df_t.empty:
                        all_model_trades[m_key].append(df_t)
                        if sym == "GTC":
                            gtc_results.setdefault(m_key, []).append(df_t)
                        elif sym == "DOOD":
                            dood_results.setdefault(m_key, []).append(df_t)
                        elif sym == "JCT":
                            jct_results.setdefault(m_key, []).append(df_t)

                elapsed = time.time() - t_start
                rate = completed / elapsed if elapsed > 0 else 1.0
                eta = (total_shards - completed) / rate
                pct = (completed / total_shards) * 100.0

                c_str = " ".join([f"{k}:{counts[k]}" for k in model_keys])
                print(f"  [{completed:3d}/{total_shards}] ({pct:5.1f}%) | Shard: {sym:12s} | B7 Trades: [{c_str}] | Elapsed: {format_eta(elapsed)} | ETA: {format_eta(eta)}", flush=True)

            except Exception as e:
                print(f"  [ERROR] Shard {sym} failed: {e}", flush=True)

    t_total = time.time() - t_start
    print("\n" + "=" * 95, flush=True)
    print(f"  STUDY S-CM COMPLETED ACROSS 384 SHARDS IN {format_eta(t_total)}", flush=True)
    print("=" * 95 + "\n", flush=True)

    model_labels = {
        "Model A": "Model A (Baseline V15.2: Static d_oi <= +35%)",
        "Model B": "Model B (Dynamic Studentized: z_oi_12h <= +2.00s)",
        "Model B2": "Model B2 (Dynamic Studentized Relaxed: z_oi_12h <= +2.50s)",
        "Model C": "Model C (Dynamic Percentile: pct_doi_30d <= 90%)",
        "Model C2": "Model C2 (Dynamic Percentile Relaxed: pct_doi_30d <= 95%)"
    }

    summary_rows = []
    for m_key in model_keys:
        t_list = all_model_trades[m_key]
        if t_list:
            all_t = pd.concat(t_list, ignore_index=True)
            is_open_bool = all_t['is_open'].fillna(False).astype(bool) if 'is_open' in all_t.columns else pd.Series(False, index=all_t.index)
            closed_t = all_t[~is_open_bool]
            n_closed = len(closed_t)
            n_tot = len(all_t)
            wr = (closed_t['pnl'] > 0).mean() * 100.0 if n_closed > 0 else 0.0
            net_log = all_t['log_ret'].sum() * 100.0
            mean_mfe = all_t['mfe'].mean() * 100.0 if 'mfe' in all_t.columns else 0.0
            mean_pnl = closed_t['pnl'].mean() * 100.0 if n_closed > 0 else 0.0
            max_gain = closed_t['pnl'].max() * 100.0 if n_closed > 0 else 0.0
            gains = closed_t.loc[closed_t['log_ret'] > 0, 'log_ret'].sum()
            losses = abs(closed_t.loc[closed_t['log_ret'] < 0, 'log_ret'].sum())
            pf = gains / losses if losses > 0 else np.nan
        else:
            n_tot, n_closed, wr, net_log, mean_mfe, mean_pnl, max_gain, pf = 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
            
        n_gtc = sum(len(x) for x in gtc_results.get(m_key, []))
        n_dood = sum(len(x) for x in dood_results.get(m_key, []))
        n_jct = sum(len(x) for x in jct_results.get(m_key, []))

        summary_rows.append({
            "Model": m_key,
            "Description": model_labels[m_key],
            "Total Trades": n_tot,
            "Closed Trades": n_closed,
            "Win Rate (%)": f"{wr:.2f}%",
            "Log PF": f"{pf:.3f}",
            "Net Log PnL (%)": f"{net_log:+.1f}%",
            "Mean PnL (%)": f"{mean_pnl:+.2f}%",
            "Mean Peak MFE (%)": f"{mean_mfe:.2f}%",
            "Max Gain (%)": f"{max_gain:+.2f}%",
            "GTC Trades": n_gtc,
            "DOOD Trades": n_dood,
            "JCT Trades": n_jct
        })

    summary_df = pd.DataFrame(summary_rows)
    print("=" * 125, flush=True)
    print("  STUDY S-CM: COMPARATIVE PERFORMANCE MATRIX (BOOK 7 TIER 3 MICRO-CAPS)", flush=True)
    print("=" * 125, flush=True)
    print(summary_df.to_string(index=False), flush=True)
    print("=" * 125 + "\n", flush=True)

    # Detailed Forensic Case Analysis
    print("FORENSIC CASE STUDIES (GTC, DOOD, JCT):", flush=True)
    for asset_name, asset_res in [("GTC", gtc_results), ("DOOD", dood_results), ("JCT", jct_results)]:
        print(f"\n--- {asset_name} ---", flush=True)
        for m_key in model_keys:
            dfs = asset_res.get(m_key, [])
            if dfs:
                comb = pd.concat(dfs, ignore_index=True)
                for _, r in comb.iterrows():
                    print(f"  [{m_key}] Entry: {r['entry']} | Exit: {r['exit']} | PnL: {r['pnl']*100:+.2f}% | LogRet: {r['log_ret']*100:+.2f}% | MFE: {r.get('mfe', 0)*100:+.1f}% | Reason: {r['reason']}", flush=True)
            else:
                print(f"  [{m_key}] 0 trades captured", flush=True)

    # Save artifact report
    out_csv = Path("v15_standalone/data/study_s_cm_summary.csv")
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    summary_df.to_csv(out_csv, index=False)
    print(f"\nSummary saved to {out_csv}", flush=True)

if __name__ == "__main__":
    run_study_s_cm()
