# Kronos V12: Institutional Symbol Tear Sheet — `OPN`
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
| **Cumulative Net Log Return** | **`+31.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.37x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+15.76%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+47.6% / -30.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-05-02 16:00` | `2026-05-09 16:00` | 168.0h | `$0.1696` | `$0.2051` | **+25.74%** | **+23.37%** | +28.8% | -2.5% | `time_cap` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2026-06-03 15:00` | `2026-06-07 15:00` | Live | `$0.1517` | `$0.1646` | **+8.50%** | **+8.16%** | +66.4% | -58.3% | `shelf_target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `time_cap` | `1` | `100.0%` | **`+23.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `OPN`

* **Total Candidate Breakouts Filtered (Vetoed):** `10`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `10` (100.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `2`
* **Saved Capital Losses Avoided:** `+256.4%`
* **Missed Upside Forgone:** `-85.6%`
* **Net Veto Alpha:** `+170.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `10` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*