# Kronos V12: Institutional Symbol Tear Sheet — `RLC`
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
| **Cumulative Net Log Return** | **`+15.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.17x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+15.51%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+21.9% / -5.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-19 23:00` | `2026-09-26 23:00` | 168.0h | `$0.3136` | `$0.3662` | **+16.77%** | **+15.51%** | +21.9% | -5.6% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `1` | `100.0%` | **`+15.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `RLC`

* **Total Candidate Breakouts Filtered (Vetoed):** `295`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `194` (65.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `50`
* **Saved Capital Losses Avoided:** `+2,925.4%`
* **Missed Upside Forgone:** `-2,476.0%`
* **Net Veto Alpha:** `+449.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `93` | `31.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `74` | `25.1%` |
| `Core 1: Macro Bear Veto` | `59` | `20.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `46` | `15.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `23` | `7.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*