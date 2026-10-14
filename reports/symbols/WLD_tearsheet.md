# Kronos V12: Institutional Symbol Tear Sheet — `WLD`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `15` (`15` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `15` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`80.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`6.810`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+131.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`3.73x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+8.78%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-13.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`49.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.4% / -4.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-10-06 17:00` | `2023-10-09 09:00` | 64.0h | `$1.6563` | `$1.5200` | **-9.16%** | **-9.56%** | +1.9% | -10.8% | `initial_stop` |
| 2 | Book 3 | `2023-11-13 21:00` | `2023-11-16 01:00` | 52.0h | `$2.2778` | `$2.4759` | **+8.70%** | **+8.34%** | +10.0% | -7.5% | `target_reclaim` |
| 3 | Book 3 | `2023-11-28 05:00` | `2023-12-01 05:00` | 72.0h | `$2.4230` | `$2.4947` | **+2.96%** | **+2.92%** | +9.0% | -4.5% | `time_expiry` |
| 4 | Book 3 | `2023-12-16 11:00` | `2023-12-16 14:00` | 3.0h | `$2.9515` | `$3.2082` | **+8.70%** | **+8.34%** | +11.8% | -1.4% | `target_reclaim` |
| 5 | Book 3 | `2024-02-18 21:00` | `2024-02-19 03:00` | 6.0h | `$5.7620` | `$6.2630` | **+8.70%** | **+8.34%** | +12.0% | -1.7% | `target_reclaim` |
| 6 | Book 3 | `2024-02-20 15:00` | `2024-02-20 21:00` | 6.0h | `$6.1912` | `$6.7296` | **+8.70%** | **+8.34%** | +8.9% | -0.6% | `target_reclaim` |
| 7 | Book 3 | `2024-03-11 00:00` | `2024-03-11 07:00` | 7.0h | `$8.8513` | `$10.2173` | **+15.43%** | **+14.35%** | +16.9% | -0.6% | `target_reclaim` |
| 8 | Book 2 | `2024-10-11 14:00` | `2024-10-16 07:00` | 113.0h | `$1.9456` | `$2.2469` | **+18.24%** | **+16.95%** | +36.2% | -3.6% | `trail_stop` |
| 9 | Book 3 | `2024-12-05 22:00` | `2024-12-06 01:00` | 3.0h | `$3.7288` | `$4.0530` | **+8.70%** | **+8.34%** | +12.6% | -5.5% | `target_reclaim` |
| 10 | Book 1 | `2025-04-22 21:00` | `2025-04-25 11:00` | 62.0h | `$0.8267` | `$0.9920` | **+29.39%** | **+25.70%** | +20.6% | -3.2% | `target_reclaim` |
| 11 | Book 2 | `2025-05-08 15:00` | `2025-05-15 15:00` | 168.0h | `$1.0265` | `$1.1933` | **+19.41%** | **+17.98%** | +32.6% | -2.7% | `time_cap` |
| 12 | Book 2 | `2025-06-10 11:00` | `2025-06-12 08:00` | 45.0h | `$1.1828` | `$1.0855` | **-9.13%** | **-9.53%** | +3.1% | -8.0% | `initial_stop` |
| 13 | Book 1 | `2025-07-10 21:00` | `2025-07-14 20:00` | 95.0h | `$1.0550` | `$1.0332` | **-3.54%** | **-3.59%** | +8.1% | -6.0% | `fast_decay_cut` |
| 14 | Book 4 | `2026-06-03 07:00` | `2026-06-03 21:00` | 14.0h | `$0.4575` | `$0.5490` | **+5.79%** | **+5.65%** | +23.9% | -3.6% | `target_reclaim` |
| 15 | Book 1 | `2026-08-20 17:00` | `2026-08-22 04:00` | 35.0h | `$0.3749` | `$0.4499` | **+33.35%** | **+29.17%** | +23.6% | -3.3% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `9` | `100.0%` | **`+116.6%`** |
| `initial_stop` | `2` | `0.0%` | **`-19.1%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-3.6%`** |
| `time_cap` | `1` | `100.0%` | **`+18.0%`** |
| `time_expiry` | `1` | `100.0%` | **`+2.9%`** |
| `trail_stop` | `1` | `100.0%` | **`+17.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `WLD`

* **Total Candidate Breakouts Filtered (Vetoed):** `608`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `397` (65.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `191`
* **Saved Capital Losses Avoided:** `+5,835.4%`
* **Missed Upside Forgone:** `-7,143.2%`
* **Net Veto Alpha:** `+-1,307.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `579` | `95.2%` |
| `Core 4: Funding Rate Cap` | `15` | `2.5%` |
| `Core 4: Defensible Whale Dump` | `8` | `1.3%` |
| `Core 4: Whale Firewall` | `6` | `1.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*