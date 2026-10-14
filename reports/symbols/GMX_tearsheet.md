# Kronos V12: Institutional Symbol Tear Sheet — `GMX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `23` (`23` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `23` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`52.2%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.746`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-22.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.80x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.98%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-38.9%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`76.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.3% / -7.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-04-19 08:00` | `2023-04-21 19:00` | 59.0h | `$78.5311` | `$72.0680` | **-8.23%** | **-8.59%** | +11.0% | -8.6% | `stop_loss` |
| 2 | Book 3 | `2023-07-05 23:00` | `2023-07-06 08:00` | 9.0h | `$55.2457` | `$57.8900` | **+4.79%** | **+4.68%** | +5.0% | -0.3% | `target_reclaim` |
| 3 | Book 3 | `2023-11-02 13:00` | `2023-11-04 06:00` | 41.0h | `$45.8251` | `$48.0100` | **+4.77%** | **+4.66%** | +4.9% | -3.8% | `target_reclaim` |
| 4 | Book 4 | `2023-11-05 09:00` | `2023-12-05 08:00` | 719.0h | `$48.7029` | `$49.8950` | **+3.26%** | **+3.22%** | +14.7% | -6.2% | `time_expiry` |
| 5 | Book 3 | `2023-12-11 02:00` | `2023-12-11 18:00` | 16.0h | `$52.1743` | `$47.8803` | **-8.23%** | **-8.59%** | +2.2% | -14.5% | `stop_loss` |
| 6 | Book 3 | `2024-02-16 14:00` | `2024-02-18 17:00` | 51.0h | `$44.2368` | `$46.0800` | **+4.17%** | **+4.08%** | +5.2% | -2.5% | `target_reclaim` |
| 7 | Book 3 | `2024-02-21 14:00` | `2024-02-22 07:00` | 17.0h | `$44.2540` | `$46.6000` | **+5.30%** | **+5.17%** | +6.6% | -0.1% | `target_reclaim` |
| 8 | Book 3 | `2024-02-27 16:00` | `2024-02-28 17:00` | 25.0h | `$51.3120` | `$47.0890` | **-8.23%** | **-8.59%** | +4.5% | -10.2% | `stop_loss` |
| 9 | Book 3 | `2024-03-14 13:00` | `2024-03-15 02:00` | 13.0h | `$58.0534` | `$53.2756` | **-8.23%** | **-8.59%** | +1.1% | -8.3% | `stop_loss` |
| 10 | Book 3 | `2024-05-22 18:00` | `2024-05-23 20:00` | 26.0h | `$31.0167` | `$28.4641` | **-8.23%** | **-8.59%** | +2.7% | -9.4% | `stop_loss` |
| 11 | Book 3 | `2024-08-25 07:00` | `2024-08-27 21:00` | 62.0h | `$28.8112` | `$26.4400` | **-8.23%** | **-8.59%** | +4.7% | -8.3% | `stop_loss` |
| 12 | Book 3 | `2024-09-25 19:00` | `2024-09-26 10:00` | 15.0h | `$25.1328` | `$26.1800` | **+4.17%** | **+4.08%** | +4.4% | -1.4% | `target_reclaim` |
| 13 | Book 3 | `2024-09-29 08:00` | `2024-10-01 15:00` | 55.0h | `$25.4429` | `$23.3489` | **-8.23%** | **-8.59%** | +3.1% | -10.8% | `stop_loss` |
| 14 | Book 4 | `2024-11-13 14:00` | `2024-11-25 16:00` | 290.0h | `$28.4336` | `$34.1203` | **+12.18%** | **+11.47%** | +24.5% | -7.8% | `target_reclaim` |
| 15 | Book 3 | `2024-12-09 20:00` | `2024-12-09 21:00` | 1.0h | `$38.5264` | `$35.3557` | **-8.23%** | **-8.59%** | +3.2% | -20.2% | `stop_loss` |
| 16 | Book 5 (Shelf Absorption Squeeze) | `2025-02-08 17:00` | `2025-02-12 17:00` | Live | `$18.6696` | `$20.2565` | **+8.50%** | **+8.16%** | +28.5% | -9.1% | `shelf_target_reclaim` |
| 17 | Book 3 | `2025-02-11 13:00` | `2025-02-11 19:00` | 6.0h | `$24.8899` | `$22.8415` | **-8.23%** | **-8.59%** | +3.0% | -8.2% | `stop_loss` |
| 18 | Book 3 | `2025-04-17 11:00` | `2025-04-18 13:00` | 26.0h | `$14.5090` | `$15.9420` | **+9.88%** | **+9.42%** | +13.2% | -2.6% | `target_reclaim` |
| 19 | Book 3 | `2025-05-17 00:00` | `2025-05-20 00:00` | 72.0h | `$14.6206` | `$14.8907` | **+1.85%** | **+1.83%** | +6.7% | -3.4% | `time_expiry` |
| 20 | Book 3 | `2025-09-19 09:00` | `2025-09-20 14:00` | 29.0h | `$15.1987` | `$15.8320` | **+4.17%** | **+4.08%** | +5.6% | -1.5% | `target_reclaim` |
| 21 | Book 3 | `2025-09-21 17:00` | `2025-09-22 06:00` | 13.0h | `$15.5118` | `$14.2352` | **-8.23%** | **-8.59%** | +2.3% | -15.4% | `stop_loss` |
| 22 | Book 3 | `2026-08-31 09:00` | `2026-09-03 09:00` | 72.0h | `$7.4599` | `$7.2059` | **-3.40%** | **-3.46%** | +3.8% | -6.2% | `time_expiry` |
| 23 | Book 3 | `2026-09-10 00:00` | `2026-09-13 00:00` | 72.0h | `$7.4503` | `$7.8992` | **+6.02%** | **+5.85%** | +6.5% | -2.1% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `10` | `0.0%` | **`-85.9%`** |
| `target_reclaim` | `8` | `100.0%` | **`+47.6%`** |
| `time_expiry` | `4` | `75.0%` | **`+7.4%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `GMX`

* **Total Candidate Breakouts Filtered (Vetoed):** `567`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `384` (67.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `18`
* **Saved Capital Losses Avoided:** `+4,694.9%`
* **Missed Upside Forgone:** `-818.4%`
* **Net Veto Alpha:** `+3,876.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `427` | `75.3%` |
| `Core 1: Macro Bear Veto` | `68` | `12.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `59` | `10.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `13` | `2.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*