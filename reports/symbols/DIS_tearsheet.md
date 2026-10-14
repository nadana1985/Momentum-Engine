# Kronos V12: Institutional Symbol Tear Sheet — `DIS`
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
| **Cumulative Net Log Return** | **`-0.2%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`1.00x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.21%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`182.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.0% / -0.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2026-08-20 08:00` | `2026-08-27 22:00` | 182.0h | `$106.9768` | `$106.6527` | **-0.21%** | **-0.21%** | +5.0% | -0.8% | `stagnation_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stagnation_cut` | `1` | `0.0%` | **`-0.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `DIS`

* **Total Candidate Breakouts Filtered (Vetoed):** `373`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `151` (40.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+492.7%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+492.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `328` | `87.9%` |
| `Core 0: Zero-Tolerance Data Firewall` | `32` | `8.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `8` | `2.1%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `5` | `1.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*