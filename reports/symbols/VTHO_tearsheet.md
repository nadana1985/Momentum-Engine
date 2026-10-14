# Kronos V12: Institutional Symbol Tear Sheet — `VTHO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.205`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+8.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.09x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.97%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-7.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`36.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+27.9% / -13.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-04-14 09:00` | `2025-04-18 09:00` | Live | `$0.0025` | `$0.0027` | **+8.50%** | **+8.16%** | +12.5% | -12.3% | `shelf_target_reclaim` |
| 2 | Book 1 | `2026-09-08 10:00` | `2026-09-09 22:00` | 36.0h | `$0.0004` | `$0.0004` | **-7.15%** | **-7.40%** | +3.2% | -4.6% | `fast_decay_cut` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2026-09-10 02:00` | `2026-09-14 02:00` | Live | `$0.0006` | `$0.0007` | **+8.50%** | **+8.16%** | +68.1% | -22.6% | `shelf_target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-7.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `VTHO`

* **Total Candidate Breakouts Filtered (Vetoed):** `17`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `10` (58.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+113.7%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+113.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `7` | `41.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `6` | `35.3%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `2` | `11.8%` |
| `Core 4: Whale Firewall` | `2` | `11.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*