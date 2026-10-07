# Kronos V12: Institutional Symbol Tear Sheet — `CHILLGUY`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `14` (`14` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `14` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`64.3%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.584`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+25.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.28x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.79%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-9.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`15.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.4% / -6.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-01 14:00` | `2025-05-01 15:00` | 1.0h | `$0.0394` | `$0.0428` | **+8.70%** | **+8.34%** | +15.2% | -0.3% | `target_reclaim` |
| 2 | Book 3 | `2025-05-04 22:00` | `2025-05-05 03:00` | 5.0h | `$0.0419` | `$0.0456` | **+8.70%** | **+8.34%** | +8.8% | -1.0% | `target_reclaim` |
| 3 | Book 3 | `2025-05-05 22:00` | `2025-05-06 20:00` | 22.0h | `$0.0528` | `$0.0485` | **-8.23%** | **-8.59%** | +3.7% | -8.2% | `stop_loss` |
| 4 | Book 3 | `2025-05-12 01:00` | `2025-05-12 02:00` | 1.0h | `$0.0889` | `$0.0967` | **+8.70%** | **+8.34%** | +16.9% | -2.7% | `target_reclaim` |
| 5 | Book 3 | `2025-05-12 05:00` | `2025-05-12 06:00` | 1.0h | `$0.0953` | `$0.1035` | **+8.70%** | **+8.34%** | +20.5% | -0.5% | `target_reclaim` |
| 6 | Book 3 | `2025-05-14 16:00` | `2025-05-15 07:00` | 15.0h | `$0.1081` | `$0.0992` | **-8.23%** | **-8.59%** | +10.0% | -8.7% | `stop_loss` |
| 7 | Book 3 | `2025-07-01 17:00` | `2025-07-02 15:00` | 22.0h | `$0.0475` | `$0.0516` | **+8.70%** | **+8.34%** | +9.2% | -5.5% | `target_reclaim` |
| 8 | Book 3 | `2025-07-03 12:00` | `2025-07-04 08:00` | 20.0h | `$0.0571` | `$0.0524` | **-8.23%** | **-8.59%** | +5.3% | -8.6% | `stop_loss` |
| 9 | Book 3 | `2025-07-12 12:00` | `2025-07-13 11:00` | 23.0h | `$0.0634` | `$0.0689` | **+8.70%** | **+8.34%** | +10.1% | -3.1% | `target_reclaim` |
| 10 | Book 3 | `2025-07-14 08:00` | `2025-07-15 03:00` | 19.0h | `$0.0686` | `$0.0630` | **-8.23%** | **-8.59%** | +3.8% | -10.0% | `stop_loss` |
| 11 | Book 3 | `2025-07-21 01:00` | `2025-07-21 02:00` | 1.0h | `$0.0715` | `$0.0777` | **+8.70%** | **+8.34%** | +9.2% | -0.4% | `target_reclaim` |
| 12 | Book 3 | `2025-07-23 10:00` | `2025-07-23 21:00` | 11.0h | `$0.0771` | `$0.0708` | **-8.23%** | **-8.59%** | +3.3% | -9.1% | `stop_loss` |
| 13 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0116` | `$0.0117` | **+1.32%** | **+1.31%** | +19.5% | -27.4% | `time_expiry` |
| 14 | Book 3 | `2026-08-28 20:00` | `2026-08-28 21:00` | 1.0h | `$0.0131` | `$0.0142` | **+8.70%** | **+8.34%** | +10.9% | -1.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `8` | `100.0%` | **`+66.7%`** |
| `stop_loss` | `5` | `0.0%` | **`-42.9%`** |
| `time_expiry` | `1` | `100.0%` | **`+1.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `CHILLGUY`

* **Total Candidate Breakouts Filtered (Vetoed):** `70`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `52` (74.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `22`
* **Saved Capital Losses Avoided:** `+1,002.2%`
* **Missed Upside Forgone:** `-820.4%`
* **Net Veto Alpha:** `+181.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `33` | `47.1%` |
| `Core 1: Macro Bear Veto` | `28` | `40.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `6` | `8.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `3` | `4.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*