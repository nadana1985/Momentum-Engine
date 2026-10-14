# Kronos V12: Institutional Symbol Tear Sheet — `1000XEC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `15` (`15` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `15` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`73.3%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.952`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+46.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.60x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+3.12%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-12.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`29.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.7% / -7.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2022-06-06 10:00` | `2022-06-10 10:00` | Live | `$0.0525` | `$0.0569` | **+8.50%** | **+8.16%** | +3.2% | -42.1% | `shelf_target_reclaim` |
| 2 | Book 3 | `2023-01-14 09:00` | `2023-01-15 00:00` | 15.0h | `$0.0292` | `$0.0304` | **+4.17%** | **+4.08%** | +6.2% | -6.4% | `target_reclaim` |
| 3 | Book 3 | `2023-01-18 15:00` | `2023-01-21 15:00` | 72.0h | `$0.0295` | `$0.0302` | **+2.46%** | **+2.43%** | +6.1% | -5.6% | `time_expiry` |
| 4 | Book 4 | `2023-06-30 06:00` | `2023-06-30 13:00` | 7.0h | `$0.0320` | `$0.0383` | **+4.83%** | **+4.61%** | +23.6% | -3.7% | `target_reclaim` |
| 5 | Book 5 (Shelf Absorption Squeeze) | `2023-09-18 11:00` | `2023-09-22 11:00` | Live | `$0.0252` | `$0.0273` | **+8.50%** | **+8.16%** | +3.0% | -13.9% | `shelf_target_reclaim` |
| 6 | Book 3 | `2023-09-18 21:00` | `2023-09-21 21:00` | 72.0h | `$0.0252` | `$0.0238` | **-5.59%** | **-5.76%** | +8.1% | -6.1% | `time_expiry` |
| 7 | Book 3 | `2023-11-09 16:00` | `2023-11-09 23:00` | 7.0h | `$0.0276` | `$0.0307` | **+11.48%** | **+10.86%** | +18.6% | -5.5% | `target_reclaim` |
| 8 | Book 3 | `2023-12-11 02:00` | `2023-12-11 03:00` | 1.0h | `$0.0343` | `$0.0373` | **+8.70%** | **+8.34%** | +9.5% | -7.0% | `target_reclaim` |
| 9 | Book 3 | `2024-05-22 04:00` | `2024-05-23 20:00` | 40.0h | `$0.0512` | `$0.0470` | **-8.23%** | **-8.59%** | +1.2% | -9.4% | `stop_loss` |
| 10 | Book 3 | `2024-07-28 08:00` | `2024-07-28 16:00` | 8.0h | `$0.0374` | `$0.0396` | **+5.69%** | **+5.54%** | +7.1% | -0.4% | `target_reclaim` |
| 11 | Book 3 | `2024-07-29 15:00` | `2024-07-31 20:00` | 53.0h | `$0.0400` | `$0.0367` | **-8.23%** | **-8.59%** | +3.1% | -8.1% | `stop_loss` |
| 12 | Book 3 | `2024-11-17 19:00` | `2024-11-20 19:00` | 72.0h | `$0.0433` | `$0.0429` | **-1.07%** | **-1.08%** | +7.6% | -2.2% | `time_expiry` |
| 13 | Book 3 | `2025-04-28 01:00` | `2025-04-28 07:00` | 6.0h | `$0.0218` | `$0.0227` | **+4.17%** | **+4.08%** | +4.7% | -0.5% | `target_reclaim` |
| 14 | Book 3 | `2025-07-14 20:00` | `2025-07-16 01:00` | 29.0h | `$0.0209` | `$0.0218` | **+4.17%** | **+4.08%** | +6.2% | -3.4% | `target_reclaim` |
| 15 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0066` | `$0.0073` | **+11.12%** | **+10.54%** | +21.7% | -0.3% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `8` | `100.0%` | **`+52.1%`** |
| `time_expiry` | `3` | `33.3%` | **`-4.4%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `1000XEC`

* **Total Candidate Breakouts Filtered (Vetoed):** `547`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `451` (82.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `68`
* **Saved Capital Losses Avoided:** `+5,809.3%`
* **Missed Upside Forgone:** `-2,389.4%`
* **Net Veto Alpha:** `+3,419.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `247` | `45.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `142` | `26.0%` |
| `Core 1: Macro Bear Veto` | `85` | `15.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `71` | `13.0%` |
| `Core 0: Zero-Tolerance Data Firewall` | `2` | `0.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*