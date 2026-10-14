# Kronos V12: Institutional Symbol Tear Sheet — `ALLO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`17.456`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+35.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.42x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+11.67%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-2.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`49.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+23.5% / -4.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2026-05-29 02:00` | `2026-05-29 05:00` | 3.0h | `$0.1869` | `$0.2243` | **+5.32%** | **+5.20%** | +30.8% | -4.0% | `target_reclaim` |
| 2 | Book 2 | `2026-09-03 18:00` | `2026-09-05 18:00` | 48.0h | `$0.2504` | `$0.2454` | **-2.11%** | **-2.13%** | +2.1% | -5.3% | `fast_decay_cut` |
| 3 | Book 2 | `2026-09-18 23:00` | `2026-09-23 00:00` | 97.0h | `$0.2245` | `$0.3012` | **+37.12%** | **+31.93%** | +37.7% | -2.7% | `climax_top_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `climax_top_harvest` | `1` | `100.0%` | **`+31.9%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-2.1%`** |
| `target_reclaim` | `1` | `100.0%` | **`+5.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `ALLO`

* **Total Candidate Breakouts Filtered (Vetoed):** `378`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `269` (71.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `249`
* **Saved Capital Losses Avoided:** `+5,945.5%`
* **Missed Upside Forgone:** `-18,306.4%`
* **Net Veto Alpha:** `+-12,360.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `378` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*