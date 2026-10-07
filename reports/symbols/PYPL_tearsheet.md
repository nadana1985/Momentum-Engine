# Kronos V12: Institutional Symbol Tear Sheet — `PYPL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-2.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.97x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.63%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`26.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+3.1% / -2.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-22 12:00` | `2026-09-23 14:00` | 26.0h | `$53.4232` | `$52.0388` | **-2.59%** | **-2.63%** | +3.1% | -2.9% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-2.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `PYPL`

* **Total Candidate Breakouts Filtered (Vetoed):** `93`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `93` (100.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+384.6%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+384.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `68` | `73.1%` |
| `Core 3: Min Turnover Velocity` | `19` | `20.4%` |
| `Core 1: Macro Bear Veto` | `6` | `6.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*