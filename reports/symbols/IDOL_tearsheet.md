# Kronos V12: Institutional Symbol Tear Sheet — `IDOL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+18.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.20x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+9.24%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`3.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+28.3% / -15.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-08-12 00:00` | `2025-08-12 03:00` | 3.0h | `$0.0146` | `$0.0162` | **+10.88%** | **+10.33%** | +15.1% | -7.1% | `target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2026-07-23 10:00` | `2026-07-27 10:00` | Live | `$0.0185` | `$0.0201` | **+8.50%** | **+8.16%** | +41.4% | -23.1% | `shelf_target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+10.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `IDOL`

* **Total Candidate Breakouts Filtered (Vetoed):** `150`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `134` (89.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `31`
* **Saved Capital Losses Avoided:** `+2,598.1%`
* **Missed Upside Forgone:** `-1,523.7%`
* **Net Veto Alpha:** `+1,074.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `147` | `98.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `3` | `2.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*