# Kronos V12: Institutional Symbol Tear Sheet — `MASK`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `25` (`25` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `25` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.057`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+5.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.06x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.22%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`29.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.2% / -7.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-01-14 09:00` | `2023-01-16 15:00` | 54.0h | `$2.9164` | `$2.6764` | **-8.23%** | **-8.59%** | +8.7% | -11.5% | `stop_loss` |
| 2 | Book 3 | `2023-01-24 21:00` | `2023-01-27 21:00` | 72.0h | `$3.0461` | `$3.1671` | **+3.97%** | **+3.89%** | +6.7% | -6.6% | `time_expiry` |
| 3 | Book 3 | `2023-02-04 21:00` | `2023-02-05 12:00` | 15.0h | `$4.9183` | `$4.5135` | **-8.23%** | **-8.59%** | +3.1% | -16.0% | `stop_loss` |
| 4 | Book 3 | `2023-03-30 03:00` | `2023-04-01 06:00` | 51.0h | `$6.4648` | `$5.9328` | **-8.23%** | **-8.59%** | +4.0% | -8.8% | `stop_loss` |
| 5 | Book 3 | `2023-07-24 01:00` | `2023-07-27 01:00` | 72.0h | `$3.6211` | `$3.6578` | **+1.01%** | **+1.01%** | +7.4% | -4.3% | `time_expiry` |
| 6 | Book 3 | `2023-10-24 15:00` | `2023-10-25 01:00` | 10.0h | `$2.7416` | `$2.9800` | **+8.70%** | **+8.34%** | +8.8% | -0.8% | `target_reclaim` |
| 7 | Book 3 | `2023-10-26 14:00` | `2023-10-29 14:00` | 72.0h | `$2.8833` | `$3.0474` | **+5.69%** | **+5.53%** | +6.4% | -2.2% | `time_expiry` |
| 8 | Book 3 | `2023-12-06 05:00` | `2023-12-09 05:00` | 72.0h | `$3.7067` | `$3.8803` | **+4.68%** | **+4.58%** | +6.0% | -4.1% | `time_expiry` |
| 9 | Book 3 | `2024-01-03 11:00` | `2024-01-03 12:00` | 1.0h | `$3.6524` | `$3.3518` | **-8.23%** | **-8.59%** | +6.8% | -19.0% | `stop_loss` |
| 10 | Book 3 | `2024-01-07 22:00` | `2024-01-08 01:00` | 3.0h | `$3.9542` | `$3.6287` | **-8.23%** | **-8.59%** | +6.9% | -9.8% | `stop_loss` |
| 11 | Book 3 | `2024-02-21 14:00` | `2024-02-22 01:00` | 11.0h | `$4.0618` | `$4.4150` | **+8.70%** | **+8.34%** | +12.1% | -4.5% | `target_reclaim` |
| 12 | Book 3 | `2024-02-28 17:00` | `2024-02-29 03:00` | 10.0h | `$4.5374` | `$4.9320` | **+8.70%** | **+8.34%** | +10.2% | -14.3% | `target_reclaim` |
| 13 | Book 3 | `2024-03-10 14:00` | `2024-03-13 14:00` | 72.0h | `$4.9284` | `$4.9925` | **+1.30%** | **+1.29%** | +6.5% | -4.9% | `time_expiry` |
| 14 | Book 3 | `2024-05-23 20:00` | `2024-05-24 00:00` | 4.0h | `$3.2136` | `$3.4930` | **+8.70%** | **+8.34%** | +8.9% | -0.2% | `target_reclaim` |
| 15 | Book 3 | `2024-06-07 18:00` | `2024-06-08 13:00` | 19.0h | `$3.4270` | `$3.1450` | **-8.23%** | **-8.59%** | +5.1% | -11.2% | `stop_loss` |
| 16 | Book 3 | `2024-09-22 22:00` | `2024-09-25 01:00` | 51.0h | `$2.1846` | `$2.3746` | **+8.70%** | **+8.34%** | +8.9% | -0.2% | `target_reclaim` |
| 17 | Book 3 | `2024-10-02 19:00` | `2024-10-04 21:00` | 50.0h | `$2.3040` | `$2.5044` | **+8.70%** | **+8.34%** | +8.9% | -3.7% | `target_reclaim` |
| 18 | Book 3 | `2024-12-02 08:00` | `2024-12-03 02:00` | 18.0h | `$3.5579` | `$3.8673` | **+8.70%** | **+8.34%** | +9.9% | -2.7% | `target_reclaim` |
| 19 | Book 3 | `2024-12-14 16:00` | `2024-12-14 17:00` | 1.0h | `$4.1269` | `$3.7873` | **-8.23%** | **-8.59%** | +4.4% | -8.2% | `stop_loss` |
| 20 | Book 3 | `2025-05-17 08:00` | `2025-05-18 15:00` | 31.0h | `$1.5442` | `$1.6785` | **+8.70%** | **+8.34%** | +10.1% | -1.5% | `target_reclaim` |
| 21 | Book 3 | `2025-05-24 17:00` | `2025-05-25 00:00` | 7.0h | `$1.7874` | `$1.6403` | **-8.23%** | **-8.59%** | +15.2% | -8.5% | `stop_loss` |
| 22 | Book 3 | `2025-05-30 23:00` | `2025-06-01 08:00` | 33.0h | `$2.0541` | `$1.8850` | **-8.23%** | **-8.59%** | +5.6% | -9.9% | `stop_loss` |
| 23 | Book 3 | `2025-06-01 17:00` | `2025-06-01 18:00` | 1.0h | `$2.3035` | `$2.5038` | **+8.70%** | **+8.34%** | +21.6% | -5.2% | `target_reclaim` |
| 24 | Book 3 | `2025-06-06 06:00` | `2025-06-06 08:00` | 2.0h | `$2.7465` | `$2.9853` | **+8.70%** | **+8.34%** | +9.0% | -3.7% | `target_reclaim` |
| 25 | Book 3 | `2025-06-06 16:00` | `2025-06-06 17:00` | 1.0h | `$2.8568` | `$2.4100` | **-15.64%** | **-17.01%** | +29.6% | -32.8% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `10` | `0.0%` | **`-94.3%`** |
| `target_reclaim` | `10` | `100.0%` | **`+83.4%`** |
| `time_expiry` | `5` | `100.0%` | **`+16.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `MASK`

* **Total Candidate Breakouts Filtered (Vetoed):** `194`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `121` (62.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `32`
* **Saved Capital Losses Avoided:** `+2,040.8%`
* **Missed Upside Forgone:** `-1,679.8%`
* **Net Veto Alpha:** `+360.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `60` | `30.9%` |
| `Core 1: Macro Bear Veto` | `48` | `24.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `42` | `21.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `37` | `19.1%` |
| `Core 4: Defensible Whale Dump` | `4` | `2.1%` |
| `Core 0: Zero-Tolerance Data Firewall` | `3` | `1.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*