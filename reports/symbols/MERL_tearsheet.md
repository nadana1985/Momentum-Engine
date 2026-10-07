# Kronos V12: Institutional Symbol Tear Sheet — `MERL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`42.9%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.782`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-5.9%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.94x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.85%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-18.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`33.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.6% / -7.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-07 00:00` | `2025-07-10 00:00` | 72.0h | `$0.1047` | `$0.1096` | **+4.75%** | **+4.64%** | +6.3% | -2.3% | `time_expiry` |
| 2 | Book 3 | `2025-07-23 20:00` | `2025-07-24 02:00` | 6.0h | `$0.1167` | `$0.1269` | **+8.70%** | **+8.34%** | +25.9% | -2.0% | `target_reclaim` |
| 3 | Book 3 | `2025-07-24 09:00` | `2025-07-24 12:00` | 3.0h | `$0.1334` | `$0.1224` | **-8.23%** | **-8.59%** | +9.6% | -8.4% | `stop_loss` |
| 4 | Book 3 | `2025-10-25 14:00` | `2025-10-26 02:00` | 12.0h | `$0.3849` | `$0.4184` | **+8.70%** | **+8.34%** | +9.0% | -0.9% | `target_reclaim` |
| 5 | Book 3 | `2025-10-27 17:00` | `2025-10-28 00:00` | 7.0h | `$0.3910` | `$0.3588` | **-8.23%** | **-8.59%** | +2.6% | -11.4% | `stop_loss` |
| 6 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0198` | `$0.0196` | **-1.48%** | **-1.49%** | +16.9% | -15.3% | `time_expiry` |
| 7 | Book 3 | `2026-08-28 10:00` | `2026-08-30 23:00` | 61.0h | `$0.0218` | `$0.0200` | **-8.23%** | **-8.59%** | +4.1% | -10.2% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |
| `time_expiry` | `2` | `50.0%` | **`+3.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `MERL`

* **Total Candidate Breakouts Filtered (Vetoed):** `57`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `49` (86.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `14`
* **Saved Capital Losses Avoided:** `+887.5%`
* **Missed Upside Forgone:** `-456.2%`
* **Net Veto Alpha:** `+431.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `36` | `63.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `10` | `17.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `8` | `14.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `3` | `5.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*