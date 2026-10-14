# Kronos V12: Institutional Symbol Tear Sheet — `1000CHEEMS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-22.9%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.80x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-7.62%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-14.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`26.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+3.3% / -8.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-02-09 21:00` | `2025-02-09 22:00` | 1.0h | `$0.0008` | `$0.0008` | **-8.23%** | **-8.59%** | +5.2% | -10.3% | `stop_loss` |
| 2 | Book 3 | `2025-07-18 19:00` | `2025-07-21 19:00` | 72.0h | `$0.0014` | `$0.0014` | **-5.52%** | **-5.68%** | +2.7% | -6.7% | `time_expiry` |
| 3 | Book 3 | `2025-08-18 00:00` | `2025-08-18 05:00` | 5.0h | `$0.0014` | `$0.0013` | **-8.23%** | **-8.59%** | +2.0% | -8.0% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `time_expiry` | `1` | `0.0%` | **`-5.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `1000CHEEMS`

* **Total Candidate Breakouts Filtered (Vetoed):** `69`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `50` (72.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `10`
* **Saved Capital Losses Avoided:** `+703.0%`
* **Missed Upside Forgone:** `-367.3%`
* **Net Veto Alpha:** `+335.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `43` | `62.3%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `14` | `20.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `12` | `17.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*