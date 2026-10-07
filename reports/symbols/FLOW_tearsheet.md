# Kronos V12: Institutional Symbol Tear Sheet — `FLOW`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+14.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.15x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+13.97%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+18.7% / -2.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-03-12 23:00` | `2023-03-19 23:00` | 168.0h | `$0.9333` | `$1.0733` | **+15.00%** | **+13.97%** | +18.7% | -2.6% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `1` | `100.0%` | **`+14.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `FLOW`

* **Total Candidate Breakouts Filtered (Vetoed):** `212`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `124` (58.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `19`
* **Saved Capital Losses Avoided:** `+1,362.5%`
* **Missed Upside Forgone:** `-598.1%`
* **Net Veto Alpha:** `+764.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `83` | `39.2%` |
| `Core 1: Macro Bear Veto` | `52` | `24.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `52` | `24.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `19` | `9.0%` |
| `Core 0: Zero-Tolerance Data Firewall` | `6` | `2.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*