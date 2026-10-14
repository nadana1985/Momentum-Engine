# Kronos V12: Institutional Symbol Tear Sheet — `FHE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.419`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+4.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.04x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.01%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`34.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.5% / -3.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-19 10:00` | `2025-05-19 16:00` | 6.0h | `$0.0893` | `$0.0983` | **+10.07%** | **+9.60%** | +11.5% | -0.0% | `target_reclaim` |
| 2 | Book 3 | `2025-05-23 20:00` | `2025-05-26 20:00` | 72.0h | `$0.0993` | `$0.0983` | **-1.04%** | **-1.05%** | +8.7% | -3.3% | `time_expiry` |
| 3 | Book 3 | `2025-07-07 09:00` | `2025-07-09 08:00` | 47.0h | `$0.0721` | `$0.0751` | **+4.17%** | **+4.08%** | +11.6% | -2.5% | `target_reclaim` |
| 4 | Book 3 | `2025-08-04 19:00` | `2025-08-05 06:00` | 11.0h | `$0.0771` | `$0.0708` | **-8.23%** | **-8.59%** | +14.1% | -9.6% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+13.7%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_expiry` | `1` | `0.0%` | **`-1.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `FHE`

* **Total Candidate Breakouts Filtered (Vetoed):** `75`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `57` (76.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `44`
* **Saved Capital Losses Avoided:** `+1,602.6%`
* **Missed Upside Forgone:** `-3,567.3%`
* **Net Veto Alpha:** `+-1,964.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `62` | `82.7%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `7` | `9.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `6` | `8.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*