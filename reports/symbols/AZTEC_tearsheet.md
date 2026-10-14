# Kronos V12: Institutional Symbol Tear Sheet — `AZTEC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.083`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+11.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.13x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.99%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`28.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.9% / -6.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-22 05:00` | `2026-08-24 10:00` | 53.0h | `$0.0139` | `$0.0145` | **+4.17%** | **+4.08%** | +6.5% | -15.1% | `target_reclaim` |
| 2 | Book 3 | `2026-08-26 00:00` | `2026-08-26 23:00` | 23.0h | `$0.0143` | `$0.0150` | **+4.93%** | **+4.81%** | +7.0% | -0.8% | `target_reclaim` |
| 3 | Book 3 | `2026-09-04 21:00` | `2026-09-07 21:00` | 72.0h | `$0.0148` | `$0.0144` | **-2.41%** | **-2.44%** | +4.3% | -3.5% | `time_expiry` |
| 4 | Book 3 | `2026-09-27 13:00` | `2026-09-27 16:00` | 3.0h | `$0.0168` | `$0.0175` | **+4.17%** | **+4.08%** | +13.1% | -4.0% | `target_reclaim` |
| 5 | Book 3 | `2026-09-28 03:00` | `2026-09-28 05:00` | 2.0h | `$0.0169` | `$0.0186` | **+10.51%** | **+10.00%** | +11.6% | -1.1% | `target_reclaim` |
| 6 | Book 3 | `2026-09-28 21:00` | `2026-09-29 16:00` | 19.0h | `$0.0188` | `$0.0172` | **-8.23%** | **-8.59%** | +4.9% | -11.5% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+23.0%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_expiry` | `1` | `0.0%` | **`-2.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `AZTEC`

* **Total Candidate Breakouts Filtered (Vetoed):** `25`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `23` (92.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `2`
* **Saved Capital Losses Avoided:** `+370.3%`
* **Missed Upside Forgone:** `-41.7%`
* **Net Veto Alpha:** `+328.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `13` | `52.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `6` | `24.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `6` | `24.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*