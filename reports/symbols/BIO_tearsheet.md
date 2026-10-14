# Kronos V12: Institutional Symbol Tear Sheet — `BIO`
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
| **Cumulative Net Log Return** | **`+5.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.05x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+5.06%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`2.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+18.3% / -5.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2026-05-02 11:00` | `2026-05-02 13:00` | 2.0h | `$0.0518` | `$0.0595` | **+5.19%** | **+5.06%** | +18.3% | -5.1% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `1` | `100.0%` | **`+5.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `BIO`

* **Total Candidate Breakouts Filtered (Vetoed):** `178`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `149` (83.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `71`
* **Saved Capital Losses Avoided:** `+3,406.5%`
* **Missed Upside Forgone:** `-3,680.8%`
* **Net Veto Alpha:** `+-274.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `145` | `81.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `33` | `18.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*