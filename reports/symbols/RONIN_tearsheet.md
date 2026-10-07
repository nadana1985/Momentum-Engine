# Kronos V12: Institutional Symbol Tear Sheet — `RONIN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `10` (`10` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `10` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.944`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-1.9%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.98x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.19%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-23.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`36.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.5% / -6.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-03-15 03:00` | `2024-03-16 07:00` | 28.0h | `$3.9220` | `$4.2630` | **+8.70%** | **+8.34%** | +10.9% | -5.1% | `target_reclaim` |
| 2 | Book 3 | `2024-09-30 23:00` | `2024-10-01 17:00` | 18.0h | `$1.7780` | `$1.6317` | **-8.23%** | **-8.59%** | +2.9% | -9.1% | `stop_loss` |
| 3 | Book 3 | `2024-12-05 22:00` | `2024-12-06 18:00` | 20.0h | `$2.1596` | `$2.3474` | **+8.70%** | **+8.34%** | +8.8% | -1.1% | `target_reclaim` |
| 4 | Book 3 | `2024-12-18 20:00` | `2024-12-19 02:00` | 6.0h | `$2.2845` | `$2.0965` | **-8.23%** | **-8.59%** | +2.9% | -8.9% | `stop_loss` |
| 5 | Book 3 | `2025-05-14 23:00` | `2025-05-17 00:00` | 49.0h | `$0.7054` | `$0.6473` | **-8.23%** | **-8.59%** | +2.3% | -8.5% | `stop_loss` |
| 6 | Book 3 | `2025-08-14 12:00` | `2025-08-17 12:00` | 72.0h | `$0.5546` | `$0.5649` | **+1.86%** | **+1.84%** | +6.0% | -3.3% | `time_expiry` |
| 7 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0561` | `$0.0565` | **+0.67%** | **+0.67%** | +13.4% | -4.4% | `time_expiry` |
| 8 | Book 3 | `2026-09-15 14:00` | `2026-09-15 15:00` | 1.0h | `$0.0540` | `$0.0496` | **-8.23%** | **-8.59%** | +2.0% | -15.0% | `stop_loss` |
| 9 | Book 3 | `2026-09-23 17:00` | `2026-09-24 17:00` | 24.0h | `$0.0573` | `$0.0622` | **+8.70%** | **+8.34%** | +9.4% | -1.7% | `target_reclaim` |
| 10 | Book 3 | `2026-09-28 05:00` | `2026-10-01 05:00` | 72.0h | `$0.0622` | `$0.0653` | **+5.04%** | **+4.92%** | +6.2% | -4.8% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `target_reclaim` | `3` | `100.0%` | **`+25.0%`** |
| `time_expiry` | `3` | `100.0%` | **`+7.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `RONIN`

* **Total Candidate Breakouts Filtered (Vetoed):** `123`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `69` (56.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `9`
* **Saved Capital Losses Avoided:** `+770.1%`
* **Missed Upside Forgone:** `-248.9%`
* **Net Veto Alpha:** `+521.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `61` | `49.6%` |
| `Core 1: Macro Bear Veto` | `53` | `43.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `8` | `6.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `0.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*