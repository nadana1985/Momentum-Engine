# Kronos V12: Institutional Symbol Tear Sheet — `AERO`
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
| **Cumulative Net Log Return** | **`+77.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.16x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+25.67%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+37.5% / -3.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2025-04-22 15:00` | `2025-04-29 15:00` | 168.0h | `$0.4278` | `$0.6181` | **+44.48%** | **+36.80%** | +55.5% | -1.6% | `time_cap` |
| 2 | Book 2 | `2025-07-09 19:00` | `2025-07-16 19:00` | 168.0h | `$0.7480` | `$0.9868` | **+31.93%** | **+27.71%** | +33.4% | -3.9% | `time_cap` |
| 3 | Book 2 | `2026-09-17 13:00` | `2026-09-24 13:00` | 168.0h | `$0.5970` | `$0.6764` | **+13.30%** | **+12.49%** | +23.7% | -3.6% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `3` | `100.0%` | **`+77.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `AERO`

* **Total Candidate Breakouts Filtered (Vetoed):** `54`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `47` (87.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `3`
* **Saved Capital Losses Avoided:** `+595.7%`
* **Missed Upside Forgone:** `-64.2%`
* **Net Veto Alpha:** `+531.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `49` | `90.7%` |
| `Core 4: Defensible Whale Dump` | `3` | `5.6%` |
| `Core 4: Funding Rate Cap` | `2` | `3.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*