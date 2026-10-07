# Kronos V12: Institutional Symbol Tear Sheet — `TRUMP`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+40.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.50x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+20.14%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`121.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+32.7% / -3.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2025-05-08 04:00` | `2025-05-15 04:00` | 168.0h | `$12.0029` | `$13.1929` | **+9.91%** | **+9.45%** | +27.1% | -5.6% | `time_cap` |
| 2 | Book 2 | `2025-10-26 09:00` | `2025-10-29 11:00` | 74.0h | `$6.0942` | `$8.2952` | **+36.12%** | **+30.83%** | +38.3% | -1.4% | `climax_top_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `climax_top_harvest` | `1` | `100.0%` | **`+30.8%`** |
| `time_cap` | `1` | `100.0%` | **`+9.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `TRUMP`

* **Total Candidate Breakouts Filtered (Vetoed):** `19`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `16` (84.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `4`
* **Saved Capital Losses Avoided:** `+184.6%`
* **Missed Upside Forgone:** `-381.5%`
* **Net Veto Alpha:** `+-196.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `19` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*