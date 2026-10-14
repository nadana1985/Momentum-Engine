# Kronos V12: Institutional Symbol Tear Sheet — `PNUT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-17.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.84x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-17.36%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`16.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+14.7% / -15.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2025-05-09 20:00` | `2025-05-10 12:00` | 16.0h | `$0.3710` | `$0.3153` | **-16.02%** | **-17.36%** | +14.7% | -15.4% | `structural_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `structural_stop` | `1` | `0.0%` | **`-17.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `PNUT`

* **Total Candidate Breakouts Filtered (Vetoed):** `260`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `233` (89.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `62`
* **Saved Capital Losses Avoided:** `+4,481.3%`
* **Missed Upside Forgone:** `-2,435.4%`
* **Net Veto Alpha:** `+2,045.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `238` | `91.5%` |
| `Core 1: Macro Bear Veto` | `21` | `8.1%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*