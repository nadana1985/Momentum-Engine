# Kronos V12: Institutional Symbol Tear Sheet — `PEOPLE`
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
| **Cumulative Net Log Return** | **`-14.2%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.87x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-7.09%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`31.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+2.1% / -9.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2023-01-10 11:00` | `2023-01-12 05:00` | 42.0h | `$0.0246` | `$0.0236` | **-5.44%** | **-5.59%** | +3.8% | -7.9% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-03 15:00` | `2026-09-04 12:00` | 21.0h | `$0.0086` | `$0.0079` | **-8.23%** | **-8.59%** | +0.5% | -10.5% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-5.6%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `PEOPLE`

* **Total Candidate Breakouts Filtered (Vetoed):** `135`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `76` (56.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `36`
* **Saved Capital Losses Avoided:** `+1,323.3%`
* **Missed Upside Forgone:** `-2,048.4%`
* **Net Veto Alpha:** `+-725.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `71` | `52.6%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `56` | `41.5%` |
| `Core 4: Funding Rate Cap` | `4` | `3.0%` |
| `Core 4: Whale Firewall` | `3` | `2.2%` |
| `Core 4: Defensible Whale Dump` | `1` | `0.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*