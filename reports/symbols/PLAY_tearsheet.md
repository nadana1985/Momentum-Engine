# Kronos V12: Institutional Symbol Tear Sheet — `PLAY`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.704`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-5.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.95x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.27%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`45.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+18.5% / -8.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-10-08 02:00` | `2025-10-10 15:00` | 61.0h | `$0.0472` | `$0.0433` | **-8.23%** | **-8.59%** | +8.4% | -9.4% | `stop_loss` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2025-12-23 14:00` | `2025-12-27 14:00` | Live | `$0.0407` | `$0.0442` | **+8.50%** | **+8.16%** | +45.3% | -8.1% | `shelf_target_reclaim` |
| 3 | Book 3 | `2026-08-27 15:00` | `2026-08-30 15:00` | 72.0h | `$0.0365` | `$0.0380` | **+4.02%** | **+3.94%** | +9.5% | -4.5% | `time_expiry` |
| 4 | Book 3 | `2026-09-25 03:00` | `2026-09-25 06:00` | 3.0h | `$0.0373` | `$0.0342` | **-8.23%** | **-8.59%** | +11.0% | -9.9% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `time_expiry` | `1` | `100.0%` | **`+3.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `PLAY`

* **Total Candidate Breakouts Filtered (Vetoed):** `115`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `100` (87.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `21`
* **Saved Capital Losses Avoided:** `+1,217.9%`
* **Missed Upside Forgone:** `-1,352.8%`
* **Net Veto Alpha:** `+-134.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `111` | `96.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `2` | `1.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `2` | `1.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*