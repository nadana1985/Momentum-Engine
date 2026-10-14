# Kronos V12: Institutional Symbol Tear Sheet — `GOAT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`83.3%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`5.431`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+38.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.46x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+6.34%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`36.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+18.5% / -11.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2024-10-26 06:00` | `2024-10-30 06:00` | Live | `$0.7654` | `$0.8305` | **+8.50%** | **+8.16%** | +26.7% | -49.4% | `shelf_target_reclaim` |
| 2 | Book 3 | `2025-04-23 16:00` | `2025-04-23 17:00` | 1.0h | `$0.0634` | `$0.0660` | **+4.17%** | **+4.08%** | +7.7% | -0.2% | `target_reclaim` |
| 3 | Book 3 | `2025-04-29 04:00` | `2025-04-29 10:00` | 6.0h | `$0.0915` | `$0.0839` | **-8.23%** | **-8.59%** | +5.2% | -9.0% | `stop_loss` |
| 4 | Book 3 | `2025-10-27 09:00` | `2025-10-27 17:00` | 8.0h | `$0.0556` | `$0.0581` | **+4.37%** | **+4.28%** | +4.5% | -0.9% | `target_reclaim` |
| 5 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0135` | `$0.0155` | **+14.99%** | **+13.96%** | +36.6% | -6.3% | `target_reclaim` |
| 6 | Book 2 | `2026-09-18 22:00` | `2026-09-25 22:00` | 168.0h | `$0.0169` | `$0.0195` | **+17.38%** | **+16.16%** | +30.5% | -3.5% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+22.3%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_cap` | `1` | `100.0%` | **`+16.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `GOAT`

* **Total Candidate Breakouts Filtered (Vetoed):** `58`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `44` (75.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `19`
* **Saved Capital Losses Avoided:** `+722.5%`
* **Missed Upside Forgone:** `-1,046.0%`
* **Net Veto Alpha:** `+-323.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `27` | `46.6%` |
| `Core 1: Macro Bear Veto` | `25` | `43.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `6` | `10.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*