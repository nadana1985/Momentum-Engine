# Kronos V12: Institutional Symbol Tear Sheet — `NEIRO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.586`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+19.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.22x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+9.81%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-7.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`108.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.7% / -7.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2025-04-22 14:00` | `2025-04-24 14:00` | 48.0h | `$0.0002` | `$0.0002` | **+31.10%** | **+27.20%** | +24.9% | -3.1% | `target_reclaim` |
| 2 | Book 4 | `2026-08-22 05:00` | `2026-08-29 05:00` | 168.0h | `$0.0001` | `$0.0001` | **-7.33%** | **-7.58%** | +2.6% | -11.2% | `stagnation_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stagnation_cut` | `1` | `0.0%` | **`-7.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+27.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `NEIRO`

* **Total Candidate Breakouts Filtered (Vetoed):** `54`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `41` (75.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `20`
* **Saved Capital Losses Avoided:** `+676.9%`
* **Missed Upside Forgone:** `-1,191.1%`
* **Net Veto Alpha:** `+-514.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `32` | `59.3%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `22` | `40.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*