# Kronos V12: Institutional Symbol Tear Sheet — `TURBO`
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
| **Cumulative Net Log Return** | **`-1.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.09%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`55.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.8% / -2.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-05-05 07:00` | `2026-05-07 14:00` | 55.0h | `$0.0013` | `$0.0013` | **-1.08%** | **-1.09%** | +5.8% | -2.2% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `TURBO`

* **Total Candidate Breakouts Filtered (Vetoed):** `100`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `65` (65.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `37`
* **Saved Capital Losses Avoided:** `+963.4%`
* **Missed Upside Forgone:** `-1,864.0%`
* **Net Veto Alpha:** `+-900.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `48` | `48.0%` |
| `Core 1: Macro Bear Veto` | `31` | `31.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `13` | `13.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `8` | `8.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*