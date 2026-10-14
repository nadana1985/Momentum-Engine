# Kronos V12: Institutional Symbol Tear Sheet — `KOMA`
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
| **Cumulative Net Log Return** | **`+22.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.26x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+7.58%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`7.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+75.6% / -10.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2024-12-22 18:00` | `2024-12-26 18:00` | Live | `$0.1098` | `$0.1191` | **+8.50%** | **+8.16%** | +70.0% | -14.5% | `shelf_target_reclaim` |
| 2 | Book 4 | `2026-07-30 04:00` | `2026-07-30 11:00` | 7.0h | `$0.0099` | `$0.0119` | **+6.87%** | **+6.44%** | +28.9% | -5.0% | `target_reclaim` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2026-07-30 11:00` | `2026-08-03 11:00` | Live | `$0.0117` | `$0.0126` | **+8.50%** | **+8.16%** | +128.0% | -13.3% | `shelf_target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `target_reclaim` | `1` | `100.0%` | **`+6.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `KOMA`

* **Total Candidate Breakouts Filtered (Vetoed):** `420`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `242` (57.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `135`
* **Saved Capital Losses Avoided:** `+5,351.8%`
* **Missed Upside Forgone:** `-7,807.7%`
* **Net Veto Alpha:** `+-2,456.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `401` | `95.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `16` | `3.8%` |
| `Core 4: Funding Rate Cap` | `3` | `0.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*