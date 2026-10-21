"""
Paper vs live resting-limit fill model (Momentum V15).

This is not an exchange order placer. Paper replay fills a buy limit at the
bid whenever the bar low trades through. Live replay fills a gap-through at
the open (the bid is not available after a gap).

KRONOS_EXECUTION=live | live_limit  -> live_limit
anything else (default)             -> paper_limit
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

from momentum_v15.config import ExecutionConfig


def execution_from_env() -> ExecutionConfig:
    raw = os.environ.get("KRONOS_EXECUTION", "paper").strip().lower()
    if raw in ("live", "live_limit"):
        return ExecutionConfig(mode="live_limit")
    return ExecutionConfig(mode="paper_limit")


def limit_fill_price(
    bid_px: float,
    bar_open: float,
    bar_low: float,
    mode: str = "paper_limit",
) -> Optional[float]:
    """Return a buy-limit fill price on a closed 1h bar, or None if unfilled."""
    if bid_px is None or bid_px <= 0:
        return None
    if bar_low > bid_px:
        return None
    if mode == "live_limit" and bar_open <= bid_px:
        return float(bar_open)
    return float(bid_px)


def working_orders_from_states(states: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Collect resting Book 3 / Book 5 bids from live-runner asset state."""
    out: List[Dict[str, Any]] = []
    for asset, blob in (states or {}).items():
        if not isinstance(blob, dict):
            continue
        eng = blob.get("engine") if isinstance(blob.get("engine"), dict) else blob
        bid = eng.get("active_flush_bid")
        if isinstance(bid, dict) and bid.get("bid_px") is not None:
            out.append({
                "asset": asset,
                "book": "Book 3",
                "side": "BUY",
                "type": "LIMIT",
                "price": bid.get("bid_px"),
                "stop": bid.get("stop_px"),
                "target": bid.get("target_px"),
                "armed_ts": str(bid.get("armed_ts") or ""),
                "ttl_hours": bid.get("ttl_bars"),
                "veto_gate": bid.get("veto_gate"),
            })
        b5 = eng.get("active_b5_bid")
        if isinstance(b5, dict) and b5.get("bid_px") is not None:
            out.append({
                "asset": asset,
                "book": "Book 5",
                "side": "BUY",
                "type": "LIMIT",
                "price": b5.get("bid_px"),
                "stop": b5.get("stop_px"),
                "target": b5.get("target_px"),
                "armed_ts": str(b5.get("armed_ts") or ""),
                "ttl_hours": b5.get("ttl_bars"),
            })
    return out


def write_working_orders(path: Path, orders: List[Dict[str, Any]]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = str(path) + ".tmp"
    payload = {"orders": orders, "count": len(orders)}
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, default=str)
    os.replace(tmp, str(path))
