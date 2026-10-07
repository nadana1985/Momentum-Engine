# Kronos V12: Institutional Symbol Tear Sheet — `ONDS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-19.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.82x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-6.44%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-11.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`31.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+1.9% / -6.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-27 14:00` | `2026-08-28 16:00` | 26.0h | `$8.5654` | `$7.9202` | **-7.53%** | **-7.83%** | +3.4% | -7.5% | `initial_stop` |
| 2 | Book 2 | `2026-09-14 14:00` | `2026-09-16 14:00` | 48.0h | `$7.3594` | `$7.1481` | **-2.87%** | **-2.91%** | +1.6% | -3.3% | `fast_decay_cut` |
| 3 | Book 2 | `2026-09-23 13:00` | `2026-09-24 08:00` | 19.0h | `$7.9368` | `$7.2836` | **-8.23%** | **-8.59%** | +0.9% | -8.7% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `2` | `0.0%` | **`-16.4%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-2.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `ONDS`

* **Total Candidate Breakouts Filtered (Vetoed):** `16`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `9` (56.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+116.6%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+116.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `16` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*