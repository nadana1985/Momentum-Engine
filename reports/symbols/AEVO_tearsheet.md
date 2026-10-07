# Kronos V12: Institutional Symbol Tear Sheet — `AEVO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.972`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-0.5%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`1.00x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.10%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`32.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.2% / -7.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-11-12 10:00` | `2024-11-13 04:00` | 18.0h | `$0.3663` | `$0.3361` | **-8.23%** | **-8.59%** | +5.9% | -9.2% | `stop_loss` |
| 2 | Book 3 | `2025-05-12 18:00` | `2025-05-13 18:00` | 24.0h | `$0.1432` | `$0.1557` | **+8.70%** | **+8.34%** | +9.6% | -7.8% | `target_reclaim` |
| 3 | Book 3 | `2025-05-14 08:00` | `2025-05-15 05:00` | 21.0h | `$0.1467` | `$0.1347` | **-8.23%** | **-8.59%** | +3.8% | -8.2% | `stop_loss` |
| 4 | Book 3 | `2025-07-17 03:00` | `2025-07-18 05:00` | 26.0h | `$0.1140` | `$0.1239` | **+8.70%** | **+8.34%** | +9.9% | -1.1% | `target_reclaim` |
| 5 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0235` | `$0.0235` | **+0.02%** | **+0.02%** | +11.9% | -13.2% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |
| `time_expiry` | `1` | `100.0%` | **`+0.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `AEVO`

* **Total Candidate Breakouts Filtered (Vetoed):** `102`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `60` (58.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `19`
* **Saved Capital Losses Avoided:** `+765.6%`
* **Missed Upside Forgone:** `-537.4%`
* **Net Veto Alpha:** `+228.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `67` | `65.7%` |
| `Core 1: Macro Bear Veto` | `24` | `23.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `11` | `10.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*