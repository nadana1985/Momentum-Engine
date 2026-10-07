# Kronos V12: Institutional Symbol Tear Sheet — `OP`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `7` (`6` Closed, `1` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`16.7%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.261`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-29.9%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.74x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-4.99%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-23.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`107.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.7% / -7.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-04-26 12:00` | `2023-04-26 19:00` | 7.0h | `$2.3447` | `$2.1518` | **-8.23%** | **-8.59%** | +0.1% | -9.8% | `initial_stop` |
| 2 | Book 2 | `2025-06-29 22:00` | `2025-06-30 14:00` | 16.0h | `$0.6155` | `$0.5649` | **-8.23%** | **-8.59%** | +1.1% | -8.2% | `initial_stop` |
| 3 | Book 1 | `2025-07-10 20:00` | `2025-07-31 20:00` | 504.0h | `$0.6244` | `$0.6817` | **+11.16%** | **+10.58%** | +39.7% | -1.7% | `time_cap` |
| 4 | Book 1 | `2025-09-18 18:00` | `2025-09-20 18:00` | 48.0h | `$0.8387` | `$0.8037` | **-5.95%** | **-6.14%** | +2.1% | -6.5% | `fast_decay_cut` |
| 5 | Book 2 | `2025-10-26 22:00` | `2025-10-28 20:00` | 46.0h | `$0.4683` | `$0.4297` | **-8.23%** | **-8.59%** | +1.6% | -8.2% | `initial_stop` |
| 6 | Book 2 | `2026-09-14 17:00` | `2026-09-15 18:00` | 25.0h | `$0.1040` | `$0.0954` | **-8.23%** | **-8.59%** | +1.4% | -9.4% | `initial_stop` |
| 7 | Book 1 | `2026-09-18 03:00` | `_Open Live_` | 457.9h | `$0.1128` | `$0.1256` | **+8.72%** | **+8.36%** | +34.4% | -5.9% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `4` | `0.0%` | **`-34.4%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-6.1%`** |
| `time_cap` | `1` | `100.0%` | **`+10.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `OP`

* **Total Candidate Breakouts Filtered (Vetoed):** `110`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `66` (60.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `29`
* **Saved Capital Losses Avoided:** `+732.4%`
* **Missed Upside Forgone:** `-1,036.5%`
* **Net Veto Alpha:** `+-304.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `67` | `60.9%` |
| `Core 4: Funding Rate Cap` | `21` | `19.1%` |
| `Core 4: Defensible Whale Dump` | `17` | `15.5%` |
| `Core 4: Whale Firewall` | `5` | `4.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*