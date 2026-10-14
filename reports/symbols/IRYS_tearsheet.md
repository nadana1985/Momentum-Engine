# Kronos V12: Institutional Symbol Tear Sheet — `IRYS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.994`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+8.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.09x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.85%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`38.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+26.7% / -20.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2026-01-05 12:00` | `2026-01-08 14:00` | 74.0h | `$0.0418` | `$0.0502` | **+9.32%** | **+8.97%** | +20.7% | -2.5% | `target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2026-05-12 01:00` | `2026-05-16 01:00` | Live | `$0.0441` | `$0.0479` | **+8.50%** | **+8.16%** | +53.8% | -49.2% | `shelf_target_reclaim` |
| 3 | Book 3 | `2026-09-28 06:00` | `2026-09-28 08:00` | 2.0h | `$0.0185` | `$0.0169` | **-8.23%** | **-8.59%** | +5.5% | -8.7% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+9.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `IRYS`

* **Total Candidate Breakouts Filtered (Vetoed):** `422`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `230` (54.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `98`
* **Saved Capital Losses Avoided:** `+2,991.7%`
* **Missed Upside Forgone:** `-3,068.0%`
* **Net Veto Alpha:** `+-76.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `413` | `97.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `6` | `1.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `3` | `0.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*