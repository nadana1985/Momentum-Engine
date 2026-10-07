# Kronos V12: Institutional Symbol Tear Sheet — `TNSR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `18` (`18` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `18` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.429`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-55.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.57x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.10%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-84.5%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`33.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.4% / -7.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-05-26 17:00` | `2024-05-27 17:00` | 24.0h | `$1.0382` | `$1.1285` | **+8.70%** | **+8.34%** | +10.3% | -5.8% | `target_reclaim` |
| 2 | Book 3 | `2024-05-28 23:00` | `2024-05-30 19:00` | 44.0h | `$1.1047` | `$1.0138` | **-8.23%** | **-8.59%** | +3.7% | -8.8% | `stop_loss` |
| 3 | Book 3 | `2024-09-28 09:00` | `2024-10-01 09:00` | 72.0h | `$0.4103` | `$0.4170` | **+1.62%** | **+1.60%** | +7.7% | -3.7% | `time_expiry` |
| 4 | Book 3 | `2024-10-25 04:00` | `2024-10-25 23:00` | 19.0h | `$0.4259` | `$0.3908` | **-8.23%** | **-8.59%** | +8.3% | -9.7% | `stop_loss` |
| 5 | Book 3 | `2024-10-27 23:00` | `2024-10-28 16:00` | 17.0h | `$0.4451` | `$0.4085` | **-8.23%** | **-8.59%** | +1.4% | -9.0% | `stop_loss` |
| 6 | Book 3 | `2024-10-30 06:00` | `2024-11-01 05:00` | 47.0h | `$0.4675` | `$0.4291` | **-8.23%** | **-8.59%** | +3.7% | -8.0% | `stop_loss` |
| 7 | Book 3 | `2024-11-12 03:00` | `2024-11-12 10:00` | 7.0h | `$0.5026` | `$0.4612` | **-8.23%** | **-8.59%** | +2.8% | -12.7% | `stop_loss` |
| 8 | Book 3 | `2024-11-14 22:00` | `2024-11-15 01:00` | 3.0h | `$0.5895` | `$0.5410` | **-8.23%** | **-8.59%** | +4.5% | -8.9% | `stop_loss` |
| 9 | Book 3 | `2024-11-16 15:00` | `2024-11-18 19:00` | 52.0h | `$0.6116` | `$0.5613` | **-8.23%** | **-8.59%** | +5.1% | -9.9% | `stop_loss` |
| 10 | Book 3 | `2025-02-01 08:00` | `2025-02-02 11:00` | 27.0h | `$0.4091` | `$0.3755` | **-8.23%** | **-8.59%** | +3.2% | -8.7% | `stop_loss` |
| 11 | Book 3 | `2025-07-04 08:00` | `2025-07-05 18:00` | 34.0h | `$0.1190` | `$0.1093` | **-8.23%** | **-8.59%** | +3.2% | -8.4% | `stop_loss` |
| 12 | Book 3 | `2025-07-15 03:00` | `2025-07-15 18:00` | 15.0h | `$0.1341` | `$0.1458` | **+8.70%** | **+8.34%** | +9.0% | -1.4% | `target_reclaim` |
| 13 | Book 3 | `2025-07-23 13:00` | `2025-07-24 06:00` | 17.0h | `$0.1456` | `$0.1337` | **-8.23%** | **-8.59%** | +4.6% | -10.1% | `stop_loss` |
| 14 | Book 3 | `2025-10-27 23:00` | `2025-10-29 18:00` | 43.0h | `$0.0620` | `$0.0569` | **-8.23%** | **-8.59%** | +3.3% | -10.4% | `stop_loss` |
| 15 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0312` | `$0.0339` | **+8.70%** | **+8.34%** | +23.5% | -10.8% | `target_reclaim` |
| 16 | Book 3 | `2026-08-31 13:00` | `2026-09-03 13:00` | 72.0h | `$0.0358` | `$0.0346` | **-3.18%** | **-3.23%** | +4.2% | -7.1% | `time_expiry` |
| 17 | Book 3 | `2026-09-23 14:00` | `2026-09-25 00:00` | 34.0h | `$0.0362` | `$0.0394` | **+8.70%** | **+8.34%** | +8.7% | -1.4% | `target_reclaim` |
| 18 | Book 3 | `2026-09-28 14:00` | `2026-10-01 14:00` | 72.0h | `$0.0379` | `$0.0406` | **+7.24%** | **+6.99%** | +8.3% | -1.4% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `11` | `0.0%` | **`-94.5%`** |
| `target_reclaim` | `4` | `100.0%` | **`+33.4%`** |
| `time_expiry` | `3` | `66.7%` | **`+5.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `TNSR`

* **Total Candidate Breakouts Filtered (Vetoed):** `96`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `76` (79.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `8`
* **Saved Capital Losses Avoided:** `+1,383.3%`
* **Missed Upside Forgone:** `-1,419.6%`
* **Net Veto Alpha:** `+-36.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `61` | `63.5%` |
| `Core 1: Macro Bear Veto` | `22` | `22.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `13` | `13.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*