# Kronos V12: Institutional Symbol Tear Sheet — `DOOD`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.042`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+0.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.01x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.14%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`17.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.3% / -9.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-12 21:00` | `2025-07-13 05:00` | 8.0h | `$0.0027` | `$0.0029` | **+8.70%** | **+8.34%** | +8.9% | -0.2% | `target_reclaim` |
| 2 | Book 3 | `2025-07-21 12:00` | `2025-07-21 15:00` | 3.0h | `$0.0044` | `$0.0048` | **+8.70%** | **+8.34%** | +8.7% | -2.2% | `target_reclaim` |
| 3 | Book 3 | `2025-07-23 16:00` | `2025-07-23 17:00` | 1.0h | `$0.0048` | `$0.0044` | **-8.23%** | **-8.59%** | +26.4% | -12.0% | `stop_loss` |
| 4 | Book 3 | `2025-10-07 07:00` | `2025-10-07 08:00` | 1.0h | `$0.0129` | `$0.0118` | **-8.23%** | **-8.59%** | +19.5% | -16.2% | `stop_loss` |
| 5 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0014` | `$0.0014` | **+1.22%** | **+1.22%** | +12.8% | -16.3% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |
| `time_expiry` | `1` | `100.0%` | **`+1.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `DOOD`

* **Total Candidate Breakouts Filtered (Vetoed):** `46`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `34` (73.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `16`
* **Saved Capital Losses Avoided:** `+613.6%`
* **Missed Upside Forgone:** `-497.0%`
* **Net Veto Alpha:** `+116.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `21` | `45.7%` |
| `Core 1: Macro Bear Veto` | `17` | `37.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `8.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `4` | `8.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*