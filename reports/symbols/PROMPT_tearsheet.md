# Kronos V12: Institutional Symbol Tear Sheet — `PROMPT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.771`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-2.5%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.98x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.82%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-10.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`49.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.3% / -5.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-12 15:00` | `2025-07-13 14:00` | 23.0h | `$0.1422` | `$0.1546` | **+8.70%** | **+8.34%** | +8.9% | -1.1% | `target_reclaim` |
| 2 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0225` | `$0.0220` | **-2.20%** | **-2.22%** | +9.4% | -5.5% | `time_expiry` |
| 3 | Book 3 | `2026-08-30 23:00` | `2026-09-02 04:00` | 53.0h | `$0.0239` | `$0.0220` | **-8.23%** | **-8.59%** | +3.6% | -8.9% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |
| `time_expiry` | `1` | `0.0%` | **`-2.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `PROMPT`

* **Total Candidate Breakouts Filtered (Vetoed):** `22`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `14` (63.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `8`
* **Saved Capital Losses Avoided:** `+203.6%`
* **Missed Upside Forgone:** `-706.4%`
* **Net Veto Alpha:** `+-502.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `16` | `72.7%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `3` | `13.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `13.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*