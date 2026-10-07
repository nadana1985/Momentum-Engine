# Kronos V12: Institutional Symbol Tear Sheet — `RKLB`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+10.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.11x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+10.53%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.2% / -3.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-15 11:00` | `2026-09-22 11:00` | 168.0h | `$64.1299` | `$71.2514` | **+11.10%** | **+10.53%** | +13.2% | -3.5% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `1` | `100.0%` | **`+10.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `RKLB`

* **Total Candidate Breakouts Filtered (Vetoed):** `15`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `10` (66.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+125.1%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+125.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `15` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*