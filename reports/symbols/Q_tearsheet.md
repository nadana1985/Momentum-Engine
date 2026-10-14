# Kronos V12: Institutional Symbol Tear Sheet — `Q`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.580`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+2.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.02x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.04%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-3.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`5.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+20.7% / -23.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2026-05-09 12:00` | `2026-05-09 17:00` | 5.0h | `$0.0143` | `$0.0172` | **+5.79%** | **+5.65%** | +24.7% | -1.6% | `target_reclaim` |
| 2 | Book 1 | `2026-09-26 11:00` | `2026-09-26 16:00` | 5.0h | `$0.0359` | `$0.0353` | **-3.53%** | **-3.58%** | +16.8% | -45.7% | `breakeven_ratchet` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `1` | `0.0%` | **`-3.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+5.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `Q`

* **Total Candidate Breakouts Filtered (Vetoed):** `111`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `102` (91.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `29`
* **Saved Capital Losses Avoided:** `+2,308.4%`
* **Missed Upside Forgone:** `-982.1%`
* **Net Veto Alpha:** `+1,326.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `103` | `92.8%` |
| `Core 4: Whale Firewall` | `6` | `5.4%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `1` | `0.9%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*