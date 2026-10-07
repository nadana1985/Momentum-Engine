# Kronos V12: Institutional Symbol Tear Sheet — `XBI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-6.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.94x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.09%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-4.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`35.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+0.7% / -2.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-02 13:00` | `2026-09-04 13:00` | 48.0h | `$165.5729` | `$162.7920` | **-1.68%** | **-1.69%** | +1.5% | -1.9% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-14 15:00` | `2026-09-15 14:00` | 23.0h | `$158.8662` | `$152.2459` | **-4.17%** | **-4.26%** | +0.1% | -4.1% | `initial_stop` |
| 3 | Book 2 | `2026-09-28 16:00` | `2026-09-30 04:00` | 36.0h | `$157.3724` | `$156.8569` | **-0.33%** | **-0.33%** | +0.4% | -1.7% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.7%`** |
| `initial_stop` | `1` | `0.0%` | **`-4.3%`** |
| `stall_bailout` | `1` | `0.0%` | **`-0.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `XBI`

* **Total Candidate Breakouts Filtered (Vetoed):** `17`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `16` (94.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+49.1%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+49.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `10` | `58.8%` |
| `Core 1: Macro Bear Veto` | `7` | `41.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*