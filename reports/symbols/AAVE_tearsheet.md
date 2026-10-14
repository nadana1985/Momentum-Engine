# Kronos V12: Institutional Symbol Tear Sheet — `AAVE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `16` (`16` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `16` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`37.5%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`1.171`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+11.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.13x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.74%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-52.2%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`67.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.2% / -7.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2022-11-04 07:00` | `2022-11-06 07:00` | 48.0h | `$95.5683` | `$91.9496` | **-6.64%** | **-6.84%** | +2.8% | -7.2% | `fast_decay_cut` |
| 2 | Book 1 | `2023-01-11 23:00` | `2023-01-14 06:00` | 55.0h | `$64.3204` | `$77.1845` | **+29.54%** | **+25.83%** | +26.8% | -2.7% | `target_reclaim` |
| 3 | Book 3 | `2023-01-18 00:00` | `2023-01-18 14:00` | 14.0h | `$84.4286` | `$90.0000` | **+6.60%** | **+6.39%** | +6.6% | -1.9% | `target_reclaim` |
| 4 | Book 2 | `2023-05-05 16:00` | `2023-05-07 04:00` | 36.0h | `$73.6938` | `$69.3662` | **-6.10%** | **-6.29%** | +0.8% | -7.2% | `stall_bailout` |
| 5 | Book 5 (Shelf Absorption Squeeze) | `2023-06-25 03:00` | `2023-06-29 03:00` | Live | `$60.6004` | `$65.7514` | **+8.50%** | **+8.16%** | +23.9% | -13.2% | `shelf_target_reclaim` |
| 6 | Book 3 | `2023-06-26 16:00` | `2023-06-28 19:00` | 51.0h | `$63.8503` | `$58.5954` | **-8.23%** | **-8.59%** | +4.4% | -10.4% | `stop_loss` |
| 7 | Book 3 | `2023-07-17 10:00` | `2023-07-20 10:00` | 72.0h | `$74.7817` | `$74.0544` | **-0.97%** | **-0.98%** | +2.3% | -5.5% | `time_expiry` |
| 8 | Book 2 | `2023-09-20 20:00` | `2023-09-22 08:00` | 36.0h | `$65.8141` | `$63.5807` | **-3.41%** | **-3.47%** | +0.4% | -6.3% | `stall_bailout` |
| 9 | Book 3 | `2023-10-07 03:00` | `2023-10-10 03:00` | 72.0h | `$66.0043` | `$63.8699` | **-3.23%** | **-3.29%** | +3.9% | -6.3% | `time_expiry` |
| 10 | Book 1 | `2023-11-13 00:00` | `2023-11-14 00:00` | 24.0h | `$103.5382` | `$91.5406` | **-12.55%** | **-13.23%** | +1.2% | -12.3% | `initial_stop` |
| 11 | Book 3 | `2024-02-28 17:00` | `2024-02-28 22:00` | 5.0h | `$100.7808` | `$104.9800` | **+4.17%** | **+4.08%** | +8.1% | -4.7% | `target_reclaim` |
| 12 | Book 3 | `2024-03-14 13:00` | `2024-03-15 03:00` | 14.0h | `$138.8464` | `$127.4193` | **-8.23%** | **-8.59%** | +2.1% | -9.6% | `stop_loss` |
| 13 | Book 4 | `2024-05-23 21:00` | `2024-06-07 18:00` | 357.0h | `$98.4575` | `$90.9933` | **-9.22%** | **-9.59%** | +16.5% | -10.7% | `structural_stop` |
| 14 | Book 3 | `2024-11-12 10:00` | `2024-11-14 14:00` | 52.0h | `$180.5684` | `$165.7076` | **-8.23%** | **-8.59%** | +4.1% | -8.8% | `stop_loss` |
| 15 | Book 4 | `2025-05-08 19:00` | `2025-05-14 01:00` | 126.0h | `$198.7777` | `$238.5333` | **+29.47%** | **+26.35%** | +20.3% | -1.5% | `target_reclaim` |
| 16 | Book 4 | `2026-08-21 08:00` | `2026-08-23 12:00` | 52.0h | `$110.0348` | `$132.0418` | **+11.25%** | **+10.50%** | +22.6% | -4.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `5` | `100.0%` | **`+73.2%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `stall_bailout` | `2` | `0.0%` | **`-9.8%`** |
| `time_expiry` | `2` | `0.0%` | **`-4.3%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `initial_stop` | `1` | `0.0%` | **`-13.2%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-6.8%`** |
| `structural_stop` | `1` | `0.0%` | **`-9.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `AAVE`

* **Total Candidate Breakouts Filtered (Vetoed):** `429`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `293` (68.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `61`
* **Saved Capital Losses Avoided:** `+3,296.6%`
* **Missed Upside Forgone:** `-2,139.2%`
* **Net Veto Alpha:** `+1,157.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `225` | `52.4%` |
| `Core 1: Macro Bear Veto` | `125` | `29.1%` |
| `Core 4: Defensible Whale Dump` | `40` | `9.3%` |
| `Core 4: Funding Rate Cap` | `21` | `4.9%` |
| `Core 4: Whale Firewall` | `12` | `2.8%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `6` | `1.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*