# Kronos V12: Institutional Symbol Tear Sheet — `DRIFT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`25.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.324`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-17.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.84x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-4.36%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`22.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.2% / -7.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-30 06:00` | `2025-05-30 12:00` | 6.0h | `$0.6816` | `$0.6255` | **-8.23%** | **-8.59%** | +8.1% | -8.3% | `stop_loss` |
| 2 | Book 3 | `2025-09-18 02:00` | `2025-09-18 08:00` | 6.0h | `$0.7930` | `$0.8620` | **+8.70%** | **+8.34%** | +8.8% | -0.5% | `target_reclaim` |
| 3 | Book 3 | `2025-09-19 15:00` | `2025-09-22 03:00` | 60.0h | `$0.8538` | `$0.7835` | **-8.23%** | **-8.59%** | +5.2% | -10.2% | `stop_loss` |
| 4 | Book 3 | `2026-09-23 14:00` | `2026-09-24 08:00` | 18.0h | `$0.0196` | `$0.0180` | **-8.23%** | **-8.59%** | +2.5% | -11.1% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `DRIFT`

* **Total Candidate Breakouts Filtered (Vetoed):** `38`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `26` (68.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `11`
* **Saved Capital Losses Avoided:** `+485.4%`
* **Missed Upside Forgone:** `-376.6%`
* **Net Veto Alpha:** `+108.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `17` | `44.7%` |
| `Core 1: Macro Bear Veto` | `15` | `39.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `5` | `13.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `2.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*