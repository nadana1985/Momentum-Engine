# Kronos V12: Institutional Symbol Tear Sheet — `SKY`
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
| **Cumulative Net Log Return** | **`+11.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.12x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+11.13%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.7% / -2.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-18 11:00` | `2026-09-25 11:00` | 168.0h | `$0.0666` | `$0.0744` | **+11.77%** | **+11.13%** | +16.7% | -2.8% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `1` | `100.0%` | **`+11.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `SKY`

* **Total Candidate Breakouts Filtered (Vetoed):** `65`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `44` (67.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `1`
* **Saved Capital Losses Avoided:** `+354.8%`
* **Missed Upside Forgone:** `-23.8%`
* **Net Veto Alpha:** `+331.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `65` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*