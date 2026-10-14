# Kronos V12: Institutional Symbol Tear Sheet — `MAGIC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `18` (`18` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `18` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`77.8%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.010`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+79.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.22x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+4.42%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`34.9h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.0% / -5.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-03-22 00:00` | `2023-03-23 13:00` | 37.0h | `$1.8313` | `$1.6806` | **-8.23%** | **-8.59%** | +6.2% | -13.1% | `stop_loss` |
| 2 | Book 3 | `2023-12-07 09:00` | `2023-12-07 16:00` | 7.0h | `$0.8404` | `$0.9252` | **+10.09%** | **+9.62%** | +12.2% | -2.6% | `target_reclaim` |
| 3 | Book 3 | `2023-12-29 15:00` | `2024-01-01 15:00` | 72.0h | `$1.0921` | `$1.0963` | **+0.38%** | **+0.38%** | +4.1% | -4.8% | `time_expiry` |
| 4 | Book 3 | `2024-02-21 09:00` | `2024-02-24 09:00` | 72.0h | `$1.2768` | `$1.2531` | **-1.86%** | **-1.88%** | +5.3% | -6.2% | `time_expiry` |
| 5 | Book 3 | `2024-03-12 17:00` | `2024-03-13 08:00` | 15.0h | `$1.3064` | `$1.4988` | **+14.73%** | **+13.74%** | +16.4% | -2.3% | `target_reclaim` |
| 6 | Book 3 | `2024-05-23 18:00` | `2024-05-23 21:00` | 3.0h | `$0.7244` | `$0.7546` | **+4.17%** | **+4.08%** | +6.1% | -2.9% | `target_reclaim` |
| 7 | Book 3 | `2024-11-13 03:00` | `2024-11-16 03:00` | 72.0h | `$0.3682` | `$0.3759` | **+2.07%** | **+2.05%** | +8.0% | -6.7% | `time_expiry` |
| 8 | Book 3 | `2024-11-20 17:00` | `2024-11-23 12:00` | 67.0h | `$0.3935` | `$0.4612` | **+17.22%** | **+15.89%** | +18.6% | -3.7% | `target_reclaim` |
| 9 | Book 3 | `2024-12-02 08:00` | `2024-12-03 00:00` | 16.0h | `$0.5441` | `$0.5975` | **+9.82%** | **+9.37%** | +12.9% | -3.7% | `target_reclaim` |
| 10 | Book 3 | `2024-12-09 09:00` | `2024-12-09 21:00` | 12.0h | `$0.6365` | `$0.5841` | **-8.23%** | **-8.59%** | +5.3% | -22.2% | `stop_loss` |
| 11 | Book 3 | `2025-04-19 18:00` | `2025-04-19 19:00` | 1.0h | `$0.1165` | `$0.1256` | **+7.81%** | **+7.52%** | +14.6% | -1.5% | `target_reclaim` |
| 12 | Book 3 | `2025-04-20 04:00` | `2025-04-20 05:00` | 1.0h | `$0.1345` | `$0.1432` | **+6.45%** | **+6.25%** | +6.7% | -1.0% | `target_reclaim` |
| 13 | Book 3 | `2025-04-23 16:00` | `2025-04-24 17:00` | 25.0h | `$0.1976` | `$0.2153` | **+8.97%** | **+8.59%** | +20.2% | -6.4% | `target_reclaim` |
| 14 | Book 4 | `2025-08-04 11:00` | `2025-08-04 17:00` | 6.0h | `$0.2165` | `$0.2598` | **+11.58%** | **+11.05%** | +28.0% | -3.4% | `target_reclaim` |
| 15 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0437` | `$0.0452` | **+3.60%** | **+3.54%** | +13.1% | -4.4% | `time_expiry` |
| 16 | Book 3 | `2026-08-30 23:00` | `2026-09-02 23:00` | 72.0h | `$0.0459` | `$0.0426` | **-7.12%** | **-7.38%** | +3.0% | -7.7% | `time_expiry` |
| 17 | Book 3 | `2026-09-28 03:00` | `2026-10-01 03:00` | 72.0h | `$0.0514` | `$0.0538` | **+4.71%** | **+4.60%** | +7.0% | -2.7% | `time_expiry` |
| 18 | Book 3 | `2026-10-08 16:00` | `2026-10-08 23:00` | 7.0h | `$0.0609` | `$0.0669` | **+9.80%** | **+9.35%** | +10.1% | -0.5% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `10` | `100.0%` | **`+95.5%`** |
| `time_expiry` | `6` | `66.7%` | **`+1.3%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `MAGIC`

* **Total Candidate Breakouts Filtered (Vetoed):** `846`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `478` (56.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `130`
* **Saved Capital Losses Avoided:** `+6,347.1%`
* **Missed Upside Forgone:** `-4,693.4%`
* **Net Veto Alpha:** `+1,653.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `655` | `77.4%` |
| `Core 1: Macro Bear Veto` | `120` | `14.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `47` | `5.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `24` | `2.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*