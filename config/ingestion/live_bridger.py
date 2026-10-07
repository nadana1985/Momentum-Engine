import os
import sys
import glob
from pathlib import Path
import pandas as pd
import requests
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging

ROOT = Path(__file__).resolve().parent.parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from config.ingestion.sync_state_manager import SyncStateManager, SYNC_STATE_PATH
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')
logger = logging.getLogger("kronos.bridger")

EXOTIC_DIR = str(ROOT / "data" / "exotic_shards")
RAW_DIR = str(ROOT / "data" / "raw_shards")

if SYNC_STATE_PATH.exists():
    _sync = SyncStateManager()
    logger.info(f"Loaded sync_state.json ({sum(_sync.total_symbols().values())} cached entries).")
else:
    logger.warning("sync_state.json not found. Run sync_state_manager --build first.")
    _sync = None

_thread_local = threading.local()

def get_session():
    if not hasattr(_thread_local, "session"):
        s = requests.Session()
        retries = Retry(total=3, backoff_factor=1.0, status_forcelist=[429, 500, 502, 503, 504])
        adapter = HTTPAdapter(max_retries=retries, pool_connections=10, pool_maxsize=10)
        s.mount("https://", adapter)
        s.headers.update({"User-Agent": "Mozilla/5.0"})
        _thread_local.session = s
    return _thread_local.session


# ---------------------------------------------------------------------------
# Rate Limiter & Atomic Parquet Writer
# ---------------------------------------------------------------------------

class RateLimiter:
    """
    Thread-safe Token Bucket rate limiter.
    Ensures that burst API requests do not trigger Binance HTTP 429 errors.
    Binance limit for futures metrics (OI + L/S) is 1,000 req / 5 min per IP.
    3.0 req/sec = 900 req / 5 min (safely within the limit).
    """
    def __init__(self, max_per_second: float = 3.0):
        self.interval = 1.0 / max_per_second
        self.lock = threading.Lock()
        self.last_called = 0.0

    def wait(self):
        with self.lock:
            now = time.time()
            elapsed = now - self.last_called
            if elapsed < self.interval:
                time.sleep(self.interval - elapsed)
            self.last_called = time.time()

metrics_limiter = RateLimiter(max_per_second=3.0)

BANNED = threading.Event()


class IpBannedError(RuntimeError):
    """Raised when Binance returns HTTP 418 (IP ban) or 451 (geo-blocked)."""
    pass


def api_get(url: str, params: dict | None = None, limiter: RateLimiter | None = None, timeout: float = 10):
    """
    Paced and circuit-broken HTTP GET request.
    If an IP ban (418) or restriction (451) is encountered, trips the global BANNED event
    and immediately halts all subsequent requests across all worker threads.
    """
    if BANNED.is_set():
        raise IpBannedError("Request skipped: Binance IP ban (418) or restriction (451) active.")
    if limiter:
        limiter.wait()
    sess = get_session()
    res = sess.get(url, params=params, timeout=timeout)
    if res.status_code == 418:
        BANNED.set()
        retry_after = res.headers.get("Retry-After", "unknown")
        logger.critical(f"Binance returned HTTP 418 (IP Ban)! Halting all requests for this run. Retry-After: {retry_after}")
        raise IpBannedError(f"HTTP 418 IP Ban (Retry-After: {retry_after})")
    if res.status_code == 451:
        BANNED.set()
        logger.critical("Binance returned HTTP 451 (Restricted Location)! Host this job outside the US.")
        raise IpBannedError("HTTP 451 Restricted Location")
    return res


def atomic_to_parquet(df: pd.DataFrame, target_path: str):
    """
    Writes DataFrame to a temporary file first, then atomically replaces
    the target file via os.replace. Prevents corrupted or truncated zero-byte shards
    if the host restarts, sleeps, or process terminates mid-write.
    """
    tmp_path = f"{target_path}.tmp.{os.getpid()}.{time.time_ns()}"
    try:
        df.to_parquet(tmp_path, index=False)
        os.replace(tmp_path, target_path)
    except Exception as e:
        if os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except OSError:
                pass
        raise e


def get_symbols():
    exotic_syms = set(
        os.path.basename(f).replace("_funding.parquet", "")
        for f in glob.glob(os.path.join(EXOTIC_DIR, "*_funding.parquet"))
    )
    raw_syms = set(
        os.path.basename(f).replace("_USDT_1h.parquet", "") + "USDT"
        for f in glob.glob(os.path.join(RAW_DIR, "*_USDT_1h.parquet"))
    )
    kline_only = raw_syms - exotic_syms
    if kline_only:
        logger.info(f"Discovered {len(kline_only)} kline-only assets (no exotic shard) — klines will be gap-filled.")
    return sorted(exotic_syms | kline_only)


def _get_last_ts_from_parquet(path):
    try:
        df = pd.read_parquet(path, columns=['timestamp'])
        if df.empty: return None
        return int(df['timestamp'].max())
    except:
        return None


# Global caches for funding rates and settlement schedule
global_funding = {}
global_next_funding_time = {}

def prefetch_global_funding():
    global global_funding, global_next_funding_time
    logger.info("Pre-fetching global funding rates & settlement schedule (Weight: 1)...")
    try:
        res = api_get("https://fapi.binance.com/fapi/v1/premiumIndex", timeout=10)
        if res.status_code == 200:
            data = res.json()
            for item in data:
                s = item.get('symbol')
                if not s:
                    continue
                if 'lastFundingRate' in item:
                    global_funding[s] = float(item['lastFundingRate'])
                if 'nextFundingTime' in item:
                    global_next_funding_time[s] = int(item['nextFundingTime'])
        logger.info(f"Loaded {len(global_funding)} global funding rates & next funding times.")
    except IpBannedError as e:
        logger.critical(f"Aborting funding prefetch: {e}")
    except Exception as e:
        logger.error(f"Failed to prefetch global funding: {e}")


def process_symbol(sym):
    if BANNED.is_set():
        return sym, False, "banned"

    funding_path = os.path.join(EXOTIC_DIR, f"{sym}_funding.parquet")
    metrics_path = os.path.join(EXOTIC_DIR, f"{sym}_metrics.parquet")

    has_exotic = os.path.exists(funding_path) and os.path.exists(metrics_path)

    current_ts = int(time.time() * 1000)
    funding_new = False
    metrics_new = False

    if has_exotic:
        funding_last_ts = (_sync.get("funding", sym) if _sync else None) or _get_last_ts_from_parquet(funding_path)
        metrics_last_ts = (_sync.get("metrics", sym) if _sync else None) or _get_last_ts_from_parquet(metrics_path)

        # --- 1. FUNDING (Only query API if settlement has passed) ---
        next_ft = global_next_funding_time.get(sym, 0)
        # Funding settles every 8h (or 4h). If current_ts < next_ft, the latest settlement is (next_ft - 8h)
        settlement_due = (current_ts >= next_ft) or (funding_last_ts is not None and funding_last_ts < next_ft - 8 * 3600000)

        if settlement_due and (funding_last_ts is None or current_ts - funding_last_ts >= 3600000):
            url_fund = f"https://fapi.binance.com/fapi/v1/fundingRate?symbol={sym}&startTime={funding_last_ts + 1}&limit=1000"
            try:
                res_fund = api_get(url_fund, timeout=10)
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

                        df = pd.read_parquet(funding_path)
                        combined = pd.concat([df, resampled.reset_index(drop=True)])
                        combined = combined.drop_duplicates(subset=['timestamp'], keep='last').sort_values('timestamp')
                        atomic_to_parquet(combined.reset_index(drop=True), funding_path)

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
                            df = pd.read_parquet(funding_path)
                            combined = pd.concat([df, df_new.drop(columns=['datetime'])])
                            combined = combined.drop_duplicates(subset=['timestamp'], keep='last').sort_values('timestamp')
                            atomic_to_parquet(combined.reset_index(drop=True), funding_path)
                            if _sync: _sync.set("funding", sym, int(combined['timestamp'].max()))
                            funding_new = True
            except IpBannedError:
                return sym, False, "banned"
            except Exception:
                pass

        # --- 2. METRICS (OI and L/S: Throttled at 3 req/sec + Paginated up to current_ts) ---
        if metrics_last_ts and current_ts - metrics_last_ts >= 3600000:
            if current_ts - metrics_last_ts > 30 * 24 * 3600000:
                logger.warning(f"[{sym}] Gap > 30 days ({int((current_ts - metrics_last_ts)/(24*3600000))}d). Binance derivatives older than 30d are unfillable.")

            curr_start = metrics_last_ts + 1
            pages_fetched = 0
            all_new_metrics = []

            while curr_start < current_ts - 3600000 and pages_fetched < 10:
                url_oi = f"https://fapi.binance.com/futures/data/openInterestHist?symbol={sym}&period=1h&startTime={curr_start}&limit=500"
                url_ls = f"https://fapi.binance.com/futures/data/topLongShortAccountRatio?symbol={sym}&period=1h&startTime={curr_start}&limit=500"

                try:
                    res_oi = api_get(url_oi, limiter=metrics_limiter, timeout=10)
                    res_ls = api_get(url_ls, limiter=metrics_limiter, timeout=10)

                    if res_oi.status_code == 200 and res_ls.status_code == 200:
                        data_oi = res_oi.json()
                        data_ls = res_ls.json()

                        if not data_oi or not data_ls:
                            break

                        df_oi = pd.DataFrame(data_oi)
                        df_ls = pd.DataFrame(data_ls)
                        df_oi['timestamp'] = pd.to_numeric(df_oi['timestamp'])
                        df_ls['timestamp'] = pd.to_numeric(df_ls['timestamp'])

                        merged = pd.merge(df_oi, df_ls, on='timestamp', how='inner')
                        if merged.empty:
                            break

                        merged['sum_open_interest'] = pd.to_numeric(merged['sumOpenInterest'])
                        merged['sum_open_interest_value'] = pd.to_numeric(merged['sumOpenInterestValue'])
                        merged['count_toptrader_long_short_ratio'] = pd.to_numeric(merged['longShortRatio'])

                        new_df = merged[['timestamp', 'sum_open_interest', 'sum_open_interest_value', 'count_toptrader_long_short_ratio']]
                        all_new_metrics.append(new_df)

                        max_batch_ts = int(new_df['timestamp'].max())
                        if max_batch_ts <= curr_start:
                            break
                        curr_start = max_batch_ts + 1
                        pages_fetched += 1

                        if len(data_oi) < 500:
                            break
                    else:
                        break
                except IpBannedError:
                    return sym, False, "banned"
                except Exception as e:
                    break

            if all_new_metrics:
                concatenated_new = pd.concat(all_new_metrics)
                df = pd.read_parquet(metrics_path)
                combined = pd.concat([df, concatenated_new])
                combined = combined.drop_duplicates(subset=['timestamp'], keep='last').sort_values('timestamp')
                atomic_to_parquet(combined.reset_index(drop=True), metrics_path)

                if _sync: _sync.set("metrics", sym, int(combined['timestamp'].max()))
                metrics_new = True

    # --- 3. KLINES (1 fast API call, Weight 5) ---
    asset = sym.replace('USDT', '')
    kline_path = os.path.join(RAW_DIR, f"{asset}_USDT_1h.parquet")
    kline_new = False
    if os.path.exists(kline_path):
        kline_last_ts = (_sync.get("raw", sym) if _sync else None) or _get_last_ts_from_parquet(kline_path)
        if kline_last_ts and current_ts - kline_last_ts >= 3600000:
            url_kline = f"https://fapi.binance.com/fapi/v1/klines?symbol={sym}&interval=1h&startTime={kline_last_ts + 1}&limit=1500"
            try:
                res_kline = api_get(url_kline, timeout=10)
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

                        # Strict firewall: filter out unclosed in-progress candles
                        df_kline = df_kline[df_kline['close_time'] <= current_ts]
                        if not df_kline.empty:
                            df = pd.read_parquet(kline_path)
                            combined = pd.concat([df, df_kline])
                            combined = combined.drop_duplicates(subset=['timestamp'], keep='last').sort_values('timestamp')
                            atomic_to_parquet(combined.reset_index(drop=True), kline_path)

                            if _sync: _sync.set("raw", sym, int(combined['timestamp'].max()))
                            kline_new = True
            except IpBannedError:
                return sym, False, "banned"
            except Exception:
                pass

    if funding_new or metrics_new or kline_new:
        return sym, True, "updated"
    else:
        return sym, "uptodate", "already up to date"


def run_bridger():
    symbols = get_symbols()
    total = len(symbols)

    prefetch_global_funding()
    if BANNED.is_set():
        logger.critical("Aborting live ingestion: Binance IP ban (418) or geo-block (451) triggered during prefetch.")
        return

    logger.info(f"Bridging gap for {total} active symbols via Hyper-Fast Bulk REST API...")
    logger.info("Workers: 10 | Token-Bucket Paced (3 req/sec metrics limiter) | Atomic Parquet Enabled")

    success = 0
    failed  = 0
    skipped = 0

    with ThreadPoolExecutor(max_workers=10) as pool:
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
    logger.info("Bridging Complete!")


if __name__ == "__main__":
    run_bridger()
