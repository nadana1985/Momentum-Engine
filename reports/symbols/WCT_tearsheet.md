# Kronos V12: Institutional Symbol Tear Sheet — `WCT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.013`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+0.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.00x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.04%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`37.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.8% / -6.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-21 10:00` | `2025-05-22 00:00` | 14.0h | `$0.6473` | `$0.5940` | **-8.23%** | **-8.59%** | +3.7% | -9.3% | `stop_loss` |
| 2 | Book 3 | `2025-07-23 20:00` | `2025-07-24 21:00` | 25.0h | `$0.3431` | `$0.3729` | **+8.70%** | **+8.34%** | +9.0% | -5.8% | `target_reclaim` |
| 3 | Book 3 | `2025-07-25 03:00` | `2025-07-28 03:00` | 72.0h | `$0.3675` | `$0.3689` | **+0.36%** | **+0.36%** | +4.7% | -4.4% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |
| `time_expiry` | `1` | `100.0%` | **`+0.4%`** |

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