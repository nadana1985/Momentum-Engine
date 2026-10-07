# Kronos V12: Institutional Symbol Tear Sheet — `XLE`
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
| **Cumulative Net Log Return** | **`-2.5%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.98x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.26%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-0.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`36.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+0.1% / -2.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-10 12:00` | `2026-09-12 00:00` | 36.0h | `$66.5058` | `$65.1567` | **-2.03%** | **-2.05%** | +0.0% | -3.1% | `stall_bailout` |
| 2 | Book 2 | `2026-10-01 20:00` | `2026-10-03 08:00` | 36.0h | `$62.9770` | `$62.6829` | **-0.47%** | **-0.47%** | +0.1% | -1.9% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `2` | `0.0%` | **`-2.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `XLE`

* **Total Candidate Breakouts Filtered (Vetoed):** `32`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `14` (43.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+28.2%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+28.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `26` | `81.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `12.5%` |
| `Core 0: Zero-Tolerance Data Firewall` | `2` | `6.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*