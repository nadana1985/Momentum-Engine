# Kronos V12: Institutional Symbol Tear Sheet — `ETHFI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+73.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.09x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+14.78%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`55.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+18.6% / -3.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2024-11-24 18:00` | `2024-11-27 23:00` | 77.0h | `$2.1428` | `$2.5714` | **+11.58%** | **+11.05%** | +20.8% | -7.2% | `target_reclaim` |
| 2 | Book 3 | `2024-12-05 01:00` | `2024-12-05 04:00` | 3.0h | `$2.5625` | `$2.7676` | **+8.01%** | **+7.70%** | +8.1% | -0.7% | `target_reclaim` |
| 3 | Book 4 | `2025-05-13 17:00` | `2025-05-15 15:00` | 46.0h | `$1.2701` | `$1.4987` | **+18.13%** | **+16.67%** | +28.5% | -2.1% | `climax_whale_euphoria_harvest` |
| 4 | Book 1 | `2025-07-09 21:00` | `2025-07-11 04:00` | 31.0h | `$1.0790` | `$1.2408` | **+26.89%** | **+24.26%** | +15.2% | -4.0% | `target_reclaim` |
| 5 | Book 4 | `2026-08-15 13:00` | `2026-08-20 11:00` | 118.0h | `$0.4864` | `$0.5837` | **+15.06%** | **+14.19%** | +20.4% | -3.5% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+57.2%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+16.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `ETHFI`

* **Total Candidate Breakouts Filtered (Vetoed):** `121`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `34` (28.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `40`
* **Saved Capital Losses Avoided:** `+309.2%`
* **Missed Upside Forgone:** `-1,214.7%`
* **Net Veto Alpha:** `+-905.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `121` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*