# Kronos V12: Institutional Symbol Tear Sheet — `WMT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-4.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.95x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.20%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-3.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`46.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+1.2% / -1.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-01 14:00` | `2026-09-03 02:00` | 36.0h | `$106.9567` | `$105.7450` | **-1.13%** | **-1.14%** | +-0.1% | -1.4% | `stall_bailout` |
| 2 | Book 2 | `2026-09-14 01:00` | `2026-09-16 19:00` | 66.0h | `$107.7487` | `$107.4407` | **-0.29%** | **-0.29%** | +2.0% | -0.5% | `fast_decay_cut` |
| 3 | Book 2 | `2026-09-22 05:00` | `2026-09-24 18:00` | 61.0h | `$108.4003` | `$108.0592` | **-0.31%** | **-0.32%** | +2.8% | -0.7% | `fast_decay_cut` |
| 4 | Book 2 | `2026-09-28 13:00` | `2026-09-29 13:00` | 24.0h | `$109.3327` | `$106.0378` | **-3.01%** | **-3.06%** | +0.1% | -3.3% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-0.6%`** |
| `initial_stop` | `1` | `0.0%` | **`-3.1%`** |
| `stall_bailout` | `1` | `0.0%` | **`-1.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `WMT`

* **Total Candidate Breakouts Filtered (Vetoed):** `14`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `10` (71.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+35.3%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+35.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `14` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*