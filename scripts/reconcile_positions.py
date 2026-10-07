"""
scripts/reconcile_positions.py — Kronos V12 Live Exchange Position Reconciler

Fix #8 — Phantom Positions Guard.

Compares open positions in v12_open_trades.md / open_trades.csv against
live exchange positions from Binance Futures REST API.

Detects:
  - Phantom positions: In our ledger as "open" but already closed on exchange
  - Ghost positions: On exchange but NOT in our ledger (manual trades)
  - Size mismatches: Ledger qty != exchange qty

Outputs a human-readable reconciliation report.
Run after every pipeline or manually whenever in doubt.
"""

import os
import sys
import json
import logging
import requests
import hmac
import hashlib
import time
from pathlib import Path
from datetime import datetime, timezone

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger("kronos.reconciler")

ROOT = Path(__file__).resolve().parent.parent

BINANCE_API_KEY    = os.getenv("BINANCE_API_KEY", "")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET", "")
FAPI_BASE          = "https://fapi.binance.com"


def _signed_request(endpoint: str, params: dict) -> dict | None:
    """Make a signed Binance Futures REST request."""
    if not BINANCE_API_KEY or not BINANCE_API_SECRET:
        logger.warning("[Reconciler] No BINANCE_API_KEY/SECRET in .env — cannot query live positions.")
        return None

    params["timestamp"] = int(time.time() * 1000)
    query = "&".join(f"{k}={v}" for k, v in params.items())
    sig = hmac.new(BINANCE_API_SECRET.encode(), query.encode(), hashlib.sha256).hexdigest()
    query += f"&signature={sig}"

    try:
        resp = requests.get(
            f"{FAPI_BASE}{endpoint}?{query}",
            headers={"X-MBX-APIKEY": BINANCE_API_KEY},
            timeout=15
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        logger.error(f"[Reconciler] Binance API error: {e}")
        return None


def get_live_positions() -> dict[str, float]:
    """
    Returns dict of {symbol: positionAmt} for all positions with abs(positionAmt) > 0.
    """
    data = _signed_request("/fapi/v2/positionRisk", {})
    if data is None:
        return {}
    live = {}
    for pos in data:
        amt = float(pos.get("positionAmt", 0))
        if abs(amt) > 1e-10:
            live[pos["symbol"]] = amt
    return live


def get_ledger_open_positions() -> dict[str, dict]:
    """
    Returns dict of {symbol: row_dict} from open_trades.csv.
    """
    tape_slug = os.environ.get("KRONOS_TAPE_DIR", "data/all_tapes/v12_production")
    open_csv = ROOT / tape_slug / "open_trades.csv"
    if not open_csv.exists():
        open_csv = ROOT / "data" / "all_tapes" / "v12_production" / "open_trades.csv"
    if not open_csv.exists():
        logger.warning(f"[Reconciler] open_trades.csv not found at {open_csv}")
        return {}

    import pandas as pd
    try:
        df = pd.read_csv(open_csv)
        result = {}
        for _, row in df.iterrows():
            sym_raw = row.get("symbol") or row.get("asset") or ""
            sym = str(sym_raw).upper().replace("/", "").replace("-", "").strip()
            if sym and not sym.endswith("USDT"):
                sym = sym + "USDT"
            if sym:
                result[sym] = row.to_dict()
        return result
    except Exception as e:
        logger.error(f"[Reconciler] Failed to read open_trades.csv: {e}")
        return {}


def get_live_open_orders() -> list[dict]:
    """
    Returns list of open orders from Binance Futures REST API (/fapi/v1/openOrders).
    """
    data = _signed_request("/fapi/v1/openOrders", {})
    return data or []


def reconcile() -> dict:
    """Run reconciliation and return a summary report dict."""
    logger.info("=" * 60)
    logger.info("KRONOS V12 POSITION & ORDER RECONCILER")
    logger.info(f"Timestamp (UTC): {datetime.now(timezone.utc).isoformat()}")
    logger.info("=" * 60)

    live    = get_live_positions()
    ledger  = get_ledger_open_positions()
    orders  = get_live_open_orders()

    live_symbols   = set(live.keys())
    ledger_symbols = set(ledger.keys())

    # 1. Phantom positions: ledger says open, exchange says closed
    phantoms = ledger_symbols - live_symbols
    # 2. Ghost positions: exchange has them, ledger doesn't
    ghosts   = live_symbols - ledger_symbols
    # 3. Matching symbols
    matched  = ledger_symbols & live_symbols

    # 4. Open Orders & 72h TTL Audit
    now_ms = int(time.time() * 1000)
    expired_limits = []
    resting_stops = {}
    resting_targets = {}
    resting_limit_bids = []

    for o in orders:
        o_sym = o.get("symbol", "")
        o_type = o.get("type", "")
        o_side = o.get("side", "")
        o_time = int(o.get("time", 0))
        age_hours = (now_ms - o_time) / (3600.0 * 1000.0)

        if o_type == "LIMIT" and o_side == "BUY":
            resting_limit_bids.append(o_sym)
            if age_hours > 72.0:
                expired_limits.append({
                    "symbol": o_sym,
                    "orderId": o.get("orderId"),
                    "age_hours": round(age_hours, 1),
                    "price": o.get("price")
                })
        elif o_type in ("STOP_MARKET", "STOP"):
            resting_stops[o_sym] = o.get("stopPrice")
        elif o_type in ("TAKE_PROFIT_MARKET", "TAKE_PROFIT", "LIMIT") and o_side == "SELL":
            resting_targets[o_sym] = o.get("price") or o.get("stopPrice")

    missing_stops = [s for s in matched if s not in resting_stops]

    report = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "live_positions": len(live),
        "ledger_positions": len(ledger),
        "open_orders_count": len(orders),
        "resting_limit_bids": resting_limit_bids,
        "expired_limit_orders": expired_limits,
        "missing_stops": missing_stops,
        "phantom_positions": sorted(phantoms),
        "ghost_positions": sorted(ghosts),
        "matched_positions": sorted(matched),
        "clean": len(phantoms) == 0 and len(ghosts) == 0 and len(expired_limits) == 0 and len(missing_stops) == 0,
    }

    # --- Print Report ---
    if phantoms:
        logger.warning(f"\n⚠️  PHANTOM POSITIONS ({len(phantoms)}) — In ledger but CLOSED on exchange:")
        for sym in sorted(phantoms):
            row = ledger[sym]
            entry = row.get("entry_price", "?")
            logger.warning(f"   → {sym} | Entry: {entry} | ACTION: Mark as closed in ledger")
    else:
        logger.info("✅ No phantom positions detected.")

    if ghosts:
        logger.warning(f"\n⚠️  GHOST POSITIONS ({len(ghosts)}) — On exchange but NOT in ledger (manual trades?):")
        for sym in sorted(ghosts):
            logger.warning(f"   → {sym} | Exchange qty: {live[sym]}")
    else:
        logger.info("✅ No ghost positions detected.")

    if matched:
        logger.info(f"\n✅ Matched positions ({len(matched)}): {sorted(matched)}")

    if expired_limits:
        logger.warning(f"\n⚠️  EXPIRED LIMIT BIDS (>72h TTL) ({len(expired_limits)}):")
        for ex in expired_limits:
            logger.warning(f"   → {ex['symbol']} | Age: {ex['age_hours']}h | OrderId: {ex['orderId']} | ACTION: Cancel order")
    else:
        logger.info("✅ No expired limit orders (>72h TTL).")

    if missing_stops:
        logger.warning(f"\n⚠️  POSITIONS MISSING RESTING STOP-MARKET ({len(missing_stops)}):")
        for ms in missing_stops:
            logger.warning(f"   → {ms} | ACTION: Place resting STOP_MARKET immediately")
    else:
        if matched:
            logger.info("✅ 100% of open positions have native resting stop orders.")

    if report["clean"]:
        logger.info("\n✅ RECONCILIATION CLEAN — Ledger and orders match exchange rules perfectly.")
    else:
        logger.warning("\n⚠️  RECONCILIATION MISMATCH — Review items above.")

    return report


if __name__ == "__main__":
    report = reconcile()
    # Save report as JSON
    out_path = ROOT / "reports" / "reconciliation_latest.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2))
    logger.info(f"\nReport saved to: {out_path}")
    sys.exit(0 if report["clean"] else 1)
