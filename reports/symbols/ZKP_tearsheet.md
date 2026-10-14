# Kronos V12: Institutional Symbol Tear Sheet — `ZKP`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.272`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-4.0%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.02%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-5.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`54.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+4.6% / -6.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-31 23:00` | `2026-09-03 23:00` | 72.0h | `$0.0453` | `$0.0460` | **+1.52%** | **+1.51%** | +8.8% | -5.0% | `time_expiry` |
| 2 | Book 3 | `2026-10-07 02:00` | `2026-10-08 15:00` | 37.0h | `$0.0471` | `$0.0446` | **-5.39%** | **-5.54%** | +0.4% | -7.1% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `1` | `0.0%` | **`-5.5%`** |
| `time_expiry` | `1` | `100.0%` | **`+1.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `ZKP`

* **Total Candidate Breakouts Filtered (Vetoed):** `23`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `21` (91.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `3`
* **Saved Capital Losses Avoided:** `+334.8%`
* **Missed Upside Forgone:** `-63.5%`
* **Net Veto Alpha:** `+271.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `14` | `60.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `8` | `34.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `4.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*