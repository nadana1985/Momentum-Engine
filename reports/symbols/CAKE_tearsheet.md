# Kronos V12: Institutional Symbol Tear Sheet — `CAKE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+21.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.24x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+21.78%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`504.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+38.0% / -5.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2026-09-03 08:00` | `2026-09-24 08:00` | 504.0h | `$1.9759` | `$2.6474` | **+24.33%** | **+21.78%** | +38.0% | -5.1% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `1` | `100.0%` | **`+21.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `CAKE`

* **Total Candidate Breakouts Filtered (Vetoed):** `64`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `39` (60.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `4`
* **Saved Capital Losses Avoided:** `+394.1%`
* **Missed Upside Forgone:** `-128.2%`
* **Net Veto Alpha:** `+265.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `44` | `68.8%` |
| `Core 4: Funding Rate Cap` | `19` | `29.7%` |
| `Core 4: Whale Firewall` | `1` | `1.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*