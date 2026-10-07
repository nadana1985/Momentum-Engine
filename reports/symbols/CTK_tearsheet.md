# Kronos V12: Institutional Symbol Tear Sheet — `CTK`
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
| **Cumulative Net Log Return** | **`+0.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.01x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.78%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`72.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.2% / -3.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-23 05:00` | `2026-08-26 05:00` | 72.0h | `$0.1122` | `$0.1131` | **+0.78%** | **+0.78%** | +6.2% | -3.3% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_expiry` | `1` | `100.0%` | **`+0.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `CTK`

* **Total Candidate Breakouts Filtered (Vetoed):** `55`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `47` (85.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `4`
* **Saved Capital Losses Avoided:** `+479.9%`
* **Missed Upside Forgone:** `-101.6%`
* **Net Veto Alpha:** `+378.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `29` | `52.7%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `22` | `40.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `7.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*