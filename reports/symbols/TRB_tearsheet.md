# Kronos V12: Institutional Symbol Tear Sheet — `TRB`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `9` (`9` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `9` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`9.327`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+67.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.96x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+7.48%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-4.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`195.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.3% / -10.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-13 23:00` | `2021-08-21 10:00` | 179.0h | `$50.5357` | `$60.6428` | **+12.72%** | **+12.09%** | +20.8% | -7.1% | `target_reclaim` |
| 2 | Book 1 | `2022-03-27 01:00` | `2022-03-31 08:00` | 103.0h | `$22.6164` | `$27.1397` | **+27.05%** | **+23.66%** | +23.0% | -3.6% | `target_reclaim` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2022-06-08 06:00` | `2022-06-12 06:00` | Live | `$12.8340` | `$13.9249` | **+8.50%** | **+8.16%** | +26.3% | -35.9% | `shelf_target_reclaim` |
| 4 | Book 5 (Shelf Absorption Squeeze) | `2022-12-17 23:00` | `2022-12-21 23:00` | Live | `$12.3464` | `$13.3958` | **+8.50%** | **+8.16%** | +6.9% | -13.0% | `shelf_target_reclaim` |
| 5 | Book 4 | `2023-01-24 05:00` | `2023-02-04 16:00` | 275.0h | `$16.5648` | `$19.8778` | **+12.93%** | **+12.28%** | +24.7% | -10.9% | `target_reclaim` |
| 6 | Book 1 | `2023-04-10 07:00` | `2023-04-11 19:00` | 36.0h | `$15.9899` | `$15.6209` | **-4.27%** | **-4.35%** | +3.8% | -3.2% | `fast_decay_cut` |
| 7 | Book 2 | `2024-09-13 17:00` | `2024-09-15 17:00` | 48.0h | `$64.4758` | `$64.1652` | **-0.54%** | **-0.54%** | +3.9% | -1.8% | `fast_decay_cut` |
| 8 | Book 4 | `2025-05-27 10:00` | `2025-05-27 16:00` | 6.0h | `$43.1797` | `$51.8156` | **+11.58%** | **+11.05%** | +31.7% | -1.7% | `target_reclaim` |
| 9 | Book 4 | `2026-08-22 05:00` | `2026-09-21 04:00` | 719.0h | `$18.6299` | `$18.0040` | **-3.14%** | **-3.19%** | +5.9% | -13.9% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+59.1%`** |
| `fast_decay_cut` | `2` | `0.0%` | **`-4.9%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `time_expiry` | `1` | `0.0%` | **`-3.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `TRB`

* **Total Candidate Breakouts Filtered (Vetoed):** `1226`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `836` (68.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `236`
* **Saved Capital Losses Avoided:** `+12,749.5%`
* **Missed Upside Forgone:** `-8,731.9%`
* **Net Veto Alpha:** `+4,017.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `498` | `40.6%` |
| `Core 0: Zero-Tolerance Data Firewall` | `373` | `30.4%` |
| `Core 1: Macro Bear Veto` | `340` | `27.7%` |
| `Core 4: Defensible Whale Dump` | `12` | `1.0%` |
| `Core 4: Funding Rate Cap` | `3` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*