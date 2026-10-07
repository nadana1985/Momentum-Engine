# Kronos V12: Institutional Symbol Tear Sheet — `BAND`
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
| **Cumulative Net Log Return** | **`+19.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.22x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+19.74%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+24.7% / -1.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2025-04-19 15:00` | `2025-04-26 15:00` | 168.0h | `$0.7022` | `$0.8554` | **+21.82%** | **+19.74%** | +24.7% | -1.1% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `1` | `100.0%` | **`+19.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `BAND`

* **Total Candidate Breakouts Filtered (Vetoed):** `302`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `168` (55.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `44`
* **Saved Capital Losses Avoided:** `+2,370.8%`
* **Missed Upside Forgone:** `-2,287.5%`
* **Net Veto Alpha:** `+83.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `93` | `30.8%` |
| `Core 0: Zero-Tolerance Data Firewall` | `74` | `24.5%` |
| `Core 1: Macro Bear Veto` | `61` | `20.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `52` | `17.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `22` | `7.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*