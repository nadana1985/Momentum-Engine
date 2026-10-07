# Kronos V12: Institutional Symbol Tear Sheet — `ADA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `9` (`9` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `9` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`9.128`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+41.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.51x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+4.60%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-4.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`147.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.0% / -3.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-10-25 14:00` | `2022-11-01 14:00` | 168.0h | `$0.3720` | `$0.4008` | **+7.73%** | **+7.45%** | +18.2% | -1.5% | `time_cap` |
| 2 | Book 2 | `2022-12-13 13:00` | `2022-12-15 01:00` | 36.0h | `$0.3159` | `$0.3019` | **-4.41%** | **-4.51%** | +0.9% | -4.6% | `stall_bailout` |
| 3 | Book 1 | `2023-01-13 21:00` | `2023-01-16 08:00` | 59.0h | `$0.3487` | `$0.3473` | **-0.26%** | **-0.26%** | +6.3% | -4.9% | `fast_decay_cut` |
| 4 | Book 2 | `2023-03-12 23:00` | `2023-03-19 23:00` | 168.0h | `$0.3308` | `$0.3438` | **+3.93%** | **+3.86%** | +11.3% | -4.5% | `time_cap` |
| 5 | Book 2 | `2023-07-13 16:00` | `2023-07-14 18:00` | 26.0h | `$0.3190` | `$0.3198` | **+0.21%** | **+0.21%** | +19.0% | -2.9% | `breakeven_ratchet` |
| 6 | Book 1 | `2023-11-02 18:00` | `2023-11-04 19:00` | 49.0h | `$0.3249` | `$0.3233` | **-0.31%** | **-0.31%** | +1.7% | -4.1% | `fast_decay_cut` |
| 7 | Book 2 | `2025-04-22 14:00` | `2025-04-29 14:00` | 168.0h | `$0.6605` | `$0.7133` | **+7.99%** | **+7.69%** | +12.9% | -1.7% | `time_cap` |
| 8 | Book 2 | `2025-05-08 03:00` | `2025-05-15 03:00` | 168.0h | `$0.7044` | `$0.7898` | **+12.13%** | **+11.45%** | +22.7% | -1.2% | `time_cap` |
| 9 | Book 1 | `2025-07-10 17:00` | `2025-07-30 19:00` | 482.0h | `$0.6591` | `$0.7382` | **+17.15%** | **+15.83%** | +41.8% | -3.2% | `trail_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `4` | `100.0%` | **`+30.4%`** |
| `fast_decay_cut` | `2` | `0.0%` | **`-0.6%`** |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.2%`** |
| `stall_bailout` | `1` | `0.0%` | **`-4.5%`** |
| `trail_stop` | `1` | `100.0%` | **`+15.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `ADA`

* **Total Candidate Breakouts Filtered (Vetoed):** `225`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `115` (51.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `55`
* **Saved Capital Losses Avoided:** `+1,364.7%`
* **Missed Upside Forgone:** `-1,926.7%`
* **Net Veto Alpha:** `+-562.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `134` | `59.6%` |
| `Core 1: Macro Bear Veto` | `67` | `29.8%` |
| `Core 4: Funding Rate Cap` | `24` | `10.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*