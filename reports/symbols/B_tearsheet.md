# Kronos V12: Institutional Symbol Tear Sheet — `B`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.485`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-8.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.92x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.95%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`16.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.3% / -7.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-10-28 20:00` | `2025-10-29 19:00` | 23.0h | `$0.1867` | `$0.2029` | **+8.70%** | **+8.34%** | +9.5% | -3.2% | `target_reclaim` |
| 2 | Book 3 | `2026-09-05 10:00` | `2026-09-06 05:00` | 19.0h | `$0.1802` | `$0.1654` | **-8.23%** | **-8.59%** | +7.0% | -10.3% | `stop_loss` |
| 3 | Book 3 | `2026-09-15 08:00` | `2026-09-15 15:00` | 7.0h | `$0.2154` | `$0.1976` | **-8.23%** | **-8.59%** | +2.4% | -8.3% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `B`

* **Total Candidate Breakouts Filtered (Vetoed):** `58`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `41` (70.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `17`
* **Saved Capital Losses Avoided:** `+822.2%`
* **Missed Upside Forgone:** `-1,041.2%`
* **Net Veto Alpha:** `+-219.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `29` | `50.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `22` | `37.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `7` | `12.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*