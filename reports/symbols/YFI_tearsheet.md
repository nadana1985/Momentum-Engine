# Kronos V12: Institutional Symbol Tear Sheet — `YFI`
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
| **Cumulative Net Log Return** | **`+9.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.10x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+9.64%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.5% / -1.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-06-20 18:00` | `2023-06-27 18:00` | 168.0h | `$5817.5075` | `$6405.9450` | **+10.11%** | **+9.64%** | +16.5% | -1.6% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `1` | `100.0%` | **`+9.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `YFI`

* **Total Candidate Breakouts Filtered (Vetoed):** `295`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `149` (50.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `81`
* **Saved Capital Losses Avoided:** `+2,162.9%`
* **Missed Upside Forgone:** `-3,127.8%`
* **Net Veto Alpha:** `+-964.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `74` | `25.1%` |
| `Core 0: Zero-Tolerance Data Firewall` | `71` | `24.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `71` | `24.1%` |
| `Core 1: Macro Bear Veto` | `56` | `19.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `23` | `7.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*