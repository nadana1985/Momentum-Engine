# Kronos V12: Institutional Symbol Tear Sheet — `POPMART`
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
| **Cumulative Net Log Return** | **`-1.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.66%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-1.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`46.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+2.3% / -2.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-24 01:00` | `2026-08-26 10:00` | 57.0h | `$19.7091` | `$19.6507` | **-0.30%** | **-0.30%** | +4.1% | -3.2% | `fast_decay_cut` |
| 2 | Book 2 | `2026-10-05 03:00` | `2026-10-06 15:00` | 36.0h | `$19.2881` | `$19.0922` | **-1.02%** | **-1.02%** | +0.6% | -1.4% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.3%`** |
| `stall_bailout` | `1` | `0.0%` | **`-1.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `POPMART`

* **Total Candidate Breakouts Filtered (Vetoed):** `0`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `0` (0.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+0.0%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+0.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*