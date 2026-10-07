# Kronos V12: Institutional Symbol Tear Sheet — `HMSTR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.454`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-6.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.94x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.23%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-3.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`51.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+4.2% / -5.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-01-07 15:00` | `2025-01-08 00:00` | 9.0h | `$0.0032` | `$0.0029` | **-8.23%** | **-8.59%** | +1.8% | -8.1% | `stop_loss` |
| 2 | Book 3 | `2025-07-12 00:00` | `2025-07-15 00:00` | 72.0h | `$0.0008` | `$0.0007` | **-3.56%** | **-3.63%** | +4.5% | -6.0% | `time_expiry` |
| 3 | Book 3 | `2026-09-23 15:00` | `2026-09-26 15:00` | 72.0h | `$0.0002` | `$0.0002` | **+5.70%** | **+5.54%** | +6.4% | -2.0% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_expiry` | `2` | `50.0%` | **`+1.9%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `HMSTR`

* **Total Candidate Breakouts Filtered (Vetoed):** `58`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `45` (77.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `23`
* **Saved Capital Losses Avoided:** `+892.8%`
* **Missed Upside Forgone:** `-1,161.8%`
* **Net Veto Alpha:** `+-268.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `46` | `79.3%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `10` | `17.2%` |
| `Core 3: Min Turnover Velocity` | `1` | `1.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `1.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*