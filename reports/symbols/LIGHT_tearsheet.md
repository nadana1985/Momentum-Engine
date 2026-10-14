# Kronos V12: Institutional Symbol Tear Sheet — `LIGHT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.227`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+2.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.02x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.65%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`45.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+33.6% / -6.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-10-19 14:00` | `2025-10-23 14:00` | Live | `$1.3501` | `$1.4649` | **+8.50%** | **+8.16%** | +88.5% | -8.0% | `shelf_target_reclaim` |
| 2 | Book 3 | `2026-08-30 23:00` | `2026-08-31 18:00` | 19.0h | `$0.1774` | `$0.1628` | **-8.23%** | **-8.59%** | +5.6% | -8.6% | `stop_loss` |
| 3 | Book 3 | `2026-09-26 05:00` | `2026-09-29 05:00` | 72.0h | `$0.1737` | `$0.1779` | **+2.41%** | **+2.38%** | +6.6% | -3.7% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_expiry` | `1` | `100.0%` | **`+2.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `LIGHT`

* **Total Candidate Breakouts Filtered (Vetoed):** `56`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `49` (87.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `31`
* **Saved Capital Losses Avoided:** `+2,035.8%`
* **Missed Upside Forgone:** `-1,874.9%`
* **Net Veto Alpha:** `+160.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `52` | `92.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `7.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*