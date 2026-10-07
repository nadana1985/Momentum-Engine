# Kronos V12: Institutional Symbol Tear Sheet — `HOT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `16` (`16` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `16` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.962`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-2.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.97x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.16%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-34.9%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`31.9h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.7% / -5.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-01-14 09:00` | `2023-01-15 18:00` | 33.0h | `$0.0018` | `$0.0019` | **+8.70%** | **+8.34%** | +9.0% | -3.3% | `target_reclaim` |
| 2 | Book 3 | `2023-01-30 09:00` | `2023-01-30 19:00` | 10.0h | `$0.0021` | `$0.0020` | **-8.23%** | **-8.59%** | +1.4% | -9.6% | `stop_loss` |
| 3 | Book 3 | `2023-02-22 02:00` | `2023-02-25 02:00` | 72.0h | `$0.0022` | `$0.0020` | **-7.25%** | **-7.53%** | +3.5% | -7.8% | `time_expiry` |
| 4 | Book 3 | `2023-10-14 07:00` | `2023-10-15 19:00` | 36.0h | `$0.0011` | `$0.0012` | **+8.70%** | **+8.34%** | +11.8% | -1.9% | `target_reclaim` |
| 5 | Book 3 | `2023-11-09 16:00` | `2023-11-09 17:00` | 1.0h | `$0.0015` | `$0.0016` | **+8.70%** | **+8.34%** | +17.3% | -0.5% | `target_reclaim` |
| 6 | Book 3 | `2023-12-04 11:00` | `2023-12-04 18:00` | 7.0h | `$0.0016` | `$0.0017` | **+8.70%** | **+8.34%** | +8.8% | -1.0% | `target_reclaim` |
| 7 | Book 3 | `2024-02-28 17:00` | `2024-02-28 18:00` | 1.0h | `$0.0025` | `$0.0027` | **+8.70%** | **+8.34%** | +15.3% | -3.1% | `target_reclaim` |
| 8 | Book 3 | `2024-03-14 04:00` | `2024-03-14 19:00` | 15.0h | `$0.0043` | `$0.0040` | **-8.23%** | **-8.59%** | +3.4% | -8.6% | `stop_loss` |
| 9 | Book 3 | `2024-05-31 16:00` | `2024-06-03 13:00` | 69.0h | `$0.0024` | `$0.0026` | **+8.70%** | **+8.34%** | +8.9% | -0.3% | `target_reclaim` |
| 10 | Book 3 | `2024-06-07 18:00` | `2024-06-10 06:00` | 60.0h | `$0.0024` | `$0.0022` | **-8.23%** | **-8.59%** | +6.9% | -8.2% | `stop_loss` |
| 11 | Book 3 | `2024-08-26 14:00` | `2024-08-28 16:00` | 50.0h | `$0.0018` | `$0.0016` | **-8.23%** | **-8.59%** | +3.5% | -9.3% | `stop_loss` |
| 12 | Book 3 | `2024-10-21 06:00` | `2024-10-22 13:00` | 31.0h | `$0.0019` | `$0.0017` | **-8.23%** | **-8.59%** | +4.9% | -8.4% | `stop_loss` |
| 13 | Book 3 | `2024-11-12 10:00` | `2024-11-13 04:00` | 18.0h | `$0.0021` | `$0.0019` | **-8.23%** | **-8.59%** | +7.9% | -8.9% | `stop_loss` |
| 14 | Book 3 | `2024-12-02 08:00` | `2024-12-02 16:00` | 8.0h | `$0.0030` | `$0.0033` | **+8.70%** | **+8.34%** | +8.8% | -0.3% | `target_reclaim` |
| 15 | Book 3 | `2025-01-18 05:00` | `2025-01-19 08:00` | 27.0h | `$0.0026` | `$0.0024` | **-8.23%** | **-8.59%** | +4.1% | -9.6% | `stop_loss` |
| 16 | Book 3 | `2026-09-23 14:00` | `2026-09-26 14:00` | 72.0h | `$0.0004` | `$0.0005` | **+6.96%** | **+6.73%** | +7.6% | -4.9% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `7` | `0.0%` | **`-60.1%`** |
| `target_reclaim` | `7` | `100.0%` | **`+58.4%`** |
| `time_expiry` | `2` | `50.0%` | **`-0.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `HOT`

* **Total Candidate Breakouts Filtered (Vetoed):** `193`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `98` (50.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `35`
* **Saved Capital Losses Avoided:** `+1,176.1%`
* **Missed Upside Forgone:** `-1,017.8%`
* **Net Veto Alpha:** `+158.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `68` | `35.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `51` | `26.4%` |
| `Core 1: Macro Bear Veto` | `42` | `21.8%` |
| `Core 0: Zero-Tolerance Data Firewall` | `20` | `10.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `12` | `6.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*