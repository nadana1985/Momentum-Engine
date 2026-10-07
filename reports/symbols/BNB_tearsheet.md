# Kronos V12: Institutional Symbol Tear Sheet — `BNB`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `25` (`25` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `25` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`44.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.823`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+41.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.52x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+1.67%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-22.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`114.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.5% / -4.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-10-23 18:00` | `2022-10-30 18:00` | 168.0h | `$274.1236` | `$314.2125` | **+14.62%** | **+13.65%** | +16.5% | -1.0% | `time_cap` |
| 2 | Book 2 | `2023-01-12 00:00` | `2023-01-19 00:00` | 168.0h | `$288.7100` | `$287.1204` | **-0.55%** | **-0.55%** | +9.2% | -4.2% | `time_cap` |
| 3 | Book 2 | `2023-03-13 00:00` | `2023-03-20 00:00` | 168.0h | `$291.2363` | `$333.2847` | **+14.44%** | **+13.49%** | +18.7% | -1.8% | `time_cap` |
| 4 | Book 2 | `2023-04-05 12:00` | `2023-04-07 00:00` | 36.0h | `$316.8000` | `$311.6290` | **-1.63%** | **-1.65%** | +0.0% | -2.1% | `stall_bailout` |
| 5 | Book 2 | `2023-04-10 22:00` | `2023-04-17 22:00` | 168.0h | `$316.1484` | `$340.2572` | **+7.63%** | **+7.35%** | +11.2% | -1.0% | `time_cap` |
| 6 | Book 2 | `2023-07-10 15:00` | `2023-07-17 15:00` | 168.0h | `$246.1238` | `$242.9411` | **-1.29%** | **-1.30%** | +6.2% | -3.3% | `time_cap` |
| 7 | Book 2 | `2023-10-23 22:00` | `2023-10-26 22:00` | 72.0h | `$230.9158` | `$223.3203` | **-3.29%** | **-3.34%** | +3.3% | -5.3% | `stagnation_cut` |
| 8 | Book 2 | `2023-12-12 03:00` | `2023-12-15 03:00` | 72.0h | `$254.0335` | `$250.3226` | **-1.46%** | **-1.47%** | +1.2% | -3.9% | `stagnation_cut` |
| 9 | Book 2 | `2023-12-20 13:00` | `2023-12-27 13:00` | 168.0h | `$259.2966` | `$308.5966` | **+19.01%** | **+17.41%** | +21.1% | -1.7% | `time_cap` |
| 10 | Book 2 | `2024-01-03 09:00` | `2024-01-03 12:00` | 3.0h | `$330.5844` | `$303.3774` | **-8.23%** | **-8.59%** | +1.1% | -13.7% | `initial_stop` |
| 11 | Book 2 | `2024-01-11 08:00` | `2024-01-12 20:00` | 36.0h | `$315.2963` | `$300.9857` | **-4.54%** | **-4.65%** | +0.5% | -5.9% | `stall_bailout` |
| 12 | Book 1 | `2024-02-26 13:00` | `2024-03-05 19:00` | 198.0h | `$394.9950` | `$375.7583` | **-5.26%** | **-5.41%** | +8.4% | -10.9% | `fast_decay_cut` |
| 13 | Book 2 | `2024-05-20 19:00` | `2024-05-27 19:00` | 168.0h | `$590.9437` | `$600.9838` | **+1.70%** | **+1.68%** | +7.1% | -2.3% | `time_cap` |
| 14 | Book 2 | `2024-09-21 08:00` | `2024-09-28 08:00` | 168.0h | `$587.2244` | `$597.9214` | **+1.82%** | **+1.81%** | +5.4% | -1.9% | `time_cap` |
| 15 | Book 2 | `2024-10-08 16:00` | `2024-10-10 04:00` | 36.0h | `$583.7858` | `$568.6548` | **-2.59%** | **-2.63%** | +0.5% | -3.1% | `stall_bailout` |
| 16 | Book 2 | `2025-01-06 16:00` | `2025-01-07 15:00` | 23.0h | `$734.5718` | `$698.9720` | **-4.85%** | **-4.97%** | +1.6% | -4.9% | `initial_stop` |
| 17 | Book 2 | `2025-02-08 14:00` | `2025-02-15 14:00` | 168.0h | `$604.0764` | `$659.9161` | **+9.24%** | **+8.84%** | +21.0% | -2.0% | `time_cap` |
| 18 | Book 2 | `2025-05-07 12:00` | `2025-05-14 12:00` | 168.0h | `$609.6503` | `$654.2503` | **+7.32%** | **+7.06%** | +13.8% | -2.1% | `time_cap` |
| 19 | Book 2 | `2025-05-21 04:00` | `2025-05-28 04:00` | 168.0h | `$662.9833` | `$682.1603` | **+2.89%** | **+2.85%** | +5.3% | -1.9% | `time_cap` |
| 20 | Book 2 | `2025-07-11 17:00` | `2025-07-13 05:00` | 36.0h | `$697.7300` | `$686.8087` | **-1.57%** | **-1.58%** | +0.0% | -2.6% | `stall_bailout` |
| 21 | Book 2 | `2025-07-16 18:00` | `2025-07-23 18:00` | 168.0h | `$709.8402` | `$774.1199` | **+9.06%** | **+8.67%** | +14.2% | -0.7% | `time_cap` |
| 22 | Book 2 | `2025-08-07 10:00` | `2025-08-14 10:00` | 168.0h | `$779.5841` | `$857.7403` | **+10.03%** | **+9.55%** | +11.6% | -1.7% | `time_cap` |
| 23 | Book 2 | `2025-09-21 01:00` | `2025-09-22 13:00` | 36.0h | `$1075.3216` | `$1020.4525` | **-5.10%** | **-5.24%** | +0.8% | -7.7% | `stall_bailout` |
| 24 | Book 2 | `2025-10-07 04:00` | `2025-10-10 21:00` | 89.0h | `$1248.9847` | `$1146.1932` | **-8.23%** | **-8.59%** | +9.1% | -34.1% | `initial_stop` |
| 25 | Book 2 | `2026-10-02 04:00` | `2026-10-03 16:00` | 36.0h | `$784.3359` | `$778.6984` | **-0.72%** | **-0.72%** | +0.1% | -3.0% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `13` | `84.6%` | **`+90.5%`** |
| `stall_bailout` | `6` | `0.0%` | **`-16.5%`** |
| `initial_stop` | `3` | `0.0%` | **`-22.1%`** |
| `stagnation_cut` | `2` | `0.0%` | **`-4.8%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-5.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `BNB`

* **Total Candidate Breakouts Filtered (Vetoed):** `396`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `206` (52.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `57`
* **Saved Capital Losses Avoided:** `+1,866.9%`
* **Missed Upside Forgone:** `-2,869.4%`
* **Net Veto Alpha:** `+-1,002.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `218` | `55.1%` |
| `Core 1: Macro Bear Veto` | `157` | `39.6%` |
| `Core 4: Defensible Whale Dump` | `12` | `3.0%` |
| `Core 4: Funding Rate Cap` | `8` | `2.0%` |
| `Core 4: Whale Firewall` | `1` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*