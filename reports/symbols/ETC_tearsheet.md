# Kronos V12: Institutional Symbol Tear Sheet — `ETC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `13` (`13` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `13` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`69.2%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.528`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+106.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.91x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+8.21%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-11.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`164.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+17.6% / -6.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2020-11-18 08:00` | `2020-11-24 02:00` | 138.0h | `$5.8998` | `$7.0798` | **+11.58%** | **+11.05%** | +22.7% | -4.2% | `target_reclaim` |
| 2 | Book 4 | `2022-03-20 16:00` | `2022-03-22 22:00` | 54.0h | `$38.6519` | `$45.6092` | **+10.80%** | **+9.93%** | +21.2% | -6.6% | `climax_whale_euphoria_harvest` |
| 3 | Book 4 | `2022-07-23 04:00` | `2022-07-25 23:00` | 67.0h | `$27.4431` | `$23.3266` | **-7.33%** | **-7.62%** | +2.7% | -15.8% | `structural_stop` |
| 4 | Book 4 | `2023-02-02 16:00` | `2023-02-09 16:00` | 168.0h | `$23.8828` | `$22.0758` | **-4.14%** | **-4.30%** | +4.6% | -9.5% | `stagnation_cut` |
| 5 | Book 2 | `2023-03-12 23:00` | `2023-03-19 23:00` | 168.0h | `$18.7758` | `$21.0143` | **+13.18%** | **+12.45%** | +20.3% | -4.2% | `time_cap` |
| 6 | Book 2 | `2023-06-20 18:00` | `2023-06-27 18:00` | 168.0h | `$15.6200` | `$18.6413` | **+21.95%** | **+20.07%** | +26.3% | -1.2% | `time_cap` |
| 7 | Book 4 | `2023-06-30 07:00` | `2023-07-30 06:00` | 719.0h | `$20.0000` | `$18.4713` | **-9.37%** | **-9.76%** | +16.6% | -12.1% | `time_expiry` |
| 8 | Book 4 | `2023-10-31 12:00` | `2023-11-10 00:00` | 228.0h | `$17.3910` | `$20.8693` | **+16.29%** | **+15.27%** | +24.5% | -4.6% | `target_reclaim` |
| 9 | Book 3 | `2024-02-28 17:00` | `2024-02-28 18:00` | 1.0h | `$26.8349` | `$27.9530` | **+4.17%** | **+4.08%** | +16.8% | -2.7% | `target_reclaim` |
| 10 | Book 3 | `2024-03-05 19:00` | `2024-03-05 20:00` | 1.0h | `$34.8404` | `$31.9730` | **-8.23%** | **-8.59%** | +2.5% | -16.8% | `stop_loss` |
| 11 | Book 4 | `2024-11-09 22:00` | `2024-11-16 11:00` | 157.0h | `$21.3980` | `$25.6777` | **+34.82%** | **+30.14%** | +21.1% | -1.1% | `target_reclaim` |
| 12 | Book 2 | `2025-05-08 02:00` | `2025-05-15 02:00` | 168.0h | `$16.6465` | `$19.7216` | **+20.57%** | **+18.88%** | +26.2% | -1.0% | `time_cap` |
| 13 | Book 4 | `2025-07-14 03:00` | `2025-07-18 05:00` | 98.0h | `$18.9944` | `$22.7933` | **+16.18%** | **+15.17%** | +23.4% | -6.3% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `5` | `100.0%` | **`+75.7%`** |
| `time_cap` | `3` | `100.0%` | **`+51.4%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+9.9%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-4.3%`** |
| `structural_stop` | `1` | `0.0%` | **`-7.6%`** |
| `time_expiry` | `1` | `0.0%` | **`-9.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `ETC`

* **Total Candidate Breakouts Filtered (Vetoed):** `940`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `470` (50.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `176`
* **Saved Capital Losses Avoided:** `+5,956.6%`
* **Missed Upside Forgone:** `-7,673.4%`
* **Net Veto Alpha:** `+-1,716.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `486` | `51.7%` |
| `Core 1: Macro Bear Veto` | `437` | `46.5%` |
| `Core 4: Funding Rate Cap` | `17` | `1.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*