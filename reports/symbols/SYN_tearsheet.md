# Kronos V12: Institutional Symbol Tear Sheet — `SYN`
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
| **Cumulative Net Log Return** | **`-22.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.80x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-11.03%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-13.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`8.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+1.0% / -17.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-20 08:00` | `2026-08-21 00:00` | 16.0h | `$0.1150` | `$0.1055` | **-8.23%** | **-8.59%** | +0.3% | -8.7% | `initial_stop` |
| 2 | Book 1 | `2026-08-22 04:00` | `2026-08-22 05:00` | 1.0h | `$0.1224` | `$0.1074` | **-12.60%** | **-13.47%** | +1.8% | -25.7% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `2` | `0.0%` | **`-22.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `SYN`

* **Total Candidate Breakouts Filtered (Vetoed):** `64`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `42` (65.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `34`
* **Saved Capital Losses Avoided:** `+758.6%`
* **Missed Upside Forgone:** `-2,262.9%`
* **Net Veto Alpha:** `+-1,504.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `33` | `51.6%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `31` | `48.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*