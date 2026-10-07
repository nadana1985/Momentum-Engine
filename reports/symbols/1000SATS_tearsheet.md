# Kronos V12: Institutional Symbol Tear Sheet — `1000SATS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `15` (`15` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `15` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`40.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.739`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-17.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.84x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.18%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-31.2%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`23.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.7% / -8.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-02-20 00:00` | `2024-02-20 15:00` | 15.0h | `$0.0005` | `$0.0005` | **-8.23%** | **-8.59%** | +4.3% | -13.4% | `stop_loss` |
| 2 | Book 3 | `2024-02-28 17:00` | `2024-02-28 18:00` | 1.0h | `$0.0005` | `$0.0005` | **-8.23%** | **-8.59%** | +8.3% | -14.2% | `stop_loss` |
| 3 | Book 3 | `2024-02-29 12:00` | `2024-02-29 22:00` | 10.0h | `$0.0006` | `$0.0005` | **-8.23%** | **-8.59%** | +4.0% | -9.5% | `stop_loss` |
| 4 | Book 3 | `2024-03-03 07:00` | `2024-03-03 10:00` | 3.0h | `$0.0006` | `$0.0006` | **+8.70%** | **+8.34%** | +9.8% | -5.8% | `target_reclaim` |
| 5 | Book 3 | `2024-03-05 16:00` | `2024-03-05 19:00` | 3.0h | `$0.0006` | `$0.0006` | **-8.23%** | **-8.59%** | +7.1% | -16.4% | `stop_loss` |
| 6 | Book 3 | `2024-05-23 12:00` | `2024-05-23 13:00` | 1.0h | `$0.0003` | `$0.0003` | **-8.23%** | **-8.59%** | +4.0% | -8.6% | `stop_loss` |
| 7 | Book 3 | `2024-06-01 04:00` | `2024-06-04 04:00` | 72.0h | `$0.0003` | `$0.0003` | **-4.86%** | **-4.98%** | +5.4% | -5.9% | `time_expiry` |
| 8 | Book 3 | `2024-07-27 17:00` | `2024-07-28 11:00` | 18.0h | `$0.0003` | `$0.0003` | **+8.70%** | **+8.34%** | +8.7% | -1.1% | `target_reclaim` |
| 9 | Book 3 | `2024-11-11 05:00` | `2024-11-12 10:00` | 29.0h | `$0.0003` | `$0.0003` | **-8.23%** | **-8.59%** | +5.7% | -13.6% | `stop_loss` |
| 10 | Book 3 | `2024-12-04 16:00` | `2024-12-07 10:00` | 66.0h | `$0.0003` | `$0.0003` | **+8.70%** | **+8.34%** | +9.2% | -4.8% | `target_reclaim` |
| 11 | Book 3 | `2025-04-27 16:00` | `2025-04-30 16:00` | 72.0h | `$0.0000` | `$0.0000` | **-2.57%** | **-2.60%** | +4.8% | -6.0% | `time_expiry` |
| 12 | Book 3 | `2025-05-14 16:00` | `2025-05-15 00:00` | 8.0h | `$0.0001` | `$0.0001` | **+8.70%** | **+8.34%** | +11.2% | -1.1% | `target_reclaim` |
| 13 | Book 3 | `2025-07-18 19:00` | `2025-07-18 22:00` | 3.0h | `$0.0000` | `$0.0001` | **+8.70%** | **+8.34%** | +9.5% | -3.5% | `target_reclaim` |
| 14 | Book 3 | `2026-08-22 05:00` | `2026-08-23 04:00` | 23.0h | `$0.0000` | `$0.0000` | **-8.23%** | **-8.59%** | +13.2% | -18.3% | `stop_loss` |
| 15 | Book 3 | `2026-09-28 09:00` | `2026-09-29 14:00` | 29.0h | `$0.0000` | `$0.0000` | **+8.70%** | **+8.34%** | +9.7% | -2.6% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `7` | `0.0%` | **`-60.1%`** |
| `target_reclaim` | `6` | `100.0%` | **`+50.0%`** |
| `time_expiry` | `2` | `0.0%` | **`-7.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `1000SATS`

* **Total Candidate Breakouts Filtered (Vetoed):** `83`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `74` (89.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `20`
* **Saved Capital Losses Avoided:** `+1,376.4%`
* **Missed Upside Forgone:** `-956.2%`
* **Net Veto Alpha:** `+420.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `41` | `49.4%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `34` | `41.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `7` | `8.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `1.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*