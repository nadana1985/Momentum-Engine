# Kronos V12: Institutional Symbol Tear Sheet — `NEO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.579`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+19.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.21x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.74%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-6.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`70.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+18.3% / -6.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-09-20 02:00` | `2023-09-21 14:00` | 36.0h | `$7.7463` | `$7.3157` | **-5.56%** | **-5.72%** | +0.2% | -6.4% | `stall_bailout` |
| 2 | Book 2 | `2023-11-01 18:00` | `2023-11-03 01:00` | 31.0h | `$9.9458` | `$9.1273` | **-6.09%** | **-6.29%** | +8.5% | -9.3% | `initial_stop` |
| 3 | Book 1 | `2023-11-03 13:00` | `2023-11-05 12:00` | 47.0h | `$10.0932` | `$14.4558` | **+28.32%** | **+24.94%** | +53.3% | -2.6% | `climax_top_harvest` |
| 4 | Book 2 | `2026-09-20 00:00` | `2026-09-27 00:00` | 168.0h | `$2.4832` | `$2.6374` | **+6.21%** | **+6.02%** | +11.1% | -6.2% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `climax_top_harvest` | `1` | `100.0%` | **`+24.9%`** |
| `initial_stop` | `1` | `0.0%` | **`-6.3%`** |
| `stall_bailout` | `1` | `0.0%` | **`-5.7%`** |
| `time_cap` | `1` | `100.0%` | **`+6.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `NEO`

* **Total Candidate Breakouts Filtered (Vetoed):** `286`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `183` (64.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `43`
* **Saved Capital Losses Avoided:** `+2,419.3%`
* **Missed Upside Forgone:** `-1,526.3%`
* **Net Veto Alpha:** `+893.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `128` | `44.8%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `84` | `29.4%` |
| `Core 1: Macro Bear Veto` | `66` | `23.1%` |
| `Core 4: Funding Rate Cap` | `5` | `1.7%` |
| `Core 4: Whale Firewall` | `2` | `0.7%` |
| `Core 4: Defensible Whale Dump` | `1` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*