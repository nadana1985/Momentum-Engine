# Kronos V12: Institutional Symbol Tear Sheet — `ORDER`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`80.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`71.797`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+24.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.27x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.83%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-0.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`20.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+28.8% / -8.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-09-28 12:00` | `2025-10-02 12:00` | Live | `$0.2134` | `$0.2316` | **+8.50%** | **+8.16%** | +114.6% | -34.7% | `shelf_target_reclaim` |
| 2 | Book 3 | `2026-08-27 10:00` | `2026-08-27 11:00` | 1.0h | `$0.0330` | `$0.0344` | **+4.17%** | **+4.08%** | +7.5% | -0.3% | `target_reclaim` |
| 3 | Book 3 | `2026-08-27 13:00` | `2026-08-27 16:00` | 3.0h | `$0.0339` | `$0.0353` | **+4.17%** | **+4.08%** | +4.4% | -1.2% | `target_reclaim` |
| 4 | Book 3 | `2026-09-09 22:00` | `2026-09-10 03:00` | 5.0h | `$0.0342` | `$0.0371` | **+8.54%** | **+8.19%** | +10.5% | -1.3% | `target_reclaim` |
| 5 | Book 3 | `2026-09-11 00:00` | `2026-09-14 00:00` | 72.0h | `$0.0342` | `$0.0341` | **-0.34%** | **-0.34%** | +7.0% | -2.9% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+16.4%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `time_expiry` | `1` | `0.0%` | **`-0.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `ORDER`

* **Total Candidate Breakouts Filtered (Vetoed):** `27`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `25` (92.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+274.8%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+274.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `21` | `77.8%` |
| `Core 1: Macro Bear Veto` | `6` | `22.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*