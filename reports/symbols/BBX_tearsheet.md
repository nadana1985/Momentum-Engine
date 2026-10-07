# Kronos V12: Institutional Symbol Tear Sheet — `BBX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-1.2%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.60%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-0.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`59.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+1.7% / -2.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-14 14:00` | `2026-09-16 02:00` | 36.0h | `$7.8325` | `$7.7965` | **-0.46%** | **-0.46%** | +1.0% | -2.1% | `stall_bailout` |
| 2 | Book 2 | `2026-09-30 14:00` | `2026-10-04 00:00` | 82.0h | `$9.1679` | `$9.1012` | **-0.73%** | **-0.73%** | +2.4% | -3.2% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.7%`** |
| `stall_bailout` | `1` | `0.0%` | **`-0.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `BBX`

* **Total Candidate Breakouts Filtered (Vetoed):** `15`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `7` (46.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+57.5%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+57.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `8` | `53.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `7` | `46.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*