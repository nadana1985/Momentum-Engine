# Kronos V12: Institutional Symbol Tear Sheet — `BEAMX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-8.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.92x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-8.59%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`34.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+3.8% / -8.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2024-09-15 07:00` | `2024-09-16 17:00` | 34.0h | `$0.0149` | `$0.0136` | **-8.23%** | **-8.59%** | +3.8% | -8.1% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `BEAMX`

* **Total Candidate Breakouts Filtered (Vetoed):** `275`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `119` (43.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `21`
* **Saved Capital Losses Avoided:** `+1,440.8%`
* **Missed Upside Forgone:** `-585.1%`
* **Net Veto Alpha:** `+855.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `149` | `54.2%` |
| `Core 1: Macro Bear Veto` | `53` | `19.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `38` | `13.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `32` | `11.6%` |
| `Core 3: Min Turnover Velocity` | `2` | `0.7%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*