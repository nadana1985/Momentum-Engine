# Kronos V12: Institutional Symbol Tear Sheet — `1000CAT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `8` (`8` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `8` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`37.5%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`1.471`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+16.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.18x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.05%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`45.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.3% / -7.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-04-26 11:00` | `2025-04-27 16:00` | 29.0h | `$0.0075` | `$0.0069` | **-8.23%** | **-8.59%** | +3.5% | -8.4% | `stop_loss` |
| 2 | Book 3 | `2025-06-30 14:00` | `2025-07-02 16:00` | 50.0h | `$0.0076` | `$0.0080` | **+5.70%** | **+5.54%** | +6.9% | -5.9% | `target_reclaim` |
| 3 | Book 3 | `2025-07-29 14:00` | `2025-07-31 23:00` | 57.0h | `$0.0106` | `$0.0097` | **-8.23%** | **-8.59%** | +13.4% | -9.2% | `stop_loss` |
| 4 | Book 3 | `2025-09-22 06:00` | `2025-09-23 02:00` | 20.0h | `$0.0076` | `$0.0070` | **-8.23%** | **-8.59%** | +1.3% | -8.6% | `stop_loss` |
| 5 | Book 3 | `2025-10-04 11:00` | `2025-10-07 11:00` | 72.0h | `$0.0081` | `$0.0092` | **+13.57%** | **+12.73%** | +21.5% | -6.4% | `target_reclaim` |
| 6 | Book 3 | `2025-10-09 10:00` | `2025-10-10 19:00` | 33.0h | `$0.0081` | `$0.0075` | **-8.23%** | **-8.59%** | +6.0% | -9.6% | `stop_loss` |
| 7 | Book 2 | `2026-09-04 10:00` | `2026-09-05 17:00` | 31.0h | `$0.0020` | `$0.0027` | **+38.86%** | **+33.01%** | +49.5% | -4.6% | `climax_top_harvest` |
| 8 | Book 3 | `2026-09-28 05:00` | `2026-10-01 05:00` | 72.0h | `$0.0023` | `$0.0023` | **-0.50%** | **-0.50%** | +4.3% | -6.3% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `target_reclaim` | `2` | `100.0%` | **`+18.3%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+33.0%`** |
| `time_expiry` | `1` | `0.0%` | **`-0.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `1000CAT`

* **Total Candidate Breakouts Filtered (Vetoed):** `54`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `39` (72.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `14`
* **Saved Capital Losses Avoided:** `+618.6%`
* **Missed Upside Forgone:** `-496.3%`
* **Net Veto Alpha:** `+122.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `32` | `59.3%` |
| `Core 1: Macro Bear Veto` | `19` | `35.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `5.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*