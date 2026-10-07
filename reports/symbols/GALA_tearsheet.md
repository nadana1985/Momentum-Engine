# Kronos V12: Institutional Symbol Tear Sheet — `GALA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+38.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.47x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+19.24%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`174.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+35.0% / -8.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2024-02-21 05:00` | `2024-02-28 17:00` | 180.0h | `$0.0288` | `$0.0353` | **+24.16%** | **+21.64%** | +50.0% | -9.0% | `trail_stop` |
| 2 | Book 2 | `2024-09-18 02:00` | `2024-09-25 02:00` | 168.0h | `$0.0187` | `$0.0222` | **+18.35%** | **+16.85%** | +20.0% | -7.5% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `1` | `100.0%` | **`+16.8%`** |
| `trail_stop` | `1` | `100.0%` | **`+21.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `GALA`

* **Total Candidate Breakouts Filtered (Vetoed):** `156`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `83` (53.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `47`
* **Saved Capital Losses Avoided:** `+1,044.3%`
* **Missed Upside Forgone:** `-2,471.1%`
* **Net Veto Alpha:** `+-1,426.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `82` | `52.6%` |
| `Core 1: Macro Bear Veto` | `39` | `25.0%` |
| `Core 0: Zero-Tolerance Data Firewall` | `27` | `17.3%` |
| `Core 4: Funding Rate Cap` | `7` | `4.5%` |
| `Core 4: Whale Firewall` | `1` | `0.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*