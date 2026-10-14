# Kronos V12: Institutional Symbol Tear Sheet — `AIA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.625`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-3.2%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.97x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.61%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`6.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.1% / -14.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0730` | `$0.0771` | **+5.52%** | **+5.37%** | +13.7% | -16.8% | `target_reclaim` |
| 2 | Book 3 | `2026-09-09 15:00` | `2026-09-10 02:00` | 11.0h | `$0.0799` | `$0.0733` | **-8.23%** | **-8.59%** | +8.6% | -11.6% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+5.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `AIA`

* **Total Candidate Breakouts Filtered (Vetoed):** `45`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `42` (93.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `9`
* **Saved Capital Losses Avoided:** `+1,088.2%`
* **Missed Upside Forgone:** `-264.2%`
* **Net Veto Alpha:** `+823.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `22` | `48.9%` |
| `Core 1: Macro Bear Veto` | `19` | `42.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `8.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*