# Kronos V12: Institutional Symbol Tear Sheet — `WOO`
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
| **Cumulative Net Log Return** | **`+17.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.19x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+17.17%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+22.8% / -2.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-10-23 16:00` | `2023-10-30 16:00` | 168.0h | `$0.1899` | `$0.2254` | **+18.73%** | **+17.17%** | +22.8% | -2.0% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `1` | `100.0%` | **`+17.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `WOO`

* **Total Candidate Breakouts Filtered (Vetoed):** `239`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `155` (64.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `27`
* **Saved Capital Losses Avoided:** `+1,905.7%`
* **Missed Upside Forgone:** `-885.6%`
* **Net Veto Alpha:** `+1,020.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `80` | `33.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `64` | `26.8%` |
| `Core 1: Macro Bear Veto` | `58` | `24.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `35` | `14.6%` |
| `Core 4: Defensible Whale Dump` | `2` | `0.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*