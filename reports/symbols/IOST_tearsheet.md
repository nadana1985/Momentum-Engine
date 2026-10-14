# Kronos V12: Institutional Symbol Tear Sheet — `IOST`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `9` (`9` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `9` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`77.8%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.368`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+105.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.87x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+11.71%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-24.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`212.9h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.5% / -11.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2020-11-28 12:00` | `2020-12-23 22:00` | 610.0h | `$0.0058` | `$0.0049` | **-18.12%** | **-19.64%** | +18.6% | -18.9% | `structural_stop` |
| 2 | Book 4 | `2021-08-12 23:00` | `2021-08-22 08:00` | 225.0h | `$0.0303` | `$0.0364` | **+89.33%** | **+65.68%** | +21.8% | -4.3% | `target_reclaim` |
| 3 | Book 1 | `2023-01-11 22:00` | `2023-01-17 13:00` | 135.0h | `$0.0081` | `$0.0097` | **+23.36%** | **+20.85%** | +21.2% | -2.5% | `target_reclaim` |
| 4 | Book 5 (Shelf Absorption Squeeze) | `2023-02-20 07:00` | `2023-02-24 07:00` | Live | `$0.0122` | `$0.0133` | **+8.50%** | **+8.16%** | +3.4% | -24.3% | `shelf_target_reclaim` |
| 5 | Book 2 | `2023-03-13 00:00` | `2023-03-20 00:00` | 168.0h | `$0.0100` | `$0.0113` | **+14.00%** | **+13.16%** | +15.3% | -4.4% | `time_cap` |
| 6 | Book 2 | `2023-07-12 00:00` | `2023-07-19 00:00` | 168.0h | `$0.0087` | `$0.0089` | **+2.67%** | **+2.64%** | +10.0% | -1.8% | `time_cap` |
| 7 | Book 1 | `2023-11-08 18:00` | `2023-11-09 16:00` | 22.0h | `$0.0093` | `$0.0081` | **-22.52%** | **-24.87%** | +4.0% | -12.3% | `initial_stop` |
| 8 | Book 4 | `2024-11-18 15:00` | `2024-11-25 09:00` | 162.0h | `$0.0063` | `$0.0076` | **+36.15%** | **+31.30%** | +20.9% | -7.6% | `target_reclaim` |
| 9 | Book 5 (Shelf Absorption Squeeze) | `2026-09-07 20:00` | `2026-09-11 20:00` | Live | `$0.0009` | `$0.0010` | **+8.50%** | **+8.16%** | +24.2% | -29.2% | `shelf_target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+117.8%`** |
| `time_cap` | `2` | `100.0%` | **`+15.8%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `initial_stop` | `1` | `0.0%` | **`-24.9%`** |
| `structural_stop` | `1` | `0.0%` | **`-19.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `IOST`

* **Total Candidate Breakouts Filtered (Vetoed):** `1240`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `528` (42.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `270`
* **Saved Capital Losses Avoided:** `+6,262.9%`
* **Missed Upside Forgone:** `-8,645.8%`
* **Net Veto Alpha:** `+-2,382.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `749` | `60.4%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `415` | `33.5%` |
| `Core 1: Macro Bear Veto` | `54` | `4.4%` |
| `Core 4: Funding Rate Cap` | `11` | `0.9%` |
| `Core 4: Whale Firewall` | `9` | `0.7%` |
| `Core 4: Defensible Whale Dump` | `2` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*