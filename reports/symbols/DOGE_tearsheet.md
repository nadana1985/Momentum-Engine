# Kronos V12: Institutional Symbol Tear Sheet — `DOGE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `8` (`8` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `8` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.184`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+6.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.07x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.82%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`263.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.6% / -10.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2023-04-03 17:00` | `2023-04-21 19:00` | 434.0h | `$0.0940` | `$0.0799` | **-7.55%** | **-8.18%** | +11.9% | -17.0% | `structural_stop` |
| 2 | Book 4 | `2023-07-24 07:00` | `2023-08-16 20:00` | 565.0h | `$0.0768` | `$0.0667` | **-6.63%** | **-7.12%** | +9.2% | -13.9% | `structural_stop` |
| 3 | Book 4 | `2023-10-25 21:00` | `2023-11-16 10:00` | 517.0h | `$0.0688` | `$0.0826` | **+19.51%** | **+18.08%** | +21.1% | -6.8% | `target_reclaim` |
| 4 | Book 3 | `2024-03-03 07:00` | `2024-03-03 11:00` | 4.0h | `$0.1286` | `$0.1398` | **+8.70%** | **+8.34%** | +11.2% | -6.8% | `target_reclaim` |
| 5 | Book 3 | `2024-03-05 19:00` | `2024-03-05 20:00` | 1.0h | `$0.1451` | `$0.1332` | **-8.23%** | **-8.59%** | +10.0% | -17.1% | `stop_loss` |
| 6 | Book 3 | `2024-11-25 22:00` | `2024-11-28 22:00` | 72.0h | `$0.3898` | `$0.4032` | **+3.44%** | **+3.38%** | +10.1% | -6.4% | `time_expiry` |
| 7 | Book 4 | `2025-05-10 06:00` | `2025-05-30 00:00` | 474.0h | `$0.2264` | `$0.2004` | **-11.36%** | **-12.07%** | +14.7% | -11.7% | `structural_stop` |
| 8 | Book 4 | `2025-07-16 14:00` | `2025-07-18 05:00` | 39.0h | `$0.2040` | `$0.2447` | **+13.47%** | **+12.76%** | +20.3% | -1.8% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `structural_stop` | `3` | `0.0%` | **`-27.4%`** |
| `target_reclaim` | `3` | `100.0%` | **`+39.2%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_expiry` | `1` | `100.0%` | **`+3.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `DOGE`

* **Total Candidate Breakouts Filtered (Vetoed):** `517`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `346` (66.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `123`
* **Saved Capital Losses Avoided:** `+4,191.1%`
* **Missed Upside Forgone:** `-8,072.7%`
* **Net Veto Alpha:** `+-3,881.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `298` | `57.6%` |
| `Core 0: Zero-Tolerance Data Firewall` | `188` | `36.4%` |
| `Core 4: Funding Rate Cap` | `31` | `6.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*