# Kronos V12: Institutional Symbol Tear Sheet — `1000000MOG`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.971`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-0.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.13%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-25.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`13.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.3% / -5.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-04-21 17:00` | `2025-04-22 02:00` | 9.0h | `$0.4543` | `$0.4938` | **+8.70%** | **+8.34%** | +8.9% | -2.8% | `target_reclaim` |
| 2 | Book 3 | `2025-04-28 01:00` | `2025-04-28 06:00` | 5.0h | `$0.5819` | `$0.6325` | **+8.70%** | **+8.34%** | +10.6% | -0.9% | `target_reclaim` |
| 3 | Book 3 | `2025-05-11 07:00` | `2025-05-11 12:00` | 5.0h | `$1.1217` | `$1.2192` | **+8.70%** | **+8.34%** | +10.3% | -1.5% | `target_reclaim` |
| 4 | Book 3 | `2025-05-23 23:00` | `2025-05-25 15:00` | 40.0h | `$1.1897` | `$1.0917` | **-8.23%** | **-8.59%** | +2.4% | -8.1% | `stop_loss` |
| 5 | Book 3 | `2025-07-04 02:00` | `2025-07-04 16:00` | 14.0h | `$1.0295` | `$0.9448` | **-8.23%** | **-8.59%** | +2.3% | -9.8% | `stop_loss` |
| 6 | Book 3 | `2025-07-14 15:00` | `2025-07-15 01:00` | 10.0h | `$1.7221` | `$1.5803` | **-8.23%** | **-8.59%** | +3.3% | -9.3% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `target_reclaim` | `3` | `100.0%` | **`+25.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `1000000MOG`

* **Total Candidate Breakouts Filtered (Vetoed):** `98`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `58` (59.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `36`
* **Saved Capital Losses Avoided:** `+930.3%`
* **Missed Upside Forgone:** `-1,347.1%`
* **Net Veto Alpha:** `+-416.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `45` | `45.9%` |
| `Core 1: Macro Bear Veto` | `32` | `32.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `19` | `19.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2` | `2.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*