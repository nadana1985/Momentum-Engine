# Kronos V12: Institutional Symbol Tear Sheet — `SUI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.743`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+48.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.62x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+8.02%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-10.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`172.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+22.6% / -6.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2024-05-20 15:00` | `2024-05-23 20:00` | 77.0h | `$1.1188` | `$1.0267` | **-8.23%** | **-8.59%** | +4.7% | -10.7% | `initial_stop` |
| 2 | Book 2 | `2024-09-29 14:00` | `2024-10-03 15:00` | 97.0h | `$1.7869` | `$1.6398` | **-8.23%** | **-8.59%** | +12.2% | -8.8% | `initial_stop` |
| 3 | Book 2 | `2024-11-05 14:00` | `2024-11-10 09:00` | 115.0h | `$2.0375` | `$3.0343` | **+48.92%** | **+39.83%** | +55.0% | -5.0% | `climax_top_harvest` |
| 4 | Book 2 | `2025-05-08 02:00` | `2025-05-15 02:00` | 168.0h | `$3.5417` | `$3.8700` | **+9.27%** | **+8.86%** | +21.4% | -3.8% | `time_cap` |
| 5 | Book 1 | `2025-07-10 04:00` | `2025-07-31 04:00` | 504.0h | `$3.1621` | `$3.8410` | **+31.06%** | **+27.05%** | +40.7% | -2.2% | `time_cap` |
| 6 | Book 1 | `2025-09-18 09:00` | `2025-09-21 09:00` | 72.0h | `$3.9024` | `$3.6176` | **-9.91%** | **-10.44%** | +1.8% | -8.1% | `stagnation_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `2` | `0.0%` | **`-17.2%`** |
| `time_cap` | `2` | `100.0%` | **`+35.9%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+39.8%`** |
| `stagnation_bailout` | `1` | `0.0%` | **`-10.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `SUI`

* **Total Candidate Breakouts Filtered (Vetoed):** `96`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `61` (63.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `9`
* **Saved Capital Losses Avoided:** `+643.2%`
* **Missed Upside Forgone:** `-257.6%`
* **Net Veto Alpha:** `+385.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `43` | `44.8%` |
| `Core 4: Defensible Whale Dump` | `40` | `41.7%` |
| `Core 4: Funding Rate Cap` | `11` | `11.5%` |
| `Core 4: Whale Firewall` | `2` | `2.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*