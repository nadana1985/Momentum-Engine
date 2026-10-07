# Kronos V12: Institutional Symbol Tear Sheet — `BOME`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `8` (`8` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `8` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`37.5%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`1.189`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+6.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.06x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.76%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-20.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`31.9h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.4% / -6.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-05-16 14:00` | `2024-05-19 14:00` | 72.0h | `$0.0116` | `$0.0112` | **-3.37%** | **-3.43%** | +8.5% | -5.1% | `time_expiry` |
| 2 | Book 3 | `2024-05-23 20:00` | `2024-05-25 07:00` | 35.0h | `$0.0118` | `$0.0134` | **+13.64%** | **+12.78%** | +15.1% | -0.0% | `target_reclaim` |
| 3 | Book 3 | `2024-09-22 16:00` | `2024-09-25 01:00` | 57.0h | `$0.0064` | `$0.0073` | **+13.64%** | **+12.78%** | +14.2% | -2.8% | `target_reclaim` |
| 4 | Book 3 | `2024-11-12 10:00` | `2024-11-13 04:00` | 18.0h | `$0.0094` | `$0.0086` | **-8.23%** | **-8.59%** | +10.4% | -8.1% | `stop_loss` |
| 5 | Book 3 | `2024-11-14 23:00` | `2024-11-15 23:00` | 24.0h | `$0.0098` | `$0.0111` | **+13.64%** | **+12.78%** | +13.8% | -5.7% | `target_reclaim` |
| 6 | Book 3 | `2025-05-15 07:00` | `2025-05-15 21:00` | 14.0h | `$0.0026` | `$0.0024` | **-8.23%** | **-8.59%** | +7.9% | -8.7% | `stop_loss` |
| 7 | Book 3 | `2025-07-22 08:00` | `2025-07-23 17:00` | 33.0h | `$0.0022` | `$0.0021` | **-8.23%** | **-8.59%** | +5.4% | -8.3% | `stop_loss` |
| 8 | Book 2 | `2026-08-21 07:00` | `2026-08-21 09:00` | 2.0h | `$0.0015` | `$0.0013` | **-3.02%** | **-3.06%** | +8.0% | -15.9% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `target_reclaim` | `3` | `100.0%` | **`+38.4%`** |
| `initial_stop` | `1` | `0.0%` | **`-3.1%`** |
| `time_expiry` | `1` | `0.0%` | **`-3.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `BOME`

* **Total Candidate Breakouts Filtered (Vetoed):** `100`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `54` (54.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `31`
* **Saved Capital Losses Avoided:** `+804.7%`
* **Missed Upside Forgone:** `-1,039.3%`
* **Net Veto Alpha:** `+-234.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `51` | `51.0%` |
| `Core 1: Macro Bear Veto` | `49` | `49.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*