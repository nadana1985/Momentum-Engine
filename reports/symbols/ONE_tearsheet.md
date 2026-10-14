# Kronos V12: Institutional Symbol Tear Sheet — `ONE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+103.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.81x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+17.20%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`138.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+22.5% / -4.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-09 22:00` | `2021-08-16 00:00` | 146.0h | `$0.0929` | `$0.1115` | **+11.58%** | **+11.05%** | +21.6% | -6.0% | `target_reclaim` |
| 2 | Book 2 | `2022-10-25 16:00` | `2022-11-01 16:00` | 168.0h | `$0.0174` | `$0.0187` | **+9.33%** | **+8.99%** | +17.2% | -1.6% | `time_cap` |
| 3 | Book 1 | `2023-01-11 22:00` | `2023-01-14 00:00` | 50.0h | `$0.0127` | `$0.0153` | **+29.01%** | **+25.37%** | +25.6% | -2.2% | `target_reclaim` |
| 4 | Book 2 | `2023-03-12 23:00` | `2023-03-19 23:00` | 168.0h | `$0.0180` | `$0.0217` | **+23.93%** | **+21.79%** | +28.3% | -5.8% | `time_cap` |
| 5 | Book 4 | `2023-11-04 11:00` | `2023-11-12 07:00` | 188.0h | `$0.0133` | `$0.0159` | **+11.42%** | **+10.90%** | +21.8% | -7.3% | `target_reclaim` |
| 6 | Book 1 | `2025-04-21 08:00` | `2025-04-26 01:00` | 113.0h | `$0.0117` | `$0.0141` | **+28.66%** | **+25.06%** | +20.3% | -3.7% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+72.4%`** |
| `time_cap` | `2` | `100.0%` | **`+30.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `ONE`

* **Total Candidate Breakouts Filtered (Vetoed):** `643`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `357` (55.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `136`
* **Saved Capital Losses Avoided:** `+5,095.3%`
* **Missed Upside Forgone:** `-3,648.8%`
* **Net Veto Alpha:** `+1,446.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `404` | `62.8%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `177` | `27.5%` |
| `Core 1: Macro Bear Veto` | `54` | `8.4%` |
| `Core 4: Funding Rate Cap` | `7` | `1.1%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*