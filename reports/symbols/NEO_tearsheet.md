# Kronos V12: Institutional Symbol Tear Sheet — `NEO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.446`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+63.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.89x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+10.57%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-6.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`100.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.0% / -8.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-07-31 08:00` | `2021-08-03 12:00` | 76.0h | `$48.1661` | `$40.9412` | **-11.29%** | **-12.24%** | +0.5% | -15.3% | `structural_stop` |
| 2 | Book 2 | `2023-09-20 02:00` | `2023-09-21 14:00` | 36.0h | `$7.7463` | `$7.3157` | **-5.99%** | **-6.16%** | +0.2% | -6.4% | `stall_bailout` |
| 3 | Book 4 | `2023-10-26 22:00` | `2023-11-01 18:00` | 140.0h | `$8.3906` | `$10.0687` | **+31.34%** | **+27.84%** | +22.2% | -3.7% | `target_reclaim` |
| 4 | Book 5 (Shelf Absorption Squeeze) | `2024-04-08 13:00` | `2024-04-12 13:00` | Live | `$18.0044` | `$19.5348` | **+8.50%** | **+8.16%** | +5.2% | -17.0% | `shelf_target_reclaim` |
| 5 | Book 4 | `2024-11-13 13:00` | `2024-11-17 01:00` | 84.0h | `$11.1407` | `$13.3688` | **+47.15%** | **+39.77%** | +20.6% | -3.6% | `target_reclaim` |
| 6 | Book 2 | `2026-09-20 00:00` | `2026-09-27 00:00` | 168.0h | `$2.4832` | `$2.6374` | **+6.25%** | **+6.07%** | +11.1% | -6.2% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+67.6%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stall_bailout` | `1` | `0.0%` | **`-6.2%`** |
| `structural_stop` | `1` | `0.0%` | **`-12.2%`** |
| `time_cap` | `1` | `100.0%` | **`+6.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `NEO`

* **Total Candidate Breakouts Filtered (Vetoed):** `878`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `414` (47.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `114`
* **Saved Capital Losses Avoided:** `+4,740.0%`
* **Missed Upside Forgone:** `-3,138.6%`
* **Net Veto Alpha:** `+1,601.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `433` | `49.3%` |
| `Core 0: Zero-Tolerance Data Firewall` | `342` | `39.0%` |
| `Core 1: Macro Bear Veto` | `97` | `11.0%` |
| `Core 4: Funding Rate Cap` | `5` | `0.6%` |
| `Core 4: Whale Firewall` | `1` | `0.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*