# Kronos V12: Institutional Symbol Tear Sheet — `RED`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `13` (`13` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `13` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`69.2%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.883`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+30.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.35x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.33%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-23.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`38.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.5% / -8.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-03-12 15:00` | `2025-03-16 15:00` | Live | `$0.5515` | `$0.5984` | **+8.50%** | **+8.16%** | +28.4% | -18.2% | `shelf_target_reclaim` |
| 2 | Book 3 | `2025-05-15 05:00` | `2025-05-17 01:00` | 44.0h | `$0.4485` | `$0.4116` | **-8.23%** | **-8.59%** | +2.6% | -11.2% | `stop_loss` |
| 3 | Book 3 | `2025-07-18 15:00` | `2025-07-20 11:00` | 44.0h | `$0.3491` | `$0.3636` | **+4.17%** | **+4.08%** | +5.9% | -5.5% | `target_reclaim` |
| 4 | Book 3 | `2025-07-23 17:00` | `2025-07-24 06:00` | 13.0h | `$0.3567` | `$0.3273` | **-8.23%** | **-8.59%** | +1.3% | -9.7% | `stop_loss` |
| 5 | Book 3 | `2025-07-28 21:00` | `2025-07-29 09:00` | 12.0h | `$0.3567` | `$0.3837` | **+7.57%** | **+7.30%** | +9.8% | -1.8% | `target_reclaim` |
| 6 | Book 3 | `2025-07-29 14:00` | `2025-07-30 12:00` | 22.0h | `$0.3986` | `$0.3658` | **-8.23%** | **-8.59%** | +1.2% | -8.4% | `stop_loss` |
| 7 | Book 3 | `2025-08-12 11:00` | `2025-08-15 00:00` | 61.0h | `$0.3986` | `$0.3658` | **-8.23%** | **-8.59%** | +8.8% | -8.3% | `stop_loss` |
| 8 | Book 5 (Shelf Absorption Squeeze) | `2026-04-06 09:00` | `2026-04-10 09:00` | Live | `$0.1279` | `$0.1387` | **+8.50%** | **+8.16%** | +42.2% | -8.6% | `shelf_target_reclaim` |
| 9 | Book 5 (Shelf Absorption Squeeze) | `2026-08-18 04:00` | `2026-08-22 04:00` | Live | `$0.0995` | `$0.1079` | **+8.50%** | **+8.16%** | +30.3% | -17.2% | `shelf_target_reclaim` |
| 10 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.1117` | `$0.1155` | **+3.43%** | **+3.37%** | +11.7% | -19.9% | `time_expiry` |
| 11 | Book 3 | `2026-09-16 13:00` | `2026-09-18 09:00` | 44.0h | `$0.1275` | `$0.1392` | **+9.19%** | **+8.79%** | +11.2% | -2.3% | `target_reclaim` |
| 12 | Book 3 | `2026-09-28 09:00` | `2026-09-30 12:00` | 51.0h | `$0.1599` | `$0.1738` | **+8.70%** | **+8.34%** | +13.0% | -2.6% | `target_reclaim` |
| 13 | Book 3 | `2026-10-02 18:00` | `2026-10-03 15:00` | 21.0h | `$0.1648` | `$0.1791` | **+8.70%** | **+8.34%** | +9.1% | -2.3% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `5` | `100.0%` | **`+36.8%`** |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `shelf_target_reclaim` | `3` | `100.0%` | **`+24.5%`** |
| `time_expiry` | `1` | `100.0%` | **`+3.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `RED`

* **Total Candidate Breakouts Filtered (Vetoed):** `74`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `56` (75.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `3`
* **Saved Capital Losses Avoided:** `+736.8%`
* **Missed Upside Forgone:** `-141.1%`
* **Net Veto Alpha:** `+595.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `30` | `40.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `22` | `29.7%` |
| `Core 1: Macro Bear Veto` | `22` | `29.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*