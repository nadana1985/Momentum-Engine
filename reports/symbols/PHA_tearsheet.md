# Kronos V12: Institutional Symbol Tear Sheet — `PHA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`57.1%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.764`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-6.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.94x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.87%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`28.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+14.0% / -6.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-15 10:00` | `2025-05-17 09:00` | 47.0h | `$0.1344` | `$0.1233` | **-8.23%** | **-8.59%** | +4.0% | -8.3% | `stop_loss` |
| 2 | Book 3 | `2025-07-23 21:00` | `2025-07-26 21:00` | 72.0h | `$0.1133` | `$0.1146` | **+1.08%** | **+1.07%** | +5.1% | -5.0% | `time_expiry` |
| 3 | Book 3 | `2025-09-19 15:00` | `2025-09-19 16:00` | 1.0h | `$0.1115` | `$0.1162` | **+4.17%** | **+4.08%** | +4.4% | -0.4% | `target_reclaim` |
| 4 | Book 5 (Shelf Absorption Squeeze) | `2026-03-03 06:00` | `2026-03-07 06:00` | Live | `$0.0309` | `$0.0335` | **+8.50%** | **+8.16%** | +63.7% | -12.3% | `shelf_target_reclaim` |
| 5 | Book 3 | `2026-09-08 10:00` | `2026-09-09 08:00` | 22.0h | `$0.0257` | `$0.0274` | **+6.58%** | **+6.37%** | +10.9% | -3.9% | `target_reclaim` |
| 6 | Book 3 | `2026-09-10 12:00` | `2026-09-11 12:00` | 24.0h | `$0.0257` | `$0.0236` | **-8.23%** | **-8.59%** | +5.6% | -8.3% | `stop_loss` |
| 7 | Book 3 | `2026-09-28 01:00` | `2026-09-28 05:00` | 4.0h | `$0.0651` | `$0.0597` | **-8.23%** | **-8.59%** | +4.5% | -9.3% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `target_reclaim` | `2` | `100.0%` | **`+10.5%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `time_expiry` | `1` | `100.0%` | **`+1.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `PHA`

* **Total Candidate Breakouts Filtered (Vetoed):** `135`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `97` (71.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `40`
* **Saved Capital Losses Avoided:** `+1,810.3%`
* **Missed Upside Forgone:** `-1,650.8%`
* **Net Veto Alpha:** `+159.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `80` | `59.3%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `35` | `25.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `16` | `11.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `3.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*