# Kronos V12: Institutional Symbol Tear Sheet — `COMP`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`25.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.529`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-5.0%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.95x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.26%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-4.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`69.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+4.2% / -5.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-12-27 09:00` | `2022-12-28 21:00` | 36.0h | `$33.2930` | `$31.9001` | **-4.18%** | **-4.27%** | +0.5% | -4.6% | `stall_bailout` |
| 2 | Book 1 | `2023-01-09 14:00` | `2023-01-11 02:00` | 36.0h | `$37.0023` | `$35.7404` | **-4.68%** | **-4.79%** | +0.1% | -6.3% | `fast_decay_cut` |
| 3 | Book 2 | `2023-03-13 00:00` | `2023-03-20 00:00` | 168.0h | `$43.1877` | `$45.6955` | **+5.81%** | **+5.64%** | +12.5% | -5.6% | `time_cap` |
| 4 | Book 1 | `2023-12-25 05:00` | `2023-12-26 17:00` | 36.0h | `$59.5084` | `$58.6829` | **-1.60%** | **-1.61%** | +3.5% | -6.2% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-6.4%`** |
| `stall_bailout` | `1` | `0.0%` | **`-4.3%`** |
| `time_cap` | `1` | `100.0%` | **`+5.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `COMP`

* **Total Candidate Breakouts Filtered (Vetoed):** `245`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `158` (64.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `43`
* **Saved Capital Losses Avoided:** `+2,044.5%`
* **Missed Upside Forgone:** `-1,604.0%`
* **Net Veto Alpha:** `+440.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `113` | `46.1%` |
| `Core 1: Macro Bear Veto` | `73` | `29.8%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `55` | `22.4%` |
| `Core 4: Funding Rate Cap` | `4` | `1.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*