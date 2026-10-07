# Kronos V12: Institutional Symbol Tear Sheet — `SOL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`20.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.800`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-4.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.95x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.95%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`102.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.2% / -7.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2022-11-05 00:00` | `2022-11-07 22:00` | 70.0h | `$35.0073` | `$29.6818` | **-14.17%** | **-15.28%** | +10.8% | -20.0% | `initial_stop` |
| 2 | Book 2 | `2023-10-01 10:00` | `2023-10-08 10:00` | 168.0h | `$23.1337` | `$23.1230` | **-0.06%** | **-0.06%** | +7.3% | -5.8% | `time_cap` |
| 3 | Book 2 | `2024-11-06 01:00` | `2024-11-13 01:00` | 168.0h | `$173.6330` | `$210.0536` | **+20.98%** | **+19.04%** | +30.0% | -1.2% | `time_cap` |
| 4 | Book 1 | `2025-04-20 01:00` | `2025-04-21 13:00` | 36.0h | `$142.0743` | `$136.7572` | **-4.46%** | **-4.56%** | +0.8% | -4.6% | `stall_bailout` |
| 5 | Book 1 | `2025-07-10 22:00` | `2025-07-13 22:00` | 72.0h | `$165.0616` | `$160.2883` | **-3.81%** | **-3.89%** | +1.9% | -4.5% | `stagnation_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `2` | `50.0%` | **`+19.0%`** |
| `initial_stop` | `1` | `0.0%` | **`-15.3%`** |
| `stagnation_bailout` | `1` | `0.0%` | **`-3.9%`** |
| `stall_bailout` | `1` | `0.0%` | **`-4.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `SOL`

* **Total Candidate Breakouts Filtered (Vetoed):** `284`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `141` (49.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `71`
* **Saved Capital Losses Avoided:** `+2,019.7%`
* **Missed Upside Forgone:** `-2,335.3%`
* **Net Veto Alpha:** `+-315.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `177` | `62.3%` |
| `Core 1: Macro Bear Veto` | `75` | `26.4%` |
| `Core 4: Funding Rate Cap` | `29` | `10.2%` |
| `Core 4: Defensible Whale Dump` | `3` | `1.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*