# Kronos V12: Institutional Symbol Tear Sheet — `NOW`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`2` Closed, `1` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.418`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+1.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.02x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.84%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-4.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`102.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.4% / -5.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-26 20:00` | `2026-09-02 20:00` | 168.0h | `$131.0067` | `$138.6924` | **+5.87%** | **+5.70%** | +14.2% | -4.2% | `time_cap` |
| 2 | Book 2 | `2026-09-15 15:00` | `2026-09-17 03:00` | 36.0h | `$146.9164` | `$141.1263` | **-3.94%** | **-4.02%** | +0.6% | -5.7% | `stall_bailout` |
| 3 | Book 2 | `2026-10-06 13:00` | `_Open Live_` | 15.9h | `$140.4903` | `$138.0300` | **-1.75%** | **-1.77%** | +0.1% | -2.9% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `1` | `0.0%` | **`-4.0%`** |
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