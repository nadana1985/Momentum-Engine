# Kronos V12: Institutional Symbol Tear Sheet — `EIGEN`
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
| **Cumulative Net Log Return** | **`+11.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.12x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+11.05%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`98.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+27.1% / -8.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2024-12-02 13:00` | `2024-12-06 15:00` | 98.0h | `$3.8333` | `$4.6000` | **+11.58%** | **+11.05%** | +27.1% | -8.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `1` | `100.0%` | **`+11.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `EIGEN`

* **Total Candidate Breakouts Filtered (Vetoed):** `382`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `245` (64.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `102`
* **Saved Capital Losses Avoided:** `+3,557.3%`
* **Missed Upside Forgone:** `-2,837.2%`
* **Net Veto Alpha:** `+720.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `349` | `91.4%` |
| `Core 1: Macro Bear Veto` | `33` | `8.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*