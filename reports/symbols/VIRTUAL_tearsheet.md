# Kronos V12: Institutional Symbol Tear Sheet — `VIRTUAL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.603`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+17.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.19x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+5.70%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`83.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.2% / -9.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2025-05-02 13:00` | `2025-05-03 01:00` | 12.0h | `$1.8609` | `$1.7078` | **-4.63%** | **-4.75%** | +1.4% | -8.2% | `initial_stop` |
| 2 | Book 2 | `2025-07-10 22:00` | `2025-07-17 22:00` | 168.0h | `$1.7913` | `$1.8109` | **+1.41%** | **+1.40%** | +7.4% | -12.6% | `time_cap` |
| 3 | Book 2 | `2025-10-25 12:00` | `2025-10-28 11:00` | 71.0h | `$1.2306` | `$1.5730` | **+22.68%** | **+20.44%** | +36.8% | -7.1% | `climax_top_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `climax_top_harvest` | `1` | `100.0%` | **`+20.4%`** |
| `initial_stop` | `1` | `0.0%` | **`-4.7%`** |
| `time_cap` | `1` | `100.0%` | **`+1.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `VIRTUAL`

* **Total Candidate Breakouts Filtered (Vetoed):** `60`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `42` (70.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `11`
* **Saved Capital Losses Avoided:** `+508.5%`
* **Missed Upside Forgone:** `-375.0%`
* **Net Veto Alpha:** `+133.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `60` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*