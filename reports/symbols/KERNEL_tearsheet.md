# Kronos V12: Institutional Symbol Tear Sheet — `KERNEL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `9` (`9` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `9` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`77.8%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.067`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+18.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.20x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.04%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`8.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.8% / -3.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-23 03:00` | `2025-05-23 05:00` | 2.0h | `$0.2115` | `$0.2203` | **+4.17%** | **+4.08%** | +7.5% | -6.0% | `target_reclaim` |
| 2 | Book 3 | `2025-07-17 16:00` | `2025-07-18 04:00` | 12.0h | `$0.1504` | `$0.1641` | **+9.09%** | **+8.70%** | +9.8% | -0.6% | `target_reclaim` |
| 3 | Book 3 | `2025-07-24 05:00` | `2025-07-24 06:00` | 1.0h | `$0.1715` | `$0.1786` | **+4.17%** | **+4.08%** | +4.5% | -2.4% | `target_reclaim` |
| 4 | Book 3 | `2025-07-25 00:00` | `2025-07-25 03:00` | 3.0h | `$0.1774` | `$0.1628` | **-8.23%** | **-8.59%** | +13.2% | -8.2% | `stop_loss` |
| 5 | Book 3 | `2025-09-19 09:00` | `2025-09-20 15:00` | 30.0h | `$0.2108` | `$0.2196` | **+4.17%** | **+4.08%** | +4.4% | -3.8% | `target_reclaim` |
| 6 | Book 3 | `2025-09-21 12:00` | `2025-09-21 15:00` | 3.0h | `$0.2154` | `$0.2250` | **+4.45%** | **+4.35%** | +6.1% | -0.1% | `target_reclaim` |
| 7 | Book 3 | `2026-08-23 03:00` | `2026-08-23 15:00` | 12.0h | `$0.0363` | `$0.0386` | **+6.31%** | **+6.12%** | +7.8% | -1.2% | `target_reclaim` |
| 8 | Book 3 | `2026-08-27 10:00` | `2026-08-27 12:00` | 2.0h | `$0.0422` | `$0.0387` | **-8.23%** | **-8.59%** | +11.4% | -8.8% | `stop_loss` |
| 9 | Book 3 | `2026-09-20 14:00` | `2026-09-21 00:00` | 10.0h | `$0.0406` | `$0.0423` | **+4.17%** | **+4.08%** | +5.6% | -0.0% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `7` | `100.0%` | **`+35.5%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `KERNEL`

* **Total Candidate Breakouts Filtered (Vetoed):** `144`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `120` (83.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `32`
* **Saved Capital Losses Avoided:** `+1,935.6%`
* **Missed Upside Forgone:** `-878.6%`
* **Net Veto Alpha:** `+1,057.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `115` | `79.9%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `17` | `11.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `11` | `7.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `0.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*