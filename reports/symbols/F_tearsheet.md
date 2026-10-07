# Kronos V12: Institutional Symbol Tear Sheet — `F`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.235`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+2.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.02x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.67%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`29.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.6% / -7.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-24 06:00` | `2025-07-24 16:00` | 10.0h | `$0.0091` | `$0.0084` | **-8.23%** | **-8.59%** | +2.6% | -9.5% | `stop_loss` |
| 2 | Book 3 | `2026-09-09 22:00` | `2026-09-12 22:00` | 72.0h | `$0.0033` | `$0.0033` | **+2.30%** | **+2.27%** | +5.1% | -5.1% | `time_expiry` |
| 3 | Book 3 | `2026-09-18 17:00` | `2026-09-18 22:00` | 5.0h | `$0.0046` | `$0.0050` | **+8.70%** | **+8.34%** | +21.2% | -6.3% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |
| `time_expiry` | `1` | `100.0%` | **`+2.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `F`

* **Total Candidate Breakouts Filtered (Vetoed):** `32`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `29` (90.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `13`
* **Saved Capital Losses Avoided:** `+655.0%`
* **Missed Upside Forgone:** `-984.3%`
* **Net Veto Alpha:** `+-329.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `24` | `75.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `6` | `18.8%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `1` | `3.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `3.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*