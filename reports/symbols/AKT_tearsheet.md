# Kronos V12: Institutional Symbol Tear Sheet — `AKT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`85.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.664`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+31.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.37x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.50%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`30.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.5% / -5.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-01-07 20:00` | `2025-01-08 15:00` | 19.0h | `$3.5282` | `$3.2378` | **-8.23%** | **-8.59%** | +2.9% | -8.1% | `stop_loss` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2025-03-12 04:00` | `2025-03-16 04:00` | Live | `$1.2714` | `$1.3795` | **+8.50%** | **+8.16%** | +15.5% | -15.8% | `shelf_target_reclaim` |
| 3 | Book 3 | `2025-04-27 16:00` | `2025-04-28 10:00` | 18.0h | `$1.2096` | `$1.2600` | **+4.17%** | **+4.08%** | +4.3% | -2.9% | `target_reclaim` |
| 4 | Book 3 | `2025-04-29 22:00` | `2025-04-30 00:00` | 2.0h | `$1.2845` | `$1.3380` | **+4.17%** | **+4.08%** | +4.8% | -1.2% | `target_reclaim` |
| 5 | Book 4 | `2026-05-03 02:00` | `2026-05-08 17:00` | 135.0h | `$0.5950` | `$0.7140` | **+15.08%** | **+14.20%** | +22.5% | -3.7% | `target_reclaim` |
| 6 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.5335` | `$0.5620` | **+5.34%** | **+5.20%** | +15.3% | -2.3% | `target_reclaim` |
| 7 | Book 3 | `2026-10-05 14:00` | `2026-10-06 00:00` | 10.0h | `$0.7587` | `$0.7923` | **+4.43%** | **+4.33%** | +8.1% | -2.5% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `5` | `100.0%` | **`+31.9%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `AKT`

* **Total Candidate Breakouts Filtered (Vetoed):** `133`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `69` (51.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `17`
* **Saved Capital Losses Avoided:** `+747.4%`
* **Missed Upside Forgone:** `-430.6%`
* **Net Veto Alpha:** `+316.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `64` | `48.1%` |
| `Core 1: Macro Bear Veto` | `30` | `22.6%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `25` | `18.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `14` | `10.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*