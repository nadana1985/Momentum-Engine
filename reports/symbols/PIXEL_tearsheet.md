# Kronos V12: Institutional Symbol Tear Sheet — `PIXEL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `10` (`10` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `10` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.605`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+17.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.19x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.76%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-10.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`33.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.2% / -6.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-05-28 04:00` | `2024-05-28 10:00` | 6.0h | `$0.4072` | `$0.4242` | **+4.17%** | **+4.08%** | +5.2% | -1.3% | `target_reclaim` |
| 2 | Book 3 | `2024-08-26 17:00` | `2024-08-27 21:00` | 28.0h | `$0.1536` | `$0.1409` | **-8.23%** | **-8.59%** | +3.3% | -9.0% | `stop_loss` |
| 3 | Book 3 | `2024-09-18 06:00` | `2024-09-19 00:00` | 18.0h | `$0.1365` | `$0.1459` | **+6.92%** | **+6.69%** | +7.9% | -7.2% | `target_reclaim` |
| 4 | Book 3 | `2024-10-23 10:00` | `2024-10-25 23:00` | 61.0h | `$0.1675` | `$0.1537` | **-8.23%** | **-8.59%** | +7.7% | -12.6% | `stop_loss` |
| 5 | Book 3 | `2024-11-12 10:00` | `2024-11-14 08:00` | 46.0h | `$0.1847` | `$0.2039` | **+10.42%** | **+9.91%** | +10.5% | -6.3% | `target_reclaim` |
| 6 | Book 3 | `2024-12-02 08:00` | `2024-12-02 21:00` | 13.0h | `$0.2414` | `$0.2624` | **+8.70%** | **+8.34%** | +9.0% | -4.7% | `target_reclaim` |
| 7 | Book 3 | `2024-12-03 14:00` | `2024-12-03 18:00` | 4.0h | `$0.2485` | `$0.2701` | **+8.70%** | **+8.34%** | +9.2% | -1.7% | `target_reclaim` |
| 8 | Book 3 | `2025-05-15 05:00` | `2025-05-16 20:00` | 39.0h | `$0.0557` | `$0.0511` | **-8.23%** | **-8.59%** | +3.5% | -9.2% | `stop_loss` |
| 9 | Book 3 | `2025-07-18 20:00` | `2025-07-20 16:00` | 44.0h | `$0.0415` | `$0.0455` | **+9.77%** | **+9.32%** | +10.7% | -1.1% | `target_reclaim` |
| 10 | Book 3 | `2026-10-05 14:00` | `2026-10-08 14:00` | 72.0h | `$0.0061` | `$0.0059` | **-3.26%** | **-3.31%** | +5.0% | -6.7% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `6` | `100.0%` | **`+46.7%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `time_expiry` | `1` | `0.0%` | **`-3.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `PIXEL`

* **Total Candidate Breakouts Filtered (Vetoed):** `366`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `193` (52.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `19`
* **Saved Capital Losses Avoided:** `+3,628.2%`
* **Missed Upside Forgone:** `-1,038.2%`
* **Net Veto Alpha:** `+2,590.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `321` | `87.7%` |
| `Core 1: Macro Bear Veto` | `25` | `6.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `14` | `3.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `6` | `1.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*