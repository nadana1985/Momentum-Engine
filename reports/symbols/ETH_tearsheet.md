# Kronos V12: Institutional Symbol Tear Sheet — `ETH`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`2.522`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+7.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.07x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.35%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-0.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`196.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.5% / -3.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2022-10-26 08:00` | `2022-10-28 08:00` | 48.0h | `$1539.9302` | `$1498.0256` | **-4.00%** | **-4.08%** | +3.6% | -3.6% | `fast_decay_cut` |
| 2 | Book 1 | `2024-11-09 19:00` | `2024-11-30 19:00` | 504.0h | `$3078.3767` | `$3682.7700` | **+12.41%** | **+11.70%** | +21.2% | -2.0% | `time_cap` |
| 3 | Book 1 | `2025-07-14 04:00` | `2025-07-15 16:00` | 36.0h | `$3059.6601` | `$3040.2404` | **-0.56%** | **-0.56%** | +0.8% | -4.2% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-4.1%`** |
| `stall_bailout` | `1` | `0.0%` | **`-0.6%`** |
| `time_cap` | `1` | `100.0%` | **`+11.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `ETH`

* **Total Candidate Breakouts Filtered (Vetoed):** `324`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `160` (49.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `22`
* **Saved Capital Losses Avoided:** `+1,702.0%`
* **Missed Upside Forgone:** `-655.5%`
* **Net Veto Alpha:** `+1,046.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `231` | `71.3%` |
| `Core 1: Macro Bear Veto` | `56` | `17.3%` |
| `Core 4: Funding Rate Cap` | `20` | `6.2%` |
| `Core 4: Defensible Whale Dump` | `12` | `3.7%` |
| `Core 4: Whale Firewall` | `5` | `1.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*