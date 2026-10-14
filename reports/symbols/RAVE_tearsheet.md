# Kronos V12: Institutional Symbol Tear Sheet — `RAVE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+101.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.76x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+33.84%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`2.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+40.1% / -30.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-12-15 16:00` | `2025-12-19 16:00` | Live | `$0.4590` | `$0.4980` | **+8.50%** | **+8.16%** | +29.1% | -39.1% | `shelf_target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2026-02-19 11:00` | `2026-02-23 11:00` | Live | `$0.4103` | `$0.4452` | **+8.50%** | **+8.16%** | +62.9% | -48.0% | `shelf_target_reclaim` |
| 3 | Book 4 | `2026-04-09 13:00` | `2026-04-09 15:00` | 2.0h | `$0.3771` | `$0.4525` | **+124.08%** | **+85.20%** | +28.4% | -3.1% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `target_reclaim` | `1` | `100.0%` | **`+85.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `RAVE`

* **Total Candidate Breakouts Filtered (Vetoed):** `387`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `302` (78.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `288`
* **Saved Capital Losses Avoided:** `+16,096.9%`
* **Missed Upside Forgone:** `-65,733.3%`
* **Net Veto Alpha:** `+-49,636.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `387` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*