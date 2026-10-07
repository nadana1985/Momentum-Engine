# Kronos V12: Institutional Symbol Tear Sheet — `ENA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`6.458`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+46.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.60x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+23.44%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`129.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+29.8% / -6.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2024-05-18 09:00` | `2024-05-19 15:00` | 30.0h | `$0.7720` | `$0.7085` | **-8.23%** | **-8.59%** | +2.7% | -8.3% | `initial_stop` |
| 2 | Book 1 | `2025-07-10 16:00` | `2025-07-20 04:00` | 228.0h | `$0.3030` | `$0.4569` | **+74.13%** | **+55.47%** | +56.9% | -4.0% | `climax_top_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `climax_top_harvest` | `1` | `100.0%` | **`+55.5%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `ENA`

* **Total Candidate Breakouts Filtered (Vetoed):** `40`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `29` (72.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `9`
* **Saved Capital Losses Avoided:** `+368.3%`
* **Missed Upside Forgone:** `-225.1%`
* **Net Veto Alpha:** `+143.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `38` | `95.0%` |
| `Core 4: Funding Rate Cap` | `2` | `5.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*