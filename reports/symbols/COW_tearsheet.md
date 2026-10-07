# Kronos V12: Institutional Symbol Tear Sheet — `COW`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `10` (`10` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `10` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.093`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+3.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.03x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.33%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-27.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`40.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.6% / -7.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-12-09 09:00` | `2024-12-09 21:00` | 12.0h | `$0.4626` | `$0.4245` | **-8.23%** | **-8.59%** | +6.8% | -23.7% | `stop_loss` |
| 2 | Book 3 | `2024-12-17 06:00` | `2024-12-17 07:00` | 1.0h | `$0.8025` | `$0.8723` | **+8.70%** | **+8.34%** | +10.4% | -1.0% | `target_reclaim` |
| 3 | Book 3 | `2024-12-27 16:00` | `2024-12-29 03:00` | 35.0h | `$0.9819` | `$1.0673` | **+8.70%** | **+8.34%** | +9.8% | -4.4% | `target_reclaim` |
| 4 | Book 3 | `2025-04-24 08:00` | `2025-04-26 00:00` | 40.0h | `$0.2912` | `$0.3165` | **+8.70%** | **+8.34%** | +11.8% | -0.5% | `target_reclaim` |
| 5 | Book 3 | `2025-04-27 02:00` | `2025-04-30 02:00` | 72.0h | `$0.2981` | `$0.2942` | **-1.31%** | **-1.32%** | +4.2% | -5.1% | `time_expiry` |
| 6 | Book 3 | `2025-05-14 22:00` | `2025-05-16 22:00` | 48.0h | `$0.3949` | `$0.3624` | **-8.23%** | **-8.59%** | +2.3% | -8.2% | `stop_loss` |
| 7 | Book 3 | `2025-05-23 20:00` | `2025-05-25 02:00` | 30.0h | `$0.4209` | `$0.3863` | **-8.23%** | **-8.59%** | +2.2% | -10.2% | `stop_loss` |
| 8 | Book 3 | `2025-08-10 02:00` | `2025-08-11 11:00` | 33.0h | `$0.4430` | `$0.4065` | **-8.23%** | **-8.59%** | +1.5% | -9.2% | `stop_loss` |
| 9 | Book 3 | `2026-09-15 18:00` | `2026-09-18 08:00` | 62.0h | `$0.1287` | `$0.1399` | **+8.70%** | **+8.34%** | +9.4% | -2.2% | `target_reclaim` |
| 10 | Book 3 | `2026-09-27 13:00` | `2026-09-30 13:00` | 72.0h | `$0.1590` | `$0.1682` | **+5.79%** | **+5.63%** | +7.2% | -6.8% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `target_reclaim` | `4` | `100.0%` | **`+33.4%`** |
| `time_expiry` | `2` | `50.0%` | **`+4.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `COW`

* **Total Candidate Breakouts Filtered (Vetoed):** `83`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `46` (55.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `9`
* **Saved Capital Losses Avoided:** `+579.5%`
* **Missed Upside Forgone:** `-278.0%`
* **Net Veto Alpha:** `+301.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `42` | `50.6%` |
| `Core 1: Macro Bear Veto` | `28` | `33.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `12` | `14.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `1.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*