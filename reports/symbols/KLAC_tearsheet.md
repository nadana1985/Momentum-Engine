# Kronos V12: Institutional Symbol Tear Sheet — `KLAC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`1.431`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+2.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.02x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.70%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-1.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`80.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+3.6% / -3.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-26 21:00` | `2026-08-28 09:00` | 36.0h | `$189.0314` | `$182.0438` | **-3.70%** | **-3.77%** | +0.8% | -4.2% | `stall_bailout` |
| 2 | Book 2 | `2026-09-04 13:00` | `2026-09-06 01:00` | 36.0h | `$186.7256` | `$184.7171` | **-1.08%** | **-1.08%** | +0.4% | -5.6% | `stall_bailout` |
| 3 | Book 2 | `2026-09-29 08:00` | `2026-10-06 08:00` | 168.0h | `$192.7607` | `$206.6122` | **+7.19%** | **+6.94%** | +9.5% | -1.1% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `2` | `0.0%` | **`-4.8%`** |
| `time_cap` | `1` | `100.0%` | **`+6.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `KLAC`

* **Total Candidate Breakouts Filtered (Vetoed):** `9`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `9` (100.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+157.8%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+157.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `9` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*