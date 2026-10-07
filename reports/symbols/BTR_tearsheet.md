# Kronos V12: Institutional Symbol Tear Sheet — `BTR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.008`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-17.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.84x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-8.85%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`2.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+21.3% / -26.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-26 10:00` | `2026-08-26 13:00` | 3.0h | `$0.1118` | `$0.1121` | **+0.14%** | **+0.14%** | +30.6% | -31.0% | `breakeven_ratchet` |
| 2 | Book 3 | `2026-08-29 14:00` | `2026-08-29 15:00` | 1.0h | `$0.1932` | `$0.1617` | **-16.34%** | **-17.84%** | +12.0% | -21.7% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.1%`** |
| `stop_loss` | `1` | `0.0%` | **`-17.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `BTR`

* **Total Candidate Breakouts Filtered (Vetoed):** `53`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `40` (75.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `31`
* **Saved Capital Losses Avoided:** `+899.4%`
* **Missed Upside Forgone:** `-1,760.7%`
* **Net Veto Alpha:** `+-861.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `42` | `79.2%` |
| `Core 4: Whale Firewall` | `8` | `15.1%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `2` | `3.8%` |
| `Core 4: Defensible Whale Dump` | `1` | `1.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*