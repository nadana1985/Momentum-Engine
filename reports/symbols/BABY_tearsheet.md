# Kronos V12: Institutional Symbol Tear Sheet — `BABY`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.169`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-7.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.93x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.57%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`43.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+4.8% / -7.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-14 15:00` | `2025-05-15 05:00` | 14.0h | `$0.0974` | `$0.0894` | **-8.23%** | **-8.59%** | +2.8% | -9.1% | `stop_loss` |
| 2 | Book 3 | `2025-08-11 11:00` | `2025-08-14 11:00` | 72.0h | `$0.0621` | `$0.0630` | **+1.46%** | **+1.45%** | +6.7% | -6.0% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_expiry` | `1` | `100.0%` | **`+1.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `BABY`

* **Total Candidate Breakouts Filtered (Vetoed):** `148`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `130` (87.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `11`
* **Saved Capital Losses Avoided:** `+1,676.4%`
* **Missed Upside Forgone:** `-648.0%`
* **Net Veto Alpha:** `+1,028.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `98` | `66.2%` |
| `Core 1: Macro Bear Veto` | `32` | `21.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `12` | `8.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `6` | `4.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*