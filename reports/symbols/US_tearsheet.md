# Kronos V12: Institutional Symbol Tear Sheet — `US`
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
| **Cumulative Net Log Return** | **`-27.2%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.76x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-13.58%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`7.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+4.8% / -11.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2026-09-23 10:00` | `2026-09-23 14:00` | 4.0h | `$0.0190` | `$0.0166` | **-16.95%** | **-18.58%** | +0.9% | -12.1% | `initial_stop` |
| 2 | Book 3 | `2026-09-27 15:00` | `2026-09-28 02:00` | 11.0h | `$0.0276` | `$0.0253` | **-8.23%** | **-8.59%** | +8.7% | -11.2% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-18.6%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `US`

* **Total Candidate Breakouts Filtered (Vetoed):** `35`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `27` (77.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `18`
* **Saved Capital Losses Avoided:** `+711.1%`
* **Missed Upside Forgone:** `-855.6%`
* **Net Veto Alpha:** `+-144.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `22` | `62.9%` |
| `Core 4: Funding Rate Cap` | `13` | `37.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*