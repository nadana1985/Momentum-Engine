# momentum_engine ?" Perfected CTA Engine

This repository represents the unified, perfected quantitative engine.

## The Mathematical Architecture

1. **Dormant Baseline (Bollinger Band Contraction):** 
   Replaces the old 30-day volume bias. The engine now calculates Bollinger Band Width (BBW) and requires it to be extremely compressed (e.g., < 15th percentile of the trailing year).
2. **Idiosyncratic Alpha:** 
   The asset must outperform Bitcoin on the ignition bar.
3. **Volume Shock (Ignition):** 
   A massive volume anomaly (e.g., > 5.0x the trailing 24h average) is required.
4. **OI Exhaustion Harvester (The Holy Grail):** 
   The engine uses Open Interest (OI) derivatives data and Taker Flow to differentiate between shakeouts and true blow-off tops. If a massive volume wick forms and OI increases, it holds. If OI collapses, it triggers the exit.

## Layout

| Module | Role |
|---|---|
| config.py | Canonical knobs (gates, dormant modes, strictness, outcomes, CTA) |
| eatures.py | Shared causal enrichment (BBW, ATR, Alpha, Shocks) |
| cta.py | The Execution Simulator (runs the OI Harvester and Structural Stops) |
