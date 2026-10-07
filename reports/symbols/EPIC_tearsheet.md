# Kronos V12: Institutional Symbol Tear Sheet — `EPIC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`21.259`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+44.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.56x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+14.75%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`40.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+27.4% / -5.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-05-04 00:00` | `2026-05-06 00:00` | 48.0h | `$0.3601` | `$0.3523` | **-2.16%** | **-2.18%** | +3.7% | -6.7% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-04 16:00` | `2026-09-06 10:00` | 42.0h | `$0.3601` | `$0.4743` | **+31.72%** | **+27.55%** | +36.0% | -5.1% | `climax_top_harvest` |
| 3 | Book 2 | `2026-09-18 18:00` | `2026-09-20 00:00` | 30.0h | `$0.3799` | `$0.4590` | **+20.79%** | **+18.89%** | +42.5% | -4.4% | `trail_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `climax_top_harvest` | `1` | `100.0%` | **`+27.5%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-2.2%`** |
| `trail_stop` | `1` | `100.0%` | **`+18.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `EPIC`

* **Total Candidate Breakouts Filtered (Vetoed):** `52`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `31` (59.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `17`
* **Saved Capital Losses Avoided:** `+594.6%`
* **Missed Upside Forgone:** `-1,492.8%`
* **Net Veto Alpha:** `+-898.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `39` | `75.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `13` | `25.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*