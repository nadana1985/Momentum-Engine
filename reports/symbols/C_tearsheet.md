# Kronos V12: Institutional Symbol Tear Sheet — `C`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`80.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.242`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+19.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.21x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.85%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`43.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+18.5% / -12.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2026-03-14 17:00` | `2026-03-18 17:00` | Live | `$0.0706` | `$0.0766` | **+8.50%** | **+8.16%** | +31.6% | -39.6% | `shelf_target_reclaim` |
| 2 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0670` | `$0.0672` | **+0.22%** | **+0.22%** | +11.9% | -8.1% | `time_expiry` |
| 3 | Book 3 | `2026-09-18 20:00` | `2026-09-20 02:00` | 30.0h | `$0.0671` | `$0.0778` | **+15.83%** | **+14.69%** | +18.1% | -5.7% | `target_reclaim` |
| 4 | Book 3 | `2026-09-20 07:00` | `2026-09-20 08:00` | 1.0h | `$0.0790` | `$0.0725` | **-8.23%** | **-8.59%** | +20.0% | -8.9% | `stop_loss` |
| 5 | Book 3 | `2026-10-07 11:00` | `2026-10-10 11:00` | 72.0h | `$0.0922` | `$0.0967` | **+4.89%** | **+4.78%** | +11.1% | -2.4% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_expiry` | `2` | `100.0%` | **`+5.0%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+14.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `C`

* **Total Candidate Breakouts Filtered (Vetoed):** `37`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `29` (78.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `5`
* **Saved Capital Losses Avoided:** `+526.3%`
* **Missed Upside Forgone:** `-175.5%`
* **Net Veto Alpha:** `+350.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `17` | `45.9%` |
| `Core 1: Macro Bear Veto` | `16` | `43.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `10.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*