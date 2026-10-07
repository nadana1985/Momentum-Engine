# Kronos V12: Institutional Symbol Tear Sheet — `INJ`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `12` (`12` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `12` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`41.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.734`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+42.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.53x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+3.53%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-25.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`135.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.2% / -7.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-06-26 13:00` | `2023-07-03 13:00` | 168.0h | `$7.6681` | `$8.7411` | **+13.88%** | **+13.00%** | +17.3% | -10.0% | `time_cap` |
| 2 | Book 2 | `2023-10-16 05:00` | `2023-10-23 05:00` | 168.0h | `$7.9027` | `$9.6029` | **+21.51%** | **+19.49%** | +23.0% | -4.3% | `time_cap` |
| 3 | Book 2 | `2023-11-30 04:00` | `2023-12-04 11:00` | 103.0h | `$17.8706` | `$16.3998` | **-8.23%** | **-8.59%** | +5.7% | -16.4% | `initial_stop` |
| 4 | Book 2 | `2024-10-29 16:00` | `2024-10-31 04:00` | 36.0h | `$20.5031` | `$19.6089` | **-4.36%** | **-4.46%** | +-0.0% | -5.4% | `stall_bailout` |
| 5 | Book 1 | `2024-11-09 22:00` | `2024-11-30 22:00` | 504.0h | `$23.2269` | `$31.1310` | **+35.84%** | **+30.63%** | +35.7% | -3.9% | `time_cap` |
| 6 | Book 2 | `2025-02-11 08:00` | `2025-02-11 18:00` | 10.0h | `$15.5819` | `$14.2995` | **-8.23%** | **-8.59%** | +0.1% | -9.0% | `initial_stop` |
| 7 | Book 2 | `2025-04-20 04:00` | `2025-04-27 04:00` | 168.0h | `$8.4922` | `$10.0319` | **+18.13%** | **+16.66%** | +24.1% | -3.3% | `time_cap` |
| 8 | Book 2 | `2025-06-10 11:00` | `2025-06-11 23:00` | 36.0h | `$14.2355` | `$13.2358` | **-7.02%** | **-7.28%** | +0.5% | -7.7% | `stall_bailout` |
| 9 | Book 1 | `2025-07-11 04:00` | `2025-07-13 05:00` | 49.0h | `$12.7107` | `$12.3830` | **-3.79%** | **-3.86%** | +4.1% | -6.3% | `fast_decay_cut` |
| 10 | Book 2 | `2026-05-05 20:00` | `2026-05-12 20:00` | 168.0h | `$3.8576` | `$4.7291` | **+22.59%** | **+20.37%** | +28.4% | -3.0% | `time_cap` |
| 11 | Book 2 | `2026-09-03 15:00` | `2026-09-04 12:00` | 21.0h | `$5.0977` | `$4.6835` | **-8.13%** | **-8.47%** | +-0.0% | -8.7% | `initial_stop` |
| 12 | Book 1 | `2026-09-07 19:00` | `2026-09-15 20:00` | 193.0h | `$6.2767` | `$5.4444` | **-15.20%** | **-16.49%** | +7.0% | -13.8% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `5` | `100.0%` | **`+100.1%`** |
| `initial_stop` | `3` | `0.0%` | **`-25.7%`** |
| `fast_decay_cut` | `2` | `0.0%` | **`-20.4%`** |
| `stall_bailout` | `2` | `0.0%` | **`-11.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `INJ`

* **Total Candidate Breakouts Filtered (Vetoed):** `153`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `72` (47.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `32`
* **Saved Capital Losses Avoided:** `+775.9%`
* **Missed Upside Forgone:** `-1,227.5%`
* **Net Veto Alpha:** `+-451.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `83` | `54.2%` |
| `Core 4: Funding Rate Cap` | `38` | `24.8%` |
| `Core 4: Defensible Whale Dump` | `23` | `15.0%` |
| `Core 4: Whale Firewall` | `9` | `5.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*