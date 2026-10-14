# Kronos V12: Institutional Symbol Tear Sheet — `W`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.573`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+6.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.07x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.19%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-1.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`54.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+1.9% / -19.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-03-23 03:00` | `2025-03-27 03:00` | Live | `$0.1068` | `$0.1159` | **+8.50%** | **+8.16%** | +0.2% | -37.0% | `shelf_target_reclaim` |
| 2 | Book 2 | `2026-05-04 18:00` | `2026-05-07 00:00` | 54.0h | `$0.0138` | `$0.0136` | **-1.77%** | **-1.78%** | +3.7% | -2.8% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.8%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `W`

* **Total Candidate Breakouts Filtered (Vetoed):** `204`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `173` (84.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `6`
* **Saved Capital Losses Avoided:** `+2,909.2%`
* **Missed Upside Forgone:** `-140.8%`
* **Net Veto Alpha:** `+2,768.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `171` | `83.8%` |
| `Core 1: Macro Bear Veto` | `33` | `16.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*