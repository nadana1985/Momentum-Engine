# Kronos V12: Institutional Symbol Tear Sheet — `US`
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
| **Cumulative Net Log Return** | **`+3.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.04x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.47%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`5.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+22.3% / -10.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2026-06-02 02:00` | `2026-06-02 07:00` | 5.0h | `$0.0098` | `$0.0118` | **+3.55%** | **+3.47%** | +22.3% | -10.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `1` | `100.0%` | **`+3.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `US`

* **Total Candidate Breakouts Filtered (Vetoed):** `416`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `275` (66.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `181`
* **Saved Capital Losses Avoided:** `+5,165.6%`
* **Missed Upside Forgone:** `-6,035.3%`
* **Net Veto Alpha:** `+-869.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `403` | `96.9%` |
| `Core 4: Funding Rate Cap` | `13` | `3.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*