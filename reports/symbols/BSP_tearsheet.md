# Kronos V12: Institutional Symbol Tear Sheet — `BSP`
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
| **Cumulative Net Log Return** | **`-12.2%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.88x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-6.12%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-5.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`42.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+1.1% / -6.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-27 19:00` | `2026-08-29 19:00` | 48.0h | `$46.1852` | `$43.2017` | **-6.46%** | **-6.68%** | +1.6% | -7.2% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-10 15:00` | `2026-09-12 03:00` | 36.0h | `$41.1526` | `$38.9225` | **-5.42%** | **-5.57%** | +0.6% | -5.9% | `stall_bailout` |
| 3 | Book 2 | `2026-10-06 16:00` | `_Open Live_` | 12.9h | `$33.9948` | `$33.2400` | **-2.22%** | **-2.25%** | +0.1% | -3.6% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-6.7%`** |
| `stall_bailout` | `1` | `0.0%` | **`-5.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `BSP`

* **Total Candidate Breakouts Filtered (Vetoed):** `9`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `4` (44.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `1`
* **Saved Capital Losses Avoided:** `+65.0%`
* **Missed Upside Forgone:** `-27.1%`
* **Net Veto Alpha:** `+38.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `6` | `66.7%` |
| `Core 0: Zero-Tolerance Data Firewall` | `3` | `33.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*