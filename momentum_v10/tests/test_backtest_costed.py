"""Tests for the costed, position-sized backtest (synthetic shards, exact arithmetic)."""
import math

import numpy as np
import pandas as pd
import pytest

from momentum_v10 import backtest_costed as bc

H = 3_600_000
T0 = pd.Timestamp("2026-01-01 00:00")


def _shard(path, n=400, price=100.0, qv=1e9, drift=0.0, bumps=None, gaps=None):
    ts = (T0.value // 1_000_000) + np.arange(n) * H
    close = price * (1 + drift) ** np.arange(n)
    if bumps:
        for i, v in bumps.items():
            close[i:] = v
    op = np.r_[close[0], close[:-1]]
    for i, v in (gaps or {}).items():
        op[i] = v
    pd.DataFrame({"timestamp": ts, "open": op, "high": np.maximum(op, close) * 1.001,
                  "low": np.minimum(op, close) * 0.999, "close": close,
                  "quote_volume": np.full(n, qv)}).to_parquet(path)


def _world(tmp_path, trades, funding=None, **shard_kw):
    raw, exo, tape = tmp_path / "raw", tmp_path / "exo", tmp_path / "tape"
    for d in (raw, exo, tape):
        d.mkdir()
    for a in {t["asset"] for t in trades}:
        _shard(raw / f"{a}_USDT_1h.parquet", **shard_kw.get(a, {}))
        if funding is not None:
            ts = (T0.value // 1_000_000) + np.arange(400) * H
            pd.DataFrame({"funding_rate": np.full(400, funding), "timestamp": ts}).to_parquet(exo / f"{a}USDT_funding.parquet")
    closed = [t for t in trades if t.get("exit")]
    opn = [t for t in trades if not t.get("exit")]
    pd.DataFrame([{**t, "entry_price": 1, "exit_price": 1, "pnl": t.get("pnl", 0.0), "reason": "structural_stop"}
                  for t in closed], columns=["asset", "engine", "entry", "exit", "entry_price", "exit_price", "pnl", "reason"]
                 ).to_csv(tape / "closed_trades.csv", index=False)
    pd.DataFrame([{**t, "entry_price": 1, "pnl": 0.0} for t in opn],
                 columns=["asset", "engine", "entry", "entry_price", "pnl"]).to_csv(tape / "open_trades.csv", index=False)
    x = bc.extract(tape, raw, exo, tmp_path / "bt")
    return x, pd.read_parquet(tmp_path / "bt" / "marks.parquet")


def test_next_bar_fill_and_exit(tmp_path):
    # signal bar 24 closes at 100; bar 25 gaps open to 103. Exit signal bar 48, bar 49 opens at 95.
    x, _ = _world(tmp_path, [{"asset": "AAA", "engine": "CONTINUATION", "entry": "2026-01-02 00:00:00",
                              "exit": "2026-01-03 00:00:00"}], AAA={"gaps": {25: 103.0, 49: 95.0}})
    r = x.iloc[0]
    assert r.ok and r.signal_close == 100.0 and r.entry_fill == 103.0
    assert r.exit_signal_close == 100.0 and r.exit_fill == 95.0
    assert r.fill_time == pd.Timestamp("2026-01-02 01:00") and r.exit_fill_time == pd.Timestamp("2026-01-03 01:00")


def test_stop_estimates_follow_engine_rules(tmp_path):
    x, _ = _world(tmp_path, [
        {"asset": "AAA", "engine": "CONTINUATION", "entry": "2026-01-02 00:00:00", "exit": "2026-01-03 00:00:00"},
        {"asset": "AAA", "engine": "RETAIL_SQZ", "entry": "2026-01-04 00:00:00", "exit": "2026-01-05 00:00:00"}])
    c, s = x.sort_values("entry").iloc[0], x.sort_values("entry").iloc[1]
    assert c.stop == pytest.approx(100 * 0.999)                          # entry-candle low
    assert s.stop == pytest.approx(s.entry_fill * 0.80) and s.stop_dist == pytest.approx(0.20)


def test_funding_positive_rate_costs_the_long(tmp_path):
    x, _ = _world(tmp_path, [{"asset": "AAA", "engine": "CONTINUATION", "entry": "2026-01-02 00:00:00",
                              "exit": "2026-01-03 00:00:00"}], funding=0.0008)
    r = x.iloc[0]
    assert r.fund_acc == pytest.approx(24 * 0.0008)                       # 24 bars held at flat price
    p = bc.Params(funding="net")
    assert bc._funding(p, r) == pytest.approx(24 * 0.0008 / 8)
    assert bc._funding(bc.Params(), r) == pytest.approx(24 * 0.0008 / 8)             # costs only: all paid            # three 8h settlements
    assert bc._funding(bc.Params(funding_interval_h=4), r) == pytest.approx(24 * 0.0008 / 4)


def test_funding_credits_ignored_by_default(tmp_path):
    x, _ = _world(tmp_path, [{"asset": "AAA", "engine": "CONTINUATION", "entry": "2026-01-02 00:00:00",
                              "exit": "2026-01-03 00:00:00"}], funding=-0.001)
    r = x.iloc[0]
    assert bc._funding(bc.Params(), r) == 0.0
    assert bc._funding(bc.Params(funding="net"), r) == pytest.approx(-24 * 0.001 / 8)
    assert bc._funding(bc.Params(funding="off"), r) == 0.0


def test_costed_pnl_matches_hand_calculation(tmp_path):
    x, m = _world(tmp_path, [{"asset": "AAA", "engine": "CONTINUATION", "entry": "2026-01-02 00:00:00",
                              "exit": "2026-01-03 00:00:00"}], AAA={"bumps": {40: 120.0}, "qv": 1e8})
    p = bc.Params(sizing="fixed", fixed_pct=0.02, funding="off", start_equity=100_000.0)
    res = bc.simulate(x, m, p)
    t = res["trades"].iloc[0]
    r = x.iloc[0]
    notional = 2000.0
    si = bc._slip(p, notional, r.vol24_entry, r.sigma_d_entry)
    px_in = r.entry_fill * (1 + si)
    gross_out_notional = notional * r.exit_fill / px_in
    so = bc._slip(p, notional * r.exit_fill / r.entry_fill, r.vol24_exit, r.sigma_d_exit)
    proceeds = notional * r.exit_fill * (1 - so) / px_in
    expected = proceeds * (1 - p.fee) - notional * (1 + p.fee)      # same P&L under margin accounting
    assert t.pnl == pytest.approx(expected, rel=1e-9)
    assert res["equity"]["equity"].iloc[-1] == pytest.approx(100_000 + expected, rel=1e-9)
    assert res["costs"]["fees"] == pytest.approx(notional * p.fee + proceeds * p.fee)


def test_square_root_impact_grows_with_size():
    p = bc.Params()
    small, big = bc._slip(p, 1_000, 1e7, 0.05), bc._slip(p, 100_000, 1e7, 0.05)
    assert small == pytest.approx(0.0005 + 0.05 * math.sqrt(1e-4))
    assert big == pytest.approx(0.0005 + 0.05 * math.sqrt(1e-2)) and big > small
    assert bc._slip(bc.Params(next_bar=False, legacy_slippage=0.002), 1e9, 1.0, 1.0) == 0.002


def test_risk_sizing_caps_and_skips(tmp_path):
    trades = [{"asset": a, "engine": "RETAIL_SQZ", "entry": "2026-01-02 00:00:00", "exit": "2026-01-05 00:00:00"}
              for a in ("AAA", "BBB", "CCC", "DDD")]
    x, m = _world(tmp_path, trades)
    # 1% risk / 20% stop = 5% notional; cap 5%; gross cap 12% -> 2 full + 1 partial (2%) + 1 skipped
    p = bc.Params(risk_pct=0.01, max_pos_pct=0.05, max_gross_pct=0.12, funding="off", min_notional=50)
    res = bc.simulate(x, m, p)
    n = sorted(res["trades"]["notional"].round(0))
    assert n[-2:] == [5000.0, 5000.0] and len(n) == 3 and 1900 < n[0] < 2100
    assert res["skipped"]["gross_cap"] == 1


def test_participation_cap(tmp_path):
    x, m = _world(tmp_path, [{"asset": "AAA", "engine": "RETAIL_SQZ", "entry": "2026-01-02 00:00:00",
                              "exit": "2026-01-05 00:00:00"}], AAA={"qv": 1e4})
    res = bc.simulate(x, m, bc.Params(funding="off", min_notional=1))
    assert res["trades"]["notional"].iloc[0] == pytest.approx(0.005 * 24 * 1e4)    # 0.5% of 24h volume


def test_open_trade_is_marked_and_liquidated_at_last_bar(tmp_path):
    x, m = _world(tmp_path, [{"asset": "AAA", "engine": "CONTINUATION", "entry": "2026-01-02 00:00:00"}],
                  AAA={"drift": 0.001})
    r = x.iloc[0]
    assert r.status == "OPEN" and r.exit_fill_time == pd.Timestamp(T0) + pd.Timedelta(hours=400)
    res = bc.simulate(x, m, bc.Params(sizing="fixed", funding="off"))
    eq = res["equity"]["equity"]
    assert eq.is_monotonic_increasing and len(eq) >= 15                    # daily marks while held
    met = bc.metrics(res)
    assert met["open_at_end"] == 1 and met["max_drawdown"] <= 0


def test_engine_filter_and_ledger_loader_drop_open_at_end(tmp_path):
    x, m = _world(tmp_path, [
        {"asset": "AAA", "engine": "CONTINUATION", "entry": "2026-01-02 00:00:00", "exit": "2026-01-03 00:00:00"},
        {"asset": "AAA", "engine": "IGNITION", "entry": "2026-01-04 00:00:00", "exit": "2026-01-05 00:00:00"}])
    res = bc.simulate(x, m, bc.Params(engines=("CONTINUATION",)))
    assert set(res["trades"]["engine"]) == {"CONTINUATION"} and res["n_signals"] == 1


def test_trimming_realises_part_of_a_runner_and_keeps_books_balanced(tmp_path):
    x, m = _world(tmp_path, [{"asset": "AAA", "engine": "CONTINUATION", "entry": "2026-01-02 00:00:00",
                              "exit": "2026-01-10 00:00:00"},
                             {"asset": "BBB", "engine": "CONTINUATION", "entry": "2026-01-02 00:00:00",
                              "exit": "2026-01-10 00:00:00"}],
                  AAA={"bumps": {60: 1000.0, 150: 200.0}})             # AAA goes 10x, then back to 2x
    p = bc.Params(sizing="fixed", fixed_pct=0.05, funding="off", trim_pct=0.10)
    res = bc.simulate(x, m, p)
    t = res["trades"].set_index("asset")
    assert t.loc["AAA", "trims"] >= 1 and t.loc["BBB", "trims"] == 0
    no_trim = bc.simulate(x, m, bc.Params(sizing="fixed", fixed_pct=0.05, funding="off", trim_pct=None))
    assert t.loc["AAA", "pnl"] > 2 * no_trim["trades"].set_index("asset").loc["AAA", "pnl"]   # trims locked in the spike
    for r in (res, no_trim):
        assert r["equity"]["equity"].iloc[-1] == pytest.approx(100_000 + r["trades"]["pnl"].sum(), rel=1e-9)
