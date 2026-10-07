# Kronos V12: Institutional Symbol Tear Sheet — `VANA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.328`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+5.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.06x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.94%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-11.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`34.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.6% / -5.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-02-10 01:00` | `2025-02-11 02:00` | 25.0h | `$5.9938` | `$6.5150` | **+8.70%** | **+8.34%** | +9.3% | -1.3% | `target_reclaim` |
| 2 | Book 3 | `2025-05-12 18:00` | `2025-05-13 12:00` | 18.0h | `$6.2302` | `$6.7720` | **+8.70%** | **+8.34%** | +13.7% | -2.9% | `target_reclaim` |
| 3 | Book 3 | `2025-05-14 13:00` | `2025-05-15 06:00` | 17.0h | `$6.6553` | `$6.1076` | **-8.23%** | **-8.59%** | +2.5% | -8.2% | `stop_loss` |
| 4 | Book 3 | `2025-07-15 01:00` | `2025-07-18 01:00` | 72.0h | `$4.8447` | `$5.0932` | **+5.13%** | **+5.00%** | +7.0% | -1.7% | `time_expiry` |
| 5 | Book 3 | `2025-07-23 20:00` | `2025-07-26 20:00` | 72.0h | `$4.9928` | `$5.0493` | **+1.13%** | **+1.13%** | +4.4% | -6.2% | `time_expiry` |
| 6 | Book 3 | `2025-09-22 01:00` | `2025-09-22 06:00` | 5.0h | `$4.6920` | `$4.3058` | **-8.23%** | **-8.59%** | +2.8% | -11.9% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |
| `time_expiry` | `2` | `100.0%` | **`+6.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `VANA`

* **Total Candidate Breakouts Filtered (Vetoed):** `49`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `33` (67.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `6`
* **Saved Capital Losses Avoided:** `+359.0%`
* **Missed Upside Forgone:** `-155.1%`
* **Net Veto Alpha:** `+203.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `18` | `36.7%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `16` | `32.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `15` | `30.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*