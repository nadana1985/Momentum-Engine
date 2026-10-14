# Kronos V12: Institutional Symbol Tear Sheet — `RECALL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.358`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+1.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.01x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.54%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`68.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.1% / -5.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-23 04:00` | `2026-08-26 04:00` | 72.0h | `$0.0479` | `$0.0465` | **-2.96%** | **-3.01%** | +9.8% | -3.9% | `time_expiry` |
| 2 | Book 3 | `2026-09-27 15:00` | `2026-09-30 08:00` | 65.0h | `$0.0478` | `$0.0498` | **+4.17%** | **+4.08%** | +4.4% | -7.4% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `1` | `100.0%` | **`+4.1%`** |
| `time_expiry` | `1` | `0.0%` | **`-3.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `RECALL`

* **Total Candidate Breakouts Filtered (Vetoed):** `24`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `22` (91.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `1`
* **Saved Capital Losses Avoided:** `+306.1%`
* **Missed Upside Forgone:** `-20.1%`
* **Net Veto Alpha:** `+285.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `19` | `79.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `5` | `20.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*