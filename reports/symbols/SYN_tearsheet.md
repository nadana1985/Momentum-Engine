# Kronos V12: Institutional Symbol Tear Sheet — `SYN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.250`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-24.5%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.78x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-8.17%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-32.7%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`8.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+2.1% / -23.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-02-12 02:00` | `2025-02-16 02:00` | Live | `$0.4031` | `$0.4374` | **+8.50%** | **+8.16%** | +4.3% | -36.7% | `shelf_target_reclaim` |
| 2 | Book 2 | `2026-08-20 08:00` | `2026-08-21 00:00` | 16.0h | `$0.1150` | `$0.1055` | **-8.81%** | **-9.19%** | +0.3% | -8.7% | `initial_stop` |
| 3 | Book 1 | `2026-08-22 04:00` | `2026-08-22 05:00` | 1.0h | `$0.1224` | `$0.1074` | **-21.27%** | **-23.49%** | +1.8% | -25.7% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `2` | `0.0%` | **`-32.7%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `SYN`

* **Total Candidate Breakouts Filtered (Vetoed):** `443`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `284` (64.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `356`
* **Saved Capital Losses Avoided:** `+6,837.1%`
* **Missed Upside Forgone:** `-31,897.6%`
* **Net Veto Alpha:** `+-25,060.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `412` | `93.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `31` | `7.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*