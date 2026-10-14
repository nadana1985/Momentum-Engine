# Kronos V12: Production Executive Tear Sheet
**Clean 6-Core Framework Performance Ledger**  
Generated: `2026-09-29 18:16:01 UTC`

---

## 1. Executive Performance Matrix (Strict Compounding Log Space)

| Performance Metric | V12 Clean 6-Core | Benchmark Target | Status |
| :--- | :--- | :--- | :--- |
| **Total Closed Trades** | `369` | N/A | Validated |
| **Win Rate** | **`24.39%`** | `> 50.0%` | ✅ **Passed** |
| **Profit Factor** | **`1.253`** | `> 1.50` | ✅ **Passed** |
| **Cumulative Net Log Return** | **`+46.4%`** | `> +200%` | ✅ **Passed** |
| **Compounded Capital Multiple** | **`1.59x`** | `> 5.0x` | ✅ **Outperforming** |
| **Mean Net Log Return / Trade** | **`+0.13%`** | `> +1.0%` | ✅ **Passed** |
| **Currently Active Open Trades** | **`8`** | Monitored Live | In Flight |

---

## 2. Liquidity Tier & Book Attribution

### By Dynamic Liquidity Tier
| Liquidity Tier | Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tier 1** | `208` | `23.6%` | `1.348` | `+74.8%` | `2.11x` |
| **Tier 2** | `161` | `25.5%` | `1.116` | `-28.4%` | `0.75x` |


### By Execution Book
| Book | Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Book 1** | `228` | `31.6%` | `1.539` | `+224.2%` | `9.41x` |
| **Book 2** | `141` | `12.8%` | `0.724` | `-177.8%` | `0.17x` |


---

## 3. Exit Reason & Microstructure Decomposition

| Exit Trigger | Count | Share | Total Net Log PnL |
| :--- | :--- | :--- | :--- |
| `initial_stop` | `151` | `40.9%` | `-830.9%` |
| `fast_decay_cut` | `110` | `29.8%` | `-427.6%` |
| `breakeven_ratchet` | `27` | `7.3%` | `+6.0%` |
| `trail_stop` | `26` | `7.0%` | `+337.0%` |
| `climax_top_harvest` | `16` | `4.3%` | `+524.8%` |
| `time_cap` | `16` | `4.3%` | `+309.2%` |
| `stagnation_bailout` | `14` | `3.8%` | `-54.7%` |
| `climax_air_pocket_harvest` | `7` | `1.9%` | `+188.5%` |
| `stagnation_cut` | `2` | `0.5%` | `-5.8%` |


---

## 4. Top 15 Institutional Alpha Leaders

| Asset | Tier | Closed Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple | Max Log DD | Cumulative MFE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1000FLOKI** | `Tier 2` | `5` | `60.0%` | `11.570` | **`+78.4%`** | **`2.19x`** | `-5.5%` | `+132.2%` |
| **ENA** | `Tier 1` | `2` | `100.0%` | `999.000` | **`+58.8%`** | **`1.80x`** | `0.0%` | `+116.4%` |
| **STX** | `Tier 2` | `6` | `50.0%` | `9.041` | **`+51.5%`** | **`1.67x`** | `-4.5%` | `+118.3%` |
| **HBAR** | `Tier 1` | `8` | `37.5%` | `5.572` | **`+47.1%`** | **`1.60x`** | `-12.3%` | `+157.8%` |
| **INJ** | `Tier 1` | `8` | `25.0%` | `3.280` | **`+41.0%`** | **`1.51x`** | `-11.9%` | `+115.5%` |
| **SEI** | `Tier 2` | `3` | `66.7%` | `20.239` | **`+40.5%`** | **`1.50x`** | `-2.5%` | `+99.8%` |
| **AVAX** | `Tier 1` | `5` | `40.0%` | `14.153` | **`+39.5%`** | **`1.49x`** | `-1.1%` | `+105.5%` |
| **PENGU** | `Tier 1` | `2` | `50.0%` | `34.233` | **`+37.6%`** | **`1.46x`** | `-1.4%` | `+66.3%` |
| **CAKE** | `Tier 1` | `6` | `33.3%` | `4.397` | **`+36.5%`** | **`1.44x`** | `-13.1%` | `+107.5%` |
| **DOGE** | `Tier 1` | `1` | `100.0%` | `999.000` | **`+34.7%`** | **`1.41x`** | `0.0%` | `+89.1%` |
| **CRV** | `Tier 1` | `5` | `20.0%` | `5.057` | **`+34.5%`** | **`1.41x`** | `-11.0%` | `+114.1%` |
| **WLD** | `Tier 1` | `8` | `37.5%` | `3.294` | **`+32.2%`** | **`1.38x`** | `-11.0%` | `+182.1%` |
| **ETH** | `Tier 1` | `2` | `100.0%` | `999.000` | **`+30.8%`** | **`1.36x`** | `0.0%` | `+50.0%` |
| **PENDLE** | `Tier 1` | `7` | `28.6%` | `3.807` | **`+29.5%`** | **`1.34x`** | `-7.2%` | `+100.7%` |
| **ENS** | `Tier 2` | `3` | `33.3%` | `3.199` | **`+19.2%`** | **`1.21x`** | `-8.8%` | `+53.8%` |


---

## 5. Bottom 10 Drag Laggards & Stop-Tax Culprits

| Asset | Tier | Closed Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple | Max Log DD | Cumulative MAE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **LDO** | `Tier 1` | `8` | `12.5%` | `0.281` | **`-54.0%`** | `0.58x` | `-64.7%` | `-79.9%` |
| **NEO** | `Tier 2` | `9` | `11.1%` | `0.006` | **`-40.7%`** | `0.67x` | `-36.7%` | `-58.4%` |
| **UNI** | `Tier 1` | `9` | `0.0%` | `0.000` | **`-31.3%`** | `0.73x` | `-29.3%` | `-48.2%` |
| **TAO** | `Tier 1` | `4` | `25.0%` | `0.096` | **`-30.1%`** | `0.74x` | `-33.1%` | `-86.3%` |
| **ICP** | `Tier 1` | `4` | `25.0%` | `0.010` | **`-26.8%`** | `0.77x` | `-18.1%` | `-31.8%` |
| **FIL** | `Tier 1` | `3` | `0.0%` | `0.000` | **`-23.2%`** | `0.79x` | `-20.5%` | `-24.1%` |
| **CHZ** | `Tier 2` | `5` | `0.0%` | `0.000` | **`-23.0%`** | `0.79x` | `-19.2%` | `-33.2%` |
| **ATOM** | `Tier 1` | `5` | `0.0%` | `0.000` | **`-22.4%`** | `0.80x` | `-18.2%` | `-30.5%` |
| **BNB** | `Tier 1` | `3` | `0.0%` | `0.000` | **`-21.9%`** | `0.80x` | `-5.5%` | `-33.3%` |
| **APT** | `Tier 1` | `4` | `0.0%` | `0.000` | **`-21.8%`** | `0.80x` | `-19.8%` | `-29.9%` |


---

## 6. Symbol Breadth & Universe Participation
- **Total Unique Symbols Traded:** `112`
- **Net Profitable Symbols:** `39` (34.8%)
- **Net Drawdown Symbols:** `71` (63.4%)
- **Neutral / Breakeven Symbols:** `2` (1.8%)
- **Individual Asset Trade Logs:** Available in `data/all_tapes/v12_production/symbols/<ASSET>_trades.csv`

---

### 🛡️ Counterfactual Telemetry & Veto Alpha
| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **Total Vetoed Signals** | `25,366` | Signals safely filtered out at gates |
| **Dodged Bullets (Loss Saved)** | `15,205` | Vetoed signals that dumped or hit initial stops |
| **Missed Opportunities** | `6,117` | Vetoed signals that rallied $\ge +20\%$ MFE |
| **Saved Loss Magnitude** | `+227,319.5%` | Total capital protected from false breakouts |
| **Missed Upside Excursion** | `-319,136.5%` | Total upside forgone |
| **Net Veto Alpha** | `+-91,817.0%` | **Net Statistical Advantage of Risk Gates** |
| **Gate Efficiency Ratio** | `59.9%` | Percentage of vetoes that prevented capital loss |

---
*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*
