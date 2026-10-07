# Kronos V12: Institutional Symbol Tear Sheet — `ZEC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`40.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`5.240`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+28.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.34x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+5.79%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-6.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`73.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.7% / -3.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-10-20 08:00` | `2023-10-21 20:00` | 36.0h | `$25.7041` | `$25.6058` | **-0.38%** | **-0.38%** | +0.9% | -1.9% | `stall_bailout` |
| 2 | Book 2 | `2024-10-06 12:00` | `2024-10-09 12:00` | 72.0h | `$29.1928` | `$28.6482` | **-1.87%** | **-1.88%** | +3.5% | -3.2% | `stagnation_cut` |
| 3 | Book 2 | `2024-10-21 06:00` | `2024-10-24 06:00` | 72.0h | `$38.8168` | `$37.0871` | **-4.46%** | **-4.56%** | +2.4% | -5.9% | `stagnation_cut` |
| 4 | Book 2 | `2025-05-07 17:00` | `2025-05-14 17:00` | 168.0h | `$39.1777` | `$41.0870` | **+4.87%** | **+4.76%** | +17.0% | -1.9% | `time_cap` |
| 5 | Book 2 | `2026-08-21 05:00` | `2026-08-22 02:00` | 21.0h | `$598.4724` | `$815.9949` | **+36.35%** | **+31.00%** | +39.8% | -1.8% | `climax_top_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stagnation_cut` | `2` | `0.0%` | **`-6.4%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+31.0%`** |
| `stall_bailout` | `1` | `0.0%` | **`-0.4%`** |
| `time_cap` | `1` | `100.0%` | **`+4.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `ZEC`

* **Total Candidate Breakouts Filtered (Vetoed):** `359`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `196` (54.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `64`
* **Saved Capital Losses Avoided:** `+2,914.4%`
* **Missed Upside Forgone:** `-2,271.0%`
* **Net Veto Alpha:** `+643.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `152` | `42.3%` |
| `Core 1: Macro Bear Veto` | `122` | `34.0%` |
| `Core 4: Defensible Whale Dump` | `40` | `11.1%` |
| `Core 4: Whale Firewall` | `26` | `7.2%` |
| `Core 4: Funding Rate Cap` | `19` | `5.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*