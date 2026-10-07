# Kronos V12: Institutional Symbol Tear Sheet — `PUMPBTC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.367`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+14.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.16x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.89%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`15.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.0% / -8.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-09-21 16:00` | `2025-09-21 17:00` | 1.0h | `$0.1472` | `$0.1600` | **+8.70%** | **+8.34%** | +16.8% | -1.1% | `target_reclaim` |
| 2 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0109` | `$0.0106` | **-1.96%** | **-1.98%** | +9.1% | -16.2% | `time_expiry` |
| 3 | Book 3 | `2026-08-26 09:00` | `2026-08-26 10:00` | 1.0h | `$0.0125` | `$0.0136` | **+8.70%** | **+8.34%** | +21.3% | -1.3% | `target_reclaim` |
| 4 | Book 3 | `2026-10-04 23:00` | `2026-10-05 00:00` | 1.0h | `$0.0116` | `$0.0106` | **-8.23%** | **-8.59%** | +10.4% | -13.7% | `stop_loss` |
| 5 | Book 3 | `2026-10-05 05:00` | `2026-10-05 06:00` | 1.0h | `$0.0151` | `$0.0164` | **+8.70%** | **+8.34%** | +17.6% | -10.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+25.0%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_expiry` | `1` | `0.0%` | **`-2.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `PUMPBTC`

* **Total Candidate Breakouts Filtered (Vetoed):** `29`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `27` (93.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `16`
* **Saved Capital Losses Avoided:** `+762.6%`
* **Missed Upside Forgone:** `-2,674.1%`
* **Net Veto Alpha:** `+-1,911.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `23` | `79.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `10.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2` | `6.9%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `1` | `3.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*