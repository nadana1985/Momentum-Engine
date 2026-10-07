# Kronos V12: Institutional Symbol Tear Sheet — `BNT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+38.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.47x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+12.85%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`127.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+21.5% / -1.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-11-07 18:00` | `2023-11-09 16:00` | 46.0h | `$0.5898` | `$0.7519` | **+27.49%** | **+24.29%** | +36.9% | -2.8% | `climax_top_harvest` |
| 2 | Book 2 | `2025-04-22 15:00` | `2025-04-29 15:00` | 168.0h | `$0.4061` | `$0.4602` | **+13.33%** | **+12.51%** | +19.5% | -1.1% | `time_cap` |
| 3 | Book 2 | `2026-08-21 07:00` | `2026-08-28 07:00` | 168.0h | `$0.3166` | `$0.3222` | **+1.77%** | **+1.75%** | +8.2% | -1.4% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `2` | `100.0%` | **`+14.3%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+24.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `BNT`

* **Total Candidate Breakouts Filtered (Vetoed):** `232`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `97` (41.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `38`
* **Saved Capital Losses Avoided:** `+1,039.4%`
* **Missed Upside Forgone:** `-1,638.0%`
* **Net Veto Alpha:** `+-598.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `152` | `65.5%` |
| `Core 1: Macro Bear Veto` | `37` | `15.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `26` | `11.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `17` | `7.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*