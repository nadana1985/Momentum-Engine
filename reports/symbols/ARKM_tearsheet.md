# Kronos V12: Institutional Symbol Tear Sheet — `ARKM`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `21` (`21` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `21` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`47.6%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.984`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-1.2%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.06%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-40.9%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`43.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.4% / -9.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2023-08-29 22:00` | `2023-09-02 22:00` | Live | `$0.3999` | `$0.4339` | **+8.50%** | **+8.16%** | +16.7% | -26.2% | `shelf_target_reclaim` |
| 2 | Book 3 | `2023-11-11 05:00` | `2023-11-13 08:00` | 51.0h | `$0.4271` | `$0.4657` | **+9.04%** | **+8.66%** | +12.0% | -4.9% | `target_reclaim` |
| 3 | Book 3 | `2023-11-17 11:00` | `2023-11-18 05:00` | 18.0h | `$0.4358` | `$0.4000` | **-8.23%** | **-8.59%** | +3.4% | -10.4% | `stop_loss` |
| 4 | Book 3 | `2023-12-16 19:00` | `2023-12-17 04:00` | 9.0h | `$0.5595` | `$0.5134` | **-8.23%** | **-8.59%** | +6.8% | -8.3% | `stop_loss` |
| 5 | Book 3 | `2023-12-18 03:00` | `2023-12-18 12:00` | 9.0h | `$0.5610` | `$0.5149` | **-8.23%** | **-8.59%** | +3.6% | -8.8% | `stop_loss` |
| 6 | Book 3 | `2023-12-19 08:00` | `2023-12-20 10:00` | 26.0h | `$0.6188` | `$0.6726` | **+8.70%** | **+8.34%** | +9.7% | -5.2% | `target_reclaim` |
| 7 | Book 3 | `2024-02-27 17:00` | `2024-02-28 14:00` | 21.0h | `$1.5448` | `$1.6791` | **+8.70%** | **+8.34%** | +20.5% | -7.4% | `target_reclaim` |
| 8 | Book 3 | `2024-02-28 17:00` | `2024-02-28 18:00` | 1.0h | `$1.6851` | `$1.8102` | **+7.43%** | **+7.16%** | +17.5% | -13.5% | `target_reclaim` |
| 9 | Book 3 | `2024-03-08 15:00` | `2024-03-08 16:00` | 1.0h | `$2.5715` | `$2.9470` | **+14.60%** | **+13.63%** | +16.2% | -4.5% | `target_reclaim` |
| 10 | Book 3 | `2024-03-10 09:00` | `2024-03-11 08:00` | 23.0h | `$3.0715` | `$3.3386` | **+8.70%** | **+8.34%** | +16.5% | -6.2% | `target_reclaim` |
| 11 | Book 3 | `2024-06-06 02:00` | `2024-06-07 18:00` | 40.0h | `$2.6328` | `$2.4162` | **-8.23%** | **-8.59%** | +4.0% | -19.6% | `stop_loss` |
| 12 | Book 3 | `2024-09-30 14:00` | `2024-10-01 15:00` | 25.0h | `$1.5266` | `$1.4010` | **-8.23%** | **-8.59%** | +3.0% | -9.9% | `stop_loss` |
| 13 | Book 3 | `2024-10-17 00:00` | `2024-10-20 00:00` | 72.0h | `$1.8088` | `$1.7723` | **-2.02%** | **-2.04%** | +3.3% | -5.9% | `time_expiry` |
| 14 | Book 3 | `2024-11-12 09:00` | `2024-11-12 10:00` | 1.0h | `$2.2672` | `$2.0806` | **-8.23%** | **-8.59%** | +4.2% | -9.1% | `stop_loss` |
| 15 | Book 3 | `2024-12-08 08:00` | `2024-12-09 20:00` | 36.0h | `$2.3631` | `$2.1686` | **-8.23%** | **-8.59%** | +3.2% | -15.8% | `stop_loss` |
| 16 | Book 3 | `2025-04-24 03:00` | `2025-04-24 14:00` | 11.0h | `$0.5288` | `$0.5508` | **+4.17%** | **+4.08%** | +7.0% | -1.5% | `target_reclaim` |
| 17 | Book 3 | `2025-05-15 03:00` | `2025-05-15 23:00` | 20.0h | `$0.7212` | `$0.6618` | **-8.23%** | **-8.59%** | +2.6% | -8.7% | `stop_loss` |
| 18 | Book 3 | `2025-07-18 20:00` | `2025-07-19 04:00` | 8.0h | `$0.5548` | `$0.5858` | **+5.59%** | **+5.44%** | +6.9% | -2.2% | `target_reclaim` |
| 19 | Book 3 | `2025-08-14 12:00` | `2025-08-17 12:00` | 72.0h | `$0.5574` | `$0.5651` | **+1.38%** | **+1.37%** | +8.2% | -6.2% | `time_expiry` |
| 20 | Book 2 | `2026-05-02 09:00` | `2026-05-04 09:00` | 48.0h | `$0.1215` | `$0.1202` | **-1.32%** | **-1.33%** | +3.2% | -4.0% | `fast_decay_cut` |
| 21 | Book 4 | `2026-09-25 12:00` | `2026-10-11 00:00` | 372.0h | `$0.1354` | `$0.1318` | **-2.60%** | **-2.63%** | +7.7% | -14.3% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `8` | `0.0%` | **`-68.7%`** |
| `target_reclaim` | `8` | `100.0%` | **`+64.0%`** |
| `time_expiry` | `3` | `33.3%` | **`-3.3%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.3%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `ARKM`

* **Total Candidate Breakouts Filtered (Vetoed):** `502`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `345` (68.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `35`
* **Saved Capital Losses Avoided:** `+4,788.6%`
* **Missed Upside Forgone:** `-1,194.3%`
* **Net Veto Alpha:** `+3,594.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `216` | `43.0%` |
| `Core 1: Macro Bear Veto` | `128` | `25.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `128` | `25.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `30` | `6.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*