# Kronos V12: Institutional Symbol Tear Sheet — `RUNE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `10` (`10` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `10` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`80.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`62.377`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+185.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`6.36x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+18.50%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-3.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`132.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+17.2% / -3.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2020-11-09 00:00` | `2020-11-13 21:00` | 117.0h | `$0.6085` | `$0.7302` | **+30.39%** | **+27.02%** | +22.4% | -8.3% | `target_reclaim` |
| 2 | Book 4 | `2022-03-14 06:00` | `2022-03-17 00:00` | 66.0h | `$6.8873` | `$8.2648` | **+20.26%** | **+18.72%** | +20.1% | -2.4% | `target_reclaim` |
| 3 | Book 1 | `2023-04-14 05:00` | `2023-04-15 17:00` | 36.0h | `$1.6922` | `$1.6748` | **-1.72%** | **-1.73%** | +0.3% | -4.3% | `stall_bailout` |
| 4 | Book 1 | `2023-07-01 23:00` | `2023-07-04 23:00` | 72.0h | `$1.0677` | `$1.0534` | **-1.27%** | **-1.28%** | +3.7% | -2.3% | `stagnation_bailout` |
| 5 | Book 4 | `2023-08-13 00:00` | `2023-08-15 01:00` | 49.0h | `$1.2959` | `$1.5551` | **+18.77%** | **+17.44%** | +21.1% | -1.5% | `target_reclaim` |
| 6 | Book 4 | `2024-09-21 13:00` | `2024-09-26 10:00` | 117.0h | `$4.5909` | `$5.5091` | **+11.58%** | **+11.05%** | +25.7% | -4.7% | `target_reclaim` |
| 7 | Book 1 | `2025-04-21 08:00` | `2025-05-03 07:00` | 287.0h | `$1.2501` | `$1.2808` | **+3.70%** | **+3.63%** | +18.5% | -3.7% | `trail_stop` |
| 8 | Book 1 | `2026-05-05 08:00` | `2026-05-08 11:00` | 75.0h | `$0.5512` | `$0.5972` | **+14.46%** | **+13.62%** | +8.5% | -2.0% | `target_reclaim` |
| 9 | Book 4 | `2026-09-03 15:00` | `2026-09-10 15:00` | 168.0h | `$0.4991` | `$0.4998` | **+40.84%** | **+35.15%** | +1.1% | -7.1% | `stagnation_cut` |
| 10 | Book 1 | `2026-09-20 15:00` | `2026-10-04 15:00` | 336.0h | `$0.5604` | `$0.8031` | **+79.62%** | **+61.35%** | +51.0% | -2.8% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `5` | `100.0%` | **`+87.9%`** |
| `stagnation_bailout` | `1` | `0.0%` | **`-1.3%`** |
| `stagnation_cut` | `1` | `100.0%` | **`+35.2%`** |
| `stall_bailout` | `1` | `0.0%` | **`-1.7%`** |
| `time_cap` | `1` | `100.0%` | **`+61.3%`** |
| `trail_stop` | `1` | `100.0%` | **`+3.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `RUNE`

* **Total Candidate Breakouts Filtered (Vetoed):** `1688`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `924` (54.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `427`
* **Saved Capital Losses Avoided:** `+12,042.9%`
* **Missed Upside Forgone:** `-12,844.0%`
* **Net Veto Alpha:** `+-801.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `799` | `47.3%` |
| `Core 0: Zero-Tolerance Data Firewall` | `595` | `35.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `259` | `15.3%` |
| `Core 4: Defensible Whale Dump` | `21` | `1.2%` |
| `Core 4: Whale Firewall` | `8` | `0.5%` |
| `Core 4: Funding Rate Cap` | `6` | `0.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*