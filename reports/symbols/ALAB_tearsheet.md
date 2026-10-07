# Kronos V12: Institutional Symbol Tear Sheet — `ALAB`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`2` Closed, `1` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`11.479`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+16.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.18x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+8.07%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`108.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.1% / -3.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-26 20:00` | `2026-08-28 20:00` | 48.0h | `$294.4543` | `$289.9533` | **-1.53%** | **-1.54%** | +5.3% | -2.7% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-17 13:00` | `2026-09-24 13:00` | 168.0h | `$290.9556` | `$347.2298` | **+19.34%** | **+17.68%** | +26.9% | -4.0% | `time_cap` |
| 3 | Book 2 | `2026-10-05 15:00` | `_Open Live_` | 37.9h | `$363.6869` | `$388.4700` | **+6.81%** | **+6.59%** | +10.5% | -2.0% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.5%`** |
| `time_cap` | `1` | `100.0%` | **`+17.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `ALAB`

* **Total Candidate Breakouts Filtered (Vetoed):** `9`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `8` (88.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `2`
* **Saved Capital Losses Avoided:** `+120.0%`
* **Missed Upside Forgone:** `-42.5%`
* **Net Veto Alpha:** `+77.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `8` | `88.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `11.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*