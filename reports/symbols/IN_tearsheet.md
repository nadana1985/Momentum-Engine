# Kronos V12: Institutional Symbol Tear Sheet — `IN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.533`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-14.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.86x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.44%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-31.0%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`13.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+14.7% / -8.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-09-24 09:00` | `2025-09-24 10:00` | 1.0h | `$0.0890` | `$0.0968` | **+8.70%** | **+8.34%** | +13.6% | -3.7% | `target_reclaim` |
| 2 | Book 3 | `2025-09-24 15:00` | `2025-09-24 17:00` | 2.0h | `$0.1071` | `$0.0983` | **-8.23%** | **-8.59%** | +14.7% | -10.1% | `stop_loss` |
| 3 | Book 3 | `2025-09-25 01:00` | `2025-09-25 02:00` | 1.0h | `$0.1140` | `$0.1029` | **-9.73%** | **-10.24%** | +15.8% | -11.4% | `stop_loss` |
| 4 | Book 3 | `2025-10-04 10:00` | `2025-10-04 11:00` | 1.0h | `$0.1294` | `$0.1146` | **-11.46%** | **-12.17%** | +20.5% | -16.9% | `stop_loss` |
| 5 | Book 3 | `2025-10-10 07:00` | `2025-10-10 08:00` | 1.0h | `$0.1831` | `$0.1990` | **+8.70%** | **+8.34%** | +20.2% | -6.4% | `target_reclaim` |
| 6 | Book 3 | `2026-09-28 02:00` | `2026-10-01 02:00` | 72.0h | `$0.0381` | `$0.0379` | **-0.30%** | **-0.30%** | +3.2% | -3.8% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-31.0%`** |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |
| `time_expiry` | `1` | `0.0%` | **`-0.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `IN`

* **Total Candidate Breakouts Filtered (Vetoed):** `42`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `34` (81.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `21`
* **Saved Capital Losses Avoided:** `+1,077.8%`
* **Missed Upside Forgone:** `-1,305.6%`
* **Net Veto Alpha:** `+-227.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `31` | `73.8%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `5` | `11.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `9.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2` | `4.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*