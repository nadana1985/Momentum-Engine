# Kronos V12: Institutional Symbol Tear Sheet — `SSV`
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
| **Cumulative Net Log Return** | **`+2.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.02x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.43%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.6% / -5.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-18 23:00` | `2026-09-25 23:00` | 168.0h | `$3.1388` | `$3.2159` | **+2.46%** | **+2.43%** | +11.6% | -5.2% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `1` | `100.0%` | **`+2.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `SSV`

* **Total Candidate Breakouts Filtered (Vetoed):** `141`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `83` (58.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `25`
* **Saved Capital Losses Avoided:** `+1,155.3%`
* **Missed Upside Forgone:** `-846.7%`
* **Net Veto Alpha:** `+308.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `61` | `43.3%` |
| `Core 1: Macro Bear Veto` | `43` | `30.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `19` | `13.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `18` | `12.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*