# Kronos V12: Institutional Symbol Tear Sheet — `RAYSOL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.529`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-7.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.93x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.42%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-15.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`220.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+18.7% / -19.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-01-18 05:00` | `2025-01-22 05:00` | Live | `$5.9020` | `$6.4037` | **+8.50%** | **+8.16%** | +35.4% | -36.1% | `shelf_target_reclaim` |
| 2 | Book 4 | `2025-07-20 16:00` | `2025-08-01 00:00` | 272.0h | `$3.0231` | `$2.6971` | **-13.06%** | **-13.83%** | +17.1% | -11.9% | `structural_stop` |
| 3 | Book 4 | `2026-08-25 00:00` | `2026-09-01 00:00` | 168.0h | `$0.8239` | `$0.8017` | **-1.57%** | **-1.60%** | +3.6% | -9.2% | `stagnation_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-1.6%`** |
| `structural_stop` | `1` | `0.0%` | **`-13.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `RAYSOL`

* **Total Candidate Breakouts Filtered (Vetoed):** `263`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `216` (82.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `5`
* **Saved Capital Losses Avoided:** `+2,659.8%`
* **Missed Upside Forgone:** `-127.8%`
* **Net Veto Alpha:** `+2,532.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `235` | `89.4%` |
| `Core 1: Macro Bear Veto` | `27` | `10.3%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*