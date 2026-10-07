# Kronos V12: Institutional Symbol Tear Sheet — `ONE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`80.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`7.359`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+54.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.73x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+10.92%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`150.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+26.1% / -4.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-10-25 16:00` | `2022-11-01 16:00` | 168.0h | `$0.0174` | `$0.0187` | **+7.58%** | **+7.30%** | +17.2% | -1.6% | `time_cap` |
| 2 | Book 1 | `2023-01-11 22:00` | `2023-01-14 14:00` | 64.0h | `$0.0127` | `$0.0172` | **+37.72%** | **+32.01%** | +43.1% | -2.2% | `climax_top_harvest` |
| 3 | Book 2 | `2023-03-12 23:00` | `2023-03-19 23:00` | 168.0h | `$0.0180` | `$0.0217` | **+20.24%** | **+18.43%** | +28.3% | -5.8% | `time_cap` |
| 4 | Book 1 | `2025-04-21 08:00` | `2025-05-03 17:00` | 297.0h | `$0.0117` | `$0.0123` | **+5.61%** | **+5.46%** | +27.9% | -3.7% | `trail_stop` |
| 5 | Book 2 | `2026-10-03 08:00` | `2026-10-05 17:00` | 57.0h | `$0.0024` | `$0.0022` | **-8.23%** | **-8.59%** | +14.0% | -8.1% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `2` | `100.0%` | **`+25.7%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+32.0%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |
| `trail_stop` | `1` | `100.0%` | **`+5.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `ONE`

* **Total Candidate Breakouts Filtered (Vetoed):** `180`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `114` (63.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `36`
* **Saved Capital Losses Avoided:** `+1,876.3%`
* **Missed Upside Forgone:** `-1,347.5%`
* **Net Veto Alpha:** `+528.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `77` | `42.8%` |
| `Core 1: Macro Bear Veto` | `53` | `29.4%` |
| `Core 0: Zero-Tolerance Data Firewall` | `43` | `23.9%` |
| `Core 4: Funding Rate Cap` | `7` | `3.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*