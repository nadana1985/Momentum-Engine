# Kronos V12: Institutional Symbol Tear Sheet — `BTW`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+17.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.19x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+17.36%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`66.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+42.0% / -3.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-10 17:00` | `2026-09-13 11:00` | 66.0h | `$0.4858` | `$0.5779` | **+18.95%** | **+17.36%** | +42.0% | -3.3% | `trail_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `trail_stop` | `1` | `100.0%` | **`+17.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `BTW`

* **Total Candidate Breakouts Filtered (Vetoed):** `54`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `52` (96.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `28`
* **Saved Capital Losses Avoided:** `+1,931.9%`
* **Missed Upside Forgone:** `-1,329.8%`
* **Net Veto Alpha:** `+602.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `41` | `75.9%` |
| `Core 4: Defensible Whale Dump` | `13` | `24.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*