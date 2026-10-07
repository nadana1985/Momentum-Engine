# Kronos V12: Institutional Symbol Tear Sheet — `LITE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`3` Closed, `1` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-9.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.91x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.03%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`75.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.2% / -4.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-26 13:00` | `2026-08-28 15:00` | 50.0h | `$905.5783` | `$901.1914` | **-0.48%** | **-0.49%** | +8.0% | -4.1% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-08 13:00` | `2026-09-14 08:00` | 139.0h | `$925.9391` | `$870.8295` | **-5.95%** | **-6.14%** | +10.9% | -6.1% | `initial_stop` |
| 3 | Book 2 | `2026-09-25 16:00` | `2026-09-27 04:00` | 36.0h | `$965.1569` | `$941.5901` | **-2.44%** | **-2.47%** | +-0.2% | -3.4% | `stall_bailout` |
| 4 | Book 2 | `2026-10-06 17:00` | `_Open Live_` | 11.9h | `$1137.3362` | `$1126.4500` | **-0.96%** | **-0.96%** | +0.1% | -1.2% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.5%`** |
| `initial_stop` | `1` | `0.0%` | **`-6.1%`** |
| `stall_bailout` | `1` | `0.0%` | **`-2.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `LITE`

* **Total Candidate Breakouts Filtered (Vetoed):** `22`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `13` (59.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+166.2%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+166.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `14` | `63.6%` |
| `Core 4: Defensible Whale Dump` | `7` | `31.8%` |
| `Core 3: Min Turnover Velocity` | `1` | `4.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*