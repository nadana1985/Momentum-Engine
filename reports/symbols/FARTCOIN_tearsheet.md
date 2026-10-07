# Kronos V12: Institutional Symbol Tear Sheet — `FARTCOIN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`42.9%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.778`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-7.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.93x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.02%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`19.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.5% / -8.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-01-19 23:00` | `2025-01-20 00:00` | 1.0h | `$2.4647` | `$2.1584` | **-12.43%** | **-13.27%** | +8.7% | -23.9% | `stop_loss` |
| 2 | Book 3 | `2025-05-03 00:00` | `2025-05-06 00:00` | 72.0h | `$1.1398` | `$1.1204` | **-1.70%** | **-1.72%** | +1.4% | -7.9% | `time_expiry` |
| 3 | Book 3 | `2025-07-12 12:00` | `2025-07-13 02:00` | 14.0h | `$1.1904` | `$1.2939` | **+8.70%** | **+8.34%** | +9.6% | -1.3% | `target_reclaim` |
| 4 | Book 3 | `2025-07-14 20:00` | `2025-07-15 14:00` | 18.0h | `$1.3003` | `$1.1933` | **-8.23%** | **-8.59%** | +1.6% | -8.3% | `stop_loss` |
| 5 | Book 3 | `2025-07-18 20:00` | `2025-07-19 15:00` | 19.0h | `$1.3231` | `$1.4382` | **+8.70%** | **+8.34%** | +11.0% | -1.1% | `target_reclaim` |
| 6 | Book 3 | `2025-07-23 20:00` | `2025-07-24 06:00` | 10.0h | `$1.4679` | `$1.3471` | **-8.23%** | **-8.59%** | +6.2% | -8.5% | `stop_loss` |
| 7 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.1686` | `$0.1833` | **+8.70%** | **+8.34%** | +28.1% | -6.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-30.4%`** |
| `target_reclaim` | `3` | `100.0%` | **`+25.0%`** |
| `time_expiry` | `1` | `0.0%` | **`-1.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `FARTCOIN`

* **Total Candidate Breakouts Filtered (Vetoed):** `78`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `56` (71.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `17`
* **Saved Capital Losses Avoided:** `+827.1%`
* **Missed Upside Forgone:** `-641.2%`
* **Net Veto Alpha:** `+185.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `53` | `67.9%` |
| `Core 4: Defensible Whale Dump` | `19` | `24.4%` |
| `Core 4: Funding Rate Cap` | `6` | `7.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*