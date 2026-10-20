---
name: adapter_pattern_integration
description: Guidelines for building wrappers (adapters) around legacy codebase features (like data ingestion or liquidity classifiers) to protect their internal rules from AI modification.
---

# Adapter Pattern Integration Skill

This skill enforces boundaries around legacy modules, preventing AI agents from editing, refactoring, or breaking complex pre-existing logic by wrapping them in adapters.

## Core Rules

1. **Isolation of Legacy Modules:**
   * Treat legacy files (`kronos/`, `config/`, etc.) as external third-party libraries. Do not edit their code.
   
2. **Standard Output Mapping:**
   * Every adapter must ingest legacy DataFrame/dict outputs and map them directly to the new `MarketContext` or `AlphaSignal` DTOs.
   
3. **Graceful Degradation:**
   * If a legacy module fails, the adapter must log the error and degrade gracefully (returning clean fallbacks rather than passing internal tracebacks down the clean pipeline).

4. **`InsufficientDataError` Contract:**
   * The ingestion adapter (`kronos_v2/adapters/data_adapter.py`) must raise `InsufficientDataError` if the legacy engine returns a DataFrame with fewer bars than `neural['min_history']`. Do NOT silently pass partial DataFrames downstream.

5. **Scope Adapters to 14 Tier 1 Points Only:**
   * The bridge adapter for override points must cover exactly the 14 currently executed points: `[01, 02, 06, 11, 15, 28, 48, 52, 56, 57, 64, 66, 69, 72]`. Do NOT attempt to bridge all 100 phantom columns. Points 73–100 are 100% NULL in the production database.
