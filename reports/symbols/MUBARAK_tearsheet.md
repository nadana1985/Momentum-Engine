# Kronos V12: Institutional Symbol Tear Sheet — `MUBARAK`
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
| **Cumulative Net Log Return** | **`+22.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.26x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+22.83%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`42.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+48.2% / -1.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-02 13:00` | `2026-09-04 07:00` | 42.0h | `$0.0226` | `$0.0285` | **+25.65%** | **+22.83%** | +48.2% | -1.7% | `trail_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `trail_stop` | `1` | `100.0%` | **`+22.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `MUBARAK`

* **Total Candidate Breakouts Filtered (Vetoed):** `43`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `31` (72.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `19`
* **Saved Capital Losses Avoided:** `+631.6%`
* **Missed Upside Forgone:** `-1,135.3%`
* **Net Veto Alpha:** `+-503.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `26` | `60.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `12` | `27.9%` |
| `Core 4: Funding Rate Cap` | `5` | `11.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*