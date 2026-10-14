# Kronos V12: Institutional Symbol Tear Sheet — `TIA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`80.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`207.414`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+77.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.16x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+15.44%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-0.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`93.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+23.5% / -3.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2024-09-13 21:00` | `2024-09-20 21:00` | 168.0h | `$4.5162` | `$5.9881` | **+40.12%** | **+34.73%** | +43.3% | -4.5% | `time_cap` |
| 2 | Book 2 | `2024-10-11 12:00` | `2024-10-18 12:00` | 168.0h | `$5.4141` | `$6.3886` | **+18.00%** | **+16.55%** | +20.2% | -2.8% | `climax_whale_euphoria_harvest` |
| 3 | Book 4 | `2024-11-23 14:00` | `2024-11-24 13:00` | 23.0h | `$6.6562` | `$7.9874` | **+16.42%** | **+15.24%** | +27.9% | -2.8% | `target_reclaim` |
| 4 | Book 2 | `2026-09-01 13:00` | `2026-09-04 05:00` | 64.0h | `$0.3578` | `$0.3566` | **-0.37%** | **-0.37%** | +4.9% | -5.6% | `fast_decay_cut` |
| 5 | Book 4 | `2026-09-21 12:00` | `2026-09-23 08:00` | 44.0h | `$0.4426` | `$0.5311` | **+11.58%** | **+11.05%** | +21.4% | -3.9% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+26.3%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+16.6%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.4%`** |
| `time_cap` | `1` | `100.0%` | **`+34.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `TIA`

* **Total Candidate Breakouts Filtered (Vetoed):** `537`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `337` (62.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `38`
* **Saved Capital Losses Avoided:** `+5,070.4%`
* **Missed Upside Forgone:** `-1,151.3%`
* **Net Veto Alpha:** `+3,919.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `476` | `88.6%` |
| `Core 1: Macro Bear Veto` | `57` | `10.6%` |
| `Core 4: Defensible Whale Dump` | `3` | `0.6%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*