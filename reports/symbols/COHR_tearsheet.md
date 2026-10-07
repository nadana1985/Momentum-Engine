# Kronos V12: Institutional Symbol Tear Sheet — `COHR`
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
| **Cumulative Net Log Return** | **`-10.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.90x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.46%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-4.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`84.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.2% / -5.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-26 19:00` | `2026-08-28 19:00` | 48.0h | `$295.2864` | `$278.5818` | **-5.66%** | **-5.82%** | +4.7% | -5.7% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-04 13:00` | `2026-09-06 01:00` | 36.0h | `$282.2439` | `$278.8312` | **-1.21%** | **-1.22%** | +0.6% | -6.3% | `stall_bailout` |
| 3 | Book 2 | `2026-09-17 11:00` | `2026-09-24 11:00` | 168.0h | `$302.3339` | `$292.3872` | **-3.29%** | **-3.35%** | +10.1% | -3.9% | `time_cap` |
| 4 | Book 2 | `2026-10-02 13:00` | `_Open Live_` | 111.9h | `$326.7147` | `$336.0200` | **+2.85%** | **+2.81%** | +5.2% | -3.6% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-5.8%`** |
| `stall_bailout` | `1` | `0.0%` | **`-1.2%`** |
| `time_cap` | `1` | `0.0%` | **`-3.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `COHR`

* **Total Candidate Breakouts Filtered (Vetoed):** `13`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `9` (69.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `1`
* **Saved Capital Losses Avoided:** `+125.4%`
* **Missed Upside Forgone:** `-23.2%`
* **Net Veto Alpha:** `+102.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `13` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*