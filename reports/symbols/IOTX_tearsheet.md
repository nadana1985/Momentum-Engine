# Kronos V12: Institutional Symbol Tear Sheet — `IOTX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `21` (`21` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `21` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`81.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.634`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+90.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.47x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+4.31%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`47.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.0% / -4.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2022-04-01 04:00` | `2022-04-02 09:00` | 29.0h | `$0.0940` | `$0.1068` | **+13.66%** | **+12.80%** | +14.9% | -1.6% | `target_reclaim` |
| 2 | Book 3 | `2023-01-24 22:00` | `2023-01-26 08:00` | 34.0h | `$0.0291` | `$0.0305` | **+4.86%** | **+4.75%** | +5.3% | -2.2% | `target_reclaim` |
| 3 | Book 3 | `2023-07-16 19:00` | `2023-07-19 19:00` | 72.0h | `$0.0197` | `$0.0203` | **+3.00%** | **+2.96%** | +6.5% | -2.0% | `time_expiry` |
| 4 | Book 4 | `2023-10-23 22:00` | `2023-10-30 03:00` | 149.0h | `$0.0197` | `$0.0236` | **+14.73%** | **+13.64%** | +22.8% | -3.1% | `target_reclaim` |
| 5 | Book 3 | `2023-11-07 09:00` | `2023-11-09 01:00` | 40.0h | `$0.0233` | `$0.0254` | **+8.70%** | **+8.34%** | +10.3% | -4.5% | `target_reclaim` |
| 6 | Book 3 | `2023-11-09 16:00` | `2023-11-10 02:00` | 10.0h | `$0.0243` | `$0.0264` | **+8.70%** | **+8.34%** | +9.2% | -6.5% | `target_reclaim` |
| 7 | Book 3 | `2023-11-14 00:00` | `2023-11-17 00:00` | 72.0h | `$0.0247` | `$0.0249` | **+0.73%** | **+0.72%** | +7.6% | -6.6% | `time_expiry` |
| 8 | Book 3 | `2024-03-10 14:00` | `2024-03-11 18:00` | 28.0h | `$0.0705` | `$0.0764` | **+8.34%** | **+8.01%** | +20.0% | -4.9% | `target_reclaim` |
| 9 | Book 3 | `2024-05-29 19:00` | `2024-05-30 14:00` | 19.0h | `$0.0533` | `$0.0586` | **+9.97%** | **+9.51%** | +10.8% | -2.0% | `target_reclaim` |
| 10 | Book 3 | `2024-07-22 23:00` | `2024-07-25 01:00` | 50.0h | `$0.0484` | `$0.0444` | **-8.23%** | **-8.59%** | +2.2% | -11.1% | `stop_loss` |
| 11 | Book 3 | `2024-09-25 23:00` | `2024-09-26 11:00` | 12.0h | `$0.0448` | `$0.0467` | **+4.17%** | **+4.08%** | +5.8% | -1.7% | `target_reclaim` |
| 12 | Book 3 | `2024-09-27 01:00` | `2024-09-28 02:00` | 25.0h | `$0.0449` | `$0.0472` | **+5.16%** | **+5.04%** | +5.2% | -0.8% | `target_reclaim` |
| 13 | Book 3 | `2024-11-12 10:00` | `2024-11-15 04:00` | 66.0h | `$0.0405` | `$0.0372` | **-8.23%** | **-8.59%** | +8.6% | -8.3% | `stop_loss` |
| 14 | Book 3 | `2024-12-03 13:00` | `2024-12-03 18:00` | 5.0h | `$0.0593` | `$0.0645` | **+8.70%** | **+8.34%** | +9.5% | -2.4% | `target_reclaim` |
| 15 | Book 3 | `2025-05-12 15:00` | `2025-05-13 13:00` | 22.0h | `$0.0183` | `$0.0205` | **+11.53%** | **+10.92%** | +16.7% | -1.5% | `target_reclaim` |
| 16 | Book 3 | `2025-06-05 19:00` | `2025-06-08 19:00` | 72.0h | `$0.0208` | `$0.0210` | **+0.98%** | **+0.97%** | +5.7% | -8.4% | `time_expiry` |
| 17 | Book 3 | `2025-08-05 14:00` | `2025-08-08 02:00` | 60.0h | `$0.0293` | `$0.0305` | **+4.23%** | **+4.14%** | +5.3% | -3.0% | `target_reclaim` |
| 18 | Book 3 | `2025-08-10 13:00` | `2025-08-13 13:00` | 72.0h | `$0.0293` | `$0.0310` | **+5.90%** | **+5.73%** | +7.2% | -4.3% | `time_expiry` |
| 19 | Book 3 | `2026-09-09 22:00` | `2026-09-11 02:00` | 28.0h | `$0.0031` | `$0.0028` | **-8.23%** | **-8.59%** | +7.5% | -8.2% | `stop_loss` |
| 20 | Book 3 | `2026-09-15 05:00` | `2026-09-16 12:00` | 31.0h | `$0.0031` | `$0.0028` | **-8.23%** | **-8.59%** | +3.7% | -8.2% | `stop_loss` |
| 21 | Book 2 | `2026-09-19 21:00` | `2026-09-23 21:00` | 96.0h | `$0.0034` | `$0.0040` | **+18.00%** | **+16.55%** | +26.3% | -5.9% | `climax_whale_euphoria_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `12` | `100.0%` | **`+97.9%`** |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `time_expiry` | `4` | `100.0%` | **`+10.4%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+16.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `IOTX`

* **Total Candidate Breakouts Filtered (Vetoed):** `902`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `613` (68.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `219`
* **Saved Capital Losses Avoided:** `+8,536.3%`
* **Missed Upside Forgone:** `-15,387.7%`
* **Net Veto Alpha:** `+-6,851.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `390` | `43.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `310` | `34.4%` |
| `Core 1: Macro Bear Veto` | `110` | `12.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `59` | `6.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `33` | `3.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*