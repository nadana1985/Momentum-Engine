"""JSON state reloads times as text and omits entry_shock. Neither may abort a step."""
import unittest

import pandas as pd

from momentum_v10.cta_dual import step_cta
from momentum_v10.config import CtaConfig
from momentum_v10.live_runner import active_trade_record


def _row(close=1.0):
    return pd.Series({
        "close": close,
        "high": close * 1.01,
        "low": close * 0.99,
    })


class StateReloadTests(unittest.TestCase):
    def test_phoenix_watch_exit_ts_may_be_text(self):
        state = {
            "active_trades": [],
            "phoenix_watch": [{
                "original_entry_price": 1.0,
                "exit_ts": "2026-09-22T01:00:00",
                "original_engine": "IGNITION",
            }],
            "armed_countdown": 0,
            "armed_shock": 0.0,
            "armed_hard_stop": 0.0,
        }
        step_cta(pd.Timestamp("2026-09-22T02:00:00"), _row(), state, CtaConfig(), asset="ABC")
        self.assertEqual(len(state["phoenix_watch"]), 1)

    def test_open_trade_without_entry_shock_still_records(self):
        trade = {
            "entry_time": "2026-09-11T03:00:00",
            "entry_price": 1.0,
            "hard_stop": 0.9,
            "trade_max_high": 1.2,
            "trade_min_low": 0.95,
            "engine": "CONTINUATION",
        }
        row = active_trade_record("ABC", trade, 1.1)
        self.assertEqual(row["shock"], 0.0)
        self.assertAlmostEqual(row["pnl"], 0.1)
        self.assertEqual(row["engine"], "CONTINUATION")

    def test_exit_duration_accepts_text_entry_time(self):
        state = {
            "active_trades": [{
                "entry_time": "2026-09-11T03:00:00",
                "entry_price": 1.0,
                "hard_stop": 0.99,
                "trade_max_high": 1.0,
                "trade_min_low": 0.98,
                "engine": "CONTINUATION",
            }],
            "phoenix_watch": [],
            "armed_countdown": 0,
            "armed_shock": 0.0,
            "armed_hard_stop": 0.0,
        }
        # Close below the hard stop, so this bar exits.
        step_cta(pd.Timestamp("2026-09-11T05:00:00"), _row(0.90), state, CtaConfig(), asset="ABC")
        self.assertEqual(state["active_trades"], [])


if __name__ == "__main__":
    unittest.main()
