# Kronos V12: Institutional Symbol Tear Sheet — `B2`
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
| **Cumulative Net Log Return** | **`+25.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.28x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+8.34%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`9.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.7% / -6.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-09-26 08:00` | `2025-09-26 09:00` | 1.0h | `$0.6732` | `$0.7317` | **+8.70%** | **+8.34%** | +11.5% | -5.9% | `target_reclaim` |
| 2 | Book 3 | `2025-09-30 16:00` | `2025-10-01 17:00` | 25.0h | `$0.8229` | `$0.8945` | **+8.70%** | **+8.34%** | +25.0% | -8.0% | `target_reclaim` |
| 3 | Book 3 | `2026-09-19 09:00` | `2026-09-19 10:00` | 1.0h | `$0.7545` | `$0.8201` | **+8.70%** | **+8.34%** | +13.6% | -4.3% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+25.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `B2`

* **Total Candidate Breakouts Filtered (Vetoed):** `37`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `24` (64.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `11`
* **Saved Capital Losses Avoided:** `+459.0%`
* **Missed Upside Forgone:** `-441.9%`
* **Net Veto Alpha:** `+17.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `31` | `83.8%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `5` | `13.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `2.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*