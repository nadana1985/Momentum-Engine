# Kronos V12: Institutional Symbol Tear Sheet — `RVN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `27` (`27` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `27` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`51.9%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.879`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-11.0%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.90x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.41%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-33.8%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`47.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.2% / -6.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2022-03-31 14:00` | `2022-04-03 14:00` | 72.0h | `$0.0697` | `$0.0721` | **+3.43%** | **+3.37%** | +8.6% | -5.9% | `time_expiry` |
| 2 | Book 3 | `2023-02-08 15:00` | `2023-02-09 09:00` | 18.0h | `$0.0311` | `$0.0326` | **+4.58%** | **+4.47%** | +7.4% | -5.1% | `target_reclaim` |
| 3 | Book 2 | `2023-03-12 23:00` | `2023-03-19 23:00` | 168.0h | `$0.0242` | `$0.0274` | **+14.82%** | **+13.91%** | +21.0% | -2.8% | `time_cap` |
| 4 | Book 3 | `2023-06-25 15:00` | `2023-06-26 21:00` | 30.0h | `$0.0205` | `$0.0188` | **-8.23%** | **-8.59%** | +2.8% | -8.1% | `stop_loss` |
| 5 | Book 3 | `2023-07-01 02:00` | `2023-07-01 15:00` | 13.0h | `$0.0218` | `$0.0200` | **-8.23%** | **-8.59%** | +8.4% | -8.1% | `stop_loss` |
| 6 | Book 3 | `2023-10-02 18:00` | `2023-10-05 18:00` | 72.0h | `$0.0153` | `$0.0145` | **-5.04%** | **-5.17%** | +1.7% | -5.9% | `time_expiry` |
| 7 | Book 3 | `2023-11-09 16:00` | `2023-11-11 14:00` | 46.0h | `$0.0180` | `$0.0191` | **+6.26%** | **+6.07%** | +6.7% | -12.6% | `target_reclaim` |
| 8 | Book 3 | `2023-11-14 00:00` | `2023-11-17 00:00` | 72.0h | `$0.0181` | `$0.0182` | **+0.68%** | **+0.68%** | +5.9% | -4.7% | `time_expiry` |
| 9 | Book 3 | `2023-11-27 18:00` | `2023-11-30 18:00` | 72.0h | `$0.0182` | `$0.0186` | **+2.54%** | **+2.51%** | +6.7% | -2.3% | `time_expiry` |
| 10 | Book 3 | `2023-12-11 02:00` | `2023-12-14 02:00` | 72.0h | `$0.0210` | `$0.0222` | **+5.74%** | **+5.58%** | +13.6% | -2.7% | `time_expiry` |
| 11 | Book 3 | `2024-02-20 15:00` | `2024-02-22 10:00` | 43.0h | `$0.0220` | `$0.0229` | **+4.17%** | **+4.08%** | +5.9% | -6.3% | `target_reclaim` |
| 12 | Book 3 | `2024-03-05 16:00` | `2024-03-05 19:00` | 3.0h | `$0.0276` | `$0.0253` | **-8.23%** | **-8.59%** | +6.4% | -20.0% | `stop_loss` |
| 13 | Book 3 | `2024-03-31 21:00` | `2024-04-02 02:00` | 29.0h | `$0.0493` | `$0.0453` | **-8.23%** | **-8.59%** | +6.8% | -10.5% | `stop_loss` |
| 14 | Book 3 | `2024-05-23 20:00` | `2024-05-26 20:00` | 72.0h | `$0.0287` | `$0.0297` | **+3.33%** | **+3.27%** | +7.9% | -2.0% | `time_expiry` |
| 15 | Book 3 | `2024-10-25 23:00` | `2024-10-28 23:00` | 72.0h | `$0.0174` | `$0.0171` | **-1.82%** | **-1.84%** | +4.3% | -6.0% | `time_expiry` |
| 16 | Book 3 | `2024-11-12 10:00` | `2024-11-15 10:00` | 72.0h | `$0.0196` | `$0.0197` | **+0.64%** | **+0.64%** | +9.2% | -6.7% | `time_expiry` |
| 17 | Book 3 | `2024-11-17 21:00` | `2024-11-18 06:00` | 9.0h | `$0.0204` | `$0.0218` | **+6.71%** | **+6.50%** | +9.3% | -0.9% | `target_reclaim` |
| 18 | Book 3 | `2024-12-02 08:00` | `2024-12-02 21:00` | 13.0h | `$0.0256` | `$0.0278` | **+8.70%** | **+8.34%** | +11.7% | -1.7% | `target_reclaim` |
| 19 | Book 3 | `2025-04-27 01:00` | `2025-04-30 01:00` | 72.0h | `$0.0123` | `$0.0116` | **-5.12%** | **-5.25%** | +3.4% | -7.4% | `time_expiry` |
| 20 | Book 3 | `2025-06-05 08:00` | `2025-06-05 09:00` | 1.0h | `$0.0172` | `$0.0158` | **-8.23%** | **-8.59%** | +12.4% | -9.1% | `stop_loss` |
| 21 | Book 3 | `2025-06-10 07:00` | `2025-06-11 12:00` | 29.0h | `$0.0189` | `$0.0220` | **+16.16%** | **+14.98%** | +16.2% | -4.0% | `target_reclaim` |
| 22 | Book 3 | `2025-07-01 03:00` | `2025-07-02 15:00` | 36.0h | `$0.0134` | `$0.0132` | **-1.91%** | **-1.93%** | +0.6% | -5.3% | `stall_bailout` |
| 23 | Book 3 | `2025-07-18 20:00` | `2025-07-20 06:00` | 34.0h | `$0.0146` | `$0.0155` | **+5.71%** | **+5.56%** | +6.7% | -1.1% | `target_reclaim` |
| 24 | Book 3 | `2025-07-25 14:00` | `2025-07-28 14:00` | 72.0h | `$0.0163` | `$0.0156` | **-4.64%** | **-4.75%** | +4.3% | -4.6% | `time_expiry` |
| 25 | Book 3 | `2025-10-28 19:00` | `2025-10-30 17:00` | 46.0h | `$0.0098` | `$0.0090` | **-8.23%** | **-8.59%** | +1.7% | -8.4% | `stop_loss` |
| 26 | Book 2 | `2026-09-13 19:00` | `2026-09-15 07:00` | 36.0h | `$0.0023` | `$0.0021` | **-11.35%** | **-11.91%** | +0.6% | -9.7% | `stall_bailout` |
| 27 | Book 3 | `2026-10-06 16:00` | `2026-10-07 02:00` | 10.0h | `$0.0023` | `$0.0021` | **-8.23%** | **-8.59%** | +4.8% | -9.0% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_expiry` | `10` | `60.0%` | **`-1.0%`** |
| `target_reclaim` | `7` | `100.0%` | **`+50.0%`** |
| `stop_loss` | `7` | `0.0%` | **`-60.1%`** |
| `stall_bailout` | `2` | `0.0%` | **`-13.8%`** |
| `time_cap` | `1` | `100.0%` | **`+13.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `RVN`

* **Total Candidate Breakouts Filtered (Vetoed):** `804`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `544` (67.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `169`
* **Saved Capital Losses Avoided:** `+8,436.2%`
* **Missed Upside Forgone:** `-6,026.7%`
* **Net Veto Alpha:** `+2,409.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `406` | `50.5%` |
| `Core 1: Macro Bear Veto` | `269` | `33.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `77` | `9.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `43` | `5.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `9` | `1.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*