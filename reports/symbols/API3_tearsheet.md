# Kronos V12: Institutional Symbol Tear Sheet — `API3`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `21` (`21` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `21` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`61.9%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.460`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+24.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.27x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.14%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-15.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`57.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.1% / -9.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-01-14 09:00` | `2023-01-15 17:00` | 32.0h | `$1.3910` | `$1.4490` | **+4.17%** | **+4.08%** | +5.0% | -9.5% | `target_reclaim` |
| 2 | Book 3 | `2023-02-09 22:00` | `2023-02-12 22:00` | 72.0h | `$1.6388` | `$1.6519` | **+0.80%** | **+0.80%** | +4.8% | -2.7% | `time_expiry` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2023-03-19 05:00` | `2023-03-23 05:00` | Live | `$1.5309` | `$1.6610` | **+8.50%** | **+8.16%** | +9.2% | -14.1% | `shelf_target_reclaim` |
| 4 | Book 3 | `2023-07-05 10:00` | `2023-07-08 10:00` | 72.0h | `$1.0591` | `$1.0424` | **-1.58%** | **-1.59%** | +4.4% | -6.2% | `time_expiry` |
| 5 | Book 5 (Shelf Absorption Squeeze) | `2023-08-06 11:00` | `2023-08-10 11:00` | Live | `$0.9743` | `$1.0571` | **+8.50%** | **+8.16%** | +24.4% | -22.2% | `shelf_target_reclaim` |
| 6 | Book 4 | `2023-10-24 08:00` | `2023-11-01 21:00` | 205.0h | `$1.2393` | `$1.4871` | **+6.15%** | **+5.80%** | +20.8% | -6.5% | `target_reclaim` |
| 7 | Book 3 | `2023-12-10 09:00` | `2023-12-10 20:00` | 11.0h | `$1.5563` | `$1.6478` | **+5.88%** | **+5.72%** | +6.4% | -1.0% | `target_reclaim` |
| 8 | Book 3 | `2023-12-31 08:00` | `2023-12-31 19:00` | 11.0h | `$2.0074` | `$2.1820` | **+8.70%** | **+8.34%** | +9.9% | -7.5% | `target_reclaim` |
| 9 | Book 3 | `2024-01-30 06:00` | `2024-01-31 12:00` | 30.0h | `$2.9461` | `$2.7037` | **-8.23%** | **-8.59%** | +4.7% | -8.3% | `stop_loss` |
| 10 | Book 3 | `2024-06-07 18:00` | `2024-06-08 05:00` | 11.0h | `$3.2282` | `$3.5125` | **+8.81%** | **+8.44%** | +9.0% | -8.6% | `target_reclaim` |
| 11 | Book 3 | `2024-08-24 21:00` | `2024-08-27 10:00` | 61.0h | `$1.7149` | `$1.5738` | **-8.23%** | **-8.59%** | +3.9% | -8.4% | `stop_loss` |
| 12 | Book 2 | `2024-09-14 01:00` | `2024-09-16 01:00` | 48.0h | `$1.5180` | `$1.4486` | **-5.30%** | **-5.43%** | +4.7% | -5.3% | `fast_decay_cut` |
| 13 | Book 5 (Shelf Absorption Squeeze) | `2025-03-17 20:00` | `2025-03-21 20:00` | Live | `$0.7793` | `$0.8456` | **+8.50%** | **+8.16%** | +62.5% | -19.2% | `shelf_target_reclaim` |
| 14 | Book 2 | `2025-04-21 16:00` | `2025-04-24 03:00` | 59.0h | `$0.7562` | `$0.7431` | **-2.12%** | **-2.14%** | +6.0% | -6.2% | `fast_decay_cut` |
| 15 | Book 3 | `2025-07-18 20:00` | `2025-07-20 06:00` | 34.0h | `$0.7361` | `$0.7668` | **+4.17%** | **+4.08%** | +4.8% | -1.4% | `target_reclaim` |
| 16 | Book 3 | `2025-07-23 13:00` | `2025-07-24 05:00` | 16.0h | `$0.7972` | `$0.7316` | **-8.23%** | **-8.59%** | +1.8% | -8.9% | `stop_loss` |
| 17 | Book 5 (Shelf Absorption Squeeze) | `2025-08-19 07:00` | `2025-08-23 07:00` | Live | `$1.3038` | `$1.4146` | **+8.50%** | **+8.16%** | +13.2% | -32.5% | `shelf_target_reclaim` |
| 18 | Book 3 | `2025-10-27 13:00` | `2025-10-29 18:00` | 53.0h | `$0.6854` | `$0.6290` | **-8.23%** | **-8.59%** | +2.5% | -8.1% | `stop_loss` |
| 19 | Book 3 | `2026-09-15 14:00` | `2026-09-18 14:00` | 72.0h | `$0.2285` | `$0.2427` | **+6.19%** | **+6.01%** | +6.6% | -4.7% | `time_expiry` |
| 20 | Book 4 | `2026-09-26 09:00` | `2026-10-03 09:00` | 168.0h | `$0.2883` | `$0.2852` | **+0.19%** | **+0.19%** | +3.0% | -9.0% | `stagnation_cut` |
| 21 | Book 3 | `2026-10-07 13:00` | `2026-10-08 15:00` | 26.0h | `$0.3048` | `$0.2797` | **-8.23%** | **-8.59%** | +3.8% | -8.1% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `6` | `100.0%` | **`+36.5%`** |
| `stop_loss` | `5` | `0.0%` | **`-42.9%`** |
| `shelf_target_reclaim` | `4` | `100.0%` | **`+32.6%`** |
| `time_expiry` | `3` | `66.7%` | **`+5.2%`** |
| `fast_decay_cut` | `2` | `0.0%` | **`-7.6%`** |
| `stagnation_cut` | `1` | `100.0%` | **`+0.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `API3`

* **Total Candidate Breakouts Filtered (Vetoed):** `204`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `144` (70.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `26`
* **Saved Capital Losses Avoided:** `+2,214.7%`
* **Missed Upside Forgone:** `-936.8%`
* **Net Veto Alpha:** `+1,277.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `68` | `33.3%` |
| `Core 1: Macro Bear Veto` | `61` | `29.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `57` | `27.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `18` | `8.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*