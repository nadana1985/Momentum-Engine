# Kronos V12: Institutional Symbol Tear Sheet — `POL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+4.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.05x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.35%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`72.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.3% / -6.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-11-13 04:00` | `2024-11-16 04:00` | 72.0h | `$0.3773` | `$0.3785` | **+0.31%** | **+0.31%** | +6.8% | -7.4% | `time_expiry` |
| 2 | Book 3 | `2025-07-23 20:00` | `2025-07-26 20:00` | 72.0h | `$0.2268` | `$0.2370` | **+4.48%** | **+4.38%** | +5.9% | -4.6% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_expiry` | `2` | `100.0%` | **`+4.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `POL`

* **Total Candidate Breakouts Filtered (Vetoed):** `110`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `45` (40.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `12`
* **Saved Capital Losses Avoided:** `+492.4%`
* **Missed Upside Forgone:** `-343.2%`
* **Net Veto Alpha:** `+149.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `62` | `56.4%` |
| `Core 1: Macro Bear Veto` | `48` | `43.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*