# Kronos V12: Institutional Symbol Tear Sheet — `FET`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.675`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-2.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.97x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.39%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`128.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.2% / -5.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2025-05-08 15:00` | `2025-05-15 15:00` | 168.0h | `$0.7445` | `$0.7889` | **+5.97%** | **+5.80%** | +22.8% | -2.1% | `time_cap` |
| 2 | Book 2 | `2026-09-06 20:00` | `2026-09-10 12:00` | 88.0h | `$0.1768` | `$0.1623` | **-8.23%** | **-8.59%** | +7.6% | -8.6% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |
| `time_cap` | `1` | `100.0%` | **`+5.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `FET`

* **Total Candidate Breakouts Filtered (Vetoed):** `115`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `55` (47.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `43`
* **Saved Capital Losses Avoided:** `+717.7%`
* **Missed Upside Forgone:** `-1,517.3%`
* **Net Veto Alpha:** `+-799.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `73` | `63.5%` |
| `Core 4: Funding Rate Cap` | `42` | `36.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*