# Kronos V12: Institutional Symbol Tear Sheet — `VIRTUAL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.806`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-2.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.97x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.33%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-13.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`291.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+19.8% / -7.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2025-04-30 22:00` | `2025-05-01 01:00` | 3.0h | `$1.3969` | `$1.6763` | **+11.58%** | **+11.05%** | +20.6% | -0.2% | `target_reclaim` |
| 2 | Book 4 | `2026-08-22 05:00` | `2026-09-15 08:00` | 579.0h | `$0.7041` | `$0.5984` | **-12.66%** | **-13.72%** | +19.0% | -15.1% | `structural_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `structural_stop` | `1` | `0.0%` | **`-13.7%`** |
| `target_reclaim` | `1` | `100.0%` | **`+11.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `VIRTUAL`

* **Total Candidate Breakouts Filtered (Vetoed):** `124`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `83` (66.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `64`
* **Saved Capital Losses Avoided:** `+1,168.1%`
* **Missed Upside Forgone:** `-2,131.4%`
* **Net Veto Alpha:** `+-963.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `124` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*