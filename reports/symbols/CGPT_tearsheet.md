# Kronos V12: Institutional Symbol Tear Sheet — `CGPT`
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
| **Cumulative Net Log Return** | **`+28.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.33x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+28.49%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`114.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+38.1% / -3.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2025-04-21 13:00` | `2025-04-26 07:00` | 114.0h | `$0.0804` | `$0.1069` | **+32.97%** | **+28.49%** | +38.1% | -3.4% | `climax_top_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `climax_top_harvest` | `1` | `100.0%` | **`+28.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `CGPT`

* **Total Candidate Breakouts Filtered (Vetoed):** `64`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `49` (76.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `8`
* **Saved Capital Losses Avoided:** `+675.8%`
* **Missed Upside Forgone:** `-218.3%`
* **Net Veto Alpha:** `+457.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `41` | `64.1%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `19` | `29.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `6.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*