# Kronos V12: Institutional Symbol Tear Sheet — `ALLO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`14.342`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+27.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.31x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+13.67%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`72.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+19.9% / -4.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-03 18:00` | `2026-09-05 18:00` | 48.0h | `$0.2504` | `$0.2454` | **-2.03%** | **-2.05%** | +2.1% | -5.3% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-18 23:00` | `2026-09-23 00:00` | 97.0h | `$0.2245` | `$0.3012` | **+34.16%** | **+29.39%** | +37.7% | -2.7% | `climax_top_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `climax_top_harvest` | `1` | `100.0%` | **`+29.4%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-2.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `ALLO`

* **Total Candidate Breakouts Filtered (Vetoed):** `32`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `20` (62.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `16`
* **Saved Capital Losses Avoided:** `+369.6%`
* **Missed Upside Forgone:** `-1,302.4%`
* **Net Veto Alpha:** `+-932.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `32` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*