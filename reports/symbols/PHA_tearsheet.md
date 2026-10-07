# Kronos V12: Institutional Symbol Tear Sheet — `PHA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `8` (`8` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `8` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`37.5%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.583`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-17.9%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.84x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.24%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-26.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`22.9h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.5% / -6.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-15 05:00` | `2025-05-16 22:00` | 41.0h | `$0.1415` | `$0.1299` | **-8.23%** | **-8.59%** | +1.0% | -8.8% | `stop_loss` |
| 2 | Book 3 | `2025-07-15 03:00` | `2025-07-16 07:00` | 28.0h | `$0.1061` | `$0.1153` | **+8.70%** | **+8.34%** | +10.8% | -0.2% | `target_reclaim` |
| 3 | Book 3 | `2025-07-18 00:00` | `2025-07-18 01:00` | 1.0h | `$0.1078` | `$0.1171` | **+8.70%** | **+8.34%** | +11.7% | -0.7% | `target_reclaim` |
| 4 | Book 3 | `2025-07-23 17:00` | `2025-07-24 06:00` | 13.0h | `$0.1176` | `$0.1079` | **-8.23%** | **-8.59%** | +2.1% | -8.4% | `stop_loss` |
| 5 | Book 3 | `2025-09-20 02:00` | `2025-09-22 06:00` | 52.0h | `$0.1069` | `$0.0981` | **-8.23%** | **-8.59%** | +5.1% | -14.9% | `stop_loss` |
| 6 | Book 3 | `2026-09-08 13:00` | `2026-09-09 08:00` | 19.0h | `$0.0252` | `$0.0274` | **+8.70%** | **+8.34%** | +13.1% | -2.0% | `target_reclaim` |
| 7 | Book 3 | `2026-09-10 01:00` | `2026-09-11 02:00` | 25.0h | `$0.0266` | `$0.0244` | **-8.23%** | **-8.59%** | +3.9% | -8.6% | `stop_loss` |
| 8 | Book 3 | `2026-09-28 01:00` | `2026-09-28 05:00` | 4.0h | `$0.0652` | `$0.0598` | **-8.23%** | **-8.59%** | +4.3% | -9.4% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `5` | `0.0%` | **`-42.9%`** |
| `target_reclaim` | `3` | `100.0%` | **`+25.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `PHA`

* **Total Candidate Breakouts Filtered (Vetoed):** `87`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `49` (56.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `21`
* **Saved Capital Losses Avoided:** `+851.5%`
* **Missed Upside Forgone:** `-1,115.1%`
* **Net Veto Alpha:** `+-263.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `35` | `40.2%` |
| `Core 1: Macro Bear Veto` | `32` | `36.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `16` | `18.4%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `4.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*