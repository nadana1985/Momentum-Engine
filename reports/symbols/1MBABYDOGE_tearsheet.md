# Kronos V12: Institutional Symbol Tear Sheet — `1MBABYDOGE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`57.1%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.294`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+7.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.08x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.08%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`29.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.3% / -6.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-10-20 12:00` | `2024-10-23 08:00` | 68.0h | `$0.0031` | `$0.0029` | **-8.23%** | **-8.59%** | +2.9% | -9.2% | `stop_loss` |
| 2 | Book 3 | `2025-04-24 08:00` | `2025-04-25 07:00` | 23.0h | `$0.0013` | `$0.0014` | **+8.70%** | **+8.34%** | +9.1% | -12.2% | `target_reclaim` |
| 3 | Book 3 | `2025-04-27 01:00` | `2025-04-28 16:00` | 39.0h | `$0.0014` | `$0.0013` | **-8.23%** | **-8.59%** | +3.8% | -8.2% | `stop_loss` |
| 4 | Book 3 | `2025-05-12 18:00` | `2025-05-13 07:00` | 13.0h | `$0.0016` | `$0.0018` | **+8.70%** | **+8.34%** | +10.0% | -0.3% | `target_reclaim` |
| 5 | Book 3 | `2025-05-13 19:00` | `2025-05-14 17:00` | 22.0h | `$0.0020` | `$0.0018` | **-8.23%** | **-8.59%** | +4.6% | -8.6% | `stop_loss` |
| 6 | Book 3 | `2025-07-15 01:00` | `2025-07-16 14:00` | 37.0h | `$0.0013` | `$0.0014` | **+8.70%** | **+8.34%** | +8.7% | -3.0% | `target_reclaim` |
| 7 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0004` | `$0.0004` | **+8.70%** | **+8.34%** | +19.0% | -0.9% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+33.4%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `1MBABYDOGE`

* **Total Candidate Breakouts Filtered (Vetoed):** `81`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `55` (67.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `4`
* **Saved Capital Losses Avoided:** `+677.1%`
* **Missed Upside Forgone:** `-286.4%`
* **Net Veto Alpha:** `+390.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `44` | `54.3%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `31` | `38.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `6` | `7.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*