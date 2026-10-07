# Kronos V12: Institutional Symbol Tear Sheet — `CVC`
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
| **Cumulative Net Log Return** | **`+0.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.01x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.62%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`72.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+4.1% / -6.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-23 21:00` | `2025-07-26 21:00` | 72.0h | `$0.1030` | `$0.1036` | **+0.62%** | **+0.62%** | +4.1% | -6.4% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_expiry` | `1` | `100.0%` | **`+0.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `CVC`

* **Total Candidate Breakouts Filtered (Vetoed):** `33`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `24` (72.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `4`
* **Saved Capital Losses Avoided:** `+305.2%`
* **Missed Upside Forgone:** `-208.4%`
* **Net Veto Alpha:** `+96.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `12` | `36.4%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `10` | `30.3%` |
| `Core 1: Macro Bear Veto` | `8` | `24.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `3` | `9.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*