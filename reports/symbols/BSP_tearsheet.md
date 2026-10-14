# Kronos V12: Institutional Symbol Tear Sheet — `BSP`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `1` (`0` Closed, `1` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `0` | $\ge 1$ | ⚠️ In-Flight |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`+0.0%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`1.00x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.00%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`0.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+0.0% / 0.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-10-06 16:00` | `_Open Live_` | 140.0h | `$33.9948` | `$38.3000` | **+12.56%** | **+11.84%** | +23.4% | -3.6% | `open_at_end` |

---

## 4. Counterfactual Risk Gate Audit for `BSP`

* **Total Candidate Breakouts Filtered (Vetoed):** `323`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `160` (49.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `85`
* **Saved Capital Losses Avoided:** `+2,363.8%`
* **Missed Upside Forgone:** `-2,612.7%`
* **Net Veto Alpha:** `+-248.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `297` | `92.0%` |
| `Core 0: Zero-Tolerance Data Firewall` | `22` | `6.8%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `2` | `0.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `2` | `0.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*