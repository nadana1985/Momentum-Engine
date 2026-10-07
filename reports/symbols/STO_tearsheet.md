# Kronos V12: Institutional Symbol Tear Sheet — `STO`
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
| **Cumulative Net Log Return** | **`-2.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.97x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.64%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`36.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+0.4% / -5.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-19 16:00` | `2026-09-21 04:00` | 36.0h | `$0.0413` | `$0.0402` | **-2.60%** | **-2.64%** | +0.4% | -5.1% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `1` | `0.0%` | **`-2.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `STO`

* **Total Candidate Breakouts Filtered (Vetoed):** `48`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `39` (81.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `32`
* **Saved Capital Losses Avoided:** `+1,337.3%`
* **Missed Upside Forgone:** `-7,573.6%`
* **Net Veto Alpha:** `+-6,236.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `38` | `79.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `9` | `18.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `2.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*