# Kronos V12: Institutional Symbol Tear Sheet — `GMX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `20` (`20` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `20` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`45.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.645`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-30.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.74x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.50%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-38.1%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`41.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.6% / -7.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-04-19 08:00` | `2023-04-21 06:00` | 46.0h | `$83.1864` | `$76.3402` | **-8.23%** | **-8.59%** | +4.8% | -8.6% | `stop_loss` |
| 2 | Book 3 | `2023-11-02 16:00` | `2023-11-04 06:00` | 38.0h | `$44.1692` | `$48.0100` | **+8.70%** | **+8.34%** | +8.8% | -0.2% | `target_reclaim` |
| 3 | Book 3 | `2023-12-11 02:00` | `2023-12-13 06:00` | 52.0h | `$50.1860` | `$46.0557` | **-8.23%** | **-8.59%** | +6.3% | -11.1% | `stop_loss` |
| 4 | Book 3 | `2024-02-20 17:00` | `2024-02-23 17:00` | 72.0h | `$45.7148` | `$46.8725` | **+2.53%** | **+2.50%** | +6.1% | -3.3% | `time_expiry` |
| 5 | Book 3 | `2024-02-28 17:00` | `2024-02-29 15:00` | 22.0h | `$49.1740` | `$53.4500` | **+8.70%** | **+8.34%** | +9.1% | -6.3% | `target_reclaim` |
| 6 | Book 3 | `2024-03-14 15:00` | `2024-03-15 03:00` | 12.0h | `$55.9636` | `$51.3578` | **-8.23%** | **-8.59%** | +2.6% | -8.9% | `stop_loss` |
| 7 | Book 3 | `2024-05-22 11:00` | `2024-05-23 20:00` | 33.0h | `$31.7308` | `$29.1194` | **-8.23%** | **-8.59%** | +2.0% | -11.4% | `stop_loss` |
| 8 | Book 3 | `2024-08-24 20:00` | `2024-08-25 07:00` | 11.0h | `$31.0482` | `$28.4929` | **-8.23%** | **-8.59%** | +2.3% | -8.5% | `stop_loss` |
| 9 | Book 3 | `2024-11-13 21:00` | `2024-11-16 21:00` | 72.0h | `$27.1004` | `$28.3460` | **+4.60%** | **+4.49%** | +6.5% | -3.3% | `time_expiry` |
| 10 | Book 3 | `2024-11-26 10:00` | `2024-11-27 15:00` | 29.0h | `$30.4612` | `$33.1100` | **+8.70%** | **+8.34%** | +9.4% | -2.7% | `target_reclaim` |
| 11 | Book 3 | `2024-12-09 09:00` | `2024-12-09 21:00` | 12.0h | `$39.9768` | `$36.6867` | **-8.23%** | **-8.59%** | +6.3% | -23.1% | `stop_loss` |
| 12 | Book 3 | `2025-02-11 18:00` | `2025-02-12 20:00` | 26.0h | `$23.8528` | `$21.8898` | **-8.23%** | **-8.59%** | +2.8% | -8.4% | `stop_loss` |
| 13 | Book 3 | `2025-04-17 11:00` | `2025-04-18 13:00` | 26.0h | `$14.6666` | `$15.9420` | **+8.70%** | **+8.34%** | +12.0% | -3.7% | `target_reclaim` |
| 14 | Book 3 | `2025-05-15 06:00` | `2025-05-17 01:00` | 43.0h | `$15.6970` | `$14.4052` | **-8.23%** | **-8.59%** | +1.7% | -8.7% | `stop_loss` |
| 15 | Book 3 | `2025-07-01 14:00` | `2025-07-02 16:00` | 26.0h | `$13.1284` | `$14.2700` | **+8.70%** | **+8.34%** | +9.8% | -1.2% | `target_reclaim` |
| 16 | Book 3 | `2025-09-21 17:00` | `2025-09-22 06:00` | 13.0h | `$15.6740` | `$14.3841` | **-8.23%** | **-8.59%** | +1.3% | -16.3% | `stop_loss` |
| 17 | Book 3 | `2025-09-25 03:00` | `2025-09-28 03:00` | 72.0h | `$16.6676` | `$16.4677` | **-1.20%** | **-1.21%** | +8.5% | -4.7% | `time_expiry` |
| 18 | Book 3 | `2026-08-30 23:00` | `2026-09-02 23:00` | 72.0h | `$7.5550` | `$7.0942` | **-6.10%** | **-6.29%** | +3.1% | -7.3% | `time_expiry` |
| 19 | Book 3 | `2026-09-09 22:00` | `2026-09-12 22:00` | 72.0h | `$7.7998` | `$7.8044` | **+0.06%** | **+0.06%** | +2.3% | -6.4% | `time_expiry` |
| 20 | Book 3 | `2026-09-23 16:00` | `2026-09-26 16:00` | 72.0h | `$7.9065` | `$8.3940` | **+6.17%** | **+5.98%** | +6.8% | -1.0% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `9` | `0.0%` | **`-77.3%`** |
| `time_expiry` | `6` | `66.7%` | **`+5.5%`** |
| `target_reclaim` | `5` | `100.0%` | **`+41.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `GMX`

* **Total Candidate Breakouts Filtered (Vetoed):** `205`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `140` (68.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `8`
* **Saved Capital Losses Avoided:** `+1,682.8%`
* **Missed Upside Forgone:** `-598.2%`
* **Net Veto Alpha:** `+1,084.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `84` | `41.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `61` | `29.8%` |
| `Core 1: Macro Bear Veto` | `47` | `22.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `13` | `6.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*