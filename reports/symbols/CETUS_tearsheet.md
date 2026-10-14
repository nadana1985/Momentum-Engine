# Kronos V12: Institutional Symbol Tear Sheet — `CETUS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`16.7%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.113`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-48.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.61x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-8.14%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-46.5%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`27.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.2% / -11.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-12-16 22:00` | `2024-12-18 19:00` | 45.0h | `$0.4099` | `$0.3761` | **-8.23%** | **-8.59%** | +1.3% | -8.0% | `stop_loss` |
| 2 | Book 3 | `2025-04-21 17:00` | `2025-04-22 11:00` | 18.0h | `$0.1025` | `$0.1091` | **+6.44%** | **+6.24%** | +7.2% | -1.2% | `target_reclaim` |
| 3 | Book 3 | `2025-05-22 10:00` | `2025-05-22 11:00` | 1.0h | `$0.2212` | `$0.1798` | **-18.70%** | **-20.70%** | +16.2% | -34.3% | `stop_loss` |
| 4 | Book 3 | `2025-07-18 08:00` | `2025-07-18 20:00` | 12.0h | `$0.1240` | `$0.1138` | **-8.23%** | **-8.59%** | +3.0% | -9.5% | `stop_loss` |
| 5 | Book 3 | `2025-07-28 19:00` | `2025-07-30 09:00` | 38.0h | `$0.1282` | `$0.1176` | **-8.23%** | **-8.59%** | +4.8% | -8.1% | `stop_loss` |
| 6 | Book 3 | `2025-10-27 13:00` | `2025-10-29 18:00` | 53.0h | `$0.0510` | `$0.0468` | **-8.23%** | **-8.59%** | +4.7% | -8.2% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `5` | `0.0%` | **`-55.1%`** |
| `target_reclaim` | `1` | `100.0%` | **`+6.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `CETUS`

* **Total Candidate Breakouts Filtered (Vetoed):** `206`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `153` (74.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `19`
* **Saved Capital Losses Avoided:** `+1,926.0%`
* **Missed Upside Forgone:** `-910.2%`
* **Net Veto Alpha:** `+1,015.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `125` | `60.7%` |
| `Core 1: Macro Bear Veto` | `46` | `22.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `26` | `12.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `9` | `4.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*