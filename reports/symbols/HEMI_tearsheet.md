# Kronos V12: Institutional Symbol Tear Sheet — `HEMI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.744`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-4.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.46%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`14.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+17.0% / -12.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-10-09 10:00` | `2025-10-10 20:00` | 34.0h | `$0.0869` | `$0.0797` | **-8.23%** | **-8.59%** | +4.2% | -14.4% | `stop_loss` |
| 2 | Book 3 | `2026-08-21 12:00` | `2026-08-21 15:00` | 3.0h | `$0.0127` | `$0.0117` | **-8.23%** | **-8.59%** | +25.9% | -20.5% | `stop_loss` |
| 3 | Book 3 | `2026-08-31 11:00` | `2026-08-31 18:00` | 7.0h | `$0.0146` | `$0.0166` | **+13.64%** | **+12.78%** | +21.0% | -1.1% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+12.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `HEMI`

* **Total Candidate Breakouts Filtered (Vetoed):** `28`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `24` (85.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `12`
* **Saved Capital Losses Avoided:** `+644.2%`
* **Missed Upside Forgone:** `-481.7%`
* **Net Veto Alpha:** `+162.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `25` | `89.3%` |
| `Core 4: Defensible Whale Dump` | `2` | `7.1%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `1` | `3.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*