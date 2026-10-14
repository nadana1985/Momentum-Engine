# Kronos V12: Institutional Symbol Tear Sheet — `SKYAI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+13.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.14x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+6.50%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`472.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+43.7% / -12.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-11-15 08:00` | `2025-11-19 08:00` | Live | `$0.0188` | `$0.0204` | **+8.50%** | **+8.16%** | +58.4% | -15.5% | `shelf_target_reclaim` |
| 2 | Book 4 | `2025-12-30 14:00` | `2026-01-19 06:00` | 472.0h | `$0.0375` | `$0.0450` | **+4.99%** | **+4.84%** | +29.1% | -9.7% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+4.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `SKYAI`

* **Total Candidate Breakouts Filtered (Vetoed):** `270`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `214` (79.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `49`
* **Saved Capital Losses Avoided:** `+3,181.6%`
* **Missed Upside Forgone:** `-3,048.7%`
* **Net Veto Alpha:** `+133.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `256` | `94.8%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `7` | `2.6%` |
| `Core 4: Defensible Whale Dump` | `7` | `2.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*