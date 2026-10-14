# Kronos V12: Institutional Symbol Tear Sheet — `SPK`
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
| **Cumulative Net Log Return** | **`+22.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.26x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+11.47%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`7.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+31.0% / -0.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2025-07-21 22:00` | `2025-07-21 23:00` | 1.0h | `$0.0513` | `$0.0616` | **+11.58%** | **+11.05%** | +39.8% | -0.6% | `target_reclaim` |
| 2 | Book 4 | `2026-04-22 00:00` | `2026-04-22 13:00` | 13.0h | `$0.0288` | `$0.0345` | **+12.50%** | **+11.89%** | +22.2% | -0.1% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+22.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `SPK`

* **Total Candidate Breakouts Filtered (Vetoed):** `745`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `483` (64.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `220`
* **Saved Capital Losses Avoided:** `+7,274.7%`
* **Missed Upside Forgone:** `-13,756.0%`
* **Net Veto Alpha:** `+-6,481.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `387` | `51.9%` |
| `Core 1: Macro Bear Veto` | `260` | `34.9%` |
| `Core 4: Defensible Whale Dump` | `98` | `13.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*