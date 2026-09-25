"""The trade book is one table. Still-open rows are flagged, not stored as closed."""
import unittest

import pandas as pd

from momentum_v10.book_store import build_scorecard, build_trades


class BookStoreTests(unittest.TestCase):
    def test_open_at_end_is_not_a_second_closed_trade(self):
        closed = pd.DataFrame({
            "asset": ["AAA", "AAA"],
            "engine": ["CONTINUATION", "IGNITION"],
            "entry": ["2026-01-01 00:00:00", "2026-02-01 00:00:00"],
            "exit": ["2026-01-02 00:00:00", "2026-09-24 23:00:00"],
            "entry_price": [1.0, 2.0],
            "exit_price": [1.1, 2.2],
            "pnl": [0.1, 0.1],
            "mfe": [0.2, 0.2],
            "mae": [-0.05, -0.05],
            "reason": ["structural_stop", "open_at_end"],
        })
        live = pd.DataFrame({
            "asset": ["AAA"],
            "engine": ["IGNITION"],
            "entry": ["2026-02-01 00:00:00"],
            "entry_price": [2.0],
            "pnl": [0.15],
            "mfe": [0.2],
            "mae": [-0.05],
        })
        book = build_trades(closed, live)
        self.assertEqual(len(book), 2)
        self.assertEqual(int((~book["still_open"]).sum()), 1)
        self.assertEqual(int(book["still_open"].sum()), 1)
        open_row = book.loc[book["still_open"]].iloc[0]
        self.assertEqual(open_row["reason"], "open_at_end")

    def test_scorecard_is_one_row_per_asset(self):
        book = build_trades(
            pd.DataFrame({
                "asset": ["AAA", "BBB"],
                "engine": ["CONTINUATION", "IGNITION"],
                "entry": ["2026-01-01 00:00:00", "2026-01-01 00:00:00"],
                "exit": ["2026-01-02 00:00:00", "2026-01-03 00:00:00"],
                "entry_price": [1.0, 1.0],
                "exit_price": [0.9, 1.2],
                "pnl": [-0.1, 0.2],
                "mfe": [0.01, 0.3],
                "mae": [-0.1, -0.01],
                "reason": ["structural_stop", "structural_stop"],
            }),
            pd.DataFrame(),
        )
        card = build_scorecard(book)
        self.assertEqual(set(card["asset"]), {"AAA", "BBB"})
        self.assertEqual(len(card), 2)


if __name__ == "__main__":
    unittest.main()
