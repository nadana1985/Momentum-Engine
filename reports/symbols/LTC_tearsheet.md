# Kronos V12: Institutional Symbol Tear Sheet — `LTC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `9` (`9` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `9` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`55.6%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.504`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+14.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.15x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.56%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-18.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`248.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.9% / -4.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-10 20:00` | `2021-09-03 13:00` | 569.0h | `$167.3507` | `$200.8208` | **+11.58%** | **+11.05%** | +20.7% | -3.9% | `target_reclaim` |
| 2 | Book 2 | `2022-10-25 19:00` | `2022-10-28 19:00` | 72.0h | `$56.9119` | `$55.0121` | **-3.72%** | **-3.78%** | +1.2% | -6.1% | `stagnation_cut` |
| 3 | Book 3 | `2023-01-30 19:00` | `2023-01-31 03:00` | 8.0h | `$88.3686` | `$95.7300` | **+8.33%** | **+8.00%** | +8.9% | -0.4% | `target_reclaim` |
| 4 | Book 2 | `2023-09-19 09:00` | `2023-09-20 21:00` | 36.0h | `$68.0697` | `$64.4585` | **-5.81%** | **-5.97%** | +0.5% | -7.2% | `stall_bailout` |
| 5 | Book 3 | `2024-02-28 17:00` | `2024-02-28 18:00` | 1.0h | `$70.2620` | `$73.7300` | **+4.94%** | **+4.82%** | +11.2% | -0.4% | `target_reclaim` |
| 6 | Book 4 | `2024-10-15 23:00` | `2024-11-03 13:00` | 446.0h | `$70.9563` | `$66.0807` | **-8.37%** | **-8.67%** | +7.4% | -7.0% | `structural_stop` |
| 7 | Book 3 | `2024-12-05 22:00` | `2024-12-08 22:00` | 72.0h | `$132.9706` | `$134.5129` | **+1.16%** | **+1.15%** | +4.8% | -3.1% | `time_expiry` |
| 8 | Book 4 | `2025-05-08 15:00` | `2025-05-30 16:00` | 529.0h | `$93.2597` | `$86.3403` | **-9.02%** | **-9.38%** | +14.9% | -7.4% | `structural_stop` |
| 9 | Book 1 | `2025-07-18 03:00` | `2025-08-08 03:00` | 504.0h | `$108.0896` | `$121.0965` | **+18.03%** | **+16.80%** | +19.5% | -7.9% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+23.9%`** |
| `structural_stop` | `2` | `0.0%` | **`-18.1%`** |
| `stall_bailout` | `1` | `0.0%` | **`-6.0%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-3.8%`** |
| `time_cap` | `1` | `100.0%` | **`+16.8%`** |
| `time_expiry` | `1` | `100.0%` | **`+1.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `LTC`

* **Total Candidate Breakouts Filtered (Vetoed):** `600`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `316` (52.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `12`
* **Saved Capital Losses Avoided:** `+3,234.7%`
* **Missed Upside Forgone:** `-319.3%`
* **Net Veto Alpha:** `+2,915.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `506` | `84.3%` |
| `Core 1: Macro Bear Veto` | `58` | `9.7%` |
| `Core 4: Funding Rate Cap` | `24` | `4.0%` |
| `Core 4: Defensible Whale Dump` | `4` | `0.7%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `4` | `0.7%` |
| `Core 4: Whale Firewall` | `4` | `0.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*