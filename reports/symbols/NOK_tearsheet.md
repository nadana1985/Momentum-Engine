# Kronos V12: Institutional Symbol Tear Sheet — `NOK`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-4.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.37%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-1.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`40.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+2.0% / -3.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-26 23:00` | `2026-08-28 11:00` | 36.0h | `$10.7769` | `$10.5236` | **-2.35%** | **-2.38%** | +0.8% | -3.9% | `stall_bailout` |
| 2 | Book 2 | `2026-09-08 16:00` | `2026-09-10 16:00` | 48.0h | `$10.8170` | `$10.7032` | **-1.05%** | **-1.06%** | +4.4% | -3.4% | `fast_decay_cut` |
| 3 | Book 2 | `2026-10-02 12:00` | `2026-10-04 00:00` | 36.0h | `$10.6165` | `$10.5436` | **-0.69%** | **-0.69%** | +1.0% | -1.8% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `2` | `0.0%` | **`-3.1%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `NOK`

* **Total Candidate Breakouts Filtered (Vetoed):** `10`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `7` (70.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+53.9%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+53.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `10` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*