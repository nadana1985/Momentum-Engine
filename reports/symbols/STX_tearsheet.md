# Kronos V12: Institutional Symbol Tear Sheet — `STX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+25.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.30x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+12.93%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`240.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+32.3% / -5.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2025-04-21 00:00` | `2025-05-04 00:00` | 312.0h | `$0.6964` | `$0.7641` | **+13.96%** | **+13.07%** | +34.0% | -9.2% | `trail_stop` |
| 2 | Book 2 | `2026-09-18 04:00` | `2026-09-25 04:00` | 168.0h | `$0.2716` | `$0.3086` | **+13.64%** | **+12.79%** | +30.6% | -1.8% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `1` | `100.0%` | **`+12.8%`** |
| `trail_stop` | `1` | `100.0%` | **`+13.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `STX`

* **Total Candidate Breakouts Filtered (Vetoed):** `123`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `65` (52.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `12`
* **Saved Capital Losses Avoided:** `+748.0%`
* **Missed Upside Forgone:** `-350.4%`
* **Net Veto Alpha:** `+397.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `49` | `39.8%` |
| `Core 1: Macro Bear Veto` | `45` | `36.6%` |
| `Core 4: Defensible Whale Dump` | `16` | `13.0%` |
| `Core 4: Funding Rate Cap` | `7` | `5.7%` |
| `Core 4: Whale Firewall` | `6` | `4.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*