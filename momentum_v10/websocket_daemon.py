"""Disabled on purpose.

This process used to append a partial websocket candle (no taker volume,
timestamp stored as text) onto the 1h parquet shards, rewrite engine state,
and call build_csv.py. That corrupted shards and replaced the live book
with the research tape.

The production clock is:

    python -m momentum_v10.hourly_job
"""
import sys


def main() -> None:
    print(
        "websocket_daemon is disabled. It appended partial candles and "
        "rewrote the trade book. Run: python -m momentum_v10.hourly_job",
        file=sys.stderr,
    )
    raise SystemExit(2)


if __name__ == "__main__":
    main()
