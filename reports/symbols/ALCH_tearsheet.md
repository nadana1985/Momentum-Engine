# Kronos V12: Institutional Symbol Tear Sheet — `ALCH`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.897`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-2.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.97x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.44%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-21.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`8.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.6% / -7.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2025-04-13 12:00` | `2025-04-13 15:00` | 3.0h | `$0.1165` | `$0.1398` | **+11.19%** | **+10.70%** | +25.0% | -3.3% | `target_reclaim` |
| 2 | Book 3 | `2025-04-15 14:00` | `2025-04-15 15:00` | 1.0h | `$0.1404` | `$0.1527` | **+8.70%** | **+8.34%** | +20.3% | -0.5% | `target_reclaim` |
| 3 | Book 3 | `2025-04-25 18:00` | `2025-04-27 06:00` | 36.0h | `$0.1653` | `$0.1517` | **-8.23%** | **-8.59%** | +2.8% | -10.3% | `stop_loss` |
| 4 | Book 3 | `2025-07-03 02:00` | `2025-07-03 08:00` | 6.0h | `$0.1361` | `$0.1418` | **+4.17%** | **+4.08%** | +5.6% | -3.4% | `target_reclaim` |
| 5 | Book 3 | `2025-10-04 10:00` | `2025-10-04 11:00` | 1.0h | `$0.0961` | `$0.0882` | **-8.23%** | **-8.59%** | +35.1% | -20.9% | `stop_loss` |
| 6 | Book 3 | `2026-09-21 21:00` | `2026-09-22 03:00` | 6.0h | `$0.0546` | `$0.0501` | **-8.23%** | **-8.59%** | +10.8% | -8.1% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `target_reclaim` | `3` | `100.0%` | **`+23.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `ALCH`

* **Total Candidate Breakouts Filtered (Vetoed):** `490`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `304` (62.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `228`
* **Saved Capital Losses Avoided:** `+6,811.6%`
* **Missed Upside Forgone:** `-8,333.0%`
* **Net Veto Alpha:** `+-1,521.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `266` | `54.3%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `131` | `26.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `88` | `18.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `0.8%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*