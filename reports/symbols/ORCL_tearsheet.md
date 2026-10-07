# Kronos V12: Institutional Symbol Tear Sheet — `ORCL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-2.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.97x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.28%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-2.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`126.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.1% / -2.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-26 13:00` | `2026-08-30 23:00` | 106.0h | `$150.2347` | `$149.5153` | **-0.48%** | **-0.48%** | +2.7% | -2.9% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-04 10:00` | `2026-09-10 13:00` | 147.0h | `$159.0867` | `$155.8195` | **-2.05%** | **-2.08%** | +7.4% | -2.9% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-2.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `ORCL`

* **Total Candidate Breakouts Filtered (Vetoed):** `27`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `10` (37.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+82.4%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+82.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `27` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*