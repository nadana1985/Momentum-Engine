# Kronos V12: Institutional Symbol Tear Sheet — `SUPER`
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
| **Cumulative Net Log Return** | **`+3.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.03x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.00%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.4% / -2.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-03 15:00` | `2026-09-10 15:00` | 168.0h | `$0.1132` | `$0.1167` | **+3.04%** | **+3.00%** | +13.4% | -2.5% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `1` | `100.0%` | **`+3.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `SUPER`

* **Total Candidate Breakouts Filtered (Vetoed):** `165`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `88` (53.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `25`
* **Saved Capital Losses Avoided:** `+1,159.5%`
* **Missed Upside Forgone:** `-670.7%`
* **Net Veto Alpha:** `+488.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `90` | `54.5%` |
| `Core 1: Macro Bear Veto` | `29` | `17.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `23` | `13.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `23` | `13.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*