# Kronos V12: Institutional Symbol Tear Sheet — `BNB`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `10` (`10` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `10` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`5.027`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+61.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.86x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+6.19%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-14.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`164.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.7% / -3.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-10-23 18:00` | `2022-10-30 18:00` | 168.0h | `$274.1236` | `$314.2125` | **+15.53%** | **+14.49%** | +16.5% | -1.0% | `time_cap` |
| 2 | Book 2 | `2023-03-13 00:00` | `2023-03-20 00:00` | 168.0h | `$291.2363` | `$333.2847` | **+14.56%** | **+13.60%** | +18.7% | -1.8% | `time_cap` |
| 3 | Book 2 | `2023-07-10 15:00` | `2023-07-17 15:00` | 168.0h | `$246.1238` | `$242.9411` | **-1.41%** | **-1.42%** | +6.2% | -3.3% | `time_cap` |
| 4 | Book 2 | `2023-10-23 22:00` | `2023-10-26 22:00` | 72.0h | `$230.9159` | `$223.3203` | **-3.40%** | **-3.46%** | +3.3% | -5.3% | `stagnation_cut` |
| 5 | Book 1 | `2024-02-26 13:00` | `2024-03-05 19:00` | 198.0h | `$394.9950` | `$375.7582` | **-9.42%** | **-9.79%** | +8.4% | -10.9% | `fast_decay_cut` |
| 6 | Book 3 | `2024-11-25 22:00` | `2024-11-28 22:00` | 72.0h | `$629.0000` | `$658.1006` | **+4.63%** | **+4.52%** | +5.6% | -4.6% | `time_expiry` |
| 7 | Book 2 | `2025-02-08 14:00` | `2025-02-15 14:00` | 168.0h | `$604.0764` | `$712.8102` | **+18.00%** | **+16.55%** | +21.0% | -2.0% | `climax_whale_euphoria_harvest` |
| 8 | Book 2 | `2025-05-07 12:00` | `2025-05-14 12:00` | 168.0h | `$609.6503` | `$654.2503` | **+7.33%** | **+7.08%** | +13.8% | -2.1% | `time_cap` |
| 9 | Book 3 | `2025-09-22 15:00` | `2025-09-25 15:00` | 72.0h | `$1000.2697` | `$993.2606` | **-0.70%** | **-0.70%** | +3.5% | -3.7% | `time_expiry` |
| 10 | Book 4 | `2026-08-20 10:00` | `2026-09-05 16:00` | 390.0h | `$645.3065` | `$774.3678` | **+22.96%** | **+21.01%** | +20.5% | -1.1% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `4` | `75.0%` | **`+33.7%`** |
| `time_expiry` | `2` | `50.0%` | **`+3.8%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-9.8%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+16.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+21.0%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-3.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `BNB`

* **Total Candidate Breakouts Filtered (Vetoed):** `467`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `244` (52.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `57`
* **Saved Capital Losses Avoided:** `+1,951.8%`
* **Missed Upside Forgone:** `-2,869.4%`
* **Net Veto Alpha:** `+-917.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `218` | `46.7%` |
| `Core 1: Macro Bear Veto` | `194` | `41.5%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `26` | `5.6%` |
| `Core 4: Defensible Whale Dump` | `16` | `3.4%` |
| `Core 4: Funding Rate Cap` | `8` | `1.7%` |
| `Core 4: Whale Firewall` | `5` | `1.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*