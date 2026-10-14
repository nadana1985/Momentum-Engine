# Kronos V12: Institutional Symbol Tear Sheet — `CAKE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`85.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`12.068`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+95.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.59x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+13.58%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`112.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+22.8% / -6.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-12-29 01:00` | `2023-12-29 09:00` | 8.0h | `$3.5201` | `$3.8092` | **+8.21%** | **+7.89%** | +9.3% | -1.6% | `target_reclaim` |
| 2 | Book 3 | `2024-03-05 19:00` | `2024-03-07 14:00` | 43.0h | `$2.9664` | `$3.4474` | **+16.21%** | **+15.03%** | +17.5% | -15.0% | `target_reclaim` |
| 3 | Book 4 | `2024-11-23 01:00` | `2024-11-24 06:00` | 29.0h | `$2.1526` | `$2.5831` | **+12.74%** | **+11.35%** | +20.6% | -5.6% | `target_reclaim` |
| 4 | Book 5 (Shelf Absorption Squeeze) | `2025-03-15 16:00` | `2025-03-19 16:00` | Live | `$1.7630` | `$1.9129` | **+8.50%** | **+8.16%** | +48.7% | -9.4% | `shelf_target_reclaim` |
| 5 | Book 3 | `2025-05-30 00:00` | `2025-05-30 22:00` | 22.0h | `$2.5138` | `$2.3069` | **-8.23%** | **-8.59%** | +4.6% | -9.1% | `stop_loss` |
| 6 | Book 4 | `2026-08-19 06:00` | `2026-08-22 04:00` | 70.0h | `$1.5441` | `$1.8529` | **+23.74%** | **+21.65%** | +20.6% | -0.8% | `target_reclaim` |
| 7 | Book 1 | `2026-09-03 08:00` | `2026-09-24 08:00` | 504.0h | `$1.9759` | `$2.6474` | **+46.64%** | **+39.57%** | +38.0% | -5.1% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+55.9%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_cap` | `1` | `100.0%` | **`+39.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `CAKE`

* **Total Candidate Breakouts Filtered (Vetoed):** `86`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `39` (45.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `11`
* **Saved Capital Losses Avoided:** `+394.1%`
* **Missed Upside Forgone:** `-272.7%`
* **Net Veto Alpha:** `+121.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `66` | `76.7%` |
| `Core 4: Funding Rate Cap` | `19` | `22.1%` |
| `Core 4: Whale Firewall` | `1` | `1.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*