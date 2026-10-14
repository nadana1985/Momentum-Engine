# Kronos V12: Institutional Symbol Tear Sheet — `DUSK`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`9.890`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+51.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.68x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+8.61%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-5.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`157.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+19.0% / -8.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2022-06-13 10:00` | `2022-06-17 10:00` | Live | `$0.1269` | `$0.1377` | **+8.50%** | **+8.16%** | +11.6% | -25.6% | `shelf_target_reclaim` |
| 2 | Book 1 | `2023-01-09 16:00` | `2023-01-11 04:00` | 36.0h | `$0.0945` | `$0.0913` | **-5.26%** | **-5.40%** | +0.5% | -4.7% | `stall_bailout` |
| 3 | Book 4 | `2023-10-25 14:00` | `2023-11-11 17:00` | 411.0h | `$0.1262` | `$0.1515` | **+23.43%** | **+21.40%** | +45.3% | -5.3% | `target_reclaim` |
| 4 | Book 4 | `2024-11-26 05:00` | `2024-11-30 22:00` | 113.0h | `$0.2323` | `$0.2788` | **+24.43%** | **+22.24%** | +20.7% | -11.7% | `target_reclaim` |
| 5 | Book 1 | `2025-04-21 12:00` | `2025-04-30 13:00` | 217.0h | `$0.0819` | `$0.0816` | **-0.41%** | **-0.41%** | +15.5% | -4.1% | `fast_decay_cut` |
| 6 | Book 4 | `2026-01-12 10:00` | `2026-01-12 22:00` | 12.0h | `$0.0630` | `$0.0756` | **+5.79%** | **+5.65%** | +20.6% | -1.0% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+49.3%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.4%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stall_bailout` | `1` | `0.0%` | **`-5.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `DUSK`

* **Total Candidate Breakouts Filtered (Vetoed):** `933`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `562` (60.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `304`
* **Saved Capital Losses Avoided:** `+10,988.0%`
* **Missed Upside Forgone:** `-23,456.4%`
* **Net Veto Alpha:** `+-12,468.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `517` | `55.4%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `394` | `42.2%` |
| `Core 4: Funding Rate Cap` | `10` | `1.1%` |
| `Core 0: Zero-Tolerance Data Firewall` | `9` | `1.0%` |
| `Core 4: Whale Firewall` | `2` | `0.2%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*