# Kronos V12: Institutional Symbol Tear Sheet — `BLUAI`
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
| **Cumulative Net Log Return** | **`+31.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.37x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+10.45%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`215.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+30.2% / -15.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2026-03-26 11:00` | `2026-03-30 11:00` | Live | `$0.0072` | `$0.0078` | **+8.50%** | **+8.16%** | +30.0% | -27.4% | `shelf_target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2026-04-07 14:00` | `2026-04-11 14:00` | Live | `$0.0079` | `$0.0086` | **+8.50%** | **+8.16%** | +39.9% | -13.8% | `shelf_target_reclaim` |
| 3 | Book 4 | `2026-04-20 15:00` | `2026-04-29 14:00` | 215.0h | `$0.0102` | `$0.0122` | **+16.02%** | **+15.04%** | +20.6% | -6.7% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `target_reclaim` | `1` | `100.0%` | **`+15.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `BLUAI`

* **Total Candidate Breakouts Filtered (Vetoed):** `311`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `143` (46.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `84`
* **Saved Capital Losses Avoided:** `+2,460.9%`
* **Missed Upside Forgone:** `-2,240.5%`
* **Net Veto Alpha:** `+220.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `300` | `96.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `11` | `3.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*