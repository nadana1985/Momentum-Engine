# Kronos V12: Institutional Symbol Tear Sheet — `AXS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `13` (`13` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `13` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`61.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.299`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+81.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.26x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+6.26%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-13.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`141.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.3% / -5.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2023-01-13 03:00` | `2023-01-14 08:00` | 29.0h | `$8.1583` | `$9.7900` | **+24.95%** | **+22.10%** | +20.9% | -4.5% | `target_reclaim` |
| 2 | Book 2 | `2023-02-15 20:00` | `2023-02-17 21:00` | 49.0h | `$10.6185` | `$10.5555` | **-0.67%** | **-0.67%** | +5.1% | -5.3% | `fast_decay_cut` |
| 3 | Book 2 | `2023-03-13 00:00` | `2023-03-20 00:00` | 168.0h | `$8.1573` | `$9.0094` | **+12.56%** | **+11.95%** | +20.3% | -6.9% | `time_cap` |
| 4 | Book 2 | `2023-04-07 04:00` | `2023-04-08 16:00` | 36.0h | `$8.8330` | `$8.5955` | **-3.07%** | **-3.12%** | +0.9% | -4.4% | `stall_bailout` |
| 5 | Book 2 | `2023-04-26 12:00` | `2023-04-26 19:00` | 7.0h | `$8.3007` | `$7.6176` | **-9.46%** | **-9.87%** | +-0.0% | -9.6% | `initial_stop` |
| 6 | Book 2 | `2023-07-13 15:00` | `2023-07-20 15:00` | 168.0h | `$6.3438` | `$6.3900` | **+0.84%** | **+0.83%** | +8.6% | -3.5% | `time_cap` |
| 7 | Book 2 | `2023-10-21 14:00` | `2023-10-28 14:00` | 168.0h | `$4.3899` | `$4.8050` | **+11.10%** | **+10.61%** | +13.3% | -1.4% | `time_cap` |
| 8 | Book 4 | `2023-11-10 00:00` | `2023-11-27 00:00` | 408.0h | `$6.1051` | `$7.3262` | **+28.39%** | **+25.48%** | +21.1% | -11.0% | `target_reclaim` |
| 9 | Book 2 | `2024-09-13 16:00` | `2024-09-15 04:00` | 36.0h | `$4.8100` | `$4.7202` | **-2.13%** | **-2.15%** | +0.9% | -2.7% | `stall_bailout` |
| 10 | Book 4 | `2024-11-16 11:00` | `2024-11-23 16:00` | 173.0h | `$5.7777` | `$6.9332` | **+18.18%** | **+15.78%** | +20.7% | -7.6% | `target_reclaim` |
| 11 | Book 2 | `2025-04-22 17:00` | `2025-04-29 17:00` | 168.0h | `$2.4210` | `$2.5616` | **+7.15%** | **+6.95%** | +11.4% | -1.2% | `time_cap` |
| 12 | Book 4 | `2026-04-25 08:00` | `2026-05-04 00:00` | 208.0h | `$1.5313` | `$1.3016` | **-8.53%** | **-8.86%** | +15.9% | -15.6% | `structural_stop` |
| 13 | Book 4 | `2026-09-25 00:00` | `2026-10-04 03:00` | 219.0h | `$1.1018` | `$1.3221` | **+13.02%** | **+12.36%** | +20.4% | -2.1% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+75.7%`** |
| `time_cap` | `4` | `100.0%` | **`+30.3%`** |
| `stall_bailout` | `2` | `0.0%` | **`-5.3%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.7%`** |
| `initial_stop` | `1` | `0.0%` | **`-9.9%`** |
| `structural_stop` | `1` | `0.0%` | **`-8.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `AXS`

* **Total Candidate Breakouts Filtered (Vetoed):** `853`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `547` (64.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `278`
* **Saved Capital Losses Avoided:** `+9,036.2%`
* **Missed Upside Forgone:** `-10,683.6%`
* **Net Veto Alpha:** `+-1,647.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `441` | `51.7%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `299` | `35.1%` |
| `Core 0: Zero-Tolerance Data Firewall` | `110` | `12.9%` |
| `Core 4: Funding Rate Cap` | `2` | `0.2%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*