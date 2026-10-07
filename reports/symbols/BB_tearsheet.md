# Kronos V12: Institutional Symbol Tear Sheet — `BB`
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
| **Cumulative Net Log Return** | **`+5.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.06x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+5.91%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+17.0% / -5.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2024-09-17 14:00` | `2024-09-24 14:00` | 168.0h | `$0.3408` | `$0.3616` | **+6.09%** | **+5.91%** | +17.0% | -5.3% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `1` | `100.0%` | **`+5.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `BB`

* **Total Candidate Breakouts Filtered (Vetoed):** `87`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `61` (70.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `13`
* **Saved Capital Losses Avoided:** `+888.2%`
* **Missed Upside Forgone:** `-383.0%`
* **Net Veto Alpha:** `+505.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `53` | `60.9%` |
| `Core 1: Macro Bear Veto` | `34` | `39.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*