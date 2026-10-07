# Kronos V12: Institutional Symbol Tear Sheet — `APT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `9` (`9` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `9` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`55.6%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.781`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+44.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.55x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+4.90%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`145.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.9% / -4.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2023-01-09 11:00` | `2023-01-12 20:00` | 81.0h | `$4.1907` | `$6.3383` | **+51.25%** | **+41.38%** | +54.7% | -2.3% | `climax_top_harvest` |
| 2 | Book 2 | `2023-07-13 16:00` | `2023-07-20 16:00` | 168.0h | `$7.3553` | `$7.4064` | **+0.69%** | **+0.69%** | +11.4% | -3.7% | `time_cap` |
| 3 | Book 2 | `2023-10-16 05:00` | `2023-10-19 01:00` | 68.0h | `$5.0125` | `$4.7730` | **-4.78%** | **-4.90%** | +4.4% | -4.6% | `initial_stop` |
| 4 | Book 1 | `2023-10-21 17:00` | `2023-11-09 16:00` | 455.0h | `$5.7975` | `$6.2743` | **+8.87%** | **+8.50%** | +33.6% | -6.0% | `trail_stop` |
| 5 | Book 1 | `2024-07-19 16:00` | `2024-07-22 16:00` | 72.0h | `$7.4205` | `$7.2698` | **-2.09%** | **-2.11%** | +3.1% | -4.8% | `stagnation_bailout` |
| 6 | Book 2 | `2025-04-24 00:00` | `2025-04-27 04:00` | 76.0h | `$5.4776` | `$5.4632` | **-0.26%** | **-0.26%** | +3.8% | -5.7% | `stagnation_cut` |
| 7 | Book 2 | `2025-05-08 15:00` | `2025-05-15 15:00` | 168.0h | `$5.1919` | `$5.5388` | **+6.68%** | **+6.47%** | +21.0% | -1.8% | `time_cap` |
| 8 | Book 2 | `2025-08-08 07:00` | `2025-08-15 07:00` | 168.0h | `$4.6617` | `$4.7995` | **+2.95%** | **+2.91%** | +10.5% | -3.9% | `time_cap` |
| 9 | Book 2 | `2025-10-26 16:00` | `2025-10-28 20:00` | 52.0h | `$3.6086` | `$3.3116` | **-8.23%** | **-8.59%** | +1.1% | -8.0% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `3` | `100.0%` | **`+10.1%`** |
| `initial_stop` | `2` | `0.0%` | **`-13.5%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+41.4%`** |
| `stagnation_bailout` | `1` | `0.0%` | **`-2.1%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-0.3%`** |
| `trail_stop` | `1` | `100.0%` | **`+8.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `APT`

* **Total Candidate Breakouts Filtered (Vetoed):** `70`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `48` (68.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `5`
* **Saved Capital Losses Avoided:** `+467.3%`
* **Missed Upside Forgone:** `-141.0%`
* **Net Veto Alpha:** `+326.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `42` | `60.0%` |
| `Core 4: Funding Rate Cap` | `18` | `25.7%` |
| `Core 0: Zero-Tolerance Data Firewall` | `5` | `7.1%` |
| `Core 4: Whale Firewall` | `3` | `4.3%` |
| `Core 4: Defensible Whale Dump` | `2` | `2.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*