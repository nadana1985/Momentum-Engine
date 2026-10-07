# Kronos V12: Institutional Symbol Tear Sheet — `SAMSUNGEM`
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
| **Cumulative Net Log Return** | **`-4.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-4.39%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`48.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+1.9% / -4.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-22 00:00` | `2026-09-24 00:00` | 48.0h | `$1113.9980` | `$1066.1280` | **-4.30%** | **-4.39%** | +1.9% | -4.8% | `fast_decay_cut` |
| 2 | Book 2 | `2026-10-06 00:00` | `_Open Live_` | 28.9h | `$1230.3682` | `$1236.5100` | **+0.50%** | **+0.50%** | +2.7% | -2.7% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-4.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `SAMSUNGEM`

* **Total Candidate Breakouts Filtered (Vetoed):** `2`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `1` (50.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+8.1%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+8.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `1` | `50.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `50.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*