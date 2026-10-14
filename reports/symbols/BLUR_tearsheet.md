# Kronos V12: Institutional Symbol Tear Sheet — `BLUR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `24` (`24` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `24` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`70.8%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.601`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+87.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.41x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+3.66%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`36.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.7% / -6.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2023-06-27 05:00` | `2023-07-01 05:00` | Live | `$0.3486` | `$0.3782` | **+8.50%** | **+8.16%** | +1.3% | -19.2% | `shelf_target_reclaim` |
| 2 | Book 3 | `2023-10-02 18:00` | `2023-10-05 18:00` | 72.0h | `$0.1787` | `$0.1693` | **-5.28%** | **-5.43%** | +5.6% | -6.7% | `time_expiry` |
| 3 | Book 3 | `2023-10-18 22:00` | `2023-10-18 23:00` | 1.0h | `$0.1838` | `$0.2037` | **+10.80%** | **+10.26%** | +10.9% | -0.5% | `target_reclaim` |
| 4 | Book 3 | `2023-10-24 04:00` | `2023-10-24 18:00` | 14.0h | `$0.2183` | `$0.2274` | **+4.17%** | **+4.08%** | +9.4% | -6.2% | `target_reclaim` |
| 5 | Book 3 | `2023-10-27 17:00` | `2023-10-30 03:00` | 58.0h | `$0.2216` | `$0.2560` | **+15.50%** | **+14.41%** | +16.3% | -1.8% | `target_reclaim` |
| 6 | Book 3 | `2023-10-31 15:00` | `2023-11-03 14:00` | 71.0h | `$0.2267` | `$0.2661` | **+17.38%** | **+16.02%** | +19.2% | -1.4% | `target_reclaim` |
| 7 | Book 3 | `2023-11-06 21:00` | `2023-11-07 06:00` | 9.0h | `$0.3522` | `$0.3828` | **+8.70%** | **+8.34%** | +13.3% | -1.1% | `target_reclaim` |
| 8 | Book 3 | `2023-11-07 09:00` | `2023-11-09 05:00` | 44.0h | `$0.3780` | `$0.3938` | **+4.17%** | **+4.08%** | +4.5% | -6.5% | `target_reclaim` |
| 9 | Book 3 | `2023-11-13 04:00` | `2023-11-14 03:00` | 23.0h | `$0.3740` | `$0.3432` | **-8.23%** | **-8.59%** | +5.9% | -8.9% | `stop_loss` |
| 10 | Book 3 | `2023-12-04 11:00` | `2023-12-05 01:00` | 14.0h | `$0.5029` | `$0.5626` | **+11.88%** | **+11.22%** | +13.1% | -7.2% | `target_reclaim` |
| 11 | Book 3 | `2024-01-03 12:00` | `2024-01-06 04:00` | 64.0h | `$0.5029` | `$0.4615` | **-8.23%** | **-8.59%** | +10.4% | -18.1% | `stop_loss` |
| 12 | Book 3 | `2024-01-19 00:00` | `2024-01-19 09:00` | 9.0h | `$0.6335` | `$0.6599` | **+4.17%** | **+4.08%** | +5.8% | -4.3% | `target_reclaim` |
| 13 | Book 3 | `2024-02-21 18:00` | `2024-02-24 15:00` | 69.0h | `$0.6847` | `$0.7902` | **+15.41%** | **+14.34%** | +19.0% | -6.2% | `target_reclaim` |
| 14 | Book 3 | `2024-07-21 07:00` | `2024-07-22 00:00` | 17.0h | `$0.2084` | `$0.2171` | **+4.17%** | **+4.08%** | +5.1% | -3.6% | `target_reclaim` |
| 15 | Book 3 | `2024-10-09 12:00` | `2024-10-12 12:00` | 72.0h | `$0.2183` | `$0.2316` | **+6.08%** | **+5.90%** | +7.3% | -7.9% | `time_expiry` |
| 16 | Book 3 | `2024-10-23 12:00` | `2024-10-25 23:00` | 59.0h | `$0.2434` | `$0.2233` | **-8.23%** | **-8.59%** | +5.5% | -12.8% | `stop_loss` |
| 17 | Book 3 | `2024-11-12 10:00` | `2024-11-13 06:00` | 20.0h | `$0.2520` | `$0.2313` | **-8.23%** | **-8.59%** | +6.2% | -8.6% | `stop_loss` |
| 18 | Book 3 | `2024-11-24 11:00` | `2024-11-24 22:00` | 11.0h | `$0.2937` | `$0.3193` | **+8.70%** | **+8.34%** | +10.4% | -5.4% | `target_reclaim` |
| 19 | Book 3 | `2024-11-26 12:00` | `2024-11-27 20:00` | 32.0h | `$0.2956` | `$0.3222` | **+8.99%** | **+8.61%** | +9.9% | -0.4% | `target_reclaim` |
| 20 | Book 3 | `2025-06-30 12:00` | `2025-07-02 00:00` | 36.0h | `$0.0721` | `$0.0676` | **-6.25%** | **-6.46%** | +0.6% | -6.6% | `stall_bailout` |
| 21 | Book 3 | `2025-07-17 01:00` | `2025-07-18 01:00` | 24.0h | `$0.0885` | `$0.0921` | **+4.17%** | **+4.08%** | +4.8% | -2.0% | `target_reclaim` |
| 22 | Book 3 | `2025-07-18 20:00` | `2025-07-20 07:00` | 35.0h | `$0.0890` | `$0.0929` | **+4.43%** | **+4.34%** | +4.8% | -2.5% | `target_reclaim` |
| 23 | Book 3 | `2025-09-19 15:00` | `2025-09-22 06:00` | 63.0h | `$0.0849` | `$0.0780` | **-8.23%** | **-8.59%** | +2.6% | -14.1% | `stop_loss` |
| 24 | Book 3 | `2026-09-10 14:00` | `2026-09-11 14:00` | 24.0h | `$0.0164` | `$0.0186` | **+13.07%** | **+12.28%** | +16.5% | -3.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `15` | `100.0%` | **`+128.6%`** |
| `stop_loss` | `5` | `0.0%` | **`-42.9%`** |
| `time_expiry` | `2` | `50.0%` | **`+0.5%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stall_bailout` | `1` | `0.0%` | **`-6.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `BLUR`

* **Total Candidate Breakouts Filtered (Vetoed):** `504`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `373` (74.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `142`
* **Saved Capital Losses Avoided:** `+6,473.4%`
* **Missed Upside Forgone:** `-5,404.8%`
* **Net Veto Alpha:** `+1,068.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `346` | `68.7%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `72` | `14.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `49` | `9.7%` |
| `Core 1: Macro Bear Veto` | `34` | `6.7%` |
| `Core 0: Zero-Tolerance Data Firewall` | `2` | `0.4%` |
| `Core 4: Defensible Whale Dump` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*