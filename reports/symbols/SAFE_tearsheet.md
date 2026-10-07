# Kronos V12: Institutional Symbol Tear Sheet — `SAFE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `12` (`12` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `12` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.721`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+20.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.22x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.67%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-9.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`44.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.6% / -4.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-12-03 13:00` | `2024-12-04 00:00` | 11.0h | `$1.2570` | `$1.3663` | **+8.70%** | **+8.34%** | +11.8% | -3.2% | `target_reclaim` |
| 2 | Book 3 | `2025-03-28 00:00` | `2025-03-29 00:00` | 24.0h | `$0.5972` | `$0.5480` | **-8.23%** | **-8.59%** | +5.5% | -8.8% | `stop_loss` |
| 3 | Book 3 | `2025-05-28 20:00` | `2025-05-29 14:00` | 18.0h | `$0.5622` | `$0.6111` | **+8.70%** | **+8.34%** | +9.6% | -0.4% | `target_reclaim` |
| 4 | Book 3 | `2025-05-30 20:00` | `2025-05-31 00:00` | 4.0h | `$0.5788` | `$0.5311` | **-8.23%** | **-8.59%** | +0.5% | -13.2% | `stop_loss` |
| 5 | Book 3 | `2025-07-01 11:00` | `2025-07-04 11:00` | 72.0h | `$0.3876` | `$0.4056` | **+4.64%** | **+4.54%** | +8.4% | -3.4% | `time_expiry` |
| 6 | Book 3 | `2025-07-07 16:00` | `2025-07-10 16:00` | 72.0h | `$0.4192` | `$0.4321` | **+3.09%** | **+3.05%** | +5.0% | -1.4% | `time_expiry` |
| 7 | Book 3 | `2025-10-29 08:00` | `2025-10-30 17:00` | 33.0h | `$0.2420` | `$0.2220` | **-8.23%** | **-8.59%** | +3.1% | -9.4% | `stop_loss` |
| 8 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0903` | `$0.0934` | **+3.39%** | **+3.33%** | +11.7% | -2.9% | `time_expiry` |
| 9 | Book 3 | `2026-09-09 22:00` | `2026-09-12 22:00` | 72.0h | `$0.0948` | `$0.0984` | **+3.76%** | **+3.70%** | +5.2% | -2.0% | `time_expiry` |
| 10 | Book 3 | `2026-09-23 23:00` | `2026-09-24 15:00` | 16.0h | `$0.1043` | `$0.1134` | **+8.70%** | **+8.34%** | +9.2% | -1.6% | `target_reclaim` |
| 11 | Book 3 | `2026-09-28 10:00` | `2026-10-01 02:00` | 64.0h | `$0.1081` | `$0.1174` | **+8.70%** | **+8.34%** | +9.9% | -3.5% | `target_reclaim` |
| 12 | Book 3 | `2026-10-01 05:00` | `2026-10-04 05:00` | 72.0h | `$0.1132` | `$0.1109` | **-2.09%** | **-2.11%** | +11.2% | -7.1% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_expiry` | `5` | `80.0%` | **`+12.5%`** |
| `target_reclaim` | `4` | `100.0%` | **`+33.4%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `SAFE`

* **Total Candidate Breakouts Filtered (Vetoed):** `72`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `59` (81.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `9`
* **Saved Capital Losses Avoided:** `+874.3%`
* **Missed Upside Forgone:** `-230.9%`
* **Net Veto Alpha:** `+643.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `32` | `44.4%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `28` | `38.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `9` | `12.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `3` | `4.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*