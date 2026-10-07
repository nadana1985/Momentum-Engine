# Kronos V12: Institutional Symbol Tear Sheet — `PARTI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`25.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.675`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-6.2%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.94x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.54%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-18.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`32.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.6% / -6.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-07 11:00` | `2025-05-08 02:00` | 15.0h | `$0.2146` | `$0.2439` | **+13.64%** | **+12.78%** | +24.2% | -3.7% | `target_reclaim` |
| 2 | Book 3 | `2025-06-17 00:00` | `2025-06-20 00:00` | 72.0h | `$0.2283` | `$0.2213` | **-3.03%** | **-3.08%** | +5.3% | -4.9% | `time_expiry` |
| 3 | Book 2 | `2026-05-04 00:00` | `2026-05-04 05:00` | 5.0h | `$0.0522` | `$0.0479` | **-10.57%** | **-11.17%** | +7.9% | -8.9% | `initial_stop` |
| 4 | Book 1 | `2026-05-06 09:00` | `2026-05-07 21:00` | 36.0h | `$0.0525` | `$0.0492` | **-4.58%** | **-4.69%** | +5.0% | -9.4% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-4.7%`** |
| `initial_stop` | `1` | `0.0%` | **`-11.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+12.8%`** |
| `time_expiry` | `1` | `0.0%` | **`-3.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `PARTI`

* **Total Candidate Breakouts Filtered (Vetoed):** `39`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `33` (84.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `7`
* **Saved Capital Losses Avoided:** `+587.8%`
* **Missed Upside Forgone:** `-183.2%`
* **Net Veto Alpha:** `+404.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `27` | `69.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `12` | `30.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*