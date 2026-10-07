# Kronos V12: Institutional Symbol Tear Sheet — `AVA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.971`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-0.5%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`1.00x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.13%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`14.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.6% / -6.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-04 23:00` | `2025-05-06 00:00` | 25.0h | `$0.5967` | `$0.5476` | **-8.23%** | **-8.59%** | +1.4% | -11.5% | `stop_loss` |
| 2 | Book 3 | `2025-05-14 15:00` | `2025-05-15 10:00` | 19.0h | `$0.7006` | `$0.6429` | **-8.23%** | **-8.59%** | +0.8% | -8.1% | `stop_loss` |
| 3 | Book 3 | `2025-09-21 09:00` | `2025-09-21 15:00` | 6.0h | `$0.5686` | `$0.6180` | **+8.70%** | **+8.34%** | +10.2% | -1.8% | `target_reclaim` |
| 4 | Book 3 | `2026-09-19 05:00` | `2026-09-19 13:00` | 8.0h | `$0.2222` | `$0.2415` | **+8.70%** | **+8.34%** | +10.0% | -2.7% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `AVA`

* **Total Candidate Breakouts Filtered (Vetoed):** `76`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `48` (63.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `2`
* **Saved Capital Losses Avoided:** `+496.8%`
* **Missed Upside Forgone:** `-54.2%`
* **Net Veto Alpha:** `+442.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `47` | `61.8%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `20` | `26.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `6` | `7.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `3.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*