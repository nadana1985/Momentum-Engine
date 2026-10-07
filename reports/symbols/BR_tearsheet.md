# Kronos V12: Institutional Symbol Tear Sheet — `BR`
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
| **Cumulative Net Log Return** | **`+30.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.35x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+30.08%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`16.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+45.0% / -9.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-13 15:00` | `2026-09-14 07:00` | 16.0h | `$0.2961` | `$0.4001` | **+35.10%** | **+30.08%** | +45.0% | -9.0% | `climax_top_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `climax_top_harvest` | `1` | `100.0%` | **`+30.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `BR`

* **Total Candidate Breakouts Filtered (Vetoed):** `56`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `44` (78.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `22`
* **Saved Capital Losses Avoided:** `+1,112.9%`
* **Missed Upside Forgone:** `-1,902.6%`
* **Net Veto Alpha:** `+-789.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `40` | `71.4%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `6` | `10.7%` |
| `Core 4: Defensible Whale Dump` | `5` | `8.9%` |
| `Core 4: Whale Firewall` | `5` | `8.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*