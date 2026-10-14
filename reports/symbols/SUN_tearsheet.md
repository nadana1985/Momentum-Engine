# Kronos V12: Institutional Symbol Tear Sheet — `SUN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`80.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`15.203`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+27.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.32x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+5.51%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-1.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`37.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.8% / -3.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-11-10 21:00` | `2024-11-11 00:00` | 3.0h | `$0.0187` | `$0.0195` | **+4.17%** | **+4.08%** | +5.8% | -1.3% | `target_reclaim` |
| 2 | Book 3 | `2024-11-12 10:00` | `2024-11-12 13:00` | 3.0h | `$0.0189` | `$0.0204` | **+7.76%** | **+7.48%** | +9.9% | -1.1% | `target_reclaim` |
| 3 | Book 3 | `2024-11-17 02:00` | `2024-11-20 02:00` | 72.0h | `$0.0214` | `$0.0210` | **-1.92%** | **-1.94%** | +7.3% | -1.9% | `time_expiry` |
| 4 | Book 3 | `2024-11-26 13:00` | `2024-11-29 13:00` | 72.0h | `$0.0202` | `$0.0223` | **+10.28%** | **+9.78%** | +14.1% | -0.4% | `time_expiry` |
| 5 | Book 5 (Shelf Absorption Squeeze) | `2025-09-20 04:00` | `2025-09-24 04:00` | Live | `$0.0255` | `$0.0276` | **+8.50%** | **+8.16%** | +46.7% | -14.9% | `shelf_target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+11.6%`** |
| `time_expiry` | `2` | `50.0%` | **`+7.8%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `SUN`

* **Total Candidate Breakouts Filtered (Vetoed):** `601`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `419` (69.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `13`
* **Saved Capital Losses Avoided:** `+2,356.6%`
* **Missed Upside Forgone:** `-659.9%`
* **Net Veto Alpha:** `+1,696.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `461` | `76.7%` |
| `Core 1: Macro Bear Veto` | `124` | `20.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `13` | `2.2%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `2` | `0.3%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*