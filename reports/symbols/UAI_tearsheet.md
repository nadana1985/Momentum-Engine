# Kronos V12: Institutional Symbol Tear Sheet — `UAI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
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
| **Average Trade Duration** | **`2.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.1% / -12.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-09-03 00:00` | `2026-09-03 04:00` | 4.0h | `$0.4347` | `$0.3989` | **-8.23%** | **-8.59%** | +1.9% | -12.8% | `stop_loss` |
| 2 | Book 3 | `2026-09-06 03:00` | `2026-09-06 04:00` | 1.0h | `$0.6039` | `$0.5542` | **-8.23%** | **-8.59%** | +14.3% | -11.7% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `UAI`

* **Total Candidate Breakouts Filtered (Vetoed):** `39`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `39` (100.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `10`
* **Saved Capital Losses Avoided:** `+1,167.5%`
* **Missed Upside Forgone:** `-275.8%`
* **Net Veto Alpha:** `+891.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `33` | `84.6%` |
| `Core 4: Whale Firewall` | `3` | `7.7%` |
| `Core 4: Defensible Whale Dump` | `2` | `5.1%` |
| `Core 4: Funding Rate Cap` | `1` | `2.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*