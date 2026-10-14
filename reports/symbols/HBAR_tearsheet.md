# Kronos V12: Institutional Symbol Tear Sheet — `HBAR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `13` (`13` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `13` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`69.2%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`5.046`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+105.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.88x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+8.15%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-18.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`129.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.2% / -9.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-23 03:00` | `2021-09-04 19:00` | 304.0h | `$0.2527` | `$0.3032` | **+11.58%** | **+11.05%** | +20.3% | -9.6% | `target_reclaim` |
| 2 | Book 2 | `2023-01-09 14:00` | `2023-01-16 14:00` | 168.0h | `$0.0446` | `$0.0520` | **+20.13%** | **+18.63%** | +22.6% | -3.3% | `time_cap` |
| 3 | Book 4 | `2023-01-27 16:00` | `2023-02-03 16:00` | 168.0h | `$0.0694` | `$0.0693` | **+3.53%** | **+3.48%** | +2.6% | -10.3% | `stagnation_cut` |
| 4 | Book 2 | `2023-04-26 08:00` | `2023-04-26 20:00` | 12.0h | `$0.0622` | `$0.0582` | **-6.80%** | **-7.03%** | +1.9% | -6.7% | `initial_stop` |
| 5 | Book 5 (Shelf Absorption Squeeze) | `2023-07-19 06:00` | `2023-07-23 06:00` | Live | `$0.0522` | `$0.0566` | **+8.50%** | **+8.16%** | +1.0% | -11.9% | `shelf_target_reclaim` |
| 6 | Book 4 | `2023-10-26 08:00` | `2023-11-02 08:00` | 168.0h | `$0.0541` | `$0.0551` | **+1.80%** | **+1.79%** | +2.6% | -8.0% | `stagnation_cut` |
| 7 | Book 1 | `2023-11-17 06:00` | `2023-11-19 06:00` | 48.0h | `$0.0662` | `$0.0614` | **-9.56%** | **-9.96%** | +3.3% | -10.0% | `fast_decay_cut` |
| 8 | Book 3 | `2024-01-03 12:00` | `2024-01-05 14:00` | 50.0h | `$0.0893` | `$0.0820` | **-8.23%** | **-8.59%** | +3.9% | -15.6% | `stop_loss` |
| 9 | Book 3 | `2024-03-03 07:00` | `2024-03-05 00:00` | 41.0h | `$0.1080` | `$0.1206` | **+11.70%** | **+11.06%** | +14.3% | -1.8% | `target_reclaim` |
| 10 | Book 3 | `2024-03-05 19:00` | `2024-03-06 21:00` | 26.0h | `$0.1109` | `$0.1249` | **+12.57%** | **+11.84%** | +14.0% | -16.5% | `target_reclaim` |
| 11 | Book 5 (Shelf Absorption Squeeze) | `2024-04-23 19:00` | `2024-04-27 19:00` | Live | `$0.1156` | `$0.1254` | **+8.50%** | **+8.16%** | +12.1% | -28.5% | `shelf_target_reclaim` |
| 12 | Book 1 | `2024-09-26 18:00` | `2024-09-29 18:00` | 72.0h | `$0.0621` | `$0.0618` | **-0.60%** | **-0.61%** | +2.8% | -3.9% | `stagnation_bailout` |
| 13 | Book 1 | `2025-07-10 02:00` | `2025-07-25 12:00` | 370.0h | `$0.1749` | `$0.2496` | **+74.99%** | **+57.97%** | +70.8% | -1.5% | `climax_top_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+34.0%`** |
| `stagnation_cut` | `2` | `100.0%` | **`+5.3%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+58.0%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-10.0%`** |
| `stagnation_bailout` | `1` | `0.0%` | **`-0.6%`** |
| `initial_stop` | `1` | `0.0%` | **`-7.0%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_cap` | `1` | `100.0%` | **`+18.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `HBAR`

* **Total Candidate Breakouts Filtered (Vetoed):** `253`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `206` (81.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `13`
* **Saved Capital Losses Avoided:** `+2,623.2%`
* **Missed Upside Forgone:** `-381.3%`
* **Net Veto Alpha:** `+2,242.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `182` | `71.9%` |
| `Core 1: Macro Bear Veto` | `55` | `21.7%` |
| `Core 4: Funding Rate Cap` | `14` | `5.5%` |
| `Core 4: Whale Firewall` | `1` | `0.4%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*