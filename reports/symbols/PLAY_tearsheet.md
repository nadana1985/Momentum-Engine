# Kronos V12: Institutional Symbol Tear Sheet — `PLAY`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-17.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.84x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-5.77%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`46.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.3% / -8.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-10-07 23:00` | `2025-10-10 15:00` | 64.0h | `$0.0480` | `$0.0441` | **-8.23%** | **-8.59%** | +6.6% | -10.9% | `stop_loss` |
| 2 | Book 3 | `2026-08-27 09:00` | `2026-08-30 09:00` | 72.0h | `$0.0374` | `$0.0373` | **-0.12%** | **-0.12%** | +2.6% | -6.6% | `time_expiry` |
| 3 | Book 3 | `2026-09-25 03:00` | `2026-09-25 06:00` | 3.0h | `$0.0368` | `$0.0337` | **-8.23%** | **-8.59%** | +12.7% | -8.6% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `time_expiry` | `1` | `0.0%` | **`-0.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `PLAY`

* **Total Candidate Breakouts Filtered (Vetoed):** `45`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `34` (75.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `21`
* **Saved Capital Losses Avoided:** `+681.8%`
* **Missed Upside Forgone:** `-1,352.8%`
* **Net Veto Alpha:** `+-670.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `41` | `91.1%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `2` | `4.4%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `2` | `4.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*