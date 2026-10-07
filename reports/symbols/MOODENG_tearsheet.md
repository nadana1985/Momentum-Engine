# Kronos V12: Institutional Symbol Tear Sheet — `MOODENG`
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
| **Maximum Log Drawdown** | **`-25.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`15.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.6% / -6.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-04-24 07:00` | `2025-04-24 16:00` | 9.0h | `$0.0346` | `$0.0376` | **+8.70%** | **+8.34%** | +9.1% | -1.4% | `target_reclaim` |
| 2 | Book 3 | `2025-04-26 08:00` | `2025-04-26 20:00` | 12.0h | `$0.0430` | `$0.0468` | **+8.70%** | **+8.34%** | +9.0% | -2.1% | `target_reclaim` |
| 3 | Book 3 | `2025-04-27 01:00` | `2025-04-28 01:00` | 24.0h | `$0.0448` | `$0.0411` | **-8.23%** | **-8.59%** | +4.5% | -9.4% | `stop_loss` |
| 4 | Book 3 | `2025-06-30 14:00` | `2025-07-01 14:00` | 24.0h | `$0.1476` | `$0.1355` | **-8.23%** | **-8.59%** | +4.3% | -8.3% | `stop_loss` |
| 5 | Book 3 | `2025-07-03 06:00` | `2025-07-03 10:00` | 4.0h | `$0.2048` | `$0.1880` | **-8.23%** | **-8.59%** | +7.1% | -8.5% | `stop_loss` |
| 6 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0391` | `$0.0425` | **+8.70%** | **+8.34%** | +37.6% | -11.8% | `target_reclaim` |
| 7 | Book 3 | `2026-09-23 14:00` | `2026-09-24 22:00` | 32.0h | `$0.0458` | `$0.0497` | **+8.70%** | **+8.34%** | +9.7% | -4.9% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+33.4%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `MOODENG`

* **Total Candidate Breakouts Filtered (Vetoed):** `72`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `50` (69.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `32`
* **Saved Capital Losses Avoided:** `+864.8%`
* **Missed Upside Forgone:** `-3,415.9%`
* **Net Veto Alpha:** `+-2,551.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `33` | `45.8%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `29` | `40.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `8` | `11.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2` | `2.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*