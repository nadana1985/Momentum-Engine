# Kronos V12: Institutional Symbol Tear Sheet — `AUCTION`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `10` (`10` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `10` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.916`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-3.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.97x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.31%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-36.8%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`27.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.2% / -6.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-02-13 13:00` | `2024-02-14 15:00` | 26.0h | `$27.1492` | `$29.5100` | **+8.70%** | **+8.34%** | +9.0% | -3.9% | `target_reclaim` |
| 2 | Book 3 | `2024-05-29 14:00` | `2024-05-30 06:00` | 16.0h | `$23.5989` | `$25.6510` | **+8.70%** | **+8.34%** | +12.2% | -2.5% | `target_reclaim` |
| 3 | Book 3 | `2024-07-30 17:00` | `2024-07-31 04:00` | 11.0h | `$16.8562` | `$18.3220` | **+8.70%** | **+8.34%** | +8.9% | -4.0% | `target_reclaim` |
| 4 | Book 3 | `2024-11-12 10:00` | `2024-11-12 22:00` | 12.0h | `$13.6132` | `$14.7970` | **+8.70%** | **+8.34%** | +8.9% | -1.3% | `target_reclaim` |
| 5 | Book 3 | `2024-12-08 04:00` | `2024-12-09 09:00` | 29.0h | `$20.1765` | `$18.5160` | **-8.23%** | **-8.59%** | +3.3% | -8.6% | `stop_loss` |
| 6 | Book 3 | `2024-12-17 14:00` | `2024-12-18 20:00` | 30.0h | `$19.6678` | `$18.0491` | **-8.23%** | **-8.59%** | +1.2% | -14.9% | `stop_loss` |
| 7 | Book 3 | `2024-12-25 06:00` | `2024-12-25 07:00` | 1.0h | `$22.3781` | `$20.5364` | **-8.23%** | **-8.59%** | +6.7% | -8.5% | `stop_loss` |
| 8 | Book 3 | `2025-05-12 01:00` | `2025-05-15 01:00` | 72.0h | `$12.9508` | `$12.6333` | **-2.45%** | **-2.48%** | +4.8% | -4.4% | `time_expiry` |
| 9 | Book 3 | `2025-09-22 05:00` | `2025-09-22 06:00` | 1.0h | `$9.4116` | `$8.6370` | **-8.23%** | **-8.59%** | +1.4% | -11.2% | `stop_loss` |
| 10 | Book 3 | `2026-09-01 02:00` | `2026-09-04 02:00` | 72.0h | `$3.3460` | `$3.3586` | **+0.37%** | **+0.37%** | +5.0% | -5.2% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `target_reclaim` | `4` | `100.0%` | **`+33.4%`** |
| `time_expiry` | `2` | `50.0%` | **`-2.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `AUCTION`

* **Total Candidate Breakouts Filtered (Vetoed):** `118`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `84` (71.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `28`
* **Saved Capital Losses Avoided:** `+1,590.8%`
* **Missed Upside Forgone:** `-1,096.1%`
* **Net Veto Alpha:** `+494.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `59` | `50.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `38` | `32.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `20` | `16.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `0.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*