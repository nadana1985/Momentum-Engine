# Kronos V12: Institutional Symbol Tear Sheet — `METIS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.602`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-11.0%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.90x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.84%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-19.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`35.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.2% / -5.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-07-24 23:00` | `2024-07-25 14:00` | 15.0h | `$47.6928` | `$43.7677` | **-8.23%** | **-8.59%** | +1.7% | -8.0% | `stop_loss` |
| 2 | Book 3 | `2024-11-24 12:00` | `2024-11-24 22:00` | 10.0h | `$52.7988` | `$57.3900` | **+8.70%** | **+8.34%** | +9.5% | -2.1% | `target_reclaim` |
| 3 | Book 3 | `2024-11-29 07:00` | `2024-11-30 05:00` | 22.0h | `$56.3224` | `$61.2200` | **+8.70%** | **+8.34%** | +9.2% | -0.1% | `target_reclaim` |
| 4 | Book 3 | `2025-04-27 16:00` | `2025-04-30 16:00` | 72.0h | `$15.5940` | `$15.2917` | **-1.94%** | **-1.96%** | +8.4% | -4.9% | `time_expiry` |
| 5 | Book 3 | `2025-07-22 08:00` | `2025-07-23 20:00` | 36.0h | `$18.3908` | `$16.8772` | **-8.23%** | **-8.59%** | +6.4% | -8.4% | `stop_loss` |
| 6 | Book 3 | `2025-09-19 14:00` | `2025-09-22 01:00` | 59.0h | `$15.7044` | `$14.4119` | **-8.23%** | **-8.59%** | +2.1% | -8.4% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |
| `time_expiry` | `1` | `0.0%` | **`-2.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `METIS`

* **Total Candidate Breakouts Filtered (Vetoed):** `93`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `50` (53.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `13`
* **Saved Capital Losses Avoided:** `+607.2%`
* **Missed Upside Forgone:** `-568.7%`
* **Net Veto Alpha:** `+38.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `60` | `64.5%` |
| `Core 1: Macro Bear Veto` | `18` | `19.4%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `14` | `15.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `1.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*