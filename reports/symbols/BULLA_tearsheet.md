# Kronos V12: Institutional Symbol Tear Sheet — `BULLA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`20.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.521`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-11.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.89x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.35%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-24.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`17.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.7% / -10.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-08-08 22:00` | `2025-08-09 01:00` | 3.0h | `$0.0797` | `$0.0905` | **+13.64%** | **+12.78%** | +15.5% | -1.0% | `target_reclaim` |
| 2 | Book 3 | `2025-08-10 01:00` | `2025-08-13 01:00` | 72.0h | `$0.0818` | `$0.0814` | **-0.58%** | **-0.58%** | +17.2% | -4.4% | `time_expiry` |
| 3 | Book 3 | `2025-09-20 18:00` | `2025-09-21 03:00` | 9.0h | `$0.0747` | `$0.0686` | **-8.23%** | **-8.59%** | +15.8% | -9.5% | `stop_loss` |
| 4 | Book 2 | `2026-09-03 16:00` | `2026-09-03 17:00` | 1.0h | `$0.0411` | `$0.0377` | **-6.54%** | **-6.76%** | +8.3% | -19.0% | `initial_stop` |
| 5 | Book 3 | `2026-09-05 10:00` | `2026-09-05 11:00` | 1.0h | `$0.0659` | `$0.0605` | **-8.23%** | **-8.59%** | +6.6% | -18.7% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `initial_stop` | `1` | `0.0%` | **`-6.8%`** |
| `target_reclaim` | `1` | `100.0%` | **`+12.8%`** |
| `time_expiry` | `1` | `0.0%` | **`-0.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `BULLA`

* **Total Candidate Breakouts Filtered (Vetoed):** `58`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `49` (84.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `37`
* **Saved Capital Losses Avoided:** `+1,860.1%`
* **Missed Upside Forgone:** `-4,687.7%`
* **Net Veto Alpha:** `+-2,827.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `51` | `87.9%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `5` | `8.6%` |
| `Core 4: Defensible Whale Dump` | `2` | `3.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*