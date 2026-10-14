# Kronos V12: Institutional Symbol Tear Sheet — `BANANA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`71.4%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.148`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+36.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.45x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+5.27%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`50.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+18.0% / -6.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-09-26 17:00` | `2024-09-27 15:00` | 22.0h | `$40.2513` | `$43.3730` | **+7.76%** | **+7.47%** | +7.8% | -2.5% | `target_reclaim` |
| 2 | Book 3 | `2024-10-04 08:00` | `2024-10-07 08:00` | 72.0h | `$46.1146` | `$48.0360` | **+4.17%** | **+4.08%** | +7.9% | -7.6% | `target_reclaim` |
| 3 | Book 3 | `2024-10-14 12:00` | `2024-10-15 16:00` | 28.0h | `$63.3216` | `$58.1102` | **-8.23%** | **-8.59%** | +4.5% | -8.3% | `stop_loss` |
| 4 | Book 3 | `2024-11-12 10:00` | `2024-11-14 22:00` | 60.0h | `$58.3467` | `$53.5447` | **-8.23%** | **-8.59%** | +8.5% | -8.5% | `stop_loss` |
| 5 | Book 5 (Shelf Absorption Squeeze) | `2025-03-11 18:00` | `2025-03-15 18:00` | Live | `$16.9206` | `$18.3589` | **+8.50%** | **+8.16%** | +52.0% | -12.3% | `shelf_target_reclaim` |
| 6 | Book 4 | `2025-07-20 11:00` | `2025-07-20 14:00` | 3.0h | `$24.6299` | `$29.5559` | **+19.20%** | **+17.81%** | +21.0% | -0.6% | `target_reclaim` |
| 7 | Book 2 | `2026-05-05 01:00` | `2026-05-10 00:00` | 119.0h | `$4.2175` | `$4.9767` | **+18.00%** | **+16.55%** | +24.0% | -5.1% | `climax_whale_euphoria_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+29.4%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+16.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `BANANA`

* **Total Candidate Breakouts Filtered (Vetoed):** `360`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `255` (70.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `24`
* **Saved Capital Losses Avoided:** `+3,162.2%`
* **Missed Upside Forgone:** `-586.4%`
* **Net Veto Alpha:** `+2,575.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `325` | `90.3%` |
| `Core 1: Macro Bear Veto` | `22` | `6.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `8` | `2.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `4` | `1.1%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*