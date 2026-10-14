# Kronos V12: Institutional Symbol Tear Sheet — `SEI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `8` (`8` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `8` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`62.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.411`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+95.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.61x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+11.99%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`90.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+20.0% / -5.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2023-11-08 12:00` | `2023-11-09 16:00` | 28.0h | `$0.1266` | `$0.1111` | **-18.20%** | **-20.00%** | +3.9% | -18.7% | `initial_stop` |
| 2 | Book 4 | `2023-11-19 23:00` | `2023-11-21 04:00` | 29.0h | `$0.1485` | `$0.1782` | **+11.58%** | **+11.05%** | +23.6% | -0.8% | `target_reclaim` |
| 3 | Book 2 | `2024-09-18 23:00` | `2024-09-25 01:00` | 146.0h | `$0.3114` | `$0.4606` | **+54.53%** | **+44.55%** | +52.4% | -4.2% | `climax_top_harvest` |
| 4 | Book 4 | `2025-06-27 02:00` | `2025-07-11 01:00` | 335.0h | `$0.2715` | `$0.3258` | **+24.27%** | **+21.96%** | +20.3% | -8.5% | `target_reclaim` |
| 5 | Book 2 | `2026-05-04 02:00` | `2026-05-05 14:00` | 36.0h | `$0.0603` | `$0.0593` | **-2.02%** | **-2.04%** | +0.1% | -3.8% | `stall_bailout` |
| 6 | Book 2 | `2026-09-02 19:00` | `2026-09-04 19:00` | 48.0h | `$0.0496` | `$0.0470` | **-5.92%** | **-6.08%** | +1.1% | -7.4% | `fast_decay_cut` |
| 7 | Book 2 | `2026-09-18 04:00` | `2026-09-21 13:00` | 81.0h | `$0.0467` | `$0.0607` | **+35.04%** | **+30.64%** | +38.5% | -1.4% | `climax_top_harvest` |
| 8 | Book 4 | `2026-09-25 07:00` | `2026-09-26 01:00` | 18.0h | `$0.0642` | `$0.0770` | **+16.92%** | **+15.82%** | +20.5% | -0.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+48.8%`** |
| `climax_top_harvest` | `2` | `100.0%` | **`+75.2%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-6.1%`** |
| `initial_stop` | `1` | `0.0%` | **`-20.0%`** |
| `stall_bailout` | `1` | `0.0%` | **`-2.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `SEI`

* **Total Candidate Breakouts Filtered (Vetoed):** `411`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `309` (75.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `44`
* **Saved Capital Losses Avoided:** `+3,090.3%`
* **Missed Upside Forgone:** `-1,239.3%`
* **Net Veto Alpha:** `+1,851.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `231` | `56.2%` |
| `Core 1: Macro Bear Veto` | `153` | `37.2%` |
| `Core 4: Funding Rate Cap` | `20` | `4.9%` |
| `Core 4: Whale Firewall` | `4` | `1.0%` |
| `Core 4: Defensible Whale Dump` | `3` | `0.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*