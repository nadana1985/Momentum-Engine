# Kronos V12: Institutional Symbol Tear Sheet — `BTCDOM`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`25.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.405`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-4.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.95x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.16%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-7.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`66.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+2.0% / -2.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-06-20 16:00` | `2023-06-27 16:00` | 168.0h | `$1820.1390` | `$1878.2925` | **+3.20%** | **+3.15%** | +5.1% | -0.9% | `time_cap` |
| 2 | Book 2 | `2024-01-09 12:00` | `2024-01-10 15:00` | 27.0h | `$2331.9152` | `$2192.5958` | **-5.97%** | **-6.16%** | +2.1% | -5.9% | `initial_stop` |
| 3 | Book 2 | `2024-02-09 17:00` | `2024-02-11 05:00` | 36.0h | `$2238.7830` | `$2223.5273` | **-0.68%** | **-0.68%** | +0.2% | -1.8% | `stall_bailout` |
| 4 | Book 2 | `2024-10-03 07:00` | `2024-10-04 19:00` | 36.0h | `$3037.5750` | `$3009.5573` | **-0.92%** | **-0.93%** | +0.8% | -1.3% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `2` | `0.0%` | **`-1.6%`** |
| `initial_stop` | `1` | `0.0%` | **`-6.2%`** |
| `time_cap` | `1` | `100.0%` | **`+3.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `BTCDOM`

* **Total Candidate Breakouts Filtered (Vetoed):** `370`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `204` (55.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `7`
* **Saved Capital Losses Avoided:** `+805.1%`
* **Missed Upside Forgone:** `-214.9%`
* **Net Veto Alpha:** `+590.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `202` | `54.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `51` | `13.8%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `50` | `13.5%` |
| `Core 0: Zero-Tolerance Data Firewall` | `39` | `10.5%` |
| `Core 4: Defensible Whale Dump` | `23` | `6.2%` |
| `Core 3: Min Turnover Velocity` | `5` | `1.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*