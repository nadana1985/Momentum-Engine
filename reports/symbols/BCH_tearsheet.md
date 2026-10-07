# Kronos V12: Institutional Symbol Tear Sheet — `BCH`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `25` (`25` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `25` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`36.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`1.153`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+9.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.09x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.36%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-27.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`101.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.0% / -4.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-10-04 08:00` | `2022-10-07 08:00` | 72.0h | `$120.1997` | `$118.5629` | **-1.36%** | **-1.37%** | +2.9% | -2.3% | `stagnation_cut` |
| 2 | Book 2 | `2022-10-25 17:00` | `2022-11-01 17:00` | 168.0h | `$113.4830` | `$115.2312` | **+1.54%** | **+1.53%** | +6.3% | -2.3% | `time_cap` |
| 3 | Book 2 | `2023-01-09 00:00` | `2023-01-16 00:00` | 168.0h | `$105.6936` | `$124.6077` | **+17.90%** | **+16.46%** | +24.7% | -2.0% | `time_cap` |
| 4 | Book 2 | `2023-02-15 20:00` | `2023-02-22 20:00` | 168.0h | `$133.3726` | `$139.2809` | **+4.43%** | **+4.33%** | +15.5% | -4.6% | `time_cap` |
| 5 | Book 2 | `2023-03-13 00:00` | `2023-03-20 00:00` | 168.0h | `$121.4830` | `$134.3333` | **+10.58%** | **+10.06%** | +13.5% | -2.0% | `time_cap` |
| 6 | Book 2 | `2023-03-30 02:00` | `2023-03-31 14:00` | 36.0h | `$125.2423` | `$123.6501` | **-1.27%** | **-1.28%** | +-0.1% | -5.1% | `stall_bailout` |
| 7 | Book 2 | `2023-04-26 12:00` | `2023-04-26 19:00` | 7.0h | `$123.4178` | `$115.8187` | **-6.16%** | **-6.35%** | +-0.1% | -8.0% | `initial_stop` |
| 8 | Book 2 | `2023-06-21 04:00` | `2023-06-21 05:00` | 1.0h | `$113.1321` | `$112.5579` | **-0.51%** | **-0.51%** | +16.5% | -0.8% | `breakeven_ratchet` |
| 9 | Book 2 | `2023-07-20 09:00` | `2023-07-21 21:00` | 36.0h | `$252.8405` | `$246.1431` | **-2.65%** | **-2.68%** | +1.0% | -5.1% | `stall_bailout` |
| 10 | Book 2 | `2023-10-20 03:00` | `2023-10-27 03:00` | 168.0h | `$237.8632` | `$243.9386` | **+2.55%** | **+2.52%** | +13.5% | -3.1% | `time_cap` |
| 11 | Book 2 | `2024-02-03 03:00` | `2024-02-04 15:00` | 36.0h | `$241.9233` | `$236.1881` | **-2.37%** | **-2.40%** | +0.9% | -2.8% | `stall_bailout` |
| 12 | Book 2 | `2024-05-15 19:00` | `2024-05-22 19:00` | 168.0h | `$461.8217` | `$499.2887` | **+8.11%** | **+7.80%** | +14.8% | -4.3% | `time_cap` |
| 13 | Book 2 | `2024-07-27 15:00` | `2024-08-01 16:00` | 121.0h | `$397.1604` | `$398.1484` | **+0.25%** | **+0.25%** | +15.5% | -3.3% | `breakeven_ratchet` |
| 14 | Book 2 | `2024-10-12 10:00` | `2024-10-13 22:00` | 36.0h | `$331.6470` | `$320.7860` | **-3.27%** | **-3.33%** | +0.5% | -4.4% | `stall_bailout` |
| 15 | Book 2 | `2024-10-24 21:00` | `2024-10-25 23:00` | 26.0h | `$368.2082` | `$337.9047` | **-8.23%** | **-8.59%** | +1.6% | -8.0% | `initial_stop` |
| 16 | Book 1 | `2024-10-29 15:00` | `2024-10-31 03:00` | 36.0h | `$388.8798` | `$371.8780` | **-5.45%** | **-5.61%** | +0.2% | -6.0% | `stall_bailout` |
| 17 | Book 2 | `2024-11-06 02:00` | `2024-11-13 02:00` | 168.0h | `$361.3812` | `$426.9500` | **+18.14%** | **+16.67%** | +34.0% | -3.9% | `time_cap` |
| 18 | Book 2 | `2025-05-06 23:00` | `2025-05-13 23:00` | 168.0h | `$375.3260` | `$409.7431` | **+9.17%** | **+8.77%** | +15.4% | -5.5% | `time_cap` |
| 19 | Book 1 | `2025-06-27 16:00` | `2025-06-29 04:00` | 36.0h | `$508.4981` | `$490.7101` | **-3.47%** | **-3.53%** | +0.4% | -4.3% | `stall_bailout` |
| 20 | Book 2 | `2025-07-08 12:00` | `2025-07-15 12:00` | 168.0h | `$503.8565` | `$487.8573` | **-3.18%** | **-3.23%** | +7.1% | -4.0% | `time_cap` |
| 21 | Book 2 | `2025-07-27 06:00` | `2025-08-01 20:00` | 134.0h | `$581.7608` | `$533.8819` | **-8.23%** | **-8.59%** | +4.6% | -8.6% | `initial_stop` |
| 22 | Book 1 | `2025-08-05 10:00` | `2025-08-06 22:00` | 36.0h | `$584.3673` | `$569.3830` | **-2.92%** | **-2.97%** | +-0.0% | -7.3% | `stall_bailout` |
| 23 | Book 2 | `2025-10-01 09:00` | `2025-10-08 09:00` | 168.0h | `$590.5026` | `$576.7645` | **-2.33%** | **-2.35%** | +4.2% | -3.0% | `time_cap` |
| 24 | Book 2 | `2025-10-26 12:00` | `2025-10-29 12:00` | 72.0h | `$563.0641` | `$553.6723` | **-1.67%** | **-1.68%** | +1.6% | -4.4% | `stagnation_cut` |
| 25 | Book 2 | `2026-05-05 10:00` | `2026-05-12 10:00` | 168.0h | `$460.7891` | `$438.9000` | **-4.75%** | **-4.87%** | +6.2% | -4.8% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `11` | `72.7%` | **`+57.7%`** |
| `stall_bailout` | `7` | `0.0%` | **`-21.8%`** |
| `initial_stop` | `3` | `0.0%` | **`-23.5%`** |
| `breakeven_ratchet` | `2` | `50.0%` | **`-0.3%`** |
| `stagnation_cut` | `2` | `0.0%` | **`-3.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `BCH`

* **Total Candidate Breakouts Filtered (Vetoed):** `241`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `135` (56.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `37`
* **Saved Capital Losses Avoided:** `+1,808.8%`
* **Missed Upside Forgone:** `-1,284.9%`
* **Net Veto Alpha:** `+524.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `149` | `61.8%` |
| `Core 1: Macro Bear Veto` | `70` | `29.0%` |
| `Core 4: Funding Rate Cap` | `13` | `5.4%` |
| `Core 4: Defensible Whale Dump` | `5` | `2.1%` |
| `Core 4: Whale Firewall` | `4` | `1.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*