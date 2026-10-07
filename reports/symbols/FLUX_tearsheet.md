# Kronos V12: Institutional Symbol Tear Sheet — `FLUX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+33.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.40x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+8.34%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`24.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.6% / -1.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-12-03 13:00` | `2024-12-03 20:00` | 7.0h | `$0.7826` | `$0.8507` | **+8.70%** | **+8.34%** | +10.8% | -0.2% | `target_reclaim` |
| 2 | Book 3 | `2025-05-13 02:00` | `2025-05-13 16:00` | 14.0h | `$0.3147` | `$0.3421` | **+8.70%** | **+8.34%** | +8.9% | -1.0% | `target_reclaim` |
| 3 | Book 3 | `2026-08-28 16:00` | `2026-08-30 23:00` | 55.0h | `$0.0457` | `$0.0496` | **+8.70%** | **+8.34%** | +9.2% | -1.0% | `target_reclaim` |
| 4 | Book 3 | `2026-09-28 14:00` | `2026-09-29 10:00` | 20.0h | `$0.0674` | `$0.0732` | **+8.70%** | **+8.34%** | +9.3% | -3.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+33.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `FLUX`

* **Total Candidate Breakouts Filtered (Vetoed):** `110`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `64` (58.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `6`
* **Saved Capital Losses Avoided:** `+632.4%`
* **Missed Upside Forgone:** `-151.3%`
* **Net Veto Alpha:** `+481.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `65` | `59.1%` |
| `Core 1: Macro Bear Veto` | `18` | `16.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `14` | `12.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `13` | `11.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*