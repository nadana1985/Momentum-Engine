# Kronos V12: Institutional Symbol Tear Sheet — `SPK`
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
| **Cumulative Net Log Return** | **`+12.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.14x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+12.78%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`13.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+23.3% / -1.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-21 07:00` | `2025-07-21 20:00` | 13.0h | `$0.0411` | `$0.0467` | **+13.64%** | **+12.78%** | +23.3% | -1.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `1` | `100.0%` | **`+12.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `SPK`

* **Total Candidate Breakouts Filtered (Vetoed):** `34`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `16` (47.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `22`
* **Saved Capital Losses Avoided:** `+294.1%`
* **Missed Upside Forgone:** `-2,207.7%`
* **Net Veto Alpha:** `+-1,913.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `24` | `70.6%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `10` | `29.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*