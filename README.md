# Kronos V10 Altcoin Momentum Engine — Standalone Package

This directory contains the **fully isolated V10 Momentum Engine**, including source code, ingestion bridge, master backtest matrix, institutional tear-sheet generator, pure Python NiceGUI dashboard, and all production data tapes.

---

## 📁 Package Structure

```
v10_standalone/
├── momentum_v10/                 # Core V10 Engine & Analytics Modules
│   ├── cta_dual.py               # V10 Dual Engine Kernel & Hill Estimator
│   ├── config.py                 # FeatureConfig & CtaConfig parameters
│   ├── features.py               # Dynamic context & causal feature enrichment
│   ├── build_csv.py              # CSV Tape splitter (open, closed, all)
│   ├── universe_generator.py     # On-demand tear-sheet math (not a batch writer)
│   ├── generate_artifact.py      # Summary artifact builder
│   ├── build_open_artifact.py   # Open trades summary artifact
│   └── dashboard_nicegui.py      # Pure Python NiceGUI Dashboard UI
├── config/ingestion/             # Live Data Ingestion Layer
│   ├── live_bridger.py           # REST API live kline & exotic metrics gap filler
│   └── sync_state_manager.py     # Timestamp cache state manager
├── build_v10_tape.py             # Master Matrix backtest execution script
├── pipeline_v10.ps1              # Master pipeline orchestrator script
├── requirements.txt              # Required Python dependencies
├── README.md                     # Package documentation
└── data/                         # Isolated Data Layer
    ├── raw_shards/               # 725 OHLCV 1-hour parquet kline shards
    ├── exotic_shards/            # Funding rate, Open Interest, L/S ratio parquet shards
    └── all_tapes/v10_production/ # Production output CSVs & 725 markdown tear sheets
```

---

## 🚀 How to Run

### 1. Hourly production (ingest, compute, email)
From this directory, on a schedule (see `deploy/v10-hourly.timer`):
```bash
python -m momentum_v10.hourly_job
```
Set `V10_SES_FROM`, `V10_ALERT_TO`, and `AWS_DEFAULT_REGION` (see `deploy/v10.env.example`). The job gap-fills shards in this repo, runs the live book, and emails open-trade and closed-trade counts. It does not run the websocket daemon.

### 2. Research rebuild (does not replace the live ledger)
```powershell
.\pipeline_v10.ps1
```
`build_v10_tape.py` writes `master_raw_tape.csv` only. `build_csv.py` refreshes `all_trades.csv` from the live open and closed files and does not rewrite them.

### 3. Launch NiceGUI Web Dashboard
To start the live dashboard UI on `http://localhost:8055`:
```bash
python momentum_v10/dashboard_nicegui.py
```

---

## 📊 Outputs & Tapes
* **Active Open Positions**: `data/all_tapes/v10_production/open_trades.csv`
* **Closed Book Ledger**: `data/all_tapes/v10_production/closed_trades.csv`
* **Full Portfolio Execution**: `data/all_tapes/v10_production/all_trades.csv`
* **Raw Master Tape** (research replay, not the live ledger): `data/all_tapes/v10_production/master_raw_tape.csv`
* **Hourly status**: `data/all_tapes/v10_production/hourly_status.json`
* **Trade book**: `data/all_tapes/v10_production/trades.parquet` (one row per trade)
* **Scorecard**: `data/all_tapes/v10_production/scorecard.parquet` (one row per symbol)
* **One tear sheet, on request**: `python -m momentum_v10.book_store ASSET`
