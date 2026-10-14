# Kronos V12: Institutional Symbol Tear Sheet — `SHELL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.936`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+26.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.30x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.43%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-9.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`50.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.9% / -6.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-24 06:00` | `2025-07-24 17:00` | 11.0h | `$0.1691` | `$0.1869` | **+10.55%** | **+10.03%** | +21.6% | -4.1% | `target_reclaim` |
| 2 | Book 3 | `2025-07-24 18:00` | `2025-07-24 19:00` | 1.0h | `$0.1911` | `$0.1991` | **+4.17%** | **+4.08%** | +10.9% | -3.5% | `target_reclaim` |
| 3 | Book 3 | `2025-08-05 14:00` | `2025-08-07 12:00` | 46.0h | `$0.1460` | `$0.1528` | **+4.67%** | **+4.56%** | +6.9% | -5.0% | `target_reclaim` |
| 4 | Book 3 | `2025-09-22 00:00` | `2025-09-22 06:00` | 6.0h | `$0.1406` | `$0.1290` | **-8.23%** | **-8.59%** | +1.7% | -21.3% | `stop_loss` |
| 5 | Book 3 | `2026-08-23 04:00` | `2026-08-26 04:00` | 72.0h | `$0.0224` | `$0.0223` | **-0.47%** | **-0.47%** | +7.8% | -3.2% | `time_expiry` |
| 6 | Book 2 | `2026-09-20 08:00` | `2026-09-27 08:00` | 168.0h | `$0.0237` | `$0.0275` | **+18.27%** | **+16.97%** | +22.3% | -2.4% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+18.7%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_cap` | `1` | `100.0%` | **`+17.0%`** |
| `time_expiry` | `1` | `0.0%` | **`-0.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `SHELL`

* **Total Candidate Breakouts Filtered (Vetoed):** `37`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `28` (75.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+425.4%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+425.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `20` | `54.1%` |
| `Core 1: Macro Bear Veto` | `15` | `40.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `2.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `2.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*