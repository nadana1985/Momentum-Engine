# Kronos V12: Institutional Symbol Tear Sheet — `MOVE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.971`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-0.5%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`1.00x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.13%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`35.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.2% / -6.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-23 11:00` | `2025-07-23 20:00` | 9.0h | `$0.1762` | `$0.1617` | **-8.23%** | **-8.59%** | +1.0% | -8.8% | `stop_loss` |
| 2 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0073` | `$0.0080` | **+8.70%** | **+8.34%** | +29.9% | -5.8% | `target_reclaim` |
| 3 | Book 3 | `2026-08-28 03:00` | `2026-08-30 21:00` | 66.0h | `$0.0091` | `$0.0083` | **-8.23%** | **-8.59%** | +5.3% | -8.1% | `stop_loss` |
| 4 | Book 3 | `2026-09-23 18:00` | `2026-09-26 13:00` | 67.0h | `$0.0092` | `$0.0100` | **+8.70%** | **+8.34%** | +8.7% | -3.4% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `MOVE`

* **Total Candidate Breakouts Filtered (Vetoed):** `22`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `21` (95.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `2`
* **Saved Capital Losses Avoided:** `+337.0%`
* **Missed Upside Forgone:** `-52.9%`
* **Net Veto Alpha:** `+284.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `13` | `59.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `5` | `22.7%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `3` | `13.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `4.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*