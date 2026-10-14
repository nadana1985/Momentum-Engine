# Kronos V12: Institutional Symbol Tear Sheet — `LSK`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+112.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`3.07x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+37.37%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`110.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+20.4% / -19.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2024-11-16 23:00` | `2024-11-25 04:00` | 197.0h | `$1.0186` | `$1.2224` | **+24.26%** | **+22.09%** | +20.6% | -7.9% | `target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2025-11-11 07:00` | `2025-11-15 07:00` | Live | `$0.2949` | `$0.3199` | **+8.50%** | **+8.16%** | +0.7% | -47.6% | `shelf_target_reclaim` |
| 3 | Book 4 | `2026-09-11 01:00` | `2026-09-12 00:00` | 23.0h | `$0.1203` | `$0.1444` | **+117.38%** | **+81.86%** | +39.9% | -2.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+104.0%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `LSK`

* **Total Candidate Breakouts Filtered (Vetoed):** `405`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `112` (27.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `35`
* **Saved Capital Losses Avoided:** `+1,065.2%`
* **Missed Upside Forgone:** `-1,273.9%`
* **Net Veto Alpha:** `+-208.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `374` | `92.3%` |
| `Core 1: Macro Bear Veto` | `31` | `7.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*