# Kronos V12: Institutional Symbol Tear Sheet — `ESPORTS`
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
| **Cumulative Net Log Return** | **`+16.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.18x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+8.16%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`nanh`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+35.6% / -28.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-07-30 21:00` | `2025-08-03 21:00` | Live | `$0.1236` | `$0.1342` | **+8.50%** | **+8.16%** | +33.0% | -42.9% | `shelf_target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2025-11-12 16:00` | `2025-11-16 16:00` | Live | `$0.3458` | `$0.3752` | **+8.50%** | **+8.16%** | +38.2% | -13.4% | `shelf_target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `ESPORTS`

* **Total Candidate Breakouts Filtered (Vetoed):** `259`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `141` (54.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `60`
* **Saved Capital Losses Avoided:** `+2,765.6%`
* **Missed Upside Forgone:** `-1,381.6%`
* **Net Veto Alpha:** `+1,384.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `158` | `61.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `101` | `39.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*