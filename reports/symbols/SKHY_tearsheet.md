# Kronos V12: Institutional Symbol Tear Sheet — `SKHY`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.047`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-3.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.19%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-0.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`103.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+3.3% / -2.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-31 13:00` | `2026-09-02 01:00` | 36.0h | `$165.1418` | `$159.6898` | **-3.30%** | **-3.36%** | +0.8% | -4.0% | `stall_bailout` |
| 2 | Book 2 | `2026-09-17 13:00` | `2026-09-24 13:00` | 168.0h | `$184.8610` | `$185.1859` | **+0.18%** | **+0.18%** | +6.2% | -2.1% | `time_cap` |
| 3 | Book 2 | `2026-10-01 17:00` | `2026-10-06 02:00` | 105.0h | `$190.7858` | `$190.0337` | **-0.39%** | **-0.39%** | +2.8% | -2.5% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.4%`** |
| `stall_bailout` | `1` | `0.0%` | **`-3.4%`** |
| `time_cap` | `1` | `100.0%` | **`+0.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `SKHY`

* **Total Candidate Breakouts Filtered (Vetoed):** `16`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `7` (43.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+64.7%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+64.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `6` | `37.5%` |
| `Core 4: Defensible Whale Dump` | `5` | `31.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `5` | `31.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*