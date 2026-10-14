# Kronos V12: Institutional Symbol Tear Sheet — `MYX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+11.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.12x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+11.28%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`1.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+40.8% / -1.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-09-18 13:00` | `2026-09-18 14:00` | 1.0h | `$0.0817` | `$0.0914` | **+11.94%** | **+11.28%** | +40.8% | -1.4% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `1` | `100.0%` | **`+11.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `MYX`

* **Total Candidate Breakouts Filtered (Vetoed):** `73`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `52` (71.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `47`
* **Saved Capital Losses Avoided:** `+1,625.5%`
* **Missed Upside Forgone:** `-13,003.2%`
* **Net Veto Alpha:** `+-11,377.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `54` | `74.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `18` | `24.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `1.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*