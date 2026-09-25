"""Refresh all_trades.csv from the live open and closed ledgers.

Does not read master_raw_tape.csv and does not rewrite open_trades.csv or
closed_trades.csv. The research replay stays in master_raw_tape.csv. The
live book is owned by live_runner.py.
"""
import numpy as np
import pandas as pd

from momentum_v10.config import TAPE_DIR

CLOSED_CSV = TAPE_DIR / "closed_trades.csv"
OPEN_CSV = TAPE_DIR / "open_trades.csv"
ALL_CSV = TAPE_DIR / "all_trades.csv"


def write_all_trades_view() -> int:
    """Concatenate the live ledgers into all_trades.csv. Returns the row count."""
    closed_df = pd.read_csv(CLOSED_CSV) if CLOSED_CSV.exists() else pd.DataFrame()
    open_df = pd.read_csv(OPEN_CSV) if OPEN_CSV.exists() else pd.DataFrame()

    if not closed_df.empty:
        if "reason" in closed_df.columns:
            closed_df["status"] = np.where(closed_df["reason"] == "open_at_end", "OPEN", "CLOSED")
        elif "status" not in closed_df.columns:
            closed_df["status"] = "CLOSED"
    if not open_df.empty:
        if "reason" in open_df.columns:
            open_df["status"] = np.where(open_df["reason"] == "open_at_end", "OPEN", "CLOSED")
        elif "status" not in open_df.columns:
            open_df["status"] = "OPEN"

    df = pd.concat([closed_df, open_df], ignore_index=True)
    if df.empty:
        ALL_CSV.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(ALL_CSV, index=False)
        print(f"[build_csv] all_trades.csv rows=0 ({ALL_CSV})")
        return 0

    subset = [c for c in ("asset", "entry", "engine", "exit") if c in df.columns]
    if subset:
        df = df.drop_duplicates(subset=subset, keep="last")

    for num_col in ["pnl", "mfe", "mae", "entry_price", "exit_price", "duration_hours"]:
        if num_col in df.columns:
            df[num_col] = pd.to_numeric(df[num_col], errors="coerce")

    if "pnl" in df.columns:
        df["pnl_pct"] = df["pnl"] * 100.0
    if "mfe" in df.columns:
        df["mfe_pct"] = df["mfe"] * 100.0
    if "mae" in df.columns:
        df["mae_pct"] = df["mae"] * 100.0
    if "entry_price" in df.columns:
        df["entry_px"] = df["entry_price"]

    if "entry" in df.columns:
        df["entry"] = df["entry"].astype(str).str.replace("T", " ", regex=False)
        df["entry_dt"] = pd.to_datetime(df["entry"], errors="coerce")
    if "exit" in df.columns:
        df["exit"] = df["exit"].astype(str).str.replace("T", " ", regex=False)
        df["exit_dt"] = pd.to_datetime(df["exit"], errors="coerce")

    if "entry_dt" in df.columns and "asset" in df.columns:
        df = df.sort_values(["asset", "entry_dt"]).reset_index(drop=True)

    ALL_CSV.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(ALL_CSV, index=False)
    print(f"[build_csv] all_trades.csv rows={len(df)} (open and closed ledgers left untouched)")
    return int(len(df))


def main() -> None:
    write_all_trades_view()


if __name__ == "__main__":
    main()
