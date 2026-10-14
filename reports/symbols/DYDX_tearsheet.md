# Kronos V12: Institutional Symbol Tear Sheet — `DYDX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`80.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`8.438`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+76.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.14x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+15.23%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-10.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`160.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.8% / -6.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-01-09 00:00` | `2023-01-16 00:00` | 168.0h | `$1.2862` | `$1.5182` | **+22.13%** | **+20.35%** | +23.9% | -2.7% | `time_cap` |
| 2 | Book 4 | `2023-01-26 05:00` | `2023-01-30 14:00` | 105.0h | `$2.1332` | `$2.5598` | **+28.74%** | **+25.59%** | +23.6% | -5.3% | `target_reclaim` |
| 3 | Book 4 | `2023-07-20 02:00` | `2023-07-30 20:00` | 258.0h | `$2.1692` | `$1.9940` | **-9.81%** | **-10.24%** | +6.5% | -9.2% | `structural_stop` |
| 4 | Book 5 (Shelf Absorption Squeeze) | `2023-08-23 16:00` | `2023-08-27 16:00` | Live | `$1.9587` | `$2.1252` | **+8.50%** | **+8.16%** | +9.3% | -11.6% | `shelf_target_reclaim` |
| 5 | Book 4 | `2024-11-23 07:00` | `2024-11-27 22:00` | 111.0h | `$1.4011` | `$1.6813` | **+37.06%** | **+32.29%** | +20.6% | -1.1% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+57.9%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `structural_stop` | `1` | `0.0%` | **`-10.2%`** |
| `time_cap` | `1` | `100.0%` | **`+20.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `DYDX`

* **Total Candidate Breakouts Filtered (Vetoed):** `446`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `177` (39.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `54`
* **Saved Capital Losses Avoided:** `+2,649.6%`
* **Missed Upside Forgone:** `-1,851.2%`
* **Net Veto Alpha:** `+798.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `340` | `76.2%` |
| `Core 1: Macro Bear Veto` | `84` | `18.8%` |
| `Core 0: Zero-Tolerance Data Firewall` | `11` | `2.5%` |
| `Core 4: Funding Rate Cap` | `6` | `1.3%` |
| `Core 4: Defensible Whale Dump` | `3` | `0.7%` |
| `Core 4: Whale Firewall` | `2` | `0.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*