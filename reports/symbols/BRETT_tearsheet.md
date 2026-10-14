# Kronos V12: Institutional Symbol Tear Sheet — `BRETT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`57.1%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.911`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+17.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.19x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.51%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`38.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.9% / -5.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-09-19 22:00` | `2024-09-20 05:00` | 7.0h | `$0.0817` | `$0.0851` | **+4.17%** | **+4.08%** | +4.9% | -1.9% | `target_reclaim` |
| 2 | Book 3 | `2024-09-20 11:00` | `2024-09-23 11:00` | 72.0h | `$0.0826` | `$0.0809` | **-2.08%** | **-2.10%** | +3.1% | -7.7% | `time_expiry` |
| 3 | Book 3 | `2025-07-14 19:00` | `2025-07-16 14:00` | 43.0h | `$0.0538` | `$0.0608` | **+12.93%** | **+12.16%** | +13.5% | -5.6% | `target_reclaim` |
| 4 | Book 3 | `2025-07-18 20:00` | `2025-07-20 15:00` | 43.0h | `$0.0548` | `$0.0628` | **+14.63%** | **+13.66%** | +15.7% | -0.7% | `target_reclaim` |
| 5 | Book 3 | `2025-09-18 21:00` | `2025-09-19 14:00` | 17.0h | `$0.0571` | `$0.0524` | **-8.23%** | **-8.59%** | +1.9% | -8.9% | `stop_loss` |
| 6 | Book 3 | `2026-05-12 10:00` | `2026-05-14 02:00` | 40.0h | `$0.0099` | `$0.0091` | **-8.23%** | **-8.59%** | +6.8% | -9.1% | `stop_loss` |
| 7 | Book 3 | `2026-09-23 15:00` | `2026-09-25 11:00` | 44.0h | `$0.0053` | `$0.0057` | **+7.19%** | **+6.94%** | +16.2% | -3.8% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+36.8%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `time_expiry` | `1` | `0.0%` | **`-2.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `BRETT`

* **Total Candidate Breakouts Filtered (Vetoed):** `488`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `396` (81.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `50`
* **Saved Capital Losses Avoided:** `+5,992.9%`
* **Missed Upside Forgone:** `-1,361.4%`
* **Net Veto Alpha:** `+4,631.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `443` | `90.8%` |
| `Core 1: Macro Bear Veto` | `24` | `4.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `16` | `3.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `4` | `0.8%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*