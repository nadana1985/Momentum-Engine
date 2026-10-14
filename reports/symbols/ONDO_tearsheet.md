# Kronos V12: Institutional Symbol Tear Sheet — `ONDO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `12` (`12` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `12` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`1.232`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+13.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.14x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.09%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-37.2%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`105.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.8% / -9.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2024-01-21 13:00` | `2024-01-25 13:00` | Live | `$0.2424` | `$0.2630` | **+8.50%** | **+8.16%** | +11.8% | -25.2% | `shelf_target_reclaim` |
| 2 | Book 3 | `2024-02-22 23:00` | `2024-02-23 15:00` | 16.0h | `$0.4278` | `$0.3926` | **-8.23%** | **-8.59%** | +5.8% | -9.4% | `stop_loss` |
| 3 | Book 3 | `2024-02-27 17:00` | `2024-02-28 17:00` | 24.0h | `$0.4324` | `$0.3968` | **-8.23%** | **-8.59%** | +3.5% | -20.2% | `stop_loss` |
| 4 | Book 3 | `2024-03-21 18:00` | `2024-03-22 12:00` | 18.0h | `$0.7429` | `$0.6818` | **-8.23%** | **-8.59%** | +5.2% | -8.5% | `stop_loss` |
| 5 | Book 3 | `2024-04-01 03:00` | `2024-04-01 05:00` | 2.0h | `$0.9272` | `$0.8509` | **-8.23%** | **-8.59%** | +1.1% | -10.7% | `stop_loss` |
| 6 | Book 3 | `2024-05-19 14:00` | `2024-05-22 14:00` | 72.0h | `$0.8967` | `$0.9236` | **+3.00%** | **+2.95%** | +9.6% | -2.2% | `time_expiry` |
| 7 | Book 2 | `2024-10-29 04:00` | `2024-11-01 04:00` | 72.0h | `$0.7332` | `$0.6929` | **-5.61%** | **-5.77%** | +2.5% | -7.6% | `stagnation_cut` |
| 8 | Book 2 | `2024-11-06 01:00` | `2024-11-13 01:00` | 168.0h | `$0.6620` | `$0.8636` | **+32.67%** | **+28.52%** | +45.6% | -1.6% | `time_cap` |
| 9 | Book 3 | `2024-12-05 00:00` | `2024-12-08 00:00` | 72.0h | `$1.7178` | `$1.6753` | **-2.48%** | **-2.51%** | +7.1% | -6.1% | `time_expiry` |
| 10 | Book 1 | `2025-07-10 16:00` | `2025-07-17 12:00` | 164.0h | `$0.8630` | `$1.0267` | **+34.13%** | **+30.03%** | +21.7% | -2.5% | `target_reclaim` |
| 11 | Book 4 | `2026-07-21 06:00` | `2026-08-11 00:00` | 498.0h | `$0.3799` | `$0.3367` | **-4.03%** | **-4.15%** | +12.6% | -11.4% | `structural_stop` |
| 12 | Book 1 | `2026-09-21 10:00` | `2026-09-23 15:00` | 53.0h | `$0.4507` | `$0.4098` | **-9.38%** | **-9.78%** | +3.0% | -11.0% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `time_expiry` | `2` | `50.0%` | **`+0.4%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-9.8%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-5.8%`** |
| `structural_stop` | `1` | `0.0%` | **`-4.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+30.0%`** |
| `time_cap` | `1` | `100.0%` | **`+28.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `ONDO`

* **Total Candidate Breakouts Filtered (Vetoed):** `383`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `267` (69.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `9`
* **Saved Capital Losses Avoided:** `+2,121.4%`
* **Missed Upside Forgone:** `-292.1%`
* **Net Veto Alpha:** `+1,829.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `360` | `94.0%` |
| `Core 4: Funding Rate Cap` | `22` | `5.7%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*