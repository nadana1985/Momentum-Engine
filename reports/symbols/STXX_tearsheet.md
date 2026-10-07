# Kronos V12: Institutional Symbol Tear Sheet — `STXX`
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
| **Cumulative Net Log Return** | **`-10.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.90x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-5.30%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`36.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+0.5% / -5.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-18 19:00` | `2026-09-20 19:00` | 48.0h | `$862.1099` | `$844.9124` | **-1.99%** | **-2.01%** | +1.2% | -2.8% | `fast_decay_cut` |
| 2 | Book 2 | `2026-10-05 13:00` | `2026-10-06 13:00` | 24.0h | `$902.9517` | `$828.6388` | **-8.23%** | **-8.59%** | +-0.1% | -8.5% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-2.0%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `STXX`

* **Total Candidate Breakouts Filtered (Vetoed):** `15`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `8` (53.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+102.1%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+102.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `13` | `86.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `2` | `13.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*