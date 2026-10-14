# Kronos V12: Institutional Symbol Tear Sheet — `ENJ`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `23` (`23` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `23` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`52.2%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.996`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+70.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.03x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+3.07%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-28.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`74.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.8% / -6.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2022-03-30 01:00` | `2022-03-30 05:00` | 4.0h | `$1.6673` | `$1.7368` | **+4.17%** | **+4.08%** | +4.2% | -0.1% | `target_reclaim` |
| 2 | Book 3 | `2023-02-09 22:00` | `2023-02-12 22:00` | 72.0h | `$0.4382` | `$0.4466` | **+1.92%** | **+1.90%** | +6.4% | -2.0% | `time_expiry` |
| 3 | Book 3 | `2023-02-21 21:00` | `2023-02-23 00:00` | 27.0h | `$0.4876` | `$0.5323` | **+9.16%** | **+8.77%** | +9.3% | -3.8% | `target_reclaim` |
| 4 | Book 3 | `2023-02-25 05:00` | `2023-02-26 17:00` | 36.0h | `$0.4870` | `$0.4753` | **-2.40%** | **-2.43%** | +0.4% | -6.7% | `stall_bailout` |
| 5 | Book 5 (Shelf Absorption Squeeze) | `2023-04-07 05:00` | `2023-04-11 05:00` | Live | `$0.4376` | `$0.4017` | **-8.20%** | **-8.56%** | +-3.2% | -21.3% | `shelf_stop_loss` |
| 6 | Book 3 | `2023-07-06 14:00` | `2023-07-09 14:00` | 72.0h | `$0.2969` | `$0.2924` | **-1.53%** | **-1.55%** | +2.9% | -2.8% | `time_expiry` |
| 7 | Book 2 | `2023-10-01 22:00` | `2023-10-02 18:00` | 20.0h | `$0.2340` | `$0.2191` | **-7.31%** | **-7.55%** | +0.0% | -7.2% | `initial_stop` |
| 8 | Book 2 | `2023-10-09 00:00` | `2023-10-09 16:00` | 16.0h | `$0.2315` | `$0.2181` | **-6.62%** | **-6.81%** | +3.6% | -7.4% | `initial_stop` |
| 9 | Book 2 | `2023-10-16 05:00` | `2023-10-18 05:00` | 48.0h | `$0.2167` | `$0.2147` | **-1.12%** | **-1.12%** | +2.5% | -3.4% | `fast_decay_cut` |
| 10 | Book 2 | `2023-10-23 00:00` | `2023-10-30 00:00` | 168.0h | `$0.2220` | `$0.2757` | **+27.76%** | **+24.86%** | +28.7% | -2.3% | `time_cap` |
| 11 | Book 4 | `2023-11-04 23:00` | `2023-12-04 22:00` | 719.0h | `$0.2892` | `$0.3015` | **+7.81%** | **+7.56%** | +13.7% | -14.6% | `time_expiry` |
| 12 | Book 3 | `2023-12-11 02:00` | `2023-12-14 02:00` | 72.0h | `$0.3064` | `$0.3405` | **+11.15%** | **+10.57%** | +12.4% | -2.0% | `time_expiry` |
| 13 | Book 3 | `2023-12-28 07:00` | `2023-12-30 08:00` | 49.0h | `$0.3931` | `$0.3608` | **-8.23%** | **-8.59%** | +3.3% | -8.4% | `stop_loss` |
| 14 | Book 3 | `2024-02-20 15:00` | `2024-02-23 15:00` | 72.0h | `$0.3311` | `$0.3317` | **+0.18%** | **+0.18%** | +5.1% | -5.2% | `time_expiry` |
| 15 | Book 3 | `2024-02-29 22:00` | `2024-03-01 12:00` | 14.0h | `$0.4137` | `$0.4549` | **+9.97%** | **+9.50%** | +13.9% | -0.1% | `target_reclaim` |
| 16 | Book 3 | `2024-03-05 05:00` | `2024-03-05 19:00` | 14.0h | `$0.5456` | `$0.5007` | **-8.23%** | **-8.59%** | +5.5% | -20.4% | `stop_loss` |
| 17 | Book 3 | `2024-05-29 16:00` | `2024-05-31 17:00` | 49.0h | `$0.3582` | `$0.3287` | **-8.23%** | **-8.59%** | +3.7% | -13.0% | `stop_loss` |
| 18 | Book 3 | `2024-10-01 14:00` | `2024-10-01 17:00` | 3.0h | `$0.1627` | `$0.1493` | **-8.23%** | **-8.59%** | +2.9% | -11.9% | `stop_loss` |
| 19 | Book 3 | `2024-11-13 04:00` | `2024-11-16 04:00` | 72.0h | `$0.1510` | `$0.1631` | **+8.01%** | **+7.71%** | +10.1% | -2.2% | `time_expiry` |
| 20 | Book 4 | `2024-11-21 12:00` | `2024-11-23 15:00` | 51.0h | `$0.1976` | `$0.2371` | **+59.33%** | **+48.21%** | +21.3% | -2.8% | `target_reclaim` |
| 21 | Book 3 | `2025-04-21 18:00` | `2025-04-21 23:00` | 5.0h | `$0.0925` | `$0.1022` | **+10.44%** | **+9.93%** | +16.0% | -3.8% | `target_reclaim` |
| 22 | Book 3 | `2026-09-05 00:00` | `2026-09-06 15:00` | 39.0h | `$0.0287` | `$0.0263` | **-8.23%** | **-8.59%** | +4.7% | -8.2% | `stop_loss` |
| 23 | Book 3 | `2026-10-02 14:00` | `2026-10-03 02:00` | 12.0h | `$0.0334` | `$0.0363` | **+8.70%** | **+8.34%** | +11.2% | -5.4% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_expiry` | `6` | `83.3%` | **`+26.4%`** |
| `target_reclaim` | `6` | `100.0%` | **`+88.8%`** |
| `stop_loss` | `5` | `0.0%` | **`-42.9%`** |
| `initial_stop` | `2` | `0.0%` | **`-14.4%`** |
| `stall_bailout` | `1` | `0.0%` | **`-2.4%`** |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.1%`** |
| `time_cap` | `1` | `100.0%` | **`+24.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `ENJ`

* **Total Candidate Breakouts Filtered (Vetoed):** `1110`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `602` (54.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `361`
* **Saved Capital Losses Avoided:** `+8,214.5%`
* **Missed Upside Forgone:** `-18,718.5%`
* **Net Veto Alpha:** `+-10,504.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `488` | `44.0%` |
| `Core 1: Macro Bear Veto` | `421` | `37.9%` |
| `Core 0: Zero-Tolerance Data Firewall` | `95` | `8.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `70` | `6.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `33` | `3.0%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `3` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*