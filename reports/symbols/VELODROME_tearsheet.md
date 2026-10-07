# Kronos V12: Institutional Symbol Tear Sheet — `VELODROME`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+16.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.18x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+8.34%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`30.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.9% / -3.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-15 03:00` | `2025-07-15 23:00` | 20.0h | `$0.0526` | `$0.0572` | **+8.70%** | **+8.34%** | +9.7% | -0.8% | `target_reclaim` |
| 2 | Book 3 | `2026-09-09 22:00` | `2026-09-11 15:00` | 41.0h | `$0.0244` | `$0.0265` | **+8.70%** | **+8.34%** | +10.1% | -5.1% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `VELODROME`

* **Total Candidate Breakouts Filtered (Vetoed):** `81`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `54` (66.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `8`
* **Saved Capital Losses Avoided:** `+623.3%`
* **Missed Upside Forgone:** `-234.2%`
* **Net Veto Alpha:** `+389.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `34` | `42.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `23` | `28.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `13` | `16.0%` |
| `Core 3: Min Turnover Velocity` | `6` | `7.4%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `5` | `6.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*