# Kronos V12: Institutional Symbol Tear Sheet — `SIREN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.097`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+1.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.02x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.41%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-11.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`37.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.2% / -7.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-13 09:00` | `2025-05-13 10:00` | 1.0h | `$0.1555` | `$0.1767` | **+13.64%** | **+12.78%** | +14.3% | -0.3% | `target_reclaim` |
| 2 | Book 3 | `2025-05-13 19:00` | `2025-05-14 09:00` | 14.0h | `$0.1663` | `$0.1526` | **-8.23%** | **-8.59%** | +5.8% | -18.8% | `stop_loss` |
| 3 | Book 3 | `2025-06-11 03:00` | `2025-06-14 03:00` | 72.0h | `$0.1381` | `$0.1467` | **+6.24%** | **+6.05%** | +12.4% | -2.5% | `time_expiry` |
| 4 | Book 3 | `2025-09-19 15:00` | `2025-09-22 06:00` | 63.0h | `$0.0960` | `$0.0881` | **-8.23%** | **-8.59%** | +4.3% | -10.0% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+12.8%`** |
| `time_expiry` | `1` | `100.0%` | **`+6.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `SIREN`

* **Total Candidate Breakouts Filtered (Vetoed):** `83`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `67` (80.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `39`
* **Saved Capital Losses Avoided:** `+1,756.3%`
* **Missed Upside Forgone:** `-3,423.3%`
* **Net Veto Alpha:** `+-1,667.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `50` | `60.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `33` | `39.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*