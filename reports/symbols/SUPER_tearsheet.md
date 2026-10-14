# Kronos V12: Institutional Symbol Tear Sheet — `SUPER`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `24` (`24` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `24` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.339`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+77.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.18x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+3.24%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`46.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.6% / -5.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-01-30 14:00` | `2024-01-30 23:00` | 9.0h | `$0.6900` | `$0.6332` | **-8.23%** | **-8.59%** | +1.4% | -8.6% | `stop_loss` |
| 2 | Book 3 | `2024-02-20 04:00` | `2024-02-21 10:00` | 30.0h | `$1.1358` | `$1.0424` | **-8.23%** | **-8.59%** | +2.6% | -8.3% | `stop_loss` |
| 3 | Book 3 | `2024-02-28 06:00` | `2024-02-28 17:00` | 11.0h | `$1.2553` | `$1.1520` | **-8.23%** | **-8.59%** | +8.4% | -19.8% | `stop_loss` |
| 4 | Book 3 | `2024-03-03 07:00` | `2024-03-04 00:00` | 17.0h | `$1.3633` | `$1.4818` | **+8.70%** | **+8.34%** | +9.3% | -4.5% | `target_reclaim` |
| 5 | Book 3 | `2024-03-08 15:00` | `2024-03-09 13:00` | 22.0h | `$1.4381` | `$1.5631` | **+8.70%** | **+8.34%** | +8.8% | -0.8% | `target_reclaim` |
| 6 | Book 3 | `2024-05-23 13:00` | `2024-05-26 13:00` | 72.0h | `$1.0585` | `$0.9939` | **-6.10%** | **-6.30%** | +3.9% | -7.7% | `time_expiry` |
| 7 | Book 3 | `2024-07-28 21:00` | `2024-07-29 03:00` | 6.0h | `$0.7104` | `$0.7475` | **+5.23%** | **+5.09%** | +5.2% | -0.4% | `target_reclaim` |
| 8 | Book 3 | `2024-09-16 17:00` | `2024-09-18 09:00` | 40.0h | `$0.8582` | `$0.7876` | **-8.23%** | **-8.59%** | +2.3% | -8.1% | `stop_loss` |
| 9 | Book 3 | `2024-10-01 17:00` | `2024-10-04 17:00` | 72.0h | `$0.9530` | `$1.0400` | **+9.13%** | **+8.74%** | +14.0% | -3.2% | `time_expiry` |
| 10 | Book 3 | `2024-10-07 23:00` | `2024-10-09 15:00` | 40.0h | `$1.0703` | `$1.1426` | **+6.76%** | **+6.54%** | +6.9% | -2.6% | `target_reclaim` |
| 11 | Book 3 | `2024-10-16 15:00` | `2024-10-19 15:00` | 72.0h | `$1.2940` | `$1.3356` | **+3.21%** | **+3.16%** | +5.2% | -2.3% | `time_expiry` |
| 12 | Book 3 | `2024-10-25 18:00` | `2024-10-25 23:00` | 5.0h | `$1.3388` | `$1.2286` | **-8.23%** | **-8.59%** | +1.5% | -10.4% | `stop_loss` |
| 13 | Book 3 | `2024-11-07 04:00` | `2024-11-10 04:00` | 72.0h | `$1.3545` | `$1.4097` | **+4.07%** | **+3.99%** | +5.3% | -5.5% | `time_expiry` |
| 14 | Book 3 | `2024-11-12 10:00` | `2024-11-13 14:00` | 28.0h | `$1.3672` | `$1.4795` | **+8.21%** | **+7.89%** | +9.0% | -5.8% | `target_reclaim` |
| 15 | Book 3 | `2024-12-09 21:00` | `2024-12-09 22:00` | 1.0h | `$1.7382` | `$1.8893` | **+8.70%** | **+8.34%** | +11.4% | -7.4% | `target_reclaim` |
| 16 | Book 3 | `2024-12-12 19:00` | `2024-12-15 19:00` | 72.0h | `$2.0801` | `$2.1553` | **+3.61%** | **+3.55%** | +4.2% | -6.1% | `time_expiry` |
| 17 | Book 3 | `2025-04-29 23:00` | `2025-05-01 11:00` | 36.0h | `$0.6952` | `$0.7478` | **+7.56%** | **+7.29%** | +8.0% | -7.1% | `target_reclaim` |
| 18 | Book 3 | `2025-05-23 12:00` | `2025-05-25 08:00` | 44.0h | `$0.8355` | `$0.7668` | **-8.23%** | **-8.59%** | +3.6% | -9.5% | `stop_loss` |
| 19 | Book 3 | `2025-07-17 20:00` | `2025-07-18 01:00` | 5.0h | `$0.8386` | `$0.8865` | **+5.71%** | **+5.55%** | +6.9% | -0.1% | `target_reclaim` |
| 20 | Book 3 | `2025-07-18 20:00` | `2025-07-21 20:00` | 72.0h | `$0.8386` | `$0.8365` | **-0.25%** | **-0.25%** | +5.7% | -4.1% | `time_expiry` |
| 21 | Book 3 | `2025-09-30 02:00` | `2025-10-02 07:00` | 53.0h | `$0.6091` | `$0.6937` | **+13.88%** | **+13.00%** | +15.3% | -6.3% | `target_reclaim` |
| 22 | Book 2 | `2026-09-03 15:00` | `2026-09-10 15:00` | 168.0h | `$0.1132` | `$0.1167` | **+3.34%** | **+3.29%** | +13.4% | -2.5% | `time_cap` |
| 23 | Book 4 | `2026-09-18 14:00` | `2026-09-22 23:00` | 105.0h | `$0.1347` | `$0.1616` | **+46.31%** | **+38.11%** | +21.3% | -3.4% | `target_reclaim` |
| 24 | Book 3 | `2026-09-28 07:00` | `2026-10-01 07:00` | 72.0h | `$0.1913` | `$0.2003` | **+4.72%** | **+4.61%** | +9.2% | -2.1% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `10` | `100.0%` | **`+108.5%`** |
| `time_expiry` | `7` | `71.4%` | **`+17.5%`** |
| `stop_loss` | `6` | `0.0%` | **`-51.5%`** |
| `time_cap` | `1` | `100.0%` | **`+3.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `SUPER`

* **Total Candidate Breakouts Filtered (Vetoed):** `555`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `330` (59.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `27`
* **Saved Capital Losses Avoided:** `+3,868.6%`
* **Missed Upside Forgone:** `-716.4%`
* **Net Veto Alpha:** `+3,152.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `462` | `83.2%` |
| `Core 1: Macro Bear Veto` | `46` | `8.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `23` | `4.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `23` | `4.1%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*