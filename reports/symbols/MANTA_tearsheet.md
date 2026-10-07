# Kronos V12: Institutional Symbol Tear Sheet — `MANTA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `14` (`14` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `14` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`57.1%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.294`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+15.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.16x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.08%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-25.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`19.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.1% / -5.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-02-23 15:00` | `2024-02-24 01:00` | 10.0h | `$3.0121` | `$2.7642` | **-8.23%** | **-8.59%** | +2.0% | -8.2% | `stop_loss` |
| 2 | Book 3 | `2024-03-10 13:00` | `2024-03-11 19:00` | 30.0h | `$3.3952` | `$3.6904` | **+8.70%** | **+8.34%** | +9.6% | -3.4% | `target_reclaim` |
| 3 | Book 3 | `2024-03-14 13:00` | `2024-03-15 03:00` | 14.0h | `$3.5211` | `$3.2313` | **-8.23%** | **-8.59%** | +4.4% | -10.4% | `stop_loss` |
| 4 | Book 3 | `2024-07-22 22:00` | `2024-07-24 21:00` | 47.0h | `$1.0139` | `$0.9305` | **-8.23%** | **-8.59%** | +4.1% | -10.4% | `stop_loss` |
| 5 | Book 3 | `2024-08-26 17:00` | `2024-08-27 21:00` | 28.0h | `$0.7709` | `$0.7074` | **-8.23%** | **-8.59%** | +2.4% | -9.1% | `stop_loss` |
| 6 | Book 3 | `2024-11-13 04:00` | `2024-11-14 06:00` | 26.0h | `$0.7669` | `$0.8336` | **+8.70%** | **+8.34%** | +8.9% | -3.9% | `target_reclaim` |
| 7 | Book 3 | `2024-12-02 04:00` | `2024-12-02 23:00` | 19.0h | `$1.1376` | `$1.2365` | **+8.70%** | **+8.34%** | +11.8% | -3.7% | `target_reclaim` |
| 8 | Book 3 | `2024-12-03 13:00` | `2024-12-03 20:00` | 7.0h | `$1.1560` | `$1.2565` | **+8.70%** | **+8.34%** | +9.8% | -2.1% | `target_reclaim` |
| 9 | Book 3 | `2025-04-24 13:00` | `2025-04-24 22:00` | 9.0h | `$0.2091` | `$0.2273` | **+8.70%** | **+8.34%** | +8.9% | -0.6% | `target_reclaim` |
| 10 | Book 3 | `2025-04-28 01:00` | `2025-04-28 07:00` | 6.0h | `$0.2256` | `$0.2452` | **+8.70%** | **+8.34%** | +9.1% | -2.1% | `target_reclaim` |
| 11 | Book 3 | `2025-05-12 18:00` | `2025-05-13 17:00` | 23.0h | `$0.3047` | `$0.3312` | **+8.70%** | **+8.34%** | +9.5% | -6.3% | `target_reclaim` |
| 12 | Book 3 | `2025-05-14 17:00` | `2025-05-15 07:00` | 14.0h | `$0.3096` | `$0.2841` | **-8.23%** | **-8.59%** | +2.7% | -8.2% | `stop_loss` |
| 13 | Book 3 | `2025-07-22 08:00` | `2025-07-23 20:00` | 36.0h | `$0.2419` | `$0.2220` | **-8.23%** | **-8.59%** | +7.3% | -9.0% | `stop_loss` |
| 14 | Book 3 | `2026-09-22 18:00` | `2026-09-22 23:00` | 5.0h | `$0.0670` | `$0.0728` | **+8.70%** | **+8.34%** | +8.9% | -0.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `8` | `100.0%` | **`+66.7%`** |
| `stop_loss` | `6` | `0.0%` | **`-51.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `MANTA`

* **Total Candidate Breakouts Filtered (Vetoed):** `114`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `70` (61.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `12`
* **Saved Capital Losses Avoided:** `+967.6%`
* **Missed Upside Forgone:** `-416.3%`
* **Net Veto Alpha:** `+551.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `69` | `60.5%` |
| `Core 1: Macro Bear Veto` | `29` | `25.4%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `16` | `14.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*