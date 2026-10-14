# Kronos V12: Institutional Symbol Tear Sheet — `SUI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `10` (`10` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `10` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`70.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.584`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+68.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.99x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+6.87%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-28.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`110.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.8% / -6.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2023-08-20 11:00` | `2023-08-24 11:00` | Live | `$0.5173` | `$0.5613` | **+8.50%** | **+8.16%** | +5.2% | -17.1% | `shelf_target_reclaim` |
| 2 | Book 3 | `2023-10-30 17:00` | `2023-10-31 00:00` | 7.0h | `$0.4438` | `$0.4745` | **+6.91%** | **+6.68%** | +7.5% | -0.4% | `target_reclaim` |
| 3 | Book 3 | `2023-12-11 02:00` | `2023-12-14 02:00` | 72.0h | `$0.6285` | `$0.6465` | **+2.85%** | **+2.81%** | +12.0% | -5.3% | `time_expiry` |
| 4 | Book 2 | `2024-05-20 15:00` | `2024-05-23 20:00` | 77.0h | `$1.1188` | `$1.0267` | **-8.61%** | **-8.99%** | +4.7% | -10.7% | `initial_stop` |
| 5 | Book 4 | `2024-08-23 16:00` | `2024-08-27 22:00` | 102.0h | `$1.0061` | `$0.8552` | **-18.12%** | **-19.64%** | +5.0% | -17.5% | `structural_stop` |
| 6 | Book 3 | `2024-11-15 01:00` | `2024-11-15 20:00` | 19.0h | `$3.2168` | `$3.4965` | **+8.70%** | **+8.34%** | +8.9% | -3.6% | `target_reclaim` |
| 7 | Book 4 | `2025-04-23 02:00` | `2025-04-24 15:00` | 37.0h | `$2.7723` | `$3.3267` | **+36.13%** | **+31.59%** | +20.7% | -1.8% | `target_reclaim` |
| 8 | Book 1 | `2025-07-10 04:00` | `2025-07-31 04:00` | 504.0h | `$3.1621` | `$3.8410` | **+40.32%** | **+34.95%** | +40.7% | -2.2% | `time_cap` |
| 9 | Book 1 | `2025-09-18 09:00` | `2025-09-21 09:00` | 72.0h | `$3.9024` | `$3.6176` | **-13.94%** | **-14.76%** | +1.8% | -8.1% | `stagnation_bailout` |
| 10 | Book 4 | `2026-09-21 03:00` | `2026-09-25 11:00` | 104.0h | `$0.9507` | `$1.1409` | **+21.30%** | **+19.61%** | +21.2% | -2.5% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+66.2%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `initial_stop` | `1` | `0.0%` | **`-9.0%`** |
| `stagnation_bailout` | `1` | `0.0%` | **`-14.8%`** |
| `structural_stop` | `1` | `0.0%` | **`-19.6%`** |
| `time_cap` | `1` | `100.0%` | **`+35.0%`** |
| `time_expiry` | `1` | `100.0%` | **`+2.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `SUI`

* **Total Candidate Breakouts Filtered (Vetoed):** `83`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `43` (51.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `12`
* **Saved Capital Losses Avoided:** `+406.2%`
* **Missed Upside Forgone:** `-355.1%`
* **Net Veto Alpha:** `+51.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `43` | `51.8%` |
| `Core 4: Defensible Whale Dump` | `22` | `26.5%` |
| `Core 4: Funding Rate Cap` | `11` | `13.3%` |
| `Core 4: Whale Firewall` | `4` | `4.8%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `3` | `3.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*