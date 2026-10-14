# Kronos V12: Institutional Symbol Tear Sheet — `A`
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
| **Cumulative Net Log Return** | **`+17.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.19x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+5.72%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`47.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.7% / -1.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-09-11 11:00` | `2026-09-13 10:00` | 47.0h | `$0.0747` | `$0.0826` | **+10.68%** | **+10.15%** | +10.9% | -0.2% | `target_reclaim` |
| 2 | Book 3 | `2026-09-23 14:00` | `2026-09-24 14:00` | 24.0h | `$0.0925` | `$0.0973` | **+5.20%** | **+5.07%** | +6.5% | -2.7% | `target_reclaim` |
| 3 | Book 3 | `2026-09-28 14:00` | `2026-10-01 14:00` | 72.0h | `$0.0926` | `$0.0944` | **+1.97%** | **+1.95%** | +8.7% | -0.6% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+15.2%`** |
| `time_expiry` | `1` | `100.0%` | **`+1.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `A`

* **Total Candidate Breakouts Filtered (Vetoed):** `57`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `36` (63.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `3`
* **Saved Capital Losses Avoided:** `+317.7%`
* **Missed Upside Forgone:** `-65.2%`
* **Net Veto Alpha:** `+252.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `26` | `45.6%` |
| `Core 1: Macro Bear Veto` | `21` | `36.8%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `8` | `14.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2` | `3.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*