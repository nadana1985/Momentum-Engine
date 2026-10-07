# Kronos V12: Institutional Symbol Tear Sheet — `AIGENSYN`
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
| **Cumulative Net Log Return** | **`+0.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.00x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.45%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`72.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+3.4% / -3.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-09-28 07:00` | `2026-10-01 07:00` | 72.0h | `$0.0203` | `$0.0204` | **+0.45%** | **+0.45%** | +3.4% | -3.5% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_expiry` | `1` | `100.0%` | **`+0.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `AIGENSYN`

* **Total Candidate Breakouts Filtered (Vetoed):** `7`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `3` (42.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `2`
* **Saved Capital Losses Avoided:** `+49.2%`
* **Missed Upside Forgone:** `-70.3%`
* **Net Veto Alpha:** `+-21.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `5` | `71.4%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `2` | `28.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*