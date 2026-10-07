# Kronos V12: Institutional Symbol Tear Sheet — `KAS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`8.281`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+4.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.05x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.33%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-0.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`164.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+19.9% / -1.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2025-04-22 04:00` | `2025-04-29 04:00` | 168.0h | `$0.0895` | `$0.0944` | **+5.44%** | **+5.30%** | +22.0% | -2.0% | `time_cap` |
| 2 | Book 1 | `2026-09-07 05:00` | `2026-09-13 22:00` | 161.0h | `$0.0333` | `$0.0331` | **-0.64%** | **-0.64%** | +17.9% | -1.7% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.6%`** |
| `time_cap` | `1` | `100.0%` | **`+5.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `KAS`

* **Total Candidate Breakouts Filtered (Vetoed):** `109`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `72` (66.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `8`
* **Saved Capital Losses Avoided:** `+781.9%`
* **Missed Upside Forgone:** `-226.9%`
* **Net Veto Alpha:** `+555.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `56` | `51.4%` |
| `Core 1: Macro Bear Veto` | `49` | `45.0%` |
| `Core 4: Funding Rate Cap` | `4` | `3.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*