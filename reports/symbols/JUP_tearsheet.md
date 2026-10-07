# Kronos V12: Institutional Symbol Tear Sheet — `JUP`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`2` Closed, `1` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-5.5%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.95x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.77%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-4.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`42.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+3.9% / -6.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2024-10-11 16:00` | `2024-10-13 17:00` | 49.0h | `$0.7823` | `$0.7769` | **-0.69%** | **-0.69%** | +3.6% | -3.1% | `fast_decay_cut` |
| 2 | Book 1 | `2026-08-27 18:00` | `2026-08-29 06:00` | 36.0h | `$0.2357` | `$0.2175` | **-4.73%** | **-4.84%** | +4.1% | -9.2% | `fast_decay_cut` |
| 3 | Book 2 | `2026-10-06 16:00` | `_Open Live_` | 12.9h | `$0.3588` | `$0.3417` | **-4.76%** | **-4.88%** | +0.2% | -5.0% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-5.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `JUP`

* **Total Candidate Breakouts Filtered (Vetoed):** `160`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `101` (63.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `18`
* **Saved Capital Losses Avoided:** `+1,085.7%`
* **Missed Upside Forgone:** `-812.0%`
* **Net Veto Alpha:** `+273.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `95` | `59.4%` |
| `Core 1: Macro Bear Veto` | `65` | `40.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*