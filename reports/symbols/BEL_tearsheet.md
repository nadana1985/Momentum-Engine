# Kronos V12: Institutional Symbol Tear Sheet — `BEL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `32` (`32` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `32` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`53.1%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.359`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+41.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.51x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+1.29%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-56.4%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`37.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.2% / -12.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-13 23:00` | `2021-08-21 08:00` | 177.0h | `$2.0788` | `$2.4946` | **+22.53%** | **+20.65%** | +22.9% | -7.4% | `target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2022-06-23 05:00` | `2022-06-27 05:00` | Live | `$0.8810` | `$0.9559` | **+8.50%** | **+8.16%** | +12.8% | -16.4% | `shelf_target_reclaim` |
| 3 | Book 4 | `2022-07-30 09:00` | `2022-07-31 22:00` | 37.0h | `$1.0279` | `$0.8737` | **-3.77%** | **-3.93%** | +1.2% | -17.6% | `structural_stop` |
| 4 | Book 3 | `2023-01-14 09:00` | `2023-01-17 09:00` | 72.0h | `$0.4712` | `$0.5051` | **+7.21%** | **+6.96%** | +12.3% | -1.0% | `time_expiry` |
| 5 | Book 3 | `2023-01-24 21:00` | `2023-01-25 01:00` | 4.0h | `$0.5480` | `$0.5029` | **-8.23%** | **-8.59%** | +2.4% | -8.1% | `stop_loss` |
| 6 | Book 3 | `2023-02-09 03:00` | `2023-02-09 22:00` | 19.0h | `$0.5920` | `$0.5433` | **-8.23%** | **-8.59%** | +9.1% | -9.6% | `stop_loss` |
| 7 | Book 5 (Shelf Absorption Squeeze) | `2023-02-20 16:00` | `2023-02-24 16:00` | Live | `$0.9212` | `$0.8457` | **-8.20%** | **-8.56%** | +-2.8% | -37.9% | `shelf_stop_loss` |
| 8 | Book 5 (Shelf Absorption Squeeze) | `2023-04-09 19:00` | `2023-04-13 19:00` | Live | `$0.6965` | `$0.7557` | **+8.50%** | **+8.16%** | +21.1% | -15.1% | `shelf_target_reclaim` |
| 9 | Book 3 | `2023-04-11 20:00` | `2023-04-14 20:00` | 72.0h | `$0.6742` | `$0.7192` | **+6.68%** | **+6.46%** | +10.3% | -4.6% | `time_expiry` |
| 10 | Book 3 | `2023-04-19 08:00` | `2023-04-20 16:00` | 32.0h | `$0.7876` | `$0.7228` | **-8.23%** | **-8.59%** | +5.2% | -9.9% | `stop_loss` |
| 11 | Book 5 (Shelf Absorption Squeeze) | `2023-05-24 05:00` | `2023-05-28 05:00` | Live | `$0.6663` | `$0.7229` | **+8.50%** | **+8.16%** | +24.6% | -39.2% | `shelf_target_reclaim` |
| 12 | Book 5 (Shelf Absorption Squeeze) | `2023-07-06 15:00` | `2023-07-10 15:00` | Live | `$0.6662` | `$0.7228` | **+8.50%** | **+8.16%** | +9.9% | -15.0% | `shelf_target_reclaim` |
| 13 | Book 3 | `2023-07-07 16:00` | `2023-07-09 00:00` | 32.0h | `$0.7302` | `$0.7606` | **+4.17%** | **+4.08%** | +5.6% | -6.3% | `target_reclaim` |
| 14 | Book 3 | `2023-07-17 10:00` | `2023-07-20 10:00` | 72.0h | `$0.7481` | `$0.7155` | **-4.35%** | **-4.45%** | +2.2% | -6.3% | `time_expiry` |
| 15 | Book 3 | `2023-10-26 14:00` | `2023-10-28 05:00` | 39.0h | `$0.5690` | `$0.6070` | **+6.69%** | **+6.47%** | +7.4% | -0.5% | `target_reclaim` |
| 16 | Book 3 | `2023-12-11 02:00` | `2023-12-12 01:00` | 23.0h | `$0.6577` | `$0.7469` | **+13.57%** | **+12.72%** | +14.3% | -6.9% | `target_reclaim` |
| 17 | Book 3 | `2024-02-20 15:00` | `2024-02-22 11:00` | 44.0h | `$0.6621` | `$0.7389` | **+11.59%** | **+10.97%** | +12.1% | -2.5% | `target_reclaim` |
| 18 | Book 3 | `2024-02-24 02:00` | `2024-02-24 09:00` | 7.0h | `$0.7307` | `$0.7611` | **+4.17%** | **+4.08%** | +4.7% | -0.5% | `target_reclaim` |
| 19 | Book 3 | `2024-02-28 17:00` | `2024-02-29 00:00` | 7.0h | `$0.7321` | `$0.7749` | **+5.85%** | **+5.68%** | +10.7% | -7.1% | `target_reclaim` |
| 20 | Book 3 | `2024-03-05 19:00` | `2024-03-07 09:00` | 38.0h | `$0.7495` | `$0.8793` | **+17.32%** | **+15.97%** | +19.8% | -9.8% | `target_reclaim` |
| 21 | Book 5 (Shelf Absorption Squeeze) | `2024-04-03 10:00` | `2024-04-07 10:00` | Live | `$1.2261` | `$1.3303` | **+8.50%** | **+8.16%** | +89.1% | -43.4% | `shelf_target_reclaim` |
| 22 | Book 3 | `2024-06-07 18:00` | `2024-06-07 19:00` | 1.0h | `$0.9347` | `$0.8578` | **-8.23%** | **-8.59%** | +3.6% | -14.1% | `stop_loss` |
| 23 | Book 3 | `2024-11-12 10:00` | `2024-11-13 04:00` | 18.0h | `$0.5714` | `$0.5243` | **-8.23%** | **-8.59%** | +2.9% | -10.8% | `stop_loss` |
| 24 | Book 3 | `2024-11-21 02:00` | `2024-11-21 10:00` | 8.0h | `$0.5685` | `$0.6529` | **+14.84%** | **+13.83%** | +15.1% | -0.3% | `target_reclaim` |
| 25 | Book 3 | `2024-11-22 13:00` | `2024-11-22 14:00` | 1.0h | `$0.6515` | `$0.5979` | **-8.23%** | **-8.59%** | +5.4% | -9.4% | `stop_loss` |
| 26 | Book 3 | `2025-02-03 01:00` | `2025-02-03 02:00` | 1.0h | `$0.7011` | `$0.6434` | **-8.23%** | **-8.59%** | +9.6% | -11.6% | `stop_loss` |
| 27 | Book 3 | `2025-02-04 08:00` | `2025-02-04 09:00` | 1.0h | `$0.7774` | `$0.7024` | **-9.64%** | **-10.14%** | +8.1% | -13.4% | `stop_loss` |
| 28 | Book 3 | `2025-07-23 17:00` | `2025-07-25 03:00` | 34.0h | `$0.2861` | `$0.2626` | **-8.23%** | **-8.59%** | +3.5% | -8.8% | `stop_loss` |
| 29 | Book 3 | `2025-07-28 14:00` | `2025-07-29 20:00` | 30.0h | `$0.2988` | `$0.2742` | **-8.23%** | **-8.59%** | +1.6% | -9.6% | `stop_loss` |
| 30 | Book 3 | `2025-09-22 05:00` | `2025-09-22 06:00` | 1.0h | `$0.2457` | `$0.2255` | **-8.23%** | **-8.59%** | +2.2% | -9.7% | `stop_loss` |
| 31 | Book 5 (Shelf Absorption Squeeze) | `2026-06-20 07:00` | `2026-06-24 07:00` | Live | `$0.1377` | `$0.1494` | **+8.50%** | **+8.16%** | +38.3% | -39.0% | `shelf_target_reclaim` |
| 32 | Book 4 | `2026-08-21 12:00` | `2026-08-28 12:00` | 168.0h | `$0.1211` | `$0.1186` | **-2.44%** | **-2.46%** | +3.8% | -12.4% | `stagnation_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `11` | `0.0%` | **`-96.0%`** |
| `target_reclaim` | `9` | `100.0%` | **`+94.5%`** |
| `shelf_target_reclaim` | `6` | `100.0%` | **`+48.9%`** |
| `time_expiry` | `3` | `66.7%` | **`+9.0%`** |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-2.5%`** |
| `structural_stop` | `1` | `0.0%` | **`-3.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `BEL`

* **Total Candidate Breakouts Filtered (Vetoed):** `840`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `560` (66.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `198`
* **Saved Capital Losses Avoided:** `+9,003.0%`
* **Missed Upside Forgone:** `-8,065.9%`
* **Net Veto Alpha:** `+937.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `356` | `42.4%` |
| `Core 1: Macro Bear Veto` | `281` | `33.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `133` | `15.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `55` | `6.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `15` | `1.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*