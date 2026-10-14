# Kronos V12: Institutional Symbol Tear Sheet — `DIA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.691`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+17.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.19x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.53%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-10.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`50.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+26.4% / -8.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2024-10-04 18:00` | `2024-10-08 18:00` | Live | `$0.7228` | `$0.7843` | **+8.50%** | **+8.16%** | +70.5% | -14.7% | `shelf_target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2025-07-20 20:00` | `2025-07-24 20:00` | Live | `$0.7532` | `$0.8172` | **+8.50%** | **+8.16%** | +40.4% | -11.0% | `shelf_target_reclaim` |
| 3 | Book 3 | `2025-10-29 22:00` | `2025-10-31 17:00` | 43.0h | `$0.5432` | `$0.4985` | **-8.23%** | **-8.59%** | +2.6% | -8.3% | `stop_loss` |
| 4 | Book 3 | `2026-09-05 14:00` | `2026-09-08 14:00` | 72.0h | `$0.1419` | `$0.1393` | **-1.84%** | **-1.86%** | +2.8% | -3.3% | `time_expiry` |
| 5 | Book 3 | `2026-10-07 02:00` | `2026-10-08 13:00` | 35.0h | `$0.1609` | `$0.1810` | **+12.51%** | **+11.79%** | +15.4% | -2.5% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+11.8%`** |
| `time_expiry` | `1` | `0.0%` | **`-1.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `DIA`

* **Total Candidate Breakouts Filtered (Vetoed):** `355`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `292` (82.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `83`
* **Saved Capital Losses Avoided:** `+4,431.4%`
* **Missed Upside Forgone:** `-5,266.6%`
* **Net Veto Alpha:** `+-835.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `286` | `80.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `37` | `10.4%` |
| `Core 1: Macro Bear Veto` | `23` | `6.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `8` | `2.3%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*