# Kronos V12: Institutional Symbol Tear Sheet — `XLM`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `15` (`15` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `15` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`8.698`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+220.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`9.04x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+14.68%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`128.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.0% / -4.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-13 00:00` | `2021-08-14 23:00` | 47.0h | `$0.3333` | `$0.4000` | **+11.58%** | **+11.05%** | +20.3% | -0.4% | `target_reclaim` |
| 2 | Book 2 | `2022-10-07 19:00` | `2022-10-11 19:00` | 96.0h | `$0.1231` | `$0.1159` | **-6.28%** | **-6.47%** | +5.4% | -5.7% | `initial_stop` |
| 3 | Book 2 | `2023-02-15 20:00` | `2023-02-22 20:00` | 168.0h | `$0.0895` | `$0.0910` | **+1.79%** | **+1.77%** | +9.3% | -4.3% | `time_cap` |
| 4 | Book 2 | `2023-03-12 23:00` | `2023-03-19 23:00` | 168.0h | `$0.0824` | `$0.0875` | **+6.75%** | **+6.55%** | +9.2% | -2.7% | `time_cap` |
| 5 | Book 4 | `2023-03-29 00:00` | `2023-04-27 23:00` | 719.0h | `$0.0997` | `$0.0941` | **-6.90%** | **-7.11%** | +14.8% | -10.5% | `time_expiry` |
| 6 | Book 2 | `2023-06-20 18:00` | `2023-06-27 18:00` | 168.0h | `$0.0829` | `$0.1008` | **+23.17%** | **+20.98%** | +23.3% | -2.1% | `time_cap` |
| 7 | Book 3 | `2024-02-17 14:00` | `2024-02-19 22:00` | 56.0h | `$0.1120` | `$0.1182` | **+5.51%** | **+5.36%** | +6.0% | -0.3% | `target_reclaim` |
| 8 | Book 3 | `2024-02-20 15:00` | `2024-02-23 15:00` | 72.0h | `$0.1152` | `$0.1143` | **-0.73%** | **-0.73%** | +3.1% | -3.7% | `time_expiry` |
| 9 | Book 3 | `2024-02-28 17:00` | `2024-02-28 22:00` | 5.0h | `$0.1166` | `$0.1214` | **+4.17%** | **+4.08%** | +7.6% | -3.8% | `target_reclaim` |
| 10 | Book 3 | `2024-03-05 19:00` | `2024-03-07 03:00` | 32.0h | `$0.1253` | `$0.1427` | **+13.93%** | **+13.04%** | +14.6% | -9.2% | `target_reclaim` |
| 11 | Book 4 | `2024-11-07 16:00` | `2024-11-12 07:00` | 111.0h | `$0.1003` | `$0.1203` | **+251.41%** | **+135.58%** | +21.5% | -0.9% | `target_reclaim` |
| 12 | Book 3 | `2024-11-16 22:00` | `2024-11-17 02:00` | 4.0h | `$0.2151` | `$0.1974` | **-8.23%** | **-8.59%** | +7.3% | -11.7% | `stop_loss` |
| 13 | Book 3 | `2024-11-24 15:00` | `2024-11-24 18:00` | 3.0h | `$0.4639` | `$0.5148` | **+10.98%** | **+10.41%** | +17.5% | -6.1% | `target_reclaim` |
| 14 | Book 2 | `2025-06-08 12:00` | `2025-06-15 12:00` | 168.0h | `$0.2714` | `$0.2566` | **-5.55%** | **-5.70%** | +5.2% | -6.9% | `time_cap` |
| 15 | Book 2 | `2025-07-06 21:00` | `2025-07-11 15:00` | 114.0h | `$0.2503` | `$0.3666` | **+48.60%** | **+39.92%** | +59.6% | -1.8% | `climax_top_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `6` | `100.0%` | **`+179.5%`** |
| `time_cap` | `4` | `75.0%` | **`+23.6%`** |
| `time_expiry` | `2` | `0.0%` | **`-7.8%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+39.9%`** |
| `initial_stop` | `1` | `0.0%` | **`-6.5%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `XLM`

* **Total Candidate Breakouts Filtered (Vetoed):** `769`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `496` (64.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `85`
* **Saved Capital Losses Avoided:** `+6,448.5%`
* **Missed Upside Forgone:** `-3,817.9%`
* **Net Veto Alpha:** `+2,630.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `466` | `60.6%` |
| `Core 1: Macro Bear Veto` | `269` | `35.0%` |
| `Core 4: Funding Rate Cap` | `25` | `3.3%` |
| `Core 4: Whale Firewall` | `5` | `0.7%` |
| `Core 4: Defensible Whale Dump` | `2` | `0.3%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `2` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*