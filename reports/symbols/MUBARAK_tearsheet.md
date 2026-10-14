# Kronos V12: Institutional Symbol Tear Sheet — `MUBARAK`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+6.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.07x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+6.52%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`15.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+26.6% / -1.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2026-08-08 14:00` | `2026-08-09 05:00` | 15.0h | `$0.0150` | `$0.0180` | **+6.70%** | **+6.52%** | +26.6% | -1.1% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `1` | `100.0%` | **`+6.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `MUBARAK`

* **Total Candidate Breakouts Filtered (Vetoed):** `316`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `151` (47.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `142`
* **Saved Capital Losses Avoided:** `+2,700.1%`
* **Missed Upside Forgone:** `-7,377.7%`
* **Net Veto Alpha:** `+-4,677.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `297` | `94.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `12` | `3.8%` |
| `Core 4: Funding Rate Cap` | `5` | `1.6%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.3%` |
| `Core 4: Whale Firewall` | `1` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*