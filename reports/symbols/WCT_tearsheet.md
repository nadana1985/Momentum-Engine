# Kronos V12: Institutional Symbol Tear Sheet — `WCT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.856`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-2.5%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.98x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.62%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`15.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.3% / -9.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-21 10:00` | `2025-05-22 00:00` | 14.0h | `$0.6473` | `$0.5940` | **-8.23%** | **-8.59%** | +3.7% | -9.3% | `stop_loss` |
| 2 | Book 3 | `2025-07-23 20:00` | `2025-07-24 21:00` | 25.0h | `$0.3492` | `$0.3729` | **+6.77%** | **+6.55%** | +7.1% | -7.5% | `target_reclaim` |
| 3 | Book 3 | `2025-07-25 00:00` | `2025-07-25 06:00` | 6.0h | `$0.3835` | `$0.3520` | **-8.23%** | **-8.59%** | +7.5% | -8.4% | `stop_loss` |
| 4 | Book 5 (Shelf Absorption Squeeze) | `2025-12-30 10:00` | `2026-01-03 10:00` | Live | `$0.0781` | `$0.0848` | **+8.50%** | **+8.16%** | +7.1% | -13.4% | `shelf_target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+6.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `WCT`

* **Total Candidate Breakouts Filtered (Vetoed):** `48`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `43` (89.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `8`
* **Saved Capital Losses Avoided:** `+739.2%`
* **Missed Upside Forgone:** `-277.1%`
* **Net Veto Alpha:** `+462.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `20` | `41.7%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `14` | `29.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `14` | `29.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*