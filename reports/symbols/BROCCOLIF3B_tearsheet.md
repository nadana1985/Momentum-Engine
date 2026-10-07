# Kronos V12: Institutional Symbol Tear Sheet — `BROCCOLIF3B`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.254`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+13.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.15x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.78%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-2.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`21.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.9% / -4.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-11 21:00` | `2025-07-12 05:00` | 8.0h | `$0.0107` | `$0.0098` | **-8.23%** | **-8.59%** | +2.0% | -8.2% | `stop_loss` |
| 2 | Book 3 | `2025-07-18 15:00` | `2025-07-18 16:00` | 1.0h | `$0.0119` | `$0.0130` | **+8.70%** | **+8.34%** | +15.1% | -0.6% | `target_reclaim` |
| 3 | Book 3 | `2025-07-19 05:00` | `2025-07-22 05:00` | 72.0h | `$0.0123` | `$0.0120` | **-2.48%** | **-2.51%** | +8.1% | -5.1% | `time_expiry` |
| 4 | Book 3 | `2025-10-08 09:00` | `2025-10-08 10:00` | 1.0h | `$0.0166` | `$0.0180` | **+8.70%** | **+8.34%** | +24.6% | -6.3% | `target_reclaim` |
| 5 | Book 3 | `2026-09-23 15:00` | `2026-09-24 15:00` | 24.0h | `$0.0072` | `$0.0078` | **+8.70%** | **+8.34%** | +9.4% | -1.8% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+25.0%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_expiry` | `1` | `0.0%` | **`-2.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `BROCCOLIF3B`

* **Total Candidate Breakouts Filtered (Vetoed):** `26`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `23` (88.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `8`
* **Saved Capital Losses Avoided:** `+515.0%`
* **Missed Upside Forgone:** `-459.7%`
* **Net Veto Alpha:** `+55.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `19` | `73.1%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `6` | `23.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `3.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*