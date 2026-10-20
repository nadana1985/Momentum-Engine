---
name: counterfactual_telemetry_collector
description: Guidelines for building the logging, telemetry, and retrospective tracking layers to measure opportunity cost of vetoes and calculate Veto Alpha.
---

# Counterfactual Telemetry Collector Skill

This skill guides the agent in building the "flight recorder" telemetry to audit the Risk Gate's decision efficiency.

## Core Rules

1. **No Silent Drops:**
   * Every trade signal, whether executed, scaled down, or vetoed, must be logged with a status tag (`status="ACTIVE"` vs `status="VETOED"`).
   
2. **Retrospective Enrichment:**
   * Telemetry must support loading past vetoed signals and enriching them with forward returns (e.g. 24h asset return post-signal) to evaluate what would have happened.
   
3. **Veto Alpha Calculation:**
   * Provide built-in methods to compute Veto Alpha ($\text{Sharpe}_{\text{actual}} - \text{Sharpe}_{\text{counterfactual}}$) to statically validate the risk gate thresholds.

4. **Telemetry Path Isolation (Critical safety constraint):**
   * The `TelemetryCollector` must write logs to `kronos_v2/telemetry/`. Do NOT write logs to the legacy `signatures/` folder. Writing telemetry records to the signatures folder will trigger file-collision false positives in the legacy miner's shard worker resumption check (`if os.path.exists(sig_path): return {"status": "skipped"}`), causing the system to silently skip mining runs.

5. **Historical Price Source (Veto Alpha Calculations):**
   * Retrieve retrospectively evaluated price data directly from `label_forward_return_24h` and `label_forward_return_48h` columns in the historical parquet database (`ETH_USDT_historical_stream.parquet`). Do not build a live network price feed for calculating retroactive return metrics.
