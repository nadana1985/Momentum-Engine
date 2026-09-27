"""REST gap-filler for 1h klines, funding and OI / long-short metrics.

Production hardening (2026-09-26):
  * Shards are written atomically (tmp file + os.replace). A crash mid-write
    can no longer truncate a shard and get it quarantined out of the universe.
  * Requests are paced per Binance rate-limit pool:
      - /futures/data/* (OI hist + top L/S ratio): 1000 req / 5 min / IP
      - /fapi/v1/fundingRate: 500 req / 5 min / IP (shared with fundingInfo)
      - everything else: 2400 request-weight / min / IP (klines weight 1-10)
    Defaults stay under those; override with V10_FUTDATA_RPS, V10_FUNDING_RPS,
    V10_KLINE_RPS.
  * Funding history is only requested once a new settlement has closed
    (from premiumIndex nextFundingTime + fundingInfo interval), instead of
    for every symbol every hour.
  * Metrics and klines paginate, so a multi-day outage is back-filled in one
    run (metrics history is only retained ~30 days by Binance).
  * HTTP 418 (IP ban) stops all further requests for the run.
"""
import os
import re
import sys
import glob
import threading
from pathlib import Path
import pandas as pd
import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = Path(__file__).resolve().parent.parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from config.ingestion.sync_state_manager import (
    SYNC_STATE_PATH,
    SyncStateManager,
    build_sync_state,
)
from momentum_v10.bar_clock import drop_forming_hours, drop_forming_klines
from momentum_v10.io_utils import RateLimiter, atomic_to_parquet
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from momentum_v10.logger import get_logger, quarantine_corrupted_shard

logger = get_logger("ingest")
data_logger = get_logger("data_quality")

BASE = os.environ.get("V10_BINANCE_BASE", "https://fapi.binance.com")
from momentum_v10.config import DATA_ROOT
EXOTIC_DIR = str(DATA_ROOT / "exotic_shards")
RAW_DIR = str(DATA_ROOT / "raw_shards")

HOUR_MS = 3_600_000
METRICS_PAGE = 500
METRICS_MAX_PAGES = 4          # 2000h > the ~720h Binance retains
KLINE_MAX_PAGES = 20

FUTDATA_LIMITER = RateLimiter(float(os.environ.get("V10_FUTDATA_RPS", "3.0")))
FUNDING_LIMITER = RateLimiter(float(os.environ.get("V10_FUNDING_RPS", "1.5")))
KLINE_LIMITER = RateLimiter(float(os.environ.get("V10_KLINE_RPS", "10")))

BANNED = threading.Event()

_sync = None

_session = None
_session_lock = threading.Lock()


class IpBannedError(RuntimeError):
    pass


def get_session():
    global _session
    with _session_lock:
        if _session is None:
            _session = requests.Session()
            retries = Retry(
                total=3,
                backoff_factor=1.0,
                status_forcelist=[429, 500, 502, 503, 504],
                respect_retry_after_header=True,
            )
            adapter = HTTPAdapter(max_retries=retries, pool_connections=50, pool_maxsize=50)
            _session.mount("https://", adapter)
            _session.mount("http://", adapter)
            _session.headers.update({"User-Agent": "Mozilla/5.0"})
    return _session


def api_get(path: str, params: dict, limiter: RateLimiter, timeout: float = 10):
    """Paced GET. Returns the Response. Raises IpBannedError after a 418."""
    if BANNED.is_set():
        raise IpBannedError("request skipped: IP banned earlier in this run")
    limiter.acquire()
    res = get_session().get(f"{BASE}{path}", params=params, timeout=timeout)
    if res.status_code == 418:
        BANNED.set()
        logger.critical("Binance returned 418 (IP ban). Halting all requests this run. Retry-After=%s",
                        res.headers.get("Retry-After"))
        raise IpBannedError("HTTP 418")
    if res.status_code == 451:
        BANNED.set()
        logger.critical("Binance returned 451 (restricted location). Host this job outside the US.")
        raise IpBannedError("HTTP 451")
    used = res.headers.get("X-MBX-USED-WEIGHT-1M")
    if used and used.isdigit() and int(used) > 2000:
        logger.warning("Request weight %s/2400 this minute; backing off 5s.", used)
        time.sleep(5)
    return res


VALID_SYMBOL = re.compile(r"^[A-Z0-9]+USDT$")


def get_symbols():
    # Primary: symbols with exotic shards (funding + metrics)
    exotic_syms = set(
        os.path.basename(f).replace("_funding.parquet", "")
        for f in glob.glob(os.path.join(EXOTIC_DIR, "*_funding.parquet"))
    )
    # Secondary: kline-only assets in raw_shards with NO exotic shard
    raw_syms = set(
        os.path.basename(f).replace("_USDT_1h.parquet", "") + "USDT"
        for f in glob.glob(os.path.join(RAW_DIR, "*_USDT_1h.parquet"))
    )
    kline_only = raw_syms - exotic_syms
    if kline_only:
        logger.info(f"Discovered {len(kline_only)} kline-only assets (no exotic shard) — klines will be gap-filled.")
    syms = exotic_syms | kline_only
    bad = sorted(s for s in syms if not VALID_SYMBOL.match(s))
    if bad:
        logger.warning(f"Skipping {len(bad)} shard(s) with unusable symbol names (mangled on save?): {bad}")
    return sorted(s for s in syms if VALID_SYMBOL.match(s))


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


def _append_shard(path: str, sym: str, shard_type: str, new: pd.DataFrame) -> int:
    """Merge new rows into a shard atomically. Returns the new max timestamp."""
    df = safe_read_parquet(path, sym, shard_type)
    combined = pd.concat([df, new]) if not df.empty else new.copy()
    combined = combined.drop_duplicates(subset=['timestamp'], keep='last').sort_values('timestamp')
    atomic_to_parquet(combined.reset_index(drop=True), path)
    return int(combined['timestamp'].max())


# Global funding caches
global_funding = {}
global_next_funding = {}
global_funding_interval_h = {}


def prefetch_global_funding():
    global global_funding, global_next_funding, global_funding_interval_h
    logger.info("Pre-fetching global funding rates and schedules...")
    try:
        res = api_get("/fapi/v1/premiumIndex", {}, KLINE_LIMITER)
        if res.status_code == 200:
            for item in res.json():
                sym = item.get('symbol')
                if not sym:
                    continue
                if 'lastFundingRate' in item and item['lastFundingRate'] not in (None, ""):
                    global_funding[sym] = float(item['lastFundingRate'])
                nft = item.get('nextFundingTime')
                if nft:
                    global_next_funding[sym] = int(nft)
        logger.info(f"Loaded {len(global_funding)} funding rates, {len(global_next_funding)} schedules.")
    except IpBannedError:
        raise
    except Exception as e:
        logger.error(f"Failed to prefetch global funding: {e}")
    try:
        res = api_get("/fapi/v1/fundingInfo", {}, FUNDING_LIMITER)
        if res.status_code == 200:
            for item in res.json():
                if item.get('symbol') and item.get('fundingIntervalHours'):
                    global_funding_interval_h[item['symbol']] = int(item['fundingIntervalHours'])
        logger.info(f"Loaded {len(global_funding_interval_h)} non-default funding intervals.")
    except IpBannedError:
        raise
    except Exception as e:
        logger.warning(f"fundingInfo unavailable, assuming 8h intervals: {e}")


def funding_call_needed(sym: str, funding_last_ts: int, current_ts: int) -> bool:
    """True when a settlement newer than the shard has closed its 1h bucket.

    Symbols missing from premiumIndex (delisted / dormant) keep the old
    behaviour: poll hourly, forward-fill after 8h of silence.
    """
    if current_ts - funding_last_ts < HOUR_MS:
        return False
    nxt = global_next_funding.get(sym)
    if not nxt:
        return True
    interval_ms = global_funding_interval_h.get(sym, 8) * HOUR_MS
    last_settlement = nxt - interval_ms
    while last_settlement > current_ts:        # stale nextFundingTime guard
        last_settlement -= interval_ms
    last_settlement_bucket = last_settlement - (last_settlement % HOUR_MS)
    if funding_last_ts >= last_settlement_bucket:
        return False
    # An older settlement is missing (e.g. after an outage): fetch it now.
    if funding_last_ts < last_settlement_bucket - interval_ms:
        return True
    # Only the newest is missing: its 1h bucket must have closed, or
    # drop_forming_hours would discard it and the call is wasted.
    return current_ts >= last_settlement_bucket + HOUR_MS


def _update_funding(sym, funding_path, funding_last_ts, current_ts):
    res_fund = api_get("/fapi/v1/fundingRate",
                       {"symbol": sym, "startTime": funding_last_ts + 1, "limit": 1000},
                       FUNDING_LIMITER)
    if res_fund.status_code != 200:
        raise RuntimeError(f"HTTP {res_fund.status_code} {res_fund.text[:160]}")
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
            last = _append_shard(funding_path, sym, "funding", resampled.reset_index(drop=True))
            if _sync: _sync.set("funding", sym, last)
            return True
    elif current_ts - funding_last_ts >= 8 * HOUR_MS:
        # Fallback for delisted or dormant coins: forward fill from last known rate
        dr = pd.date_range(start=pd.to_datetime(funding_last_ts, unit='ms'),
                           end=pd.to_datetime(current_ts, unit='ms'), freq='1h')
        if len(dr) > 1:
            funding_val = global_funding.get(sym, 0.0)
            df_new = pd.DataFrame({'datetime': dr})
            df_new['funding_rate'] = funding_val
            df_new['timestamp'] = df_new['datetime'].astype('datetime64[ms]').astype('int64')
            df_new = drop_forming_hours(df_new, current_ts)
            if not df_new.empty:
                last = _append_shard(funding_path, sym, "funding", df_new.drop(columns=['datetime']))
                if _sync: _sync.set("funding", sym, last)
                return True
    return False


def _fetch_metrics_pages(sym, start_ts, current_ts):
    """Page OI hist + top L/S ratio forward from start_ts. Returns merged frame."""
    frames = []
    cursor = start_ts
    for _ in range(METRICS_MAX_PAGES):
        params = {"symbol": sym, "period": "1h", "startTime": cursor + 1, "limit": METRICS_PAGE}
        res_oi = api_get("/futures/data/openInterestHist", params, FUTDATA_LIMITER)
        res_ls = api_get("/futures/data/topLongShortAccountRatio", params, FUTDATA_LIMITER)
        if res_oi.status_code != 200 or res_ls.status_code != 200:
            bad = res_oi if res_oi.status_code != 200 else res_ls
            raise RuntimeError(f"HTTP oi={res_oi.status_code} ls={res_ls.status_code} {bad.text[:160]}")
        data_oi, data_ls = res_oi.json(), res_ls.json()
        if not data_oi or not data_ls:
            break
        df_oi = pd.DataFrame(data_oi)
        df_ls = pd.DataFrame(data_ls)
        df_oi['timestamp'] = pd.to_numeric(df_oi['timestamp'])
        df_ls['timestamp'] = pd.to_numeric(df_ls['timestamp'])
        merged = pd.merge(df_oi, df_ls, on='timestamp', how='inner')
        if not merged.empty:
            frames.append(merged)
        page_max = int(max(df_oi['timestamp'].max(), df_ls['timestamp'].max()))
        if (len(data_oi) < METRICS_PAGE and len(data_ls) < METRICS_PAGE) or page_max <= cursor \
                or page_max + HOUR_MS >= current_ts:
            break
        cursor = page_max
    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index=True)


def _update_metrics(sym, metrics_path, metrics_last_ts, current_ts):
    merged = _fetch_metrics_pages(sym, metrics_last_ts, current_ts)
    if merged.empty:
        return False
    merged['sum_open_interest'] = pd.to_numeric(merged['sumOpenInterest'])
    merged['sum_open_interest_value'] = pd.to_numeric(merged['sumOpenInterestValue'])
    merged['count_toptrader_long_short_ratio'] = pd.to_numeric(merged['longShortRatio'])
    new_df = merged[['timestamp', 'sum_open_interest', 'sum_open_interest_value', 'count_toptrader_long_short_ratio']]
    new_df = drop_forming_hours(new_df, current_ts)
    if new_df.empty:
        return False
    last = _append_shard(metrics_path, sym, "metrics", new_df)
    if _sync: _sync.set("metrics", sym, last)
    return True


KLINE_COLS = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_volume',
              'count', 'taker_buy_base_volume', 'taker_buy_quote_volume', 'ignore']


def _kline_limit(gap_hours: float) -> int:
    # Binance weight: 1 for <100, 2 for <500, 5 for <=1000, 10 for >1000
    need = int(gap_hours) + 2
    if need < 100:
        return 99
    if need < 500:
        return 499
    return 1000


def _update_klines(sym, kline_path, kline_last_ts, current_ts):
    gap_hours = (current_ts - kline_last_ts) / HOUR_MS
    if gap_hours >= 24:
        logger.warning(f"[{sym}] Gap detected: {gap_hours:.1f} hours behind last kline.")
    limit = _kline_limit(gap_hours)
    rows = []
    cursor = kline_last_ts
    for _ in range(KLINE_MAX_PAGES):
        res = api_get("/fapi/v1/klines",
                      {"symbol": sym, "interval": "1h", "startTime": cursor + 1, "limit": limit},
                      KLINE_LIMITER)
        if res.status_code != 200:
            raise RuntimeError(f"HTTP {res.status_code} {res.text[:160]}")
        page = res.json()
        if not page:
            break
        rows.extend(page)
        page_max = int(page[-1][0])
        if len(page) < limit or page_max <= cursor or page_max + HOUR_MS >= current_ts:
            break
        cursor = page_max
    if not rows:
        return False
    df_kline = pd.DataFrame(rows, columns=KLINE_COLS)
    for c in ['timestamp', 'close_time', 'count']:
        df_kline[c] = pd.to_numeric(df_kline[c]).astype('int64')
    for c in ['open', 'high', 'low', 'close', 'volume', 'quote_volume', 'taker_buy_base_volume', 'taker_buy_quote_volume']:
        df_kline[c] = pd.to_numeric(df_kline[c]).astype('float64')
    df_kline['ignore'] = df_kline['ignore'].astype(str)
    df_kline['amount'] = df_kline['quote_volume']
    # The last row is often the hour still printing. Do not store it.
    df_kline = drop_forming_klines(df_kline, current_ts)
    if df_kline.empty:
        return False
    last = _append_shard(kline_path, sym, "kline", df_kline)
    if _sync: _sync.set("raw", sym, last)
    return True


def process_symbol(sym):
    funding_path = os.path.join(EXOTIC_DIR, f"{sym}_funding.parquet")
    metrics_path = os.path.join(EXOTIC_DIR, f"{sym}_metrics.parquet")
    has_exotic = os.path.exists(funding_path) and os.path.exists(metrics_path)

    current_ts = int(time.time() * 1000)
    updated = False
    errors = []

    if BANNED.is_set():
        return sym, False, "skipped: IP banned this run"

    # Delisted contracts: Binance rejects their OI/L-S/funding requests (HTTP 400)
    # every hour. Skip those calls once premiumIndex (the live-contract list) is
    # loaded; never forward-fill made-up funding for them. Klines still run for
    # any raw shard, so a live asset missing from premiumIndex stays fresh.
    listed = (not global_next_funding) or sym in global_next_funding
    asset_kline = os.path.join(RAW_DIR, f"{sym.replace('USDT', '')}_USDT_1h.parquet")
    if not listed and not os.path.exists(asset_kline):
        return sym, "delisted", "not listed on Binance futures"

    if has_exotic and listed:
        funding_last_ts = (_sync.get("funding", sym) if _sync else None) or _get_last_ts_from_parquet(funding_path)
        metrics_last_ts = (_sync.get("metrics", sym) if _sync else None) or _get_last_ts_from_parquet(metrics_path)

        if funding_last_ts and funding_call_needed(sym, funding_last_ts, current_ts):
            try:
                updated |= _update_funding(sym, funding_path, funding_last_ts, current_ts)
            except Exception as e:
                errors.append(f"funding: {e}")
                logger.error("funding %s: %s", sym, e)

        if metrics_last_ts and current_ts - metrics_last_ts >= 2 * HOUR_MS:
            # >= 2h: the bar at last+1h must have closed before it is storable
            try:
                updated |= _update_metrics(sym, metrics_path, metrics_last_ts, current_ts)
            except Exception as e:
                errors.append(f"metrics: {e}")
                logger.error("metrics %s: %s", sym, e)

    asset = sym.replace('USDT', '')
    kline_path = os.path.join(RAW_DIR, f"{asset}_USDT_1h.parquet")
    if os.path.exists(kline_path):
        kline_last_ts = (_sync.get("raw", sym) if _sync else None) or _get_last_ts_from_parquet(kline_path)
        if kline_last_ts and current_ts - kline_last_ts >= 2 * HOUR_MS:
            try:
                updated |= _update_klines(sym, kline_path, kline_last_ts, current_ts)
            except Exception as e:
                errors.append(f"kline: {e}")
                logger.error("kline %s: %s", sym, e)

    if errors:
        return sym, False, "; ".join(errors)
    if updated:
        return sym, True, "updated"
    return sym, "uptodate", "already up to date"


def run_bridger():
    global _sync
    t_start = time.perf_counter()
    BANNED.clear()
    # Temp files orphaned by a hard kill (atomic writes never expose them).
    for d in (RAW_DIR, EXOTIC_DIR):
        for tmp in glob.glob(os.path.join(d, ".*.tmp")):
            try:
                os.remove(tmp)
                logger.warning("Removed orphaned temp file %s", tmp)
            except OSError:
                pass
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
    failed = 0
    skipped = 0
    delisted = 0

    with ThreadPoolExecutor(max_workers=20) as pool:
        futures = {pool.submit(process_symbol, sym): sym for sym in symbols}
        for i, fut in enumerate(as_completed(futures), 1):
            sym, ok, reason = fut.result()

            if ok == "delisted":
                delisted += 1
            elif ok == "uptodate":
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
    logger.info(f"Bridging Complete in {elapsed:.1f}s! Updated={success} UpToDate={skipped} "
                f"Delisted(skipped)={delisted} Failed={failed}")
    return {"symbols": total, "updated": success, "uptodate": skipped, "failed": failed, "delisted": delisted,
            "banned": BANNED.is_set(), "elapsed_s": round(elapsed, 1)}


if __name__ == "__main__":
    run_bridger()
