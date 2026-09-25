"""A mid-hour fetch must not be stored or stepped as a finished bar."""
import unittest

import pandas as pd

from momentum_v10.bar_clock import bar_is_closed, drop_forming_hours, drop_forming_klines


class BarClockTests(unittest.TestCase):
    def test_open_hour_is_not_closed_at_16_41(self):
        now = pd.Timestamp("2026-09-24 16:41", tz="UTC")
        self.assertFalse(bar_is_closed("2026-09-24 16:00", now))
        self.assertTrue(bar_is_closed("2026-09-24 15:00", now))

    def test_forming_kline_is_not_stored(self):
        # 16:00 bar closes at 16:59:59.999. At 16:41 it is still open.
        now_ms = int(pd.Timestamp("2026-09-24 16:41", tz="UTC").timestamp() * 1000)
        close_16 = int(pd.Timestamp("2026-09-24 16:59:59.999", tz="UTC").timestamp() * 1000)
        close_15 = int(pd.Timestamp("2026-09-24 15:59:59.999", tz="UTC").timestamp() * 1000)
        frame = pd.DataFrame({
            "timestamp": [1, 2],
            "close_time": [close_15, close_16],
            "close": [10.0, 11.0],
        })
        kept = drop_forming_klines(frame, now_ms)
        self.assertEqual(list(kept["close"]), [10.0])

    def test_closed_kline_is_kept_after_the_hour(self):
        now_ms = int(pd.Timestamp("2026-09-24 17:01", tz="UTC").timestamp() * 1000)
        close_16 = int(pd.Timestamp("2026-09-24 16:59:59.999", tz="UTC").timestamp() * 1000)
        frame = pd.DataFrame({"close_time": [close_16], "close": [12.0]})
        kept = drop_forming_klines(frame, now_ms)
        self.assertEqual(list(kept["close"]), [12.0])

    def test_forming_hour_bucket_is_dropped(self):
        now_ms = int(pd.Timestamp("2026-09-24 17:17", tz="UTC").timestamp() * 1000)
        open_16 = int(pd.Timestamp("2026-09-24 16:00", tz="UTC").timestamp() * 1000)
        open_17 = int(pd.Timestamp("2026-09-24 17:00", tz="UTC").timestamp() * 1000)
        frame = pd.DataFrame({"timestamp": [open_16, open_17], "funding_rate": [0.01, 0.02]})
        kept = drop_forming_hours(frame, now_ms)
        self.assertEqual(list(kept["timestamp"]), [open_16])


if __name__ == "__main__":
    unittest.main()
