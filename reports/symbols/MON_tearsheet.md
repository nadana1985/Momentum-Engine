# Kronos V12: Institutional Symbol Tear Sheet — `MON`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.614`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+5.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.06x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.71%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`44.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.3% / -5.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-19 16:00` | `2026-09-20 03:00` | 11.0h | `$0.0258` | `$0.0237` | **-8.44%** | **-8.81%** | +0.0% | -8.1% | `initial_stop` |
| 2 | Book 1 | `2026-09-25 07:00` | `2026-09-28 12:00` | 77.0h | `$0.0259` | `$0.0297` | **+15.34%** | **+14.23%** | +16.6% | -2.7% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-8.8%`** |
| `target_reclaim` | `1` | `100.0%` | **`+14.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `MON`

* **Total Candidate Breakouts Filtered (Vetoed):** `31`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `20` (64.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `7`
* **Saved Capital Losses Avoided:** `+212.2%`
* **Missed Upside Forgone:** `-167.9%`
* **Net Veto Alpha:** `+44.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `31` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*