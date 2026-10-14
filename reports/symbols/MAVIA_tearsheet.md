# Kronos V12: Institutional Symbol Tear Sheet — `MAVIA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`80.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.682`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+23.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.26x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.61%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`23.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+22.8% / -12.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-14 17:00` | `2025-07-17 17:00` | 72.0h | `$0.1729` | `$0.1813` | **+4.90%** | **+4.78%** | +10.7% | -1.9% | `time_expiry` |
| 2 | Book 3 | `2025-08-11 22:00` | `2025-08-12 17:00` | 19.0h | `$0.1846` | `$0.1979` | **+7.20%** | **+6.95%** | +14.6% | -8.6% | `target_reclaim` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2025-10-26 11:00` | `2025-10-30 11:00` | Live | `$0.0995` | `$0.1079` | **+8.50%** | **+8.16%** | +65.4% | -31.7% | `shelf_target_reclaim` |
| 4 | Book 3 | `2025-10-26 20:00` | `2025-10-26 21:00` | 1.0h | `$0.1431` | `$0.1609` | **+12.45%** | **+11.73%** | +16.2% | -1.2% | `target_reclaim` |
| 5 | Book 3 | `2025-10-28 09:00` | `2025-10-28 10:00` | 1.0h | `$0.2154` | `$0.1976` | **-8.23%** | **-8.59%** | +7.3% | -16.7% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+18.7%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_expiry` | `1` | `100.0%` | **`+4.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `MAVIA`

* **Total Candidate Breakouts Filtered (Vetoed):** `54`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `48` (88.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `7`
* **Saved Capital Losses Avoided:** `+1,887.3%`
* **Missed Upside Forgone:** `-258.7%`
* **Net Veto Alpha:** `+1,628.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `36` | `66.7%` |
| `Core 1: Macro Bear Veto` | `14` | `25.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `5.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `1.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*