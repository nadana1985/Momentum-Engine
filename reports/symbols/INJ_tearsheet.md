# Kronos V12: Institutional Symbol Tear Sheet — `INJ`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `16` (`16` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `16` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.191`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+96.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.61x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+6.00%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-28.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`99.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.5% / -6.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2023-01-21 18:00` | `2023-01-25 14:00` | 92.0h | `$1.7927` | `$2.1512` | **+74.52%** | **+55.72%** | +36.7% | -4.4% | `target_reclaim` |
| 2 | Book 3 | `2023-02-05 12:00` | `2023-02-06 23:00` | 35.0h | `$3.7362` | `$3.4287` | **-8.23%** | **-8.59%** | +5.0% | -12.3% | `stop_loss` |
| 3 | Book 3 | `2023-11-12 00:00` | `2023-11-12 07:00` | 7.0h | `$17.4882` | `$18.3770` | **+5.08%** | **+4.96%** | +5.5% | -3.6% | `target_reclaim` |
| 4 | Book 3 | `2023-12-15 22:00` | `2023-12-16 00:00` | 2.0h | `$31.5208` | `$28.9267` | **-8.23%** | **-8.59%** | +3.2% | -8.6% | `stop_loss` |
| 5 | Book 3 | `2024-02-28 11:00` | `2024-02-28 17:00` | 6.0h | `$39.2224` | `$35.9944` | **-8.23%** | **-8.59%** | +5.6% | -13.8% | `stop_loss` |
| 6 | Book 3 | `2024-03-15 09:00` | `2024-03-16 10:00` | 25.0h | `$41.6335` | `$47.9470` | **+15.16%** | **+14.12%** | +18.0% | -3.5% | `target_reclaim` |
| 7 | Book 2 | `2024-10-29 16:00` | `2024-10-31 04:00` | 36.0h | `$20.5031` | `$19.6089` | **-4.58%** | **-4.68%** | +-0.0% | -5.4% | `stall_bailout` |
| 8 | Book 1 | `2024-11-09 22:00` | `2024-11-30 22:00` | 504.0h | `$23.2269` | `$31.1310` | **+58.30%** | **+47.10%** | +35.7% | -3.9% | `time_cap` |
| 9 | Book 3 | `2024-12-03 14:00` | `2024-12-03 20:00` | 6.0h | `$30.4472` | `$32.0540` | **+5.28%** | **+5.14%** | +6.5% | -2.1% | `target_reclaim` |
| 10 | Book 2 | `2025-02-11 08:00` | `2025-02-11 18:00` | 10.0h | `$15.5819` | `$14.2995` | **-9.71%** | **-10.13%** | +0.1% | -9.0% | `initial_stop` |
| 11 | Book 2 | `2025-04-20 04:00` | `2025-04-27 04:00` | 168.0h | `$8.4922` | `$10.0319` | **+22.32%** | **+20.51%** | +24.1% | -3.3% | `time_cap` |
| 12 | Book 2 | `2025-06-10 11:00` | `2025-06-11 23:00` | 36.0h | `$14.2355` | `$13.2358` | **-7.13%** | **-7.39%** | +0.5% | -7.7% | `stall_bailout` |
| 13 | Book 1 | `2025-07-11 04:00` | `2025-07-13 05:00` | 49.0h | `$12.7107` | `$12.3830` | **-4.26%** | **-4.34%** | +4.1% | -6.3% | `fast_decay_cut` |
| 14 | Book 2 | `2026-05-05 20:00` | `2026-05-12 20:00` | 168.0h | `$3.8576` | `$4.7291` | **+26.02%** | **+23.46%** | +28.4% | -3.0% | `time_cap` |
| 15 | Book 4 | `2026-05-18 23:00` | `2026-05-29 06:00` | 247.0h | `$5.1477` | `$6.1773` | **+5.79%** | **+5.65%** | +20.1% | -8.1% | `target_reclaim` |
| 16 | Book 1 | `2026-09-07 19:00` | `2026-09-15 20:00` | 193.0h | `$6.2767` | `$5.4444` | **-25.40%** | **-28.32%** | +7.0% | -13.8% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `5` | `100.0%` | **`+85.6%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `time_cap` | `3` | `100.0%` | **`+91.1%`** |
| `fast_decay_cut` | `2` | `0.0%` | **`-32.7%`** |
| `stall_bailout` | `2` | `0.0%` | **`-12.1%`** |
| `initial_stop` | `1` | `0.0%` | **`-10.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `INJ`

* **Total Candidate Breakouts Filtered (Vetoed):** `364`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `160` (44.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `56`
* **Saved Capital Losses Avoided:** `+1,740.3%`
* **Missed Upside Forgone:** `-1,512.1%`
* **Net Veto Alpha:** `+228.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `312` | `85.7%` |
| `Core 4: Defensible Whale Dump` | `23` | `6.3%` |
| `Core 4: Whale Firewall` | `13` | `3.6%` |
| `Core 4: Funding Rate Cap` | `13` | `3.6%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `3` | `0.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*