# Kronos V12: Institutional Symbol Tear Sheet — `ILV`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `13` (`13` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `13` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`69.2%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.510`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+32.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.39x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.53%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-12.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`41.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.1% / -4.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-02-20 17:00` | `2024-02-23 17:00` | 72.0h | `$95.8560` | `$95.1017` | **-0.79%** | **-0.79%** | +6.5% | -3.9% | `time_expiry` |
| 2 | Book 3 | `2024-03-16 17:00` | `2024-03-16 23:00` | 6.0h | `$143.8097` | `$131.9742` | **-8.23%** | **-8.59%** | +3.8% | -8.5% | `stop_loss` |
| 3 | Book 2 | `2024-09-13 21:00` | `2024-09-15 09:00` | 36.0h | `$40.7316` | `$39.4811` | **-3.78%** | **-3.84%** | +0.6% | -2.9% | `stall_bailout` |
| 4 | Book 3 | `2024-09-22 10:00` | `2024-09-24 16:00` | 54.0h | `$38.2580` | `$41.0800` | **+7.38%** | **+7.12%** | +8.6% | -3.3% | `target_reclaim` |
| 5 | Book 3 | `2024-11-13 06:00` | `2024-11-13 14:00` | 8.0h | `$37.9729` | `$41.3610` | **+8.92%** | **+8.55%** | +10.3% | -0.2% | `target_reclaim` |
| 6 | Book 3 | `2024-11-20 18:00` | `2024-11-23 08:00` | 62.0h | `$40.5014` | `$46.3950` | **+14.55%** | **+13.59%** | +15.2% | -1.9% | `target_reclaim` |
| 7 | Book 3 | `2024-12-03 13:00` | `2024-12-03 21:00` | 8.0h | `$58.6721` | `$63.7740` | **+8.70%** | **+8.34%** | +9.0% | -3.1% | `target_reclaim` |
| 8 | Book 3 | `2025-04-21 17:00` | `2025-04-22 21:00` | 28.0h | `$13.3661` | `$13.9230` | **+4.17%** | **+4.08%** | +5.2% | -3.1% | `target_reclaim` |
| 9 | Book 3 | `2025-04-26 11:00` | `2025-04-29 11:00` | 72.0h | `$15.4330` | `$15.4742` | **+0.27%** | **+0.27%** | +3.1% | -6.6% | `time_expiry` |
| 10 | Book 3 | `2025-07-14 15:00` | `2025-07-16 00:00` | 33.0h | `$12.4039` | `$13.0120` | **+4.90%** | **+4.79%** | +5.0% | -4.9% | `target_reclaim` |
| 11 | Book 3 | `2025-07-23 13:00` | `2025-07-24 18:00` | 29.0h | `$13.4418` | `$14.3040` | **+6.41%** | **+6.22%** | +6.7% | -7.6% | `target_reclaim` |
| 12 | Book 3 | `2025-10-03 17:00` | `2025-10-06 17:00` | 72.0h | `$15.0652` | `$15.3376` | **+1.81%** | **+1.79%** | +3.1% | -3.7% | `time_expiry` |
| 13 | Book 3 | `2025-10-28 02:00` | `2025-10-30 10:00` | 56.0h | `$11.6408` | `$10.6827` | **-8.23%** | **-8.59%** | +1.9% | -8.5% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `7` | `100.0%` | **`+52.7%`** |
| `time_expiry` | `3` | `66.7%` | **`+1.3%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `stall_bailout` | `1` | `0.0%` | **`-3.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `ILV`

* **Total Candidate Breakouts Filtered (Vetoed):** `429`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `237` (55.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `29`
* **Saved Capital Losses Avoided:** `+3,849.3%`
* **Missed Upside Forgone:** `-849.8%`
* **Net Veto Alpha:** `+2,999.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `367` | `85.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `32` | `7.5%` |
| `Core 1: Macro Bear Veto` | `22` | `5.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `7` | `1.6%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*