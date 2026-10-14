# Kronos V12: Institutional Symbol Tear Sheet — `ONG`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`75.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`28.353`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+41.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.52x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+10.40%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-1.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`116.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+40.9% / -6.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2024-03-05 23:00` | `2024-03-13 19:00` | 188.0h | `$0.3974` | `$0.4769` | **+16.40%** | **+15.38%** | +20.4% | -4.9% | `target_reclaim` |
| 2 | Book 2 | `2024-09-13 15:00` | `2024-09-15 15:00` | 48.0h | `$0.2803` | `$0.2766` | **-1.51%** | **-1.52%** | +1.6% | -2.1% | `fast_decay_cut` |
| 3 | Book 4 | `2024-11-16 08:00` | `2024-11-24 06:00` | 190.0h | `$0.3344` | `$0.4012` | **+25.54%** | **+23.16%** | +30.2% | -4.5% | `target_reclaim` |
| 4 | Book 4 | `2026-08-20 13:00` | `2026-08-22 05:00` | 40.0h | `$0.0758` | `$0.0645` | **+4.82%** | **+4.61%** | +111.6% | -15.6% | `structural_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+38.5%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.5%`** |
| `structural_stop` | `1` | `100.0%` | **`+4.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `ONG`

* **Total Candidate Breakouts Filtered (Vetoed):** `757`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `333` (44.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `59`
* **Saved Capital Losses Avoided:** `+5,311.0%`
* **Missed Upside Forgone:** `-1,639.4%`
* **Net Veto Alpha:** `+3,671.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `702` | `92.7%` |
| `Core 1: Macro Bear Veto` | `53` | `7.0%` |
| `Core 4: Defensible Whale Dump` | `1` | `0.1%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*