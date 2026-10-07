# Kronos V12: Institutional Symbol Tear Sheet — `RED`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `10` (`10` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `10` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.971`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-1.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.13%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-26.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`36.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.5% / -7.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-15 05:00` | `2025-05-17 01:00` | 44.0h | `$0.4485` | `$0.4116` | **-8.23%** | **-8.59%** | +2.6% | -11.2% | `stop_loss` |
| 2 | Book 3 | `2025-07-18 20:00` | `2025-07-20 11:00` | 39.0h | `$0.3345` | `$0.3636` | **+8.70%** | **+8.34%** | +10.5% | -1.4% | `target_reclaim` |
| 3 | Book 3 | `2025-07-23 17:00` | `2025-07-24 07:00` | 14.0h | `$0.3496` | `$0.3208` | **-8.23%** | **-8.59%** | +3.3% | -8.7% | `stop_loss` |
| 4 | Book 3 | `2025-07-29 00:00` | `2025-07-29 09:00` | 9.0h | `$0.3530` | `$0.3837` | **+8.70%** | **+8.34%** | +11.0% | -0.8% | `target_reclaim` |
| 5 | Book 3 | `2025-07-29 14:00` | `2025-07-30 19:00` | 29.0h | `$0.3912` | `$0.3590` | **-8.23%** | **-8.59%** | +3.1% | -9.6% | `stop_loss` |
| 6 | Book 3 | `2025-08-11 12:00` | `2025-08-14 12:00` | 72.0h | `$0.4213` | `$0.3866` | **-8.23%** | **-8.59%** | +5.1% | -12.4% | `stop_loss` |
| 7 | Book 3 | `2026-08-22 05:00` | `2026-08-24 01:00` | 44.0h | `$0.1165` | `$0.1069` | **-8.23%** | **-8.59%** | +7.1% | -23.2% | `stop_loss` |
| 8 | Book 3 | `2026-09-16 13:00` | `2026-09-18 09:00` | 44.0h | `$0.1281` | `$0.1392` | **+8.70%** | **+8.34%** | +10.6% | -2.7% | `target_reclaim` |
| 9 | Book 3 | `2026-09-28 09:00` | `2026-09-30 12:00` | 51.0h | `$0.1599` | `$0.1738` | **+8.70%** | **+8.34%** | +13.0% | -2.6% | `target_reclaim` |
| 10 | Book 3 | `2026-10-02 18:00` | `2026-10-03 15:00` | 21.0h | `$0.1648` | `$0.1791` | **+8.70%** | **+8.34%** | +9.1% | -2.3% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `5` | `0.0%` | **`-42.9%`** |
| `target_reclaim` | `5` | `100.0%` | **`+41.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `RED`

* **Total Candidate Breakouts Filtered (Vetoed):** `49`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `34` (69.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `3`
* **Saved Capital Losses Avoided:** `+486.6%`
* **Missed Upside Forgone:** `-141.1%`
* **Net Veto Alpha:** `+345.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `22` | `44.9%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `20` | `40.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `7` | `14.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*