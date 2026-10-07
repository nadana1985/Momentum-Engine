# Kronos V12: Institutional Symbol Tear Sheet — `USUAL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`40.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.487`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-11.0%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.90x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.20%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`44.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.7% / -6.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-14 17:00` | `2025-05-15 06:00` | 13.0h | `$0.1596` | `$0.1465` | **-8.23%** | **-8.59%** | +2.4% | -9.0% | `stop_loss` |
| 2 | Book 3 | `2025-07-04 16:00` | `2025-07-07 16:00` | 72.0h | `$0.0650` | `$0.0663` | **+2.13%** | **+2.11%** | +8.5% | -2.4% | `time_expiry` |
| 3 | Book 3 | `2025-07-28 14:00` | `2025-07-29 16:00` | 26.0h | `$0.0887` | `$0.0814` | **-8.23%** | **-8.59%** | +2.4% | -8.2% | `stop_loss` |
| 4 | Book 3 | `2026-09-23 14:00` | `2026-09-25 07:00` | 41.0h | `$0.0133` | `$0.0145` | **+8.70%** | **+8.34%** | +8.8% | -5.1% | `target_reclaim` |
| 5 | Book 3 | `2026-09-29 15:00` | `2026-10-02 15:00` | 72.0h | `$0.0137` | `$0.0131` | **-4.19%** | **-4.28%** | +6.1% | -5.7% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `time_expiry` | `2` | `50.0%` | **`-2.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `USUAL`

* **Total Candidate Breakouts Filtered (Vetoed):** `47`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `28` (59.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `17`
* **Saved Capital Losses Avoided:** `+352.2%`
* **Missed Upside Forgone:** `-612.1%`
* **Net Veto Alpha:** `+-259.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `18` | `38.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `17` | `36.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `10` | `21.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2` | `4.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*