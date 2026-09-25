import os
import sys
import glob
from pathlib import Path
import pandas as pd
import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging

ROOT = Path(__file__).resolve().parent.parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from config.ingestion.sync_state_manager import (
    SYNC_STATE_PATH,
    SyncStateManager,
    build_sync_state,
)
from momentum_v10.bar_clock import drop_forming_hours, drop_forming_klines
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from momentum_v10.logger import get_logger, quarantine_corrupted_shard

logger = get_logger("ingest")
data_logger = get_logger("data_quality")

EXOTIC_DIR = str(ROOT / "data" / "exotic_shards")
RAW_DIR = str(ROOT / "data" / "raw_shards")

_sync = None

_session = None

def get_session():
    global _session
    if _session is None:
        _session = requests.Session()
        retries = Retry(total=3, backoff_factor=1.0, status_forcelist=[429, 500, 502, 503, 504])
        adapter = HTTPAdapter(max_retries=retries, pool_connections=50, pool_maxsize=50)
        _session.mount("https://", adapter)
        _session.headers.update({"User-Agent": "Mozilla/5.0"})
    return _session

def get_symbols():
    # Primary: symbols with exotic shards (funding + metrics)
    exotic_syms = set(
        os.path.basename(f).replace("_funding.parquet", "")
        for f in glob.glob(os.path.join(EXOTIC_DIR, "*_funding.parquet"))
    )
    # Secondary: kline-only assets in raw_shards with NO exotic shard
    # These were silently skipped before — now included for kline gap-fill
    raw_syms = set(
        os.path.basename(f).replace("_USDT_1h.parquet", "") + "USDT"
        for f in glob.glob(os.path.join(RAW_DIR, "*_USDT_1h.parquet"))
    )
    kline_only = raw_syms - exotic_syms
    if kline_only:
        logger.info(f"Discovered {len(kline_only)} kline-only assets (no exotic shard) — klines will be gap-filled.")
    return sorted(exotic_syms | kline_only)

def safe_read_parquet(path: str, sym: str, shard_type: str) -> pd.DataFrame:
    """Read a parquet file safely, quarantining it if corrupted."""
    if not os.path.exists(path):
        return pd.DataFrame()
    try:
        return pd.read_parquet(path)
    except Exception as e:
        data_logger.error(f"[{sym}] Corrupted {shard_type} shard detected at {path}: {e}")
        quarantine_corrupted_shard(path, reason=f"{shard_type} corrupted: {e}")
        return pd.DataFrame()

def _get_last_ts_from_parquet(path):
    try:
        df = pd.read_parquet(path, columns=['timestamp'])
        if df.empty: return None
        return int(df['timestamp'].max())
    except Exception as e:
        data_logger.warning("Unreadable or corrupted timestamp in %s: %s", path, e)
        return None

# Global funding cache
global_funding = {}

def prefetch_global_funding():
    global global_funding
    logger.info("Pre-fetching global funding rates (Weight: 1)...")
    try:
        sess = get_session()
        res = sess.get("https://fapi.binance.com/fapi/v1/premiumIndex", timeout=10)
        if res.status_code == 200:
            data = res.json()
            for item in data:
                if 'lastFundingRate' in item:
                    global_funding[item['symbol']] = float(item['lastFundingRate'])
        logger.info(f"Loaded {len(global_funding)} global funding rates.")
    except Exception as e:
        logger.error(f"Failed to prefetch global funding: {e}")

def process_symbol(sym):
    funding_path = os.path.join(EXOTIC_DIR, f"{sym}_funding.parquet")
    metrics_path = os.path.join(EXOTIC_DIR, f"{sym}_metrics.parquet")

    # Determine whether exotic shards exist — kline-only assets skip funding/metrics
    has_exotic = os.path.exists(funding_path) and os.path.exists(metrics_path)

    current_ts = int(time.time() * 1000)
    funding_new = False
    metrics_new = False
    errors = []

    if has_exotic:
        funding_last_ts = (_sync.get("funding", sym) if _sync else None) or _get_last_ts_from_parquet(funding_path)
        metrics_last_ts = (_sync.get("metrics", sym) if _sync else None) or _get_last_ts_from_parquet(metrics_path)

        # --- FUNDING (Real historical settlement queries via Live API) ---
        if funding_last_ts and current_ts - funding_last_ts >= 3600000:
            url_fund = f"https://fapi.binance.com/fapi/v1/fundingRate?symbol={sym}&startTime={funding_last_ts + 1}&limit=1000"
            sess = get_session()
            try:
                res_fund = sess.get(url_fund, timeout=10)
                if res_fund.status_code == 200:
                    data_fund = res_fund.json()
                    if data_fund:
                        df_new_fund = pd.DataFrame(data_fund)
                        df_new_fund['timestamp'] = pd.to_numeric(df_new_fund['fundingTime'])
                        df_new_fund['funding_rate'] = pd.to_numeric(df_new_fund['fundingRate'])
                        df_new_fund['datetime'] = pd.to_datetime(df_new_fund['timestamp'], unit='ms')
                        resampled = df_new_fund.set_index('datetime')[['funding_rate']].resample('1h').ffill()
                        resampled['timestamp'] = resampled.index.astype('datetime64[ms]').astype('int64')
                        resampled = resampled.dropna(subset=['timestamp'])
                        resampled = drop_forming_hours(resampled, current_ts)

                        if not resampled.empty:
                            df = safe_read_parquet(funding_path, sym, "funding")
                            combined = pd.concat([df, resampled.reset_index(drop=True)])
                            combined = combined.drop_duplicates(subset=['timestamp'], keep='last').sort_values('timestamp')
                            combined.reset_index(drop=True).to_parquet(funding_path, index=False)

                            if _sync: _sync.set("funding", sym, int(combined['timestamp'].max()))
                            funding_new = True
                    elif current_ts - funding_last_ts >= 8 * 3600000:
                        # Fallback for delisted or dormant coins: forward fill from last known rate
                        dr = pd.date_range(start=pd.to_datetime(funding_last_ts, unit='ms'), end=pd.to_datetime(current_ts, unit='ms'), freq='1h')
                        if len(dr) > 1:
                            funding_val = global_funding.get(sym, 0.0)
                            df_new = pd.DataFrame({'datetime': dr})
                            df_new['funding_rate'] = funding_val
                            df_new['timestamp'] = df_new['datetime'].astype('datetime64[ms]').astype('int64')
                            df_new = drop_forming_hours(df_new, current_ts)
                            if not df_new.empty:
                                df = safe_read_parquet(funding_path, sym, "funding")
                                combined = pd.concat([df, df_new.drop(columns=['datetime'])])
                                combined = combined.drop_duplicates(subset=['timestamp'], keep='last').sort_values('timestamp')
                                combined.reset_index(drop=True).to_parquet(funding_path, index=False)
                                if _sync: _sync.set("funding", sym, int(combined['timestamp'].max()))
                                funding_new = True
            except Exception as e:
                errors.append(f"funding: {e}")
                logger.error("funding %s: %s", sym, e)

    # --- METRICS (2 fast API calls, Weight 2) ---
        if metrics_last_ts and current_ts - metrics_last_ts >= 3600000:
            url_oi = f"https://fapi.binance.com/futures/data/openInterestHist?symbol={sym}&period=1h&startTime={metrics_last_ts + 1}&limit=500"
            url_ls = f"https://fapi.binance.com/futures/data/topLongShortAccountRatio?symbol={sym}&period=1h&startTime={metrics_last_ts + 1}&limit=500"
            
            sess = get_session()
            try:
                res_oi = sess.get(url_oi, timeout=10)
                res_ls = sess.get(url_ls, timeout=10)
                
                if res_oi.status_code == 200 and res_ls.status_code == 200:
                    data_oi = res_oi.json()
                    data_ls = res_ls.json()
                    
                    if data_oi and data_ls:
                        df_oi = pd.DataFrame(data_oi)
                        df_ls = pd.DataFrame(data_ls)
                        df_oi['timestamp'] = pd.to_numeric(df_oi['timestamp'])
                        df_ls['timestamp'] = pd.to_numeric(df_ls['timestamp'])

                        merged = pd.merge(df_oi, df_ls, on='timestamp', how='inner')
                        if not merged.empty:
                            merged['sum_open_interest'] = pd.to_numeric(merged['sumOpenInterest'])
                            merged['sum_open_interest_value'] = pd.to_numeric(merged['sumOpenInterestValue'])
                            merged['count_toptrader_long_short_ratio'] = pd.to_numeric(merged['longShortRatio'])

                            new_df = merged[['timestamp', 'sum_open_interest', 'sum_open_interest_value', 'count_toptrader_long_short_ratio']]
                            new_df = drop_forming_hours(new_df, current_ts)
                            if not new_df.empty:
                                df = safe_read_parquet(metrics_path, sym, "metrics")
                                combined = pd.concat([df, new_df])
                                combined = combined.drop_duplicates(subset=['timestamp'], keep='last').sort_values('timestamp')
                                combined.reset_index(drop=True).to_parquet(metrics_path, index=False)

                                if _sync: _sync.set("metrics", sym, int(combined['timestamp'].max()))
                                metrics_new = True
            except Exception as e:
                errors.append(f"metrics: {e}")
                logger.error("metrics %s: %s", sym, e)


    # --- KLINES (1 fast API call, Weight 5) ---
    asset = sym.replace('USDT', '')
    kline_path = os.path.join(RAW_DIR, f"{asset}_USDT_1h.parquet")
    kline_new = False
    if os.path.exists(kline_path):
        kline_last_ts = (_sync.get("raw", sym) if _sync else None) or _get_last_ts_from_parquet(kline_path)
        if kline_last_ts and current_ts - kline_last_ts >= 3600000:
            gap_hours = (current_ts - kline_last_ts) / 3600000.0
            if gap_hours >= 24:
                logger.warning(f"[{sym}] Gap detected: {gap_hours:.1f} hours behind last kline.")
            url_kline = f"https://fapi.binance.com/fapi/v1/klines?symbol={sym}&interval=1h&startTime={kline_last_ts + 1}&limit=1500"
            sess = get_session()
            try:
                res_kline = sess.get(url_kline, timeout=10)
                if res_kline.status_code == 200:
                    data_kline = res_kline.json()
                    if data_kline:
                        cols = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_volume', 'count', 'taker_buy_base_volume', 'taker_buy_quote_volume', 'ignore']
                        df_kline = pd.DataFrame(data_kline, columns=cols)
                        for c in ['timestamp', 'close_time', 'count']:
                            df_kline[c] = pd.to_numeric(df_kline[c]).astype('int64')
                        for c in ['open', 'high', 'low', 'close', 'volume', 'quote_volume', 'taker_buy_base_volume', 'taker_buy_quote_volume']:
                            df_kline[c] = pd.to_numeric(df_kline[c]).astype('float64')
                        df_kline['ignore'] = df_kline['ignore'].astype(str)
                        df_kline['amount'] = df_kline['quote_volume']
                        # The last row is often the hour still printing. Do not store it.
                        df_kline = drop_forming_klines(df_kline, current_ts)
                        if not df_kline.empty:
                            df = safe_read_parquet(kline_path, sym, "kline")
                            combined = pd.concat([df, df_kline])
                            combined = combined.drop_duplicates(subset=['timestamp'], keep='last').sort_values('timestamp')
                            combined.reset_index(drop=True).to_parquet(kline_path, index=False)

                            if _sync: _sync.set("raw", sym, int(combined['timestamp'].max()))
                            kline_new = True
            except Exception as e:
                errors.append(f"kline: {e}")
                logger.error("kline %s: %s", sym, e)

    if funding_new or metrics_new or kline_new:
        return sym, True, "updated"
    if errors:
        return sym, False, "; ".join(errors)
    return sym, "uptodate", "already up to date"

def run_bridger():
    global _sync
    t_start = time.perf_counter()
    if SYNC_STATE_PATH.exists():
        _sync = SyncStateManager()
        logger.info(
            "Loaded sync_state.json (%s cached entries).",
            sum(_sync.total_symbols().values()),
        )
    else:
        logger.warning("sync_state.json missing at %s — building it from shards.", SYNC_STATE_PATH)
        _sync = build_sync_state(verbose=True)

    symbols = get_symbols()
    total = len(symbols)

    prefetch_global_funding()

    logger.info("Shard dirs: raw=%s exotic=%s", RAW_DIR, EXOTIC_DIR)
    logger.info("Bridging gap for %s symbols.", total)

    success = 0
    failed  = 0
    skipped = 0

    with ThreadPoolExecutor(max_workers=20) as pool:
        futures = {pool.submit(process_symbol, sym): sym for sym in symbols}
        for i, fut in enumerate(as_completed(futures), 1):
            sym, ok, reason = fut.result()

            if ok == "uptodate":
                skipped += 1
            elif ok:
                success += 1
            else:
                failed += 1

            if i % 100 == 0 or i == total:
                logger.info(f"Progress {i}/{total} | Updated={success} | UpToDate={skipped} | Failed={failed}")

    if _sync is not None:
        _sync.save()
        logger.info("sync_state.json updated.")
    elapsed = time.perf_counter() - t_start
    logger.info(f"Bridging Complete in {elapsed:.1f}s! Updated={success} UpToDate={skipped} Failed={failed}")
    return {"symbols": total, "updated": success, "uptodate": skipped, "failed": failed}


if __name__ == "__main__":
    run_bridger()
