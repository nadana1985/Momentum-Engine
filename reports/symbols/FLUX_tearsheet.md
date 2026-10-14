# Kronos V12: Institutional Symbol Tear Sheet — `FLUX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `9` (`9` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `9` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+62.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.86x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+6.91%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`29.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.5% / -1.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-11-13 06:00` | `2024-11-13 14:00` | 8.0h | `$0.5448` | `$0.5825` | **+6.92%** | **+6.69%** | +9.5% | -0.4% | `target_reclaim` |
| 2 | Book 3 | `2024-12-03 13:00` | `2024-12-03 20:00` | 7.0h | `$0.7826` | `$0.8507` | **+8.70%** | **+8.34%** | +10.8% | -0.2% | `target_reclaim` |
| 3 | Book 3 | `2025-04-23 21:00` | `2025-04-24 22:00` | 25.0h | `$0.2655` | `$0.2766` | **+4.17%** | **+4.08%** | +4.6% | -2.0% | `target_reclaim` |
| 4 | Book 3 | `2025-04-28 02:00` | `2025-04-28 07:00` | 5.0h | `$0.2730` | `$0.2897` | **+6.12%** | **+5.94%** | +7.9% | -0.1% | `target_reclaim` |
| 5 | Book 3 | `2025-04-29 23:00` | `2025-04-30 12:00` | 13.0h | `$0.3053` | `$0.3180` | **+4.17%** | **+4.08%** | +5.3% | -1.4% | `target_reclaim` |
| 6 | Book 3 | `2025-07-04 15:00` | `2025-07-06 16:00` | 49.0h | `$0.1952` | `$0.2033` | **+4.17%** | **+4.08%** | +4.5% | -1.5% | `target_reclaim` |
| 7 | Book 3 | `2025-07-22 01:00` | `2025-07-23 04:00` | 27.0h | `$0.2696` | `$0.2808` | **+4.17%** | **+4.08%** | +4.3% | -2.4% | `target_reclaim` |
| 8 | Book 4 | `2026-09-22 00:00` | `2026-09-26 17:00` | 113.0h | `$0.0624` | `$0.0748` | **+17.80%** | **+16.60%** | +20.5% | -0.8% | `target_reclaim` |
| 9 | Book 3 | `2026-09-28 14:00` | `2026-09-29 10:00` | 20.0h | `$0.0674` | `$0.0732` | **+8.70%** | **+8.34%** | +9.3% | -3.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `9` | `100.0%` | **`+62.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `FLUX`

* **Total Candidate Breakouts Filtered (Vetoed):** `125`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `81` (64.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `6`
* **Saved Capital Losses Avoided:** `+945.0%`
* **Missed Upside Forgone:** `-151.3%`
* **Net Veto Alpha:** `+793.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `83` | `66.4%` |
| `Core 1: Macro Bear Veto` | `18` | `14.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `13` | `10.4%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `11` | `8.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*