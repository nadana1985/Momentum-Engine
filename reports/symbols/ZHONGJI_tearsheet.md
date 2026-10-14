# Kronos V12: Institutional Symbol Tear Sheet — `ZHONGJI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-6.5%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.94x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.26%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-3.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`60.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+1.7% / -4.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-09-23 03:00` | `2026-09-26 03:00` | 72.0h | `$151.9720` | `$147.2809` | **-3.09%** | **-3.14%** | +2.1% | -5.5% | `time_expiry` |
| 2 | Book 2 | `2026-10-05 02:00` | `2026-10-07 02:00` | 48.0h | `$141.5129` | `$136.9169` | **-3.33%** | **-3.38%** | +1.3% | -3.3% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-3.4%`** |
| `time_expiry` | `1` | `0.0%` | **`-3.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `ZHONGJI`

* **Total Candidate Breakouts Filtered (Vetoed):** `7`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `7` (100.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+82.7%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+82.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `7` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*