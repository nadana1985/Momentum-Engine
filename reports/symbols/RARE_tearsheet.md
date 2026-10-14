# Kronos V12: Institutional Symbol Tear Sheet — `RARE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.292`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+5.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.05x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.83%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`15.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.8% / -4.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-11-01 22:00` | `2024-11-02 04:00` | 6.0h | `$0.1319` | `$0.1374` | **+4.17%** | **+4.08%** | +6.1% | -8.4% | `target_reclaim` |
| 2 | Book 3 | `2025-04-24 08:00` | `2025-04-24 13:00` | 5.0h | `$0.0584` | `$0.0635` | **+8.70%** | **+8.34%** | +11.1% | -0.4% | `target_reclaim` |
| 3 | Book 3 | `2025-05-12 18:00` | `2025-05-13 16:00` | 22.0h | `$0.0716` | `$0.0758` | **+5.85%** | **+5.68%** | +6.2% | -2.1% | `target_reclaim` |
| 4 | Book 3 | `2025-05-15 04:00` | `2025-05-15 23:00` | 19.0h | `$0.0716` | `$0.0657` | **-8.23%** | **-8.59%** | +1.2% | -8.6% | `stop_loss` |
| 5 | Book 3 | `2025-08-05 14:00` | `2025-08-06 04:00` | 14.0h | `$0.0654` | `$0.0600` | **-8.23%** | **-8.59%** | +5.4% | -8.6% | `stop_loss` |
| 6 | Book 3 | `2026-09-23 15:00` | `2026-09-24 17:00` | 26.0h | `$0.0127` | `$0.0132` | **+4.17%** | **+4.08%** | +4.6% | -0.9% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+22.2%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `RARE`

* **Total Candidate Breakouts Filtered (Vetoed):** `329`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `247` (75.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `39`
* **Saved Capital Losses Avoided:** `+3,510.0%`
* **Missed Upside Forgone:** `-1,174.8%`
* **Net Veto Alpha:** `+2,335.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `254` | `77.2%` |
| `Core 1: Macro Bear Veto` | `45` | `13.7%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `24` | `7.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `6` | `1.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*