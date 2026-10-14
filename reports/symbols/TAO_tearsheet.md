# Kronos V12: Institutional Symbol Tear Sheet — `TAO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`71.4%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.432`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+18.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.20x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.62%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-42.5%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`128.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.4% / -14.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2024-09-20 03:00` | `2024-09-23 01:00` | 70.0h | `$408.7322` | `$490.4786` | **+26.64%** | **+23.42%** | +22.5% | -3.7% | `target_reclaim` |
| 2 | Book 3 | `2024-10-09 22:00` | `2024-10-11 20:00` | 46.0h | `$566.2029` | `$634.3500` | **+12.04%** | **+11.36%** | +13.7% | -5.4% | `target_reclaim` |
| 3 | Book 4 | `2025-05-01 14:00` | `2025-05-09 07:00` | 185.0h | `$373.4193` | `$448.1031` | **+14.18%** | **+13.40%** | +20.5% | -9.2% | `target_reclaim` |
| 4 | Book 1 | `2025-07-11 04:00` | `2025-07-29 00:00` | 428.0h | `$384.3786` | `$395.8978` | **+5.61%** | **+5.49%** | +20.1% | -2.9% | `trail_stop` |
| 5 | Book 1 | `2025-09-18 18:00` | `2025-09-20 06:00` | 36.0h | `$372.6493` | `$344.9654` | **-13.50%** | **-14.32%** | +0.1% | -8.3% | `stall_bailout` |
| 6 | Book 1 | `2025-10-10 08:00` | `2025-10-10 21:00` | 13.0h | `$370.8548` | `$314.4385` | **-24.88%** | **-28.22%** | +7.3% | -64.8% | `initial_stop` |
| 7 | Book 4 | `2026-03-19 22:00` | `2026-03-24 20:00` | 118.0h | `$275.0720` | `$330.0864` | **+7.47%** | **+7.24%** | +23.2% | -5.4% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+55.4%`** |
| `initial_stop` | `1` | `0.0%` | **`-28.2%`** |
| `stall_bailout` | `1` | `0.0%` | **`-14.3%`** |
| `trail_stop` | `1` | `100.0%` | **`+5.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `TAO`

* **Total Candidate Breakouts Filtered (Vetoed):** `405`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `267` (65.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `68`
* **Saved Capital Losses Avoided:** `+2,429.3%`
* **Missed Upside Forgone:** `-1,940.1%`
* **Net Veto Alpha:** `+489.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `394` | `97.3%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `8` | `2.0%` |
| `Core 4: Defensible Whale Dump` | `2` | `0.5%` |
| `Core 4: Whale Firewall` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*