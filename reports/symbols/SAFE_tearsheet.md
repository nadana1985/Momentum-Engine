# Kronos V12: Institutional Symbol Tear Sheet — `SAFE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `12` (`11` Closed, `1` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `11` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`81.8%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.820`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+31.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.37x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.84%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`50.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.9% / -10.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2024-12-05 11:00` | `2024-12-09 11:00` | Live | `$1.5537` | `$1.6858` | **+8.50%** | **+8.16%** | +4.5% | -42.9% | `shelf_target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2025-03-27 00:00` | `2025-03-31 00:00` | Live | `$0.4937` | `$0.5356` | **+8.50%** | **+8.16%** | +15.1% | -30.5% | `shelf_target_reclaim` |
| 3 | Book 3 | `2025-03-27 16:00` | `2025-03-27 21:00` | 5.0h | `$0.6184` | `$0.6491` | **+4.97%** | **+4.85%** | +7.9% | -2.3% | `target_reclaim` |
| 4 | Book 3 | `2025-05-28 09:00` | `2025-05-29 14:00` | 29.0h | `$0.5867` | `$0.6111` | **+4.17%** | **+4.08%** | +5.0% | -4.5% | `target_reclaim` |
| 5 | Book 3 | `2025-05-30 14:00` | `2025-05-30 22:00` | 8.0h | `$0.5904` | `$0.5418` | **-8.23%** | **-8.59%** | +6.0% | -9.1% | `stop_loss` |
| 6 | Book 3 | `2025-07-01 11:00` | `2025-07-04 11:00` | 72.0h | `$0.3876` | `$0.4056` | **+4.64%** | **+4.54%** | +8.4% | -3.4% | `time_expiry` |
| 7 | Book 3 | `2025-07-08 00:00` | `2025-07-11 00:00` | 72.0h | `$0.4168` | `$0.4421` | **+6.08%** | **+5.90%** | +8.1% | -0.8% | `time_expiry` |
| 8 | Book 3 | `2025-10-28 02:00` | `2025-10-30 12:00` | 58.0h | `$0.2525` | `$0.2317` | **-8.23%** | **-8.59%** | +2.5% | -8.8% | `stop_loss` |
| 9 | Book 3 | `2026-09-09 22:00` | `2026-09-12 22:00` | 72.0h | `$0.0946` | `$0.0984` | **+4.00%** | **+3.93%** | +5.5% | -1.8% | `time_expiry` |
| 10 | Book 3 | `2026-09-28 07:00` | `2026-10-01 02:00` | 67.0h | `$0.1096` | `$0.1174` | **+7.17%** | **+6.92%** | +8.3% | -4.9% | `target_reclaim` |
| 11 | Book 3 | `2026-10-01 13:00` | `2026-10-04 13:00` | 72.0h | `$0.1096` | `$0.1117` | **+1.92%** | **+1.90%** | +4.4% | -4.0% | `time_expiry` |
| 12 | Book 3 | `2026-10-13 00:00` | `_Open Live_` | 12.2h | `$0.1258` | `$0.1239` | **-1.49%** | **-1.50%** | +7.0% | -3.8% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_expiry` | `4` | `100.0%` | **`+16.3%`** |
| `target_reclaim` | `3` | `100.0%` | **`+15.9%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `SAFE`

* **Total Candidate Breakouts Filtered (Vetoed):** `154`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `141` (91.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `12`
* **Saved Capital Losses Avoided:** `+2,705.4%`
* **Missed Upside Forgone:** `-301.3%`
* **Net Veto Alpha:** `+2,404.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `109` | `70.8%` |
| `Core 1: Macro Bear Veto` | `32` | `20.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `9` | `5.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `4` | `2.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*