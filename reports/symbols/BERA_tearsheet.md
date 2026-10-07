# Kronos V12: Institutional Symbol Tear Sheet — `BERA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.805`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+15.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.17x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+5.17%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`45.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.0% / -6.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-23 20:00` | `2025-07-25 03:00` | 31.0h | `$2.2898` | `$2.1013` | **-8.23%** | **-8.59%** | +8.7% | -9.1% | `stop_loss` |
| 2 | Book 3 | `2025-08-15 13:00` | `2025-08-16 22:00` | 33.0h | `$2.0830` | `$2.3670` | **+13.64%** | **+12.78%** | +14.9% | -5.1% | `target_reclaim` |
| 3 | Book 3 | `2025-09-25 17:00` | `2025-09-28 17:00` | 72.0h | `$2.4596` | `$2.7541` | **+11.97%** | **+11.31%** | +12.5% | -3.8% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+12.8%`** |
| `time_expiry` | `1` | `100.0%` | **`+11.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `BERA`

* **Total Candidate Breakouts Filtered (Vetoed):** `43`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `26` (60.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `3`
* **Saved Capital Losses Avoided:** `+433.4%`
* **Missed Upside Forgone:** `-106.4%`
* **Net Veto Alpha:** `+327.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `23` | `53.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `20` | `46.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*