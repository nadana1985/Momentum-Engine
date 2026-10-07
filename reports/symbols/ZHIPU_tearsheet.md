# Kronos V12: Institutional Symbol Tear Sheet — `ZHIPU`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`2` Closed, `1` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-11.2%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.89x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-5.61%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-2.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`51.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+4.7% / -7.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-21 06:00` | `2026-08-24 01:00` | 67.0h | `$142.7259` | `$130.9796` | **-8.23%** | **-8.59%** | +9.1% | -9.5% | `initial_stop` |
| 2 | Book 2 | `2026-09-30 01:00` | `2026-10-01 13:00` | 36.0h | `$83.4681` | `$81.2963` | **-2.60%** | **-2.64%** | +0.3% | -5.6% | `stall_bailout` |
| 3 | Book 2 | `2026-10-05 02:00` | `_Open Live_` | 50.9h | `$83.6386` | `$87.7600` | **+4.93%** | **+4.81%** | +11.0% | -3.0% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |
| `stall_bailout` | `1` | `0.0%` | **`-2.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `ZHIPU`

* **Total Candidate Breakouts Filtered (Vetoed):** `30`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `30` (100.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+253.1%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+253.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `29` | `96.7%` |
| `Core 1: Macro Bear Veto` | `1` | `3.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*