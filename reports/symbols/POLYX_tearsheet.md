# Kronos V12: Institutional Symbol Tear Sheet — `POLYX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `11` (`11` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `11` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`45.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.740`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-13.0%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.88x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.18%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-35.2%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`46.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+14.9% / -10.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2023-10-26 10:00` | `2023-10-30 10:00` | Live | `$0.2105` | `$0.2284` | **+8.50%** | **+8.16%** | +87.9% | -25.7% | `shelf_target_reclaim` |
| 2 | Book 3 | `2023-12-04 11:00` | `2023-12-04 23:00` | 12.0h | `$0.2146` | `$0.2259` | **+5.28%** | **+5.14%** | +15.9% | -12.2% | `target_reclaim` |
| 3 | Book 3 | `2024-01-06 07:00` | `2024-01-06 13:00` | 6.0h | `$0.2078` | `$0.2165` | **+4.17%** | **+4.08%** | +9.8% | -5.6% | `target_reclaim` |
| 4 | Book 3 | `2024-02-28 09:00` | `2024-02-28 17:00` | 8.0h | `$0.1937` | `$0.1778` | **-8.23%** | **-8.59%** | +3.1% | -10.3% | `stop_loss` |
| 5 | Book 3 | `2024-03-05 19:00` | `2024-03-08 17:00` | 70.0h | `$0.2170` | `$0.2480` | **+14.30%** | **+13.37%** | +20.9% | -16.1% | `target_reclaim` |
| 6 | Book 3 | `2024-04-01 05:00` | `2024-04-01 18:00` | 13.0h | `$0.6019` | `$0.5524` | **-8.23%** | **-8.59%** | +2.4% | -8.1% | `stop_loss` |
| 7 | Book 3 | `2024-07-21 13:00` | `2024-07-23 16:00` | 51.0h | `$0.2852` | `$0.2618` | **-8.23%** | **-8.59%** | +2.3% | -9.0% | `stop_loss` |
| 8 | Book 3 | `2024-12-03 14:00` | `2024-12-03 16:00` | 2.0h | `$0.3715` | `$0.3959` | **+6.58%** | **+6.37%** | +10.1% | -0.4% | `target_reclaim` |
| 9 | Book 3 | `2025-04-28 01:00` | `2025-05-01 01:00` | 72.0h | `$0.1527` | `$0.1524` | **-0.16%** | **-0.16%** | +6.2% | -4.0% | `time_expiry` |
| 10 | Book 4 | `2025-07-21 13:00` | `2025-07-24 06:00` | 65.0h | `$0.1702` | `$0.1447` | **-18.12%** | **-19.64%** | +1.1% | -16.8% | `structural_stop` |
| 11 | Book 4 | `2026-09-23 04:00` | `2026-09-30 04:00` | 168.0h | `$0.0449` | `$0.0430` | **-4.49%** | **-4.57%** | +4.4% | -8.3% | `stagnation_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+29.0%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-4.6%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `structural_stop` | `1` | `0.0%` | **`-19.6%`** |
| `time_expiry` | `1` | `0.0%` | **`-0.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `POLYX`

* **Total Candidate Breakouts Filtered (Vetoed):** `439`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `275` (62.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `99`
* **Saved Capital Losses Avoided:** `+4,457.1%`
* **Missed Upside Forgone:** `-2,436.9%`
* **Net Veto Alpha:** `+2,020.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `394` | `89.7%` |
| `Core 1: Macro Bear Veto` | `24` | `5.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `20` | `4.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*