# Kronos V12: Institutional Symbol Tear Sheet — `BCH`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `20` (`20` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `20` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`40.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.727`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+45.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.58x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+2.27%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-31.1%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`120.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.7% / -4.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2020-10-12 16:00` | `2020-11-03 03:00` | 515.0h | `$242.6835` | `$230.7733` | **-6.01%** | **-6.16%** | +15.8% | -6.0% | `structural_stop` |
| 2 | Book 4 | `2021-08-09 14:00` | `2021-08-15 00:00` | 130.0h | `$584.6457` | `$701.5748` | **+14.08%** | **+13.31%** | +20.8% | -1.9% | `target_reclaim` |
| 3 | Book 2 | `2022-10-04 08:00` | `2022-10-07 08:00` | 72.0h | `$120.1997` | `$118.5628` | **-1.65%** | **-1.66%** | +2.9% | -2.3% | `stagnation_cut` |
| 4 | Book 2 | `2022-10-25 17:00` | `2022-11-01 17:00` | 168.0h | `$113.4830` | `$115.2312` | **+1.86%** | **+1.84%** | +6.3% | -2.3% | `time_cap` |
| 5 | Book 2 | `2023-01-09 00:00` | `2023-01-16 00:00` | 168.0h | `$105.6936` | `$124.6077` | **+20.45%** | **+18.81%** | +24.7% | -2.0% | `time_cap` |
| 6 | Book 4 | `2023-01-27 17:00` | `2023-02-09 19:00` | 314.0h | `$136.2641` | `$124.9124` | **-10.12%** | **-10.57%** | +5.4% | -8.4% | `structural_stop` |
| 7 | Book 2 | `2023-02-15 20:00` | `2023-02-22 20:00` | 168.0h | `$133.3726` | `$139.2809` | **+4.46%** | **+4.37%** | +15.5% | -4.6% | `time_cap` |
| 8 | Book 2 | `2023-03-13 00:00` | `2023-03-20 00:00` | 168.0h | `$121.4830` | `$134.3333` | **+11.18%** | **+10.62%** | +13.5% | -2.0% | `time_cap` |
| 9 | Book 2 | `2023-03-30 02:00` | `2023-03-31 14:00` | 36.0h | `$125.2423` | `$123.6501` | **-1.32%** | **-1.32%** | +-0.1% | -5.1% | `stall_bailout` |
| 10 | Book 2 | `2023-04-26 12:00` | `2023-04-26 19:00` | 7.0h | `$123.4178` | `$115.8187` | **-6.38%** | **-6.59%** | +-0.1% | -8.0% | `initial_stop` |
| 11 | Book 2 | `2023-06-21 04:00` | `2023-06-23 16:00` | 60.0h | `$113.1321` | `$173.8244` | **+56.36%** | **+45.12%** | +61.3% | -0.8% | `climax_top_harvest` |
| 12 | Book 3 | `2023-06-24 07:00` | `2023-06-24 09:00` | 2.0h | `$184.4183` | `$195.1300` | **+5.81%** | **+5.65%** | +6.3% | -2.2% | `target_reclaim` |
| 13 | Book 3 | `2023-10-03 12:00` | `2023-10-06 12:00` | 72.0h | `$238.2014` | `$226.2629` | **-5.01%** | **-5.14%** | +1.2% | -6.4% | `time_expiry` |
| 14 | Book 3 | `2024-04-02 02:00` | `2024-04-04 07:00` | 53.0h | `$604.3664` | `$656.9200` | **+8.70%** | **+8.34%** | +11.5% | -7.0% | `target_reclaim` |
| 15 | Book 2 | `2024-10-12 10:00` | `2024-10-13 22:00` | 36.0h | `$331.6470` | `$320.7860` | **-3.44%** | **-3.50%** | +0.5% | -4.4% | `stall_bailout` |
| 16 | Book 1 | `2024-10-29 15:00` | `2024-10-31 03:00` | 36.0h | `$388.8798` | `$371.8780` | **-8.17%** | **-8.45%** | +0.2% | -6.0% | `stall_bailout` |
| 17 | Book 4 | `2025-04-25 11:00` | `2025-05-02 11:00` | 168.0h | `$379.3882` | `$367.7276` | **-2.66%** | **-2.70%** | +1.4% | -10.1% | `stagnation_cut` |
| 18 | Book 1 | `2025-06-27 16:00` | `2025-06-29 04:00` | 36.0h | `$508.4981` | `$490.7101` | **-6.11%** | **-6.27%** | +0.4% | -4.3% | `stall_bailout` |
| 19 | Book 1 | `2025-08-05 10:00` | `2025-08-06 22:00` | 36.0h | `$584.3673` | `$569.3830` | **-5.03%** | **-5.13%** | +-0.0% | -7.3% | `stall_bailout` |
| 20 | Book 2 | `2026-05-05 10:00` | `2026-05-12 10:00` | 168.0h | `$460.7891` | `$438.9000` | **-4.97%** | **-5.10%** | +6.2% | -4.8% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `5` | `0.0%` | **`-24.7%`** |
| `time_cap` | `5` | `80.0%` | **`+30.5%`** |
| `target_reclaim` | `3` | `100.0%` | **`+27.3%`** |
| `stagnation_cut` | `2` | `0.0%` | **`-4.4%`** |
| `structural_stop` | `2` | `0.0%` | **`-16.7%`** |
| `initial_stop` | `1` | `0.0%` | **`-6.6%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+45.1%`** |
| `time_expiry` | `1` | `0.0%` | **`-5.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `BCH`

* **Total Candidate Breakouts Filtered (Vetoed):** `916`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `460` (50.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `35`
* **Saved Capital Losses Avoided:** `+4,031.0%`
* **Missed Upside Forgone:** `-1,183.5%`
* **Net Veto Alpha:** `+2,847.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `783` | `85.5%` |
| `Core 1: Macro Bear Veto` | `88` | `9.6%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `20` | `2.2%` |
| `Core 4: Funding Rate Cap` | `13` | `1.4%` |
| `Core 4: Whale Firewall` | `7` | `0.8%` |
| `Core 4: Defensible Whale Dump` | `5` | `0.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*