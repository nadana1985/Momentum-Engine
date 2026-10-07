# Kronos V12: Institutional Symbol Tear Sheet — `THETA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`3.836`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+12.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.13x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.03%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-3.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`54.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.5% / -3.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-10-23 22:00` | `2023-10-26 14:00` | 64.0h | `$0.6528` | `$0.6450` | **-1.20%** | **-1.21%** | +4.3% | -3.6% | `fast_decay_cut` |
| 2 | Book 1 | `2023-11-08 09:00` | `2023-11-11 00:00` | 63.0h | `$0.8367` | `$1.0349` | **+17.78%** | **+16.37%** | +41.5% | -1.9% | `climax_top_harvest` |
| 3 | Book 2 | `2024-09-15 06:00` | `2024-09-16 18:00` | 36.0h | `$1.3457` | `$1.3051` | **-3.01%** | **-3.06%** | +0.6% | -5.3% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `climax_top_harvest` | `1` | `100.0%` | **`+16.4%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.2%`** |
| `stall_bailout` | `1` | `0.0%` | **`-3.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `THETA`

* **Total Candidate Breakouts Filtered (Vetoed):** `306`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `170` (55.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `81`
* **Saved Capital Losses Avoided:** `+2,540.0%`
* **Missed Upside Forgone:** `-2,911.5%`
* **Net Veto Alpha:** `+-371.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `150` | `49.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `87` | `28.4%` |
| `Core 1: Macro Bear Veto` | `59` | `19.3%` |
| `Core 4: Funding Rate Cap` | `10` | `3.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*