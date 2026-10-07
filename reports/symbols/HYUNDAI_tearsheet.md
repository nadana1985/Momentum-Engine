# Kronos V12: Institutional Symbol Tear Sheet — `HYUNDAI`
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
| **Cumulative Net Log Return** | **`-9.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.91x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-4.71%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-3.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`30.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+0.4% / -4.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-31 23:00` | `2026-09-02 00:00` | 25.0h | `$296.8904` | `$280.3828` | **-5.56%** | **-5.72%** | +0.3% | -5.9% | `initial_stop` |
| 2 | Book 2 | `2026-09-22 00:00` | `2026-09-23 12:00` | 36.0h | `$270.2439` | `$260.4373` | **-3.63%** | **-3.70%** | +0.5% | -3.7% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-5.7%`** |
| `stall_bailout` | `1` | `0.0%` | **`-3.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `HYUNDAI`

* **Total Candidate Breakouts Filtered (Vetoed):** `13`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `9` (69.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+109.2%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+109.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `13` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*