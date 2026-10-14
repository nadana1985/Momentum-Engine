# Kronos V12: Institutional Symbol Tear Sheet — `1000SHIB`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `8` (`8` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `8` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`75.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.734`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+35.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.42x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.42%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-11.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`115.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+14.7% / -7.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-10-04 19:00` | `2021-10-04 20:00` | 1.0h | `$0.0126` | `$0.0151` | **+9.72%** | **+9.28%** | +22.9% | -0.2% | `target_reclaim` |
| 2 | Book 2 | `2022-10-29 08:00` | `2022-10-29 15:00` | 7.0h | `$0.0124` | `$0.0130` | **+7.00%** | **+6.80%** | +17.2% | -4.1% | `target_reclaim` |
| 3 | Book 4 | `2023-04-15 23:00` | `2023-04-20 16:00` | 113.0h | `$0.0116` | `$0.0105` | **-11.22%** | **-11.80%** | +2.7% | -11.9% | `structural_stop` |
| 4 | Book 5 (Shelf Absorption Squeeze) | `2023-08-04 12:00` | `2023-08-08 12:00` | Live | `$0.0080` | `$0.0086` | **+8.50%** | **+8.16%** | +29.3% | -17.9% | `shelf_target_reclaim` |
| 5 | Book 3 | `2023-11-05 13:00` | `2023-11-06 12:00` | 23.0h | `$0.0079` | `$0.0083` | **+4.17%** | **+4.08%** | +4.4% | -0.2% | `target_reclaim` |
| 6 | Book 3 | `2023-11-07 17:00` | `2023-11-09 02:00` | 33.0h | `$0.0080` | `$0.0084` | **+5.64%** | **+5.49%** | +6.5% | -0.2% | `target_reclaim` |
| 7 | Book 4 | `2023-11-10 01:00` | `2023-12-06 06:00` | 629.0h | `$0.0084` | `$0.0101` | **+24.06%** | **+21.93%** | +21.8% | -9.7% | `target_reclaim` |
| 8 | Book 3 | `2024-03-05 04:00` | `2024-03-05 05:00` | 1.0h | `$0.0393` | `$0.0361` | **-8.23%** | **-8.59%** | +12.8% | -11.8% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `5` | `100.0%` | **`+47.6%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `structural_stop` | `1` | `0.0%` | **`-11.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `1000SHIB`

* **Total Candidate Breakouts Filtered (Vetoed):** `786`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `457` (58.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `158`
* **Saved Capital Losses Avoided:** `+6,878.7%`
* **Missed Upside Forgone:** `-10,141.5%`
* **Net Veto Alpha:** `+-3,262.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `410` | `52.2%` |
| `Core 1: Macro Bear Veto` | `353` | `44.9%` |
| `Core 4: Funding Rate Cap` | `23` | `2.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*