# Kronos V12: Institutional Symbol Tear Sheet — `KERNEL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`40.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.647`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-9.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.91x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.82%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`11.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.7% / -7.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-23 05:00` | `2025-05-23 11:00` | 6.0h | `$0.2027` | `$0.1860` | **-8.23%** | **-8.59%** | +9.3% | -12.1% | `stop_loss` |
| 2 | Book 3 | `2025-07-17 16:00` | `2025-07-18 04:00` | 12.0h | `$0.1510` | `$0.1641` | **+8.70%** | **+8.34%** | +9.4% | -1.0% | `target_reclaim` |
| 3 | Book 3 | `2025-07-25 02:00` | `2025-07-25 15:00` | 13.0h | `$0.1643` | `$0.1786` | **+8.70%** | **+8.34%** | +13.5% | -2.8% | `target_reclaim` |
| 4 | Book 3 | `2026-08-27 10:00` | `2026-08-27 11:00` | 1.0h | `$0.0429` | `$0.0394` | **-8.23%** | **-8.59%** | +9.6% | -9.7% | `stop_loss` |
| 5 | Book 3 | `2026-09-22 13:00` | `2026-09-23 14:00` | 25.0h | `$0.0590` | `$0.0542` | **-8.23%** | **-8.59%** | +6.5% | -13.8% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `KERNEL`

* **Total Candidate Breakouts Filtered (Vetoed):** `48`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `38` (79.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `9`
* **Saved Capital Losses Avoided:** `+662.2%`
* **Missed Upside Forgone:** `-369.4%`
* **Net Veto Alpha:** `+292.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `19` | `39.6%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `17` | `35.4%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `11` | `22.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `2.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*