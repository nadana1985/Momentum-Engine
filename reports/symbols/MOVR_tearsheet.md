# Kronos V12: Institutional Symbol Tear Sheet — `MOVR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`57.1%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.450`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+11.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.12x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.66%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`26.9h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.1% / -6.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-03-13 08:00` | `2024-03-14 13:00` | 29.0h | `$27.0899` | `$24.8604` | **-8.23%** | **-8.59%** | +5.5% | -9.6% | `stop_loss` |
| 2 | Book 3 | `2024-06-07 18:00` | `2024-06-08 03:00` | 9.0h | `$14.2560` | `$16.2000` | **+13.64%** | **+12.78%** | +15.1% | -1.3% | `target_reclaim` |
| 3 | Book 3 | `2024-07-23 17:00` | `2024-07-26 17:00` | 72.0h | `$10.6216` | `$10.8728` | **+2.36%** | **+2.34%** | +7.0% | -6.6% | `time_expiry` |
| 4 | Book 3 | `2024-12-05 22:00` | `2024-12-06 16:00` | 18.0h | `$18.0030` | `$20.4580` | **+13.64%** | **+12.78%** | +13.6% | -0.7% | `target_reclaim` |
| 5 | Book 3 | `2025-06-13 00:00` | `2025-06-14 20:00` | 44.0h | `$6.0711` | `$5.5715` | **-8.23%** | **-8.59%** | +2.2% | -9.2% | `stop_loss` |
| 6 | Book 3 | `2025-07-23 17:00` | `2025-07-24 06:00` | 13.0h | `$6.4583` | `$5.9268` | **-8.23%** | **-8.59%** | +2.9% | -8.8% | `stop_loss` |
| 7 | Book 2 | `2026-09-30 05:00` | `2026-09-30 08:00` | 3.0h | `$1.4255` | `$1.6702` | **+9.93%** | **+9.47%** | +38.2% | -8.4% | `trail_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `target_reclaim` | `2` | `100.0%` | **`+25.6%`** |
| `time_expiry` | `1` | `100.0%` | **`+2.3%`** |
| `trail_stop` | `1` | `100.0%` | **`+9.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `MOVR`

* **Total Candidate Breakouts Filtered (Vetoed):** `69`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `34` (49.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `8`
* **Saved Capital Losses Avoided:** `+587.6%`
* **Missed Upside Forgone:** `-231.4%`
* **Net Veto Alpha:** `+356.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `53` | `76.8%` |
| `Core 1: Macro Bear Veto` | `15` | `21.7%` |
| `Core 4: Funding Rate Cap` | `1` | `1.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*