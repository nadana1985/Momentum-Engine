# Kronos V12: Institutional Symbol Tear Sheet — `OGN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `24` (`24` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `24` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`58.3%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.757`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+55.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.74x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+2.31%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-27.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`60.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.4% / -9.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-10-30 17:00` | `2021-11-11 04:00` | 275.0h | `$1.0775` | `$1.2930` | **+14.91%** | **+14.05%** | +26.4% | -12.3% | `target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2022-05-31 14:00` | `2022-06-04 14:00` | Live | `$0.2922` | `$0.2682` | **-8.20%** | **-8.56%** | +-0.8% | -44.5% | `shelf_stop_loss` |
| 3 | Book 3 | `2023-02-09 03:00` | `2023-02-09 14:00` | 11.0h | `$0.1344` | `$0.1538` | **+14.47%** | **+13.52%** | +14.6% | -2.1% | `target_reclaim` |
| 4 | Book 3 | `2023-02-13 17:00` | `2023-02-16 17:00` | 72.0h | `$0.1362` | `$0.1498` | **+9.99%** | **+9.52%** | +10.7% | -3.0% | `time_expiry` |
| 5 | Book 5 (Shelf Absorption Squeeze) | `2023-07-23 12:00` | `2023-07-27 12:00` | Live | `$0.0920` | `$0.0998` | **+8.50%** | **+8.16%** | +7.6% | -19.4% | `shelf_target_reclaim` |
| 6 | Book 4 | `2023-07-26 15:00` | `2023-08-05 13:00` | 238.0h | `$0.1128` | `$0.0959` | **-10.24%** | **-11.10%** | +7.8% | -15.0% | `structural_stop` |
| 7 | Book 5 (Shelf Absorption Squeeze) | `2023-09-08 04:00` | `2023-09-12 04:00` | Live | `$0.0960` | `$0.1041` | **+8.50%** | **+8.16%** | +2.3% | -20.0% | `shelf_target_reclaim` |
| 8 | Book 3 | `2023-11-09 16:00` | `2023-11-10 02:00` | 10.0h | `$0.1201` | `$0.1383` | **+15.18%** | **+14.13%** | +19.3% | -5.9% | `target_reclaim` |
| 9 | Book 3 | `2023-11-11 04:00` | `2023-11-14 04:00` | 72.0h | `$0.1283` | `$0.1233` | **-3.87%** | **-3.95%** | +6.4% | -6.4% | `time_expiry` |
| 10 | Book 3 | `2023-12-18 08:00` | `2023-12-20 16:00` | 56.0h | `$0.1329` | `$0.1548` | **+16.49%** | **+15.27%** | +17.0% | -2.9% | `target_reclaim` |
| 11 | Book 3 | `2024-02-20 15:00` | `2024-02-23 15:00` | 72.0h | `$0.1690` | `$0.1701` | **+0.63%** | **+0.62%** | +7.4% | -3.8% | `time_expiry` |
| 12 | Book 3 | `2024-03-05 19:00` | `2024-03-05 20:00` | 1.0h | `$0.1958` | `$0.1789` | **-8.66%** | **-9.06%** | +4.0% | -16.4% | `stop_loss` |
| 13 | Book 3 | `2024-03-11 00:00` | `2024-03-11 08:00` | 8.0h | `$0.2175` | `$0.2364` | **+8.70%** | **+8.34%** | +9.2% | -3.7% | `target_reclaim` |
| 14 | Book 3 | `2024-03-14 04:00` | `2024-03-15 03:00` | 23.0h | `$0.2423` | `$0.2224` | **-8.23%** | **-8.59%** | +2.0% | -10.7% | `stop_loss` |
| 15 | Book 3 | `2024-04-09 14:00` | `2024-04-10 12:00` | 22.0h | `$0.2258` | `$0.2072` | **-8.23%** | **-8.59%** | +3.1% | -8.5% | `stop_loss` |
| 16 | Book 3 | `2024-07-29 14:00` | `2024-07-31 20:00` | 54.0h | `$0.1034` | `$0.0949` | **-8.23%** | **-8.59%** | +2.5% | -8.0% | `stop_loss` |
| 17 | Book 5 (Shelf Absorption Squeeze) | `2024-11-02 08:00` | `2024-11-06 08:00` | Live | `$0.0843` | `$0.0914` | **+8.50%** | **+8.16%** | +16.0% | -15.6% | `shelf_target_reclaim` |
| 18 | Book 3 | `2024-11-02 18:00` | `2024-11-03 14:00` | 20.0h | `$0.0920` | `$0.0844` | **-8.23%** | **-8.59%** | +6.1% | -8.4% | `stop_loss` |
| 19 | Book 3 | `2024-11-19 21:00` | `2024-11-22 21:00` | 72.0h | `$0.1020` | `$0.1075` | **+5.41%** | **+5.27%** | +7.8% | -5.5% | `time_expiry` |
| 20 | Book 3 | `2025-06-16 23:00` | `2025-06-19 23:00` | 72.0h | `$0.0527` | `$0.0498` | **-5.56%** | **-5.72%** | +2.6% | -7.2% | `time_expiry` |
| 21 | Book 3 | `2025-07-19 14:00` | `2025-07-20 01:00` | 11.0h | `$0.0609` | `$0.0635` | **+4.34%** | **+4.25%** | +4.7% | -0.4% | `target_reclaim` |
| 22 | Book 2 | `2026-09-20 00:00` | `2026-09-22 00:00` | 48.0h | `$0.0198` | `$0.0197` | **-0.36%** | **-0.36%** | +2.3% | -6.1% | `fast_decay_cut` |
| 23 | Book 3 | `2026-09-28 07:00` | `2026-09-30 10:00` | 51.0h | `$0.0200` | `$0.0210` | **+5.20%** | **+5.07%** | +5.6% | -4.6% | `target_reclaim` |
| 24 | Book 3 | `2026-10-07 02:00` | `2026-10-07 20:00` | 18.0h | `$0.0207` | `$0.0238` | **+14.96%** | **+13.94%** | +15.7% | -1.4% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `8` | `100.0%` | **`+88.6%`** |
| `stop_loss` | `5` | `0.0%` | **`-43.4%`** |
| `time_expiry` | `5` | `60.0%` | **`+5.7%`** |
| `shelf_target_reclaim` | `3` | `100.0%` | **`+24.5%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.4%`** |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `structural_stop` | `1` | `0.0%` | **`-11.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `OGN`

* **Total Candidate Breakouts Filtered (Vetoed):** `670`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `485` (72.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `86`
* **Saved Capital Losses Avoided:** `+8,580.7%`
* **Missed Upside Forgone:** `-2,643.3%`
* **Net Veto Alpha:** `+5,937.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `243` | `36.3%` |
| `Core 1: Macro Bear Veto` | `180` | `26.9%` |
| `Core 0: Zero-Tolerance Data Firewall` | `178` | `26.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `58` | `8.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `11` | `1.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*