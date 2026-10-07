# Kronos V12: Institutional Symbol Tear Sheet — `SUN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+6.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.06x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+6.03%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.0% / -2.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-05-03 05:00` | `2026-05-10 05:00` | 168.0h | `$0.0190` | `$0.0202` | **+6.22%** | **+6.03%** | +7.0% | -2.7% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `1` | `100.0%` | **`+6.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `SUN`

* **Total Candidate Breakouts Filtered (Vetoed):** `130`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `72` (55.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `13`
* **Saved Capital Losses Avoided:** `+448.1%`
* **Missed Upside Forgone:** `-659.9%`
* **Net Veto Alpha:** `+-211.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `78` | `60.0%` |
| `Core 1: Macro Bear Veto` | `47` | `36.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `5` | `3.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*