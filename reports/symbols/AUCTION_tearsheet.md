# Kronos V12: Institutional Symbol Tear Sheet — `AUCTION`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `15` (`15` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `15` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`80.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.723`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+70.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.02x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+4.68%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-16.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`29.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.2% / -8.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-02-13 13:00` | `2024-02-14 15:00` | 26.0h | `$26.1500` | `$29.5100` | **+12.85%** | **+12.09%** | +13.2% | -0.2% | `target_reclaim` |
| 2 | Book 3 | `2024-05-29 14:00` | `2024-05-30 06:00` | 16.0h | `$23.5760` | `$25.6510` | **+8.80%** | **+8.44%** | +12.3% | -2.4% | `target_reclaim` |
| 3 | Book 3 | `2024-07-30 17:00` | `2024-07-31 04:00` | 11.0h | `$16.7208` | `$18.3220` | **+9.58%** | **+9.14%** | +9.8% | -3.3% | `target_reclaim` |
| 4 | Book 5 (Shelf Absorption Squeeze) | `2024-07-31 07:00` | `2024-08-04 07:00` | Live | `$16.9188` | `$18.3569` | **+8.50%** | **+8.16%** | +2.8% | -37.6% | `shelf_target_reclaim` |
| 5 | Book 5 (Shelf Absorption Squeeze) | `2024-08-17 17:00` | `2024-08-21 17:00` | Live | `$15.1312` | `$16.4174` | **+8.50%** | **+8.16%** | +45.5% | -24.3% | `shelf_target_reclaim` |
| 6 | Book 3 | `2024-09-20 11:00` | `2024-09-22 00:00` | 37.0h | `$14.9636` | `$15.6790` | **+4.78%** | **+4.67%** | +6.7% | -1.5% | `target_reclaim` |
| 7 | Book 3 | `2024-11-12 10:00` | `2024-11-12 22:00` | 12.0h | `$13.6396` | `$14.7970` | **+8.49%** | **+8.14%** | +8.7% | -1.5% | `target_reclaim` |
| 8 | Book 4 | `2024-11-26 05:00` | `2024-12-01 06:00` | 121.0h | `$16.0731` | `$19.2877` | **+25.12%** | **+22.81%** | +22.8% | -10.3% | `target_reclaim` |
| 9 | Book 3 | `2024-12-08 05:00` | `2024-12-09 11:00` | 30.0h | `$19.9624` | `$18.3195` | **-8.23%** | **-8.59%** | +4.4% | -8.1% | `stop_loss` |
| 10 | Book 3 | `2024-12-16 10:00` | `2024-12-16 22:00` | 12.0h | `$20.2038` | `$21.3780` | **+5.81%** | **+5.65%** | +7.4% | -1.9% | `target_reclaim` |
| 11 | Book 3 | `2024-12-25 06:00` | `2024-12-25 15:00` | 9.0h | `$20.7477` | `$19.0401` | **-8.23%** | **-8.59%** | +15.1% | -8.2% | `stop_loss` |
| 12 | Book 3 | `2025-05-10 04:00` | `2025-05-10 11:00` | 7.0h | `$13.5139` | `$14.0770` | **+4.17%** | **+4.08%** | +5.6% | -0.7% | `target_reclaim` |
| 13 | Book 3 | `2025-09-21 09:00` | `2025-09-22 06:00` | 21.0h | `$9.8208` | `$9.0125` | **-8.23%** | **-8.59%** | +3.3% | -14.9% | `stop_loss` |
| 14 | Book 3 | `2026-08-23 04:00` | `2026-08-23 09:00` | 5.0h | `$3.0106` | `$3.1360` | **+4.17%** | **+4.08%** | +4.5% | -0.4% | `target_reclaim` |
| 15 | Book 3 | `2026-09-01 02:00` | `2026-09-04 02:00` | 72.0h | `$3.3419` | `$3.3586` | **+0.50%** | **+0.50%** | +5.2% | -5.1% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `9` | `100.0%` | **`+79.1%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `time_expiry` | `1` | `100.0%` | **`+0.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `AUCTION`

* **Total Candidate Breakouts Filtered (Vetoed):** `457`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `254` (55.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `79`
* **Saved Capital Losses Avoided:** `+4,922.1%`
* **Missed Upside Forgone:** `-2,445.1%`
* **Net Veto Alpha:** `+2,477.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `290` | `63.5%` |
| `Core 1: Macro Bear Veto` | `146` | `31.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `20` | `4.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*