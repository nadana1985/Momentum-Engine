# Kronos V12: Institutional Symbol Tear Sheet — `AIN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.078`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-100.2%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.37x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-33.41%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-108.7%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`1.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+25.4% / -31.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-09-19 14:00` | `2025-09-19 16:00` | 2.0h | `$0.1519` | `$0.1583` | **+4.17%** | **+4.08%** | +10.0% | -4.6% | `target_reclaim` |
| 2 | Book 3 | `2026-09-14 12:00` | `2026-09-14 13:00` | 1.0h | `$0.0967` | `$0.1010` | **+4.53%** | **+4.43%** | +10.2% | -12.0% | `target_reclaim` |
| 3 | Book 3 | `2026-09-16 01:00` | `2026-09-16 02:00` | 1.0h | `$0.1094` | `$0.0369` | **-66.29%** | **-108.73%** | +56.1% | -79.1% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+8.5%`** |
| `stop_loss` | `1` | `0.0%` | **`-108.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `AIN`

* **Total Candidate Breakouts Filtered (Vetoed):** `171`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `147` (86.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `42`
* **Saved Capital Losses Avoided:** `+3,785.8%`
* **Missed Upside Forgone:** `-1,702.7%`
* **Net Veto Alpha:** `+2,083.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `164` | `95.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `6` | `3.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `1` | `0.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*