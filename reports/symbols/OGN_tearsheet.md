# Kronos V12: Institutional Symbol Tear Sheet — `OGN`
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
| **Cumulative Net Log Return** | **`-0.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`1.00x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.35%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`48.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+2.3% / -6.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-20 00:00` | `2026-09-22 00:00` | 48.0h | `$0.0198` | `$0.0197` | **-0.35%** | **-0.35%** | +2.3% | -6.1% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `OGN`

* **Total Candidate Breakouts Filtered (Vetoed):** `174`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `122` (70.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `18`
* **Saved Capital Losses Avoided:** `+1,595.4%`
* **Missed Upside Forgone:** `-592.2%`
* **Net Veto Alpha:** `+1,003.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `58` | `33.3%` |
| `Core 1: Macro Bear Veto` | `51` | `29.3%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `43` | `24.7%` |
| `Core 0: Zero-Tolerance Data Firewall` | `17` | `9.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `5` | `2.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*