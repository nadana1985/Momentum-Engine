"""Render bt/results.json (from backtest_costed.py) as one self-contained HTML page.

    python -m momentum_v10.backtest_report [bt_dir] [findings.json]

findings.json (optional) = {"verdict": "...", "findings": ["...", ...], "actions": ["...", ...]}
"""
from __future__ import annotations

import html
import json
import sys
from pathlib import Path


def _pct(v, d=1, sign=True):
    if v is None:
        return "—"
    return f"{v * 100:+.{d}f}%" if sign else f"{v * 100:.{d}f}%"


def _num(v, d=2):
    return "—" if v is None else f"{v:,.{d}f}"


def _usd(v):
    return "—" if v is None else f"${v:,.0f}"


def _cls(v):
    return "" if v is None else ("pos" if v > 0 else "neg" if v < 0 else "")


def _table(head, rows, cls=""):
    th = "".join(f"<th>{html.escape(h)}</th>" for h in head)
    body = "".join("<tr>" + "".join(f"<td{c}>{v}</td>" for v, c in r) + "</tr>" for r in rows)
    return f'<div class="tw"><table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


def _c(v, fmt=_pct, color=True):
    return (fmt(v), f' class="{_cls(v)}"' if color else "")


def scen_rows(items):
    rows = []
    for s in items:
        rows.append([
            (html.escape(s["name"]), ""), (f'{s.get("taken", 0):,} / {s.get("signals", 0):,}', ""),
            _c(s.get("total_return")), _c(s.get("cagr")), _c(s.get("max_drawdown"), color=False),
            (_num(s.get("sharpe")), f' class="{_cls(s.get("sharpe"))}"'), (_num(s.get("profit_factor")), ""),
            (_pct(s.get("win_rate"), 0, False), ""),
            (_usd(s.get("pnl_ex_top5")), f' class="{_cls(s.get("pnl_ex_top5"))}"'),
            (_usd((s.get("fees") or 0) + (s.get("slippage") or 0)), ""), (_usd(s.get("funding")), ""),
        ])
    return rows


SCEN_HEAD = ["Scenario", "Trades taken / signals", "Total return", "CAGR", "Max drawdown", "Sharpe",
             "Profit factor", "Win rate", "P&L without top 5 trades", "Fees + slippage", "Funding"]


def render(res: dict, findings: dict | None = None) -> str:
    f = findings or {}
    d = res["data"]
    sc = {s["name"][:1]: s for s in res["scenarios"]}
    A, C = sc.get("A", {}), sc.get("C", {})
    curves = res.get("curves", {})
    names = {s["name"][:1]: s["name"] for s in res["scenarios"]}
    pal = {"A": "#8b95a7", "B": "#c08a2e", "C": "#d64545", "D": "#7b61ff", "E": "#1f9d6b", "F": "#2b7bd6"}
    datasets = []
    for k, series in curves.items():
        datasets.append({"label": names.get(k, k), "data": [{"x": dte, "y": v} for dte, v in series.items()],
                         "borderColor": pal.get(k, "#888"), "borderWidth": 2 if k in ("A", "C", "E") else 1.3,
                         "pointRadius": 0, "tension": 0, "hidden": k in ("B", "F")})
    disp = res.get("dispersion", {})
    disp_ds = [{"label": lab, "data": [{"x": r["name"], "y": None if r.get("cagr") is None else round(r["cagr"] * 100, 1)} for r in disp.get(k, [])],
                "backgroundColor": col} for k, lab, col in (("C", "All engines (C)", "#d64545"), ("E", "CONTINUATION + squeezes (E)", "#1f9d6b"))]

    pt_rows = [[(html.escape(r["engine"]), ""), (f'{r["trades"]:,}', ""), _c(r["ledger_mean"], lambda v: _pct(v, 2)),
                _c(r["nextbar_mean"], lambda v: _pct(v, 2)), _c(r["costed_mean"], lambda v: _pct(v, 2)),
                _c(r["costed_median"], lambda v: _pct(v, 2)), (_pct(r["costed_win_rate"], 0, False), ""),
                (_pct(r["median_slip_rt"], 2, False), ""), (_pct(r["mean_funding"], 2), "")]
               for r in sorted(res["per_trade"], key=lambda r: -r["costed_mean"])]
    rs_rows = [[(html.escape(r["reason"]), ""), (f'{r["trades"]:,}', ""), _c(r["ledger_mean"]), _c(r["nextbar_mean"]),
                _c(r["costed_mean"])] for r in sorted(res["per_trade_reason"], key=lambda r: -r["trades"])]
    wf = res.get("walk_forward", {})
    wf_rows = [[(html.escape(e), ""), _c(wf["in_sample_expectancy"].get(e), lambda v: _pct(v, 2)),
                _c(wf.get("out_of_sample_expectancy", {}).get(e), lambda v: _pct(v, 2)),
                ("✓" if e in wf.get("chosen", []) else "", "")] for e in sorted(wf.get("in_sample_expectancy", {}))]
    years = res.get("years_C", {})
    yr_rows = [[(y, ""), _c(v)] for y, v in years.items()]
    dflt = res.get("defaults", {})
    fd = res.get("funding_diag", {})
    credit_note = ", ".join(f'{html.escape(c["asset"])} {c["f"] * 100:+,.0f}% of notional' for c in fd.get("top_credits", [])[:2]) or "none"

    def bullets(xs):
        return "".join(f"<li>{x}</li>" for x in xs)

    kpis = [
        ("Ledger, as recorded (A)", _pct(A.get("total_return"), 0), f'CAGR {_pct(A.get("cagr"))} · max DD {_pct(A.get("max_drawdown"), 0)}'),
        ("Costed + risk-sized (C)", _pct(C.get("total_return"), 0), f'CAGR {_pct(C.get("cagr"))} · max DD {_pct(C.get("max_drawdown"), 0)}'),
        ("Sharpe A → C", f'{_num(A.get("sharpe"))} → {_num(C.get("sharpe"))}', "daily, annualised"),
        ("Signals the account could take (C)", f'{C.get("taken", 0):,}', f'of {C.get("signals", 0):,} — the rest hit the exposure caps'),
    ]
    kpi_html = "".join(f'<div class="kpi"><div class="kl">{html.escape(a)}</div><div class="kv">{b}</div><div class="ks">{html.escape(c)}</div></div>' for a, b, c in kpis)

    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>V10 Costed Backtest</title>
<meta name="robots" content="noindex, nofollow">
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.4/dist/chart.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns@3.0.0/dist/chartjs-adapter-date-fns.bundle.min.js"></script>
<style>
:root {{ --bg:#f7f7f5; --card:#ffffff; --ink:#1b1f24; --muted:#5d6673; --line:#e3e5e8; --pos:#16794f; --neg:#b3261e; --accent:#2b5fd6; --chip:#eef1f5; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --bg:#0f1318; --card:#171c23; --ink:#e8ebef; --muted:#9aa4b2; --line:#2a313b; --pos:#3ecf8e; --neg:#ff6b6b; --accent:#7aa2ff; --chip:#212833; }} }}
:root[data-theme="dark"] {{ --bg:#0f1318; --card:#171c23; --ink:#e8ebef; --muted:#9aa4b2; --line:#2a313b; --pos:#3ecf8e; --neg:#ff6b6b; --accent:#7aa2ff; --chip:#212833; }}
* {{ box-sizing:border-box; }}
body {{ margin:0; background:var(--bg); color:var(--ink); font:15px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif; }}
main {{ max-width:1180px; margin:0 auto; padding:28px 16px 64px; }}
h1 {{ font-size:1.7rem; margin:0 0 4px; letter-spacing:-.01em; }}
h2 {{ font-size:1.15rem; margin:34px 0 10px; }}
p.sub {{ color:var(--muted); margin:0 0 18px; }}
.verdict {{ background:var(--card); border:1px solid var(--line); border-left:4px solid var(--accent); border-radius:10px; padding:14px 18px; margin:16px 0 20px; }}
.kpis {{ display:grid; grid-template-columns:repeat(4,1fr); gap:12px; }}
.kpi {{ background:var(--card); border:1px solid var(--line); border-radius:10px; padding:12px 14px; }}
.kl {{ color:var(--muted); font-size:.8rem; }} .kv {{ font-size:1.45rem; font-weight:650; font-variant-numeric:tabular-nums; }} .ks {{ color:var(--muted); font-size:.78rem; }}
.card {{ background:var(--card); border:1px solid var(--line); border-radius:10px; padding:14px 16px; }}
.tw {{ overflow-x:auto; }}
table {{ border-collapse:collapse; width:100%; font-size:.86rem; font-variant-numeric:tabular-nums; }}
th {{ text-align:left; color:var(--muted); font-weight:550; border-bottom:1px solid var(--line); padding:7px 8px; white-space:nowrap; }}
td {{ border-bottom:1px solid var(--line); padding:7px 8px; white-space:nowrap; }}
td:first-child {{ white-space:normal; min-width:180px; }}
.pos {{ color:var(--pos); }} .neg {{ color:var(--neg); }}
.chart {{ position:relative; height:380px; }}
.grid2 {{ display:grid; grid-template-columns:1fr 1fr; gap:14px; }} .grid2 > * {{ min-width:0; }}
ul {{ padding-left:20px; }} li {{ margin:4px 0; }}
.note {{ color:var(--muted); font-size:.84rem; }}
.chip {{ display:inline-block; background:var(--chip); border-radius:6px; padding:1px 7px; font-size:.8rem; margin:2px 3px 2px 0; }}
@media (max-width:820px) {{ .kpis {{ grid-template-columns:1fr 1fr; }} .grid2 {{ grid-template-columns:1fr; }} .chart {{ height:300px; }} }}
</style></head><body><main>
<h1>V10 Momentum Engine — costed, position-sized backtest</h1>
<p class="sub">{d["replayable"]:,} of {d["ledger_trades"]:,} ledger signals replayed on hourly Binance USDT-M data,
{html.escape(d["entry_min"][:10])} → {html.escape(d["entry_max"][:10])}. One account, $100k start, open positions marked daily and liquidated at the last bar. Paper research, not advice.</p>
{f'<div class="verdict">{f["verdict"]}</div>' if f.get("verdict") else ""}
<div class="kpis">{kpi_html}</div>

{f'<h2>What this shows</h2><div class="card"><ul>{bullets(f["findings"])}</ul></div>' if f.get("findings") else ""}

<h2>Equity curves (log scale)</h2>
<div class="card"><div class="chart"><canvas id="eq"></canvas></div>
<p class="note">Click a legend entry to show or hide a scenario. B and F start hidden.</p></div>

<h2>1–3 · Scenarios, same signals</h2>
<div class="card">{_table(SCEN_HEAD, scen_rows(res["scenarios"]))}
<p class="note">A replays the ledger as recorded (fills at the signal close +0.2%, no fees or funding) at 2% of equity per trade. B keeps that sizing and adds realistic execution. C adds risk-based sizing and caps. D–F repeat C on engine subsets. Profit factor and win rate count open positions at their liquidation value.</p></div>

<h2>1 · What realistic execution does to each trade</h2>
<div class="card">{_table(["Engine", "Closed trades", "Ledger mean", "Next-bar fills, no costs", "Costed mean", "Costed median", "Costed win rate", "Median slippage (round trip)", "Mean funding"], pt_rows)}
<p class="note">Unsized: $10k per trade, so size-driven impact stays small. Costed = next-bar-open fills, {_pct(dflt.get("fee"), 2, False)} taker fee per side, half-spread + square-root impact, and funding paid (the prevailing rate, 8h settlement assumed; credits not counted).</p></div>

<div class="grid2" style="margin-top:14px">
<div class="card"><h3 style="margin:0 0 8px;font-size:1rem">By exit reason</h3>{_table(["Exit reason", "Trades", "Ledger mean", "Next-bar", "Costed"], rs_rows)}</div>
<div class="card"><h3 style="margin:0 0 8px;font-size:1rem">Scenario C by calendar year</h3>{_table(["Year", "Return"], yr_rows)}</div>
</div>

<h2>3 · Each engine on its own (C rules)</h2>
<div class="card">{_table(SCEN_HEAD, scen_rows(res.get("engine_standalone", [])))}</div>

<h2>3 · Walk-forward engine choice</h2>
<div class="card">
<p style="margin-top:0">Engines were picked on the first half of the history (costed per-trade expectancy &gt; 0, before {html.escape(wf.get("split", ""))}), then run from that date with C rules. This tests whether the choice would have held out of sample.</p>
{_table(["Engine", "In-sample expectancy", "Out-of-sample expectancy", "Chosen"], wf_rows)}
<div style="margin-top:12px">{_table(SCEN_HEAD, scen_rows([wf[k] for k in ("all engines", "chosen engines") if k in wf]))}</div></div>

<h2>How much is timing luck? CAGR by start date</h2>
<div class="card"><div class="chart" style="height:300px"><canvas id="disp"></canvas></div>
<p class="note">The same rules started at the beginning of each quarter and run to the end. A robust strategy keeps a similar CAGR whatever the start date.</p></div>

<h2>2 · Sensitivity around C</h2>
<div class="card">{_table(SCEN_HEAD, scen_rows(res.get("sensitivity", [])))}</div>

<h2>Assumptions</h2>
<div class="card"><ul>
<li><b>Fills:</b> the engine decides on a closed hourly bar, so entries and exits fill at the <i>next</i> bar's open. The ledger books the signal bar's close.</li>
<li><b>Fees:</b> {_pct(dflt.get("fee"), 2, False)} per side (Binance USDT-M VIP0 taker).</li>
<li><b>Slippage:</b> half-spread {_pct(dflt.get("half_spread"), 2, False)} + Y·σ<sub>daily</sub>·√(order / 24h volume), with Y = {dflt.get("impact_y")}. Volume and volatility are trailing values known at decision time.</li>
<li><b>Funding:</b> longs pay the prevailing rate, accrued hourly as rate ÷ {dflt.get("funding_interval_h"):g}h and scaled by price drift. Funding <i>received</i> (negative rates) is not counted by default. The stored series is a forward-filled prevailing rate, not settlement records, and a few coins show implausible credits: {credit_note}. Net funding and a 4h interval are shown under Sensitivity.</li>
<li><b>Sizing:</b> risk {_pct(dflt.get("risk_pct"), 2, False)} of equity to the initial stop. Caps: {_pct(dflt.get("max_pos_pct"), 0, False)} of equity per position, {_pct(dflt.get("max_participation"), 1, False)} of 24h volume, {dflt.get("max_gross_pct"):g}× gross exposure, {dflt.get("max_positions")} positions. A signal that doesn't fit is skipped, not queued. A winner is trimmed back to {_pct(dflt.get("trim_pct"), 0, False)} of equity at the daily mark once it passes 1.25× that (fees and impact charged). Without trimming, one or two runners end up as most of the account.</li>
<li><b>Initial stops</b> follow the engine code: entry-candle low (CONTINUATION, PHOENIX_*), −20% (squeeze engines), and the lowest low of the 12-bar arming window for IGNITION (never tighter than the real one). Minimum stop distance for sizing is {_pct(dflt.get("min_stop_dist"), 0, False)}.</li>
<li><b>Not modelled:</b> exits inside the bar (a stop triggers only on an hourly close, as in the engine), delisting gaps, liquidation (gross ≤ {dflt.get("max_gross_pct"):g}×, and positions never go below 0), and survivorship in the symbol list. {d["not_replayable"] and ("Not replayable: " + ", ".join(f"{html.escape(k)} ({v})" for k, v in d["not_replayable"].items()) + ".") or ""}</li>
</ul></div>

{f'<h2>Recommended changes</h2><div class="card"><ul>{bullets(f["actions"])}</ul></div>' if f.get("actions") else ""}
</main>
<script>
const css = n => getComputedStyle(document.documentElement).getPropertyValue(n).trim();
Chart.defaults.color = css('--muted'); Chart.defaults.borderColor = css('--line');
new Chart(document.getElementById('eq'), {{ type: 'line', data: {{ datasets: {json.dumps(datasets)} }},
  options: {{ responsive: true, maintainAspectRatio: false, animation: false, parsing: true, interaction: {{ mode: 'nearest', intersect: false, axis: 'x' }},
    scales: {{ x: {{ type: 'time', time: {{ unit: 'quarter' }} }}, y: {{ type: 'logarithmic', ticks: {{ callback: v => '$' + Number(v).toLocaleString() }} }} }},
    plugins: {{ legend: {{ position: 'bottom', labels: {{ boxWidth: 12 }} }},
      tooltip: {{ callbacks: {{ label: c => c.dataset.label.slice(0, 2) + ' $' + Math.round(c.parsed.y).toLocaleString() }} }} }} }} }});
new Chart(document.getElementById('disp'), {{ type: 'bar', data: {{ datasets: {json.dumps(disp_ds)} }},
  options: {{ responsive: true, maintainAspectRatio: false, animation: false,
    scales: {{ y: {{ title: {{ display: true, text: 'CAGR %' }} }} }}, plugins: {{ legend: {{ position: 'bottom' }} }} }} }});
</script></body></html>"""


def main(argv=None):
    argv = argv or sys.argv[1:]
    bt = Path(argv[0]) if argv else Path("bt")
    findings = json.loads(Path(argv[1]).read_text()) if len(argv) > 1 else None
    res = json.loads((bt / "results.json").read_text())
    out = bt / "backtest_report.html"
    out.write_text(render(res, findings), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
