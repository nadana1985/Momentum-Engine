# Kronos V12: Institutional Symbol Tear Sheet — `GLM`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.359`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+6.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.06x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.03%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`41.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.7% / -5.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-07-23 05:00` | `2024-07-24 10:00` | 29.0h | `$0.3358` | `$0.3650` | **+8.70%** | **+8.34%** | +8.8% | -3.3% | `target_reclaim` |
| 2 | Book 3 | `2024-10-01 13:00` | `2024-10-01 17:00` | 4.0h | `$0.3568` | `$0.3274` | **-8.23%** | **-8.59%** | +3.2% | -10.1% | `stop_loss` |
| 3 | Book 3 | `2024-11-14 14:00` | `2024-11-16 11:00` | 45.0h | `$0.3240` | `$0.3522` | **+8.70%** | **+8.34%** | +10.0% | -4.1% | `target_reclaim` |
| 4 | Book 3 | `2024-11-20 01:00` | `2024-11-23 01:00` | 72.0h | `$0.3548` | `$0.3752` | **+5.76%** | **+5.60%** | +6.8% | -5.5% | `time_expiry` |
| 5 | Book 3 | `2025-04-28 01:00` | `2025-05-01 01:00` | 72.0h | `$0.2664` | `$0.2693` | **+1.08%** | **+1.07%** | +6.3% | -1.9% | `time_expiry` |
| 6 | Book 3 | `2025-07-27 11:00` | `2025-07-28 13:00` | 26.0h | `$0.3178` | `$0.2916` | **-8.23%** | **-8.59%** | +5.0% | -8.1% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |
| `time_expiry` | `2` | `100.0%` | **`+6.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `GLM`

* **Total Candidate Breakouts Filtered (Vetoed):** `123`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `63` (51.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `6`
* **Saved Capital Losses Avoided:** `+750.8%`
* **Missed Upside Forgone:** `-261.5%`
* **Net Veto Alpha:** `+489.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `60` | `48.8%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `41` | `33.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `22` | `17.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*