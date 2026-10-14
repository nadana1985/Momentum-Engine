# Kronos V12: Institutional Symbol Tear Sheet — `CAT`
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
| **Cumulative Net Log Return** | **`-3.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.97x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.66%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-2.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`54.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+1.5% / -2.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-10-02 12:00` | `2026-10-05 13:00` | 73.0h | `$842.2203` | `$831.6956` | **-1.30%** | **-1.30%** | +2.1% | -2.0% | `fast_decay_cut` |
| 2 | Book 3 | `2026-10-07 14:00` | `2026-10-09 02:00` | 36.0h | `$818.0417` | `$801.7307` | **-1.99%** | **-2.01%** | +1.0% | -3.2% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.3%`** |
| `stall_bailout` | `1` | `0.0%` | **`-2.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `CAT`

* **Total Candidate Breakouts Filtered (Vetoed):** `4`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `2` (50.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+11.8%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+11.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `2` | `50.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `2` | `50.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*