# Kronos V12: Institutional Symbol Tear Sheet — `MOODENG`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.380`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+6.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.07x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.30%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`8.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.1% / -8.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-04-23 06:00` | `2025-04-23 09:00` | 3.0h | `$0.0361` | `$0.0376` | **+4.17%** | **+4.08%** | +5.4% | -1.7% | `target_reclaim` |
| 2 | Book 4 | `2025-05-09 08:00` | `2025-05-09 16:00` | 8.0h | `$0.1275` | `$0.1530` | **+9.90%** | **+9.45%** | +20.9% | -11.7% | `target_reclaim` |
| 3 | Book 3 | `2025-06-30 12:00` | `2025-07-01 12:00` | 24.0h | `$0.1503` | `$0.1379` | **-8.23%** | **-8.59%** | +2.5% | -8.5% | `stop_loss` |
| 4 | Book 3 | `2025-07-03 06:00` | `2025-07-03 10:00` | 4.0h | `$0.2059` | `$0.1890` | **-8.23%** | **-8.59%** | +6.5% | -9.0% | `stop_loss` |
| 5 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0384` | `$0.0425` | **+10.70%** | **+10.16%** | +40.1% | -10.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+23.7%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `MOODENG`

* **Total Candidate Breakouts Filtered (Vetoed):** `384`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `303` (78.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `195`
* **Saved Capital Losses Avoided:** `+5,334.7%`
* **Missed Upside Forgone:** `-14,854.0%`
* **Net Veto Alpha:** `+-9,519.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `328` | `85.4%` |
| `Core 1: Macro Bear Veto` | `33` | `8.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `21` | `5.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2` | `0.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*