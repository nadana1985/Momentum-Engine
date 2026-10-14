# Kronos V12: Institutional Symbol Tear Sheet — `AR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+88.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.41x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+14.67%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`123.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+20.8% / -5.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-01-08 23:00` | `2023-01-15 23:00` | 168.0h | `$7.3002` | `$9.0792` | **+30.00%** | **+26.85%** | +30.8% | -0.9% | `time_cap` |
| 2 | Book 1 | `2023-10-30 08:00` | `2023-10-30 16:00` | 8.0h | `$5.3453` | `$5.5140` | **+5.36%** | **+5.24%** | +4.7% | -3.7% | `target_reclaim` |
| 3 | Book 4 | `2023-10-30 19:00` | `2023-11-05 12:00` | 137.0h | `$5.7216` | `$6.8659` | **+23.00%** | **+21.04%** | +26.0% | -2.5% | `target_reclaim` |
| 4 | Book 5 (Shelf Absorption Squeeze) | `2023-11-18 23:00` | `2023-11-22 23:00` | Live | `$7.4529` | `$8.0864` | **+8.50%** | **+8.16%** | +10.0% | -11.9% | `shelf_target_reclaim` |
| 5 | Book 4 | `2024-11-28 01:00` | `2024-12-02 02:00` | 97.0h | `$21.9979` | `$26.3975` | **+17.67%** | **+16.48%** | +22.3% | -8.3% | `target_reclaim` |
| 6 | Book 1 | `2026-09-03 01:00` | `2026-09-11 18:00` | 209.0h | `$2.4160` | `$2.5815` | **+10.77%** | **+10.25%** | +30.6% | -4.2% | `trail_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+42.8%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `time_cap` | `1` | `100.0%` | **`+26.8%`** |
| `trail_stop` | `1` | `100.0%` | **`+10.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `AR`

* **Total Candidate Breakouts Filtered (Vetoed):** `454`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `249` (54.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `45`
* **Saved Capital Losses Avoided:** `+4,128.6%`
* **Missed Upside Forgone:** `-1,476.0%`
* **Net Veto Alpha:** `+2,652.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `343` | `75.6%` |
| `Core 1: Macro Bear Veto` | `96` | `21.1%` |
| `Core 0: Zero-Tolerance Data Firewall` | `8` | `1.8%` |
| `Core 4: Whale Firewall` | `4` | `0.9%` |
| `Core 4: Funding Rate Cap` | `3` | `0.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*