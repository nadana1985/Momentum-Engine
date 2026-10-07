# Kronos V12: Institutional Symbol Tear Sheet — `HAEDAL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.086`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+0.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.01x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.25%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`26.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.5% / -7.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-15 06:00` | `2025-07-15 10:00` | 4.0h | `$0.1935` | `$0.2103` | **+8.70%** | **+8.34%** | +9.1% | -2.4% | `target_reclaim` |
| 2 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0185` | `$0.0187` | **+0.99%** | **+0.99%** | +11.1% | -11.6% | `time_expiry` |
| 3 | Book 3 | `2026-09-08 10:00` | `2026-09-08 13:00` | 3.0h | `$0.0206` | `$0.0189` | **-8.23%** | **-8.59%** | +2.4% | -8.6% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |
| `time_expiry` | `1` | `100.0%` | **`+1.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `HAEDAL`

* **Total Candidate Breakouts Filtered (Vetoed):** `29`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `22` (75.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `5`
* **Saved Capital Losses Avoided:** `+425.0%`
* **Missed Upside Forgone:** `-161.4%`
* **Net Veto Alpha:** `+263.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `17` | `58.6%` |
| `Core 1: Macro Bear Veto` | `8` | `27.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `10.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `3.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*