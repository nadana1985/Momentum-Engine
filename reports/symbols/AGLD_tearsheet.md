# Kronos V12: Institutional Symbol Tear Sheet — `AGLD`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `15` (`15` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `15` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.490`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-40.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.67x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.69%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-53.9%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`18.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.2% / -7.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-10-25 16:00` | `2023-10-25 17:00` | 1.0h | `$0.9405` | `$0.8631` | **-8.23%** | **-8.59%** | +48.2% | -14.1% | `stop_loss` |
| 2 | Book 3 | `2024-03-03 07:00` | `2024-03-04 05:00` | 22.0h | `$1.5347` | `$1.6682` | **+8.70%** | **+8.34%** | +11.1% | -2.8% | `target_reclaim` |
| 3 | Book 3 | `2024-03-05 17:00` | `2024-03-05 19:00` | 2.0h | `$1.5655` | `$1.4366` | **-8.23%** | **-8.59%** | +4.2% | -18.9% | `stop_loss` |
| 4 | Book 3 | `2024-05-23 20:00` | `2024-05-24 15:00` | 19.0h | `$1.0436` | `$1.1343` | **+8.70%** | **+8.34%** | +8.9% | -1.0% | `target_reclaim` |
| 5 | Book 3 | `2024-06-07 10:00` | `2024-06-07 18:00` | 8.0h | `$1.6013` | `$1.4695` | **-8.23%** | **-8.59%** | +6.5% | -10.3% | `stop_loss` |
| 6 | Book 3 | `2024-10-22 12:00` | `2024-10-22 13:00` | 1.0h | `$1.1341` | `$1.0407` | **-8.23%** | **-8.59%** | +5.5% | -8.6% | `stop_loss` |
| 7 | Book 3 | `2024-11-12 10:00` | `2024-11-13 02:00` | 16.0h | `$1.3710` | `$1.2582` | **-8.23%** | **-8.59%** | +8.3% | -8.6% | `stop_loss` |
| 8 | Book 3 | `2024-11-13 08:00` | `2024-11-13 10:00` | 2.0h | `$2.4502` | `$2.2486` | **-8.23%** | **-8.59%** | +12.7% | -12.6% | `stop_loss` |
| 9 | Book 3 | `2024-12-23 00:00` | `2024-12-23 02:00` | 2.0h | `$1.5816` | `$1.4514` | **-8.23%** | **-8.59%** | +2.9% | -8.9% | `stop_loss` |
| 10 | Book 3 | `2024-12-28 00:00` | `2024-12-28 08:00` | 8.0h | `$1.9729` | `$1.8106` | **-8.23%** | **-8.59%** | +5.2% | -8.4% | `stop_loss` |
| 11 | Book 3 | `2025-05-12 14:00` | `2025-05-14 05:00` | 39.0h | `$1.0311` | `$1.1208` | **+8.70%** | **+8.34%** | +9.9% | -6.6% | `target_reclaim` |
| 12 | Book 3 | `2025-05-15 01:00` | `2025-05-15 14:00` | 13.0h | `$1.0391` | `$0.9536` | **-8.23%** | **-8.59%** | +3.4% | -8.4% | `stop_loss` |
| 13 | Book 3 | `2025-06-06 01:00` | `2025-06-09 01:00` | 72.0h | `$0.8067` | `$0.7917` | **-1.86%** | **-1.88%** | +3.4% | -5.4% | `time_expiry` |
| 14 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.1607` | `$0.1747` | **+8.70%** | **+8.34%** | +16.5% | -0.3% | `target_reclaim` |
| 15 | Book 3 | `2026-09-15 07:00` | `2026-09-18 07:00` | 72.0h | `$0.1696` | `$0.1792` | **+5.60%** | **+5.45%** | +6.0% | -4.2% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `9` | `0.0%` | **`-77.3%`** |
| `target_reclaim` | `4` | `100.0%` | **`+33.4%`** |
| `time_expiry` | `2` | `50.0%` | **`+3.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `AGLD`

* **Total Candidate Breakouts Filtered (Vetoed):** `181`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `123` (68.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `28`
* **Saved Capital Losses Avoided:** `+1,843.7%`
* **Missed Upside Forgone:** `-1,395.2%`
* **Net Veto Alpha:** `+448.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `76` | `42.0%` |
| `Core 1: Macro Bear Veto` | `52` | `28.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `32` | `17.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `21` | `11.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*