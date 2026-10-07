# Kronos V12: Institutional Symbol Tear Sheet — `ARPA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+38.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.47x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+19.21%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`133.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+31.2% / -5.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-03-12 23:00` | `2023-03-17 02:00` | 99.0h | `$0.0344` | `$0.0462` | **+34.35%** | **+29.53%** | +42.6% | -4.4% | `climax_top_harvest` |
| 2 | Book 2 | `2023-06-20 18:00` | `2023-06-27 18:00` | 168.0h | `$0.0520` | `$0.0569` | **+9.30%** | **+8.89%** | +19.8% | -5.9% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `climax_top_harvest` | `1` | `100.0%` | **`+29.5%`** |
| `time_cap` | `1` | `100.0%` | **`+8.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `ARPA`

* **Total Candidate Breakouts Filtered (Vetoed):** `162`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `114` (70.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `20`
* **Saved Capital Losses Avoided:** `+1,493.9%`
* **Missed Upside Forgone:** `-694.2%`
* **Net Veto Alpha:** `+799.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `62` | `38.3%` |
| `Core 1: Macro Bear Veto` | `52` | `32.1%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `39` | `24.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `6` | `3.7%` |
| `Core 0: Zero-Tolerance Data Firewall` | `3` | `1.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*