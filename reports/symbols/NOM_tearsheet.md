# Kronos V12: Institutional Symbol Tear Sheet — `NOM`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-0.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`1.00x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.27%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`69.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.1% / -4.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-19 17:00` | `2026-09-22 14:00` | 69.0h | `$0.0017` | `$0.0017` | **-0.27%** | **-0.27%** | +6.1% | -4.3% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `NOM`

* **Total Candidate Breakouts Filtered (Vetoed):** `27`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `21` (77.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `13`
* **Saved Capital Losses Avoided:** `+489.5%`
* **Missed Upside Forgone:** `-1,228.1%`
* **Net Veto Alpha:** `+-738.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `27` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*