# Kronos V12: Institutional Symbol Tear Sheet — `1000PEPE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.623`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+27.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.32x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+6.97%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-12.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`188.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+29.1% / -5.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2025-05-08 03:00` | `2025-05-12 18:00` | 111.0h | `$0.0087` | `$0.0131` | **+49.45%** | **+40.18%** | +76.3% | -4.2% | `trail_stop` |
| 2 | Book 2 | `2025-06-29 22:00` | `2025-07-01 05:00` | 31.0h | `$0.0104` | `$0.0095` | **-8.23%** | **-8.59%** | +1.3% | -8.6% | `initial_stop` |
| 3 | Book 1 | `2025-07-09 21:00` | `2025-07-29 13:00` | 472.0h | `$0.0112` | `$0.0116` | **+4.99%** | **+4.87%** | +32.3% | -2.4% | `trail_stop` |
| 4 | Book 2 | `2025-08-08 18:00` | `2025-08-14 13:00` | 139.0h | `$0.0119` | `$0.0109` | **-8.23%** | **-8.59%** | +6.5% | -8.1% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `2` | `0.0%` | **`-17.2%`** |
| `trail_stop` | `2` | `100.0%` | **`+45.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `1000PEPE`

* **Total Candidate Breakouts Filtered (Vetoed):** `98`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `64` (65.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `34`
* **Saved Capital Losses Avoided:** `+992.3%`
* **Missed Upside Forgone:** `-1,975.9%`
* **Net Veto Alpha:** `+-983.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `46` | `46.9%` |
| `Core 4: Funding Rate Cap` | `43` | `43.9%` |
| `Core 4: Whale Firewall` | `5` | `5.1%` |
| `Core 4: Defensible Whale Dump` | `4` | `4.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*