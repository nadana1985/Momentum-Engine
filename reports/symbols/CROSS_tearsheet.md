# Kronos V12: Institutional Symbol Tear Sheet — `CROSS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`75.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.218`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+19.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.21x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.76%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`86.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.3% / -5.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-09-22 19:00` | `2025-09-24 09:00` | 38.0h | `$0.2335` | `$0.2649` | **+13.41%** | **+12.58%** | +14.2% | -1.9% | `target_reclaim` |
| 2 | Book 4 | `2026-08-01 16:00` | `2026-08-14 09:00` | 305.0h | `$0.0982` | `$0.1179` | **+5.46%** | **+5.33%** | +28.7% | -7.8% | `target_reclaim` |
| 3 | Book 3 | `2026-09-16 03:00` | `2026-09-16 05:00` | 2.0h | `$0.1165` | `$0.1284` | **+10.22%** | **+9.73%** | +19.0% | -1.6% | `target_reclaim` |
| 4 | Book 3 | `2026-09-18 15:00` | `2026-09-18 17:00` | 2.0h | `$0.1402` | `$0.1287` | **-8.23%** | **-8.59%** | +3.4% | -8.6% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+27.6%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `CROSS`

* **Total Candidate Breakouts Filtered (Vetoed):** `76`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `75` (98.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `10`
* **Saved Capital Losses Avoided:** `+1,748.0%`
* **Missed Upside Forgone:** `-391.9%`
* **Net Veto Alpha:** `+1,356.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `69` | `90.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `6` | `7.9%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `1` | `1.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*