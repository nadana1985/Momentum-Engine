# Kronos V12: Institutional Symbol Tear Sheet — `REZ`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.359`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+8.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.08x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.33%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-13.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`24.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.9% / -9.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-06-02 20:00` | `2024-06-04 13:00` | 41.0h | `$0.1558` | `$0.1771` | **+13.64%** | **+12.78%** | +17.1% | -1.8% | `target_reclaim` |
| 2 | Book 3 | `2024-11-12 10:00` | `2024-11-12 16:00` | 6.0h | `$0.0415` | `$0.0381` | **-8.23%** | **-8.59%** | +1.3% | -8.6% | `stop_loss` |
| 3 | Book 3 | `2025-05-12 18:00` | `2025-05-13 17:00` | 23.0h | `$0.0149` | `$0.0169` | **+13.64%** | **+12.78%** | +15.8% | -2.5% | `target_reclaim` |
| 4 | Book 3 | `2025-08-10 17:00` | `2025-08-13 17:00` | 72.0h | `$0.0146` | `$0.0153` | **+4.79%** | **+4.67%** | +11.2% | -6.7% | `time_expiry` |
| 5 | Book 3 | `2025-10-10 15:00` | `2025-10-10 20:00` | 5.0h | `$0.0146` | `$0.0134` | **-8.23%** | **-8.59%** | +5.0% | -13.6% | `stop_loss` |
| 6 | Book 2 | `2026-09-13 15:00` | `2026-09-13 16:00` | 1.0h | `$0.0048` | `$0.0044` | **-4.95%** | **-5.07%** | +3.1% | -21.5% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `2` | `100.0%` | **`+25.6%`** |
| `initial_stop` | `1` | `0.0%` | **`-5.1%`** |
| `time_expiry` | `1` | `100.0%` | **`+4.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `REZ`

* **Total Candidate Breakouts Filtered (Vetoed):** `70`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `42` (60.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `15`
* **Saved Capital Losses Avoided:** `+687.6%`
* **Missed Upside Forgone:** `-702.0%`
* **Net Veto Alpha:** `+-14.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `37` | `52.9%` |
| `Core 1: Macro Bear Veto` | `32` | `45.7%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `1.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*