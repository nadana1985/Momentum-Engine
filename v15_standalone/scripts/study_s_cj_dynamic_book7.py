"""
Study S-CJ: Clean-Room Dynamic Studentized Microstructure Governor for Book 7 (MSSR)
Rule 7 Certified: Eliminating Arbitrary Static Constants (FR <= 0.0 & d_oi <= +35%)
in Tier 3 Micro-Caps.

Tests 4 Models across all available Tier 3 Shards:
- Model 0 (Baseline V15.0): Static FR <= 0.0 & Static d_oi_tokens_24h <= 35%
- Model 1 (Dynamic Studentized Funding): z_fnd_30d <= +0.25 sigma (or FR <= 0.0)
- Model 2 (Whale Conviction Carry Override): z_fnd <= +0.50 sigma IF z_ls <= -1.50 sigma
- Model 3 (Unified Sovereign Rule 7 Stack): Studentized Funding + Whale Override + Studentized OI Bubble (z_oi <= 2.0s)
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

def run_study_s_cj():
    t_start = time.time()
    print("=" * 80)
    print("  STUDY S-CJ: CLEAN-ROOM DYNAMIC STUDENTIZED BOOK 7 ENGINE (TIER 3 MICRO-CAPS)")
    print("=" * 80 + "\n")

    t1, t2, t3, _ = get_all_universe_tiers()
    btc_df = get_btc_macro()
    raw_dir = Path("data/raw_shards")
    exotic_dir = Path("data/exotic_shards")
    
    tier3_symbols = [s for s in t3 if (raw_dir / f"{s}_USDT_1h.parquet").exists() or (raw_dir / f"1000{s}_USDT_1h.parquet").exists()]
    print(f"Total Active Tier 3 Shards on Disk: {len(tier3_symbols)}")
    
    # Pre-load and compute features for all Tier 3 shards once to avoid redundant computations
    print("Pre-computing features across all Tier 3 shards...")
    feature_cache = {}
    cfg_base = V12Config()
    for sym in tier3_symbols:
        shard_df = load_shard(sym, raw_dir, exotic_dir)
        if shard_df is not None and not shard_df.empty:
            f_df = compute_features_v12(shard_df, btc_df, tier_label="Tier 3", cfg=cfg_base)
            feature_cache[sym] = f_df
            
    print(f"Successfully cached {len(feature_cache)} Tier 3 feature frames.\n")
    
    # 4 Model Configurations
    models = {
        "Model 0 (V15.0 Baseline)": Book7Config(
            enable_book7=True,
            require_negative_carry=True,
            max_funding_rate=0.0,
            enable_studentized_carry=False,
            enable_whale_carry_override=False,
            enable_studentized_oi_bubble=False,
            max_d_oi_tokens=0.35,
        ),
        "Model 1 (Studentized Funding z<=+0.25s)": Book7Config(
            enable_book7=True,
            require_negative_carry=True,
            max_funding_rate=0.0,
            enable_studentized_carry=True,
            max_z_funding=0.25,
            enable_whale_carry_override=False,
            enable_studentized_oi_bubble=False,
            max_d_oi_tokens=0.35,
        ),
        "Model 2 (Whale Conviction Carry Override)": Book7Config(
            enable_book7=True,
            require_negative_carry=True,
            max_funding_rate=0.0,
            enable_studentized_carry=True,
            max_z_funding=0.25,
            enable_whale_carry_override=True,
            whale_override_max_z_ls=-1.50,
            whale_override_max_z_fnd=0.50,
            enable_studentized_oi_bubble=False,
            max_d_oi_tokens=0.35,
        ),
        "Model 3 (Unified Rule 7 Dynamic Heuristics)": Book7Config(
            enable_book7=True,
            require_negative_carry=True,
            max_funding_rate=0.0,
            enable_studentized_carry=True,
            max_z_funding=0.25,
            enable_whale_carry_override=True,
            whale_override_max_z_ls=-1.50,
            whale_override_max_z_fnd=0.50,
            enable_studentized_oi_bubble=True,
            max_z_oi=2.00,
            max_d_oi_tokens=0.50,
        )
    }

    results = {}
    
    for m_name, b7_cfg in models.items():
        print(f"--- Simulating: {m_name} ---")
        cfg_variant = V12Config(book7=b7_cfg)
        b7_trades_list = []
        jct_trades = []
        dood_trades = []
        
        for sym, feat_df in feature_cache.items():
            trades_df = run_v12_engine(feat_df, sym, cfg=cfg_variant)
            if not trades_df.empty:
                b7_t = trades_df[trades_df['book'] == 'Book 7']
                if not b7_t.empty:
                    b7_trades_list.append(b7_t)
                    if sym == 'JCT':
                        jct_trades.append(b7_t)
                    if sym == 'DOOD':
                        dood_trades.append(b7_t)
                        
        if b7_trades_list:
            combined = pd.concat(b7_trades_list, ignore_index=True)
            n_t = len(combined)
            wr = (combined['pnl'] > 0).mean() * 100.0
            w_sum = combined[combined['pnl'] > 0]['pnl'].sum()
            l_sum = abs(combined[combined['pnl'] <= 0]['pnl'].sum())
            pf = w_sum / l_sum if l_sum > 0 else 999.0
            log_ret = combined['log_ret'].sum() * 100.0
            mean_ret = combined['pnl'].mean() * 100.0
            mfe_mean = combined['mfe'].mean() * 100.0
        else:
            combined = pd.DataFrame()
            n_t, wr, pf, log_ret, mean_ret, mfe_mean = 0, 0.0, 0.0, 0.0, 0.0, 0.0
            
        jct_cnt = len(pd.concat(jct_trades)) if jct_trades else 0
        dood_cnt = len(pd.concat(dood_trades)) if dood_trades else 0
        
        results[m_name] = {
            "trades": n_t,
            "win_rate": wr,
            "log_pf": pf,
            "net_log": log_ret,
            "mean_pnl": mean_ret,
            "mfe_mean": mfe_mean,
            "jct_trades": jct_cnt,
            "dood_trades": dood_cnt,
            "df": combined
        }
        print(f"  -> Trades: {n_t:,} | WR: {wr:.2f}% | Log PF: {pf:.3f} | Net Log: {log_ret:+.1f}% | Mean MFE: {mfe_mean:.1f}%")
        print(f"  -> JCT Captured: {jct_cnt} trades | DOOD Captured: {dood_cnt} trades\n")
        if jct_cnt > 0:
            for _, r in pd.concat(jct_trades).iterrows():
                print(f"     [JCT Trade] Entry: {r['entry']} ({r['entry_price']}) -> Exit: {r['exit']} ({r['exit_price']}) | PnL={r['pnl']:+.2%} | Reason={r['reason']}")
        if dood_cnt > 0:
            for _, r in pd.concat(dood_trades).iterrows():
                print(f"     [DOOD Trade] Entry: {r['entry']} ({r['entry_price']}) -> Exit: {r['exit']} ({r['exit_price']}) | PnL={r['pnl']:+.2%} | Reason={r['reason']}")

    elapsed = time.time() - t_start
    print(f"\nStudy S-CJ completed in {elapsed:.1f}s.")
    return results

if __name__ == "__main__":
    run_study_s_cj()
