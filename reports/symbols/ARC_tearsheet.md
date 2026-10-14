# Kronos V12: Institutional Symbol Tear Sheet — `ARC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `9` (`9` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `9` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`55.6%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.837`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-5.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.94x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.64%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-26.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`20.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.5% / -13.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-01-18 15:00` | `2025-01-22 15:00` | Live | `$0.3291` | `$0.3571` | **+8.50%** | **+8.16%** | +55.3% | -56.4% | `shelf_target_reclaim` |
| 2 | Book 3 | `2025-04-23 16:00` | `2025-04-23 18:00` | 2.0h | `$0.0518` | `$0.0540` | **+4.17%** | **+4.08%** | +9.4% | -12.2% | `target_reclaim` |
| 3 | Book 3 | `2025-04-25 09:00` | `2025-04-25 11:00` | 2.0h | `$0.0603` | `$0.0628` | **+4.17%** | **+4.08%** | +7.9% | -5.3% | `target_reclaim` |
| 4 | Book 3 | `2025-04-25 13:00` | `2025-04-25 16:00` | 3.0h | `$0.0618` | `$0.0567` | **-8.23%** | **-8.59%** | +2.1% | -10.0% | `stop_loss` |
| 5 | Book 3 | `2025-04-27 01:00` | `2025-04-27 02:00` | 1.0h | `$0.0648` | `$0.0588` | **-9.23%** | **-9.68%** | +6.9% | -14.2% | `stop_loss` |
| 6 | Book 3 | `2025-04-28 15:00` | `2025-04-30 03:00` | 36.0h | `$0.0648` | `$0.0595` | **-8.23%** | **-8.59%** | +8.2% | -8.4% | `stop_loss` |
| 7 | Book 3 | `2025-05-09 07:00` | `2025-05-09 08:00` | 1.0h | `$0.0716` | `$0.0746` | **+4.17%** | **+4.08%** | +9.3% | -0.9% | `target_reclaim` |
| 8 | Book 3 | `2025-07-11 21:00` | `2025-07-14 04:00` | 55.0h | `$0.0311` | `$0.0341` | **+9.70%** | **+9.25%** | +10.6% | -6.6% | `target_reclaim` |
| 9 | Book 3 | `2026-09-16 16:00` | `2026-09-19 09:00` | 65.0h | `$0.0734` | `$0.0673` | **-8.23%** | **-8.59%** | +3.0% | -8.1% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `4` | `0.0%` | **`-35.4%`** |
| `target_reclaim` | `4` | `100.0%` | **`+21.5%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `ARC`

* **Total Candidate Breakouts Filtered (Vetoed):** `80`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `68` (85.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `22`
* **Saved Capital Losses Avoided:** `+1,986.2%`
* **Missed Upside Forgone:** `-661.2%`
* **Net Veto Alpha:** `+1,325.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `65` | `81.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `13` | `16.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2` | `2.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*