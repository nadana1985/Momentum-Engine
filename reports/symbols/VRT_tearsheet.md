# Kronos V12: Institutional Symbol Tear Sheet — `VRT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-9.5%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.91x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-4.75%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-2.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`119.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.3% / -5.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-03 14:00` | `2026-09-10 13:00` | 167.0h | `$266.5848` | `$248.4929` | **-7.29%** | **-7.54%** | +10.5% | -7.8% | `initial_stop` |
| 2 | Book 3 | `2026-10-07 11:00` | `2026-10-10 11:00` | 72.0h | `$247.3056` | `$242.4923` | **-1.95%** | **-1.97%** | +2.0% | -2.8% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-7.5%`** |
| `time_expiry` | `1` | `0.0%` | **`-2.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `VRT`

* **Total Candidate Breakouts Filtered (Vetoed):** `1`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `1` (100.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+6.6%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+6.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*