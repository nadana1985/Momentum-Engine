"""
Kronos V12: Master Multi-Worker Runner with Thread-Firewall (build_v12_tape.py)
Executes Clean 6-Core matrix across Tier 1 and Tier 2 universe with zero OpenBLAS CPU contention.
"""

import os
# --- Thread-count firewall: must be set BEFORE numpy/pandas are imported ---
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("SCIPY_OPENBLAS64_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
import multiprocessing
from concurrent.futures import ProcessPoolExecutor, as_completed
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from momentum_v12.config import V12Config, MacroConfig, TierConfig, MicrostructureConfig, SizingConfig, ShadowReclaimConfig, Book3FlushReclaimConfig
from momentum_v12.tier_classifier import get_universe_tiers, get_all_universe_tiers
from momentum_v12.features_v12 import get_btc_macro, load_shard, compute_features_v12
from momentum_v12.telemetry_v12 import TelemetryCollector
from momentum_v12.engine_v12 import run_v12_engine

def get_runtime_config() -> V12Config:
    tier_cfg = TierConfig()
    macro_cfg = MacroConfig(enable_rs_btc_extension_veto=False) if os.environ.get("KRONOS_DISABLE_RS_VETO", "0") == "1" else MacroConfig()
    profile = os.environ.get("KRONOS_PROFILE", "production").lower()
    if profile in ("legacy", "baseline", "v12_legacy"):
        micro = MicrostructureConfig(
            enable_funding_sqz_exception=False,
            enable_turnover_scaling=False
        )
        sizing = SizingConfig(
            enable_lambda_sizing=False
        )
        return V12Config(macro=macro_cfg, tier=tier_cfg, micro=micro, sizing=sizing)
    elif profile in ("shadow_reclaim", "s_p", "shadow"):
        shadow = ShadowReclaimConfig(
            enable_bear_shadow_reclaims=True
        )
        return V12Config(macro=macro_cfg, tier=tier_cfg, shadow_reclaim=shadow)
    elif profile in ("baseline_no_book3", "book1_book2_only", "no_book3"):
        book3 = Book3FlushReclaimConfig(enable_book3_flush_reclaim=False)
        return V12Config(macro=macro_cfg, tier=tier_cfg, book3_flush=book3)
    elif profile in ("book3_flush", "flush_reclaim", "s_ac", "book3"):
        book3 = Book3FlushReclaimConfig(enable_book3_flush_reclaim=True)
        return V12Config(macro=macro_cfg, tier=tier_cfg, book3_flush=book3)
    # Canonical Production Architecture: Full-Stack Remediated + S-Q Sizing + Optimized S-AC Book 3
    return V12Config(macro=macro_cfg, tier=tier_cfg)

CFG = get_runtime_config()
RAW_DIR = ROOT / "data" / "raw_shards"
EXOTIC_DIR = ROOT / "data" / "exotic_shards"

tape_dir_env = os.environ.get("KRONOS_TAPE_DIR")
if not tape_dir_env:
    profile = os.environ.get("KRONOS_PROFILE", "production").lower()
    if profile in ("legacy", "baseline", "v12_legacy"):
        tape_dir_env = "data/all_tapes/v12_legacy_baseline"
    elif profile in ("shadow_reclaim", "s_p", "shadow"):
        tape_dir_env = "data/all_tapes/v12_shadow_reclaim_arm"
    elif profile in ("book3_flush", "flush_reclaim", "s_ac", "book3"):
        tape_dir_env = "data/all_tapes/v12_book3_flush_reclaim_arm"
    else:
        tape_dir_env = "data/all_tapes/v12_production"

TAPE_DIR = ROOT / Path(tape_dir_env)
TELEMETRY_DIR = ROOT / "telemetry" if "v12_production" == TAPE_DIR.name else (ROOT / "telemetry" / TAPE_DIR.name)


def process_asset(args):
    asset, tier = args
    try:
        btc_df = get_btc_macro(raw_dir=RAW_DIR)
        shard = load_shard(asset, raw_dir=RAW_DIR, exotic_dir=EXOTIC_DIR)
        if shard is None or len(shard) < (24 * 30):
            # MEDIUM-1: Log skipped assets with explicit reason
            n_bars = len(shard) if shard is not None else 0
            print(f"  [SKIP] {asset:<12} ({tier}) - shard missing or < 30 days ({n_bars} bars)")
            return None, None

        feat = compute_features_v12(shard, btc_df, tier_label=tier, cfg=CFG)
        telemetry = TelemetryCollector(storage_dir=TELEMETRY_DIR)
        trades_df = run_v12_engine(feat, asset, cfg=CFG, telemetry=telemetry)

        # Retrospectively enrich telemetry with forward metrics
        tel_df = telemetry.to_dataframe()
        if not tel_df.empty:
            tel_df = TelemetryCollector.enrich_forward_returns(tel_df, shard)

        # MEDIUM-1: Structured per-asset result log
        if trades_df is not None and not trades_df.empty:
            closed_t = trades_df[~trades_df['is_open']]
            n_closed = len(closed_t)
            net_log  = closed_t['log_ret'].sum() * 100.0 if n_closed > 0 else 0.0
            n_open   = len(trades_df[trades_df['is_open']])
            print(f"  [OK]   {asset:<12} ({tier}) - {n_closed} closed, {n_open} open | Net Log: {net_log:+.1f}%")
        else:
            print(f"  [ZERO] {asset:<12} ({tier}) - 0 trades (no signals fired)")

        return trades_df, tel_df
    except Exception as e:
        # MEDIUM-1: Log every failure with exception type for debugging
        print(f"  [ERR]  {asset:<12} ({tier}) - {type(e).__name__}: {e}")
        return None, None


def main():
    print("=" * 105)
    print("KRONOS V12: CLEAN 6-CORE MASTER PRODUCTION MATRIX")
    print("=" * 105)

    btc = get_btc_macro(raw_dir=RAW_DIR)
    if btc is None:
        print("ERROR: BTC macro shard not found. Run live_bridger.py first!")
        return

    btc_c = btc['close'].iloc[-1]
    btc_ema = btc['ema_200d'].iloc[-1]
    btc_ret30d = btc['ret_30d'].iloc[-1] * 100.0
    btc_dist = ((btc_c - btc_ema) / btc_ema) * 100.0
    is_macro_bull = (btc_c > btc_ema) and (btc_ret30d > 0.0)

    print(f"Macro Weather (BTC/USDT): Price: ${btc_c:,.2f} | 200d EMA: ${btc_ema:,.2f} ({btc_dist:+.2f}%)")
    print(f"BTC 30-Day Return:        {btc_ret30d:+.2f}%")
    print(f"Regime Conviction:        {'[RISK-ON BULL]' if is_macro_bull else '[DEFENSIVE BEAR - CASH PRESERVATION]'}\n")

    if CFG.tier.enable_tier3:
        t1_assets, t2_assets, t3_assets, _ = get_all_universe_tiers(CFG.tier)
        print(f"Discovered Liquid Universe: Tier 1: {len(t1_assets)} assets | Tier 2: {len(t2_assets)} assets | Tier 3: {len(t3_assets)} assets (Total: {len(t1_assets)+len(t2_assets)+len(t3_assets)})")
        task_list = [(a, "Tier 1") for a in t1_assets] + [(a, "Tier 2") for a in t2_assets] + [(a, "Tier 3") for a in t3_assets]
    else:
        t1_assets, t2_assets, _ = get_universe_tiers(CFG.tier)
        print(f"Discovered Liquid Universe: Tier 1: {len(t1_assets)} assets | Tier 2: {len(t2_assets)} assets (Total: {len(t1_assets)+len(t2_assets)})")
        task_list = [(a, "Tier 1") for a in t1_assets] + [(a, "Tier 2") for a in t2_assets]

    workers = min(16, multiprocessing.cpu_count())
    print(f"Spinning up {workers} workers with Thread-Count Firewall...\n")

    all_trades = []
    all_telemetry = []

    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(process_asset, item): item[0] for item in task_list}
        for future in as_completed(futures):
            sym = futures[future]
            t_df, tel_df = future.result()
            if t_df is not None and not t_df.empty:
                all_trades.append(t_df)
            if tel_df is not None and not tel_df.empty:
                all_telemetry.append(tel_df)

    # 1. Save Master Trades
    TAPE_DIR.mkdir(parents=True, exist_ok=True)
    if all_trades:
        df_trades = pd.concat(all_trades, ignore_index=True)
        trades_out = TAPE_DIR / "trades.parquet"
        raw_csv_out = TAPE_DIR / "master_raw_tape.csv"
        df_trades.to_parquet(trades_out, index=False)
        df_trades.to_csv(raw_csv_out, index=False)
        print(f"  [Tape] Master trades saved: {len(df_trades):,} records -> {trades_out}")

        # Summary Metrics — CRITICAL-3 FIX: PF in log-return space
        closed = df_trades[~df_trades['is_open']].copy()
        if not closed.empty:
            wins   = closed[closed['log_ret'] > 0]
            losses = closed[closed['log_ret'] <= 0]
            wr  = len(wins) / len(closed) * 100.0
            # CRITICAL-3: log-space PF
            log_wins   = wins['log_ret'].sum()
            log_losses = abs(losses['log_ret'].sum())
            pf  = (log_wins / log_losses) if log_losses > 1e-12 else 999.0
            tot_log = closed['log_ret'].sum() * 100.0
            mult = np.exp(tot_log / 100.0)

            # MEDIUM-2: Trade type breakdown for macro veto visibility
            n_reclaim = int(closed.get('is_reclaim', pd.Series(False)).sum()) if 'is_reclaim' in closed.columns else 0
            n_continuation = int(closed.get('is_continuation', pd.Series(False)).sum()) if 'is_continuation' in closed.columns else 0
            n_book2 = int((closed['book'] == 'Book 2').sum()) if 'book' in closed.columns else 0
            n_book3 = int((closed['book'] == 'Book 3').sum()) if 'book' in closed.columns else 0

            print("\n" + "=" * 105)
            print("V12 CLEAN 6-CORE HISTORICAL ATTRIBUTION")
            print("=" * 105)
            print(f"Total Closed Trades:        {len(closed):,}")
            print(f"Win Rate:                   {wr:.2f}%")
            print(f"Profit Factor (Log-Space):  {pf:.3f}   <- strict log-return PF (not arithmetic %)")
            print(f"Total Net Log Return:       {tot_log:+.1f}%")
            print(f"Compounded Capital Multiple:{mult:.2f}x ({mult*100-100:+.1f}% Net Compounded Gain)")
            print(f"Trade Type Breakdown:       Book 2 Squeezes: {n_book2} | Book 3 Flush Reclaims: {n_book3} | Bear-Trap Reclaims: {n_reclaim} | Continuation: {n_continuation}")

            print("\nAttribution by Liquidity Tier:")
            for t_name in ['Tier 1', 'Tier 2', 'Tier 3']:
                t_df = closed[closed['tier'] == t_name]
                if not t_df.empty:
                    t_w = t_df[t_df['pnl'] > 0]
                    t_l = t_df[t_df['pnl'] <= 0]
                    t_wr = len(t_w) / len(t_df) * 100.0
                    t_pf = t_w['pnl'].sum() / abs(t_l['pnl'].sum()) if len(t_l) > 0 else 999.0
                    t_log = t_df['log_ret'].sum() * 100.0
                    t_mult = np.exp(t_log / 100.0)
                    print(f"  {t_name:8s}: {len(t_df):4d} trades | WR: {t_wr:5.1f}% | PF: {t_pf:6.3f} | Net Log: {t_log:+7.1f}% | Mult: {t_mult:7.2f}x")

            print("\nAttribution by Book:")
            for b_name in ['Book 1', 'Book 2', 'Book 3']:
                b_df = closed[closed['book'] == b_name]
                if not b_df.empty:
                    b_w = b_df[b_df['pnl'] > 0]
                    b_l = b_df[b_df['pnl'] <= 0]
                    b_wr = len(b_w) / len(b_df) * 100.0
                    b_pf = b_w['pnl'].sum() / abs(b_l['pnl'].sum()) if len(b_l) > 0 else 999.0
                    b_log = b_df['log_ret'].sum() * 100.0
                    b_mult = np.exp(b_log / 100.0)
                    print(f"  {b_name:8s}: {len(b_df):4d} trades | WR: {b_wr:5.1f}% | PF: {b_pf:6.3f} | Net Log: {b_log:+7.1f}% | Mult: {b_mult:7.2f}x")
    else:
        print("  [Tape] No trades executed.")

    # 2. Save Telemetry
    TELEMETRY_DIR.mkdir(parents=True, exist_ok=True)
    if all_telemetry:
        df_tel = pd.concat(all_telemetry, ignore_index=True)
        tel_out = TELEMETRY_DIR / "veto_telemetry.parquet"
        df_tel.to_parquet(tel_out, index=False)
        print(f"  [Telemetry] Telemetry saved: {len(df_tel):,} records -> {tel_out}")

        summary = TelemetryCollector.compute_veto_alpha_summary(df_tel)
        print("\n" + "-" * 60)
        print("COUNTERFACTUAL VETO ALPHA SUMMARY")
        print("-" * 60)
        print(f"Total Vetoed Signals:       {summary['total_vetoes']:,}")
        print(f"Dodged Bullets (Loss Saved):{summary['dodged_bullets']:,}")
        print(f"Missed Opportunities:       {summary['missed_opportunities']:,}")
        print(f"Saved Capital Loss:         +{summary['saved_losses_pct']:.1f}%")
        print(f"Missed Upside Excursion:    -{summary['missed_upside_pct']:.1f}%")
        print(f"Net Veto Alpha:             {summary['net_veto_alpha_pct']:+.1f}% (Efficiency: {summary['efficiency_ratio']:.1f}%)")


if __name__ == "__main__":
    main()
