# Kronos V12: Institutional Symbol Tear Sheet — `NEAR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `15` (`15` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `15` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`5.731`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+208.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`8.02x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+13.88%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`87.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.5% / -6.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-12 01:00` | `2021-08-17 01:00` | 120.0h | `$3.1024` | `$3.7229` | **+131.23%** | **+88.67%** | +21.5% | -4.0% | `target_reclaim` |
| 2 | Book 1 | `2023-11-01 09:00` | `2023-11-05 09:00` | 96.0h | `$1.3654` | `$1.6385` | **+22.09%** | **+19.84%** | +20.3% | -1.9% | `target_reclaim` |
| 3 | Book 3 | `2023-11-14 18:00` | `2023-11-15 16:00` | 22.0h | `$1.4764` | `$1.7170` | **+16.29%** | **+15.10%** | +18.1% | -2.4% | `target_reclaim` |
| 4 | Book 3 | `2023-12-11 02:00` | `2023-12-12 14:00` | 36.0h | `$2.3164` | `$2.4630` | **+6.33%** | **+6.14%** | +8.4% | -7.6% | `target_reclaim` |
| 5 | Book 3 | `2023-12-22 06:00` | `2023-12-23 22:00` | 40.0h | `$3.4040` | `$3.7000` | **+8.70%** | **+8.34%** | +11.3% | -5.8% | `target_reclaim` |
| 6 | Book 3 | `2023-12-26 17:00` | `2023-12-28 17:00` | 48.0h | `$4.1198` | `$3.7807` | **-8.23%** | **-8.59%** | +7.0% | -8.4% | `stop_loss` |
| 7 | Book 3 | `2024-02-20 14:00` | `2024-02-21 18:00` | 28.0h | `$3.3542` | `$3.0782` | **-8.23%** | **-8.59%** | +5.2% | -8.1% | `stop_loss` |
| 8 | Book 3 | `2024-03-03 07:00` | `2024-03-03 09:00` | 2.0h | `$3.9431` | `$4.2200` | **+7.02%** | **+6.79%** | +8.6% | -4.7% | `target_reclaim` |
| 9 | Book 3 | `2024-03-05 19:00` | `2024-03-06 15:00` | 20.0h | `$4.0457` | `$4.6970` | **+16.10%** | **+14.93%** | +19.5% | -15.0% | `target_reclaim` |
| 10 | Book 3 | `2024-03-15 03:00` | `2024-03-15 08:00` | 5.0h | `$7.9943` | `$7.3364` | **-8.23%** | **-8.59%** | +7.6% | -8.2% | `stop_loss` |
| 11 | Book 3 | `2024-12-03 13:00` | `2024-12-04 11:00` | 22.0h | `$6.9171` | `$7.6010` | **+9.89%** | **+9.43%** | +11.0% | -2.6% | `target_reclaim` |
| 12 | Book 1 | `2025-04-25 09:00` | `2025-04-28 09:00` | 72.0h | `$2.6456` | `$2.5546` | **-5.02%** | **-5.15%** | +3.1% | -8.6% | `stagnation_bailout` |
| 13 | Book 1 | `2025-07-10 16:00` | `2025-07-18 01:00` | 177.0h | `$2.4010` | `$2.8812` | **+33.53%** | **+29.32%** | +21.7% | -2.3% | `target_reclaim` |
| 14 | Book 4 | `2025-09-18 02:00` | `2025-09-30 15:00` | 301.0h | `$2.8643` | `$2.5711` | **-12.40%** | **-13.09%** | +16.5% | -10.4% | `structural_stop` |
| 15 | Book 1 | `2026-09-04 19:00` | `2026-09-18 01:00` | 318.0h | `$2.1714` | `$3.2169` | **+67.39%** | **+53.66%** | +52.6% | -7.3% | `climax_top_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `9` | `100.0%` | **`+198.5%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+53.7%`** |
| `stagnation_bailout` | `1` | `0.0%` | **`-5.1%`** |
| `structural_stop` | `1` | `0.0%` | **`-13.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `NEAR`

* **Total Candidate Breakouts Filtered (Vetoed):** `769`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `408` (53.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `279`
* **Saved Capital Losses Avoided:** `+6,193.7%`
* **Missed Upside Forgone:** `-9,598.9%`
* **Net Veto Alpha:** `+-3,405.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `575` | `74.8%` |
| `Core 1: Macro Bear Veto` | `146` | `19.0%` |
| `Core 4: Funding Rate Cap` | `47` | `6.1%` |
| `Core 4: Whale Firewall` | `1` | `0.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*