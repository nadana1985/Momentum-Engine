# Kronos V12: Institutional Symbol Tear Sheet — `PUNDIX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.269`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+18.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.20x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.07%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-7.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`88.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.7% / -7.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-05-02 05:00` | `2025-05-06 05:00` | Live | `$0.4892` | `$0.5307` | **+8.50%** | **+8.16%** | +11.9% | -25.5% | `shelf_target_reclaim` |
| 2 | Book 3 | `2025-07-14 18:00` | `2025-07-15 00:00` | 6.0h | `$0.3208` | `$0.3342` | **+4.17%** | **+4.08%** | +24.3% | -1.8% | `target_reclaim` |
| 3 | Book 2 | `2026-05-05 18:00` | `2026-05-08 00:00` | 54.0h | `$0.1583` | `$0.1574` | **-0.64%** | **-0.64%** | +4.2% | -2.6% | `fast_decay_cut` |
| 4 | Book 3 | `2026-09-12 08:00` | `2026-09-12 15:00` | 7.0h | `$0.0975` | `$0.1073` | **+10.07%** | **+9.59%** | +11.5% | -0.3% | `target_reclaim` |
| 5 | Book 3 | `2026-09-13 03:00` | `2026-09-13 04:00` | 1.0h | `$0.1172` | `$0.1229` | **+4.81%** | **+4.70%** | +7.4% | -0.5% | `target_reclaim` |
| 6 | Book 4 | `2026-09-25 12:00` | `2026-10-11 00:00` | 372.0h | `$0.1233` | `$0.1158` | **-7.25%** | **-7.47%** | +5.2% | -14.6% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+18.4%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.6%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `time_expiry` | `1` | `0.0%` | **`-7.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `PUNDIX`

* **Total Candidate Breakouts Filtered (Vetoed):** `83`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `66` (79.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `2`
* **Saved Capital Losses Avoided:** `+610.7%`
* **Missed Upside Forgone:** `-64.3%`
* **Net Veto Alpha:** `+546.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `58` | `69.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `14` | `16.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `7` | `8.4%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `4` | `4.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*