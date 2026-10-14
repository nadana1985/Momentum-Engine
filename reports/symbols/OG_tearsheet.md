# Kronos V12: Institutional Symbol Tear Sheet — `OG`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`83.3%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.966`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+25.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.29x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.24%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`38.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.9% / -3.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-15 04:00` | `2025-07-15 17:00` | 13.0h | `$4.4333` | `$4.6180` | **+4.17%** | **+4.08%** | +4.5% | -0.3% | `target_reclaim` |
| 2 | Book 3 | `2025-07-24 05:00` | `2025-07-25 22:00` | 41.0h | `$4.5653` | `$5.1530` | **+12.87%** | **+12.11%** | +13.0% | -2.4% | `target_reclaim` |
| 3 | Book 3 | `2025-07-28 01:00` | `2025-07-28 09:00` | 8.0h | `$5.3472` | `$5.5700` | **+4.17%** | **+4.08%** | +4.9% | -2.5% | `target_reclaim` |
| 4 | Book 3 | `2026-05-13 14:00` | `2026-05-16 10:00` | 68.0h | `$3.3859` | `$3.1072` | **-8.23%** | **-8.59%** | +3.0% | -9.9% | `stop_loss` |
| 5 | Book 3 | `2026-08-22 05:00` | `2026-08-23 07:00` | 26.0h | `$2.6534` | `$2.8440` | **+7.18%** | **+6.94%** | +19.6% | -7.7% | `target_reclaim` |
| 6 | Book 3 | `2026-08-23 12:00` | `2026-08-26 12:00` | 72.0h | `$2.7246` | `$2.9177` | **+7.09%** | **+6.85%** | +14.3% | -0.4% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+27.2%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_expiry` | `1` | `100.0%` | **`+6.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `OG`

* **Total Candidate Breakouts Filtered (Vetoed):** `381`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `64` (16.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `145`
* **Saved Capital Losses Avoided:** `+780.3%`
* **Missed Upside Forgone:** `-7,875.9%`
* **Net Veto Alpha:** `+-7,095.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `336` | `88.2%` |
| `Core 1: Macro Bear Veto` | `40` | `10.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `1.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*