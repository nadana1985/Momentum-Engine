# Kronos V12: Institutional Symbol Tear Sheet — `PROVE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.283`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+1.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.02x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.90%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-6.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`72.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.8% / -16.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2026-05-21 04:00` | `2026-05-25 04:00` | Live | `$0.2295` | `$0.2491` | **+8.50%** | **+8.16%** | +25.1% | -26.1% | `shelf_target_reclaim` |
| 2 | Book 3 | `2026-10-02 08:00` | `2026-10-05 08:00` | 72.0h | `$0.2263` | `$0.2124` | **-6.16%** | **-6.36%** | +2.6% | -7.6% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `time_expiry` | `1` | `0.0%` | **`-6.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `PROVE`

* **Total Candidate Breakouts Filtered (Vetoed):** `62`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `53` (85.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `5`
* **Saved Capital Losses Avoided:** `+579.2%`
* **Missed Upside Forgone:** `-151.0%`
* **Net Veto Alpha:** `+428.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `30` | `48.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `17` | `27.4%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `14` | `22.6%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `1` | `1.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*