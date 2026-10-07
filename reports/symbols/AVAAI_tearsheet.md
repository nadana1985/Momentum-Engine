# Kronos V12: Institutional Symbol Tear Sheet — `AVAAI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `10` (`10` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `10` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`40.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.603`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-22.0%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.80x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.20%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-38.1%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`7.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.1% / -8.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-04-23 06:00` | `2025-04-23 16:00` | 10.0h | `$0.0425` | `$0.0390` | **-8.23%** | **-8.59%** | +13.3% | -14.6% | `stop_loss` |
| 2 | Book 3 | `2025-04-25 00:00` | `2025-04-25 07:00` | 7.0h | `$0.0473` | `$0.0514` | **+8.70%** | **+8.34%** | +13.1% | -3.1% | `target_reclaim` |
| 3 | Book 3 | `2025-04-30 12:00` | `2025-04-30 13:00` | 1.0h | `$0.0508` | `$0.0466` | **-8.23%** | **-8.59%** | +5.8% | -8.1% | `stop_loss` |
| 4 | Book 3 | `2025-05-06 20:00` | `2025-05-06 23:00` | 3.0h | `$0.0705` | `$0.0766` | **+8.70%** | **+8.34%** | +10.2% | -4.3% | `target_reclaim` |
| 5 | Book 3 | `2025-05-10 15:00` | `2025-05-10 18:00` | 3.0h | `$0.0846` | `$0.0919` | **+8.70%** | **+8.34%** | +9.0% | -1.2% | `target_reclaim` |
| 6 | Book 3 | `2025-07-07 14:00` | `2025-07-08 02:00` | 12.0h | `$0.0318` | `$0.0292` | **-8.23%** | **-8.59%** | +4.4% | -9.3% | `stop_loss` |
| 7 | Book 3 | `2025-07-11 22:00` | `2025-07-12 15:00` | 17.0h | `$0.0344` | `$0.0315` | **-8.23%** | **-8.59%** | +6.5% | -8.5% | `stop_loss` |
| 8 | Book 3 | `2025-08-11 00:00` | `2025-08-11 11:00` | 11.0h | `$0.0443` | `$0.0407` | **-8.23%** | **-8.59%** | +17.6% | -8.2% | `stop_loss` |
| 9 | Book 3 | `2026-08-21 01:00` | `2026-08-21 02:00` | 1.0h | `$0.0160` | `$0.0141` | **-11.65%** | **-12.38%** | +17.0% | -19.4% | `stop_loss` |
| 10 | Book 3 | `2026-09-16 01:00` | `2026-09-16 11:00` | 10.0h | `$0.0089` | `$0.0097` | **+8.70%** | **+8.34%** | +13.9% | -3.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `6` | `0.0%` | **`-55.3%`** |
| `target_reclaim` | `4` | `100.0%` | **`+33.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `AVAAI`

* **Total Candidate Breakouts Filtered (Vetoed):** `70`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `54` (77.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `28`
* **Saved Capital Losses Avoided:** `+1,164.3%`
* **Missed Upside Forgone:** `-1,016.0%`
* **Net Veto Alpha:** `+148.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `35` | `50.0%` |
| `Core 1: Macro Bear Veto` | `27` | `38.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `6` | `8.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `2` | `2.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*