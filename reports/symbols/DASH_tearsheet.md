# Kronos V12: Institutional Symbol Tear Sheet — `DASH`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `8` (`8` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `8` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`75.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.829`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+80.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.23x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+10.05%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-43.9%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`121.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.4% / -8.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-11 01:00` | `2021-08-15 23:00` | 118.0h | `$179.1383` | `$214.9660` | **+23.14%** | **+21.16%** | +21.6% | -4.9% | `target_reclaim` |
| 2 | Book 4 | `2023-01-20 20:00` | `2023-01-27 20:00` | 168.0h | `$51.6173` | `$51.7423` | **+0.63%** | **+0.63%** | +4.6% | -7.5% | `stagnation_cut` |
| 3 | Book 1 | `2023-11-12 20:00` | `2023-11-14 20:00` | 48.0h | `$33.8945` | `$30.5335` | **-16.40%** | **-17.75%** | +1.3% | -12.1% | `fast_decay_cut` |
| 4 | Book 1 | `2023-12-27 12:00` | `2023-12-30 12:00` | 72.0h | `$37.4935` | `$32.8178` | **-23.65%** | **-26.19%** | +3.7% | -14.4% | `stagnation_bailout` |
| 5 | Book 3 | `2024-02-28 17:00` | `2024-02-29 04:00` | 11.0h | `$29.4240` | `$32.7200` | **+11.20%** | **+10.62%** | +12.5% | -5.9% | `target_reclaim` |
| 6 | Book 4 | `2024-11-13 14:00` | `2024-11-23 09:00` | 235.0h | `$26.2994` | `$31.5593` | **+63.43%** | **+50.92%** | +20.6% | -6.5% | `target_reclaim` |
| 7 | Book 3 | `2024-12-05 06:00` | `2024-12-05 14:00` | 8.0h | `$52.9471` | `$59.4700` | **+12.32%** | **+11.62%** | +14.2% | -3.1% | `target_reclaim` |
| 8 | Book 4 | `2026-08-22 05:00` | `2026-09-04 02:00` | 309.0h | `$41.3519` | `$49.6223` | **+33.46%** | **+29.37%** | +21.0% | -10.9% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `5` | `100.0%` | **`+123.7%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-17.8%`** |
| `stagnation_bailout` | `1` | `0.0%` | **`-26.2%`** |
| `stagnation_cut` | `1` | `100.0%` | **`+0.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `DASH`

* **Total Candidate Breakouts Filtered (Vetoed):** `711`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `381` (53.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `134`
* **Saved Capital Losses Avoided:** `+4,266.0%`
* **Missed Upside Forgone:** `-4,393.3%`
* **Net Veto Alpha:** `+-127.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `508` | `71.4%` |
| `Core 1: Macro Bear Veto` | `178` | `25.0%` |
| `Core 4: Funding Rate Cap` | `22` | `3.1%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `2` | `0.3%` |
| `Core 4: Whale Firewall` | `1` | `0.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*