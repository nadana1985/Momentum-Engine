# Kronos V12: Institutional Symbol Tear Sheet — `BROCCOLI714`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `8` (`8` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `8` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`62.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.381`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+35.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.43x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.45%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`21.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.7% / -12.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-10 00:00` | `2025-05-10 10:00` | 10.0h | `$0.0400` | `$0.0367` | **-8.23%** | **-8.59%** | +18.0% | -11.2% | `stop_loss` |
| 2 | Book 4 | `2025-07-01 01:00` | `2025-07-02 10:00` | 33.0h | `$0.0364` | `$0.0436` | **+20.38%** | **+18.83%** | +21.0% | -4.7% | `target_reclaim` |
| 3 | Book 3 | `2025-07-12 15:00` | `2025-07-13 05:00` | 14.0h | `$0.0413` | `$0.0470` | **+13.69%** | **+12.83%** | +14.3% | -2.5% | `target_reclaim` |
| 4 | Book 3 | `2025-09-17 08:00` | `2025-09-18 07:00` | 23.0h | `$0.0292` | `$0.0339` | **+16.10%** | **+14.93%** | +19.1% | -4.4% | `target_reclaim` |
| 5 | Book 3 | `2025-09-18 19:00` | `2025-09-19 14:00` | 19.0h | `$0.0345` | `$0.0316` | **-8.23%** | **-8.59%** | +8.2% | -8.7% | `stop_loss` |
| 6 | Book 3 | `2025-10-07 15:00` | `2025-10-07 22:00` | 7.0h | `$0.0504` | `$0.0463` | **-8.23%** | **-8.59%** | +6.2% | -9.9% | `stop_loss` |
| 7 | Book 5 (Shelf Absorption Squeeze) | `2025-12-31 19:00` | `2026-01-04 19:00` | Live | `$0.0338` | `$0.0367` | **+8.50%** | **+8.16%** | +2.8% | -56.5% | `shelf_target_reclaim` |
| 8 | Book 4 | `2026-08-07 14:00` | `2026-08-09 07:00` | 41.0h | `$0.0154` | `$0.0185` | **+6.84%** | **+6.61%** | +20.2% | -3.5% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+53.2%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `BROCCOLI714`

* **Total Candidate Breakouts Filtered (Vetoed):** `740`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `419` (56.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `119`
* **Saved Capital Losses Avoided:** `+6,117.0%`
* **Missed Upside Forgone:** `-3,533.4%`
* **Net Veto Alpha:** `+2,583.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `433` | `58.5%` |
| `Core 1: Macro Bear Veto` | `295` | `39.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `7` | `0.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `0.5%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*