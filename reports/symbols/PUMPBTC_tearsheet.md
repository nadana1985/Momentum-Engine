# Kronos V12: Institutional Symbol Tear Sheet — `PUMPBTC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+48.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.63x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+9.76%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`15.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.6% / -6.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-09-21 13:00` | `2025-09-21 14:00` | 1.0h | `$0.1536` | `$0.1600` | **+4.17%** | **+4.08%** | +9.5% | -2.3% | `target_reclaim` |
| 2 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0103` | `$0.0106` | **+3.74%** | **+3.67%** | +15.4% | -11.3% | `time_expiry` |
| 3 | Book 3 | `2026-08-26 09:00` | `2026-08-26 10:00` | 1.0h | `$0.0125` | `$0.0148` | **+18.00%** | **+16.55%** | +21.3% | -1.3% | `climax_whale_euphoria_harvest` |
| 4 | Book 3 | `2026-10-05 00:00` | `2026-10-05 01:00` | 1.0h | `$0.0107` | `$0.0126` | **+17.55%** | **+16.17%** | +19.4% | -6.7% | `target_reclaim` |
| 5 | Book 3 | `2026-10-05 05:00` | `2026-10-05 06:00` | 1.0h | `$0.0151` | `$0.0164` | **+8.70%** | **+8.34%** | +17.6% | -10.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+28.6%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+16.6%`** |
| `time_expiry` | `1` | `100.0%` | **`+3.7%`** |

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