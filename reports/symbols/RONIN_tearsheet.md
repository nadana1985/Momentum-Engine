# Kronos V12: Institutional Symbol Tear Sheet — `RONIN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `11` (`11` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `11` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`54.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.033`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+1.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.01x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.13%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-24.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`23.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.0% / -8.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-03-15 02:00` | `2024-03-16 07:00` | 29.0h | `$3.9368` | `$4.2630` | **+8.29%** | **+7.96%** | +10.5% | -5.5% | `target_reclaim` |
| 2 | Book 3 | `2024-09-30 18:00` | `2024-10-01 15:00` | 21.0h | `$1.7989` | `$1.6509` | **-8.23%** | **-8.59%** | +1.7% | -8.5% | `stop_loss` |
| 3 | Book 3 | `2024-11-24 12:00` | `2024-11-24 20:00` | 8.0h | `$1.6023` | `$1.6831` | **+5.04%** | **+4.92%** | +5.8% | -2.0% | `target_reclaim` |
| 4 | Book 3 | `2024-11-26 11:00` | `2024-11-27 16:00` | 29.0h | `$1.6023` | `$1.8358` | **+14.58%** | **+13.61%** | +15.5% | -1.1% | `target_reclaim` |
| 5 | Book 3 | `2024-12-05 22:00` | `2024-12-06 18:00` | 20.0h | `$2.1596` | `$2.3474` | **+8.70%** | **+8.34%** | +8.8% | -1.1% | `target_reclaim` |
| 6 | Book 3 | `2024-12-18 20:00` | `2024-12-19 02:00` | 6.0h | `$2.2840` | `$2.0960` | **-8.23%** | **-8.59%** | +2.9% | -8.9% | `stop_loss` |
| 7 | Book 3 | `2025-05-14 08:00` | `2025-05-15 10:00` | 26.0h | `$0.7265` | `$0.6667` | **-8.23%** | **-8.59%** | +2.1% | -8.1% | `stop_loss` |
| 8 | Book 3 | `2025-08-14 12:00` | `2025-08-17 12:00` | 72.0h | `$0.5571` | `$0.5649` | **+1.40%** | **+1.39%** | +5.5% | -3.7% | `time_expiry` |
| 9 | Book 5 (Shelf Absorption Squeeze) | `2026-05-18 18:00` | `2026-05-22 18:00` | Live | `$0.1045` | `$0.1134` | **+8.50%** | **+8.16%** | +2.3% | -33.3% | `shelf_target_reclaim` |
| 10 | Book 3 | `2026-08-22 05:00` | `2026-08-23 04:00` | 23.0h | `$0.0585` | `$0.0537` | **-8.23%** | **-8.59%** | +8.7% | -8.4% | `stop_loss` |
| 11 | Book 3 | `2026-09-15 15:00` | `2026-09-15 18:00` | 3.0h | `$0.0514` | `$0.0472` | **-8.23%** | **-8.59%** | +2.0% | -10.6% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `5` | `0.0%` | **`-42.9%`** |
| `target_reclaim` | `4` | `100.0%` | **`+34.8%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `time_expiry` | `1` | `100.0%` | **`+1.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `RONIN`

* **Total Candidate Breakouts Filtered (Vetoed):** `333`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `178` (53.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `12`
* **Saved Capital Losses Avoided:** `+2,865.4%`
* **Missed Upside Forgone:** `-311.1%`
* **Net Veto Alpha:** `+2,554.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `271` | `81.4%` |
| `Core 1: Macro Bear Veto` | `53` | `15.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `8` | `2.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*