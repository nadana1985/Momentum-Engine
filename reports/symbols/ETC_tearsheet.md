# Kronos V12: Institutional Symbol Tear Sheet — `ETC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+45.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.58x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+15.30%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+24.3% / -2.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-03-12 23:00` | `2023-03-19 23:00` | 168.0h | `$18.7758` | `$21.0143` | **+11.92%** | **+11.26%** | +20.3% | -4.2% | `time_cap` |
| 2 | Book 2 | `2023-06-20 18:00` | `2023-06-27 18:00` | 168.0h | `$15.6200` | `$18.6413` | **+19.34%** | **+17.68%** | +26.3% | -1.2% | `time_cap` |
| 3 | Book 2 | `2025-05-08 02:00` | `2025-05-15 02:00` | 168.0h | `$16.6465` | `$19.7216` | **+18.47%** | **+16.95%** | +26.2% | -1.0% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `3` | `100.0%` | **`+45.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `ETC`

* **Total Candidate Breakouts Filtered (Vetoed):** `189`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `95` (50.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `64`
* **Saved Capital Losses Avoided:** `+1,417.5%`
* **Missed Upside Forgone:** `-4,271.6%`
* **Net Veto Alpha:** `+-2,854.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `117` | `61.9%` |
| `Core 1: Macro Bear Veto` | `55` | `29.1%` |
| `Core 4: Funding Rate Cap` | `17` | `9.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*