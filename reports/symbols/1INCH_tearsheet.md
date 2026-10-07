# Kronos V12: Institutional Symbol Tear Sheet — `1INCH`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`8.577`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+36.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.45x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+6.16%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-4.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`77.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.7% / -3.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-10-25 17:00` | `2022-10-28 02:00` | 57.0h | `$0.5912` | `$0.5870` | **-0.70%** | **-0.70%** | +5.2% | -2.2% | `fast_decay_cut` |
| 2 | Book 2 | `2023-03-13 00:00` | `2023-03-20 00:00` | 168.0h | `$0.4791` | `$0.5451` | **+13.78%** | **+12.91%** | +21.5% | -3.5% | `time_cap` |
| 3 | Book 2 | `2023-07-12 00:00` | `2023-07-16 11:00` | 107.0h | `$0.3169` | `$0.4230` | **+33.50%** | **+28.89%** | +37.1% | -1.2% | `climax_top_harvest` |
| 4 | Book 2 | `2023-09-21 01:00` | `2023-09-23 01:00` | 48.0h | `$0.2648` | `$0.2632` | **-0.57%** | **-0.58%** | +5.6% | -4.3% | `fast_decay_cut` |
| 5 | Book 2 | `2023-10-16 05:00` | `2023-10-18 05:00` | 48.0h | `$0.2543` | `$0.2530` | **-0.54%** | **-0.54%** | +1.0% | -3.4% | `fast_decay_cut` |
| 6 | Book 2 | `2026-05-06 03:00` | `2026-05-07 15:00` | 36.0h | `$0.0993` | `$0.0964` | **-3.01%** | **-3.06%** | +-0.0% | -3.2% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `3` | `0.0%` | **`-1.8%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+28.9%`** |
| `stall_bailout` | `1` | `0.0%` | **`-3.1%`** |
| `time_cap` | `1` | `100.0%` | **`+12.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `1INCH`

* **Total Candidate Breakouts Filtered (Vetoed):** `310`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `174` (56.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `40`
* **Saved Capital Losses Avoided:** `+2,380.0%`
* **Missed Upside Forgone:** `-2,049.1%`
* **Net Veto Alpha:** `+330.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `99` | `31.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `91` | `29.4%` |
| `Core 0: Zero-Tolerance Data Firewall` | `69` | `22.3%` |
| `Core 1: Macro Bear Veto` | `43` | `13.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `8` | `2.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*