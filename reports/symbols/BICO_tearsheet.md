# Kronos V12: Institutional Symbol Tear Sheet — `BICO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+52.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.68x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+13.03%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`108.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+32.4% / -28.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2023-11-09 16:00` | `2023-11-15 05:00` | 133.0h | `$0.2564` | `$0.3077` | **+11.38%** | **+10.86%** | +21.0% | -4.4% | `target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2024-04-07 05:00` | `2024-04-11 05:00` | Live | `$0.7147` | `$0.7755` | **+8.50%** | **+8.16%** | +15.8% | -45.3% | `shelf_target_reclaim` |
| 3 | Book 4 | `2024-11-21 14:00` | `2024-11-25 01:00` | 83.0h | `$0.2933` | `$0.3520` | **+27.74%** | **+24.96%** | +27.1% | -8.6% | `target_reclaim` |
| 4 | Book 5 (Shelf Absorption Squeeze) | `2026-06-19 16:00` | `2026-06-23 16:00` | Live | `$0.0297` | `$0.0322` | **+8.50%** | **+8.16%** | +65.6% | -55.1% | `shelf_target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `target_reclaim` | `2` | `100.0%` | **`+35.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `BICO`

* **Total Candidate Breakouts Filtered (Vetoed):** `546`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `324` (59.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `204`
* **Saved Capital Losses Avoided:** `+7,495.9%`
* **Missed Upside Forgone:** `-11,544.5%`
* **Net Veto Alpha:** `+-4,048.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `317` | `58.1%` |
| `Core 1: Macro Bear Veto` | `229` | `41.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*