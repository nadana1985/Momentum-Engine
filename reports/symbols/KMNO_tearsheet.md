# Kronos V12: Institutional Symbol Tear Sheet — `KMNO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `13` (`13` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `13` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`69.2%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.720`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+22.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.26x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.76%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`23.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.7% / -6.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-01-26 15:00` | `2025-01-30 15:00` | Live | `$0.1210` | `$0.1111` | **-8.20%** | **-8.56%** | +-6.7% | -45.8% | `shelf_stop_loss` |
| 2 | Book 3 | `2025-04-27 01:00` | `2025-04-27 09:00` | 8.0h | `$0.0609` | `$0.0634` | **+4.17%** | **+4.08%** | +4.8% | -1.2% | `target_reclaim` |
| 3 | Book 3 | `2025-04-30 17:00` | `2025-05-01 03:00` | 10.0h | `$0.0623` | `$0.0699` | **+12.13%** | **+11.45%** | +23.7% | -0.5% | `target_reclaim` |
| 4 | Book 3 | `2025-05-05 15:00` | `2025-05-05 17:00` | 2.0h | `$0.0747` | `$0.0778` | **+4.17%** | **+4.08%** | +8.4% | -0.1% | `target_reclaim` |
| 5 | Book 3 | `2025-05-06 15:00` | `2025-05-06 22:00` | 7.0h | `$0.0752` | `$0.0802` | **+6.70%** | **+6.48%** | +19.7% | -3.2% | `target_reclaim` |
| 6 | Book 3 | `2025-07-18 15:00` | `2025-07-21 02:00` | 59.0h | `$0.0635` | `$0.0662` | **+4.17%** | **+4.08%** | +4.2% | -3.9% | `target_reclaim` |
| 7 | Book 3 | `2025-07-23 12:00` | `2025-07-23 20:00` | 8.0h | `$0.0645` | `$0.0592` | **-8.23%** | **-8.59%** | +0.5% | -8.1% | `stop_loss` |
| 8 | Book 3 | `2025-08-14 16:00` | `2025-08-17 16:00` | 72.0h | `$0.0612` | `$0.0624` | **+1.93%** | **+1.91%** | +5.3% | -5.6% | `time_expiry` |
| 9 | Book 3 | `2025-10-29 18:00` | `2025-10-29 21:00` | 3.0h | `$0.0632` | `$0.0681` | **+7.90%** | **+7.60%** | +8.7% | -0.1% | `target_reclaim` |
| 10 | Book 3 | `2026-08-25 19:00` | `2026-08-26 03:00` | 8.0h | `$0.0261` | `$0.0240` | **-8.23%** | **-8.59%** | +1.0% | -8.3% | `stop_loss` |
| 11 | Book 4 | `2026-08-26 18:00` | `2026-08-27 17:00` | 23.0h | `$0.0254` | `$0.0305` | **+11.58%** | **+11.05%** | +22.6% | -0.9% | `target_reclaim` |
| 12 | Book 3 | `2026-08-28 17:00` | `2026-08-31 17:00` | 72.0h | `$0.0260` | `$0.0244` | **-5.97%** | **-6.15%** | +2.0% | -6.8% | `time_expiry` |
| 13 | Book 3 | `2026-09-25 01:00` | `2026-09-25 09:00` | 8.0h | `$0.0368` | `$0.0383` | **+4.17%** | **+4.08%** | +5.7% | -1.7% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `8` | `100.0%` | **`+52.9%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `time_expiry` | `2` | `50.0%` | **`-4.2%`** |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `KMNO`

* **Total Candidate Breakouts Filtered (Vetoed):** `189`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `141` (74.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `32`
* **Saved Capital Losses Avoided:** `+2,077.3%`
* **Missed Upside Forgone:** `-955.4%`
* **Net Veto Alpha:** `+1,122.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `112` | `59.3%` |
| `Core 1: Macro Bear Veto` | `55` | `29.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `18` | `9.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `2.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*