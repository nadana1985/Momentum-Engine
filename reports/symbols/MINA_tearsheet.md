# Kronos V12: Institutional Symbol Tear Sheet — `MINA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+29.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.34x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+29.32%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`116.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+39.9% / -3.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-07 09:00` | `2026-09-12 05:00` | 116.0h | `$0.0817` | `$0.1096` | **+34.07%** | **+29.32%** | +39.9% | -3.7% | `climax_top_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `climax_top_harvest` | `1` | `100.0%` | **`+29.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `MINA`

* **Total Candidate Breakouts Filtered (Vetoed):** `120`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `77` (64.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `4`
* **Saved Capital Losses Avoided:** `+988.7%`
* **Missed Upside Forgone:** `-175.4%`
* **Net Veto Alpha:** `+813.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `69` | `57.5%` |
| `Core 1: Macro Bear Veto` | `42` | `35.0%` |
| `Core 4: Funding Rate Cap` | `9` | `7.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*