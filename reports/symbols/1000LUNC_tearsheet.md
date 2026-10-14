# Kronos V12: Institutional Symbol Tear Sheet — `1000LUNC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`40.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.275`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+27.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.32x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+5.48%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-9.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`148.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.8% / -12.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2023-06-04 14:00` | `2023-06-08 14:00` | Live | `$0.0944` | `$0.1024` | **+8.50%** | **+8.16%** | +1.9% | -29.7% | `shelf_target_reclaim` |
| 2 | Book 4 | `2024-05-30 15:00` | `2024-06-06 15:00` | 168.0h | `$0.1252` | `$0.1185` | **-2.91%** | **-3.00%** | +0.5% | -8.7% | `stagnation_cut` |
| 3 | Book 4 | `2026-02-28 19:00` | `2026-03-07 19:00` | 168.0h | `$0.0466` | `$0.0405` | **-6.19%** | **-6.40%** | +3.1% | -13.1% | `stagnation_cut` |
| 4 | Book 4 | `2026-04-16 03:00` | `2026-04-23 23:00` | 188.0h | `$0.0429` | `$0.0515` | **+35.76%** | **+31.30%** | +22.9% | -5.2% | `target_reclaim` |
| 5 | Book 2 | `2026-09-20 16:00` | `2026-09-23 14:00` | 70.0h | `$0.0550` | `$0.0535` | **-2.61%** | **-2.65%** | +5.6% | -6.0% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stagnation_cut` | `2` | `0.0%` | **`-9.4%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-2.6%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+31.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `1000LUNC`

* **Total Candidate Breakouts Filtered (Vetoed):** `732`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `437` (59.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `286`
* **Saved Capital Losses Avoided:** `+6,862.6%`
* **Missed Upside Forgone:** `-9,704.7%`
* **Net Veto Alpha:** `+-2,842.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `520` | `71.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `197` | `26.9%` |
| `Core 4: Defensible Whale Dump` | `7` | `1.0%` |
| `Core 4: Whale Firewall` | `4` | `0.5%` |
| `Core 4: Funding Rate Cap` | `3` | `0.4%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*