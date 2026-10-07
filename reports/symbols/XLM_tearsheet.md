# Kronos V12: Institutional Symbol Tear Sheet — `XLM`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `8` (`8` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `8` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.796`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+41.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.52x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+5.24%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-14.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`121.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+14.4% / -4.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-10-07 19:00` | `2022-10-11 19:00` | 96.0h | `$0.1231` | `$0.1159` | **-5.79%** | **-5.97%** | +5.4% | -5.7% | `initial_stop` |
| 2 | Book 2 | `2023-02-15 20:00` | `2023-02-22 20:00` | 168.0h | `$0.0895` | `$0.0910` | **+1.65%** | **+1.64%** | +9.3% | -4.3% | `time_cap` |
| 3 | Book 2 | `2023-03-12 23:00` | `2023-03-19 23:00` | 168.0h | `$0.0824` | `$0.0875` | **+6.11%** | **+5.93%** | +9.2% | -2.7% | `time_cap` |
| 4 | Book 2 | `2023-06-20 18:00` | `2023-06-27 18:00` | 168.0h | `$0.0829` | `$0.1008` | **+21.56%** | **+19.52%** | +23.3% | -2.1% | `time_cap` |
| 5 | Book 2 | `2025-01-30 15:00` | `2025-02-01 19:00` | 52.0h | `$0.4356` | `$0.3998` | **-8.23%** | **-8.59%** | +1.9% | -9.0% | `initial_stop` |
| 6 | Book 2 | `2025-06-08 12:00` | `2025-06-15 12:00` | 168.0h | `$0.2714` | `$0.2566` | **-5.46%** | **-5.62%** | +5.2% | -6.9% | `time_cap` |
| 7 | Book 2 | `2025-07-06 21:00` | `2025-07-11 15:00` | 114.0h | `$0.2503` | `$0.3666` | **+46.44%** | **+38.14%** | +59.6% | -1.8% | `climax_top_harvest` |
| 8 | Book 2 | `2025-08-04 00:00` | `2025-08-05 12:00` | 36.0h | `$0.4160` | `$0.4031` | **-3.11%** | **-3.15%** | +0.8% | -4.6% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `4` | `75.0%` | **`+21.5%`** |
| `initial_stop` | `2` | `0.0%` | **`-14.6%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+38.1%`** |
| `stall_bailout` | `1` | `0.0%` | **`-3.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `XLM`

* **Total Candidate Breakouts Filtered (Vetoed):** `232`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `136` (58.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `52`
* **Saved Capital Losses Avoided:** `+1,880.6%`
* **Missed Upside Forgone:** `-2,532.1%`
* **Net Veto Alpha:** `+-651.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `109` | `47.0%` |
| `Core 1: Macro Bear Veto` | `91` | `39.2%` |
| `Core 4: Funding Rate Cap` | `25` | `10.8%` |
| `Core 4: Whale Firewall` | `5` | `2.2%` |
| `Core 4: Defensible Whale Dump` | `2` | `0.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*