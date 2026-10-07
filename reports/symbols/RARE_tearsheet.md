# Kronos V12: Institutional Symbol Tear Sheet — `RARE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.942`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+16.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.18x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.70%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`12.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.3% / -4.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-11-01 22:00` | `2024-11-02 04:00` | 6.0h | `$0.1264` | `$0.1374` | **+8.70%** | **+8.34%** | +10.8% | -4.4% | `target_reclaim` |
| 2 | Book 3 | `2025-04-24 08:00` | `2025-04-24 13:00` | 5.0h | `$0.0584` | `$0.0635` | **+8.70%** | **+8.34%** | +11.1% | -0.4% | `target_reclaim` |
| 3 | Book 3 | `2025-05-15 05:00` | `2025-05-16 22:00` | 41.0h | `$0.0698` | `$0.0640` | **-8.23%** | **-8.59%** | +3.7% | -8.1% | `stop_loss` |
| 4 | Book 3 | `2025-08-05 14:00` | `2025-08-06 04:00` | 14.0h | `$0.0651` | `$0.0597` | **-8.23%** | **-8.59%** | +5.8% | -8.2% | `stop_loss` |
| 5 | Book 3 | `2026-09-26 00:00` | `2026-09-26 06:00` | 6.0h | `$0.0149` | `$0.0162` | **+8.70%** | **+8.34%** | +46.0% | -1.6% | `target_reclaim` |
| 6 | Book 3 | `2026-09-27 00:00` | `2026-09-27 05:00` | 5.0h | `$0.0200` | `$0.0217` | **+8.70%** | **+8.34%** | +14.2% | -6.7% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+33.4%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `RARE`

* **Total Candidate Breakouts Filtered (Vetoed):** `46`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `29` (63.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `11`
* **Saved Capital Losses Avoided:** `+503.2%`
* **Missed Upside Forgone:** `-354.6%`
* **Net Veto Alpha:** `+148.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `22` | `47.8%` |
| `Core 1: Macro Bear Veto` | `15` | `32.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `6` | `13.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `3` | `6.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*