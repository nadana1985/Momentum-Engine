# Kronos V12: Institutional Symbol Tear Sheet — `VANA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.582`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-10.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.90x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.80%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-25.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`27.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.6% / -6.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-02-10 01:00` | `2025-02-11 02:00` | 25.0h | `$5.9938` | `$6.5150` | **+8.70%** | **+8.34%** | +9.3% | -1.3% | `target_reclaim` |
| 2 | Book 3 | `2025-05-12 18:00` | `2025-05-13 12:00` | 18.0h | `$6.3342` | `$6.7720` | **+6.91%** | **+6.68%** | +11.8% | -4.5% | `target_reclaim` |
| 3 | Book 3 | `2025-05-15 01:00` | `2025-05-15 14:00` | 13.0h | `$6.3342` | `$5.8129` | **-8.23%** | **-8.59%** | +3.3% | -8.1% | `stop_loss` |
| 4 | Book 3 | `2025-07-14 14:00` | `2025-07-17 14:00` | 72.0h | `$5.0554` | `$5.0533` | **-0.04%** | **-0.04%** | +2.5% | -5.8% | `time_expiry` |
| 5 | Book 3 | `2025-07-23 13:00` | `2025-07-24 06:00` | 17.0h | `$5.1506` | `$4.7267` | **-8.23%** | **-8.59%** | +3.7% | -9.1% | `stop_loss` |
| 6 | Book 3 | `2025-09-22 06:00` | `2025-09-23 01:00` | 19.0h | `$4.4083` | `$4.0455` | **-8.23%** | **-8.59%** | +2.7% | -9.6% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `target_reclaim` | `2` | `100.0%` | **`+15.0%`** |
| `time_expiry` | `1` | `0.0%` | **`-0.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `VANA`

* **Total Candidate Breakouts Filtered (Vetoed):** `49`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `33` (67.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `6`
* **Saved Capital Losses Avoided:** `+359.0%`
* **Missed Upside Forgone:** `-155.1%`
* **Net Veto Alpha:** `+203.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `18` | `36.7%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `16` | `32.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `15` | `30.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*