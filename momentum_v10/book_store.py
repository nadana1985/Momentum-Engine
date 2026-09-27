"""One trade table and one scorecard, instead of a Markdown file per symbol.

trades.parquet is the book: closed rows plus still-open rows. scorecard.parquet
is one row per symbol, recomputed from that table. A sheet for one symbol is
rendered on request from these files. It is not written for the whole universe.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

from momentum_v10.config import SHARD_DIR, TAPE_DIR

TRADE_COLUMNS = (
    "asset",
    "engine",
    "entry",
    "exit",
    "entry_price",
    "exit_price",
    "pnl",
    "mfe",
    "mae",
    "reason",
    "still_open",
)


def _as_frame(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    return pd.read_csv(path)


def build_trades(closed: pd.DataFrame, open_trades: pd.DataFrame) -> pd.DataFrame:
    """Stack the ledgers. open_at_end rows are still open, not closed trades."""
    frames: list[pd.DataFrame] = []
    if not closed.empty:
        done = closed.copy()
        reason = done["reason"].fillna("").astype(str).str.strip() if "reason" in done.columns else ""
        done["still_open"] = reason.eq("open_at_end") if "reason" in done.columns else False
        done = done.loc[~done["still_open"]].copy()
        frames.append(done)
    if not open_trades.empty:
        live = open_trades.copy()
        live["still_open"] = True
        if "reason" not in live.columns:
            live["reason"] = "open_at_end"
        else:
            blank = live["reason"].fillna("").astype(str).str.strip().isin(["", "nan"])
            live.loc[blank, "reason"] = "open_at_end"
        frames.append(live)
    if not frames:
        return pd.DataFrame(columns=list(TRADE_COLUMNS))
    book = pd.concat(frames, ignore_index=True)
    for column in TRADE_COLUMNS:
        if column not in book.columns:
            book[column] = pd.NA
    book["entry"] = pd.to_datetime(book["entry"], format="mixed", errors="coerce")
    book["exit"] = pd.to_datetime(book["exit"], format="mixed", errors="coerce")
    book["still_open"] = book["still_open"].fillna(False).astype(bool)
    book = book.drop_duplicates(subset=["asset", "engine", "entry", "still_open"], keep="last")
    return book.loc[:, list(TRADE_COLUMNS)].sort_values(["asset", "entry"], kind="mergesort").reset_index(drop=True)


def build_scorecard(trades: pd.DataFrame) -> pd.DataFrame:
    """One scorecard row per symbol. Empty book returns an empty frame."""
    from momentum_v10.universe_generator import compute_scorecard

    if trades.empty:
        return pd.DataFrame()
    rows = []
    for asset, group in trades.groupby("asset", sort=True):
        ordered = group.sort_values("entry", kind="mergesort")
        card = compute_scorecard(ordered)
        card["asset"] = asset
        card["still_open"] = int(ordered["still_open"].sum())
        rows.append(card)
    card_df = pd.DataFrame(rows)
    front = ["asset", "still_open"]
    rest = [c for c in card_df.columns if c not in front]
    return card_df.loc[:, front + rest]


def write_book(tape_dir: Path | None = None, closed: pd.DataFrame | None = None, open_trades: pd.DataFrame | None = None) -> dict:
    """Write trades.parquet and scorecard.parquet. Returns row counts."""
    tape_dir = Path(tape_dir) if tape_dir is not None else TAPE_DIR
    if closed is None:
        closed = _as_frame(tape_dir / "closed_trades.csv")
    if open_trades is None:
        open_trades = _as_frame(tape_dir / "open_trades.csv")
    trades = build_trades(closed, open_trades)
    scorecard = build_scorecard(trades)
    tape_dir.mkdir(parents=True, exist_ok=True)
    from momentum_v10.io_utils import atomic_to_parquet
    atomic_to_parquet(trades, tape_dir / "trades.parquet")
    atomic_to_parquet(scorecard, tape_dir / "scorecard.parquet")
    print(
        f"[book] trades={len(trades)} still_open={int(trades['still_open'].sum()) if not trades.empty else 0} "
        f"scorecard={len(scorecard)} -> {tape_dir}",
        flush=True,
    )
    return {"trades": int(len(trades)), "scorecard": int(len(scorecard))}


def render_asset(asset: str, tape_dir: Path | None = None) -> str:
    """One tear sheet from the stored book. Does not recompute the engine."""
    from momentum_v10.universe_generator import render_tear_sheet

    tape_dir = Path(tape_dir) if tape_dir is not None else TAPE_DIR
    trades = pd.read_parquet(tape_dir / "trades.parquet")
    asset_trades = trades.loc[trades["asset"].astype(str) == asset].copy()
    if asset_trades.empty:
        return f"# {asset} — Institutional Momentum Tear Sheet\n\n**NO TRADES**\n"
    shard = SHARD_DIR / f"{asset}_USDT_1h.parquet"
    if shard.exists():
        stamps = pd.read_parquet(shard, columns=["timestamp"])
        stamps = pd.to_datetime(pd.to_numeric(stamps["timestamp"]), unit="ms")
        index = pd.DatetimeIndex([stamps.min(), stamps.max()])
    else:
        index = pd.DatetimeIndex([asset_trades["entry"].min(), asset_trades["entry"].max()])
    mark = index.max()
    open_rows = asset_trades["still_open"].fillna(False).astype(bool)
    asset_trades.loc[open_rows, "exit"] = mark
    asset_trades.loc[open_rows, "reason"] = "open_at_end"
    missing_exit = asset_trades["exit_price"].isna() & asset_trades["entry_price"].notna() & asset_trades["pnl"].notna()
    asset_trades.loc[missing_exit, "exit_price"] = asset_trades.loc[missing_exit, "entry_price"] * (
        1.0 + asset_trades.loc[missing_exit, "pnl"]
    )
    return render_tear_sheet(asset, pd.DataFrame(index=index), asset_trades)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Write the trade book, or render one symbol.")
    parser.add_argument("asset", nargs="?", help="Render this symbol to stdout from trades.parquet")
    parser.add_argument("--out", type=str, default=None, help="Write the one sheet here instead of stdout")
    args = parser.parse_args(argv)
    if args.asset:
        text = render_asset(args.asset)
        if args.out:
            Path(args.out).write_text(text, encoding="utf-8")
            print(f"[book] wrote {args.out}", flush=True)
        else:
            sys.stdout.write(text)
        return 0
    write_book()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
