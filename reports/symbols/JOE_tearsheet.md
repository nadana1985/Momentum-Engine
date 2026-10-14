# Kronos V12: Institutional Symbol Tear Sheet — `JOE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `18` (`18` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `18` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.247`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+17.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.19x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.99%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-26.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`36.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.5% / -8.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2023-08-31 06:00` | `2023-09-04 06:00` | Live | `$0.2387` | `$0.2590` | **+8.50%** | **+8.16%** | +14.9% | -12.0% | `shelf_target_reclaim` |
| 2 | Book 3 | `2023-10-02 18:00` | `2023-10-04 19:00` | 49.0h | `$0.2485` | `$0.2620` | **+5.42%** | **+5.27%** | +6.8% | -4.2% | `target_reclaim` |
| 3 | Book 3 | `2023-10-08 08:00` | `2023-10-09 16:00` | 32.0h | `$0.2556` | `$0.2346` | **-8.23%** | **-8.59%** | +2.5% | -8.9% | `stop_loss` |
| 4 | Book 3 | `2023-10-31 15:00` | `2023-11-01 18:00` | 27.0h | `$0.2582` | `$0.2740` | **+6.10%** | **+5.92%** | +6.6% | -2.5% | `target_reclaim` |
| 5 | Book 3 | `2023-11-09 16:00` | `2023-11-10 17:00` | 25.0h | `$0.3051` | `$0.3237` | **+6.11%** | **+5.93%** | +8.1% | -12.7% | `target_reclaim` |
| 6 | Book 3 | `2023-11-18 01:00` | `2023-11-18 07:00` | 6.0h | `$0.3763` | `$0.3453` | **-8.23%** | **-8.59%** | +3.3% | -8.8% | `stop_loss` |
| 7 | Book 3 | `2023-12-04 11:00` | `2023-12-04 12:00` | 1.0h | `$0.4330` | `$0.4510` | **+4.17%** | **+4.08%** | +9.8% | -0.7% | `target_reclaim` |
| 8 | Book 3 | `2023-12-24 22:00` | `2023-12-26 17:00` | 43.0h | `$0.6609` | `$0.6065` | **-8.23%** | **-8.59%** | +14.5% | -8.0% | `stop_loss` |
| 9 | Book 3 | `2024-02-20 09:00` | `2024-02-21 18:00` | 33.0h | `$0.5226` | `$0.4796` | **-8.23%** | **-8.59%** | +4.7% | -8.7% | `stop_loss` |
| 10 | Book 3 | `2024-03-16 18:00` | `2024-03-17 09:00` | 15.0h | `$0.7968` | `$0.9274` | **+16.38%** | **+15.17%** | +19.9% | -3.0% | `target_reclaim` |
| 11 | Book 3 | `2024-03-19 23:00` | `2024-03-20 02:00` | 3.0h | `$0.9301` | `$0.8536` | **-8.23%** | **-8.59%** | +2.9% | -8.8% | `stop_loss` |
| 12 | Book 3 | `2024-09-29 07:00` | `2024-10-01 14:00` | 55.0h | `$0.3833` | `$0.3518` | **-8.23%** | **-8.59%** | +2.8% | -8.0% | `stop_loss` |
| 13 | Book 3 | `2024-10-08 07:00` | `2024-10-11 07:00` | 72.0h | `$0.3261` | `$0.3157` | **-3.18%** | **-3.23%** | +2.4% | -6.7% | `time_expiry` |
| 14 | Book 4 | `2024-11-16 03:00` | `2024-11-23 00:00` | 165.0h | `$0.3817` | `$0.4581` | **+38.43%** | **+33.34%** | +20.4% | -9.0% | `target_reclaim` |
| 15 | Book 3 | `2025-04-27 13:00` | `2025-04-28 01:00` | 12.0h | `$0.1969` | `$0.1807` | **-8.23%** | **-8.59%** | +1.4% | -8.0% | `stop_loss` |
| 16 | Book 3 | `2025-07-18 20:00` | `2025-07-20 08:00` | 36.0h | `$0.1716` | `$0.1843` | **+7.40%** | **+7.14%** | +7.6% | -0.8% | `target_reclaim` |
| 17 | Book 5 (Shelf Absorption Squeeze) | `2026-04-08 01:00` | `2026-04-12 01:00` | Live | `$0.0625` | `$0.0574` | **-8.20%** | **-8.56%** | +-16.9% | -38.2% | `shelf_stop_loss` |
| 18 | Book 3 | `2026-09-20 01:00` | `2026-09-20 13:00` | 12.0h | `$0.0330` | `$0.0345` | **+4.75%** | **+4.64%** | +5.0% | -4.3% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `8` | `100.0%` | **`+81.5%`** |
| `stop_loss` | `7` | `0.0%` | **`-60.1%`** |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `time_expiry` | `1` | `0.0%` | **`-3.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `JOE`

* **Total Candidate Breakouts Filtered (Vetoed):** `490`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `335` (68.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `88`
* **Saved Capital Losses Avoided:** `+4,086.8%`
* **Missed Upside Forgone:** `-2,311.7%`
* **Net Veto Alpha:** `+1,775.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `371` | `75.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `50` | `10.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `36` | `7.3%` |
| `Core 1: Macro Bear Veto` | `33` | `6.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*