# Kronos V12: Institutional Symbol Tear Sheet — `MOVE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.394`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-10.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.90x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.47%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`33.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.7% / -8.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-21 16:00` | `2025-07-23 13:00` | 45.0h | `$0.1821` | `$0.1671` | **-8.23%** | **-8.59%** | +3.5% | -8.3% | `stop_loss` |
| 2 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0074` | `$0.0080` | **+7.01%** | **+6.77%** | +27.8% | -7.3% | `target_reclaim` |
| 3 | Book 3 | `2026-08-28 16:00` | `2026-08-30 23:00` | 55.0h | `$0.0087` | `$0.0080` | **-8.23%** | **-8.59%** | +9.7% | -9.2% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+6.8%`** |

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