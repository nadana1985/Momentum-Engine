# Kronos V12: Institutional Symbol Tear Sheet — `SPELL`
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
| **Cumulative Net Log Return** | **`-1.5%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.48%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`36.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+0.4% / -5.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-20 16:00` | `2026-09-22 04:00` | 36.0h | `$0.0001` | `$0.0001` | **-1.47%** | **-1.48%** | +0.4% | -5.7% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `1` | `0.0%` | **`-1.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `SPELL`

* **Total Candidate Breakouts Filtered (Vetoed):** `127`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `80` (63.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `18`
* **Saved Capital Losses Avoided:** `+927.8%`
* **Missed Upside Forgone:** `-631.9%`
* **Net Veto Alpha:** `+296.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `60` | `47.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `35` | `27.6%` |
| `Core 1: Macro Bear Veto` | `21` | `16.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `8` | `6.3%` |
| `Core 0: Zero-Tolerance Data Firewall` | `3` | `2.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*