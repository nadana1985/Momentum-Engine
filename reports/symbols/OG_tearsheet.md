# Kronos V12: Institutional Symbol Tear Sheet — `OG`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`85.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.987`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+34.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.41x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.89%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`40.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.0% / -5.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-23 15:00` | `2025-07-25 22:00` | 55.0h | `$4.7408` | `$5.1530` | **+8.70%** | **+8.34%** | +8.8% | -6.0% | `target_reclaim` |
| 2 | Book 3 | `2025-07-28 17:00` | `2025-07-30 17:00` | 48.0h | `$5.1244` | `$5.5700` | **+8.70%** | **+8.34%** | +8.9% | -3.9% | `target_reclaim` |
| 3 | Book 3 | `2025-08-15 01:00` | `2025-08-15 02:00` | 1.0h | `$14.5434` | `$15.8080` | **+8.70%** | **+8.34%** | +11.9% | -4.3% | `target_reclaim` |
| 4 | Book 3 | `2025-09-25 13:00` | `2025-09-26 20:00` | 31.0h | `$16.8388` | `$18.3030` | **+8.70%** | **+8.34%** | +9.8% | -1.3% | `target_reclaim` |
| 5 | Book 3 | `2026-05-11 10:00` | `2026-05-13 14:00` | 52.0h | `$3.6340` | `$3.3349` | **-8.23%** | **-8.59%** | +4.3% | -8.2% | `stop_loss` |
| 6 | Book 3 | `2026-08-22 05:00` | `2026-08-23 07:00` | 26.0h | `$2.6165` | `$2.8440` | **+8.70%** | **+8.34%** | +21.3% | -6.4% | `target_reclaim` |
| 7 | Book 3 | `2026-08-23 08:00` | `2026-08-26 08:00` | 72.0h | `$2.8796` | `$2.9127` | **+1.15%** | **+1.14%** | +11.7% | -5.7% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `5` | `100.0%` | **`+41.7%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_expiry` | `1` | `100.0%` | **`+1.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `OG`

* **Total Candidate Breakouts Filtered (Vetoed):** `67`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `36` (53.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `21`
* **Saved Capital Losses Avoided:** `+541.2%`
* **Missed Upside Forgone:** `-1,033.4%`
* **Net Veto Alpha:** `+-492.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `39` | `58.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `23` | `34.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `6.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `1.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*