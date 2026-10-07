# Kronos V12: Institutional Symbol Tear Sheet — `FOGO`
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
| **Cumulative Net Log Return** | **`+8.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.09x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+8.34%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`2.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.5% / -5.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-22 05:00` | `2026-08-22 07:00` | 2.0h | `$0.0088` | `$0.0096` | **+8.70%** | **+8.34%** | +13.5% | -5.0% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `FOGO`

* **Total Candidate Breakouts Filtered (Vetoed):** `19`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `16` (84.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+248.7%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+248.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `16` | `84.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `15.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*