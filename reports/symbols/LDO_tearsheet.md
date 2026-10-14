# Kronos V12: Institutional Symbol Tear Sheet — `LDO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `13` (`13` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `13` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`46.2%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.651`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+42.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.52x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+3.23%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-24.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`91.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.2% / -8.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-01-24 19:00` | `2023-01-24 22:00` | 3.0h | `$2.5484` | `$2.3387` | **-8.23%** | **-8.59%** | +2.6% | -10.2% | `stop_loss` |
| 2 | Book 1 | `2023-07-03 02:00` | `2023-07-05 13:00` | 59.0h | `$2.1943` | `$2.0573` | **-8.42%** | **-8.77%** | +2.4% | -7.1% | `fast_decay_cut` |
| 3 | Book 4 | `2023-10-24 17:00` | `2023-11-09 15:00` | 382.0h | `$1.7960` | `$2.1552` | **+35.73%** | **+31.28%** | +32.5% | -5.4% | `target_reclaim` |
| 4 | Book 3 | `2023-12-26 17:00` | `2023-12-27 14:00` | 21.0h | `$2.3058` | `$2.6286` | **+14.00%** | **+13.10%** | +20.4% | -0.2% | `target_reclaim` |
| 5 | Book 3 | `2024-01-03 12:00` | `2024-01-03 13:00` | 1.0h | `$2.8364` | `$3.0830` | **+8.70%** | **+8.34%** | +14.8% | -15.4% | `target_reclaim` |
| 6 | Book 3 | `2024-02-20 09:00` | `2024-02-23 09:00` | 72.0h | `$3.1581` | `$2.9694` | **-5.98%** | **-6.16%** | +6.4% | -7.1% | `time_expiry` |
| 7 | Book 3 | `2024-02-28 17:00` | `2024-02-29 01:00` | 8.0h | `$3.1581` | `$3.5607` | **+12.75%** | **+12.00%** | +13.8% | -3.1% | `target_reclaim` |
| 8 | Book 4 | `2024-05-24 14:00` | `2024-06-07 18:00` | 340.0h | `$2.4818` | `$2.1095` | **-18.12%** | **-19.64%** | +9.1% | -26.8% | `structural_stop` |
| 9 | Book 4 | `2024-11-24 23:00` | `2024-11-25 15:00` | 16.0h | `$1.4610` | `$1.7532` | **+14.45%** | **+13.64%** | +22.3% | -4.0% | `target_reclaim` |
| 10 | Book 3 | `2025-02-01 22:00` | `2025-02-02 16:00` | 18.0h | `$2.0844` | `$1.9128` | **-8.23%** | **-8.59%** | +0.8% | -8.8% | `stop_loss` |
| 11 | Book 2 | `2025-05-27 08:00` | `2025-05-30 00:00` | 64.0h | `$0.9315` | `$0.8549` | **-9.41%** | **-9.82%** | +8.7% | -9.3% | `initial_stop` |
| 12 | Book 1 | `2025-07-10 17:00` | `2025-07-17 16:00` | 167.0h | `$0.8139` | `$0.9767` | **+32.29%** | **+28.24%** | +24.0% | -2.6% | `target_reclaim` |
| 13 | Book 2 | `2026-05-06 09:00` | `2026-05-07 21:00` | 36.0h | `$0.3920` | `$0.3818` | **-2.97%** | **-3.01%** | +0.9% | -4.9% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `6` | `100.0%` | **`+106.6%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-8.8%`** |
| `stall_bailout` | `1` | `0.0%` | **`-3.0%`** |
| `initial_stop` | `1` | `0.0%` | **`-9.8%`** |
| `structural_stop` | `1` | `0.0%` | **`-19.6%`** |
| `time_expiry` | `1` | `0.0%` | **`-6.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `LDO`

* **Total Candidate Breakouts Filtered (Vetoed):** `75`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `54` (72.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `5`
* **Saved Capital Losses Avoided:** `+635.8%`
* **Missed Upside Forgone:** `-116.2%`
* **Net Veto Alpha:** `+519.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `48` | `64.0%` |
| `Core 4: Funding Rate Cap` | `12` | `16.0%` |
| `Core 0: Zero-Tolerance Data Firewall` | `10` | `13.3%` |
| `Core 4: Whale Firewall` | `4` | `5.3%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `1.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*