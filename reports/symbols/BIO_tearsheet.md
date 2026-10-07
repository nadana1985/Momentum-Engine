# Kronos V12: Institutional Symbol Tear Sheet — `BIO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.376`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-21.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.81x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.57%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-34.4%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`25.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.5% / -9.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-04-24 01:00` | `2025-04-25 13:00` | 36.0h | `$0.0697` | `$0.0792` | **+13.64%** | **+12.78%** | +16.0% | -7.1% | `target_reclaim` |
| 2 | Book 3 | `2025-05-14 15:00` | `2025-05-15 06:00` | 15.0h | `$0.0893` | `$0.0820` | **-8.23%** | **-8.59%** | +2.7% | -9.4% | `stop_loss` |
| 3 | Book 3 | `2025-07-29 15:00` | `2025-07-31 14:00` | 47.0h | `$0.0696` | `$0.0639` | **-8.23%** | **-8.59%** | +8.8% | -9.0% | `stop_loss` |
| 4 | Book 3 | `2025-08-13 07:00` | `2025-08-14 12:00` | 29.0h | `$0.1156` | `$0.1061` | **-8.23%** | **-8.59%** | +6.2% | -13.5% | `stop_loss` |
| 5 | Book 3 | `2025-09-22 02:00` | `2025-09-22 06:00` | 4.0h | `$0.1651` | `$0.1515` | **-8.23%** | **-8.59%** | +0.9% | -14.1% | `stop_loss` |
| 6 | Book 2 | `2026-05-02 09:00` | `2026-05-03 08:00` | 23.0h | `$0.0513` | `$0.0514` | **+0.14%** | **+0.14%** | +28.7% | -4.4% | `breakeven_ratchet` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.1%`** |
| `target_reclaim` | `1` | `100.0%` | **`+12.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `BIO`

* **Total Candidate Breakouts Filtered (Vetoed):** `64`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `48` (75.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `19`
* **Saved Capital Losses Avoided:** `+871.8%`
* **Missed Upside Forgone:** `-1,282.3%`
* **Net Veto Alpha:** `+-410.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `33` | `51.6%` |
| `Core 1: Macro Bear Veto` | `31` | `48.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*