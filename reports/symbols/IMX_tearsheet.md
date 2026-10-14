# Kronos V12: Institutional Symbol Tear Sheet — `IMX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `27` (`27` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `27` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`74.1%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.781`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+127.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`3.56x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+4.71%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-11.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`63.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.3% / -4.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2022-03-22 04:00` | `2022-04-06 13:00` | 369.0h | `$2.4215` | `$2.0583` | **-6.41%** | **-6.66%** | +18.0% | -16.9% | `structural_stop` |
| 2 | Book 2 | `2022-10-25 19:00` | `2022-11-01 19:00` | 168.0h | `$0.5764` | `$0.5787` | **+0.49%** | **+0.49%** | +17.5% | -3.2% | `time_cap` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2022-12-19 21:00` | `2022-12-23 21:00` | Live | `$0.4045` | `$0.4389` | **+8.50%** | **+8.16%** | +5.5% | -14.7% | `shelf_target_reclaim` |
| 4 | Book 3 | `2023-01-18 15:00` | `2023-01-18 18:00` | 3.0h | `$0.5876` | `$0.6121` | **+4.17%** | **+4.08%** | +6.4% | -5.6% | `target_reclaim` |
| 5 | Book 3 | `2023-02-05 12:00` | `2023-02-05 16:00` | 4.0h | `$0.8507` | `$0.9247` | **+8.70%** | **+8.34%** | +9.5% | -2.5% | `target_reclaim` |
| 6 | Book 3 | `2023-02-09 03:00` | `2023-02-09 07:00` | 4.0h | `$0.9445` | `$1.0260` | **+8.63%** | **+8.27%** | +8.8% | -0.7% | `target_reclaim` |
| 7 | Book 3 | `2023-02-16 13:00` | `2023-02-16 18:00` | 5.0h | `$1.1567` | `$1.2550` | **+8.50%** | **+8.15%** | +9.8% | -1.2% | `target_reclaim` |
| 8 | Book 3 | `2023-03-15 15:00` | `2023-03-15 19:00` | 4.0h | `$1.0809` | `$1.1660` | **+7.88%** | **+7.58%** | +13.0% | -5.0% | `target_reclaim` |
| 9 | Book 3 | `2023-07-04 15:00` | `2023-07-07 00:00` | 57.0h | `$0.7435` | `$0.6823` | **-8.23%** | **-8.59%** | +2.7% | -8.4% | `stop_loss` |
| 10 | Book 2 | `2023-07-13 16:00` | `2023-07-20 16:00` | 168.0h | `$0.7247` | `$0.7312` | **+0.96%** | **+0.95%** | +10.4% | -2.1% | `time_cap` |
| 11 | Book 5 (Shelf Absorption Squeeze) | `2023-07-28 02:00` | `2023-08-01 02:00` | Live | `$0.7269` | `$0.7887` | **+8.50%** | **+8.16%** | +1.7% | -10.1% | `shelf_target_reclaim` |
| 12 | Book 5 (Shelf Absorption Squeeze) | `2023-09-21 00:00` | `2023-09-25 00:00` | Live | `$0.6101` | `$0.5600` | **-8.20%** | **-8.56%** | +-1.5% | -18.1% | `shelf_stop_loss` |
| 13 | Book 3 | `2023-09-23 03:00` | `2023-09-26 03:00` | 72.0h | `$0.6101` | `$0.5980` | **-1.98%** | **-2.00%** | +1.9% | -4.9% | `time_expiry` |
| 14 | Book 2 | `2023-10-23 08:00` | `2023-10-30 08:00` | 168.0h | `$0.5957` | `$0.6748` | **+14.29%** | **+13.41%** | +15.8% | -1.9% | `time_cap` |
| 15 | Book 3 | `2023-11-02 15:00` | `2023-11-02 23:00` | 8.0h | `$0.6625` | `$0.6901` | **+4.17%** | **+4.08%** | +5.2% | -1.2% | `target_reclaim` |
| 16 | Book 3 | `2023-11-12 00:00` | `2023-11-12 20:00` | 20.0h | `$1.0768` | `$1.1704` | **+8.70%** | **+8.34%** | +9.0% | -0.1% | `target_reclaim` |
| 17 | Book 3 | `2023-11-13 04:00` | `2023-11-13 14:00` | 10.0h | `$1.0940` | `$1.1891` | **+8.70%** | **+8.34%** | +8.7% | -1.1% | `target_reclaim` |
| 18 | Book 3 | `2023-11-14 18:00` | `2023-11-15 14:00` | 20.0h | `$1.0956` | `$1.2111` | **+10.55%** | **+10.03%** | +10.9% | -3.3% | `target_reclaim` |
| 19 | Book 3 | `2023-11-25 11:00` | `2023-11-25 23:00` | 12.0h | `$1.3545` | `$1.4235` | **+5.10%** | **+4.97%** | +5.9% | -0.1% | `target_reclaim` |
| 20 | Book 3 | `2023-12-12 21:00` | `2023-12-14 12:00` | 39.0h | `$1.9572` | `$2.2252` | **+13.69%** | **+12.83%** | +17.6% | -0.2% | `target_reclaim` |
| 21 | Book 3 | `2023-12-28 16:00` | `2023-12-31 16:00` | 72.0h | `$2.2806` | `$2.2197` | **-2.67%** | **-2.71%** | +4.6% | -4.4% | `time_expiry` |
| 22 | Book 3 | `2024-03-12 17:00` | `2024-03-15 02:00` | 57.0h | `$3.3810` | `$3.1028` | **-8.23%** | **-8.59%** | +7.9% | -8.9% | `stop_loss` |
| 23 | Book 4 | `2024-11-23 11:00` | `2024-11-28 22:00` | 131.0h | `$1.5635` | `$1.8763` | **+28.42%** | **+25.51%** | +23.1% | -2.0% | `target_reclaim` |
| 24 | Book 3 | `2024-12-04 17:00` | `2024-12-05 12:00` | 19.0h | `$1.9918` | `$2.1650` | **+8.70%** | **+8.34%** | +10.4% | -1.7% | `target_reclaim` |
| 25 | Book 3 | `2025-07-14 14:00` | `2025-07-16 18:00` | 52.0h | `$0.5299` | `$0.5594` | **+5.57%** | **+5.42%** | +5.9% | -4.5% | `target_reclaim` |
| 26 | Book 3 | `2025-08-14 08:00` | `2025-08-14 12:00` | 4.0h | `$0.6169` | `$0.5661` | **-8.23%** | **-8.59%** | +0.8% | -8.8% | `stop_loss` |
| 27 | Book 4 | `2025-09-16 03:00` | `2025-09-18 13:00` | 58.0h | `$0.6624` | `$0.7949` | **+18.81%** | **+17.27%** | +21.4% | -1.8% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `15` | `100.0%` | **`+141.6%`** |
| `time_cap` | `3` | `100.0%` | **`+14.9%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `time_expiry` | `2` | `0.0%` | **`-4.7%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `structural_stop` | `1` | `0.0%` | **`-6.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `IMX`

* **Total Candidate Breakouts Filtered (Vetoed):** `1536`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `860` (56.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `129`
* **Saved Capital Losses Avoided:** `+11,241.2%`
* **Missed Upside Forgone:** `-3,881.1%`
* **Net Veto Alpha:** `+7,360.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `718` | `46.7%` |
| `Core 1: Macro Bear Veto` | `317` | `20.6%` |
| `Core 0: Zero-Tolerance Data Firewall` | `228` | `14.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `224` | `14.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `39` | `2.5%` |
| `Core 4: Defensible Whale Dump` | `6` | `0.4%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `4` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*