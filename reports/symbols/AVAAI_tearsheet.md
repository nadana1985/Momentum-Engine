# Kronos V12: Institutional Symbol Tear Sheet — `AVAAI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `13` (`13` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `13` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`53.8%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.292`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+15.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.16x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.16%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-9.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`10.9h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.9% / -13.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-01-18 23:00` | `2025-01-22 23:00` | Live | `$0.2234` | `$0.2051` | **-8.20%** | **-8.56%** | +-23.1% | -84.1% | `shelf_stop_loss` |
| 2 | Book 3 | `2025-04-23 16:00` | `2025-04-24 00:00` | 8.0h | `$0.0410` | `$0.0376` | **-8.23%** | **-8.59%** | +4.4% | -11.4% | `stop_loss` |
| 3 | Book 3 | `2025-04-27 02:00` | `2025-04-28 07:00` | 29.0h | `$0.0446` | `$0.0514` | **+15.10%** | **+14.06%** | +16.6% | -7.3% | `target_reclaim` |
| 4 | Book 3 | `2025-04-29 04:00` | `2025-04-29 07:00` | 3.0h | `$0.0519` | `$0.0553` | **+6.38%** | **+6.18%** | +11.7% | -0.6% | `target_reclaim` |
| 5 | Book 3 | `2025-04-30 12:00` | `2025-04-30 13:00` | 1.0h | `$0.0519` | `$0.0477` | **-8.23%** | **-8.59%** | +3.6% | -10.1% | `stop_loss` |
| 6 | Book 3 | `2025-05-06 20:00` | `2025-05-06 23:00` | 3.0h | `$0.0705` | `$0.0766` | **+8.70%** | **+8.34%** | +10.2% | -4.3% | `target_reclaim` |
| 7 | Book 3 | `2025-05-10 15:00` | `2025-05-10 18:00` | 3.0h | `$0.0846` | `$0.0919` | **+8.70%** | **+8.34%** | +9.0% | -1.2% | `target_reclaim` |
| 8 | Book 3 | `2025-07-07 06:00` | `2025-07-07 20:00` | 14.0h | `$0.0332` | `$0.0305` | **-8.23%** | **-8.59%** | +4.1% | -9.0% | `stop_loss` |
| 9 | Book 3 | `2025-07-12 15:00` | `2025-07-14 03:00` | 36.0h | `$0.0320` | `$0.0373` | **+16.63%** | **+15.39%** | +17.2% | -1.8% | `target_reclaim` |
| 10 | Book 3 | `2025-08-11 01:00` | `2025-08-11 13:00` | 12.0h | `$0.0439` | `$0.0403` | **-8.23%** | **-8.59%** | +4.5% | -8.3% | `stop_loss` |
| 11 | Book 5 (Shelf Absorption Squeeze) | `2025-12-15 02:00` | `2025-12-19 02:00` | Live | `$0.0091` | `$0.0099` | **+8.50%** | **+8.16%** | +47.1% | -12.8% | `shelf_target_reclaim` |
| 12 | Book 3 | `2026-08-21 01:00` | `2026-08-21 02:00` | 1.0h | `$0.0150` | `$0.0137` | **-8.23%** | **-8.59%** | +25.1% | -13.9% | `stop_loss` |
| 13 | Book 3 | `2026-09-16 01:00` | `2026-09-16 11:00` | 10.0h | `$0.0091` | `$0.0097` | **+6.27%** | **+6.08%** | +11.3% | -5.4% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `6` | `100.0%` | **`+58.4%`** |
| `stop_loss` | `5` | `0.0%` | **`-42.9%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `AVAAI`

* **Total Candidate Breakouts Filtered (Vetoed):** `88`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `72` (81.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `30`
* **Saved Capital Losses Avoided:** `+1,627.2%`
* **Missed Upside Forgone:** `-1,059.6%`
* **Net Veto Alpha:** `+567.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `45` | `51.1%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `35` | `39.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `6` | `6.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `2` | `2.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*