# Kronos V12: Institutional Symbol Tear Sheet — `SNXX`
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
| **Cumulative Net Log Return** | **`-12.0%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.89x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-6.02%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-3.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`72.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+-6.8% / -42.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2026-07-10 19:00` | `2026-07-14 19:00` | Live | `$25.8060` | `$23.6899` | **-8.20%** | **-8.56%** | +-15.8% | -77.0% | `shelf_stop_loss` |
| 2 | Book 3 | `2026-09-24 04:00` | `2026-09-27 04:00` | 72.0h | `$17.9106` | `$17.2966` | **-3.43%** | **-3.49%** | +2.1% | -7.8% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_expiry` | `1` | `0.0%` | **`-3.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `SNXX`

* **Total Candidate Breakouts Filtered (Vetoed):** `6`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `6` (100.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+135.5%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+135.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `5` | `83.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `16.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*