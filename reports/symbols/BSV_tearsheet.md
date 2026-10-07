# Kronos V12: Institutional Symbol Tear Sheet — `BSV`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.836`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-2.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.97x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.70%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`50.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.4% / -7.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-01-01 15:00` | `2024-01-03 11:00` | 44.0h | `$101.0712` | `$92.7530` | **-8.23%** | **-8.59%** | +7.3% | -10.5% | `stop_loss` |
| 2 | Book 3 | `2024-07-23 16:00` | `2024-07-25 20:00` | 52.0h | `$44.1232` | `$40.4919` | **-8.23%** | **-8.59%** | +5.3% | -8.7% | `stop_loss` |
| 3 | Book 3 | `2024-11-21 15:00` | `2024-11-23 02:00` | 35.0h | `$68.4204` | `$74.3700` | **+8.70%** | **+8.34%** | +10.2% | -4.9% | `target_reclaim` |
| 4 | Book 3 | `2026-09-15 14:00` | `2026-09-18 14:00` | 72.0h | `$16.2288` | `$17.2368` | **+6.21%** | **+6.03%** | +6.8% | -4.7% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |
| `time_expiry` | `1` | `100.0%` | **`+6.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `BSV`

* **Total Candidate Breakouts Filtered (Vetoed):** `127`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `80` (63.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `29`
* **Saved Capital Losses Avoided:** `+771.9%`
* **Missed Upside Forgone:** `-1,189.0%`
* **Net Veto Alpha:** `+-417.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `47` | `37.0%` |
| `Core 1: Macro Bear Veto` | `43` | `33.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `24` | `18.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `13` | `10.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*