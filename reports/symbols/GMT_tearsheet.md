# Kronos V12: Institutional Symbol Tear Sheet — `GMT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+9.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.10x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+9.83%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+19.3% / -3.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-06-20 17:00` | `2023-06-27 17:00` | 168.0h | `$0.2073` | `$0.2287` | **+10.33%** | **+9.83%** | +19.3% | -3.0% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `1` | `100.0%` | **`+9.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `GMT`

* **Total Candidate Breakouts Filtered (Vetoed):** `201`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `140` (69.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `26`
* **Saved Capital Losses Avoided:** `+1,904.1%`
* **Missed Upside Forgone:** `-1,625.0%`
* **Net Veto Alpha:** `+279.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `75` | `37.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `42` | `20.9%` |
| `Core 1: Macro Bear Veto` | `35` | `17.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `30` | `14.9%` |
| `Core 0: Zero-Tolerance Data Firewall` | `19` | `9.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*