# Kronos V12: Institutional Symbol Tear Sheet — `BANANAS31`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`71.4%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.719`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+29.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.34x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.22%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`100.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+24.7% / -11.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-10 09:00` | `2025-05-10 10:00` | 1.0h | `$0.0055` | `$0.0050` | **-8.23%** | **-8.59%** | +6.5% | -15.4% | `stop_loss` |
| 2 | Book 3 | `2025-05-14 15:00` | `2025-05-17 15:00` | 72.0h | `$0.0055` | `$0.0056` | **+2.07%** | **+2.04%** | +9.4% | -5.3% | `time_expiry` |
| 3 | Book 3 | `2025-07-09 22:00` | `2025-07-10 00:00` | 2.0h | `$0.0231` | `$0.0251` | **+8.70%** | **+8.34%** | +9.1% | -2.1% | `target_reclaim` |
| 4 | Book 3 | `2025-07-11 14:00` | `2025-07-11 17:00` | 3.0h | `$0.0253` | `$0.0232` | **-8.23%** | **-8.59%** | +4.2% | -10.8% | `stop_loss` |
| 5 | Book 5 (Shelf Absorption Squeeze) | `2025-11-16 19:00` | `2025-11-20 19:00` | Live | `$0.0030` | `$0.0032` | **+8.50%** | **+8.16%** | +97.3% | -31.0% | `shelf_target_reclaim` |
| 6 | Book 4 | `2026-02-10 04:00` | `2026-03-03 18:00` | 518.0h | `$0.0046` | `$0.0055` | **+26.24%** | **+23.73%** | +21.6% | -9.5% | `target_reclaim` |
| 7 | Book 4 | `2026-08-09 09:00` | `2026-08-09 18:00` | 9.0h | `$0.0083` | `$0.0100` | **+4.54%** | **+4.43%** | +25.2% | -3.4% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+36.5%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `time_expiry` | `1` | `100.0%` | **`+2.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `BANANAS31`

* **Total Candidate Breakouts Filtered (Vetoed):** `523`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `313` (59.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `85`
* **Saved Capital Losses Avoided:** `+4,308.1%`
* **Missed Upside Forgone:** `-5,181.2%`
* **Net Veto Alpha:** `+-873.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `496` | `94.8%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `17` | `3.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `5` | `1.0%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `4` | `0.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*