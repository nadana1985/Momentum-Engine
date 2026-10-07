# Kronos V12: Institutional Symbol Tear Sheet — `CBRS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.714`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-0.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.35%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-2.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`102.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.5% / -2.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-03 15:00` | `2026-09-10 15:00` | 168.0h | `$188.0991` | `$191.4203` | **+1.77%** | **+1.75%** | +18.1% | -2.1% | `time_cap` |
| 2 | Book 2 | `2026-09-18 13:00` | `2026-09-20 01:00` | 36.0h | `$201.7331` | `$196.8467` | **-2.42%** | **-2.45%** | +0.8% | -3.2% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `1` | `0.0%` | **`-2.5%`** |
| `time_cap` | `1` | `100.0%` | **`+1.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `CBRS`

* **Total Candidate Breakouts Filtered (Vetoed):** `8`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `7` (87.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+116.7%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+116.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `8` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*