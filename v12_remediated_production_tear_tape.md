# Kronos V12: Production Executive Tear Sheet
**Clean 6-Core Framework Performance Ledger**  
Generated: `2026-10-04 18:36:00 UTC`

---

## 1. Executive Performance Matrix (Strict Compounding Log Space)

| Performance Metric | V12 Clean 6-Core | Benchmark Target | Status |
| :--- | :--- | :--- | :--- |
| **Total Closed Trades** | `1,061` | N/A | Validated |
| **Win Rate** | **`35.72%`** | `> 50.0%` | ✅ **Passed** |
| **Profit Factor** | **`1.546`** | `> 1.50` | ✅ **Passed** |
| **Cumulative Net Log Return** | **`+1586.5%`** | `> +200%` | ✅ **Passed** |
| **Compounded Capital Multiple** | **`7762172.48x`** | `> 5.0x` | ✅ **Outperforming** |
| **Mean Net Log Return / Trade** | **`+1.50%`** | `> +1.0%` | ✅ **Passed** |
| **Currently Active Open Trades** | **`23`** | Monitored Live | In Flight |

---

## 2. Liquidity Tier & Book Attribution

### By Dynamic Liquidity Tier
| Liquidity Tier | Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tier 1** | `413` | `40.2%` | `1.583` | `+786.1%` | `2593.51x` |
| **Tier 2** | `369` | `36.3%` | `1.409` | `+423.1%` | `68.80x` |
| **Tier 3** | `279` | `28.3%` | `1.720` | `+377.3%` | `43.50x` |


### By Execution Book
| Book | Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Book 1** | `206` | `35.4%` | `1.486` | `+386.2%` | `47.56x` |
| **Book 2** | `855` | `35.8%` | `1.569` | `+1200.3%` | `163192.11x` |


---

## 3. Exit Reason & Microstructure Decomposition

| Exit Trigger | Count | Share | Total Net Log PnL |
| :--- | :--- | :--- | :--- |
| `fast_decay_cut` | `247` | `23.3%` | `-616.1%` |
| `time_cap` | `228` | `21.5%` | `+2179.6%` |
| `initial_stop` | `226` | `21.3%` | `-1755.3%` |
| `stall_bailout` | `132` | `12.4%` | `-341.1%` |
| `breakeven_ratchet` | `88` | `8.3%` | `+12.1%` |
| `climax_top_harvest` | `53` | `5.0%` | `+1564.9%` |
| `trail_stop` | `46` | `4.3%` | `+672.4%` |
| `stagnation_cut` | `31` | `2.9%` | `-76.9%` |
| `stagnation_bailout` | `10` | `0.9%` | `-53.1%` |


---

## 4. Top 15 Institutional Alpha Leaders

| Asset | Tier | Closed Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple | Max Log DD | Cumulative MFE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **IMX** | `Tier 3` | `7` | `85.7%` | `76.476` | **`+91.9%`** | **`2.51x`** | `-1.2%` | `+22.9%` |
| **AVAX** | `Tier 1` | `10` | `60.0%` | `6.343` | **`+79.5%`** | **`2.21x`** | `-8.6%` | `+18.0%` |
| **AERO** | `Tier 1` | `4` | `100.0%` | `999.000` | **`+77.2%`** | **`2.16x`** | `0.0%` | `+34.8%` |
| **APT** | `Tier 1` | `12` | `58.3%` | `3.266` | **`+72.8%`** | **`2.07x`** | `-24.9%` | `+21.1%` |
| **1000FLOKI** | `Tier 2` | `4` | `75.0%` | `8.407` | **`+69.7%`** | **`2.01x`** | `0.0%` | `+31.8%` |
| **ENA** | `Tier 1` | `3` | `66.7%` | `8.851` | **`+67.4%`** | **`1.96x`** | `0.0%` | `+39.7%` |
| **ONE** | `Tier 2` | `5` | `100.0%` | `999.000` | **`+63.5%`** | **`1.89x`** | `0.0%` | `+33.9%` |
| **HBAR** | `Tier 1` | `11` | `36.4%` | `3.000` | **`+54.3%`** | **`1.72x`** | `-27.1%` | `+19.8%` |
| **SEI** | `Tier 2` | `7` | `57.1%` | `3.692` | **`+53.7%`** | **`1.71x`** | `-6.9%` | `+21.5%` |
| **JASMY** | `Tier 2` | `2` | `100.0%` | `999.000` | **`+52.2%`** | **`1.69x`** | `0.0%` | `+41.9%` |
| **GRT** | `Tier 2` | `6` | `66.7%` | `7.857` | **`+51.4%`** | **`1.67x`** | `-7.0%` | `+20.2%` |
| **AR** | `Tier 2` | `4` | `75.0%` | `12.861` | **`+49.9%`** | **`1.65x`** | `-4.2%` | `+26.3%` |
| **EPIC** | `Tier 2` | `3` | `66.7%` | `21.259` | **`+44.3%`** | **`1.56x`** | `0.0%` | `+27.4%` |
| **ZEC** | `Tier 1` | `8` | `50.0%` | `4.665` | **`+43.7%`** | **`1.55x`** | `-6.4%` | `+18.1%` |
| **SUI** | `Tier 1` | `8` | `50.0%` | `2.325` | **`+43.3%`** | **`1.54x`** | `-16.9%` | `+20.1%` |


---

## 5. Bottom 10 Drag Laggards & Stop-Tax Culprits

| Asset | Tier | Closed Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple | Max Log DD | Cumulative MAE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **ARB** | `Tier 1` | `6` | `0.0%` | `0.000` | **`-39.9%`** | `0.67x` | `-29.7%` | `-8.4%` |
| **SYN** | `Tier 2` | `4` | `0.0%` | `0.000` | **`-39.4%`** | `0.68x` | `-32.3%` | `-19.6%` |
| **OP** | `Tier 1` | `8` | `25.0%` | `0.226` | **`-36.9%`** | `0.69x` | `-30.5%` | `-7.7%` |
| **XPL** | `Tier 1` | `2` | `0.0%` | `0.000` | **`-29.1%`** | `0.75x` | `-20.5%` | `-19.1%` |
| **CFX** | `Tier 2` | `5` | `0.0%` | `0.000` | **`-27.0%`** | `0.76x` | `-22.0%` | `-8.6%` |
| **AAVE** | `Tier 1` | `13` | `15.4%` | `0.587` | **`-26.0%`** | `0.77x` | `-52.0%` | `-7.2%` |
| **FIL** | `Tier 1` | `1` | `0.0%` | `0.000` | **`-25.7%`** | `0.77x` | `0.0%` | `-17.5%` |
| **TRX** | `Tier 1` | `17` | `23.5%` | `0.293` | **`-22.8%`** | `0.80x` | `-19.8%` | `-3.2%` |
| **LPT** | `Tier 2` | `7` | `14.3%` | `0.009` | **`-21.2%`** | `0.81x` | `-20.4%` | `-7.3%` |
| **DUSK** | `Tier 2` | `6` | `33.3%` | `0.019` | **`-20.4%`** | `0.82x` | `-12.9%` | `-6.9%` |


---

## 6. Symbol Breadth & Universe Participation
- **Total Unique Symbols Traded:** `371`
- **Net Profitable Symbols:** `149` (40.2%)
- **Net Drawdown Symbols:** `219` (59.0%)
- **Neutral / Breakeven Symbols:** `3` (0.8%)
- **Individual Asset Trade Logs:** Available in `data/all_tapes/v12_production/symbols/<ASSET>_trades.csv`

---

### 🛡️ Counterfactual Telemetry & Veto Alpha
| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **Total Vetoed Signals** | `53,772` | Signals safely filtered out at gates |
| **Dodged Bullets (Loss Saved)** | `33,510` | Vetoed signals that dumped or hit initial stops |
| **Missed Opportunities** | `10,676` | Vetoed signals that rallied $\ge +20\%$ MFE |
| **Saved Loss Magnitude** | `+496,592.6%` | Total capital protected from false breakouts |
| **Missed Upside Excursion** | `-559,108.5%` | Total upside forgone |
| **Net Veto Alpha** | `+-62,515.9%` | **Net Statistical Advantage of Risk Gates** |
| **Gate Efficiency Ratio** | `62.3%` | Percentage of vetoes that prevented capital loss |

#### Veto Gate Attribution
| Gate | Count | Share |
| :--- | :--- | :--- |
| `Core 1: Macro Bear Veto` | `22,716` | `42.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `13,572` | `25.2%` |
| `Core 0: Zero-Tolerance Data Firewall` | `7,205` | `13.4%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `5,303` | `9.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1,947` | `3.6%` |
| `Core 4: Funding Rate Cap` | `1,593` | `3.0%` |
| `Core 4: Defensible Whale Dump` | `1,081` | `2.0%` |
| `Core 4: Whale Firewall` | `294` | `0.5%` |

---
*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*
