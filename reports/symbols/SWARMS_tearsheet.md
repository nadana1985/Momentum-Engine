# Kronos V12: Institutional Symbol Tear Sheet — `SWARMS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`57.1%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.863`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-2.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.97x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.39%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-20.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`17.9h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.5% / -8.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-04-23 03:00` | `2025-04-23 04:00` | 1.0h | `$0.0367` | `$0.0383` | **+4.17%** | **+4.08%** | +10.8% | -3.8% | `target_reclaim` |
| 2 | Book 3 | `2025-05-12 05:00` | `2025-05-12 07:00` | 2.0h | `$0.0422` | `$0.0440` | **+4.17%** | **+4.08%** | +10.0% | -2.5% | `target_reclaim` |
| 3 | Book 3 | `2025-07-05 13:00` | `2025-07-08 13:00` | 72.0h | `$0.0227` | `$0.0221` | **-2.88%** | **-2.92%** | +14.5% | -5.1% | `time_expiry` |
| 4 | Book 3 | `2025-08-10 22:00` | `2025-08-11 00:00` | 2.0h | `$0.0294` | `$0.0270` | **-8.23%** | **-8.59%** | +8.2% | -11.4% | `stop_loss` |
| 5 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0089` | `$0.0082` | **-8.23%** | **-8.59%** | +11.0% | -28.0% | `stop_loss` |
| 6 | Book 3 | `2026-09-22 14:00` | `2026-09-22 16:00` | 2.0h | `$0.0081` | `$0.0084` | **+4.17%** | **+4.08%** | +5.5% | -1.8% | `target_reclaim` |
| 7 | Book 3 | `2026-09-23 14:00` | `2026-09-25 11:00` | 45.0h | `$0.0081` | `$0.0086` | **+5.22%** | **+5.09%** | +6.4% | -6.9% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+17.3%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `time_expiry` | `1` | `0.0%` | **`-2.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `SWARMS`

* **Total Candidate Breakouts Filtered (Vetoed):** `72`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `61` (84.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `9`
* **Saved Capital Losses Avoided:** `+1,222.8%`
* **Missed Upside Forgone:** `-249.9%`
* **Net Veto Alpha:** `+972.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `57` | `79.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `6` | `8.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `5` | `6.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `5.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*