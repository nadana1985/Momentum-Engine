# Kronos V12: Institutional Symbol Tear Sheet — `ICP`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `9` (`9` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `9` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.307`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+61.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.84x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+6.80%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-9.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`76.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.9% / -7.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2023-01-14 23:00` | `2023-01-27 17:00` | 306.0h | `$5.0756` | `$6.0907` | **+8.09%** | **+7.83%** | +22.2% | -4.9% | `target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2023-04-29 02:00` | `2023-05-03 02:00` | Live | `$5.7279` | `$6.2148` | **+8.50%** | **+8.16%** | +4.9% | -21.2% | `shelf_target_reclaim` |
| 3 | Book 2 | `2023-06-21 16:00` | `2023-06-24 16:00` | 72.0h | `$4.2556` | `$4.2045` | **-1.33%** | **-1.33%** | +3.6% | -3.7% | `stagnation_cut` |
| 4 | Book 3 | `2023-12-31 20:00` | `2024-01-02 00:00` | 28.0h | `$13.5421` | `$12.4276` | **-8.23%** | **-8.59%** | +4.1% | -8.0% | `stop_loss` |
| 5 | Book 3 | `2024-02-15 05:00` | `2024-02-15 14:00` | 9.0h | `$13.1990` | `$13.7490` | **+4.17%** | **+4.08%** | +4.9% | -1.1% | `target_reclaim` |
| 6 | Book 3 | `2024-03-05 19:00` | `2024-03-06 17:00` | 22.0h | `$13.3606` | `$15.5510` | **+16.39%** | **+15.18%** | +17.2% | -15.2% | `target_reclaim` |
| 7 | Book 3 | `2024-03-27 19:00` | `2024-03-28 14:00` | 19.0h | `$18.9575` | `$17.3973` | **-8.23%** | **-8.59%** | +2.3% | -8.4% | `stop_loss` |
| 8 | Book 3 | `2024-11-13 03:00` | `2024-11-16 03:00` | 72.0h | `$8.3715` | `$9.0533` | **+8.14%** | **+7.83%** | +8.5% | -6.5% | `time_expiry` |
| 9 | Book 2 | `2026-05-05 11:00` | `2026-05-08 20:00` | 81.0h | `$2.4902` | `$3.4464` | **+43.30%** | **+36.65%** | +48.8% | -1.1% | `climax_top_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+27.1%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+36.6%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-1.3%`** |
| `time_expiry` | `1` | `100.0%` | **`+7.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `ICP`

* **Total Candidate Breakouts Filtered (Vetoed):** `382`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `297` (77.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `92`
* **Saved Capital Losses Avoided:** `+4,855.4%`
* **Missed Upside Forgone:** `-5,196.0%`
* **Net Veto Alpha:** `+-340.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `367` | `96.1%` |
| `Core 4: Funding Rate Cap` | `14` | `3.7%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*