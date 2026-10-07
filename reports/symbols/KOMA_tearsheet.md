# Kronos V12: Institutional Symbol Tear Sheet — `KOMA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`83.3%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`7.442`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+55.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.74x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+9.22%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`12.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+17.7% / -4.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-02-13 03:00` | `2025-02-13 05:00` | 2.0h | `$0.0637` | `$0.0724` | **+13.64%** | **+12.78%** | +14.0% | -10.1% | `target_reclaim` |
| 2 | Book 3 | `2025-04-23 05:00` | `2025-04-23 08:00` | 3.0h | `$0.0262` | `$0.0297` | **+13.64%** | **+12.78%** | +17.0% | -0.2% | `target_reclaim` |
| 3 | Book 3 | `2025-05-09 16:00` | `2025-05-09 23:00` | 7.0h | `$0.0328` | `$0.0373` | **+13.64%** | **+12.78%** | +15.7% | -3.1% | `target_reclaim` |
| 4 | Book 3 | `2025-10-09 15:00` | `2025-10-10 15:00` | 24.0h | `$0.0235` | `$0.0216` | **-8.23%** | **-8.59%** | +10.2% | -8.6% | `stop_loss` |
| 5 | Book 3 | `2026-09-06 01:00` | `2026-09-07 10:00` | 33.0h | `$0.0145` | `$0.0165` | **+13.64%** | **+12.78%** | +31.1% | -6.1% | `target_reclaim` |
| 6 | Book 3 | `2026-09-14 13:00` | `2026-09-14 16:00` | 3.0h | `$0.0186` | `$0.0211` | **+13.64%** | **+12.78%** | +18.5% | -1.5% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `5` | `100.0%` | **`+63.9%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `KOMA`

* **Total Candidate Breakouts Filtered (Vetoed):** `46`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `39` (84.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `16`
* **Saved Capital Losses Avoided:** `+931.0%`
* **Missed Upside Forgone:** `-1,932.6%`
* **Net Veto Alpha:** `+-1,001.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `27` | `58.7%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `16` | `34.8%` |
| `Core 4: Funding Rate Cap` | `3` | `6.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*