# Kronos V12: Institutional Symbol Tear Sheet — `CKB`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `16` (`16` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `16` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`56.2%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.328`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+16.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.17x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.01%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-38.2%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`38.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.6% / -5.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-10-04 00:00` | `2023-10-07 00:00` | 72.0h | `$0.0026` | `$0.0028` | **+5.44%** | **+5.29%** | +6.6% | -2.2% | `time_expiry` |
| 2 | Book 3 | `2023-12-11 02:00` | `2023-12-14 02:00` | 72.0h | `$0.0033` | `$0.0034` | **+1.64%** | **+1.62%** | +7.5% | -6.7% | `time_expiry` |
| 3 | Book 3 | `2024-02-26 11:00` | `2024-02-26 16:00` | 5.0h | `$0.0143` | `$0.0155` | **+8.70%** | **+8.34%** | +12.8% | -0.4% | `target_reclaim` |
| 4 | Book 3 | `2024-02-27 08:00` | `2024-02-28 01:00` | 17.0h | `$0.0165` | `$0.0152` | **-8.23%** | **-8.59%** | +4.6% | -8.4% | `stop_loss` |
| 5 | Book 3 | `2024-03-05 19:00` | `2024-03-06 03:00` | 8.0h | `$0.0174` | `$0.0189` | **+8.70%** | **+8.34%** | +9.0% | -13.1% | `target_reclaim` |
| 6 | Book 3 | `2024-03-09 10:00` | `2024-03-10 01:00` | 15.0h | `$0.0216` | `$0.0235` | **+8.70%** | **+8.34%** | +8.9% | -0.5% | `target_reclaim` |
| 7 | Book 3 | `2024-03-12 08:00` | `2024-03-13 21:00` | 37.0h | `$0.0234` | `$0.0215` | **-8.23%** | **-8.59%** | +5.5% | -8.7% | `stop_loss` |
| 8 | Book 3 | `2024-04-10 18:00` | `2024-04-11 07:00` | 13.0h | `$0.0333` | `$0.0305` | **-8.23%** | **-8.59%** | +2.6% | -8.0% | `stop_loss` |
| 9 | Book 3 | `2024-07-22 22:00` | `2024-07-25 02:00` | 52.0h | `$0.0122` | `$0.0112` | **-8.23%** | **-8.59%** | +2.8% | -8.7% | `stop_loss` |
| 10 | Book 3 | `2024-09-20 11:00` | `2024-09-23 11:00` | 72.0h | `$0.0166` | `$0.0160` | **-3.75%** | **-3.83%** | +3.7% | -4.8% | `time_expiry` |
| 11 | Book 3 | `2024-09-30 09:00` | `2024-10-01 15:00` | 30.0h | `$0.0171` | `$0.0157` | **-8.23%** | **-8.59%** | +1.4% | -8.5% | `stop_loss` |
| 12 | Book 3 | `2024-12-02 08:00` | `2024-12-03 06:00` | 22.0h | `$0.0163` | `$0.0178` | **+8.70%** | **+8.34%** | +9.8% | -6.8% | `target_reclaim` |
| 13 | Book 3 | `2025-07-15 03:00` | `2025-07-16 18:00` | 39.0h | `$0.0041` | `$0.0044` | **+8.70%** | **+8.34%** | +9.1% | -1.4% | `target_reclaim` |
| 14 | Book 3 | `2026-08-30 23:00` | `2026-09-01 04:00` | 29.0h | `$0.0010` | `$0.0011` | **+8.70%** | **+8.34%** | +9.1% | -0.4% | `target_reclaim` |
| 15 | Book 3 | `2026-09-10 18:00` | `2026-09-13 01:00` | 55.0h | `$0.0011` | `$0.0012` | **+8.70%** | **+8.34%** | +8.8% | -3.9% | `target_reclaim` |
| 16 | Book 3 | `2026-09-28 07:00` | `2026-10-01 07:00` | 72.0h | `$0.0013` | `$0.0013` | **-2.37%** | **-2.40%** | +2.7% | -4.7% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `7` | `100.0%` | **`+58.4%`** |
| `stop_loss` | `5` | `0.0%` | **`-42.9%`** |
| `time_expiry` | `4` | `50.0%` | **`+0.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `CKB`

* **Total Candidate Breakouts Filtered (Vetoed):** `153`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `90` (58.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `24`
* **Saved Capital Losses Avoided:** `+1,210.3%`
* **Missed Upside Forgone:** `-1,529.9%`
* **Net Veto Alpha:** `+-319.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `45` | `29.4%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `45` | `29.4%` |
| `Core 1: Macro Bear Veto` | `34` | `22.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `29` | `19.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*