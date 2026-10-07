# Kronos V12: Institutional Symbol Tear Sheet — `RVN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.289`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+2.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.03x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.40%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-9.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`102.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.8% / -6.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-03-12 23:00` | `2023-03-19 23:00` | 168.0h | `$0.0242` | `$0.0274` | **+13.28%** | **+12.47%** | +21.0% | -2.8% | `time_cap` |
| 2 | Book 2 | `2026-09-13 19:00` | `2026-09-15 07:00` | 36.0h | `$0.0023` | `$0.0021` | **-9.22%** | **-9.67%** | +0.6% | -9.7% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `1` | `0.0%` | **`-9.7%`** |
| `time_cap` | `1` | `100.0%` | **`+12.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `RVN`

* **Total Candidate Breakouts Filtered (Vetoed):** `199`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `124` (62.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `37`
* **Saved Capital Losses Avoided:** `+1,656.1%`
* **Missed Upside Forgone:** `-1,223.9%`
* **Net Veto Alpha:** `+432.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `74` | `37.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `43` | `21.6%` |
| `Core 1: Macro Bear Veto` | `42` | `21.1%` |
| `Core 0: Zero-Tolerance Data Firewall` | `31` | `15.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `9` | `4.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*