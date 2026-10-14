# Kronos V12: Institutional Symbol Tear Sheet — `ZHIPU`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.219`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+2.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.03x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.67%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`54.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.4% / -10.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2026-07-21 03:00` | `2026-07-25 03:00` | Live | `$130.2168` | `$141.2852` | **+8.50%** | **+8.16%** | +20.5% | -24.4% | `shelf_target_reclaim` |
| 2 | Book 2 | `2026-08-21 06:00` | `2026-08-24 01:00` | 67.0h | `$142.7259` | `$130.9796` | **-8.55%** | **-8.92%** | +9.1% | -9.5% | `initial_stop` |
| 3 | Book 3 | `2026-08-28 18:00` | `2026-08-31 05:00` | 59.0h | `$134.6397` | `$143.9400` | **+6.91%** | **+6.68%** | +7.7% | -1.6% | `target_reclaim` |
| 4 | Book 2 | `2026-09-30 01:00` | `2026-10-01 13:00` | 36.0h | `$83.4681` | `$81.2963` | **-3.20%** | **-3.24%** | +0.3% | -5.6% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-8.9%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stall_bailout` | `1` | `0.0%` | **`-3.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+6.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `ZHIPU`

* **Total Candidate Breakouts Filtered (Vetoed):** `30`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `30` (100.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+253.1%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+253.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `29` | `96.7%` |
| `Core 1: Macro Bear Veto` | `1` | `3.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*