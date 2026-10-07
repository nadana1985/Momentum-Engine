# Kronos V12: Institutional Symbol Tear Sheet — `KNC`
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
| **Cumulative Net Log Return** | **`-6.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.94x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-6.35%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.7% / -7.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-03-28 14:00` | `2022-04-04 14:00` | 168.0h | `$3.3143` | `$3.1102` | **-6.16%** | **-6.35%** | +13.7% | -7.5% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `1` | `0.0%` | **`-6.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `KNC`

* **Total Candidate Breakouts Filtered (Vetoed):** `303`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `184` (60.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `34`
* **Saved Capital Losses Avoided:** `+2,299.2%`
* **Missed Upside Forgone:** `-1,178.5%`
* **Net Veto Alpha:** `+1,120.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `93` | `30.7%` |
| `Core 1: Macro Bear Veto` | `74` | `24.4%` |
| `Core 0: Zero-Tolerance Data Firewall` | `69` | `22.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `63` | `20.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `4` | `1.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*