# Kronos V12: Institutional Symbol Tear Sheet — `NXPC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`8.447`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+13.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.15x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.64%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-1.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`25.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.4% / -2.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-23 21:00` | `2025-07-23 23:00` | 2.0h | `$1.0161` | `$1.1190` | **+10.13%** | **+9.65%** | +10.7% | -1.0% | `target_reclaim` |
| 2 | Book 3 | `2025-07-24 05:00` | `2025-07-24 07:00` | 2.0h | `$1.0956` | `$1.1651` | **+6.35%** | **+6.15%** | +8.8% | -0.4% | `target_reclaim` |
| 3 | Book 3 | `2025-07-25 03:00` | `2025-07-28 03:00` | 72.0h | `$1.0956` | `$1.0753` | **-1.85%** | **-1.87%** | +2.7% | -7.4% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+15.8%`** |
| `time_expiry` | `1` | `0.0%` | **`-1.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `NXPC`

* **Total Candidate Breakouts Filtered (Vetoed):** `133`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `97` (72.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+1,150.0%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+1,150.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `119` | `89.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `7` | `5.3%` |
| `Core 3: Min Turnover Velocity` | `5` | `3.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `2` | `1.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*