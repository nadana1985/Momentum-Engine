# Kronos V12: Institutional Symbol Tear Sheet — `ALT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `11` (`11` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `11` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`36.4%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.395`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-36.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.70x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.30%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-51.8%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`15.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.9% / -7.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-03-27 08:00` | `2024-03-28 18:00` | 34.0h | `$0.6050` | `$0.6576` | **+8.70%** | **+8.34%** | +10.4% | -4.3% | `target_reclaim` |
| 2 | Book 3 | `2024-10-01 12:00` | `2024-10-01 14:00` | 2.0h | `$0.1334` | `$0.1224` | **-8.23%** | **-8.59%** | +2.0% | -8.5% | `stop_loss` |
| 3 | Book 3 | `2024-11-12 10:00` | `2024-11-13 04:00` | 18.0h | `$0.1135` | `$0.1041` | **-8.23%** | **-8.59%** | +6.2% | -8.8% | `stop_loss` |
| 4 | Book 3 | `2024-11-14 07:00` | `2024-11-14 14:00` | 7.0h | `$0.1200` | `$0.1101` | **-8.23%** | **-8.59%** | +6.6% | -8.7% | `stop_loss` |
| 5 | Book 3 | `2024-12-03 13:00` | `2024-12-03 21:00` | 8.0h | `$0.1702` | `$0.1850` | **+8.70%** | **+8.34%** | +9.2% | -4.7% | `target_reclaim` |
| 6 | Book 3 | `2025-04-29 22:00` | `2025-04-30 05:00` | 7.0h | `$0.0318` | `$0.0292` | **-8.23%** | **-8.59%** | +1.9% | -13.8% | `stop_loss` |
| 7 | Book 3 | `2025-05-15 05:00` | `2025-05-15 23:00` | 18.0h | `$0.0385` | `$0.0353` | **-8.23%** | **-8.59%** | +2.2% | -8.9% | `stop_loss` |
| 8 | Book 3 | `2025-06-16 10:00` | `2025-06-16 14:00` | 4.0h | `$0.0399` | `$0.0366` | **-8.23%** | **-8.59%** | +15.2% | -9.1% | `stop_loss` |
| 9 | Book 3 | `2025-07-11 06:00` | `2025-07-11 08:00` | 2.0h | `$0.0464` | `$0.0426` | **-8.23%** | **-8.59%** | +12.9% | -10.0% | `stop_loss` |
| 10 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0062` | `$0.0065` | **+4.17%** | **+4.08%** | +15.4% | -4.5% | `target_reclaim` |
| 11 | Book 3 | `2026-09-28 03:00` | `2026-10-01 03:00` | 72.0h | `$0.0076` | `$0.0078` | **+3.06%** | **+3.02%** | +5.1% | -3.5% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `7` | `0.0%` | **`-60.1%`** |
| `target_reclaim` | `3` | `100.0%` | **`+20.8%`** |
| `time_expiry` | `1` | `100.0%` | **`+3.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `ALT`

* **Total Candidate Breakouts Filtered (Vetoed):** `238`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `162` (68.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `15`
* **Saved Capital Losses Avoided:** `+3,385.3%`
* **Missed Upside Forgone:** `-354.6%`
* **Net Veto Alpha:** `+3,030.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `189` | `79.4%` |
| `Core 1: Macro Bear Veto` | `27` | `11.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `17` | `7.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `5` | `2.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*