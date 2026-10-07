# Kronos V12: Institutional Symbol Tear Sheet — `AIXBT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `9` (`9` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `9` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.347`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+24.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.28x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.71%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`36.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.2% / -4.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-04-26 11:00` | `2025-04-26 15:00` | 4.0h | `$0.1452` | `$0.1578` | **+8.70%** | **+8.34%** | +9.5% | -2.1% | `target_reclaim` |
| 2 | Book 3 | `2025-06-16 23:00` | `2025-06-17 16:00` | 17.0h | `$0.1689` | `$0.1550` | **-8.23%** | **-8.59%** | +3.1% | -9.9% | `stop_loss` |
| 3 | Book 3 | `2025-06-30 08:00` | `2025-07-03 08:00` | 72.0h | `$0.1305` | `$0.1363` | **+4.41%** | **+4.32%** | +6.3% | -7.9% | `time_expiry` |
| 4 | Book 3 | `2025-07-12 15:00` | `2025-07-13 14:00` | 23.0h | `$0.1402` | `$0.1524` | **+8.70%** | **+8.34%** | +8.7% | -0.6% | `target_reclaim` |
| 5 | Book 3 | `2025-07-14 08:00` | `2025-07-15 08:00` | 24.0h | `$0.1576` | `$0.1446` | **-8.23%** | **-8.59%** | +3.0% | -8.7% | `stop_loss` |
| 6 | Book 3 | `2025-07-17 16:00` | `2025-07-20 16:00` | 72.0h | `$0.1685` | `$0.1769` | **+4.94%** | **+4.83%** | +7.1% | -5.5% | `time_expiry` |
| 7 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0191` | `$0.0208` | **+8.70%** | **+8.34%** | +22.7% | -0.8% | `target_reclaim` |
| 8 | Book 3 | `2026-09-23 14:00` | `2026-09-25 09:00` | 43.0h | `$0.0217` | `$0.0236` | **+8.70%** | **+8.34%** | +9.2% | -2.1% | `target_reclaim` |
| 9 | Book 3 | `2026-09-28 09:00` | `2026-10-01 09:00` | 72.0h | `$0.0229` | `$0.0227` | **-0.92%** | **-0.93%** | +4.6% | -4.6% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+33.4%`** |
| `time_expiry` | `3` | `66.7%` | **`+8.2%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `AIXBT`

* **Total Candidate Breakouts Filtered (Vetoed):** `74`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `63` (85.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `21`
* **Saved Capital Losses Avoided:** `+880.4%`
* **Missed Upside Forgone:** `-719.4%`
* **Net Veto Alpha:** `+161.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `40` | `54.1%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `21` | `28.4%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `10` | `13.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `3` | `4.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*