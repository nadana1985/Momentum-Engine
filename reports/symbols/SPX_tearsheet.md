# Kronos V12: Institutional Symbol Tear Sheet — `SPX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.744`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-4.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.46%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`11.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.7% / -7.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-01-19 22:00` | `2025-01-20 02:00` | 4.0h | `$1.4809` | `$1.3590` | **-8.23%** | **-8.59%** | +8.6% | -9.5% | `stop_loss` |
| 2 | Book 3 | `2025-04-27 22:00` | `2025-04-28 06:00` | 8.0h | `$0.5350` | `$0.6079` | **+13.64%** | **+12.78%** | +15.8% | -4.2% | `target_reclaim` |
| 3 | Book 3 | `2025-07-29 21:00` | `2025-07-30 19:00` | 22.0h | `$1.9623` | `$1.8008` | **-8.23%** | **-8.59%** | +4.8% | -10.1% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+12.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `SPX`

* **Total Candidate Breakouts Filtered (Vetoed):** `104`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `72` (69.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `28`
* **Saved Capital Losses Avoided:** `+960.8%`
* **Missed Upside Forgone:** `-882.6%`
* **Net Veto Alpha:** `+78.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `54` | `51.9%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `50` | `48.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*