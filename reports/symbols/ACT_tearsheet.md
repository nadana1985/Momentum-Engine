# Kronos V12: Institutional Symbol Tear Sheet — `ACT`
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
| **Cumulative Net Log Return** | **`+7.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.07x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+7.21%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.7% / -2.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-05-02 15:00` | `2026-05-09 15:00` | 168.0h | `$0.0148` | `$0.0159` | **+7.47%** | **+7.21%** | +15.7% | -2.5% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `1` | `100.0%` | **`+7.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `ACT`

* **Total Candidate Breakouts Filtered (Vetoed):** `28`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `24` (85.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `5`
* **Saved Capital Losses Avoided:** `+408.2%`
* **Missed Upside Forgone:** `-180.0%`
* **Net Veto Alpha:** `+228.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `20` | `71.4%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `7` | `25.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `3.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*