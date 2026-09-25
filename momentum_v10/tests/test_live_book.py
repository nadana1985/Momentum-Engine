"""Live-book counts and dedupe. No shards, no network."""
import tempfile
import unittest
from pathlib import Path

import pandas as pd

from momentum_v10.hourly_job import render_report
from momentum_v10.live_book import (
    count_closed,
    count_open,
    dedupe_new_trades,
    preserve_research_open,
)


class LiveBookTests(unittest.TestCase):
    def test_open_at_end_is_neither_open_nor_closed(self):
        research = pd.DataFrame({
            "asset": ["AAA", "BBB"],
            "reason": ["open_at_end", "structural_stop"],
            "engine": ["CONTINUATION", "CONTINUATION"],
        })
        self.assertEqual(count_open(research), 0)
        self.assertEqual(count_closed(research), 1)

    def test_live_open_file_has_no_reason_column(self):
        live = pd.DataFrame({
            "asset": ["AAA"],
            "engine": ["CONTINUATION"],
            "entry": ["2026-09-24 01:00:00"],
            "entry_price": [1.0],
        })
        self.assertEqual(count_open(live), 1)
        self.assertEqual(count_closed(live), 1)

    def test_dedupe_matches_space_and_t_timestamps(self):
        existing = pd.DataFrame({
            "asset": ["AAA"],
            "engine": ["CONTINUATION"],
            "entry": ["2026-09-24 01:00:00"],
            "exit": ["2026-09-24 05:00:00"],
        })
        new = pd.DataFrame({
            "asset": ["AAA", "BBB"],
            "engine": ["CONTINUATION", "IGNITION"],
            "entry": ["2026-09-24T01:00:00", "2026-09-24T02:00:00"],
            "exit": ["2026-09-24T05:00:00", "2026-09-24T06:00:00"],
        })
        kept = dedupe_new_trades(existing, new)
        self.assertEqual(list(kept["asset"]), ["BBB"])

    def test_preserve_research_open_once(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "open_trades.csv"
            pd.DataFrame({
                "asset": ["AAA"],
                "reason": ["open_at_end"],
            }).to_csv(path, index=False)
            dest = preserve_research_open(path)
            self.assertEqual(dest.name, "research_open_at_end.csv")
            self.assertTrue(dest.exists())
            self.assertIsNone(preserve_research_open(path))

    def test_email_subject_uses_both_counts(self):
        subject, body = render_report({
            "ok": True,
            "open": 4,
            "closed": 90,
            "closed_this_hour": 2,
            "ingest_updated": 1,
            "ingest_failed": 0,
            "assets": 10,
            "assets_failed": 0,
            "started_utc": "2026-09-24 12:00:00",
            "finished_utc": "2026-09-24 12:05:00",
        })
        self.assertEqual(subject, "V10 hourly: 4 open, 90 closed (2 new)")
        self.assertIn("Open trades: 4", body)
        self.assertIn("Closed trades: 90", body)
        self.assertIn("Closed this hour: 2", body)


if __name__ == "__main__":
    unittest.main()
