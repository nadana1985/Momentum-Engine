# Kronos V12: Institutional Symbol Tear Sheet — `FARTCOIN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`42.9%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.686`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-12.2%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.88x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.75%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-33.4%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`24.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+20.6% / -12.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2024-12-30 20:00` | `2025-01-03 20:00` | Live | `$0.8634` | `$0.9368` | **+8.50%** | **+8.16%** | +66.9% | -27.9% | `shelf_target_reclaim` |
| 2 | Book 3 | `2025-01-19 23:00` | `2025-01-20 00:00` | 1.0h | `$2.4647` | `$2.1584` | **-12.43%** | **-13.27%** | +8.7% | -23.9% | `stop_loss` |
| 3 | Book 4 | `2025-04-09 19:00` | `2025-04-11 10:00` | 39.0h | `$0.7535` | `$0.9042` | **+5.79%** | **+5.65%** | +23.4% | -10.0% | `target_reclaim` |
| 4 | Book 3 | `2025-05-02 21:00` | `2025-05-05 02:00` | 53.0h | `$1.1475` | `$1.0530` | **-8.23%** | **-8.59%** | +2.9% | -8.5% | `stop_loss` |
| 5 | Book 3 | `2025-07-14 18:00` | `2025-07-15 14:00` | 20.0h | `$1.3026` | `$1.1954` | **-8.23%** | **-8.59%** | +2.9% | -8.4% | `stop_loss` |
| 6 | Book 3 | `2025-07-24 06:00` | `2025-07-25 15:00` | 33.0h | `$1.3805` | `$1.2669` | **-8.23%** | **-8.59%** | +5.0% | -9.2% | `stop_loss` |
| 7 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.1610` | `$0.1833` | **+13.86%** | **+12.98%** | +34.2% | -1.7% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `4` | `0.0%` | **`-39.0%`** |
| `target_reclaim` | `2` | `100.0%` | **`+18.6%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `FARTCOIN`

* **Total Candidate Breakouts Filtered (Vetoed):** `121`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `89` (73.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `23`
* **Saved Capital Losses Avoided:** `+1,229.2%`
* **Missed Upside Forgone:** `-817.3%`
* **Net Veto Alpha:** `+411.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `95` | `78.5%` |
| `Core 4: Defensible Whale Dump` | `19` | `15.7%` |
| `Core 4: Funding Rate Cap` | `6` | `5.0%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*