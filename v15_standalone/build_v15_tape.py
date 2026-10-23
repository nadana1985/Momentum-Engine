"""
Kronos V15: Master Multi-Worker Runner with Thread-Firewall (build_v15_tape.py)
Executes Clean Master Production Matrix across all 652 assets in the universe.
Synthesizes:
  1. Study S-CD Dynamic Heuristic Microstructure Governor & Toxic Long Trap Firewall (Rule 7 Certified)
  2. Study S-CG / S-CI Fat-Tail Convexity Preservation via Unconstrained 72h Donchian Trail
  3. Study S-BK Dual Confluence & Trapped Whale Squeeze Immunity
  4. Study S-CA Causal Day Close P_NB_High Acceptance
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

from momentum_v15.config import (
    V12Config, MacroConfig, TierConfig, MicrostructureConfig, SizingConfig,
    ShadowReclaimConfig, Book3FlushReclaimConfig, Book4Config, Book6Config, Book7Config, ExitConfig
)
from momentum_v15.tier_classifier import get_universe_tiers, get_all_universe_tiers
from momentum_v15.features_v12 import get_btc_macro, load_shard, compute_features_v12
from momentum_v15.telemetry_v12 import TelemetryCollector
from momentum_v15.engine_v12 import run_v12_engine

def get_runtime_config() -> V12Config:
    tier_cfg = TierConfig(enable_tier3=True)
    macro_cfg = MacroConfig(enable_rs_btc_extension_veto=False) if os.environ.get("KRONOS_DISABLE_RS_VETO", "0") == "1" else MacroConfig()
    
    # Canonical V15.0 Production Architecture:
    # Synthesizes Study S-CD Dynamic Governor + Rule 7 Dynamic Heuristics + Convexity Preservation
    book4_cfg = Book4Config(
        enable_toxic_long_firewall=True,
        enable_dynamic_whale_sizing=True,
        enable_climax_scoring_harvest=False # Preserves 72h Donchian convexity on macro runners
    )
    book6_cfg = Book6Config(
        enable_toxic_long_firewall=True,
        enable_dynamic_funding_sizing=True,
        enable_dynamic_whale_sizing=True,
        enable_oi_absorption_filter=True
    )
    exit_cfg = ExitConfig(
        enable_climax_scoring_engine=True,
        climax_harvest_urgency=55,
        climax_ratchet_urgency=35,
        enable_whale_squeeze_immunity=True
    )
    return V12Config(
        macro=macro_cfg,
        tier=tier_cfg,
        exit=exit_cfg,
        book4=book4_cfg,
        book6=book6_cfg,
        book7=Book7Config(
            enable_book7=True,
            require_negative_carry=True,
            max_funding_rate=0.0,
            enable_studentized_carry=True,
            max_z_funding=0.25,
            min_bars_below=168,
            max_dist_200d=0.20,
            enable_direct_breakout=True,
            direct_breakout_max_z_ls=-1.50,
            tranche_a_target_pct=0.03,
            breakeven_mfe_trigger=0.03,
            breakeven_cushion_pct=0.005,
            donchian_trail_bars=72
        )
    )

CFG = get_runtime_config()
RAW_DIR = ROOT / "data" / "raw_shards"
EXOTIC_DIR = ROOT / "data" / "exotic_shards"
if not RAW_DIR.exists():
    RAW_DIR = ROOT.parent / "data" / "raw_shards"
    EXOTIC_DIR = ROOT.parent / "data" / "exotic_shards"

tape_dir_env = os.environ.get("KRONOS_TAPE_DIR")
if not tape_dir_env:
    tape_dir_env = "data/all_tapes/v15_2_production"

TAPE_DIR = ROOT / Path(tape_dir_env)
TELEMETRY_DIR = ROOT / "telemetry"

def process_asset(args):
    asset, tier = args
    try:
        btc_df = get_btc_macro(raw_dir=RAW_DIR)
        shard = load_shard(asset, raw_dir=RAW_DIR, exotic_dir=EXOTIC_DIR)
        if shard is None or len(shard) < (24 * 30):
            return None, None

        feat = compute_features_v12(shard, btc_df, tier_label=tier, cfg=CFG)
        telemetry = TelemetryCollector(storage_dir=TELEMETRY_DIR)
        trades_df = run_v12_engine(feat, asset, cfg=CFG, telemetry=telemetry)

        tel_df = telemetry.to_dataframe()
        if not tel_df.empty:
            tel_df = TelemetryCollector.enrich_forward_returns(tel_df, shard)

        return trades_df, tel_df
    except Exception as e:
        import traceback
        err_msg = f"[CRITICAL ERROR] Failed processing asset '{asset}' ({tier}): {e}\n{traceback.format_exc()}"
        print(err_msg, file=sys.stderr)
        raise RuntimeError(f"Processing failed for asset '{asset}': {e}") from e

def main():
    print("=" * 105)
    print("KRONOS V15: MASTER UNIFIED PRODUCTION MATRIX (COLD BUILD)")
    print("Synthesizing Dynamic Microstructure Governor (S-CD) & Convexity Preservation (S-CG/S-CI)")
    print("=" * 105)

    btc = get_btc_macro(raw_dir=RAW_DIR)
    if btc is None:
        print("ERROR: BTC macro shard not found.")
        return

    btc_c = btc['close'].iloc[-1]
    btc_ema = btc['ema_200d'].iloc[-1]
    btc_ret30d = btc['ret_30d'].iloc[-1] * 100.0
    btc_dist = ((btc_c - btc_ema) / btc_ema) * 100.0
    is_macro_bull = (btc_c > btc_ema) and (btc_ret30d > 0.0)

    print(f"Macro Weather (BTC/USDT): Price: ${btc_c:,.2f} | 200d EMA: ${btc_ema:,.2f} ({btc_dist:+.2f}%)")
    print(f"BTC 30-Day Return:        {btc_ret30d:+.2f}%")
    print(f"Regime Conviction:        {'[RISK-ON BULL]' if is_macro_bull else '[DEFENSIVE BEAR - CASH PRESERVATION]'}\n")

    t1_assets, t2_assets, t3_assets, _ = get_all_universe_tiers(CFG.tier)
    print(f"Discovered Liquid Universe: Tier 1: {len(t1_assets)} assets | Tier 2: {len(t2_assets)} assets | Tier 3: {len(t3_assets)} assets (Total: {len(t1_assets)+len(t2_assets)+len(t3_assets)})")
    task_list = [(a, "Tier 1") for a in t1_assets] + [(a, "Tier 2") for a in t2_assets] + [(a, "Tier 3") for a in t3_assets]

    profile = os.environ.get("KRONOS_PROFILE", "fresh").lower()
    workers = min(16, multiprocessing.cpu_count())
    print(f"Spinning up {workers} workers with Thread-Count Firewall (Profile: {profile})...\n")

    all_trades = []
    all_telemetry = []
    completed = 0
    total = len(task_list)

    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(process_asset, item): item[0] for item in task_list}
        for future in as_completed(futures):
            sym = futures[future]
            try:
                t_df, tel_df = future.result()
            except Exception as e:
                print(f"\n[FATAL ERROR] Engine execution aborted: asset '{sym}' failed: {e}", file=sys.stderr)
                executor.shutdown(wait=False, cancel_futures=True)
                raise SystemExit(1)
            completed += 1
            if completed % 25 == 0 or completed == total:
                print(f"  [Progress] Processed {completed}/{total} shards ({completed/total*100:.1f}%)", flush=True)
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
        print(f"\n  [Tape] Master V15.0 trades saved: {len(df_trades):,} records -> {trades_out}")

        # Mirror to canonical production repository
        for canon_dir in [ROOT / "data" / "canonical", ROOT.parent / "data" / "canonical"]:
            canon_dir.mkdir(parents=True, exist_ok=True)
            canon_p15_2 = canon_dir / "canonical_v15_2_tape.parquet"
            canon_csv15_2 = canon_dir / "canonical_v15_2_tape.csv"
            df_trades.to_parquet(canon_p15_2, index=False)
            df_trades.to_csv(canon_csv15_2, index=False)
            
            # Backward compatibility mirrors for existing consumers
            canon_p15_1 = canon_dir / "canonical_v15_1_tape.parquet"
            canon_csv15_1 = canon_dir / "canonical_v15_1_tape.csv"
            df_trades.to_parquet(canon_p15_1, index=False)
            df_trades.to_csv(canon_csv15_1, index=False)
            
            canon_p15_0 = canon_dir / "canonical_v15_0_tape.parquet"
            canon_csv15_0 = canon_dir / "canonical_v15_0_tape.csv"
            df_trades.to_parquet(canon_p15_0, index=False)
            df_trades.to_csv(canon_csv15_0, index=False)
        print(f"  [Canonical] Master V15.2 Tape mirrored -> {canon_p15_2}")

        # Summary Metrics
        is_open_bool = df_trades['is_open'].fillna(False).astype(bool) if 'is_open' in df_trades.columns else pd.Series(False, index=df_trades.index)
        closed = df_trades[~is_open_bool].copy()
        if not closed.empty:
            wins   = closed[closed['log_ret'] > 0]
            losses = closed[closed['log_ret'] <= 0]
            wr  = len(wins) / len(closed) * 100.0
            log_wins   = wins['log_ret'].sum()
            log_losses = abs(losses['log_ret'].sum())
            pf  = (log_wins / log_losses) if log_losses > 1e-12 else 999.0
            tot_log = closed['log_ret'].sum() * 100.0
            mult = np.exp(tot_log / 100.0)

            n_book1 = int((closed['book'] == 'Book 1').sum()) if 'book' in closed.columns else 0
            n_book2 = int((closed['book'] == 'Book 2').sum()) if 'book' in closed.columns else 0
            n_book3 = int((closed['book'] == 'Book 3').sum()) if 'book' in closed.columns else 0
            n_book4 = int((closed['book'] == 'Book 4').sum()) if 'book' in closed.columns else 0
            n_book5 = int(closed['book'].isin(['Book 5', 'Book 5 (Shelf Absorption Squeeze)']).sum()) if 'book' in closed.columns else 0
            n_book6 = int(closed['book'].isin(['Book 6', 'Book 6 (Orderflow Base Reclaim)']).sum()) if 'book' in closed.columns else 0
            n_book7 = int((closed['book'] == 'Book 7').sum()) if 'book' in closed.columns else 0

            mult_str = f"{mult:.2e}x" if mult > 1e18 else f"{mult:,.2f}x"
            print("\n" + "=" * 105)
            print("KRONOS V15.0 MASTER UNIFIED PRODUCTION HISTORICAL ATTRIBUTION")
            print("=" * 105)
            print(f"Total Closed Trades:        {len(closed):,}")
            print(f"Win Rate:                   {wr:.2f}%")
            print(f"Profit Factor (Log-Space):  {pf:.3f}")
            print(f"Total Net Log Return:       {tot_log:+.1f}%")
            print(f"Compounded Capital Multiple:{mult_str}")
            print(f"Trade Type Breakdown:       Book 1: {n_book1} | Book 2 Squeezes: {n_book2} | Book 3 Flush Reclaims: {n_book3} | Book 4 200d Reclaims: {n_book4} | Book 5 Shelf Squeezes: {n_book5} | Book 6 3-SARE: {n_book6} | Book 7 MSSR: {n_book7}")

            print("\nAttribution by Liquidity Tier:")
            for t_name in ['Tier 1', 'Tier 2', 'Tier 3']:
                t_df = closed[closed['tier'] == t_name]
                if not t_df.empty:
                    t_w = t_df[t_df['log_ret'] > 0]
                    t_l = t_df[t_df['log_ret'] <= 0]
                    t_wr = len(t_w) / len(t_df) * 100.0
                    t_pf = t_w['log_ret'].sum() / max(1e-5, abs(t_l['log_ret'].sum())) if len(t_l) > 0 else 999.0
                    t_log = t_df['log_ret'].sum() * 100.0
                    print(f"  {t_name:8s}: {len(t_df):4d} trades | WR: {t_wr:5.1f}% | Log PF: {t_pf:6.3f} | Net Log: {t_log:+7.1f}%")

            print("\nAttribution by Book:")
            for b_name in ['Book 1', 'Book 2', 'Book 3', 'Book 4', 'Book 5', 'Book 6', 'Book 7']:
                b_df = closed[closed['book'] == b_name]
                if not b_df.empty:
                    b_w = b_df[b_df['log_ret'] > 0]
                    b_l = b_df[b_df['log_ret'] <= 0]
                    b_wr = len(b_w) / len(b_df) * 100.0
                    b_pf = b_w['log_ret'].sum() / max(1e-5, abs(b_l['log_ret'].sum())) if len(b_l) > 0 else 999.0
                    b_log = b_df['log_ret'].sum() * 100.0
                    print(f"  {b_name:18s}: {len(b_df):4d} trades | WR: {b_wr:5.1f}% | Log PF: {b_pf:6.3f} | Net Log: {b_log:+7.1f}%")
    else:
        print("  [Tape] No trades executed.")

    # 2. Save Telemetry
    TELEMETRY_DIR.mkdir(parents=True, exist_ok=True)
    if all_telemetry:
        df_tel = pd.concat(all_telemetry, ignore_index=True)
        tel_out = TELEMETRY_DIR / "veto_telemetry.parquet"
        df_tel.to_parquet(tel_out, index=False)
        (TAPE_DIR / "veto_telemetry.parquet").write_bytes(tel_out.read_bytes())
        print(f"\n  [Telemetry] Telemetry saved: {len(df_tel):,} records -> {tel_out}")

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
