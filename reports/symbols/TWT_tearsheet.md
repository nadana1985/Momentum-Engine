# Kronos V12: Institutional Symbol Tear Sheet — `TWT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `12` (`12` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `12` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.435`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+16.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.18x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.41%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-36.0%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`94.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+14.0% / -7.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2023-11-04 16:00` | `2023-11-08 16:00` | Live | `$1.1743` | `$1.2741` | **+8.50%** | **+8.16%** | +36.8% | -19.0% | `shelf_target_reclaim` |
| 2 | Book 3 | `2023-12-09 23:00` | `2023-12-12 23:00` | 72.0h | `$1.2143` | `$1.1797` | **-2.85%** | **-2.89%** | +4.1% | -6.9% | `time_expiry` |
| 3 | Book 4 | `2024-02-13 04:00` | `2024-02-29 05:00` | 385.0h | `$1.1993` | `$1.4392` | **+22.89%** | **+20.95%** | +20.1% | -2.3% | `target_reclaim` |
| 4 | Book 3 | `2024-03-14 13:00` | `2024-03-15 03:00` | 14.0h | `$1.5377` | `$1.4111` | **-8.23%** | **-8.59%** | +3.3% | -8.7% | `stop_loss` |
| 5 | Book 3 | `2024-06-07 18:00` | `2024-06-08 22:00` | 28.0h | `$1.2678` | `$1.1635` | **-8.23%** | **-8.59%** | +1.2% | -12.6% | `stop_loss` |
| 6 | Book 3 | `2024-09-16 00:00` | `2024-09-16 22:00` | 22.0h | `$0.9348` | `$0.8578` | **-8.23%** | **-8.59%** | +2.6% | -23.2% | `stop_loss` |
| 7 | Book 3 | `2024-10-07 22:00` | `2024-10-10 22:00` | 72.0h | `$1.0408` | `$1.0238` | **-1.63%** | **-1.65%** | +3.1% | -3.6% | `time_expiry` |
| 8 | Book 3 | `2024-11-12 10:00` | `2024-11-14 14:00` | 52.0h | `$1.0530` | `$0.9664` | **-8.23%** | **-8.59%** | +1.4% | -8.1% | `stop_loss` |
| 9 | Book 3 | `2025-04-28 02:00` | `2025-05-01 02:00` | 72.0h | `$0.7837` | `$0.7945` | **+1.37%** | **+1.36%** | +5.9% | -0.9% | `time_expiry` |
| 10 | Book 4 | `2025-09-18 12:00` | `2025-09-30 15:00` | 291.0h | `$0.8839` | `$1.2375` | **+14.95%** | **+13.08%** | +73.9% | -2.7% | `donchian_floor` |
| 11 | Book 3 | `2025-10-09 11:00` | `2025-10-10 04:00` | 17.0h | `$1.4650` | `$1.5898` | **+8.52%** | **+8.18%** | +11.5% | -2.7% | `target_reclaim` |
| 12 | Book 3 | `2026-09-01 17:00` | `2026-09-02 04:00` | 11.0h | `$0.5290` | `$0.5510` | **+4.17%** | **+4.08%** | +4.2% | -1.1% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `time_expiry` | `3` | `33.3%` | **`-3.2%`** |
| `target_reclaim` | `3` | `100.0%` | **`+33.2%`** |
| `donchian_floor` | `1` | `100.0%` | **`+13.1%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `TWT`

* **Total Candidate Breakouts Filtered (Vetoed):** `725`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `393` (54.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `129`
* **Saved Capital Losses Avoided:** `+3,011.2%`
* **Missed Upside Forgone:** `-3,943.4%`
* **Net Veto Alpha:** `+-932.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `306` | `42.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `194` | `26.8%` |
| `Core 1: Macro Bear Veto` | `172` | `23.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `53` | `7.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*