# Kronos V12: Institutional Symbol Tear Sheet — `AGT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`80.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.668`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+22.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.26x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.58%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`121.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+47.3% / -12.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2026-03-05 08:00` | `2026-03-15 10:00` | 242.0h | `$0.0064` | `$0.0077` | **+7.26%** | **+7.03%** | +21.2% | -2.1% | `target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2026-04-25 18:00` | `2026-04-29 18:00` | Live | `$0.0138` | `$0.0150` | **+8.50%** | **+8.16%** | +46.9% | -21.6% | `shelf_target_reclaim` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2026-05-22 06:00` | `2026-05-26 06:00` | Live | `$0.0124` | `$0.0135` | **+8.50%** | **+8.16%** | +49.1% | -11.9% | `shelf_target_reclaim` |
| 4 | Book 5 (Shelf Absorption Squeeze) | `2026-06-17 10:00` | `2026-06-21 10:00` | Live | `$0.0175` | `$0.0190` | **+8.50%** | **+8.16%** | +98.5% | -21.0% | `shelf_target_reclaim` |
| 5 | Book 3 | `2026-09-22 05:00` | `2026-09-22 06:00` | 1.0h | `$0.0227` | `$0.0209` | **-8.23%** | **-8.59%** | +20.9% | -8.0% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `3` | `100.0%` | **`+24.5%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+7.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `AGT`

* **Total Candidate Breakouts Filtered (Vetoed):** `302`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `130` (43.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `16`
* **Saved Capital Losses Avoided:** `+2,578.0%`
* **Missed Upside Forgone:** `-986.8%`
* **Net Veto Alpha:** `+1,591.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `300` | `99.3%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `1` | `0.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*