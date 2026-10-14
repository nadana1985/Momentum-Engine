# Kronos V12: Institutional Symbol Tear Sheet — `WOO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `27` (`27` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `27` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`55.6%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.297`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+28.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.32x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.04%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-20.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`45.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.8% / -6.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2023-01-10 14:00` | `2023-01-21 07:00` | 257.0h | `$0.1804` | `$0.2165` | **+8.07%** | **+7.81%** | +20.6% | -13.0% | `target_reclaim` |
| 2 | Book 3 | `2023-02-20 01:00` | `2023-02-21 21:00` | 44.0h | `$0.2561` | `$0.2350` | **-8.23%** | **-8.59%** | +6.7% | -10.3% | `stop_loss` |
| 3 | Book 3 | `2023-03-19 23:00` | `2023-03-20 19:00` | 20.0h | `$0.2208` | `$0.2026` | **-8.23%** | **-8.59%** | +2.4% | -10.0% | `stop_loss` |
| 4 | Book 3 | `2023-09-21 20:00` | `2023-09-24 20:00` | 72.0h | `$0.1675` | `$0.1649` | **-1.54%** | **-1.56%** | +1.3% | -2.9% | `time_expiry` |
| 5 | Book 3 | `2023-10-03 14:00` | `2023-10-05 04:00` | 38.0h | `$0.1704` | `$0.1798` | **+5.57%** | **+5.42%** | +5.6% | -0.6% | `target_reclaim` |
| 6 | Book 2 | `2023-10-23 16:00` | `2023-10-30 16:00` | 168.0h | `$0.1899` | `$0.2254` | **+18.81%** | **+17.24%** | +22.8% | -2.0% | `time_cap` |
| 7 | Book 3 | `2023-11-03 01:00` | `2023-11-06 01:00` | 72.0h | `$0.2152` | `$0.2270` | **+5.50%** | **+5.35%** | +8.3% | -1.1% | `time_expiry` |
| 8 | Book 3 | `2023-11-13 21:00` | `2023-11-14 18:00` | 21.0h | `$0.2511` | `$0.2304` | **-8.23%** | **-8.59%** | +2.2% | -10.0% | `stop_loss` |
| 9 | Book 3 | `2023-11-17 10:00` | `2023-11-18 07:00` | 21.0h | `$0.2610` | `$0.2395` | **-8.23%** | **-8.59%** | +1.5% | -9.1% | `stop_loss` |
| 10 | Book 3 | `2023-12-11 02:00` | `2023-12-12 07:00` | 29.0h | `$0.2273` | `$0.2612` | **+14.91%** | **+13.89%** | +15.0% | -2.5% | `target_reclaim` |
| 11 | Book 3 | `2023-12-17 16:00` | `2023-12-18 20:00` | 28.0h | `$0.3654` | `$0.4238` | **+15.98%** | **+14.83%** | +16.0% | -4.9% | `target_reclaim` |
| 12 | Book 3 | `2023-12-28 16:00` | `2023-12-31 16:00` | 72.0h | `$0.4455` | `$0.4153` | **-6.77%** | **-7.01%** | +4.5% | -7.4% | `time_expiry` |
| 13 | Book 3 | `2024-02-18 12:00` | `2024-02-18 16:00` | 4.0h | `$0.4172` | `$0.4346` | **+4.17%** | **+4.08%** | +5.7% | -0.7% | `target_reclaim` |
| 14 | Book 3 | `2024-02-20 14:00` | `2024-02-22 15:00` | 49.0h | `$0.4263` | `$0.4441` | **+4.17%** | **+4.08%** | +6.4% | -7.5% | `target_reclaim` |
| 15 | Book 3 | `2024-02-24 01:00` | `2024-02-24 08:00` | 7.0h | `$0.4423` | `$0.4643` | **+4.98%** | **+4.86%** | +6.6% | -0.8% | `target_reclaim` |
| 16 | Book 3 | `2024-03-05 17:00` | `2024-03-05 19:00` | 2.0h | `$0.5343` | `$0.4903` | **-8.23%** | **-8.59%** | +3.2% | -19.5% | `stop_loss` |
| 17 | Book 3 | `2024-09-28 13:00` | `2024-09-30 14:00` | 49.0h | `$0.1860` | `$0.1965` | **+5.64%** | **+5.49%** | +10.1% | -5.3% | `target_reclaim` |
| 18 | Book 3 | `2024-10-01 17:00` | `2024-10-02 19:00` | 26.0h | `$0.1847` | `$0.1695` | **-8.23%** | **-8.59%** | +3.8% | -8.6% | `stop_loss` |
| 19 | Book 3 | `2024-10-23 15:00` | `2024-10-25 23:00` | 56.0h | `$0.1936` | `$0.1777` | **-8.23%** | **-8.59%** | +5.3% | -14.3% | `stop_loss` |
| 20 | Book 3 | `2024-11-26 09:00` | `2024-11-27 16:00` | 31.0h | `$0.2427` | `$0.2725` | **+12.27%** | **+11.57%** | +12.3% | -4.6% | `target_reclaim` |
| 21 | Book 3 | `2024-12-02 08:00` | `2024-12-02 15:00` | 7.0h | `$0.2880` | `$0.3131` | **+8.70%** | **+8.34%** | +13.2% | -1.3% | `target_reclaim` |
| 22 | Book 3 | `2025-05-03 07:00` | `2025-05-04 17:00` | 34.0h | `$0.0742` | `$0.0681` | **-8.23%** | **-8.59%** | +2.8% | -8.0% | `stop_loss` |
| 23 | Book 3 | `2025-05-29 18:00` | `2025-05-30 16:00` | 22.0h | `$0.0863` | `$0.0792` | **-8.23%** | **-8.59%** | +2.8% | -8.7% | `stop_loss` |
| 24 | Book 3 | `2025-07-01 23:00` | `2025-07-02 15:00` | 16.0h | `$0.0637` | `$0.0685` | **+7.46%** | **+7.20%** | +11.5% | -1.3% | `target_reclaim` |
| 25 | Book 3 | `2025-08-14 12:00` | `2025-08-15 15:00` | 27.0h | `$0.0794` | `$0.0729` | **-8.23%** | **-8.59%** | +4.4% | -8.4% | `stop_loss` |
| 26 | Book 3 | `2026-08-23 03:00` | `2026-08-23 21:00` | 18.0h | `$0.0117` | `$0.0122` | **+4.43%** | **+4.34%** | +4.9% | -3.2% | `target_reclaim` |
| 27 | Book 3 | `2026-09-29 02:00` | `2026-09-30 08:00` | 30.0h | `$0.0128` | `$0.0138` | **+8.31%** | **+7.98%** | +9.8% | -0.0% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `13` | `100.0%` | **`+99.9%`** |
| `stop_loss` | `10` | `0.0%` | **`-85.9%`** |
| `time_expiry` | `3` | `33.3%` | **`-3.2%`** |
| `time_cap` | `1` | `100.0%` | **`+17.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `WOO`

* **Total Candidate Breakouts Filtered (Vetoed):** `381`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `273` (71.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `30`
* **Saved Capital Losses Avoided:** `+3,406.2%`
* **Missed Upside Forgone:** `-950.7%`
* **Net Veto Alpha:** `+2,455.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `128` | `33.6%` |
| `Core 1: Macro Bear Veto` | `97` | `25.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `93` | `24.4%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `61` | `16.0%` |
| `Core 4: Defensible Whale Dump` | `2` | `0.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*