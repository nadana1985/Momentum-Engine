# Kronos V12: Institutional Symbol Tear Sheet — `KAITO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-15.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.85x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-5.28%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-13.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`30.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+2.8% / -10.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2025-04-20 04:00` | `2025-04-22 04:00` | 48.0h | `$0.7878` | `$0.7704` | **-2.21%** | **-2.23%** | +1.8% | -6.9% | `fast_decay_cut` |
| 2 | Book 1 | `2026-05-05 01:00` | `2026-05-06 13:00` | 36.0h | `$0.5129` | `$0.4943` | **-4.89%** | **-5.02%** | +0.7% | -8.2% | `fast_decay_cut` |
| 3 | Book 2 | `2026-08-21 22:00` | `2026-08-22 05:00` | 7.0h | `$0.3911` | `$0.3589` | **-8.23%** | **-8.59%** | +5.9% | -17.3% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-7.3%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `KAITO`

* **Total Candidate Breakouts Filtered (Vetoed):** `84`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `63` (75.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `11`
* **Saved Capital Losses Avoided:** `+838.9%`
* **Missed Upside Forgone:** `-350.8%`
* **Net Veto Alpha:** `+488.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `62` | `73.8%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `22` | `26.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*