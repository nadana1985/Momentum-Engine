# Kronos V12: Institutional Symbol Tear Sheet — `AR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+54.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.72x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+18.04%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`175.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+32.1% / -3.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-01-08 23:00` | `2023-01-15 23:00` | 168.0h | `$7.3002` | `$9.0792` | **+24.37%** | **+21.81%** | +30.8% | -0.9% | `time_cap` |
| 2 | Book 1 | `2023-10-30 08:00` | `2023-11-05 12:00` | 148.0h | `$5.3453` | `$6.8917` | **+27.43%** | **+24.24%** | +34.9% | -3.7% | `climax_top_harvest` |
| 3 | Book 1 | `2026-09-03 01:00` | `2026-09-11 18:00` | 209.0h | `$2.4160` | `$2.5815` | **+8.42%** | **+8.08%** | +30.6% | -4.2% | `trail_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `climax_top_harvest` | `1` | `100.0%` | **`+24.2%`** |
| `time_cap` | `1` | `100.0%` | **`+21.8%`** |
| `trail_stop` | `1` | `100.0%` | **`+8.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `AR`

* **Total Candidate Breakouts Filtered (Vetoed):** `178`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `95` (53.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `25`
* **Saved Capital Losses Avoided:** `+1,161.7%`
* **Missed Upside Forgone:** `-1,020.5%`
* **Net Veto Alpha:** `+141.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `84` | `47.2%` |
| `Core 1: Macro Bear Veto` | `79` | `44.4%` |
| `Core 0: Zero-Tolerance Data Firewall` | `8` | `4.5%` |
| `Core 4: Whale Firewall` | `4` | `2.2%` |
| `Core 4: Funding Rate Cap` | `3` | `1.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*