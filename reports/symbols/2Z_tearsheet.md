# Kronos V12: Institutional Symbol Tear Sheet — `2Z`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`6.632`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+3.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.04x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.73%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`26.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+3.3% / -1.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-05-02 15:00` | `2026-05-04 15:00` | 48.0h | `$0.0848` | `$0.0843` | **-0.61%** | **-0.62%** | +2.1% | -2.3% | `fast_decay_cut` |
| 2 | Book 3 | `2026-09-25 06:00` | `2026-09-25 10:00` | 4.0h | `$0.0534` | `$0.0556` | **+4.17%** | **+4.08%** | +4.5% | -0.3% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+4.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `2Z`

* **Total Candidate Breakouts Filtered (Vetoed):** `37`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `26` (70.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `4`
* **Saved Capital Losses Avoided:** `+288.5%`
* **Missed Upside Forgone:** `-133.0%`
* **Net Veto Alpha:** `+155.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `31` | `83.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `4` | `10.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `2` | `5.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*