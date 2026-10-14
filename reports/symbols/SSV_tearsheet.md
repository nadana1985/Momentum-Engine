# Kronos V12: Institutional Symbol Tear Sheet — `SSV`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `19` (`19` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `19` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`68.4%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.317`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+62.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.88x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+3.31%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-13.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`28.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.6% / -7.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2023-02-25 15:00` | `2023-03-01 15:00` | Live | `$37.3796` | `$40.5569` | **+8.50%** | **+8.16%** | +6.9% | -30.2% | `shelf_target_reclaim` |
| 2 | Book 3 | `2023-10-31 14:00` | `2023-11-02 00:00` | 34.0h | `$14.5344` | `$15.1400` | **+4.17%** | **+4.08%** | +4.9% | -6.2% | `target_reclaim` |
| 3 | Book 3 | `2023-11-05 13:00` | `2023-11-05 23:00` | 10.0h | `$14.5977` | `$15.4100` | **+5.56%** | **+5.42%** | +6.6% | -1.0% | `target_reclaim` |
| 4 | Book 3 | `2023-12-04 11:00` | `2023-12-06 01:00` | 38.0h | `$25.4731` | `$29.3000` | **+15.02%** | **+14.00%** | +15.4% | -6.1% | `target_reclaim` |
| 5 | Book 3 | `2024-01-03 12:00` | `2024-01-03 16:00` | 4.0h | `$25.7537` | `$28.9100` | **+12.26%** | **+11.56%** | +13.5% | -14.2% | `target_reclaim` |
| 6 | Book 3 | `2024-01-11 16:00` | `2024-01-11 23:00` | 7.0h | `$34.3783` | `$37.0100` | **+7.66%** | **+7.38%** | +9.9% | -0.1% | `target_reclaim` |
| 7 | Book 3 | `2024-01-12 17:00` | `2024-01-14 19:00` | 50.0h | `$36.1376` | `$33.1635` | **-8.23%** | **-8.59%** | +6.4% | -8.1% | `stop_loss` |
| 8 | Book 3 | `2024-03-03 07:00` | `2024-03-05 04:00` | 45.0h | `$31.5600` | `$36.8400` | **+16.73%** | **+15.47%** | +24.0% | -2.2% | `target_reclaim` |
| 9 | Book 3 | `2024-05-22 00:00` | `2024-05-23 11:00` | 35.0h | `$45.6860` | `$47.8450` | **+4.73%** | **+4.62%** | +4.8% | -7.5% | `target_reclaim` |
| 10 | Book 3 | `2024-05-27 14:00` | `2024-05-30 14:00` | 72.0h | `$45.6860` | `$43.5459` | **-4.68%** | **-4.80%** | +3.4% | -7.4% | `time_expiry` |
| 11 | Book 3 | `2024-09-30 16:00` | `2024-10-01 17:00` | 25.0h | `$23.2564` | `$21.3424` | **-8.23%** | **-8.59%** | +7.3% | -8.5% | `stop_loss` |
| 12 | Book 3 | `2024-11-24 12:00` | `2024-11-25 09:00` | 21.0h | `$20.8415` | `$24.1500` | **+15.87%** | **+14.73%** | +18.7% | -1.5% | `target_reclaim` |
| 13 | Book 3 | `2024-12-05 01:00` | `2024-12-05 12:00` | 11.0h | `$32.0439` | `$34.3200` | **+7.10%** | **+6.86%** | +7.5% | -2.7% | `target_reclaim` |
| 14 | Book 3 | `2024-12-08 05:00` | `2024-12-09 08:00` | 27.0h | `$32.4846` | `$29.8111` | **-8.23%** | **-8.59%** | +4.7% | -8.0% | `stop_loss` |
| 15 | Book 3 | `2025-04-27 13:00` | `2025-04-29 06:00` | 41.0h | `$6.1695` | `$6.7060` | **+8.70%** | **+8.34%** | +9.8% | -2.0% | `target_reclaim` |
| 16 | Book 3 | `2025-06-12 19:00` | `2025-06-13 00:00` | 5.0h | `$10.0206` | `$9.1959` | **-8.23%** | **-8.59%** | +1.9% | -10.8% | `stop_loss` |
| 17 | Book 3 | `2025-07-14 15:00` | `2025-07-15 18:00` | 27.0h | `$9.1496` | `$9.7090` | **+6.11%** | **+5.93%** | +6.2% | -5.5% | `target_reclaim` |
| 18 | Book 3 | `2025-07-22 08:00` | `2025-07-23 17:00` | 33.0h | `$10.5150` | `$9.6496` | **-8.23%** | **-8.59%** | +7.0% | -8.8% | `stop_loss` |
| 19 | Book 3 | `2026-09-04 12:00` | `2026-09-05 20:00` | 32.0h | `$2.9299` | `$3.0520` | **+4.17%** | **+4.08%** | +4.5% | -2.0% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `12` | `100.0%` | **`+102.5%`** |
| `stop_loss` | `5` | `0.0%` | **`-42.9%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `time_expiry` | `1` | `0.0%` | **`-4.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `SSV`

* **Total Candidate Breakouts Filtered (Vetoed):** `536`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `307` (57.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `82`
* **Saved Capital Losses Avoided:** `+5,087.9%`
* **Missed Upside Forgone:** `-2,233.3%`
* **Net Veto Alpha:** `+2,854.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `390` | `72.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `82` | `15.3%` |
| `Core 1: Macro Bear Veto` | `43` | `8.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `20` | `3.7%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*