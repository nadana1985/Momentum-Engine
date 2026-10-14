# Kronos V12: Institutional Symbol Tear Sheet — `USUAL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.688`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-5.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.95x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.34%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`35.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.0% / -5.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-15 05:00` | `2025-05-15 23:00` | 18.0h | `$0.1488` | `$0.1366` | **-8.23%** | **-8.59%** | +3.4% | -9.0% | `stop_loss` |
| 2 | Book 3 | `2025-07-04 16:00` | `2025-07-07 16:00` | 72.0h | `$0.0650` | `$0.0663` | **+2.13%** | **+2.11%** | +8.5% | -2.4% | `time_expiry` |
| 3 | Book 3 | `2025-07-28 08:00` | `2025-07-28 19:00` | 11.0h | `$0.0925` | `$0.0849` | **-8.23%** | **-8.59%** | +1.6% | -8.0% | `stop_loss` |
| 4 | Book 3 | `2026-09-23 14:00` | `2026-09-25 07:00` | 41.0h | `$0.0131` | `$0.0145` | **+10.19%** | **+9.71%** | +10.3% | -3.8% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+9.7%`** |
| `time_expiry` | `1` | `100.0%` | **`+2.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `USUAL`

* **Total Candidate Breakouts Filtered (Vetoed):** `47`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `28` (59.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `17`
* **Saved Capital Losses Avoided:** `+352.2%`
* **Missed Upside Forgone:** `-612.1%`
* **Net Veto Alpha:** `+-259.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `18` | `38.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `17` | `36.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `10` | `21.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2` | `4.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*