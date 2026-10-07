# Kronos V12: Institutional Symbol Tear Sheet — `BAN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-17.2%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.84x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-8.59%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`30.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.5% / -9.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-01-25 12:00` | `2025-01-25 13:00` | 1.0h | `$0.0756` | `$0.0694` | **-8.23%** | **-8.59%** | +6.1% | -9.9% | `stop_loss` |
| 2 | Book 3 | `2025-04-29 20:00` | `2025-05-02 07:00` | 59.0h | `$0.0502` | `$0.0460` | **-8.23%** | **-8.59%** | +12.9% | -9.6% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `BAN`

* **Total Candidate Breakouts Filtered (Vetoed):** `92`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `48` (52.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `14`
* **Saved Capital Losses Avoided:** `+1,524.0%`
* **Missed Upside Forgone:** `-475.1%`
* **Net Veto Alpha:** `+1,048.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `82` | `89.1%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `10` | `10.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*