# Kronos V12: Institutional Symbol Tear Sheet — `ROSE`
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
| **Cumulative Net Log Return** | **`+29.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.35x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+14.92%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+24.6% / -2.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-03-13 00:00` | `2023-03-20 00:00` | 168.0h | `$0.0548` | `$0.0622` | **+13.53%** | **+12.69%** | +25.5% | -2.9% | `time_cap` |
| 2 | Book 2 | `2023-10-23 19:00` | `2023-10-30 19:00` | 168.0h | `$0.0439` | `$0.0521` | **+18.71%** | **+17.15%** | +23.6% | -1.2% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `2` | `100.0%` | **`+29.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `ROSE`

* **Total Candidate Breakouts Filtered (Vetoed):** `264`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `148` (56.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `31`
* **Saved Capital Losses Avoided:** `+1,798.2%`
* **Missed Upside Forgone:** `-833.0%`
* **Net Veto Alpha:** `+965.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `93` | `35.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `70` | `26.5%` |
| `Core 1: Macro Bear Veto` | `53` | `20.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `41` | `15.5%` |
| `Core 0: Zero-Tolerance Data Firewall` | `7` | `2.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*