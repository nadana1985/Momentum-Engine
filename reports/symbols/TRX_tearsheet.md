# Kronos V12: Institutional Symbol Tear Sheet — `TRX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `17` (`17` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `17` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`23.5%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.293`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-22.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.80x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.34%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-19.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`91.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+3.0% / -3.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2022-03-31 06:00` | `2022-04-02 11:00` | 53.0h | `$0.0770` | `$0.0747` | **-2.95%** | **-3.00%** | +3.5% | -7.4% | `fast_decay_cut` |
| 2 | Book 2 | `2022-10-26 08:00` | `2022-10-30 22:00` | 110.0h | `$0.0631` | `$0.0629` | **-0.32%** | **-0.33%** | +2.7% | -1.0% | `stagnation_cut` |
| 3 | Book 2 | `2022-11-04 14:00` | `2022-11-07 14:00` | 72.0h | `$0.0636` | `$0.0619` | **-2.63%** | **-2.67%** | +2.8% | -2.8% | `stagnation_cut` |
| 4 | Book 2 | `2023-02-15 20:00` | `2023-02-17 08:00` | 36.0h | `$0.0710` | `$0.0678` | **-4.41%** | **-4.51%** | +0.8% | -6.4% | `stall_bailout` |
| 5 | Book 2 | `2023-03-12 23:00` | `2023-03-19 23:00` | 168.0h | `$0.0648` | `$0.0663` | **+2.35%** | **+2.32%** | +6.6% | -4.9% | `time_cap` |
| 6 | Book 2 | `2023-04-10 22:00` | `2023-04-11 17:00` | 19.0h | `$0.0674` | `$0.0653` | **-3.14%** | **-3.19%** | +0.7% | -3.6% | `initial_stop` |
| 7 | Book 2 | `2023-05-01 06:00` | `2023-05-08 06:00` | 168.0h | `$0.0685` | `$0.0684` | **-0.12%** | **-0.12%** | +4.2% | -2.1% | `time_cap` |
| 8 | Book 2 | `2023-07-07 15:00` | `2023-07-10 08:00` | 65.0h | `$0.0795` | `$0.0761` | **-4.28%** | **-4.37%** | +1.2% | -4.3% | `initial_stop` |
| 9 | Book 2 | `2023-11-09 14:00` | `2023-11-16 14:00` | 168.0h | `$0.1010` | `$0.1030` | **+1.91%** | **+1.89%** | +11.9% | -3.7% | `time_cap` |
| 10 | Book 2 | `2023-11-25 21:00` | `2023-11-28 01:00` | 52.0h | `$0.1078` | `$0.1002` | **-7.00%** | **-7.26%** | +2.0% | -7.2% | `initial_stop` |
| 11 | Book 2 | `2024-02-17 09:00` | `2024-02-24 09:00` | 168.0h | `$0.1360` | `$0.1376` | **+1.19%** | **+1.18%** | +3.5% | -1.0% | `time_cap` |
| 12 | Book 2 | `2024-07-25 09:00` | `2024-07-29 10:00` | 97.0h | `$0.1367` | `$0.1358` | **-0.65%** | **-0.65%** | +2.0% | -1.4% | `stagnation_cut` |
| 13 | Book 2 | `2024-10-08 18:00` | `2024-10-12 00:00` | 78.0h | `$0.1596` | `$0.1590` | **-0.39%** | **-0.39%** | +1.6% | -1.0% | `stagnation_cut` |
| 14 | Book 2 | `2024-10-24 02:00` | `2024-10-31 02:00` | 168.0h | `$0.1623` | `$0.1690` | **+4.17%** | **+4.08%** | +4.8% | -0.8% | `time_cap` |
| 15 | Book 2 | `2025-06-09 21:00` | `2025-06-12 02:00` | 53.0h | `$0.2893` | `$0.2749` | **-4.97%** | **-5.10%** | +1.8% | -4.8% | `initial_stop` |
| 16 | Book 2 | `2026-09-08 07:00` | `2026-09-09 22:00` | 39.0h | `$0.3388` | `$0.3372` | **-0.45%** | **-0.46%** | +0.5% | -0.6% | `stall_bailout` |
| 17 | Book 2 | `2026-09-20 13:00` | `2026-09-22 01:00` | 36.0h | `$0.3472` | `$0.3463` | **-0.27%** | **-0.27%** | +0.4% | -1.5% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `5` | `80.0%` | **`+9.4%`** |
| `stagnation_cut` | `4` | `0.0%` | **`-4.0%`** |
| `initial_stop` | `4` | `0.0%` | **`-19.9%`** |
| `stall_bailout` | `3` | `0.0%` | **`-5.2%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-3.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `TRX`

* **Total Candidate Breakouts Filtered (Vetoed):** `494`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `240` (48.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `41`
* **Saved Capital Losses Avoided:** `+1,837.5%`
* **Missed Upside Forgone:** `-1,569.9%`
* **Net Veto Alpha:** `+267.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `244` | `49.4%` |
| `Core 0: Zero-Tolerance Data Firewall` | `132` | `26.7%` |
| `Core 4: Defensible Whale Dump` | `93` | `18.8%` |
| `Core 4: Funding Rate Cap` | `24` | `4.9%` |
| `Core 4: Whale Firewall` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*