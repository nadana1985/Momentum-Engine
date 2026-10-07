# Kronos V12: Institutional Symbol Tear Sheet — `NOT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.504`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-14.5%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.86x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.42%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`30.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.4% / -6.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-11-14 14:00` | `2024-11-17 14:00` | 72.0h | `$0.0076` | `$0.0074` | **-3.49%** | **-3.55%** | +6.8% | -7.9% | `time_expiry` |
| 2 | Book 3 | `2024-11-24 17:00` | `2024-11-24 18:00` | 1.0h | `$0.0093` | `$0.0085` | **-8.23%** | **-8.59%** | +12.1% | -10.9% | `stop_loss` |
| 3 | Book 3 | `2025-05-15 05:00` | `2025-05-15 23:00` | 18.0h | `$0.0031` | `$0.0028` | **-8.23%** | **-8.59%** | +3.8% | -9.4% | `stop_loss` |
| 4 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0004` | `$0.0004` | **+8.70%** | **+8.34%** | +29.7% | -0.8% | `target_reclaim` |
| 5 | Book 3 | `2026-09-01 07:00` | `2026-09-02 01:00` | 18.0h | `$0.0005` | `$0.0004` | **-8.23%** | **-8.59%** | +2.3% | -8.8% | `stop_loss` |
| 6 | Book 3 | `2026-09-23 14:00` | `2026-09-26 14:00` | 72.0h | `$0.0005` | `$0.0005` | **+6.66%** | **+6.44%** | +7.3% | -3.5% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `time_expiry` | `2` | `50.0%` | **`+2.9%`** |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `NOT`

* **Total Candidate Breakouts Filtered (Vetoed):** `92`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `62` (67.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `20`
* **Saved Capital Losses Avoided:** `+777.2%`
* **Missed Upside Forgone:** `-1,201.0%`
* **Net Veto Alpha:** `+-423.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `41` | `44.6%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `39` | `42.4%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `11` | `12.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `1.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*