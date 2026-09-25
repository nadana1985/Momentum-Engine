"""
sync_state_manager.py — Unified sync state cache for Kronos V1-Alt ingestion.

Maintains a single `data/sync_state.json` file that stores the last known
timestamp for all three shard types:
  - raw_shards   (Klines, from unified_ingestion_engine.py)
  - funding      (Funding Rates, from binance_vision_scraper.py + live_bridger.py)
  - metrics      (OI + L/S Ratio, from binance_vision_scraper.py + live_bridger.py)

This eliminates the need to open 2,249 Parquet files on every ingestion run
just to discover the last timestamp. Instead, the engine reads/writes this
single JSON file.

Usage:
    # Build the initial index from scratch (run once):
    python -m config.ingestion.sync_state_manager --build

    # Read last timestamp for a symbol:
    from config.ingestion.sync_state_manager import SyncStateManager
    mgr = SyncStateManager()
    ts = mgr.get("raw", "BTC_USDT")

    # Write updated timestamp after a successful append:
    mgr.set("raw", "BTC_USDT", 1788915600000)
    mgr.save()
"""
from __future__ import annotations

import glob
import json
import os
import time
from pathlib import Path

import pandas as pd

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent.parent   # package root (this repo)
SYNC_STATE_PATH = ROOT / "data" / "sync_state.json"

RAW_DIR     = ROOT / "data" / "raw_shards"
EXOTIC_DIR  = ROOT / "data" / "exotic_shards"


# ---------------------------------------------------------------------------
# Manager
# ---------------------------------------------------------------------------

class SyncStateManager:
    """
    In-memory sync state cache backed by a single JSON file.

    Schema:
    {
        "raw":     { "BTC_USDT": 1788915600000, ... },
        "funding": { "BTCUSDT":  1788912000000, ... },
        "metrics": { "BTCUSDT":  1788922800000, ... },
        "_meta":   { "built_at": "...", "total_symbols": N }
    }
    """

    VALID_TYPES = ("raw", "funding", "metrics")

    def __init__(self, path: Path = SYNC_STATE_PATH):
        self.path = path
        self._state: dict = {}
        self._dirty = False
        if path.exists():
            self._load()
        else:
            self._state = {"raw": {}, "funding": {}, "metrics": {}, "_meta": {}}

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _load(self):
        with open(self.path, "r") as f:
            self._state = json.load(f)
        # Ensure all keys exist
        for t in self.VALID_TYPES:
            self._state.setdefault(t, {})
        self._state.setdefault("_meta", {})

    def save(self):
        """Atomically write state to disk."""
        if not self._dirty:
            return
        tmp = self.path.with_suffix(".tmp")
        with open(tmp, "w") as f:
            json.dump(self._state, f)
        tmp.replace(self.path)
        self._dirty = False

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def _normalize_key(self, shard_type: str, symbol: str) -> tuple[str, str]:
        st = "raw" if shard_type in ("raw", "klines") else shard_type
        bucket = self._state.get(st, {})
        if symbol in bucket:
            return st, symbol
        if "_" in symbol:
            alt = symbol.replace("_", "")
        elif symbol.endswith("USDT"):
            alt = symbol[:-4] + "_USDT"
        else:
            alt = symbol
        if alt in bucket:
            return st, alt
        return st, symbol

    def get(self, shard_type: str, symbol: str) -> int | None:
        """Return cached last timestamp (ms) or None if not found."""
        st, sym = self._normalize_key(shard_type, symbol)
        return self._state.get(st, {}).get(sym)

    def set(self, shard_type: str, symbol: str, last_ts: int):
        """Update last timestamp for a symbol. Call save() to persist."""
        st, sym = self._normalize_key(shard_type, symbol)
        assert st in self.VALID_TYPES, f"Invalid type: {shard_type}"
        bucket = self._state.setdefault(st, {})
        prev = bucket.get(sym)
        if prev != last_ts:
            bucket[sym] = last_ts
            self._dirty = True

    def total_symbols(self) -> dict:
        return {t: len(self._state.get(t, {})) for t in self.VALID_TYPES}


# ---------------------------------------------------------------------------
# Builder — reads all Parquet files ONCE to populate the index
# ---------------------------------------------------------------------------

def build_sync_state(verbose: bool = True) -> SyncStateManager:
    """
    Scan all existing Parquet shards and build the sync_state.json from
    scratch. Run this once after setup, or to repair a corrupted index.
    """
    mgr = SyncStateManager.__new__(SyncStateManager)
    mgr.path = SYNC_STATE_PATH
    mgr._state = {"raw": {}, "funding": {}, "metrics": {}, "_meta": {}}
    mgr._dirty = True

    start = time.time()

    # --- Raw shards ---
    raw_files = sorted(RAW_DIR.glob("*_USDT_1h.parquet"))
    if verbose:
        print(f"\n[RAW] Scanning {len(raw_files)} raw shards...")
    for f in raw_files:
        sym = f.name.replace("_1h.parquet", "")   # e.g. BTC_USDT
        try:
            df = pd.read_parquet(f, columns=["timestamp"])
            ts = int(df["timestamp"].max())
            mgr._state["raw"][sym] = ts
        except Exception as e:
            if verbose:
                print(f"  WARN {f.name}: {e}")

    # --- Funding shards ---
    funding_files = sorted(EXOTIC_DIR.glob("*_funding.parquet"))
    if verbose:
        print(f"[FUNDING] Scanning {len(funding_files)} funding shards...")
    for f in funding_files:
        sym = f.name.replace("_funding.parquet", "")   # e.g. BTCUSDT
        try:
            df = pd.read_parquet(f, columns=["timestamp"])
            ts = int(df["timestamp"].max())
            mgr._state["funding"][sym] = ts
        except Exception as e:
            if verbose:
                print(f"  WARN {f.name}: {e}")

    # --- Metrics shards ---
    metrics_files = sorted(EXOTIC_DIR.glob("*_metrics.parquet"))
    if verbose:
        print(f"[METRICS] Scanning {len(metrics_files)} metrics shards...")
    for f in metrics_files:
        sym = f.name.replace("_metrics.parquet", "")   # e.g. BTCUSDT
        try:
            df = pd.read_parquet(f, columns=["timestamp"])
            ts = int(df["timestamp"].max())
            mgr._state["metrics"][sym] = ts
        except Exception as e:
            if verbose:
                print(f"  WARN {f.name}: {e}")

    elapsed = time.time() - start
    total = sum(mgr.total_symbols().values())
    mgr._state["_meta"] = {
        "built_at": pd.Timestamp.now('UTC').isoformat(),
        "total_symbols": total,
        "build_time_s": round(elapsed, 2),
    }

    mgr.save()

    if verbose:
        print(f"\n[DONE] sync_state.json built in {elapsed:.1f}s")
        print(f"   Raw:     {mgr.total_symbols()['raw']} symbols")
        print(f"   Funding: {mgr.total_symbols()['funding']} symbols")
        print(f"   Metrics: {mgr.total_symbols()['metrics']} symbols")
        print(f"   Saved -> {SYNC_STATE_PATH}")

    return mgr


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Kronos Sync State Manager")
    parser.add_argument("--build", action="store_true", help="Build sync_state.json from scratch by scanning all Parquet files")
    parser.add_argument("--show", metavar="SYMBOL", help="Show cached timestamps for a symbol prefix (e.g. BTC)")
    args = parser.parse_args()

    if args.build:
        build_sync_state(verbose=True)

    elif args.show:
        mgr = SyncStateManager()
        sym = args.show.upper()
        found = False
        for t in SyncStateManager.VALID_TYPES:
            for k, v in mgr._state[t].items():
                if sym in k:
                    ts = pd.Timestamp(v, unit="ms", tz="UTC")
                    print(f"  [{t:8s}] {k}: {v}  ({ts})")
                    found = True
        if not found:
            print(f"No cached entries found matching '{sym}'")

    else:
        parser.print_help()
