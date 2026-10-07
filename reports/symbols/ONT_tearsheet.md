# Kronos V12: Institutional Symbol Tear Sheet — `ONT`
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
| **Cumulative Net Log Return** | **`+11.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.12x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+11.25%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.6% / -3.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-03-27 00:00` | `2022-04-03 00:00` | 168.0h | `$0.6038` | `$0.6757` | **+11.91%** | **+11.25%** | +16.6% | -3.5% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `1` | `100.0%` | **`+11.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `ONT`

* **Total Candidate Breakouts Filtered (Vetoed):** `361`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `215` (59.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `45`
* **Saved Capital Losses Avoided:** `+3,093.3%`
* **Missed Upside Forgone:** `-1,414.5%`
* **Net Veto Alpha:** `+1,678.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `110` | `30.5%` |
| `Core 0: Zero-Tolerance Data Firewall` | `108` | `29.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `82` | `22.7%` |
| `Core 1: Macro Bear Veto` | `45` | `12.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `16` | `4.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*