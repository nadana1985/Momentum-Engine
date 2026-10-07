# Kronos V12: Institutional Symbol Tear Sheet — `PIPPIN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.183`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+4.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.05x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.79%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-12.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`22.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+17.0% / -11.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-04-30 03:00` | `2025-04-30 13:00` | 10.0h | `$0.0205` | `$0.0188` | **-8.23%** | **-8.59%** | +6.7% | -8.6% | `stop_loss` |
| 2 | Book 3 | `2025-07-19 21:00` | `2025-07-21 15:00` | 42.0h | `$0.0190` | `$0.0216` | **+13.64%** | **+12.78%** | +14.6% | -1.7% | `target_reclaim` |
| 3 | Book 3 | `2025-07-22 17:00` | `2025-07-23 00:00` | 7.0h | `$0.0206` | `$0.0234` | **+13.64%** | **+12.78%** | +33.5% | -7.8% | `target_reclaim` |
| 4 | Book 3 | `2025-07-23 05:00` | `2025-07-23 06:00` | 1.0h | `$0.0261` | `$0.0239` | **-8.36%** | **-8.73%** | +27.7% | -28.1% | `stop_loss` |
| 5 | Book 3 | `2025-10-01 07:00` | `2025-10-04 07:00` | 72.0h | `$0.0206` | `$0.0217` | **+5.23%** | **+5.10%** | +8.4% | -5.0% | `time_expiry` |
| 6 | Book 3 | `2025-10-25 22:00` | `2025-10-26 01:00` | 3.0h | `$0.0345` | `$0.0316` | **-8.23%** | **-8.59%** | +11.0% | -19.1% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-25.9%`** |
| `target_reclaim` | `2` | `100.0%` | **`+25.6%`** |
| `time_expiry` | `1` | `100.0%` | **`+5.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `PIPPIN`

* **Total Candidate Breakouts Filtered (Vetoed):** `66`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `58` (87.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `30`
* **Saved Capital Losses Avoided:** `+1,758.9%`
* **Missed Upside Forgone:** `-2,054.0%`
* **Net Veto Alpha:** `+-295.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `41` | `62.1%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `25` | `37.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*