# Kronos V12: Institutional Symbol Tear Sheet — `CRDO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+21.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.24x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+10.80%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.0% / -2.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-16 23:00` | `2026-09-23 23:00` | 168.0h | `$166.6656` | `$192.8766` | **+18.00%** | **+16.72%** | +17.6% | -1.8% | `time_cap` |
| 2 | Book 2 | `2026-10-01 15:00` | `2026-10-08 15:00` | 168.0h | `$205.7631` | `$215.8091` | **+5.01%** | **+4.89%** | +12.3% | -2.2% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `2` | `100.0%` | **`+21.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `CRDO`

* **Total Candidate Breakouts Filtered (Vetoed):** `16`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `14` (87.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+128.8%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+128.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `15` | `93.8%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `6.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*