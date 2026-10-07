# Kronos V12: Institutional Symbol Tear Sheet — `ILV`
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
| **Cumulative Net Log Return** | **`-3.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.97x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.12%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`36.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+0.6% / -2.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2024-09-13 21:00` | `2024-09-15 09:00` | 36.0h | `$40.7316` | `$39.4811` | **-3.07%** | **-3.12%** | +0.6% | -2.9% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `1` | `0.0%` | **`-3.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `ILV`

* **Total Candidate Breakouts Filtered (Vetoed):** `150`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `94` (62.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `10`
* **Saved Capital Losses Avoided:** `+1,198.5%`
* **Missed Upside Forgone:** `-393.0%`
* **Net Veto Alpha:** `+805.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `88` | `58.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `32` | `21.3%` |
| `Core 1: Macro Bear Veto` | `22` | `14.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `7` | `4.7%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*