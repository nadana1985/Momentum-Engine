# Kronos V12: Institutional Symbol Tear Sheet — `USAR`
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
| **Cumulative Net Log Return** | **`-4.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.30%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-1.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`42.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+2.2% / -2.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-14 15:00` | `2026-09-16 03:00` | 36.0h | `$15.9899` | `$15.4712` | **-3.24%** | **-3.30%** | +0.6% | -4.2% | `stall_bailout` |
| 2 | Book 2 | `2026-09-21 13:00` | `2026-09-23 13:00` | 48.0h | `$16.5011` | `$16.2892` | **-1.28%** | **-1.29%** | +3.9% | -1.5% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.3%`** |
| `stall_bailout` | `1` | `0.0%` | **`-3.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `USAR`

* **Total Candidate Breakouts Filtered (Vetoed):** `15`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `8` (53.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+122.2%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+122.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `15` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*