# Kronos V12: Institutional Symbol Tear Sheet — `FIDA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.971`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-0.5%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`1.00x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.13%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`28.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.9% / -5.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-12-05 01:00` | `2024-12-05 23:00` | 22.0h | `$0.3469` | `$0.3770` | **+8.70%** | **+8.34%** | +8.8% | -2.0% | `target_reclaim` |
| 2 | Book 3 | `2025-01-19 09:00` | `2025-01-19 16:00` | 7.0h | `$0.2744` | `$0.2518` | **-8.23%** | **-8.59%** | +6.4% | -8.5% | `stop_loss` |
| 3 | Book 3 | `2025-07-04 08:00` | `2025-07-05 02:00` | 18.0h | `$0.0772` | `$0.0839` | **+8.70%** | **+8.34%** | +10.1% | -1.8% | `target_reclaim` |
| 4 | Book 3 | `2026-09-07 00:00` | `2026-09-09 20:00` | 68.0h | `$0.0215` | `$0.0197` | **-8.23%** | **-8.59%** | +2.4% | -8.4% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `FIDA`

* **Total Candidate Breakouts Filtered (Vetoed):** `41`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `29` (70.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `13`
* **Saved Capital Losses Avoided:** `+387.8%`
* **Missed Upside Forgone:** `-636.5%`
* **Net Veto Alpha:** `+-248.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `22` | `53.7%` |
| `Core 1: Macro Bear Veto` | `18` | `43.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `2.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*