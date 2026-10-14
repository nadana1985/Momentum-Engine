# Kronos V12: Institutional Symbol Tear Sheet — `AXTI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-19.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.82x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-9.67%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-6.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`132.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.8% / -8.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2026-09-21 14:00` | `2026-09-23 20:00` | 54.0h | `$79.4582` | `$72.4265` | **-12.19%** | **-13.00%** | +3.6% | -9.2% | `initial_stop` |
| 2 | Book 1 | `2026-09-29 13:00` | `2026-10-08 08:00` | 211.0h | `$81.7739` | `$77.2065` | **-6.13%** | **-6.33%** | +8.0% | -7.8% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `2` | `0.0%` | **`-19.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `AXTI`

* **Total Candidate Breakouts Filtered (Vetoed):** `217`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `168` (77.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `46`
* **Saved Capital Losses Avoided:** `+3,098.2%`
* **Missed Upside Forgone:** `-950.3%`
* **Net Veto Alpha:** `+2,148.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `210` | `96.8%` |
| `Core 3: Min Turnover Velocity` | `6` | `2.8%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*