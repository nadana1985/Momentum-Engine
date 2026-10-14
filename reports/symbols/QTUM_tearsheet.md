# Kronos V12: Institutional Symbol Tear Sheet — `QTUM`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `23` (`23` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `23` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`65.2%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.488`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+84.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.34x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+3.69%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-27.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`95.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.3% / -7.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-06 13:00` | `2021-08-07 04:00` | 15.0h | `$8.4977` | `$10.1973` | **+26.63%** | **+24.05%** | +22.7% | -1.6% | `target_reclaim` |
| 2 | Book 3 | `2023-02-05 12:00` | `2023-02-05 13:00` | 1.0h | `$2.7398` | `$2.8540` | **+4.17%** | **+4.08%** | +10.7% | -4.2% | `target_reclaim` |
| 3 | Book 3 | `2023-02-06 05:00` | `2023-02-07 17:00` | 36.0h | `$2.7505` | `$2.9090` | **+5.76%** | **+5.60%** | +6.0% | -0.3% | `target_reclaim` |
| 4 | Book 3 | `2023-02-09 19:00` | `2023-02-09 22:00` | 3.0h | `$2.8124` | `$2.5809` | **-8.23%** | **-8.59%** | +4.8% | -8.6% | `stop_loss` |
| 5 | Book 3 | `2023-03-22 19:00` | `2023-03-25 19:00` | 72.0h | `$3.0559` | `$3.0404` | **-0.51%** | **-0.51%** | +12.2% | -4.1% | `time_expiry` |
| 6 | Book 4 | `2023-07-01 00:00` | `2023-07-26 09:00` | 609.0h | `$2.9634` | `$2.5189` | **-8.90%** | **-9.65%** | +17.3% | -15.3% | `structural_stop` |
| 7 | Book 5 (Shelf Absorption Squeeze) | `2023-08-01 14:00` | `2023-08-05 14:00` | Live | `$2.5098` | `$2.7231` | **+8.50%** | **+8.16%** | +1.0% | -18.0% | `shelf_target_reclaim` |
| 8 | Book 3 | `2023-10-04 00:00` | `2023-10-07 00:00` | 72.0h | `$2.1926` | `$2.2573` | **+2.95%** | **+2.91%** | +4.1% | -2.3% | `time_expiry` |
| 9 | Book 4 | `2023-10-26 20:00` | `2023-10-28 06:00` | 34.0h | `$2.4657` | `$2.9588` | **+24.72%** | **+22.48%** | +20.9% | -2.1% | `target_reclaim` |
| 10 | Book 3 | `2023-11-03 01:00` | `2023-11-05 12:00` | 59.0h | `$3.0360` | `$3.4470` | **+13.54%** | **+12.70%** | +13.8% | -5.1% | `target_reclaim` |
| 11 | Book 3 | `2023-12-11 02:00` | `2023-12-14 02:00` | 72.0h | `$3.2042` | `$3.1651` | **-1.22%** | **-1.23%** | +6.1% | -11.1% | `time_expiry` |
| 12 | Book 3 | `2024-01-03 12:00` | `2024-01-06 06:00` | 66.0h | `$3.2242` | `$2.9588` | **-8.23%** | **-8.59%** | +8.7% | -16.3% | `stop_loss` |
| 13 | Book 3 | `2024-02-28 18:00` | `2024-02-29 00:00` | 6.0h | `$3.3371` | `$3.6540` | **+9.49%** | **+9.07%** | +9.8% | -0.6% | `target_reclaim` |
| 14 | Book 3 | `2024-04-08 18:00` | `2024-04-08 21:00` | 3.0h | `$4.8586` | `$5.0610` | **+4.17%** | **+4.08%** | +5.0% | -0.0% | `target_reclaim` |
| 15 | Book 3 | `2024-10-01 17:00` | `2024-10-04 17:00` | 72.0h | `$2.3773` | `$2.3591` | **-0.77%** | **-0.77%** | +6.1% | -5.2% | `time_expiry` |
| 16 | Book 4 | `2024-11-14 00:00` | `2024-11-18 17:00` | 113.0h | `$2.7241` | `$3.2689` | **+15.40%** | **+14.46%** | +21.2% | -4.2% | `target_reclaim` |
| 17 | Book 5 (Shelf Absorption Squeeze) | `2025-01-31 14:00` | `2025-02-04 14:00` | Live | `$3.4012` | `$3.6903` | **+8.50%** | **+8.16%** | +0.8% | -27.0% | `shelf_target_reclaim` |
| 18 | Book 3 | `2025-02-02 17:00` | `2025-02-02 22:00` | 5.0h | `$3.2165` | `$2.9518` | **-8.23%** | **-8.59%** | +1.4% | -10.2% | `stop_loss` |
| 19 | Book 3 | `2025-04-28 01:00` | `2025-05-01 01:00` | 72.0h | `$2.1445` | `$2.1516` | **+0.33%** | **+0.33%** | +4.9% | -3.4% | `time_expiry` |
| 20 | Book 4 | `2025-07-16 20:00` | `2025-08-01 20:00` | 384.0h | `$2.3836` | `$2.0260` | **-17.63%** | **-19.12%** | +13.8% | -15.3% | `structural_stop` |
| 21 | Book 2 | `2026-05-04 02:00` | `2026-05-11 02:00` | 168.0h | `$0.8902` | `$1.0224` | **+17.44%** | **+16.26%** | +31.1% | -2.3% | `time_cap` |
| 22 | Book 3 | `2026-09-15 14:00` | `2026-09-18 14:00` | 72.0h | `$0.8711` | `$0.9331` | **+7.11%** | **+6.87%** | +8.1% | -4.2% | `time_expiry` |
| 23 | Book 3 | `2026-09-28 07:00` | `2026-10-01 07:00` | 72.0h | `$0.9636` | `$0.9898` | **+2.72%** | **+2.68%** | +6.9% | -1.5% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `8` | `100.0%` | **`+96.5%`** |
| `time_expiry` | `7` | `57.1%` | **`+10.3%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `structural_stop` | `2` | `0.0%` | **`-28.8%`** |
| `time_cap` | `1` | `100.0%` | **`+16.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `QTUM`

* **Total Candidate Breakouts Filtered (Vetoed):** `1315`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `686` (52.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `234`
* **Saved Capital Losses Avoided:** `+7,922.8%`
* **Missed Upside Forgone:** `-7,682.2%`
* **Net Veto Alpha:** `+240.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `567` | `43.1%` |
| `Core 0: Zero-Tolerance Data Firewall` | `504` | `38.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `93` | `7.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `82` | `6.2%` |
| `Core 1: Macro Bear Veto` | `69` | `5.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*