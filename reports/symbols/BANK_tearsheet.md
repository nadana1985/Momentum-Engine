# Kronos V12: Institutional Symbol Tear Sheet — `BANK`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.411`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-11.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.89x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.90%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-19.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`37.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+57.8% / -13.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-10-08 02:00` | `2025-10-12 02:00` | Live | `$0.0842` | `$0.0914` | **+8.50%** | **+8.16%** | +157.6% | -14.4% | `shelf_target_reclaim` |
| 2 | Book 4 | `2026-06-11 04:00` | `2026-06-12 20:00` | 40.0h | `$0.0453` | `$0.0385` | **-8.93%** | **-9.29%** | +6.9% | -17.7% | `structural_stop` |
| 3 | Book 2 | `2026-09-14 08:00` | `2026-09-15 18:00` | 34.0h | `$0.0292` | `$0.0268` | **-10.13%** | **-10.57%** | +8.9% | -9.6% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-10.6%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `structural_stop` | `1` | `0.0%` | **`-9.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `BANK`

* **Total Candidate Breakouts Filtered (Vetoed):** `107`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `89` (83.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `26`
* **Saved Capital Losses Avoided:** `+2,352.4%`
* **Missed Upside Forgone:** `-2,735.1%`
* **Net Veto Alpha:** `+-382.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `86` | `80.4%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `21` | `19.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*