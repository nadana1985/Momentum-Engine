# Kronos V12: Institutional Symbol Tear Sheet — `MANA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `10` (`10` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `10` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`6.640`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+161.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`5.03x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+16.15%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-13.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`149.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.8% / -5.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-21 01:00` | `2021-08-29 23:00` | 214.0h | `$0.8651` | `$1.0381` | **+18.76%** | **+17.43%** | +21.5% | -5.8% | `target_reclaim` |
| 2 | Book 4 | `2021-10-28 16:00` | `2021-10-29 00:00` | 8.0h | `$0.8357` | `$1.0028` | **+119.64%** | **+83.00%** | +22.9% | -4.1% | `target_reclaim` |
| 3 | Book 4 | `2023-01-20 20:00` | `2023-02-13 09:00` | 565.0h | `$0.7227` | `$0.6143` | **-7.55%** | **-8.18%** | +16.8% | -15.2% | `structural_stop` |
| 4 | Book 2 | `2023-03-29 08:00` | `2023-03-30 20:00` | 36.0h | `$0.6045` | `$0.5760` | **-5.04%** | **-5.17%** | +0.4% | -6.1% | `stall_bailout` |
| 5 | Book 2 | `2023-06-20 18:00` | `2023-06-27 18:00` | 168.0h | `$0.3464` | `$0.3881` | **+14.80%** | **+13.97%** | +24.9% | -1.2% | `time_cap` |
| 6 | Book 1 | `2023-07-13 23:00` | `2023-07-15 11:00` | 36.0h | `$0.4435` | `$0.4181` | **-9.66%** | **-10.10%** | +1.1% | -10.1% | `fast_decay_cut` |
| 7 | Book 4 | `2023-11-02 00:00` | `2023-11-11 16:00` | 232.0h | `$0.3932` | `$0.4718` | **+11.38%** | **+10.77%** | +21.6% | -4.9% | `target_reclaim` |
| 8 | Book 4 | `2024-11-15 12:00` | `2024-11-16 11:00` | 23.0h | `$0.3417` | `$0.4101` | **+62.10%** | **+50.04%** | +29.6% | -3.1% | `target_reclaim` |
| 9 | Book 2 | `2026-09-13 03:00` | `2026-09-15 03:00` | 48.0h | `$0.0773` | `$0.0737` | **-5.07%** | **-5.19%** | +2.1% | -5.1% | `fast_decay_cut` |
| 10 | Book 2 | `2026-09-19 00:00` | `2026-09-26 00:00` | 168.0h | `$0.0795` | `$0.0915` | **+16.02%** | **+14.93%** | +17.4% | -1.0% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+161.2%`** |
| `fast_decay_cut` | `2` | `0.0%` | **`-15.3%`** |
| `time_cap` | `2` | `100.0%` | **`+28.9%`** |
| `structural_stop` | `1` | `0.0%` | **`-8.2%`** |
| `stall_bailout` | `1` | `0.0%` | **`-5.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `MANA`

* **Total Candidate Breakouts Filtered (Vetoed):** `1444`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `817` (56.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `326`
* **Saved Capital Losses Avoided:** `+10,664.9%`
* **Missed Upside Forgone:** `-29,981.5%`
* **Net Veto Alpha:** `+-19,316.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `720` | `49.9%` |
| `Core 0: Zero-Tolerance Data Firewall` | `642` | `44.5%` |
| `Core 1: Macro Bear Veto` | `68` | `4.7%` |
| `Core 4: Funding Rate Cap` | `14` | `1.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*