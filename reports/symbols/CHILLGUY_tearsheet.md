# Kronos V12: Institutional Symbol Tear Sheet — `CHILLGUY`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `12` (`12` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `12` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.986`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-0.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.06%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-21.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`20.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.1% / -7.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-04-23 16:00` | `2025-04-23 17:00` | 1.0h | `$0.0258` | `$0.0269` | **+4.17%** | **+4.08%** | +27.9% | -1.6% | `target_reclaim` |
| 2 | Book 3 | `2025-05-05 22:00` | `2025-05-06 20:00` | 22.0h | `$0.0528` | `$0.0485` | **-8.23%** | **-8.59%** | +3.7% | -8.2% | `stop_loss` |
| 3 | Book 3 | `2025-05-12 01:00` | `2025-05-12 02:00` | 1.0h | `$0.0889` | `$0.0967` | **+8.70%** | **+8.34%** | +16.9% | -2.7% | `target_reclaim` |
| 4 | Book 3 | `2025-05-12 05:00` | `2025-05-12 06:00` | 1.0h | `$0.0953` | `$0.1035` | **+8.70%** | **+8.34%** | +20.5% | -0.5% | `target_reclaim` |
| 5 | Book 3 | `2025-05-14 17:00` | `2025-05-15 13:00` | 20.0h | `$0.1054` | `$0.0968` | **-8.23%** | **-8.59%** | +8.9% | -8.9% | `stop_loss` |
| 6 | Book 3 | `2025-07-01 04:00` | `2025-07-01 20:00` | 16.0h | `$0.0495` | `$0.0454` | **-8.23%** | **-8.59%** | +1.6% | -9.5% | `stop_loss` |
| 7 | Book 3 | `2025-07-03 15:00` | `2025-07-06 15:00` | 72.0h | `$0.0553` | `$0.0578` | **+4.46%** | **+4.37%** | +6.7% | -7.3% | `time_expiry` |
| 8 | Book 3 | `2025-07-14 05:00` | `2025-07-14 12:00` | 7.0h | `$0.0716` | `$0.0657` | **-8.23%** | **-8.59%** | +4.6% | -9.4% | `stop_loss` |
| 9 | Book 3 | `2025-07-22 08:00` | `2025-07-22 16:00` | 8.0h | `$0.0709` | `$0.0777` | **+9.58%** | **+9.15%** | +12.6% | -0.7% | `target_reclaim` |
| 10 | Book 3 | `2025-07-23 07:00` | `2025-07-23 17:00` | 10.0h | `$0.0786` | `$0.0721` | **-8.23%** | **-8.59%** | +8.1% | -9.2% | `stop_loss` |
| 11 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0111` | `$0.0131` | **+18.00%** | **+16.55%** | +24.5% | -24.3% | `climax_whale_euphoria_harvest` |
| 12 | Book 3 | `2026-08-30 07:00` | `2026-08-30 21:00` | 14.0h | `$0.0127` | `$0.0117` | **-8.23%** | **-8.59%** | +9.7% | -8.9% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `6` | `0.0%` | **`-51.5%`** |
| `target_reclaim` | `4` | `100.0%` | **`+29.9%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+16.6%`** |
| `time_expiry` | `1` | `100.0%` | **`+4.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `CHILLGUY`

* **Total Candidate Breakouts Filtered (Vetoed):** `70`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `52` (74.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `22`
* **Saved Capital Losses Avoided:** `+1,001.3%`
* **Missed Upside Forgone:** `-820.4%`
* **Net Veto Alpha:** `+180.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `33` | `47.1%` |
| `Core 1: Macro Bear Veto` | `28` | `40.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `6` | `8.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `3` | `4.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*