# Kronos V12: Institutional Symbol Tear Sheet — `AWE`
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
| **Cumulative Net Log Return** | **`+43.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.54x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+14.43%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`28.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+19.2% / -6.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-02 14:00` | `2025-07-03 00:00` | 10.0h | `$0.0642` | `$0.0672` | **+4.76%** | **+4.65%** | +16.7% | -4.5% | `target_reclaim` |
| 2 | Book 4 | `2025-09-12 06:00` | `2025-09-14 13:00` | 55.0h | `$0.0626` | `$0.0752` | **+26.26%** | **+21.58%** | +20.9% | -13.0% | `target_reclaim` |
| 3 | Book 4 | `2026-02-06 01:00` | `2026-02-06 20:00` | 19.0h | `$0.0626` | `$0.0751` | **+18.32%** | **+17.05%** | +20.1% | -0.6% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+43.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `AWE`

* **Total Candidate Breakouts Filtered (Vetoed):** `1018`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `396` (38.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `350`
* **Saved Capital Losses Avoided:** `+7,129.2%`
* **Missed Upside Forgone:** `-10,289.5%`
* **Net Veto Alpha:** `+-3,160.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `864` | `84.9%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `138` | `13.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `16` | `1.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*