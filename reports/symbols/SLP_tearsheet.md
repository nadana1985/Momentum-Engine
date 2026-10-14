# Kronos V12: Institutional Symbol Tear Sheet — `SLP`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.871`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-0.9%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.45%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`120.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+4.7% / -5.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2026-08-27 04:00` | `2026-09-03 04:00` | 168.0h | `$0.0007` | `$0.0006` | **-6.64%** | **-6.92%** | +1.3% | -11.2% | `stagnation_cut` |
| 2 | Book 3 | `2026-09-29 02:00` | `2026-10-02 02:00` | 72.0h | `$0.0006` | `$0.0007` | **+6.21%** | **+6.03%** | +8.1% | -0.1% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stagnation_cut` | `1` | `0.0%` | **`-6.9%`** |
| `time_expiry` | `1` | `100.0%` | **`+6.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `SLP`

* **Total Candidate Breakouts Filtered (Vetoed):** `23`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `16` (69.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `2`
* **Saved Capital Losses Avoided:** `+199.0%`
* **Missed Upside Forgone:** `-46.7%`
* **Net Veto Alpha:** `+152.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `13` | `56.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `10` | `43.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*