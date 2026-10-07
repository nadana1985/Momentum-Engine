# Kronos V12: Institutional Symbol Tear Sheet — `GUN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.485`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-8.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.92x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.95%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`5.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.4% / -9.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-15 01:00` | `2025-05-15 14:00` | 13.0h | `$0.0638` | `$0.0586` | **-8.23%** | **-8.59%** | +7.2% | -13.8% | `stop_loss` |
| 2 | Book 3 | `2025-07-04 04:00` | `2025-07-04 06:00` | 2.0h | `$0.0306` | `$0.0332` | **+8.70%** | **+8.34%** | +10.1% | -0.6% | `target_reclaim` |
| 3 | Book 3 | `2026-09-20 09:00` | `2026-09-20 10:00` | 1.0h | `$0.0032` | `$0.0030` | **-8.23%** | **-8.59%** | +17.1% | -13.3% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `GUN`

* **Total Candidate Breakouts Filtered (Vetoed):** `56`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `38` (67.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `24`
* **Saved Capital Losses Avoided:** `+801.0%`
* **Missed Upside Forgone:** `-1,017.7%`
* **Net Veto Alpha:** `+-216.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `42` | `75.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `13` | `23.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `1.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*