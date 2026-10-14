# Kronos V12: Institutional Symbol Tear Sheet — `MASK`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `27` (`27` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `27` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`59.3%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.394`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+31.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.37x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.17%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-25.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`25.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.0% / -9.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2022-03-29 02:00` | `2022-03-31 08:00` | 54.0h | `$5.6525` | `$5.8880` | **+4.17%** | **+4.08%** | +5.1% | -4.0% | `target_reclaim` |
| 2 | Book 3 | `2022-03-31 16:00` | `2022-04-01 00:00` | 8.0h | `$5.9956` | `$6.2460` | **+4.18%** | **+4.09%** | +4.7% | -4.6% | `target_reclaim` |
| 3 | Book 4 | `2022-10-31 09:00` | `2022-11-02 03:00` | 42.0h | `$2.4236` | `$2.9084` | **+5.47%** | **+5.34%** | +30.1% | -11.9% | `target_reclaim` |
| 4 | Book 3 | `2023-01-14 09:00` | `2023-01-15 08:00` | 23.0h | `$3.0432` | `$2.7927` | **-8.23%** | **-8.59%** | +4.2% | -15.2% | `stop_loss` |
| 5 | Book 3 | `2023-01-24 17:00` | `2023-01-25 01:00` | 8.0h | `$3.1011` | `$2.8459` | **-8.23%** | **-8.59%** | +2.5% | -8.2% | `stop_loss` |
| 6 | Book 5 (Shelf Absorption Squeeze) | `2023-01-31 01:00` | `2023-02-04 01:00` | Live | `$3.6101` | `$3.9169` | **+8.50%** | **+8.16%** | +37.5% | -18.6% | `shelf_target_reclaim` |
| 7 | Book 3 | `2023-01-31 10:00` | `2023-01-31 14:00` | 4.0h | `$3.7670` | `$3.9240` | **+4.17%** | **+4.08%** | +10.4% | -2.8% | `target_reclaim` |
| 8 | Book 3 | `2023-02-04 21:00` | `2023-02-05 12:00` | 15.0h | `$4.9094` | `$4.5054` | **-8.23%** | **-8.59%** | +3.3% | -15.9% | `stop_loss` |
| 9 | Book 5 (Shelf Absorption Squeeze) | `2023-03-06 18:00` | `2023-03-10 18:00` | Live | `$3.3129` | `$3.5945` | **+8.50%** | **+8.16%** | +88.8% | -28.1% | `shelf_target_reclaim` |
| 10 | Book 3 | `2023-07-23 00:00` | `2023-07-26 00:00` | 72.0h | `$3.7057` | `$3.6868` | **-0.51%** | **-0.51%** | +4.9% | -6.4% | `time_expiry` |
| 11 | Book 3 | `2023-09-21 20:00` | `2023-09-24 20:00` | 72.0h | `$2.6539` | `$2.5935` | **-2.28%** | **-2.30%** | +5.1% | -2.8% | `time_expiry` |
| 12 | Book 3 | `2024-01-03 12:00` | `2024-01-06 05:00` | 65.0h | `$3.4462` | `$3.1626` | **-8.23%** | **-8.59%** | +7.9% | -14.1% | `stop_loss` |
| 13 | Book 3 | `2024-01-08 00:00` | `2024-01-08 03:00` | 3.0h | `$3.7769` | `$3.4660` | **-8.23%** | **-8.59%** | +4.8% | -8.8% | `stop_loss` |
| 14 | Book 3 | `2024-02-28 17:00` | `2024-02-29 03:00` | 10.0h | `$4.4617` | `$4.9320` | **+10.54%** | **+10.02%** | +12.1% | -12.9% | `target_reclaim` |
| 15 | Book 3 | `2024-05-23 13:00` | `2024-05-24 00:00` | 11.0h | `$3.3533` | `$3.4930` | **+4.17%** | **+4.08%** | +4.4% | -4.4% | `target_reclaim` |
| 16 | Book 3 | `2024-06-07 18:00` | `2024-06-08 22:00` | 28.0h | `$3.3770` | `$3.0991` | **-8.23%** | **-8.59%** | +6.6% | -9.9% | `stop_loss` |
| 17 | Book 3 | `2024-10-02 19:00` | `2024-10-04 21:00` | 50.0h | `$2.3058` | `$2.5044` | **+8.61%** | **+8.26%** | +8.9% | -3.8% | `target_reclaim` |
| 18 | Book 5 (Shelf Absorption Squeeze) | `2024-10-29 16:00` | `2024-11-02 16:00` | Live | `$2.6607` | `$2.8869` | **+8.50%** | **+8.16%** | +31.6% | -17.2% | `shelf_target_reclaim` |
| 19 | Book 3 | `2024-12-14 16:00` | `2024-12-14 17:00` | 1.0h | `$4.1269` | `$3.7873` | **-8.23%** | **-8.59%** | +4.4% | -8.2% | `stop_loss` |
| 20 | Book 3 | `2025-05-19 04:00` | `2025-05-19 21:00` | 17.0h | `$1.4929` | `$1.6785` | **+12.43%** | **+11.72%** | +13.1% | -3.2% | `target_reclaim` |
| 21 | Book 3 | `2025-05-24 17:00` | `2025-05-25 16:00` | 23.0h | `$1.7765` | `$1.6303` | **-8.23%** | **-8.59%** | +15.9% | -8.5% | `stop_loss` |
| 22 | Book 3 | `2025-05-31 08:00` | `2025-06-01 13:00` | 29.0h | `$1.9655` | `$2.2327` | **+13.59%** | **+12.74%** | +15.8% | -5.9% | `target_reclaim` |
| 23 | Book 3 | `2025-06-01 17:00` | `2025-06-01 18:00` | 1.0h | `$2.2019` | `$2.5038` | **+13.71%** | **+12.85%** | +27.2% | -0.8% | `target_reclaim` |
| 24 | Book 3 | `2025-06-06 16:00` | `2025-06-06 17:00` | 1.0h | `$2.5864` | `$2.3735` | **-8.23%** | **-8.59%** | +43.1% | -25.7% | `stop_loss` |
| 25 | Book 3 | `2025-07-12 15:00` | `2025-07-12 23:00` | 8.0h | `$1.2749` | `$1.3280` | **+4.17%** | **+4.08%** | +4.8% | -0.2% | `target_reclaim` |
| 26 | Book 3 | `2025-07-13 02:00` | `2025-07-16 02:00` | 72.0h | `$1.3665` | `$1.3902` | **+1.74%** | **+1.72%** | +3.4% | -5.0% | `time_expiry` |
| 27 | Book 3 | `2025-07-18 20:00` | `2025-07-18 21:00` | 1.0h | `$1.4118` | `$1.4706` | **+4.17%** | **+4.08%** | +5.6% | -0.1% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `12` | `100.0%` | **`+85.4%`** |
| `stop_loss` | `9` | `0.0%` | **`-77.3%`** |
| `shelf_target_reclaim` | `3` | `100.0%` | **`+24.5%`** |
| `time_expiry` | `3` | `33.3%` | **`-1.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `MASK`

* **Total Candidate Breakouts Filtered (Vetoed):** `483`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `333` (68.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `119`
* **Saved Capital Losses Avoided:** `+5,034.2%`
* **Missed Upside Forgone:** `-4,421.9%`
* **Net Veto Alpha:** `+612.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `338` | `70.0%` |
| `Core 1: Macro Bear Veto` | `48` | `9.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `48` | `9.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `42` | `8.7%` |
| `Core 4: Defensible Whale Dump` | `4` | `0.8%` |
| `Core 0: Zero-Tolerance Data Firewall` | `3` | `0.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*