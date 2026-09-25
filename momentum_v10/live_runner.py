import os
import json
import argparse
import traceback
import pandas as pd
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
from momentum_v10.bar_clock import bar_is_closed
from momentum_v10.cta_dual import compute_features, step_cta
from momentum_v10.config import ROOT, SHARD_DIR, TAPE_DIR, FeatureConfig, CtaConfig
from momentum_v10.live_book import count_closed, count_open, dedupe_new_trades, preserve_research_open
from momentum_v10.universe_generator import load_with_oi, discover_assets
from momentum_v10.logger import get_logger, quarantine_corrupted_shard

logger = get_logger("engine")
trade_logger = get_logger("trades")
data_logger = get_logger("data_quality")

STATE_FILE = ROOT / 'data' / 'engine_state.json'
CLOSED_TRADES_FILE = TAPE_DIR / 'closed_trades.csv'
OPEN_TRADES_FILE = TAPE_DIR / 'open_trades.csv'

def active_trade_record(asset, trade, curr_close):
    """Open-book row. Saved trades have no entry_shock key; that is not a failure."""
    entry_price = trade['entry_price']
    return {
        'asset': asset,
        'engine': trade['engine'],
        'entry': trade['entry_time'],
        'entry_price': entry_price,
        'pnl': (curr_close - entry_price) / entry_price,
        'shock': trade.get('entry_shock', 0.0),
        'mae': (trade['trade_min_low'] - entry_price) / entry_price,
        'mfe': (trade['trade_max_high'] - entry_price) / entry_price,
    }

def process_live_asset(asset, data_dir, current_state):
    try:
        try:
            df = load_with_oi(asset, data_dir)
        except Exception as io_err:
            raw_file = Path(data_dir) / f"{asset}_USDT_1h.parquet"
            data_logger.error(f"[live_runner] Corrupted shard detected for {asset}: {io_err}")
            quarantine_corrupted_shard(raw_file, reason=str(io_err))
            raise
        fcfg = FeatureConfig(
            shock_percentile=99.0,
            shock_mult=None,
            year_min_periods=720,
            dormant_mode='relative',
            max_notional_usd=150000.0,
            require_taker=True,
            taker_buffer=0.01,
            first_of_run=True,
        )
        cfg = CtaConfig()
        
        # Vectorized math over the whole history (fast)
        feat = compute_features(df, fcfg, asset=asset)
        
        # Only iterate loop over NEW rows
        last_ts_str = current_state.get('last_processed_timestamp', '1970-01-01T00:00:00')
        last_ts = pd.to_datetime(last_ts_str)
        
        new_rows = feat[feat.index > last_ts]
        now = pd.Timestamp.now(tz='UTC')

        completed_trades = []
        last_stepped_ts = None
        last_stepped_close = None
        for ts, row in new_rows.iterrows():
            # The forming hour is not a bar yet. Leave the clock on the prior close
            # so the official candle is stepped once it has closed.
            if not bar_is_closed(ts, now):
                continue
            # Convert string timestamps back to datetime for active trades
            for t in current_state['active_trades']:
                if isinstance(t['entry_time'], str):
                    t['entry_time'] = pd.to_datetime(t['entry_time'])

            new_completed = step_cta(ts, row, current_state, cfg, asset)
            completed_trades.extend(new_completed)
            last_stepped_ts = ts
            last_stepped_close = row['close']

        # Convert datetimes back to strings for JSON
        for t in current_state['active_trades']:
            if hasattr(t['entry_time'], 'strftime'):
                t['entry_time'] = t['entry_time'].strftime('%Y-%m-%dT%H:%M:%S')

        if last_stepped_ts is not None:
            current_state['last_processed_timestamp'] = pd.Timestamp(last_stepped_ts).strftime('%Y-%m-%dT%H:%M:%S')
            curr_close = float(last_stepped_close)
        elif not feat.empty:
            closed_idx = [ts for ts in feat.index if bar_is_closed(ts, now)]
            curr_close = float(feat.loc[closed_idx[-1], 'close']) if closed_idx else 0.0
        else:
            curr_close = 0.0
        active_trades_records = [
            active_trade_record(asset, t, curr_close)
            for t in current_state['active_trades']
        ]

        return asset, current_state, completed_trades, active_trades_records

    except Exception as e:
        logger.error(f"[live_runner] {asset} failed: {e}")
        return asset, None, [], []

def run(data_dir: Path | None = None, workers: int | None = None) -> dict:
    data_dir = Path(data_dir) if data_dir is not None else SHARD_DIR
    if not data_dir.is_absolute():
        data_dir = ROOT / data_dir
    assets = discover_assets(data_dir)
    workers = workers or min(16, os.cpu_count() or 1)
    total_assets = len(assets)

    logger.info(f"[live_runner] Found {total_assets} assets in {data_dir}. Spawning {workers} workers.")

    if STATE_FILE.exists():
        with open(STATE_FILE, 'r') as f:
            engine_state = json.load(f)
    else:
        engine_state = {}

    all_completed = []
    all_active = []
    assets_failed = 0
    failed_assets = set()
    previous_open = pd.read_csv(OPEN_TRADES_FILE) if OPEN_TRADES_FILE.exists() else pd.DataFrame()

    milestone_step = max(1, total_assets // 4)
    completed_tasks = 0

    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = {}
        for asset in assets:
            state = engine_state.get(asset, {
                'active_trades': [],
                'armed_countdown': 0,
                'armed_shock': 0.0,
                'armed_hard_stop': 0.0,
                'last_processed_timestamp': '1970-01-01T00:00:00'
            })
            futures[executor.submit(process_live_asset, asset, data_dir, state)] = asset

        for future in as_completed(futures):
            completed_tasks += 1
            asset = futures[future]
            try:
                asset, new_state, completed, active = future.result()
                if new_state:
                    engine_state[asset] = new_state
                else:
                    assets_failed += 1
                    failed_assets.add(asset)
                all_completed.extend(completed)
                all_active.extend(active)
            except Exception as e:
                assets_failed += 1
                failed_assets.add(asset)
                logger.error(f"Error processing {asset}: {e}")

            if completed_tasks % milestone_step == 0 or completed_tasks == total_assets:
                pct = (completed_tasks / total_assets) * 100.0
                logger.info(f"[live_runner] Progress {completed_tasks}/{total_assets} ({pct:.0f}%) | Succeeded: {completed_tasks - assets_failed} | Failed: {assets_failed}")

    # Save new state atomically
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp_file = STATE_FILE.with_name(STATE_FILE.name + '.tmp')
    with open(tmp_file, 'w') as f:
        json.dump(engine_state, f, indent=4, default=lambda o: o.strftime('%Y-%m-%dT%H:%M:%S') if hasattr(o, 'strftime') else str(o))
    os.replace(tmp_file, STATE_FILE)

    # Append completed trades with aligned columns. Never duplicate a row
    # already in the closed ledger (a cold start replays full history).
    n_appended = 0
    if all_completed:
        df_completed = pd.DataFrame(all_completed)
        if 'entry_price' in df_completed.columns:
            df_completed['entry_px'] = df_completed['entry_price']
        if 'exit_price' in df_completed.columns:
            df_completed['exit_px'] = df_completed['exit_price']
        if 'entry' in df_completed.columns and 'exit' in df_completed.columns:
            e_dt = pd.to_datetime(df_completed['entry'], errors='coerce')
            x_dt = pd.to_datetime(df_completed['exit'], errors='coerce')
            dur_hrs = (x_dt - e_dt).dt.total_seconds() / 3600.0
            df_completed['duration_hours'] = dur_hrs
            df_completed['duration'] = dur_hrs.apply(lambda h: f"{int(h//24)}d {int(h%24)}h" if pd.notna(h) and h >= 24 else f"{int(h)}h" if pd.notna(h) else "")
        df_completed['status'] = 'CLOSED'

        if CLOSED_TRADES_FILE.exists():
            df_existing = pd.read_csv(CLOSED_TRADES_FILE)
        else:
            df_existing = pd.DataFrame()
        df_new = dedupe_new_trades(df_existing, df_completed)
        n_appended = int(len(df_new))

        # Trade Audit Logging for closed exits
        for _, tr in df_new.iterrows():
            pnl_val = float(tr['pnl']) if 'pnl' in tr and pd.notna(tr['pnl']) else 0.0
            trade_logger.info(
                f"[EXIT] {tr.get('asset')} | Engine: {tr.get('engine')} | "
                f"Entry: {tr.get('entry')} @ {float(tr.get('entry_px', 0)):.4f} | "
                f"Exit: {tr.get('exit')} @ {float(tr.get('exit_px', 0)):.4f} | "
                f"Reason: {tr.get('reason')} | PnL: {pnl_val*100:+.2f}% | "
                f"Hold: {tr.get('duration', '')}"
            )

        if df_existing.empty:
            df_combined = df_new
        elif df_new.empty:
            df_combined = df_existing
        else:
            df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        CLOSED_TRADES_FILE.parent.mkdir(parents=True, exist_ok=True)
        df_combined.to_csv(CLOSED_TRADES_FILE, index=False)
        logger.info(f"[live_runner] Appended {n_appended} new closed trades (skipped {len(df_completed) - n_appended} duplicates).")
    else:
        df_combined = pd.read_csv(CLOSED_TRADES_FILE) if CLOSED_TRADES_FILE.exists() else pd.DataFrame()

    preserved = preserve_research_open(OPEN_TRADES_FILE)
    if preserved is not None:
        logger.info(f"[live_runner] Preserved research open_at_end rows -> {preserved.name}")

    df_active = pd.DataFrame(all_active)
    if failed_assets and not previous_open.empty and 'asset' in previous_open.columns:
        carried = previous_open[previous_open['asset'].astype(str).isin(failed_assets)].copy()
        if 'reason' in carried.columns:
            carried = carried.loc[~carried['reason'].fillna('').astype(str).str.strip().eq('open_at_end')]
        if not carried.empty:
            df_active = pd.concat([df_active, carried], ignore_index=True)
            logger.warning(f"[live_runner] Carried {len(carried)} open rows for {len(failed_assets)} assets that failed this hour.")
    OPEN_TRADES_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not df_active.empty:
        df_active.to_csv(OPEN_TRADES_FILE, index=False)
        # Trade Audit Logging for newly opened positions
        prev_keys = set()
        if not previous_open.empty and {'asset', 'entry'}.issubset(previous_open.columns):
            prev_keys = set(zip(previous_open['asset'].astype(str), previous_open['entry'].astype(str)))
        for _, tr in df_active.iterrows():
            k = (str(tr.get('asset')), str(tr.get('entry')))
            if k not in prev_keys:
                trade_logger.info(
                    f"[ENTRY] New position: {tr.get('asset')} | Engine: {tr.get('engine')} | "
                    f"Entry: {tr.get('entry')} @ {float(tr.get('entry_price', 0)):.4f} | "
                    f"Shock: {float(tr.get('shock', 0)):.1f}x"
                )
    else:
        pd.DataFrame(columns=['asset', 'engine', 'entry', 'entry_price', 'pnl', 'shock', 'mae', 'mfe']).to_csv(OPEN_TRADES_FILE, index=False)

    n_open = count_open(df_active)
    n_closed = count_closed(df_combined)
    from momentum_v10.book_store import write_book
    write_book()
    logger.info(f"[live_runner] State updated. Open={n_open} Closed={n_closed} NewClosed={n_appended} FailedAssets={assets_failed}")
    return {
        "open": n_open,
        "closed": n_closed,
        "closed_this_hour": n_appended,
        "assets": total_assets,
        "assets_failed": assets_failed,
    }



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-dir', type=str, default=None)
    parser.add_argument('--workers', type=int, default=None)
    args = parser.parse_args()
    run(data_dir=Path(args.data_dir) if args.data_dir else None, workers=args.workers)

if __name__ == '__main__':
    main()

