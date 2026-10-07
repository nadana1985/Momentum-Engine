# Kronos V12: Institutional Symbol Tear Sheet — `LISTA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-8.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.92x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-8.59%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`20.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+2.0% / -10.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2024-08-13 17:00` | `2024-08-14 13:00` | 20.0h | `$0.3928` | `$0.3605` | **-8.23%** | **-8.59%** | +2.0% | -10.1% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `LISTA`

* **Total Candidate Breakouts Filtered (Vetoed):** `125`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `85` (68.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `9`
* **Saved Capital Losses Avoided:** `+1,197.9%`
* **Missed Upside Forgone:** `-311.4%`
* **Net Veto Alpha:** `+886.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `79` | `63.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `35` | `28.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `7` | `5.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `3.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*