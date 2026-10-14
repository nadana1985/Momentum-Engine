# Kronos V12: Institutional Symbol Tear Sheet — `RIF`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `17` (`17` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `17` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`64.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.424`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+22.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.25x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.32%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-33.7%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`40.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.3% / -9.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2024-01-08 22:00` | `2024-01-12 22:00` | Live | `$0.1421` | `$0.1542` | **+8.50%** | **+8.16%** | +17.1% | -23.5% | `shelf_target_reclaim` |
| 2 | Book 3 | `2024-01-10 01:00` | `2024-01-10 03:00` | 2.0h | `$0.1619` | `$0.1725` | **+6.52%** | **+6.31%** | +16.8% | -1.1% | `target_reclaim` |
| 3 | Book 3 | `2024-01-10 06:00` | `2024-01-10 07:00` | 1.0h | `$0.1612` | `$0.1826` | **+13.28%** | **+12.47%** | +22.6% | -3.8% | `target_reclaim` |
| 4 | Book 3 | `2024-03-05 19:00` | `2024-03-05 20:00` | 1.0h | `$0.2271` | `$0.2063` | **-9.16%** | **-9.61%** | +3.6% | -21.2% | `stop_loss` |
| 5 | Book 3 | `2024-04-02 00:00` | `2024-04-02 02:00` | 2.0h | `$0.2941` | `$0.2699` | **-8.23%** | **-8.59%** | +5.5% | -13.7% | `stop_loss` |
| 6 | Book 5 (Shelf Absorption Squeeze) | `2024-07-28 01:00` | `2024-08-01 01:00` | Live | `$0.0933` | `$0.1012` | **+8.50%** | **+8.16%** | +29.1% | -44.7% | `shelf_target_reclaim` |
| 7 | Book 3 | `2024-07-28 16:00` | `2024-07-29 01:00` | 9.0h | `$0.0920` | `$0.0959` | **+4.17%** | **+4.08%** | +6.9% | -3.6% | `target_reclaim` |
| 8 | Book 2 | `2024-08-11 09:00` | `2024-08-11 14:00` | 5.0h | `$0.0816` | `$0.0748` | **-10.13%** | **-10.57%** | +2.7% | -8.7% | `initial_stop` |
| 9 | Book 3 | `2024-08-14 13:00` | `2024-08-15 18:00` | 29.0h | `$0.0787` | `$0.0723` | **-8.23%** | **-8.59%** | +2.4% | -11.5% | `stop_loss` |
| 10 | Book 3 | `2024-09-30 00:00` | `2024-09-30 23:00` | 23.0h | `$0.1010` | `$0.0927` | **-8.23%** | **-8.59%** | +1.7% | -9.1% | `stop_loss` |
| 11 | Book 3 | `2024-11-24 12:00` | `2024-11-24 17:00` | 5.0h | `$0.1139` | `$0.1216` | **+6.83%** | **+6.60%** | +6.8% | -0.1% | `target_reclaim` |
| 12 | Book 3 | `2024-12-02 08:00` | `2024-12-03 02:00` | 18.0h | `$0.1292` | `$0.1404` | **+8.70%** | **+8.34%** | +9.5% | -2.8% | `target_reclaim` |
| 13 | Book 3 | `2024-12-03 13:00` | `2024-12-03 16:00` | 3.0h | `$0.1370` | `$0.1444` | **+5.43%** | **+5.29%** | +7.1% | -2.8% | `target_reclaim` |
| 14 | Book 3 | `2025-05-15 23:00` | `2025-05-18 23:00` | 72.0h | `$0.0568` | `$0.0574` | **+1.01%** | **+1.01%** | +4.9% | -6.2% | `time_expiry` |
| 15 | Book 4 | `2025-07-15 22:00` | `2025-07-30 19:00` | 357.0h | `$0.0617` | `$0.0583` | **-6.79%** | **-6.99%** | +6.9% | -7.3% | `structural_stop` |
| 16 | Book 4 | `2026-04-14 08:00` | `2026-04-15 04:00` | 20.0h | `$0.0403` | `$0.0483` | **+7.56%** | **+7.33%** | +20.9% | -1.9% | `target_reclaim` |
| 17 | Book 3 | `2026-09-16 11:00` | `2026-09-18 17:00` | 54.0h | `$0.0785` | `$0.0847` | **+7.91%** | **+7.61%** | +9.9% | -2.1% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `8` | `100.0%` | **`+58.0%`** |
| `stop_loss` | `4` | `0.0%` | **`-35.4%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `initial_stop` | `1` | `0.0%` | **`-10.6%`** |
| `structural_stop` | `1` | `0.0%` | **`-7.0%`** |
| `time_expiry` | `1` | `100.0%` | **`+1.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `RIF`

* **Total Candidate Breakouts Filtered (Vetoed):** `1318`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `674` (51.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `82`
* **Saved Capital Losses Avoided:** `+6,403.3%`
* **Missed Upside Forgone:** `-2,280.4%`
* **Net Veto Alpha:** `+4,122.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `724` | `54.9%` |
| `Core 1: Macro Bear Veto` | `553` | `42.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `31` | `2.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `8` | `0.6%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.1%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*