# Kronos V12: Institutional Symbol Tear Sheet — `UNI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `11` (`11` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `11` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`27.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`2.732`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+42.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.54x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+3.90%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-12.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`114.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.4% / -5.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2022-10-30 01:00` | `2022-11-01 01:00` | 48.0h | `$7.2581` | `$6.9715` | **-2.35%** | **-2.38%** | +1.5% | -7.8% | `fast_decay_cut` |
| 2 | Book 1 | `2023-01-12 07:00` | `2023-01-18 20:00` | 157.0h | `$6.0882` | `$6.0598` | **-0.61%** | **-0.61%** | +14.5% | -3.9% | `fast_decay_cut` |
| 3 | Book 2 | `2023-04-14 00:00` | `2023-04-17 00:00` | 72.0h | `$6.3779` | `$6.0897` | **-4.52%** | **-4.62%** | +2.0% | -4.4% | `stagnation_cut` |
| 4 | Book 1 | `2023-06-25 07:00` | `2023-06-28 01:00` | 66.0h | `$5.2631` | `$5.1581` | **-1.37%** | **-1.38%** | +5.5% | -2.3% | `fast_decay_cut` |
| 5 | Book 2 | `2023-07-13 16:00` | `2023-07-20 16:00` | 168.0h | `$5.6431` | `$5.9112` | **+4.75%** | **+4.64%** | +11.2% | -2.7% | `time_cap` |
| 6 | Book 2 | `2023-09-19 09:00` | `2023-09-20 21:00` | 36.0h | `$4.4701` | `$4.3631` | **-2.40%** | **-2.42%** | +0.2% | -3.8% | `stall_bailout` |
| 7 | Book 1 | `2023-11-09 06:00` | `2023-11-12 00:00` | 66.0h | `$5.3032` | `$5.2598` | **-0.48%** | **-0.48%** | +4.5% | -13.6% | `fast_decay_cut` |
| 8 | Book 2 | `2024-05-15 15:00` | `2024-05-22 15:00` | 168.0h | `$7.2771` | `$9.2558` | **+27.19%** | **+24.05%** | +33.3% | -3.2% | `time_cap` |
| 9 | Book 2 | `2024-09-13 15:00` | `2024-09-15 03:00` | 36.0h | `$7.0506` | `$6.7232` | **-4.64%** | **-4.76%** | +0.5% | -6.8% | `stall_bailout` |
| 10 | Book 2 | `2025-06-29 09:00` | `2025-07-01 23:00` | 62.0h | `$7.2370` | `$6.6745` | **-7.77%** | **-8.09%** | +3.7% | -9.1% | `initial_stop` |
| 11 | Book 1 | `2025-07-05 22:00` | `2025-07-21 14:00` | 376.0h | `$7.3824` | `$11.2787` | **+47.58%** | **+38.92%** | +59.2% | -5.1% | `climax_top_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `4` | `0.0%` | **`-4.9%`** |
| `time_cap` | `2` | `100.0%` | **`+28.7%`** |
| `stall_bailout` | `2` | `0.0%` | **`-7.2%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+38.9%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-4.6%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `UNI`

* **Total Candidate Breakouts Filtered (Vetoed):** `182`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `116` (63.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `28`
* **Saved Capital Losses Avoided:** `+1,549.2%`
* **Missed Upside Forgone:** `-819.5%`
* **Net Veto Alpha:** `+729.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `86` | `47.3%` |
| `Core 1: Macro Bear Veto` | `74` | `40.7%` |
| `Core 4: Funding Rate Cap` | `13` | `7.1%` |
| `Core 4: Whale Firewall` | `8` | `4.4%` |
| `Core 4: Defensible Whale Dump` | `1` | `0.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*