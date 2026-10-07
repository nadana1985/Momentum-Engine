# Kronos V12: Institutional Symbol Tear Sheet — `GTC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-1.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.31%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`104.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.4% / -3.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-19 07:00` | `2026-09-23 15:00` | 104.0h | `$0.0847` | `$0.0836` | **-1.30%** | **-1.31%** | +5.4% | -3.4% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `GTC`

* **Total Candidate Breakouts Filtered (Vetoed):** `232`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `135` (58.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `48`
* **Saved Capital Losses Avoided:** `+2,051.6%`
* **Missed Upside Forgone:** `-1,813.5%`
* **Net Veto Alpha:** `+238.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `86` | `37.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `56` | `24.1%` |
| `Core 1: Macro Bear Veto` | `46` | `19.8%` |
| `Core 0: Zero-Tolerance Data Firewall` | `24` | `10.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `20` | `8.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*