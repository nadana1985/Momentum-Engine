# Kronos V12: Institutional Symbol Tear Sheet — `BOT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`2.069`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+2.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.02x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.76%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-1.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`67.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.7% / -3.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-03 14:00` | `2026-09-05 14:00` | 48.0h | `$26.8169` | `$26.7430` | **-0.30%** | **-0.30%** | +3.0% | -3.9% | `fast_decay_cut` |
| 2 | Book 3 | `2026-09-18 02:00` | `2026-09-18 16:00` | 14.0h | `$27.5149` | `$28.7500` | **+4.49%** | **+4.39%** | +4.6% | -1.0% | `target_reclaim` |
| 3 | Book 2 | `2026-10-02 18:00` | `2026-10-08 15:00` | 141.0h | `$28.6214` | `$28.1216` | **-1.81%** | **-1.82%** | +21.5% | -4.2% | `breakeven_ratchet` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `1` | `0.0%` | **`-1.8%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.3%`** |
| `target_reclaim` | `1` | `100.0%` | **`+4.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `BOT`

* **Total Candidate Breakouts Filtered (Vetoed):** `8`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `6` (75.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+46.2%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+46.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `7` | `87.5%` |
| `Core 1: Macro Bear Veto` | `1` | `12.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*