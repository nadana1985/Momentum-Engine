# Kronos V12: Institutional Symbol Tear Sheet — `XTZ`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `10` (`10` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `10` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`9.696`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+132.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`3.77x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+13.27%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-3.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`109.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.2% / -5.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2020-11-30 16:00` | `2020-12-07 16:00` | 168.0h | `$2.4747` | `$2.2916` | **-9.15%** | **-9.51%** | +3.4% | -11.5% | `stagnation_cut` |
| 2 | Book 4 | `2021-01-05 16:00` | `2021-01-10 08:00` | 112.0h | `$2.4266` | `$2.9120` | **+11.58%** | **+11.05%** | +21.7% | -7.4% | `target_reclaim` |
| 3 | Book 4 | `2021-08-11 19:00` | `2021-08-23 18:00` | 287.0h | `$3.5563` | `$4.2676` | **+36.37%** | **+31.77%** | +20.4% | -9.5% | `target_reclaim` |
| 4 | Book 2 | `2023-03-13 00:00` | `2023-03-20 00:00` | 168.0h | `$1.0637` | `$1.2549` | **+19.87%** | **+18.27%** | +19.0% | -3.9% | `time_cap` |
| 5 | Book 2 | `2023-07-13 17:00` | `2023-07-15 17:00` | 48.0h | `$0.8892` | `$0.8768` | **-2.21%** | **-2.23%** | +3.8% | -4.6% | `fast_decay_cut` |
| 6 | Book 1 | `2023-11-06 23:00` | `2023-11-09 16:00` | 65.0h | `$0.8351` | `$0.8259` | **-0.84%** | **-0.85%** | +7.9% | -8.8% | `fast_decay_cut` |
| 7 | Book 4 | `2024-11-16 02:00` | `2024-11-18 14:00` | 60.0h | `$0.7611` | `$0.9134` | **+70.28%** | **+55.32%** | +21.7% | -0.8% | `target_reclaim` |
| 8 | Book 4 | `2025-07-18 04:00` | `2025-07-19 15:00` | 35.0h | `$0.6980` | `$0.8377` | **+23.82%** | **+21.73%** | +22.5% | -2.6% | `target_reclaim` |
| 9 | Book 1 | `2026-09-09 10:00` | `2026-09-15 11:00` | 145.0h | `$0.2637` | `$0.2591` | **-2.63%** | **-2.66%** | +16.1% | -7.3% | `breakeven_ratchet` |
| 10 | Book 4 | `2026-09-19 01:00` | `2026-09-19 06:00` | 5.0h | `$0.3070` | `$0.3684` | **+10.34%** | **+9.79%** | +25.2% | -0.6% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `5` | `100.0%` | **`+129.7%`** |
| `fast_decay_cut` | `2` | `0.0%` | **`-3.1%`** |
| `breakeven_ratchet` | `1` | `0.0%` | **`-2.7%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-9.5%`** |
| `time_cap` | `1` | `100.0%` | **`+18.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `XTZ`

* **Total Candidate Breakouts Filtered (Vetoed):** `1452`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `820` (56.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `360`
* **Saved Capital Losses Avoided:** `+11,060.0%`
* **Missed Upside Forgone:** `-15,245.7%`
* **Net Veto Alpha:** `+-4,185.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `746` | `51.4%` |
| `Core 0: Zero-Tolerance Data Firewall` | `582` | `40.1%` |
| `Core 1: Macro Bear Veto` | `113` | `7.8%` |
| `Core 4: Funding Rate Cap` | `11` | `0.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*