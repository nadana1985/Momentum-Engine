# Kronos V12: Institutional Symbol Tear Sheet — `FET`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`83.3%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`12.215`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+103.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.82x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+17.25%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-9.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`59.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.7% / -3.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-04-16 01:00` | `2023-04-17 09:00` | 32.0h | `$0.4000` | `$0.4208` | **+5.20%** | **+5.07%** | +5.8% | -2.0% | `target_reclaim` |
| 2 | Book 4 | `2023-10-23 16:00` | `2023-10-25 06:00` | 38.0h | `$0.2429` | `$0.2914` | **+81.26%** | **+62.06%** | +21.0% | -2.3% | `target_reclaim` |
| 3 | Book 3 | `2024-02-28 17:00` | `2024-02-28 20:00` | 3.0h | `$1.1364` | `$1.3074` | **+15.05%** | **+14.02%** | +15.7% | -2.6% | `target_reclaim` |
| 4 | Book 2 | `2025-05-08 15:00` | `2025-05-15 15:00` | 168.0h | `$0.7445` | `$0.8785` | **+18.00%** | **+16.55%** | +22.8% | -2.1% | `climax_whale_euphoria_harvest` |
| 5 | Book 2 | `2026-09-06 20:00` | `2026-09-10 12:00` | 88.0h | `$0.1768` | `$0.1623` | **-8.84%** | **-9.23%** | +7.6% | -8.6% | `initial_stop` |
| 6 | Book 4 | `2026-09-24 04:00` | `2026-09-25 10:00` | 30.0h | `$0.1996` | `$0.2395` | **+16.02%** | **+15.04%** | +21.1% | -3.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+96.2%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+16.6%`** |
| `initial_stop` | `1` | `0.0%` | **`-9.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `FET`

* **Total Candidate Breakouts Filtered (Vetoed):** `265`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `204` (77.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `43`
* **Saved Capital Losses Avoided:** `+2,521.6%`
* **Missed Upside Forgone:** `-1,517.3%`
* **Net Veto Alpha:** `+1,004.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `223` | `84.2%` |
| `Core 4: Funding Rate Cap` | `42` | `15.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*