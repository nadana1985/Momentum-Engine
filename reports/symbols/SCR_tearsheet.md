# Kronos V12: Institutional Symbol Tear Sheet — `SCR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `11` (`11` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `11` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`72.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.099`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+28.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.33x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.57%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-25.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`25.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.6% / -5.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-11-29 06:00` | `2024-11-30 03:00` | 21.0h | `$0.7854` | `$0.8537` | **+8.70%** | **+8.34%** | +10.6% | -0.4% | `target_reclaim` |
| 2 | Book 3 | `2024-12-05 01:00` | `2024-12-06 02:00` | 25.0h | `$0.9093` | `$0.9884` | **+8.70%** | **+8.34%** | +9.0% | -2.3% | `target_reclaim` |
| 3 | Book 3 | `2024-12-09 11:00` | `2024-12-09 21:00` | 10.0h | `$0.9636` | `$0.8843` | **-8.23%** | **-8.59%** | +6.9% | -15.1% | `stop_loss` |
| 4 | Book 3 | `2024-12-10 12:00` | `2024-12-10 15:00` | 3.0h | `$1.0341` | `$0.9490` | **-8.23%** | **-8.59%** | +9.5% | -9.6% | `stop_loss` |
| 5 | Book 3 | `2025-05-14 13:00` | `2025-05-15 05:00` | 16.0h | `$0.4170` | `$0.3827` | **-8.23%** | **-8.59%** | +2.4% | -9.7% | `stop_loss` |
| 6 | Book 3 | `2025-07-14 20:00` | `2025-07-16 00:00` | 28.0h | `$0.3304` | `$0.3591` | **+8.70%** | **+8.34%** | +8.9% | -4.8% | `target_reclaim` |
| 7 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0222` | `$0.0224` | **+0.88%** | **+0.87%** | +10.1% | -9.0% | `time_expiry` |
| 8 | Book 3 | `2026-08-28 14:00` | `2026-08-29 16:00` | 26.0h | `$0.0227` | `$0.0247` | **+8.70%** | **+8.34%** | +9.0% | -1.8% | `target_reclaim` |
| 9 | Book 3 | `2026-09-28 03:00` | `2026-10-01 03:00` | 72.0h | `$0.0242` | `$0.0250` | **+3.24%** | **+3.18%** | +5.4% | -5.5% | `time_expiry` |
| 10 | Book 3 | `2026-10-01 22:00` | `2026-10-02 01:00` | 3.0h | `$0.0263` | `$0.0285` | **+8.70%** | **+8.34%** | +24.2% | -1.6% | `target_reclaim` |
| 11 | Book 3 | `2026-10-02 07:00` | `2026-10-02 10:00` | 3.0h | `$0.0289` | `$0.0314` | **+8.70%** | **+8.34%** | +8.9% | -1.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `6` | `100.0%` | **`+50.0%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `time_expiry` | `2` | `100.0%` | **`+4.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `SCR`

* **Total Candidate Breakouts Filtered (Vetoed):** `58`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `34` (58.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `13`
* **Saved Capital Losses Avoided:** `+430.4%`
* **Missed Upside Forgone:** `-344.2%`
* **Net Veto Alpha:** `+86.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `45` | `77.6%` |
| `Core 1: Macro Bear Veto` | `7` | `12.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `6.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2` | `3.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*