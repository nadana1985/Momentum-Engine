# Kronos V12: Institutional Symbol Tear Sheet — `SQQQ`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`2` Closed, `1` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-4.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.07%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-1.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`42.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+0.9% / -3.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-28 14:00` | `2026-09-30 02:00` | 36.0h | `$35.4384` | `$34.6631` | **-2.32%** | **-2.35%** | +0.2% | -3.3% | `stall_bailout` |
| 2 | Book 2 | `2026-10-08 16:00` | `2026-10-10 16:00` | 48.0h | `$33.4133` | `$32.8676` | **-1.77%** | **-1.79%** | +1.7% | -3.0% | `fast_decay_cut` |
| 3 | Book 2 | `2026-10-12 13:00` | `_Open Live_` | 23.2h | `$33.5236` | `$34.4500` | **+3.12%** | **+3.08%** | +3.3% | -1.3% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.8%`** |
| `stall_bailout` | `1` | `0.0%` | **`-2.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `SQQQ`

* **Total Candidate Breakouts Filtered (Vetoed):** `23`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `15` (65.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+119.5%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+119.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `20` | `87.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `2` | `8.7%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `4.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*