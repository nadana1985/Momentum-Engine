# Kronos V12: Institutional Symbol Tear Sheet — `THETA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`15.515`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+66.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.95x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+16.72%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-3.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`54.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.9% / -3.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-10-23 22:00` | `2023-10-26 14:00` | 64.0h | `$0.6528` | `$0.6450` | **-1.30%** | **-1.31%** | +4.3% | -3.6% | `fast_decay_cut` |
| 2 | Book 1 | `2023-11-08 09:00` | `2023-11-11 00:00` | 63.0h | `$0.8367` | `$1.0349` | **+26.08%** | **+23.35%** | +41.5% | -1.9% | `climax_top_harvest` |
| 3 | Book 2 | `2024-09-15 06:00` | `2024-09-16 18:00` | 36.0h | `$1.3457` | `$1.3051` | **-3.25%** | **-3.30%** | +0.6% | -5.3% | `stall_bailout` |
| 4 | Book 4 | `2024-11-16 08:00` | `2024-11-18 16:00` | 56.0h | `$1.4348` | `$1.7218` | **+60.29%** | **+48.15%** | +21.1% | -2.6% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `climax_top_harvest` | `1` | `100.0%` | **`+23.4%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.3%`** |
| `stall_bailout` | `1` | `0.0%` | **`-3.3%`** |
| `target_reclaim` | `1` | `100.0%` | **`+48.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `THETA`

* **Total Candidate Breakouts Filtered (Vetoed):** `608`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `272` (44.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `164`
* **Saved Capital Losses Avoided:** `+3,724.7%`
* **Missed Upside Forgone:** `-4,801.2%`
* **Net Veto Alpha:** `+-1,076.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `389` | `64.0%` |
| `Core 0: Zero-Tolerance Data Firewall` | `150` | `24.7%` |
| `Core 1: Macro Bear Veto` | `59` | `9.7%` |
| `Core 4: Funding Rate Cap` | `10` | `1.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*