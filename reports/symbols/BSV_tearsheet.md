# Kronos V12: Institutional Symbol Tear Sheet — `BSV`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `10` (`10` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `10` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.784`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-7.9%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.92x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.79%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-15.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`62.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.4% / -10.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-12-04 11:00` | `2023-12-06 00:00` | 37.0h | `$49.9257` | `$53.7400` | **+7.64%** | **+7.36%** | +10.3% | -0.9% | `target_reclaim` |
| 2 | Book 3 | `2024-01-02 16:00` | `2024-01-03 12:00` | 20.0h | `$96.2403` | `$88.3197` | **-8.23%** | **-8.59%** | +5.3% | -23.7% | `stop_loss` |
| 3 | Book 3 | `2024-02-10 08:00` | `2024-02-11 03:00` | 19.0h | `$77.0617` | `$80.6900` | **+4.71%** | **+4.60%** | +6.2% | -1.7% | `target_reclaim` |
| 4 | Book 3 | `2024-05-22 20:00` | `2024-05-25 20:00` | 72.0h | `$65.1168` | `$63.7103` | **-2.16%** | **-2.18%** | +2.9% | -7.1% | `time_expiry` |
| 5 | Book 3 | `2024-07-23 05:00` | `2024-07-25 18:00` | 61.0h | `$44.6091` | `$40.9378` | **-8.23%** | **-8.59%** | +4.2% | -8.4% | `stop_loss` |
| 6 | Book 5 (Shelf Absorption Squeeze) | `2024-07-29 08:00` | `2024-08-02 08:00` | Live | `$47.4996` | `$51.5371` | **+8.50%** | **+8.16%** | +3.5% | -37.1% | `shelf_target_reclaim` |
| 7 | Book 3 | `2025-07-22 04:00` | `2025-07-24 05:00` | 49.0h | `$29.6800` | `$27.2373` | **-8.23%** | **-8.59%** | +3.4% | -8.5% | `stop_loss` |
| 8 | Book 3 | `2026-05-07 03:00` | `2026-05-10 03:00` | 72.0h | `$16.1280` | `$16.2892` | **+1.00%** | **+0.99%** | +3.9% | -1.6% | `time_expiry` |
| 9 | Book 4 | `2026-08-14 01:00` | `2026-08-21 16:00` | 183.0h | `$15.3530` | `$18.4236` | **+7.77%** | **+7.53%** | +21.2% | -7.5% | `target_reclaim` |
| 10 | Book 3 | `2026-09-14 12:00` | `2026-09-16 16:00` | 52.0h | `$16.9344` | `$15.5407` | **-8.23%** | **-8.59%** | +3.0% | -8.4% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `target_reclaim` | `3` | `100.0%` | **`+19.5%`** |
| `time_expiry` | `2` | `50.0%` | **`-1.2%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `BSV`

* **Total Candidate Breakouts Filtered (Vetoed):** `213`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `154` (72.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `29`
* **Saved Capital Losses Avoided:** `+1,450.8%`
* **Missed Upside Forgone:** `-1,189.0%`
* **Net Veto Alpha:** `+261.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `88` | `41.3%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `88` | `41.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `24` | `11.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `13` | `6.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*