# Kronos V12: Institutional Symbol Tear Sheet — `SFP`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`14.663`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+7.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.08x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.86%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`110.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.6% / -2.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-10-06 10:00` | `2023-10-08 14:00` | 52.0h | `$0.6191` | `$0.6157` | **-0.56%** | **-0.56%** | +3.0% | -2.1% | `fast_decay_cut` |
| 2 | Book 2 | `2023-10-23 22:00` | `2023-10-30 22:00` | 168.0h | `$0.6553` | `$0.7119` | **+8.63%** | **+8.28%** | +14.3% | -2.0% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.6%`** |
| `time_cap` | `1` | `100.0%` | **`+8.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `SFP`

* **Total Candidate Breakouts Filtered (Vetoed):** `217`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `143` (65.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `19`
* **Saved Capital Losses Avoided:** `+1,735.3%`
* **Missed Upside Forgone:** `-804.8%`
* **Net Veto Alpha:** `+930.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `80` | `36.9%` |
| `Core 0: Zero-Tolerance Data Firewall` | `47` | `21.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `43` | `19.8%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `37` | `17.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `7` | `3.2%` |
| `Core 4: Defensible Whale Dump` | `2` | `0.9%` |
| `Core 3: Min Turnover Velocity` | `1` | `0.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*