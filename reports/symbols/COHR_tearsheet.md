# Kronos V12: Institutional Symbol Tear Sheet — `COHR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-12.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.88x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.19%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-6.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`93.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.2% / -4.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-26 19:00` | `2026-08-28 19:00` | 48.0h | `$295.2864` | `$278.5818` | **-6.21%** | **-6.39%** | +4.7% | -5.7% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-04 13:00` | `2026-09-06 01:00` | 36.0h | `$282.2439` | `$278.8312` | **-1.34%** | **-1.35%** | +0.6% | -6.3% | `stall_bailout` |
| 3 | Book 2 | `2026-09-17 11:00` | `2026-09-24 11:00` | 168.0h | `$302.3340` | `$292.3872` | **-3.51%** | **-3.57%** | +10.1% | -3.9% | `time_cap` |
| 4 | Book 2 | `2026-10-02 13:00` | `2026-10-07 13:00` | 120.0h | `$326.7147` | `$322.0129` | **-1.46%** | **-1.47%** | +5.2% | -3.6% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-7.9%`** |
| `stall_bailout` | `1` | `0.0%` | **`-1.4%`** |
| `time_cap` | `1` | `0.0%` | **`-3.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `COHR`

* **Total Candidate Breakouts Filtered (Vetoed):** `91`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `87` (95.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `1`
* **Saved Capital Losses Avoided:** `+1,466.8%`
* **Missed Upside Forgone:** `-23.2%`
* **Net Veto Alpha:** `+1,443.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `91` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*