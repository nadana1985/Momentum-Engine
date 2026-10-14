# Kronos V12: Institutional Symbol Tear Sheet — `TA`
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
| **Cumulative Net Log Return** | **`-15.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.86x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-7.54%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`171.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.2% / -11.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2026-04-30 09:00` | `2026-05-14 15:00` | 342.0h | `$0.0520` | `$0.0466` | **-6.31%** | **-6.48%** | +8.1% | -10.9% | `structural_stop` |
| 2 | Book 3 | `2026-10-07 16:00` | `2026-10-07 17:00` | 1.0h | `$0.0603` | `$0.0553` | **-8.23%** | **-8.59%** | +14.3% | -11.5% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `structural_stop` | `1` | `0.0%` | **`-6.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `TA`

* **Total Candidate Breakouts Filtered (Vetoed):** `152`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `140` (92.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `74`
* **Saved Capital Losses Avoided:** `+4,024.5%`
* **Missed Upside Forgone:** `-5,256.1%`
* **Net Veto Alpha:** `+-1,231.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `148` | `97.4%` |
| `Core 3: Min Turnover Velocity` | `2` | `1.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `0.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `0.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*