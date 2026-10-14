# Kronos V12: Institutional Symbol Tear Sheet — `KAVA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `8` (`8` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `8` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`62.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.538`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+61.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.86x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+7.73%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-4.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`275.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+19.6% / -8.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-01-16 00:00` | `2021-01-22 00:00` | 144.0h | `$2.1422` | `$1.8209` | **-18.12%** | **-19.64%** | +17.8% | -19.6% | `structural_stop` |
| 2 | Book 4 | `2023-05-20 18:00` | `2023-05-23 06:00` | 60.0h | `$1.0594` | `$1.2713` | **+11.58%** | **+11.05%** | +45.7% | -4.8% | `target_reclaim` |
| 3 | Book 2 | `2023-11-06 00:00` | `2023-11-09 16:00` | 88.0h | `$0.7384` | `$0.7140` | **-3.43%** | **-3.49%** | +5.8% | -13.2% | `fast_decay_cut` |
| 4 | Book 4 | `2023-11-11 02:00` | `2023-12-11 01:00` | 719.0h | `$0.7866` | `$0.8363` | **-1.22%** | **-1.23%** | +14.1% | -12.0% | `time_expiry` |
| 5 | Book 4 | `2024-02-19 06:00` | `2024-03-02 12:00` | 294.0h | `$0.7806` | `$0.9367` | **+16.13%** | **+15.13%** | +21.0% | -4.6% | `target_reclaim` |
| 6 | Book 4 | `2024-11-17 08:00` | `2024-11-24 02:00` | 162.0h | `$0.4434` | `$0.5320` | **+33.61%** | **+29.63%** | +20.4% | -3.9% | `target_reclaim` |
| 7 | Book 1 | `2026-09-03 10:00` | `2026-09-07 17:00` | 103.0h | `$0.0503` | `$0.0603` | **+33.19%** | **+29.02%** | +21.5% | -2.9% | `target_reclaim` |
| 8 | Book 4 | `2026-09-14 13:00` | `2026-10-11 00:00` | 635.0h | `$0.0666` | `$0.0678` | **+1.36%** | **+1.35%** | +10.5% | -3.8% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+84.8%`** |
| `time_expiry` | `2` | `50.0%` | **`+0.1%`** |
| `structural_stop` | `1` | `0.0%` | **`-19.6%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-3.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `KAVA`

* **Total Candidate Breakouts Filtered (Vetoed):** `959`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `498` (51.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `149`
* **Saved Capital Losses Avoided:** `+5,966.6%`
* **Missed Upside Forgone:** `-4,324.0%`
* **Net Veto Alpha:** `+1,642.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `449` | `46.8%` |
| `Core 1: Macro Bear Veto` | `313` | `32.6%` |
| `Core 0: Zero-Tolerance Data Firewall` | `183` | `19.1%` |
| `Core 4: Funding Rate Cap` | `12` | `1.3%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.1%` |
| `Core 4: Defensible Whale Dump` | `1` | `0.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*