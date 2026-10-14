# Kronos V12: Institutional Symbol Tear Sheet — `IN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.067`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+1.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.01x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.28%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-12.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`3.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+24.5% / -9.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-09-25 21:00` | `2025-09-25 23:00` | 2.0h | `$0.0836` | `$0.0767` | **-8.23%** | **-8.59%** | +5.4% | -8.1% | `stop_loss` |
| 2 | Book 3 | `2025-10-04 10:00` | `2025-10-04 11:00` | 1.0h | `$0.1294` | `$0.1146` | **-11.46%** | **-12.17%** | +20.5% | -16.9% | `stop_loss` |
| 3 | Book 3 | `2025-10-10 07:00` | `2025-10-10 08:00` | 1.0h | `$0.1831` | `$0.1990` | **+8.70%** | **+8.34%** | +20.2% | -6.4% | `target_reclaim` |
| 4 | Book 4 | `2026-05-22 17:00` | `2026-05-23 01:00` | 8.0h | `$0.0719` | `$0.0862` | **+5.79%** | **+5.65%** | +26.0% | -0.4% | `target_reclaim` |
| 5 | Book 5 (Shelf Absorption Squeeze) | `2026-05-22 23:00` | `2026-05-26 23:00` | Live | `$0.0724` | `$0.0785` | **+8.50%** | **+8.16%** | +50.4% | -13.3% | `shelf_target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-20.8%`** |
| `target_reclaim` | `2` | `100.0%` | **`+14.0%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `IN`

* **Total Candidate Breakouts Filtered (Vetoed):** `453`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `319` (70.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `163`
* **Saved Capital Losses Avoided:** `+6,513.0%`
* **Missed Upside Forgone:** `-6,060.8%`
* **Net Veto Alpha:** `+452.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `442` | `97.6%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `5` | `1.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `0.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2` | `0.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*