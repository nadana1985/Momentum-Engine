# Kronos V12: Institutional Symbol Tear Sheet — `HPE`
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
| **Cumulative Net Log Return** | **`-0.5%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.55%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`48.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+1.1% / -9.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-11 13:00` | `2026-09-13 13:00` | 48.0h | `$61.6738` | `$61.3363` | **-0.55%** | **-0.55%** | +1.1% | -9.1% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-30 11:00` | `_Open Live_` | 161.9h | `$64.5209` | `$70.7700` | **+9.69%** | **+9.24%** | +10.8% | -5.3% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `HPE`

* **Total Candidate Breakouts Filtered (Vetoed):** `22`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `12` (54.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+68.5%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+68.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `17` | `77.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `13.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2` | `9.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*