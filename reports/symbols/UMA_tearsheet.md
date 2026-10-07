# Kronos V12: Institutional Symbol Tear Sheet — `UMA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-5.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.95x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.67%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-0.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`28.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+0.5% / -6.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-10-01 22:00` | `2023-10-02 18:00` | 20.0h | `$1.4596` | `$1.3900` | **-4.77%** | **-4.89%** | +0.2% | -7.9% | `initial_stop` |
| 2 | Book 2 | `2026-09-19 16:00` | `2026-09-21 05:00` | 37.0h | `$0.3936` | `$0.3918` | **-0.45%** | **-0.45%** | +0.8% | -5.3% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-4.9%`** |
| `stall_bailout` | `1` | `0.0%` | **`-0.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `UMA`

* **Total Candidate Breakouts Filtered (Vetoed):** `117`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `72` (61.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `20`
* **Saved Capital Losses Avoided:** `+927.0%`
* **Missed Upside Forgone:** `-1,079.7%`
* **Net Veto Alpha:** `+-152.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `44` | `37.6%` |
| `Core 1: Macro Bear Veto` | `43` | `36.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `28` | `23.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `0.9%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*