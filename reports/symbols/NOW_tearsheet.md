# Kronos V12: Institutional Symbol Tear Sheet — `NOW`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.964`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-0.2%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`1.00x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.07%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-5.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`80.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.1% / -4.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-26 20:00` | `2026-09-02 20:00` | 168.0h | `$131.0067` | `$138.6924` | **+5.87%** | **+5.70%** | +14.2% | -4.2% | `time_cap` |
| 2 | Book 2 | `2026-09-15 15:00` | `2026-09-17 03:00` | 36.0h | `$146.9164` | `$141.1263` | **-3.94%** | **-4.02%** | +0.6% | -5.7% | `stall_bailout` |
| 3 | Book 2 | `2026-10-06 13:00` | `2026-10-08 01:00` | 36.0h | `$140.4903` | `$137.8545` | **-1.88%** | **-1.89%** | +0.4% | -2.9% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `2` | `0.0%` | **`-5.9%`** |
| `time_cap` | `1` | `100.0%` | **`+5.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `NOW`

* **Total Candidate Breakouts Filtered (Vetoed):** `28`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `18` (64.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+124.5%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+124.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `27` | `96.4%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `3.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*