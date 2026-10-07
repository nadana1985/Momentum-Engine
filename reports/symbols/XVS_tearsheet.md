# Kronos V12: Institutional Symbol Tear Sheet — `XVS`
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
| **Cumulative Net Log Return** | **`-3.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.59%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`36.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+-0.1% / -5.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-03 15:00` | `2026-09-05 03:00` | 36.0h | `$3.2311` | `$3.1172` | **-3.52%** | **-3.59%** | +-0.1% | -5.2% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `1` | `0.0%` | **`-3.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `XVS`

* **Total Candidate Breakouts Filtered (Vetoed):** `181`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `99` (54.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `18`
* **Saved Capital Losses Avoided:** `+1,080.7%`
* **Missed Upside Forgone:** `-589.3%`
* **Net Veto Alpha:** `+491.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `80` | `44.2%` |
| `Core 1: Macro Bear Veto` | `53` | `29.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `37` | `20.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `11` | `6.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*