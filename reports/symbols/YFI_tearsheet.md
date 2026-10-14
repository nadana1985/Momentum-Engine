# Kronos V12: Institutional Symbol Tear Sheet — `YFI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `15` (`15` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `15` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`80.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`7.479`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+115.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`3.18x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+7.71%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`95.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+19.5% / -6.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-11 13:00` | `2021-09-05 17:00` | 604.0h | `$36582.7920` | `$43899.3504` | **+18.02%** | **+16.79%** | +20.1% | -3.9% | `target_reclaim` |
| 2 | Book 3 | `2022-03-25 17:00` | `2022-03-27 21:00` | 52.0h | `$20615.4286` | `$21629.0000` | **+4.92%** | **+4.80%** | +5.7% | -1.2% | `target_reclaim` |
| 3 | Book 3 | `2022-04-04 01:00` | `2022-04-06 14:00` | 61.0h | `$23772.4800` | `$21816.0049` | **-8.23%** | **-8.59%** | +3.3% | -8.5% | `stop_loss` |
| 4 | Book 5 (Shelf Absorption Squeeze) | `2022-06-24 04:00` | `2022-06-28 04:00` | Live | `$5063.6800` | `$5494.0928` | **+8.50%** | **+8.16%** | +28.3% | -8.1% | `shelf_target_reclaim` |
| 5 | Book 4 | `2023-02-21 22:00` | `2023-02-24 01:00` | 51.0h | `$8213.3015` | `$9855.9618` | **+24.26%** | **+22.10%** | +21.1% | -3.9% | `target_reclaim` |
| 6 | Book 5 (Shelf Absorption Squeeze) | `2023-02-22 03:00` | `2023-02-26 03:00` | Live | `$7765.7200` | `$8425.8062` | **+8.50%** | **+8.16%** | +29.1% | -18.2% | `shelf_target_reclaim` |
| 7 | Book 2 | `2023-06-20 18:00` | `2023-06-27 18:00` | 168.0h | `$5817.5075` | `$6405.9450` | **+11.59%** | **+11.04%** | +16.5% | -1.6% | `time_cap` |
| 8 | Book 3 | `2023-11-09 16:00` | `2023-11-09 17:00` | 1.0h | `$5751.0000` | `$6272.0000` | **+9.06%** | **+8.67%** | +19.2% | -0.7% | `target_reclaim` |
| 9 | Book 5 (Shelf Absorption Squeeze) | `2023-11-11 13:00` | `2023-11-15 13:00` | Live | `$8196.2800` | `$8892.9638` | **+8.50%** | **+8.16%** | +76.1% | -15.6% | `shelf_target_reclaim` |
| 10 | Book 3 | `2023-11-17 15:00` | `2023-11-18 03:00` | 12.0h | `$14120.4857` | `$12958.3697` | **-8.23%** | **-8.59%** | +5.8% | -11.4% | `stop_loss` |
| 11 | Book 3 | `2024-03-03 07:00` | `2024-03-04 05:00` | 22.0h | `$8459.4000` | `$9617.0000` | **+13.68%** | **+12.83%** | +14.1% | -0.5% | `target_reclaim` |
| 12 | Book 3 | `2024-03-05 19:00` | `2024-03-07 17:00` | 46.0h | `$8413.0000` | `$9893.0000` | **+17.59%** | **+16.20%** | +20.0% | -5.9% | `target_reclaim` |
| 13 | Book 3 | `2024-05-23 13:00` | `2024-05-25 13:00` | 48.0h | `$6967.6800` | `$7258.0000` | **+4.17%** | **+4.08%** | +8.1% | -4.4% | `target_reclaim` |
| 14 | Book 3 | `2024-10-01 15:00` | `2024-10-04 15:00` | 72.0h | `$5015.7143` | `$4982.5125` | **-0.66%** | **-0.66%** | +4.1% | -4.9% | `time_expiry` |
| 15 | Book 4 | `2024-11-10 05:00` | `2024-11-10 08:00` | 3.0h | `$5764.6340` | `$6917.5608` | **+13.16%** | **+12.45%** | +21.2% | -2.4% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `8` | `100.0%` | **`+97.9%`** |
| `shelf_target_reclaim` | `3` | `100.0%` | **`+24.5%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `time_cap` | `1` | `100.0%` | **`+11.0%`** |
| `time_expiry` | `1` | `0.0%` | **`-0.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `YFI`

* **Total Candidate Breakouts Filtered (Vetoed):** `1431`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `689` (48.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `256`
* **Saved Capital Losses Avoided:** `+8,589.0%`
* **Missed Upside Forgone:** `-9,125.8%`
* **Net Veto Alpha:** `+-536.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `487` | `34.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `474` | `33.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `215` | `15.0%` |
| `Core 1: Macro Bear Veto` | `150` | `10.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `102` | `7.1%` |
| `Core 4: Defensible Whale Dump` | `3` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*