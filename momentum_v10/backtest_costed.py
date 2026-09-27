"""Costed, position-sized portfolio backtest of the V10 trade ledger.

The engine's own ledger (closed_trades.csv / open_trades.csv) records every
signal as if it were filled at the signal bar's close + 0.2%, with no fees, no
funding, unlimited size and unlimited concurrent positions. Its "sum of per-trade
%" is not something an account could have earned. This module replays the same
signals as a single account:

  1. Realistic costs (per trade)
     * next-bar fills: the engine decides on a closed hourly bar, so entries and
       exits fill at the NEXT bar's open (the job runs a few minutes after close)
     * taker fees on both sides (default 0.05% = Binance USDT-M VIP0 taker)
     * funding: longs pay/receive the settled rate at every settlement while held
       (settlement interval inferred from the hourly-ffilled funding shard)
     * slippage = half-spread + square-root market impact
           slip = half_spread + Y * sigma_daily * sqrt(order_notional / volume_24h)
       using the trailing 24h quote volume and trailing 30d volatility known at
       decision time (no look-ahead)

  2. Position sizing and a real equity curve
     * risk a fixed fraction of equity per trade to the initial stop
       (notional = risk% * equity / stop_distance)
     * caps: max notional per position (% equity), max participation of 24h
       volume, max gross exposure (% equity), max concurrent positions; a signal
       that does not fit is skipped (counted), never queued
     * equity is marked to market daily -> drawdown, Sharpe, Sortino, CAGR

  3. Engine selection: the same simulation per engine subset, plus a
     walk-forward check (choose engines on the first half, test on the second)

Two stages so the heavy part runs once, where the 1.5 GB of shards live:
    python -m momentum_v10.backtest_costed extract   -> bt/trades_x.parquet, bt/marks.parquet
    python -m momentum_v10.backtest_costed report    -> bt/results.json (+ CSVs)
"""
from __future__ import annotations

import dataclasses
import json
import math
import os
import sys
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import pandas as pd

HOUR_MS = 3_600_000
DAY = pd.Timedelta(days=1)


# --------------------------------------------------------------------------- inputs
def load_ledger(tape_dir: Path) -> pd.DataFrame:
    """Closed + open trades exactly as the dashboard shows them."""
    closed = pd.read_csv(tape_dir / "closed_trades.csv")
    reason = closed.get("reason", pd.Series("", index=closed.index)).fillna("").astype(str)
    closed = closed.loc[reason.ne("open_at_end")]
    closed = closed.drop_duplicates(subset=["asset", "engine", "entry", "exit"])
    closed = closed.assign(status="CLOSED")
    opn = pd.read_csv(tape_dir / "open_trades.csv")
    if "reason" in opn.columns:
        opn = opn.loc[opn["reason"].fillna("").astype(str).str.strip().isin(["", "nan"])]
    opn = opn.assign(status="OPEN", exit=pd.NaT, exit_price=np.nan, reason="open")
    cols = ["asset", "engine", "entry", "exit", "entry_price", "exit_price", "pnl", "reason", "status"]
    df = pd.concat([closed[cols], opn[cols]], ignore_index=True)
    df["entry"] = pd.to_datetime(df["entry"], format="mixed")
    df["exit"] = pd.to_datetime(df["exit"], format="mixed")
    df = df.sort_values(["entry", "asset", "engine"]).reset_index(drop=True)
    df["trade_id"] = np.arange(1, len(df) + 1)
    return df


def _stop_estimate(engine: str, i: int, low: np.ndarray, close: np.ndarray, entry_fill: float) -> float:
    """Initial stop the engine would have used (cta_dual.step_cta)."""
    sqz = "SQZ" in engine or "SQUEEZE" in engine
    if sqz:
        return entry_fill * 0.80
    if engine == "IGNITION":
        # armed_hard_stop = low of the hyper-ignition bar, which is within the
        # 12 bars up to the entry bar; the min over that window is never tighter.
        return float(np.nanmin(low[max(0, i - 12): i + 1]))
    return float(low[i])                         # CONTINUATION, PHOENIX_* (entry-candle low)


def extract(tape_dir: Path, shard_dir: Path, exotic_dir: Path, out_dir: Path,
            assets: list[str] | None = None, tag: str = "") -> pd.DataFrame:
    """Per-trade fills, stops, liquidity, volatility, funding and daily marks."""
    out_dir.mkdir(parents=True, exist_ok=True)
    ledger = load_ledger(tape_dir)
    if assets is not None:
        ledger = ledger.loc[ledger["asset"].isin(assets)]
    rows, marks = [], []
    for asset, grp in ledger.groupby("asset", sort=True):
        path = shard_dir / f"{asset}_USDT_1h.parquet"
        if not path.exists():
            for r in grp.itertuples():
                rows.append({"trade_id": r.trade_id, "ok": False, "why": "no price shard"})
            continue
        px = pd.read_parquet(path, columns=["timestamp", "open", "low", "close", "quote_volume"])
        px = px.drop_duplicates("timestamp").sort_values("timestamp").reset_index(drop=True)
        ts = px["timestamp"].to_numpy(np.int64)
        op, lo, cl = (px[c].to_numpy(float) for c in ("open", "low", "close"))
        qv = px["quote_volume"].to_numpy(float)
        v24 = pd.Series(qv).rolling(24, min_periods=12).sum().to_numpy()
        lr = np.log(pd.Series(cl)).diff()
        sig_d = (lr.rolling(720, min_periods=168).std() * math.sqrt(24)).to_numpy()
        fpath = exotic_dir / f"{asset}USDT_funding.parquet"
        fund = None
        if fpath.exists():
            f = pd.read_parquet(fpath).drop_duplicates("timestamp").sort_values("timestamp")
            f["funding_rate"] = pd.to_numeric(f["funding_rate"], errors="coerce").ffill().fillna(0.0)
            fund = (f["timestamp"].to_numpy(np.int64), f["funding_rate"].to_numpy(float))
        pos = {int(t): k for k, t in enumerate(ts)}
        day_end = (ts // HOUR_MS) % 24 == 23          # bar 23:00 closes the UTC day
        for r in grp.itertuples():
            e_ms = int(pd.Timestamp(r.entry).value // 1_000_000)
            i = pos.get(e_ms)
            if i is None or i + 1 >= len(ts):
                rows.append({"trade_id": r.trade_id, "ok": False, "why": "entry bar missing / no next bar"})
                continue
            entry_fill = op[i + 1]
            if r.status == "CLOSED":
                j = pos.get(int(pd.Timestamp(r.exit).value // 1_000_000))
                if j is None:
                    rows.append({"trade_id": r.trade_id, "ok": False, "why": "exit bar missing"})
                    continue
                if j + 1 < len(ts):
                    exit_fill, exit_ms = op[j + 1], ts[j + 1]
                else:
                    exit_fill, exit_ms = cl[j], ts[j] + HOUR_MS
            else:                                       # open: mark at the last close
                j = len(ts) - 1
                exit_fill, exit_ms = cl[j], ts[j] + HOUR_MS
            fill_ms = ts[i + 1]
            stop = _stop_estimate(r.engine, i, lo, cl, entry_fill)
            stop_dist = (entry_fill - stop) / entry_fill if entry_fill > 0 else np.nan
            # Funding. The shard is the prevailing rate forward-filled hourly (its
            # values change at non-settlement hours too), so the settlement interval
            # cannot be read from it reliably. Accrue rate/interval every hour held
            # (interval is a simulation parameter, default 8h = Binance standard),
            # scaled by price drift. Store the hourly sums; simulate() divides.
            fund_acc, fund_acc_pos = 0.0, 0.0
            if fund is not None:
                fts, frt = fund
                hrs = ts[i + 1: j + 1]                       # bars held (fill bar .. exit bar)
                k = np.searchsorted(fts, hrs, "right") - 1
                ok_k = k >= 0
                if ok_k.any():
                    terms = frt[k[ok_k]] * cl[i + 1: j + 1][ok_k] / entry_fill
                    fund_acc = float(np.sum(terms))
                    fund_acc_pos = float(np.sum(np.clip(terms, 0, None)))
            rows.append({
                "trade_id": r.trade_id, "ok": True, "why": "",
                "fill_time": pd.Timestamp(fill_ms, unit="ms"), "exit_fill_time": pd.Timestamp(exit_ms, unit="ms"),
                "signal_close": cl[i], "entry_fill": entry_fill, "exit_signal_close": cl[j], "exit_fill": exit_fill,
                "stop": stop, "stop_dist": stop_dist,
                "vol24_entry": v24[i], "vol24_exit": v24[j],
                "sigma_d_entry": sig_d[i], "sigma_d_exit": sig_d[j],
                "fund_acc": fund_acc, "fund_acc_pos": fund_acc_pos, "has_funding": fund is not None,
            })
            k0, k1 = i + 1, j
            idx = np.flatnonzero(day_end[k0:k1 + 1]) + k0
            for k in idx:
                marks.append((r.trade_id, pd.Timestamp(ts[k], unit="ms").normalize(), cl[k] / entry_fill))
    x = ledger.merge(pd.DataFrame(rows), on="trade_id", how="left")
    m = pd.DataFrame(marks, columns=["trade_id", "date", "ratio"])
    x.to_parquet(out_dir / f"trades_x{tag}.parquet", index=False)
    m.to_parquet(out_dir / f"marks{tag}.parquet", index=False)
    return x


# --------------------------------------------------------------------------- simulation
@dataclass
class Params:
    name: str = "costed_risk_sized"
    start_equity: float = 100_000.0
    engines: tuple | None = None                  # None = all engines
    # costs
    next_bar: bool = True
    fee: float = 0.0005                           # per side, taker
    half_spread: float = 0.0005
    impact_y: float = 1.0                         # square-root impact coefficient
    funding: str = "costs_only"                   # "costs_only" | "net" | "off" (see report)
    funding_interval_h: float = 8.0               # settlement interval assumed for the hourly rate
    legacy_slippage: float = 0.0                  # the ledger's flat 0.2% when not next-bar
    # sizing
    sizing: str = "risk"                          # "risk" | "fixed"
    risk_pct: float = 0.005                       # equity lost if the initial stop is hit
    fixed_pct: float = 0.02                       # notional per trade when sizing == "fixed"
    min_stop_dist: float = 0.02
    max_pos_pct: float = 0.05
    max_participation: float = 0.005              # of trailing 24h quote volume
    max_gross_pct: float = 2.0                    # 2x gross leverage on the futures account
    max_positions: int = 40
    trim_pct: float | None = 0.20                 # trim a winner back to this share of equity at the daily mark
    min_notional: float = 50.0
    period: tuple | None = None                   # (start, end) on entry time

    def label(self) -> str:
        return self.name


def _slip(p: Params, notional: float, vol24: float, sigma_d: float) -> float:
    if not p.next_bar:
        return p.legacy_slippage
    sig = sigma_d if np.isfinite(sigma_d) and sigma_d > 0 else 0.08
    if not (np.isfinite(vol24) and vol24 > 0):
        return p.half_spread + 0.05
    return p.half_spread + p.impact_y * sig * math.sqrt(max(notional, 0.0) / vol24)


def _funding(p: Params, r) -> float:
    """Funding cost as a fraction of entry notional (negative = received)."""
    if p.funding == "off":
        return 0.0
    v = getattr(r, "fund_acc_pos" if p.funding == "costs_only" else "fund_acc", 0.0)
    return float(v) / p.funding_interval_h if v is not None and np.isfinite(v) else 0.0


def simulate(x: pd.DataFrame, marks: pd.DataFrame, p: Params) -> dict:
    t = x.loc[x["ok"].fillna(False).astype(bool)].copy()
    if p.engines is not None:
        t = t.loc[t["engine"].isin(p.engines)]
    if p.period is not None:
        t = t.loc[(t["entry"] >= pd.Timestamp(p.period[0])) & (t["entry"] < pd.Timestamp(p.period[1]))]
    if p.next_bar:
        t["t_in"], t["t_out"] = t["fill_time"], t["exit_fill_time"]
        t["px_in"], t["px_out"] = t["entry_fill"], t["exit_fill"]
    else:                                            # ledger timing: signal close
        t["t_in"] = t["entry"] + pd.Timedelta(hours=1)
        t["t_out"] = t["exit"].fillna(t["exit_fill_time"] - pd.Timedelta(hours=1)) + pd.Timedelta(hours=1)
        t["px_in"], t["px_out"] = t["signal_close"], t["exit_signal_close"]
    t = t.sort_values(["t_in", "asset", "engine"])
    # event queue: exits before entries at the same timestamp (frees capital)
    ev = [(r.t_out, 0, r.trade_id) for r in t.itertuples()] + [(r.t_in, 1, r.trade_id) for r in t.itertuples()]
    ev.sort(key=lambda e: (e[0], e[1], e[2]))
    tr = t.set_index("trade_id")
    cash = p.start_equity
    open_pos: dict[int, dict] = {}
    realized, skipped = [], {"gross_cap": 0, "max_positions": 0, "too_small": 0, "bad_stop": 0}
    costs = {"fees": 0.0, "slippage": 0.0, "funding": 0.0}
    # daily marks for open positions
    mk = marks.loc[marks["trade_id"].isin(tr.index)]
    mk_by_day = {d: g.set_index("trade_id")["ratio"] for d, g in mk.groupby("date")}
    days = pd.date_range(t["t_in"].min().normalize(), t["t_out"].max().normalize(), freq="D") if len(t) else []
    curve, ei, d_i = [], 0, 0
    last_ratio: dict[int, float] = {}

    # Futures-account accounting: "cash" is the realised balance (collateral); a
    # position contributes its unrealised P&L. Entry fees are paid immediately.
    def value(tid, q):
        return q["notional"] * q["adj"] * last_ratio.get(tid, 1.0)

    def equity_now() -> float:
        return cash + sum(value(tid, q) - q["notional"] for tid, q in open_pos.items())

    def mark_day(d):
        nonlocal cash
        ratios = mk_by_day.get(d)
        if ratios is not None:
            for tid in open_pos:
                if tid in ratios.index:
                    last_ratio[tid] = float(ratios.loc[tid])
        if p.trim_pct:
            eq = equity_now()
            for tid, q in open_pos.items():
                v = value(tid, q)
                if eq > 0 and v > p.trim_pct * eq * 1.25:       # trim once 25% over the cap, back to the cap
                    f = 1 - p.trim_pct * eq / v
                    sold = f * v
                    r = tr.loc[tid]
                    slip = _slip(p, sold, r.vol24_entry, r.sigma_d_entry)
                    gain = f * (v - q["notional"]) - sold * (slip + p.fee)
                    cash += gain
                    q["realized"] = q.get("realized", 0.0) + gain
                    q["notional"] *= (1 - f)
                    costs["fees"] += sold * p.fee; costs["slippage"] += sold * slip
                    q["trims"] = q.get("trims", 0) + 1
        curve.append((d, equity_now(), sum(value(tid, q) for tid, q in open_pos.items())))

    for when, kind, tid in ev:
        while d_i < len(days) and days[d_i] + DAY <= when:     # close the days before this event
            mark_day(days[d_i]); d_i += 1
        r = tr.loc[tid]
        if kind == 0:
            q = open_pos.pop(tid, None)
            if q is None:
                continue
            slip = _slip(p, q["notional"] * r.px_out / r.px_in, r.vol24_exit, r.sigma_d_exit)
            px_out = r.px_out * (1 - slip)
            gross = q["notional"] * px_out / q["px_in"]
            fee = gross * p.fee
            fund = q["notional0"] * _funding(p, r)           # funding accrued on the entry notional
            pnl = gross - q["notional"] - q["fee_in"] - fee - fund + q.get("realized", 0.0)
            cash += gross - q["notional"] - fee - fund
            costs["fees"] += fee; costs["funding"] += fund
            costs["slippage"] += q["notional"] * r.px_out / q["px_in"] * slip + q["slip_cost"]
            last_ratio.pop(tid, None)
            realized.append({"trade_id": tid, "asset": r.asset, "engine": r.engine, "status": r.status,
                             "t_in": r.t_in, "t_out": r.t_out, "notional": q["notional0"], "pnl": pnl,
                             "ret": pnl / q["notional0"], "trims": q.get("trims", 0), "r_mult": pnl / q["risk"] if q["risk"] > 0 else np.nan,
                             "equity_at_entry": q["eq"]})
        else:
            eq = equity_now()
            sd = r.stop_dist
            if not np.isfinite(sd) or sd <= 0:
                skipped["bad_stop"] += 1
                sd = p.min_stop_dist
            sd = max(sd, p.min_stop_dist)
            if p.sizing == "risk":
                notional = p.risk_pct * eq / sd
            else:
                notional = p.fixed_pct * eq
            notional = min(notional, p.max_pos_pct * eq)
            if np.isfinite(r.vol24_entry) and r.vol24_entry > 0:
                notional = min(notional, p.max_participation * r.vol24_entry)
            if len(open_pos) >= p.max_positions:
                skipped["max_positions"] += 1; continue
            if eq <= 0:
                skipped["gross_cap"] += 1; continue
            gross_open = sum(value(k, q) for k, q in open_pos.items())
            headroom = max(0.0, p.max_gross_pct * eq - gross_open)
            if headroom < p.min_notional:
                skipped["gross_cap"] += 1; continue
            notional = min(notional, headroom)
            if notional < p.min_notional:
                skipped["too_small"] += 1; continue
            slip = _slip(p, notional, r.vol24_entry, r.sigma_d_entry)
            px_in = r.px_in * (1 + slip)
            fee = notional * p.fee
            cash -= fee
            costs["fees"] += fee
            open_pos[tid] = {"notional": notional, "notional0": notional, "px_in": px_in, "fee_in": fee, "eq": eq, "adj": r.px_in / px_in,
                             "risk": notional * sd, "slip_cost": notional * slip}
    while d_i < len(days):
        mark_day(days[d_i]); d_i += 1
    ec = pd.DataFrame(curve, columns=["date", "equity", "gross"]).set_index("date")
    return {"params": p, "equity": ec, "trades": pd.DataFrame(realized), "skipped": skipped,
            "costs": costs, "n_signals": int(len(t))}


def metrics(res: dict) -> dict:
    ec, tr, p = res["equity"], res["trades"], res["params"]
    out = {"name": p.name, "signals": res["n_signals"], "taken": int(len(tr)),
           "skipped": int(sum(res["skipped"].values())), "skipped_by": res["skipped"]}
    if ec.empty or tr.empty:
        return out
    eq = ec["equity"]
    ret = eq.pct_change().dropna()
    years = max((eq.index[-1] - eq.index[0]).days / 365.25, 1e-9)
    dd = eq / eq.cummax() - 1
    total = eq.iloc[-1] / p.start_equity - 1
    cagr = (eq.iloc[-1] / p.start_equity) ** (1 / years) - 1 if eq.iloc[-1] > 0 else -1.0
    sd = ret.std()
    down = ret[ret < 0].std()
    closed = tr                                     # open positions are liquidated at the last bar
    wins = closed.loc[closed["pnl"] > 0, "pnl"].sum(); losses = -closed.loc[closed["pnl"] <= 0, "pnl"].sum()
    top = tr["pnl"].sort_values(ascending=False)
    k1 = max(1, len(top) // 100)
    out.update({
        "start": str(eq.index[0].date()), "end": str(eq.index[-1].date()), "years": round(years, 2),
        "final_equity": round(float(eq.iloc[-1]), 0), "total_return": float(total), "cagr": float(cagr),
        "max_drawdown": float(dd.min()), "max_dd_date": str(dd.idxmin().date()),
        "sharpe": float(ret.mean() / sd * math.sqrt(365)) if sd > 0 else None,
        "sortino": float(ret.mean() / down * math.sqrt(365)) if down and down > 0 else None,
        "calmar": float(cagr / -dd.min()) if dd.min() < 0 else None,
        "win_rate": float((closed["pnl"] > 0).mean()) if len(closed) else None,
        "profit_factor": float(wins / losses) if losses > 0 else None,
        "avg_r": float(tr["r_mult"].mean()), "median_r": float(tr["r_mult"].median()),
        "avg_exposure": float((ec["gross"] / ec["equity"]).mean()),
        "pnl_top1pct_share": float(top.iloc[:k1].sum() / top.sum()) if top.sum() != 0 else None,
        "pnl_top5": float(top.iloc[:5].sum()), "pnl_ex_top5": float(top.iloc[5:].sum()),
        "pnl_ex_top1pct": float(top.iloc[k1:].sum()),
        "open_at_end": int((tr["status"] == "OPEN").sum()),
        "open_at_end_pnl": float(tr.loc[tr["status"] == "OPEN", "pnl"].sum()),
        "fees": res["costs"]["fees"], "slippage": res["costs"]["slippage"], "funding": res["costs"]["funding"],
        "turnover_x": float((tr["notional"].sum() * 2) / p.start_equity / years),
    })
    return out


def by_engine(res: dict) -> pd.DataFrame:
    tr = res["trades"]
    if tr.empty:
        return pd.DataFrame()
    g = tr.groupby("engine")
    return pd.DataFrame({"trades": g.size(), "win_rate": g["pnl"].apply(lambda s: (s > 0).mean()),
                         "pnl_usd": g["pnl"].sum(), "avg_ret": g["ret"].mean(), "median_ret": g["ret"].median(),
                         "avg_r": g["r_mult"].mean()}).sort_values("pnl_usd", ascending=False)


def per_trade_costed(x: pd.DataFrame, p: Params, notional: float = 10_000.0) -> pd.DataFrame:
    """Unsized, per-trade view: ledger % vs next-bar-and-costed % at a fixed $ size."""
    t = x.loc[x["ok"].fillna(False).astype(bool)].copy()
    si = np.array([_slip(p, notional, v, s) for v, s in zip(t["vol24_entry"], t["sigma_d_entry"])])
    so = np.array([_slip(p, notional, v, s) for v, s in zip(t["vol24_exit"], t["sigma_d_exit"])])
    pin, pout = t["entry_fill"] * (1 + si), t["exit_fill"] * (1 - so)
    t["ret_ledger"] = t["pnl"]
    t["ret_nextbar_nocost"] = t["exit_fill"] / t["entry_fill"] - 1
    t["ret_costed"] = (pout / pin) * (1 - p.fee) - 1 - p.fee - np.array([_funding(p, r) for r in t.itertuples()])
    t["slip_rt"] = si + so
    return t


# --------------------------------------------------------------------------- report
KEEP = ("CONTINUATION", "RETAIL_SQZ", "SQUEEZE_IGN")
NO_PHX_CONT = ("CONTINUATION", "IGNITION", "PHOENIX_IGNITION", "RETAIL_SQZ", "SQUEEZE_IGN")


def scenarios() -> list[Params]:
    return [
        Params(name="A. Ledger as recorded: close fills +0.2%, no fees or funding, 2% per trade",
               next_bar=False, fee=0, funding="off", legacy_slippage=0.002, sizing="fixed"),
        Params(name="B. A + next-bar fills, fees, slippage, funding", sizing="fixed"),
        Params(name="C. B + 0.5% risk sizing and portfolio caps (all engines)"),
        Params(name="D. C without PHOENIX_CONTINUATION", engines=NO_PHX_CONT),
        Params(name="E. C without IGNITION and PHOENIX_* (the item-3 proposal)", engines=KEEP),
        Params(name="F. C, CONTINUATION only", engines=("CONTINUATION",)),
    ]


def start_dispersion(x, marks, base: Params, starts) -> list[dict]:
    """Same rules, different start dates: how much of the result is timing luck."""
    end = x["entry"].max() + DAY
    out = []
    for st in starts:
        m = metrics(simulate(x, marks, dataclasses.replace(base, name=str(st.date()), period=(st, end))))
        out.append({k: m.get(k) for k in ("name", "taken", "cagr", "total_return", "max_drawdown", "sharpe")})
    return out


def run_report(bt_dir: Path) -> dict:
    x = pd.read_parquet(bt_dir / "trades_x.parquet")
    marks = pd.read_parquet(bt_dir / "marks.parquet")
    ok = x["ok"].fillna(False).astype(bool)
    out = {"data": {"ledger_trades": int(len(x)), "replayable": int(ok.sum()),
                    "not_replayable": x.loc[~ok, "why"].value_counts().to_dict(),
                    "with_funding_data": int(x.loc[ok, "has_funding"].sum()),
                    "entry_min": str(x["entry"].min()), "entry_max": str(x["entry"].max()),
                    "open_trades": int((x["status"] == "OPEN").sum())},
           "defaults": dataclasses.asdict(Params()),
           "scenarios": [], "engines": {}, "sensitivity": [], "walk_forward": {}}
    curves = {}
    for p in scenarios():
        res = simulate(x, marks, p)
        out["scenarios"].append(metrics(res))
        curves[p.name[:1]] = res["equity"]["equity"]
        out["engines"][p.name[:1]] = by_engine(res).reset_index().to_dict("records")
        if p.name.startswith("C."):
            res["trades"].to_csv(bt_dir / "trades_C.csv", index=False)
            yr = res["equity"]["equity"].resample("YE").last()
            prev = pd.concat([pd.Series([p.start_equity], index=[yr.index[0] - pd.offsets.YearEnd()]), yr])
            out["years_C"] = {str(k.year): float(v) for k, v in (yr / prev.shift(1).loc[yr.index] - 1).items()}
    pd.DataFrame(curves).to_csv(bt_dir / "equity_curves.csv")
    out["curves"] = {k: {str(d.date()): round(float(v), 2) for d, v in s.dropna().items()} for k, s in curves.items()}
    # each engine alone, same costs and sizing
    out["engine_standalone"] = [metrics(simulate(x, marks, Params(name=e, engines=(e,))))
                                for e in sorted(x["engine"].dropna().unique())]
    # sensitivity around C
    for label, kw in [("fees 0.02% (maker)", dict(fee=0.0002)), ("fees 0.08%", dict(fee=0.0008)),
                      ("impact Y=0.5", dict(impact_y=0.5)), ("impact Y=2", dict(impact_y=2.0)),
                      ("funding off", dict(funding="off")), ("funding net (credits counted)", dict(funding="net")),
                      ("funding interval 4h", dict(funding_interval_h=4.0)),
                      ("risk 0.25%", dict(risk_pct=0.0025)), ("risk 1%", dict(risk_pct=0.01)),
                      ("gross cap 1x", dict(max_gross_pct=1.0)), ("gross cap 3x", dict(max_gross_pct=3.0)),
                      ("max 20 positions", dict(max_positions=20)), ("no trimming of winners", dict(trim_pct=None)),
                      ("trim winners at 10%", dict(trim_pct=0.10)), ("participation 0.1% of 24h vol", dict(max_participation=0.001)),
                      ("equity $10k", dict(start_equity=10_000.0)), ("equity $1m", dict(start_equity=1_000_000.0)),
                      ("ledger timing, costed", dict(next_bar=False, legacy_slippage=0.002))]:
        out["sensitivity"].append(metrics(simulate(x, marks, Params(name=label, **kw))))
    # start-date dispersion (quarterly starts, at least 1 year of data after)
    t0, t1 = x["entry"].min(), x["entry"].max()
    starts = [d for d in pd.date_range(t0.normalize() + pd.offsets.QuarterBegin(startingMonth=1), t1 - pd.Timedelta(days=365), freq="QS")]
    out["dispersion"] = {"C": start_dispersion(x, marks, Params(), starts),
                         "E": start_dispersion(x, marks, Params(engines=KEEP), starts)}
    # walk-forward engine choice: in-sample costed expectancy > 0 (first half) -> test on second half
    mid = t0 + (t1 - t0) / 2
    ins = per_trade_costed(x.loc[x["entry"] < mid], Params())
    ins = ins.loc[ins["status"] == "CLOSED"]
    exp = ins.groupby("engine")["ret_costed"].mean()
    chosen = tuple(sorted(exp[exp > 0].index))
    wf = {"split": str(mid.date()), "in_sample_expectancy": exp.round(4).to_dict(), "chosen": list(chosen)}
    oos = per_trade_costed(x.loc[x["entry"] >= mid], Params())
    oos = oos.loc[oos["status"] == "CLOSED"]
    wf["out_of_sample_expectancy"] = oos.groupby("engine")["ret_costed"].mean().round(4).to_dict()
    for nm, eng in (("all engines", None), ("chosen engines", chosen)):
        wf[nm] = metrics(simulate(x, marks, Params(name=nm, engines=eng, period=(mid, t1 + DAY))))
    out["walk_forward"] = wf
    # unsized per-trade view ($10k a trade), closed trades
    pt = per_trade_costed(x, Params())
    closed = pt.loc[pt["status"] == "CLOSED"]
    g = closed.groupby("engine")
    out["per_trade"] = pd.DataFrame({
        "trades": g.size(), "ledger_mean": g["ret_ledger"].mean(), "nextbar_mean": g["ret_nextbar_nocost"].mean(),
        "costed_mean": g["ret_costed"].mean(), "costed_median": g["ret_costed"].median(),
        "costed_win_rate": g["ret_costed"].apply(lambda v: (v > 0).mean()),
        "median_slip_rt": g["slip_rt"].median(),
        "mean_funding": g["fund_acc_pos"].mean() / 8.0}).reset_index().to_dict("records")
    out["per_trade_reason"] = closed.groupby("reason").agg(
        trades=("ret_ledger", "size"), ledger_mean=("ret_ledger", "mean"),
        nextbar_mean=("ret_nextbar_nocost", "mean"), costed_mean=("ret_costed", "mean")).reset_index().to_dict("records")
    f8 = pt["fund_acc"] / 8.0
    credits = (-f8.clip(upper=0)).sort_values(ascending=False)
    out["funding_diag"] = {"trades_receiving": int((f8 < 0).sum()), "trades_paying": int((f8 > 0).sum()),
                           "credit_top10_share": float(credits.iloc[:10].sum() / credits.sum()) if credits.sum() > 0 else None,
                           "top_credits": pt.assign(f=f8).nsmallest(8, "f")[["asset", "engine", "entry", "f"]]
                           .assign(entry=lambda d: d["entry"].astype(str)).to_dict("records")}
    (bt_dir / "results.json").write_text(json.dumps(out, default=_json_default, indent=1))
    return out


def _json_default(o):
    if isinstance(o, Params):
        return dataclasses.asdict(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return None if not np.isfinite(o) else float(o)
    if isinstance(o, (pd.Timestamp,)):
        return str(o)
    return str(o)


def main(argv=None):
    argv = argv or sys.argv[1:]
    from momentum_v10.config import DATA_ROOT
    tape = Path(os.environ.get("V10_TAPE_DIR") or DATA_ROOT / "all_tapes" / "v10_production")
    bt = Path(os.environ.get("V10_BT_DIR") or DATA_ROOT.parent / "bt")
    if argv and argv[0] == "extract":
        # extract [i n]: chunk i of n (by sorted asset) so each run stays short
        i, n = (int(argv[1]), int(argv[2])) if len(argv) > 2 else (0, 1)
        allassets = sorted(load_ledger(tape)["asset"].unique())
        chunk = allassets[i::n]
        x = extract(tape, DATA_ROOT / "raw_shards", DATA_ROOT / "exotic_shards", bt / "parts", chunk, tag=f"_{i:02d}of{n:02d}")
        print(f"chunk {i}/{n}: extracted {int(x['ok'].fillna(False).sum())}/{len(x)} trades")
    elif argv and argv[0] == "merge":
        parts = bt / "parts"
        pd.concat([pd.read_parquet(f) for f in sorted(parts.glob("trades_x_*.parquet"))]).sort_values("trade_id") \
            .to_parquet(bt / "trades_x.parquet", index=False)
        pd.concat([pd.read_parquet(f) for f in sorted(parts.glob("marks_*.parquet"))]).to_parquet(bt / "marks.parquet", index=False)
        print("merged", len(list(parts.glob("trades_x_*.parquet"))), "parts")
    elif argv and argv[0] == "report":
        out = run_report(bt)
        for s in out["scenarios"]:
            print(f"{s['name']:60} ret {s.get('total_return', 0):+.1%}  dd {s.get('max_drawdown', 0):.1%}  sharpe {s.get('sharpe')}")
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
