# Version 10
"""momentum_v10/l5_generator.py — Full-history Layer 5 Relative Strength Cross-Sectional Ranking Generator.

Generates the complete historical L5 ranking parquet (data/l5_ranking.parquet)
across the full universe of altcoins from the beginning of available history
up to the latest hourly candle.

Pipeline Flow:
  1. Loads BTC_USDT_1h benchmark from data/raw_shards/.
  2. For all 530+ altcoins:
     - Computes hourly RS = Alt Close / BTC Close.
     - Resamples to Daily RS -> computes L2.6 Daily structural state machine.
     - Resamples to Weekly RS-OHLC (W-MON) -> computes L2.6 Weekly states & events.
     - Computes L2.7 Quality score metric.
  3. Executes L4B CTLE Engine (detects phase transitions: EARLY/CONFIRMED/LATE/FAILED, delta_t, recency).
  4. Executes L5 Composite Engine (filters quality >= 0.5 & phase != FAILED, sorts by priority/delta_t/recency/symbol).
  5. Serializes canonical ['date', 'symbol', 'rank'] to data/l5_ranking.parquet.
"""
from __future__ import annotations

import argparse
import logging
import os
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

# Resolve RelativeStrengthResearch path
RS_RESEARCH_DIR = Path("F:/RelativeStrengthResearch")
if RS_RESEARCH_DIR.exists() and str(RS_RESEARCH_DIR) not in sys.path:
    sys.path.insert(0, str(RS_RESEARCH_DIR))

try:
    from src_v2.layer2_6.core import run_layer2_6_pipeline
    from src_v2.layer2_7.core.metrics.quality import compute_quality
    from src_v2.layer4b.engine import CTLEEngine
    from src_v2.layer5.core.composite_engine import CompositeEngine
except ImportError as err:
    raise ImportError(
        f"Failed to import RelativeStrengthResearch modules from {RS_RESEARCH_DIR}: {err}"
    ) from err

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [l5_generator] %(message)s",
)
logger = logging.getLogger("momentum_v10.l5_generator")


def _to_epoch_ms(dt_index: pd.DatetimeIndex) -> np.ndarray:
    """Safely convert DatetimeIndex to integer epoch milliseconds across pandas versions."""
    int_vals = dt_index.view("int64")
    dtype_str = str(dt_index.dtype)
    if "ns" in dtype_str:
        return int_vals // 1_000_000
    elif "us" in dtype_str:
        return int_vals // 1_000
    elif "ms" in dtype_str:
        return int_vals
    elif "s" in dtype_str:
        return int_vals * 1_000
    return (int_vals // 1_000_000)


def generate_l5_rankings(
    raw_dir: Path | str = Path("data/raw_shards"),
    output_path: Path | str = Path("data/l5_ranking.parquet"),
    min_hours: int = 240,
    min_weeks: int = 8,
) -> pd.DataFrame:
    """Generate full-history cross-sectional L5 rankings for all assets in raw_dir."""
    raw_path = Path(raw_dir)
    out_file = Path(output_path)
    out_file.parent.mkdir(parents=True, exist_ok=True)

    t0 = time.time()
    btc_file = raw_path / "BTC_USDT_1h.parquet"
    if not btc_file.exists():
        raise FileNotFoundError(f"Benchmark BTC shard not found at {btc_file}")

    logger.info("Loading BTC benchmark shard: %s", btc_file)
    btc = pd.read_parquet(btc_file, columns=["timestamp", "close"])
    btc["dt"] = pd.to_datetime(btc["timestamp"], unit="ms", utc=True)
    btc = btc.set_index("dt").sort_index()

    # Discover altcoins
    suffix = "_USDT_1h.parquet"
    asset_files = sorted(
        p for p in raw_path.glob(f"*{suffix}")
        if p.name != "BTC_USDT_1h.parquet"
    )
    total_assets = len(asset_files)
    logger.info("Discovered %d altcoin shards in %s", total_assets, raw_path)

    l26_daily_list: list[pd.DataFrame] = []
    l26_weekly_list: list[pd.DataFrame] = []
    l27_list: list[pd.DataFrame] = []

    processed_count = 0
    skipped_count = 0

    for idx, p in enumerate(asset_files, 1):
        asset = p.name[:-len(suffix)]
        symbol = f"{asset}USDT"

        try:
            alt = pd.read_parquet(p, columns=["timestamp", "close"])
            if len(alt) < min_hours:
                skipped_count += 1
                continue

            alt["dt"] = pd.to_datetime(alt["timestamp"], unit="ms", utc=True)
            alt = alt.set_index("dt").sort_index()

            # Align alt with BTC
            joined = pd.DataFrame({"alt": alt["close"], "btc": btc["close"]}).dropna()
            if len(joined) < min_hours:
                skipped_count += 1
                continue

            # Hourly RS
            joined["rs"] = joined["alt"] / joined["btc"]

            # 1. Daily RS (resample 1D, last close)
            daily = joined["rs"].resample("1D").last().dropna()
            if len(daily) < 14:
                skipped_count += 1
                continue

            d_vals = daily.values.astype(np.float64)
            d_vals.flags.writeable = False
            d_states, _, _, _ = run_layer2_6_pipeline(d_vals, d_vals, d_vals, d_vals)

            d_ms = _to_epoch_ms(daily.index)
            l26_daily_list.append(pd.DataFrame({
                "ts_ms": d_ms,
                "symbol": symbol,
                "state": d_states,
            }))

            # 2. Weekly RS-OHLC (resample W-MON, label='left', closed='left')
            weekly = joined["rs"].resample("W-MON", label="left", closed="left").agg({
                "open": "first",
                "high": "max",
                "low": "min",
                "close": "last",
            }).dropna()

            if len(weekly) < min_weeks:
                skipped_count += 1
                continue

            w_o = weekly["open"].values.astype(np.float64)
            w_h = weekly["high"].values.astype(np.float64)
            w_l = weekly["low"].values.astype(np.float64)
            w_c = weekly["close"].values.astype(np.float64)
            for arr in (w_o, w_h, w_l, w_c):
                arr.flags.writeable = False

            w_states, w_events, _, _ = run_layer2_6_pipeline(w_o, w_h, w_l, w_c)
            w_ms = _to_epoch_ms(weekly.index)
            w_dates = weekly.index.strftime("%Y-%m-%d")

            l26_weekly_list.append(pd.DataFrame({
                "ts_ms": w_ms,
                "date": w_dates,
                "symbol": symbol,
                "state": w_states,
                "structural_state": w_states,
                "close_rs": weekly["close"].values,
            }))

            # 3. L2.7 Quality metric scoring
            q_scores = compute_quality(weekly, w_states.tolist(), w_events.tolist())
            l27_list.append(pd.DataFrame({
                "date": w_dates,
                "symbol": symbol,
                "quality_score": q_scores,
            }))

            processed_count += 1
            if idx % 50 == 0 or idx == total_assets:
                logger.info("Processed %d/%d assets (valid: %d, skipped: %d)...",
                            idx, total_assets, processed_count, skipped_count)

        except Exception as e:
            logger.warning("Error processing %s: %s", symbol, e)
            skipped_count += 1
            continue

    logger.info("Asset feature extraction complete: %d assets processed in %.1fs",
                processed_count, time.time() - t0)

    if not l26_daily_list or not l26_weekly_list:
        raise RuntimeError("No valid asset series processed for L5 generation.")

    # Concat panels
    l26_daily = pd.concat(l26_daily_list, ignore_index=True)
    l26_weekly = pd.concat(l26_weekly_list, ignore_index=True)
    l27_df = pd.concat(l27_list, ignore_index=True)

    # 4. CTLE Engine (L4B)
    t_ctle = time.time()
    logger.info("Executing L4B CTLE lead/lag engine across panel...")
    ctle = CTLEEngine()
    l4b_df = ctle.run(l26_daily, l26_weekly)
    logger.info("L4B CTLE completed in %.1fs (panel rows: %d)",
                time.time() - t_ctle, len(l4b_df))

    # 5. Composite Engine (L5)
    t_comp = time.time()
    logger.info("Executing L5 Composite Engine for cross-sectional ranking...")
    ranked_df = CompositeEngine.run(l27_df, l4b_df, l26_weekly)
    logger.info("L5 CompositeEngine completed in %.1fs", time.time() - t_comp)

    if ranked_df.empty:
        raise RuntimeError("CompositeEngine returned zero ranked records.")

    # Canonical schema: ['date', 'symbol', 'rank']
    canonical_df = ranked_df[["date", "symbol", "rank"]].copy()
    canonical_df["rank"] = canonical_df["rank"].astype("int64")
    canonical_df = canonical_df.sort_values(["date", "rank", "symbol"]).reset_index(drop=True)

    # Save artifact
    canonical_df.to_parquet(out_file, index=False, compression="snappy")
    elapsed = time.time() - t0

    dates_count = canonical_df["date"].nunique()
    symbols_count = canonical_df["symbol"].nunique()
    first_date = canonical_df["date"].min()
    last_date = canonical_df["date"].max()
    file_size_kb = out_file.stat().st_size / 1024

    logger.info("============================================================")
    logger.info(" L5 RANKING ARTIFACT GENERATED SUCCESSFULLY")
    logger.info(" Output:        %s (%.1f KB)", out_file, file_size_kb)
    logger.info(" Total Records: %d", len(canonical_df))
    logger.info(" Total Dates:   %d (%s to %s)", dates_count, first_date, last_date)
    logger.info(" Total Symbols: %d", symbols_count)
    logger.info(" Wall Clock:    %.1f seconds", elapsed)
    logger.info("============================================================")

    return canonical_df


def main():
    parser = argparse.ArgumentParser(
        description="Generate full-history L5 relative strength rankings across the altcoin universe."
    )
    parser.add_argument(
        "--raw-dir",
        type=str,
        default="data/raw_shards",
        help="Path to directory with *_1h.parquet shards (default: data/raw_shards)",
    )
    parser.add_argument(
        "--out",
        type=str,
        default="data/l5_ranking.parquet",
        help="Output parquet path (default: data/l5_ranking.parquet)",
    )
    args = parser.parse_args()

    generate_l5_rankings(raw_dir=args.raw_dir, output_path=args.out)


if __name__ == "__main__":
    main()

