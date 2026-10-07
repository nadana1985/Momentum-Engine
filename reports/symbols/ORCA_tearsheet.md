# Kronos V12: Institutional Symbol Tear Sheet — `ORCA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-10.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.90x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-5.41%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-1.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`101.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.8% / -9.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-07 00:00` | `2026-09-13 22:00` | 166.0h | `$1.5037` | `$1.3200` | **-9.34%** | **-9.81%** | +13.3% | -12.2% | `initial_stop` |
| 2 | Book 2 | `2026-09-23 12:00` | `2026-09-25 00:00` | 36.0h | `$1.5920` | `$1.5761` | **-1.00%** | **-1.01%** | +0.3% | -6.4% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-9.8%`** |
| `stall_bailout` | `1` | `0.0%` | **`-1.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `ORCA`

* **Total Candidate Breakouts Filtered (Vetoed):** `36`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `26` (72.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `9`
* **Saved Capital Losses Avoided:** `+389.0%`
* **Missed Upside Forgone:** `-345.7%`
* **Net Veto Alpha:** `+43.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `25` | `69.4%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `11` | `30.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*