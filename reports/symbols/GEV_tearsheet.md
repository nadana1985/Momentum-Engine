# Kronos V12: Institutional Symbol Tear Sheet — `GEV`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`1` Closed, `1` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-0.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.75%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`166.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+4.8% / -2.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-03 14:00` | `2026-09-10 12:00` | 166.0h | `$937.3676` | `$930.3782` | **-0.75%** | **-0.75%** | +4.8% | -2.3% | `fast_decay_cut` |
| 2 | Book 2 | `2026-10-06 13:00` | `_Open Live_` | 15.9h | `$1052.6250` | `$1030.0300` | **-2.15%** | **-2.17%** | +0.0% | -5.2% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `GEV`

* **Total Candidate Breakouts Filtered (Vetoed):** `10`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `6` (60.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+58.3%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+58.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `6` | `60.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `30.0%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `10.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*