# Kronos V12: Institutional Symbol Tear Sheet — `CRM`
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
| **Cumulative Net Log Return** | **`-1.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.98x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.91%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-0.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`49.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+2.3% / -1.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-21 14:00` | `2026-08-23 02:00` | 36.0h | `$211.2568` | `$208.5274` | **-1.29%** | **-1.30%** | +0.1% | -2.0% | `stall_bailout` |
| 2 | Book 2 | `2026-09-14 01:00` | `2026-09-16 15:00` | 62.0h | `$251.5072` | `$250.1929` | **-0.52%** | **-0.52%** | +4.6% | -1.1% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.5%`** |
| `stall_bailout` | `1` | `0.0%` | **`-1.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `CRM`

* **Total Candidate Breakouts Filtered (Vetoed):** `23`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `14` (60.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+75.1%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+75.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `17` | `73.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `5` | `21.7%` |
| `Core 4: Defensible Whale Dump` | `1` | `4.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*