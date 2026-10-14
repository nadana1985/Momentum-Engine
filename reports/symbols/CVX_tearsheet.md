# Kronos V12: Institutional Symbol Tear Sheet — `CVX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+21.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.24x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+7.30%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`13.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.0% / -9.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-07-24 12:00` | `2025-07-28 12:00` | Live | `$4.4270` | `$4.8033` | **+8.50%** | **+8.16%** | +27.6% | -23.2% | `shelf_target_reclaim` |
| 2 | Book 3 | `2026-08-25 12:00` | `2026-08-26 10:00` | 22.0h | `$2.1046` | `$2.2070` | **+4.86%** | **+4.75%** | +6.7% | -6.1% | `target_reclaim` |
| 3 | Book 3 | `2026-10-01 22:00` | `2026-10-02 02:00` | 4.0h | `$2.0869` | `$2.2830` | **+9.40%** | **+8.98%** | +10.7% | -0.5% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+13.7%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `CVX`

* **Total Candidate Breakouts Filtered (Vetoed):** `116`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `99` (85.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `1`
* **Saved Capital Losses Avoided:** `+931.5%`
* **Missed Upside Forgone:** `-24.8%`
* **Net Veto Alpha:** `+906.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `99` | `85.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `13` | `11.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `3` | `2.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `0.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*