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
| **Profit Factor (Log-Space)** | **`1.747`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+6.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.07x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.14%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`36.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.9% / -8.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-15 06:00` | `2025-07-15 10:00` | 4.0h | `$0.1911` | `$0.2103` | **+10.05%** | **+9.58%** | +10.5% | -1.2% | `target_reclaim` |
| 2 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0177` | `$0.0187` | **+5.58%** | **+5.43%** | +16.1% | -7.6% | `time_expiry` |
| 3 | Book 3 | `2026-09-08 13:00` | `2026-09-09 22:00` | 33.0h | `$0.0192` | `$0.0176` | **-8.23%** | **-8.59%** | +6.1% | -16.5% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+9.6%`** |
| `time_expiry` | `1` | `100.0%` | **`+5.4%`** |

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