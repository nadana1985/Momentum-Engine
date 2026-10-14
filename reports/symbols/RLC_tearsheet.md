# Kronos V12: Institutional Symbol Tear Sheet — `RLC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `26` (`26` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `26` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`57.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.607`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+45.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.58x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+1.76%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-42.2%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`41.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.8% / -6.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2022-04-01 02:00` | `2022-04-01 18:00` | 16.0h | `$2.2002` | `$2.4809` | **+12.76%** | **+12.01%** | +14.4% | -2.3% | `target_reclaim` |
| 2 | Book 3 | `2023-01-30 10:00` | `2023-02-02 00:00` | 62.0h | `$1.6784` | `$1.8243` | **+8.70%** | **+8.34%** | +9.6% | -6.9% | `target_reclaim` |
| 3 | Book 3 | `2023-02-05 12:00` | `2023-02-05 14:00` | 2.0h | `$1.7455` | `$1.9072` | **+9.27%** | **+8.86%** | +16.3% | -3.6% | `target_reclaim` |
| 4 | Book 5 (Shelf Absorption Squeeze) | `2023-03-21 02:00` | `2023-03-25 02:00` | Live | `$1.6633` | `$1.8046` | **+8.50%** | **+8.16%** | +26.1% | -12.7% | `shelf_target_reclaim` |
| 5 | Book 3 | `2023-03-25 05:00` | `2023-03-25 12:00` | 7.0h | `$1.9945` | `$1.8303` | **-8.23%** | **-8.59%** | +10.2% | -8.2% | `stop_loss` |
| 6 | Book 3 | `2023-04-19 08:00` | `2023-04-19 17:00` | 9.0h | `$1.8180` | `$1.6684` | **-8.23%** | **-8.59%** | +0.9% | -10.8% | `stop_loss` |
| 7 | Book 5 (Shelf Absorption Squeeze) | `2023-04-29 21:00` | `2023-05-03 21:00` | Live | `$1.6772` | `$1.5396` | **-8.20%** | **-8.56%** | +-2.2% | -23.2% | `shelf_stop_loss` |
| 8 | Book 3 | `2023-05-03 07:00` | `2023-05-04 16:00` | 33.0h | `$1.8810` | `$1.7262` | **-8.23%** | **-8.59%** | +1.5% | -8.3% | `stop_loss` |
| 9 | Book 5 (Shelf Absorption Squeeze) | `2023-05-21 09:00` | `2023-05-25 09:00` | Live | `$1.5543` | `$1.6134` | **+3.80%** | **+3.73%** | +-0.3% | -12.3% | `shelf_trail` |
| 10 | Book 3 | `2023-10-02 18:00` | `2023-10-05 18:00` | 72.0h | `$1.0286` | `$0.9984` | **-2.94%** | **-2.98%** | +3.8% | -5.9% | `time_expiry` |
| 11 | Book 3 | `2023-10-16 23:00` | `2023-10-18 16:00` | 41.0h | `$1.0456` | `$0.9596` | **-8.23%** | **-8.59%** | +3.7% | -8.2% | `stop_loss` |
| 12 | Book 3 | `2023-10-31 15:00` | `2023-11-01 20:00` | 29.0h | `$1.1086` | `$1.1671` | **+5.28%** | **+5.15%** | +6.2% | -2.0% | `target_reclaim` |
| 13 | Book 3 | `2023-11-09 16:00` | `2023-11-10 05:00` | 13.0h | `$1.1226` | `$1.3105` | **+16.74%** | **+15.48%** | +16.9% | -2.0% | `target_reclaim` |
| 14 | Book 3 | `2023-11-21 17:00` | `2023-11-24 14:00` | 69.0h | `$1.4147` | `$1.5377` | **+8.70%** | **+8.34%** | +11.7% | -7.0% | `target_reclaim` |
| 15 | Book 3 | `2024-01-31 11:00` | `2024-02-03 11:00` | 72.0h | `$2.3061` | `$2.3929` | **+3.77%** | **+3.70%** | +7.0% | -3.1% | `time_expiry` |
| 16 | Book 3 | `2024-02-23 16:00` | `2024-02-26 16:00` | 72.0h | `$3.7128` | `$3.8805` | **+4.52%** | **+4.42%** | +5.8% | -3.9% | `time_expiry` |
| 17 | Book 3 | `2024-06-03 14:00` | `2024-06-06 14:00` | 72.0h | `$3.4057` | `$3.3462` | **-1.75%** | **-1.76%** | +1.2% | -3.9% | `time_expiry` |
| 18 | Book 3 | `2024-09-28 09:00` | `2024-09-29 19:00` | 34.0h | `$1.6699` | `$1.7395` | **+4.17%** | **+4.08%** | +5.7% | -1.6% | `target_reclaim` |
| 19 | Book 3 | `2024-11-12 10:00` | `2024-11-14 15:00` | 53.0h | `$1.7172` | `$1.5759` | **-8.23%** | **-8.59%** | +6.6% | -8.2% | `stop_loss` |
| 20 | Book 3 | `2024-11-26 10:00` | `2024-11-27 11:00` | 25.0h | `$2.0296` | `$2.2061` | **+8.70%** | **+8.34%** | +8.9% | -1.6% | `target_reclaim` |
| 21 | Book 3 | `2024-12-02 08:00` | `2024-12-03 04:00` | 20.0h | `$2.2265` | `$2.4201` | **+8.70%** | **+8.34%** | +9.2% | -1.1% | `target_reclaim` |
| 22 | Book 3 | `2025-07-23 20:00` | `2025-07-24 06:00` | 10.0h | `$1.0990` | `$1.0085` | **-8.23%** | **-8.59%** | +2.6% | -8.3% | `stop_loss` |
| 23 | Book 4 | `2025-08-27 22:00` | `2025-08-28 00:00` | 2.0h | `$1.3862` | `$1.6634` | **+4.83%** | **+4.61%** | +24.9% | -2.9% | `target_reclaim` |
| 24 | Book 3 | `2025-10-07 00:00` | `2025-10-10 00:00` | 72.0h | `$1.1065` | `$1.0872` | **-1.74%** | **-1.76%** | +4.6% | -6.9% | `time_expiry` |
| 25 | Book 2 | `2026-09-19 23:00` | `2026-09-26 23:00` | 168.0h | `$0.3136` | `$0.3662` | **+18.69%** | **+17.28%** | +21.9% | -5.6% | `time_cap` |
| 26 | Book 3 | `2026-10-09 15:00` | `2026-10-09 16:00` | 1.0h | `$0.9422` | `$0.8647` | **-8.23%** | **-8.59%** | +10.9% | -12.6% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `10` | `100.0%` | **`+83.5%`** |
| `stop_loss` | `7` | `0.0%` | **`-60.1%`** |
| `time_expiry` | `5` | `40.0%` | **`+1.6%`** |
| `shelf_trail` | `1` | `100.0%` | **`+3.7%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_cap` | `1` | `100.0%` | **`+17.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `RLC`

* **Total Candidate Breakouts Filtered (Vetoed):** `858`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `483` (56.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `52`
* **Saved Capital Losses Avoided:** `+6,492.5%`
* **Missed Upside Forgone:** `-2,436.0%`
* **Net Veto Alpha:** `+4,056.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `429` | `50.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `206` | `24.0%` |
| `Core 0: Zero-Tolerance Data Firewall` | `154` | `17.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `45` | `5.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `24` | `2.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*