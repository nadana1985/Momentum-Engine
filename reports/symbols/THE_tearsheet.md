# Kronos V12: Institutional Symbol Tear Sheet — `THE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.146`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+3.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.03x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.53%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`22.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.7% / -5.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-02-13 06:00` | `2025-02-13 08:00` | 2.0h | `$0.7878` | `$0.7230` | **-8.23%** | **-8.59%** | +7.2% | -14.2% | `stop_loss` |
| 2 | Book 3 | `2025-04-28 01:00` | `2025-04-29 00:00` | 23.0h | `$0.2658` | `$0.2889` | **+8.70%** | **+8.34%** | +8.7% | -0.1% | `target_reclaim` |
| 3 | Book 3 | `2025-05-15 01:00` | `2025-05-15 07:00` | 6.0h | `$0.3538` | `$0.3247` | **-8.23%** | **-8.59%** | +2.9% | -8.8% | `stop_loss` |
| 4 | Book 3 | `2025-09-17 10:00` | `2025-09-17 19:00` | 9.0h | `$0.3676` | `$0.3996` | **+8.70%** | **+8.34%** | +9.8% | -1.0% | `target_reclaim` |
| 5 | Book 3 | `2026-09-07 07:00` | `2026-09-08 07:00` | 24.0h | `$0.0721` | `$0.0784` | **+8.70%** | **+8.34%** | +10.1% | -0.8% | `target_reclaim` |
| 6 | Book 3 | `2026-09-28 03:00` | `2026-10-01 03:00` | 72.0h | `$0.0806` | `$0.0770` | **-4.54%** | **-4.65%** | +1.5% | -7.4% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+25.0%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `time_expiry` | `1` | `0.0%` | **`-4.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `THE`

* **Total Candidate Breakouts Filtered (Vetoed):** `54`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `37` (68.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `19`
* **Saved Capital Losses Avoided:** `+633.3%`
* **Missed Upside Forgone:** `-828.7%`
* **Net Veto Alpha:** `+-195.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `28` | `51.9%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `24` | `44.4%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `2` | `3.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*