# Kronos V12: Institutional Symbol Tear Sheet — `EDU`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `18` (`18` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `18` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.681`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+77.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.17x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+4.30%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-18.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`40.9h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.1% / -8.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2023-05-10 15:00` | `2023-05-14 15:00` | Live | `$1.1499` | `$1.2477` | **+8.50%** | **+8.16%** | +24.2% | -16.0% | `shelf_target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2023-05-25 10:00` | `2023-05-29 10:00` | Live | `$1.1328` | `$1.2291` | **+8.50%** | **+8.16%** | +4.4% | -44.8% | `shelf_target_reclaim` |
| 3 | Book 3 | `2023-10-03 18:00` | `2023-10-05 06:00` | 36.0h | `$0.4414` | `$0.4354` | **-1.36%** | **-1.37%** | +0.7% | -4.8% | `stall_bailout` |
| 4 | Book 3 | `2023-10-24 15:00` | `2023-10-25 14:00` | 23.0h | `$0.4438` | `$0.4676` | **+5.37%** | **+5.23%** | +8.3% | -2.4% | `target_reclaim` |
| 5 | Book 3 | `2023-11-01 05:00` | `2023-11-04 05:00` | 72.0h | `$0.4891` | `$0.5034` | **+2.92%** | **+2.88%** | +6.9% | -4.4% | `time_expiry` |
| 6 | Book 3 | `2023-11-13 21:00` | `2023-11-15 09:00` | 36.0h | `$0.5422` | `$0.5975` | **+10.21%** | **+9.72%** | +10.3% | -7.8% | `target_reclaim` |
| 7 | Book 3 | `2023-11-30 08:00` | `2023-12-03 08:00` | 72.0h | `$0.6401` | `$0.6394` | **-0.10%** | **-0.10%** | +4.1% | -1.4% | `time_expiry` |
| 8 | Book 3 | `2023-12-07 09:00` | `2023-12-07 13:00` | 4.0h | `$0.6508` | `$0.7610` | **+16.93%** | **+15.64%** | +18.2% | -1.3% | `target_reclaim` |
| 9 | Book 3 | `2024-02-20 15:00` | `2024-02-22 18:00` | 51.0h | `$0.7617` | `$0.8607` | **+13.00%** | **+12.23%** | +13.5% | -2.8% | `target_reclaim` |
| 10 | Book 3 | `2024-03-05 19:00` | `2024-03-07 00:00` | 29.0h | `$0.8363` | `$0.9538` | **+14.05%** | **+13.15%** | +15.4% | -15.3% | `target_reclaim` |
| 11 | Book 5 (Shelf Absorption Squeeze) | `2024-05-22 08:00` | `2024-05-26 08:00` | Live | `$0.6976` | `$0.7569` | **+8.50%** | **+8.16%** | +51.0% | -13.2% | `shelf_target_reclaim` |
| 12 | Book 3 | `2024-05-27 12:00` | `2024-05-29 20:00` | 56.0h | `$0.9601` | `$0.8811` | **-8.23%** | **-8.59%** | +4.4% | -8.1% | `stop_loss` |
| 13 | Book 3 | `2024-09-28 08:00` | `2024-09-29 05:00` | 21.0h | `$0.6369` | `$0.7178` | **+12.71%** | **+11.96%** | +14.7% | -0.4% | `target_reclaim` |
| 14 | Book 3 | `2024-11-26 11:00` | `2024-11-26 16:00` | 5.0h | `$0.5440` | `$0.5895` | **+8.36%** | **+8.03%** | +9.0% | -0.1% | `target_reclaim` |
| 15 | Book 3 | `2025-01-19 06:00` | `2025-01-19 23:00` | 17.0h | `$0.5442` | `$0.4994` | **-8.23%** | **-8.59%** | +4.4% | -8.2% | `stop_loss` |
| 16 | Book 3 | `2025-04-28 15:00` | `2025-05-01 15:00` | 72.0h | `$0.1492` | `$0.1467` | **-1.64%** | **-1.65%** | +8.9% | -6.1% | `time_expiry` |
| 17 | Book 3 | `2025-05-13 01:00` | `2025-05-15 01:00` | 48.0h | `$0.1787` | `$0.1640` | **-8.23%** | **-8.59%** | +7.4% | -8.3% | `stop_loss` |
| 18 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0404` | `$0.0416` | **+3.06%** | **+3.01%** | +11.3% | -8.4% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `7` | `100.0%` | **`+76.0%`** |
| `time_expiry` | `4` | `50.0%` | **`+4.1%`** |
| `shelf_target_reclaim` | `3` | `100.0%` | **`+24.5%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `stall_bailout` | `1` | `0.0%` | **`-1.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `EDU`

* **Total Candidate Breakouts Filtered (Vetoed):** `861`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `470` (54.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `103`
* **Saved Capital Losses Avoided:** `+7,258.9%`
* **Missed Upside Forgone:** `-3,433.1%`
* **Net Veto Alpha:** `+3,825.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `706` | `82.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `61` | `7.1%` |
| `Core 1: Macro Bear Veto` | `53` | `6.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `41` | `4.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*