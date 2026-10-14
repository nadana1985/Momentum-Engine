# Kronos V12: Institutional Symbol Tear Sheet — `GAS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `12` (`12` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `12` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.119`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+29.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.34x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.43%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-22.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`20.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.1% / -4.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-03-03 07:00` | `2024-03-03 09:00` | 2.0h | `$6.8918` | `$7.1790` | **+4.17%** | **+4.08%** | +6.1% | -7.4% | `target_reclaim` |
| 2 | Book 3 | `2024-03-14 19:00` | `2024-03-15 00:00` | 5.0h | `$7.1091` | `$8.1650` | **+14.85%** | **+13.85%** | +15.0% | -0.2% | `target_reclaim` |
| 3 | Book 3 | `2024-07-21 17:00` | `2024-07-22 00:00` | 7.0h | `$3.8766` | `$4.0410` | **+4.24%** | **+4.15%** | +6.3% | -2.7% | `target_reclaim` |
| 4 | Book 3 | `2024-11-11 06:00` | `2024-11-11 23:00` | 17.0h | `$4.1820` | `$4.5230` | **+8.15%** | **+7.84%** | +9.3% | -0.2% | `target_reclaim` |
| 5 | Book 3 | `2024-11-13 04:00` | `2024-11-14 00:00` | 20.0h | `$4.1820` | `$4.5690` | **+9.25%** | **+8.85%** | +11.0% | -1.4% | `target_reclaim` |
| 6 | Book 5 (Shelf Absorption Squeeze) | `2025-01-09 02:00` | `2025-01-13 02:00` | Live | `$5.6019` | `$5.1425` | **-8.20%** | **-8.56%** | +-1.1% | -25.3% | `shelf_stop_loss` |
| 7 | Book 3 | `2025-02-01 14:00` | `2025-02-02 03:00` | 13.0h | `$4.7587` | `$4.3671` | **-8.23%** | **-8.59%** | +1.9% | -9.7% | `stop_loss` |
| 8 | Book 3 | `2025-07-22 01:00` | `2025-07-23 08:00` | 31.0h | `$3.4541` | `$3.5980` | **+4.17%** | **+4.08%** | +4.7% | -1.5% | `target_reclaim` |
| 9 | Book 3 | `2025-07-23 20:00` | `2025-07-25 06:00` | 34.0h | `$3.4992` | `$3.2112` | **-8.23%** | **-8.59%** | +2.8% | -8.3% | `stop_loss` |
| 10 | Book 2 | `2026-05-05 01:00` | `2026-05-07 03:00` | 50.0h | `$1.6401` | `$1.6349` | **-0.35%** | **-0.35%** | +3.0% | -1.0% | `fast_decay_cut` |
| 11 | Book 3 | `2026-08-27 06:00` | `2026-08-28 00:00` | 18.0h | `$1.3010` | `$1.3820` | **+6.23%** | **+6.04%** | +6.7% | 0.0% | `target_reclaim` |
| 12 | Book 3 | `2026-09-20 13:00` | `2026-09-21 14:00` | 25.0h | `$1.3097` | `$1.3960` | **+6.59%** | **+6.38%** | +6.8% | -0.5% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `8` | `100.0%` | **`+55.3%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `GAS`

* **Total Candidate Breakouts Filtered (Vetoed):** `161`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `117` (72.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `27`
* **Saved Capital Losses Avoided:** `+1,886.5%`
* **Missed Upside Forgone:** `-1,080.9%`
* **Net Veto Alpha:** `+805.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `97` | `60.2%` |
| `Core 1: Macro Bear Veto` | `46` | `28.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `14` | `8.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `3` | `1.9%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*