# Kronos V12: Institutional Symbol Tear Sheet — `EVAA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.907`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+7.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.08x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.59%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`nanh`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+90.6% / -36.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-10-20 17:00` | `2025-10-24 17:00` | Live | `$3.7032` | `$4.0180` | **+8.50%** | **+8.16%** | +242.0% | -47.0% | `shelf_target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2026-06-14 19:00` | `2026-06-18 19:00` | Live | `$0.6291` | `$0.6826` | **+8.50%** | **+8.16%** | +44.5% | -13.7% | `shelf_target_reclaim` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2026-07-07 09:00` | `2026-07-11 09:00` | Live | `$1.3474` | `$1.2369` | **-8.20%** | **-8.56%** | +-14.6% | -48.4% | `shelf_stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `EVAA`

* **Total Candidate Breakouts Filtered (Vetoed):** `60`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `47` (78.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `32`
* **Saved Capital Losses Avoided:** `+1,350.6%`
* **Missed Upside Forgone:** `-2,357.0%`
* **Net Veto Alpha:** `+-1,006.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `55` | `91.7%` |
| `Core 4: Funding Rate Cap` | `5` | `8.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*