# Kronos V12: Institutional Symbol Tear Sheet — `DOGE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `8` (`8` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `8` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`62.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.192`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+29.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.34x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.65%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`26.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+20.6% / -6.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-10-27 19:00` | `2022-10-27 22:00` | 3.0h | `$0.0831` | `$0.0762` | **-7.08%** | **-7.34%** | +2.9% | -8.2% | `initial_stop` |
| 2 | Book 1 | `2022-10-28 12:00` | `2022-10-30 15:00` | 51.0h | `$0.0836` | `$0.1136` | **+20.11%** | **+18.32%** | +81.6% | -4.1% | `trail_stop` |
| 3 | Book 3 | `2023-11-16 15:00` | `2023-11-17 06:00` | 15.0h | `$0.0762` | `$0.0828` | **+8.70%** | **+8.34%** | +8.8% | -0.3% | `target_reclaim` |
| 4 | Book 3 | `2024-02-20 15:00` | `2024-02-23 15:00` | 72.0h | `$0.0820` | `$0.0836` | **+1.93%** | **+1.91%** | +5.5% | -0.3% | `time_expiry` |
| 5 | Book 3 | `2024-03-03 07:00` | `2024-03-03 11:00` | 4.0h | `$0.1286` | `$0.1398` | **+8.70%** | **+8.34%** | +11.2% | -6.8% | `target_reclaim` |
| 6 | Book 3 | `2024-03-05 19:00` | `2024-03-05 20:00` | 1.0h | `$0.1451` | `$0.1332` | **-8.23%** | **-8.59%** | +10.0% | -17.1% | `stop_loss` |
| 7 | Book 2 | `2024-11-11 15:00` | `2024-11-12 05:00` | 14.0h | `$0.3108` | `$0.3989` | **+18.35%** | **+16.84%** | +36.1% | -7.0% | `climax_top_harvest` |
| 8 | Book 3 | `2024-11-23 16:00` | `2024-11-25 22:00` | 54.0h | `$0.4205` | `$0.3859` | **-8.23%** | **-8.59%** | +9.1% | -9.4% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `initial_stop` | `1` | `0.0%` | **`-7.3%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+16.8%`** |
| `time_expiry` | `1` | `100.0%` | **`+1.9%`** |
| `trail_stop` | `1` | `100.0%` | **`+18.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `DOGE`

* **Total Candidate Breakouts Filtered (Vetoed):** `146`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `92` (63.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `59`
* **Saved Capital Losses Avoided:** `+1,584.8%`
* **Missed Upside Forgone:** `-6,296.1%`
* **Net Veto Alpha:** `+-4,711.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `69` | `47.3%` |
| `Core 1: Macro Bear Veto` | `46` | `31.5%` |
| `Core 4: Funding Rate Cap` | `31` | `21.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*