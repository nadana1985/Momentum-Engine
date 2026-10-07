# Kronos V12: Institutional Symbol Tear Sheet — `NET`
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
| **Mean Net Log Return / Trade** | **`-0.65%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`163.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.6% / -2.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-21 14:00` | `2026-09-28 09:00` | 163.0h | `$344.9603` | `$342.7111` | **-0.65%** | **-0.65%** | +6.6% | -2.0% | `fast_decay_cut` |
| 2 | Book 2 | `2026-10-05 13:00` | `_Open Live_` | 39.9h | `$356.6895` | `$355.2600` | **-0.40%** | **-0.40%** | +3.8% | -2.1% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `NET`

* **Total Candidate Breakouts Filtered (Vetoed):** `11`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `4` (36.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+17.5%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+17.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `9` | `81.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `9.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `9.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*