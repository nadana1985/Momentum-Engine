"""
Taguchi Robustness Stress Test Battery for V13.2 Master Canonical Tape (trades.parquet - 5,010 Trades)
Applies Taguchi Quality Engineering methodology:
1. Controllable Factors: Multi-Book Strategy Stack (Books 1 to 6)
2. Noise Factors:
   - Slippage / Friction amplification (+10 bps, +25 bps, +50 bps, +100 bps)
   - Entry Delay / Execution lag (negative price excursion jitter: -25 bps, -50 bps, -100 bps)
   - Adverse fill penalty / roundtrip haircut
   - 1,000-Path Block-Bootstrap Monte Carlo resampling (block size = 20)
3. Taguchi Robustness Metrics:
   - Normalized Percentile Spread: (P90 - P10) / (|Median| + 1e-4)
   - Downside Robustness Loss: (Median - P10) / (|Median| + 1e-4)
   - Stress Survival Ratio: P10 / (|Median| + 1e-4)
"""

import numpy as np
import pandas as pd
import json

def load_data():
    df = pd.read_parquet('v12_standalone/data/all_tapes/v13_production/trades.parquet')
    return df

def compute_metrics(returns):
    wins = returns > 0
    losses = returns < 0
    wr = float(wins.mean() * 100.0)
    tot_log = float(returns.sum())
    gain = float(returns[wins].sum()) if wins.any() else 0.0
    loss = float(abs(returns[losses].sum())) if losses.any() else 1e-6
    pf = gain / loss if loss > 0 else 999.0
    return {
        "trades": len(returns),
        "win_rate": wr,
        "total_log_ret": tot_log,
        "log_pf": pf,
        "mean_bps": float(returns.mean() * 10000.0)
    }

def run_slippage_stress(df, slippage_bps_list=[0, 10, 25, 50, 75, 100]):
    results = {}
    base_log = df['log_ret'].values
    for s_bps in slippage_bps_list:
        # Subtract additional friction in log terms
        # 1 bp = 0.0001
        friction = (s_bps / 10000.0)
        stressed_log = base_log - friction
        m = compute_metrics(stressed_log)
        results[f"+{s_bps}bps"] = m
    return results

def run_execution_jitter_stress(df, jitter_bps_list=[0, 25, 50, 75, 100], n_sims=500, seed=42):
    """
    Simulates stochastic fill degradation: each trade suffers random execution slippage 
    drawn from Exponential or Half-Normal with scale = jitter_bps.
    """
    rng = np.random.default_rng(seed)
    base_log = df['log_ret'].values
    n = len(base_log)
    results = {}
    
    for j_bps in jitter_bps_list:
        if j_bps == 0:
            results["0bps"] = compute_metrics(base_log)
            continue
            
        pf_list = []
        wr_list = []
        tot_list = []
        for _ in range(n_sims):
            jitter = rng.exponential(scale=j_bps / 10000.0, size=n)
            stressed_log = base_log - jitter
            m = compute_metrics(stressed_log)
            pf_list.append(m['log_pf'])
            wr_list.append(m['win_rate'])
            tot_list.append(m['total_log_ret'])
            
        p10_pf = float(np.percentile(pf_list, 10))
        p50_pf = float(np.median(pf_list))
        p90_pf = float(np.percentile(pf_list, 90))
        denom = abs(p50_pf) + 1e-4
        
        results[f"jitter_{j_bps}bps"] = {
            "median_pf": p50_pf,
            "p10_pf": p10_pf,
            "p90_pf": p90_pf,
            "median_wr": float(np.median(wr_list)),
            "p10_wr": float(np.percentile(wr_list, 10)),
            "norm_spread": (p90_pf - p10_pf) / denom,
            "downside_loss": (p50_pf - p10_pf) / denom,
            "survival_ratio": p10_pf / denom
        }
    return results

def run_block_bootstrap(df, n_sims=1000, block_size=20, seed=42):
    rng = np.random.default_rng(seed)
    base_log = df['log_ret'].values
    n = len(base_log)
    n_blocks = int(np.ceil(n / block_size))
    max_start = n - block_size
    
    pf_arr = np.zeros(n_sims)
    wr_arr = np.zeros(n_sims)
    tot_arr = np.zeros(n_sims)
    
    for i in range(n_sims):
        starts = rng.integers(0, max_start + 1, size=n_blocks)
        sample = np.concatenate([base_log[s : s + block_size] for s in starts])[:n]
        m = compute_metrics(sample)
        pf_arr[i] = m['log_pf']
        wr_arr[i] = m['win_rate']
        tot_arr[i] = m['total_log_ret']
        
    p10_pf = float(np.percentile(pf_arr, 10))
    p50_pf = float(np.median(pf_arr))
    p90_pf = float(np.percentile(pf_arr, 90))
    denom = abs(p50_pf) + 1e-4
    
    p10_wr = float(np.percentile(wr_arr, 10))
    p50_wr = float(np.median(wr_arr))
    p90_wr = float(np.percentile(wr_arr, 90))
    
    return {
        "n_simulations": n_sims,
        "block_size": block_size,
        "log_pf": {
            "median": p50_pf,
            "p10": p10_pf,
            "p90": p90_pf,
            "norm_percentile_spread": (p90_pf - p10_pf) / denom,
            "downside_loss": (p50_pf - p10_pf) / denom,
            "survival_ratio": p10_pf / denom,
        },
        "win_rate": {
            "median": p50_wr,
            "p10": p10_wr,
            "p90": p90_wr,
            "norm_percentile_spread": (p90_wr - p10_wr) / (p50_wr + 1e-4),
        },
        "total_log_return": {
            "median": float(np.median(tot_arr)),
            "p10": float(np.percentile(tot_arr, 10)),
            "p90": float(np.percentile(tot_arr, 90)),
        }
    }

def run_per_book_stress(df, friction_bps=25):
    friction = friction_bps / 10000.0
    book_res = {}
    for book_name, b_df in df.groupby('book'):
        base_log = b_df['log_ret'].values
        base_m = compute_metrics(base_log)
        stressed_m = compute_metrics(base_log - friction)
        book_res[book_name] = {
            "trades": len(base_log),
            "baseline_pf": base_m['log_pf'],
            "baseline_wr": base_m['win_rate'],
            "stressed_pf_25bps": stressed_m['log_pf'],
            "stressed_wr_25bps": stressed_m['win_rate'],
            "pf_retention": stressed_m['log_pf'] / (base_m['log_pf'] + 1e-4)
        }
    return book_res

if __name__ == '__main__':
    df = load_data()
    print("=== 1. BASELINE V13.2 AUDIT (5,010 TRADES) ===")
    base = compute_metrics(df['log_ret'].values)
    print(json.dumps(base, indent=2))
    
    print("\n=== 2. SLIPPAGE & FRICTION AMPLIFICATION (0 to 100 bps) ===")
    slip_res = run_slippage_stress(df)
    for k, v in slip_res.items():
        print(f"{k}: Win Rate={v['win_rate']:.2f}% | Log PF={v['log_pf']:.3f} | Total Log Ret={v['total_log_ret']:.1f}")
        
    print("\n=== 3. STOCHASTIC EXECUTION JITTER (0 to 100 bps) ===")
    jit_res = run_execution_jitter_stress(df)
    for k, v in jit_res.items():
        if k == "0bps":
            continue
        print(f"{k}: Median PF={v['median_pf']:.3f} | P10 PF={v['p10_pf']:.3f} | Spread={v['norm_spread']:.3f} | Survival={v['survival_ratio']:.3f} | Median WR={v['median_wr']:.2f}% (P10 WR={v['p10_wr']:.2f}%)")
        
    print("\n=== 4. 1,000-PATH BLOCK BOOTSTRAP MONTE CARLO ===")
    mc_res = run_block_bootstrap(df)
    print(json.dumps(mc_res, indent=2))
    
    print("\n=== 5. PER-BOOK ROBUSTNESS AT +25 BPS FRICTION ===")
    book_res = run_per_book_stress(df, 25)
    for b, d in book_res.items():
        print(f"[{b} | {d['trades']} trades] Baseline PF={d['baseline_pf']:.3f} -> Stressed={d['stressed_pf_25bps']:.3f} (Retention: {d['pf_retention']*100:.1f}%) | WR: {d['baseline_wr']:.1f}% -> {d['stressed_wr_25bps']:.1f}%")
