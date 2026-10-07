# Kronos V12: Institutional Symbol Tear Sheet — `JTO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.014`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-14.0%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.87x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-4.67%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-13.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`48.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.2% / -11.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2025-04-22 16:00` | `2025-04-24 16:00` | 48.0h | `$1.8182` | `$1.8101` | **-0.45%** | **-0.45%** | +4.7% | -7.0% | `fast_decay_cut` |
| 2 | Book 1 | `2026-08-21 22:00` | `2026-08-22 05:00` | 7.0h | `$0.6463` | `$0.5673` | **-12.85%** | **-13.76%** | +4.8% | -23.4% | `initial_stop` |
| 3 | Book 1 | `2026-09-25 09:00` | `2026-09-29 02:00` | 89.0h | `$0.5341` | `$0.5355` | **+0.20%** | **+0.20%** | +21.0% | -3.5% | `breakeven_ratchet` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.2%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.5%`** |
| `initial_stop` | `1` | `0.0%` | **`-13.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `JTO`

* **Total Candidate Breakouts Filtered (Vetoed):** `120`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `81` (67.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `13`
* **Saved Capital Losses Avoided:** `+1,217.4%`
* **Missed Upside Forgone:** `-413.6%`
* **Net Veto Alpha:** `+803.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `62` | `51.7%` |
| `Core 1: Macro Bear Veto` | `55` | `45.8%` |
| `Core 4: Funding Rate Cap` | `3` | `2.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*