# Kronos V12: Institutional Symbol Tear Sheet — `ACE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.615`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+5.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.05x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.64%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`57.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+23.0% / -7.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-07 15:00` | `2026-09-08 21:00` | 30.0h | `$0.1821` | `$0.1671` | **-8.23%** | **-8.59%** | +10.5% | -8.5% | `initial_stop` |
| 2 | Book 2 | `2026-09-20 01:00` | `2026-09-23 14:00` | 85.0h | `$0.1609` | `$0.1848` | **+14.88%** | **+13.87%** | +35.5% | -5.8% | `trail_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |
| `trail_stop` | `1` | `100.0%` | **`+13.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `ACE`

* **Total Candidate Breakouts Filtered (Vetoed):** `57`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `47` (82.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `16`
* **Saved Capital Losses Avoided:** `+1,053.1%`
* **Missed Upside Forgone:** `-694.9%`
* **Net Veto Alpha:** `+358.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `35` | `61.4%` |
| `Core 1: Macro Bear Veto` | `21` | `36.8%` |
| `Core 4: Funding Rate Cap` | `1` | `1.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*