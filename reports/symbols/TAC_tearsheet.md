# Kronos V12: Institutional Symbol Tear Sheet — `TAC`
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
| **Cumulative Net Log Return** | **`-31.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.73x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-15.80%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-27.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`1.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.7% / -24.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-26 09:00` | `2026-08-26 10:00` | 1.0h | `$0.0040` | `$0.0036` | **-3.76%** | **-3.83%** | +8.7% | -14.7% | `initial_stop` |
| 2 | Book 3 | `2026-08-27 10:00` | `2026-08-27 11:00` | 1.0h | `$0.0039` | `$0.0030` | **-24.25%** | **-27.77%** | +24.8% | -33.8% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-3.8%`** |
| `stop_loss` | `1` | `0.0%` | **`-27.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `TAC`

* **Total Candidate Breakouts Filtered (Vetoed):** `40`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `24` (60.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `26`
* **Saved Capital Losses Avoided:** `+625.6%`
* **Missed Upside Forgone:** `-1,683.0%`
* **Net Veto Alpha:** `+-1,057.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `34` | `85.0%` |
| `Core 4: Defensible Whale Dump` | `3` | `7.5%` |
| `Core 4: Funding Rate Cap` | `3` | `7.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*