# Kronos V12: Institutional Symbol Tear Sheet — `CFX`
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
| **Cumulative Net Log Return** | **`-5.9%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.94x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.94%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-0.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`53.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+3.5% / -5.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2023-10-02 00:00` | `2023-10-03 12:00` | 36.0h | `$0.1388` | `$0.1342` | **-4.87%** | **-4.99%** | +0.8% | -8.2% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-20 16:00` | `2026-09-23 14:00` | 70.0h | `$0.0527` | `$0.0522` | **-0.88%** | **-0.88%** | +6.2% | -3.0% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-5.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `CFX`

* **Total Candidate Breakouts Filtered (Vetoed):** `117`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `74` (63.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `15`
* **Saved Capital Losses Avoided:** `+941.9%`
* **Missed Upside Forgone:** `-812.8%`
* **Net Veto Alpha:** `+129.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `66` | `56.4%` |
| `Core 1: Macro Bear Veto` | `45` | `38.5%` |
| `Core 4: Funding Rate Cap` | `6` | `5.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*