# Kronos V12: Institutional Symbol Tear Sheet — `SHOP`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+4.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.05x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.63%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.8% / -3.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-21 17:00` | `2026-09-28 17:00` | 168.0h | `$135.3174` | `$141.7248` | **+4.74%** | **+4.63%** | +11.8% | -3.5% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `1` | `100.0%` | **`+4.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `SHOP`

* **Total Candidate Breakouts Filtered (Vetoed):** `8`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `4` (50.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+17.3%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+17.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `3` | `37.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `37.5%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `12.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `12.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*