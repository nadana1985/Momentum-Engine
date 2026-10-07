# Kronos V12: Institutional Symbol Tear Sheet — `EDEN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`2.627`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+17.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.19x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+5.71%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-10.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`31.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.0% / -6.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-26 03:00` | `2026-08-28 11:00` | 56.0h | `$0.0548` | `$0.0722` | **+31.90%** | **+27.69%** | +39.3% | -4.6% | `climax_top_harvest` |
| 2 | Book 2 | `2026-09-17 10:00` | `2026-09-17 11:00` | 1.0h | `$0.0539` | `$0.0494` | **-8.23%** | **-8.59%** | +0.8% | -8.0% | `initial_stop` |
| 3 | Book 1 | `2026-09-22 01:00` | `2026-09-23 14:00` | 37.0h | `$0.0602` | `$0.0589` | **-1.93%** | **-1.95%** | +7.9% | -6.3% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `climax_top_harvest` | `1` | `100.0%` | **`+27.7%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-2.0%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `EDEN`

* **Total Candidate Breakouts Filtered (Vetoed):** `30`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `24` (80.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `16`
* **Saved Capital Losses Avoided:** `+599.4%`
* **Missed Upside Forgone:** `-977.3%`
* **Net Veto Alpha:** `+-377.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `28` | `93.3%` |
| `Core 4: Defensible Whale Dump` | `2` | `6.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*