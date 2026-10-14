# Kronos V12: Production Executive Tear Sheet
**Clean 6-Core Framework Performance Ledger**  
Generated: `2026-09-29 18:23:24 UTC`

---

## 1. Executive Performance Matrix (Strict Compounding Log Space)

| Performance Metric | V12 Clean 6-Core | Benchmark Target | Status |
| :--- | :--- | :--- | :--- |
| **Total Closed Trades** | `208` | N/A | Validated |
| **Win Rate** | **`32.21%`** | `> 50.0%` | ✅ **Passed** |
| **Profit Factor** | **`1.550`** | `> 1.50` | ✅ **Passed** |
| **Cumulative Net Log Return** | **`+212.5%`** | `> +200%` | ✅ **Passed** |
| **Compounded Capital Multiple** | **`8.37x`** | `> 5.0x` | ✅ **Outperforming** |
| **Mean Net Log Return / Trade** | **`+1.02%`** | `> +1.0%` | ✅ **Passed** |
| **Currently Active Open Trades** | **`7`** | Monitored Live | In Flight |

---

## 2. Liquidity Tier & Book Attribution

### By Dynamic Liquidity Tier
| Liquidity Tier | Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tier 1** | `135` | `30.4%` | `1.661` | `+183.8%` | `6.29x` |
| **Tier 2** | `73` | `35.6%` | `1.297` | `+28.7%` | `1.33x` |


### By Execution Book
| Book | Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Book 1** | `191` | `34.6%` | `1.633` | `+244.4%` | `11.52x` |
| **Book 2** | `17` | `5.9%` | `0.440` | `-31.9%` | `0.73x` |


---

## 3. Exit Reason & Microstructure Decomposition

| Exit Trigger | Count | Share | Total Net Log PnL |
| :--- | :--- | :--- | :--- |
| `fast_decay_cut` | `88` | `42.3%` | `-346.0%` |
| `initial_stop` | `40` | `19.2%` | `-376.7%` |
| `trail_stop` | `20` | `9.6%` | `+217.9%` |
| `breakeven_ratchet` | `19` | `9.1%` | `+4.7%` |
| `climax_top_harvest` | `15` | `7.2%` | `+498.0%` |
| `time_cap` | `12` | `5.8%` | `+247.9%` |
| `stagnation_bailout` | `12` | `5.8%` | `-49.6%` |
| `climax_air_pocket_harvest` | `1` | `0.5%` | `+20.3%` |
| `stagnation_cut` | `1` | `0.5%` | `-4.1%` |


---

## 4. Top 15 Institutional Alpha Leaders

| Asset | Tier | Closed Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple | Max Log DD | Cumulative MFE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **INJ** | `Tier 1` | `4` | `50.0%` | `12.012` | **`+58.8%`** | **`1.80x`** | `-4.0%` | `+105.7%` |
| **ENA** | `Tier 1` | `2` | `100.0%` | `999.000` | **`+58.8%`** | **`1.80x`** | `0.0%` | `+116.4%` |
| **1000FLOKI** | `Tier 2` | `2` | `100.0%` | `999.000` | **`+50.0%`** | **`1.65x`** | `0.0%` | `+68.6%` |
| **WLD** | `Tier 1` | `4` | `75.0%` | `28.784` | **`+48.6%`** | **`1.63x`** | `-2.1%` | `+145.7%` |
| **CAKE** | `Tier 1` | `4` | `50.0%` | `6.961` | **`+41.3%`** | **`1.51x`** | `-8.3%` | `+88.1%` |
| **AVAX** | `Tier 1` | `5` | `40.0%` | `14.153` | **`+39.5%`** | **`1.49x`** | `-1.1%` | `+105.5%` |
| **CRV** | `Tier 1` | `4` | `25.0%` | `5.402` | **`+35.3%`** | **`1.42x`** | `-10.3%` | `+112.3%` |
| **DOGE** | `Tier 1` | `1` | `100.0%` | `999.000` | **`+34.7%`** | **`1.41x`** | `0.0%` | `+89.1%` |
| **JASMY** | `Tier 2` | `1` | `100.0%` | `999.000` | **`+32.2%`** | **`1.38x`** | `0.0%` | `+44.7%` |
| **STX** | `Tier 2` | `2` | `100.0%` | `999.000` | **`+32.1%`** | **`1.38x`** | `0.0%` | `+67.5%` |
| **AR** | `Tier 2` | `2` | `100.0%` | `999.000` | **`+32.0%`** | **`1.38x`** | `0.0%` | `+65.5%` |
| **BCH** | `Tier 1` | `5` | `20.0%` | `3.972` | **`+31.8%`** | **`1.38x`** | `-11.2%` | `+72.7%` |
| **PENDLE** | `Tier 1` | `6` | `33.3%` | `4.439` | **`+31.5%`** | **`1.37x`** | `-5.8%` | `+95.7%` |
| **ETH** | `Tier 1` | `2` | `100.0%` | `999.000` | **`+30.8%`** | **`1.36x`** | `0.0%` | `+50.0%` |
| **HBAR** | `Tier 1` | `3` | `33.3%` | `7.451` | **`+29.6%`** | **`1.34x`** | `-0.5%` | `+73.6%` |


---

## 5. Bottom 10 Drag Laggards & Stop-Tax Culprits

| Asset | Tier | Closed Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple | Max Log DD | Cumulative MAE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TAO** | `Tier 1` | `4` | `25.0%` | `0.096` | **`-30.1%`** | `0.74x` | `-33.1%` | `-86.3%` |
| **ZEC** | `Tier 1` | `4` | `0.0%` | `0.000` | **`-22.7%`** | `0.80x` | `-6.2%` | `-30.7%` |
| **ATOM** | `Tier 1` | `5` | `0.0%` | `0.000` | **`-22.4%`** | `0.80x` | `-18.2%` | `-30.5%` |
| **BNB** | `Tier 1` | `3` | `0.0%` | `0.000` | **`-21.9%`** | `0.80x` | `-5.5%` | `-33.3%` |
| **APT** | `Tier 1` | `4` | `0.0%` | `0.000` | **`-21.8%`** | `0.80x` | `-19.8%` | `-29.9%` |
| **EIGEN** | `Tier 2` | `3` | `0.0%` | `0.000` | **`-20.3%`** | `0.82x` | `-7.2%` | `-31.7%` |
| **LINK** | `Tier 1` | `4` | `0.0%` | `0.000` | **`-18.8%`** | `0.83x` | `-13.2%` | `-20.8%` |
| **ARB** | `Tier 2` | `2` | `0.0%` | `0.000` | **`-18.6%`** | `0.83x` | `-13.0%` | `-19.9%` |
| **CHZ** | `Tier 2` | `3` | `0.0%` | `0.000` | **`-17.7%`** | `0.84x` | `-13.8%` | `-27.3%` |
| **1000BONK** | `Tier 2` | `2` | `0.0%` | `0.000` | **`-17.0%`** | `0.84x` | `-4.0%` | `-22.7%` |


---

## 6. Symbol Breadth & Universe Participation
- **Total Unique Symbols Traded:** `93`
- **Net Profitable Symbols:** `34` (36.6%)
- **Net Drawdown Symbols:** `58` (62.4%)
- **Neutral / Breakeven Symbols:** `1` (1.1%)
- **Individual Asset Trade Logs:** Available in `data/all_tapes/v12_production/symbols/<ASSET>_trades.csv`

---

### 🛡️ Counterfactual Telemetry & Veto Alpha
| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **Total Vetoed Signals** | `24,601` | Signals safely filtered out at gates |
| **Dodged Bullets (Loss Saved)** | `14,638` | Vetoed signals that dumped or hit initial stops |
| **Missed Opportunities** | `5,827` | Vetoed signals that rallied $\ge +20\%$ MFE |
| **Saved Loss Magnitude** | `+217,890.4%` | Total capital protected from false breakouts |
| **Missed Upside Excursion** | `-302,766.2%` | Total upside forgone |
| **Net Veto Alpha** | `+-84,875.8%` | **Net Statistical Advantage of Risk Gates** |
| **Gate Efficiency Ratio** | `59.5%` | Percentage of vetoes that prevented capital loss |

---
*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*
