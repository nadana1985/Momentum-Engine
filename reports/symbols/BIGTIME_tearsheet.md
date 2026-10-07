# Kronos V12: Institutional Symbol Tear Sheet — `BIGTIME`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `14` (`14` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `14` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`57.1%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.112`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+5.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.06x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.41%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-34.4%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`26.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.9% / -6.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-11-13 14:00` | `2023-11-13 16:00` | 2.0h | `$0.1939` | `$0.1780` | **-8.23%** | **-8.59%** | +8.7% | -8.0% | `stop_loss` |
| 2 | Book 3 | `2023-12-04 14:00` | `2023-12-04 15:00` | 1.0h | `$0.5100` | `$0.5543` | **+8.70%** | **+8.34%** | +13.0% | -2.0% | `target_reclaim` |
| 3 | Book 3 | `2023-12-06 11:00` | `2023-12-06 15:00` | 4.0h | `$0.6128` | `$0.6661` | **+8.70%** | **+8.34%** | +12.4% | -4.8% | `target_reclaim` |
| 4 | Book 3 | `2024-02-12 02:00` | `2024-02-13 04:00` | 26.0h | `$0.3894` | `$0.4233` | **+8.70%** | **+8.34%** | +10.4% | -4.4% | `target_reclaim` |
| 5 | Book 3 | `2024-03-03 07:00` | `2024-03-03 08:00` | 1.0h | `$0.4448` | `$0.4835` | **+8.70%** | **+8.34%** | +14.8% | -9.9% | `target_reclaim` |
| 6 | Book 3 | `2024-03-11 00:00` | `2024-03-12 17:00` | 41.0h | `$0.5307` | `$0.4871` | **-8.23%** | **-8.59%** | +9.2% | -10.8% | `stop_loss` |
| 7 | Book 3 | `2024-09-20 11:00` | `2024-09-22 21:00` | 58.0h | `$0.1328` | `$0.1219` | **-8.23%** | **-8.59%** | +6.5% | -8.8% | `stop_loss` |
| 8 | Book 3 | `2024-10-20 04:00` | `2024-10-21 13:00` | 33.0h | `$0.1541` | `$0.1415` | **-8.23%** | **-8.59%** | +2.1% | -8.1% | `stop_loss` |
| 9 | Book 3 | `2024-10-23 04:00` | `2024-10-24 00:00` | 20.0h | `$0.1749` | `$0.1605` | **-8.23%** | **-8.59%** | +11.7% | -9.3% | `stop_loss` |
| 10 | Book 3 | `2024-12-03 13:00` | `2024-12-03 18:00` | 5.0h | `$0.1831` | `$0.1990` | **+8.70%** | **+8.34%** | +9.6% | -5.9% | `target_reclaim` |
| 11 | Book 3 | `2024-12-05 01:00` | `2024-12-05 12:00` | 11.0h | `$0.2069` | `$0.2248` | **+8.70%** | **+8.34%** | +11.5% | -2.8% | `target_reclaim` |
| 12 | Book 3 | `2024-12-08 05:00` | `2024-12-09 07:00` | 26.0h | `$0.2224` | `$0.2041` | **-8.23%** | **-8.59%** | +1.0% | -8.1% | `stop_loss` |
| 13 | Book 3 | `2025-04-26 13:00` | `2025-04-29 13:00` | 72.0h | `$0.0787` | `$0.0807` | **+2.58%** | **+2.55%** | +8.5% | -4.2% | `time_expiry` |
| 14 | Book 3 | `2026-09-15 07:00` | `2026-09-18 07:00` | 72.0h | `$0.0070` | `$0.0074` | **+4.86%** | **+4.75%** | +5.5% | -3.2% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `6` | `0.0%` | **`-51.5%`** |
| `target_reclaim` | `6` | `100.0%` | **`+50.0%`** |
| `time_expiry` | `2` | `100.0%` | **`+7.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `BIGTIME`

* **Total Candidate Breakouts Filtered (Vetoed):** `100`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `65` (65.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `24`
* **Saved Capital Losses Avoided:** `+930.5%`
* **Missed Upside Forgone:** `-1,950.1%`
* **Net Veto Alpha:** `+-1,019.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `31` | `31.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `29` | `29.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `21` | `21.0%` |
| `Core 1: Macro Bear Veto` | `19` | `19.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*