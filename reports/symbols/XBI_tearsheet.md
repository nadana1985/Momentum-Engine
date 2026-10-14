# Kronos V12: Institutional Symbol Tear Sheet — `XBI`
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
| **Cumulative Net Log Return** | **`-4.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.95x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.32%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-0.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`29.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+0.3% / -2.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-14 15:00` | `2026-09-15 14:00` | 23.0h | `$158.8662` | `$152.2459` | **-4.22%** | **-4.31%** | +0.1% | -4.1% | `initial_stop` |
| 2 | Book 2 | `2026-09-28 16:00` | `2026-09-30 04:00` | 36.0h | `$157.3724` | `$156.8569` | **-0.33%** | **-0.33%** | +0.4% | -1.7% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-4.3%`** |
| `stall_bailout` | `1` | `0.0%` | **`-0.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `XBI`

* **Total Candidate Breakouts Filtered (Vetoed):** `35`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `34` (97.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+125.5%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+125.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `22` | `62.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `11` | `31.4%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `2.9%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `2.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*