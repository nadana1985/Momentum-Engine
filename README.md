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

---

## 🛡️ Production hardening (2026-09-26)

Settings live in `deploy/v10.env` (see `deploy/v10.env.example`).

| Area | Change |
|---|---|
| Data location | `V10_DATA_ROOT` points every module at one data directory (default `<repo>/data`). The job fails closed if it finds fewer than `V10_MIN_SHARDS` (100) raw shards. |
| Crash safety | Every shard, ledger, state and status file is written to a temp file and swapped in with `os.replace`. The engine watermark (`engine_state.json`) is committed **after** the ledgers, so a crash replays the hour instead of losing exits. Orphaned temp files are swept at the start of each run. |
| Overlap | `flock` on `<data>/.hourly.lock`; a second run exits with code 3. |
| Binance pacing | OI/L-S ≤ 3 req/s (limit 1000/5 min), funding ≤ 1.5 req/s (limit 500/5 min), klines at the lowest weight bucket. Funding is fetched only after a new settlement. Metrics and klines paginate to back-fill outages. 418/451 stop all requests for the run. |
| Health gates | The run is marked failed (email subject `FAILED`, exit 1) if fewer than `V10_MIN_FRESH_PCT` (80%) of shards hold the last closed bar, or more than `V10_MAX_FAIL_PCT` (20%) of assets or symbols fail, or Binance blocks the run. |
| Backup | `V10_BACKUP_BUCKET`: ledger and state go to `latest/` every hour and to `daily/<date>/` at 00 UTC (expire with a 35-day lifecycle rule). All shards are mirrored to `data/` once a day. Restore a fresh host with `python -m momentum_v10.ops restore`. |
| Heartbeat | `V10_CW_NAMESPACE`: publishes `HourlyOK`, `OpenTrades`, `IngestFailed`, `AssetsFailed` and `RunSeconds` to CloudWatch. Alarm on missing `HourlyOK` to catch a dead host. |
| Symbols | Shards whose names were mangled to `?` are skipped with a warning. |
| Dependencies | Pinned in `requirements.txt`; dashboard in `requirements-dashboard.txt`; tests in `requirements-dev.txt` (`python -m pytest momentum_v10/tests`). |

Steady-state hourly runtime is dominated by OI/L-S pacing: about 1,720 requests at 3/s is about 10 minutes, and compute is about 1 minute.
Not addressed here: the strategy/execution findings in the Phase 2 audit (same-bar fills, toxic-regime exit price, funding forward-fill from current `premiumIndex`).

### AWS deployment (EC2, eu-west-2)

`deploy/aws/deploy.sh` creates or reuses the following, all tagged `Project=v10-momentum`:
- S3 bucket `v10-momentum-<account>-eu-west-2`
- SNS topic, with email subscriptions
- IAM role, least-privilege, plus SSM access
- security group with no inbound rules
- a `t4g.small` Amazon Linux 2023 instance: IMDSv2, encrypted gp3, termination protection
- a CloudWatch heartbeat alarm

It uploads the code and your `../data` folder, and the instance installs itself on first boot.

```bash
cd deploy/aws
./deploy.sh            # first deploy (asks for confirmation)
./deploy.sh status     # last run status, timer, memory, disk
./deploy.sh logs       # bootstrap log + journal
./deploy.sh update     # ship code changes (waits for a running job)
./deploy.sh run-now    # trigger a run
./deploy.sh destroy    # remove everything except the S3 bucket
```

On the instance:
- code: `/opt/v10_standalone` (read-only)
- venv: `/opt/v10_venv`
- data: `/var/lib/v10/data`
- logs: `/var/log/v10`
- settings: `/etc/v10/v10.env`
- service: `v10-hourly.service` runs as the unprivileged `v10` user under systemd sandboxing.

## Costed, position-sized backtest

`momentum_v10/backtest_costed.py` replays the trade ledger as one account: next-bar-open fills, taker fees, square-root market impact, funding, risk-based sizing with portfolio caps and trimming of winners, daily mark-to-market, plus engine-subset, walk-forward, start-date and sensitivity runs. `momentum_v10/backtest_report.py` renders the results as a single HTML page.

```bash
export V10_DATA_ROOT=../data V10_BT_DIR=../backtest
for i in 0 1 2 3 4 5 6 7; do python -m momentum_v10.backtest_costed extract $i 8; done   # per-trade fills, liquidity, funding
python -m momentum_v10.backtest_costed merge
python -m momentum_v10.backtest_costed report                                               # -> results.json, equity_curves.csv, trades_C.csv
python -m momentum_v10.backtest_report ../backtest ../backtest/findings.json              # -> backtest_report.html
```

## Documentation

- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md): how the hourly run works, the six engines, and which file and function does each job
- [`docs/code-map.html`](docs/code-map.html): the same map with diagrams (download it and open it in a browser)
- [`docs/backtest/backtest-report.html`](docs/backtest/backtest-report.html): the latest costed, position-sized backtest report (see `docs/backtest/findings.json` for its written findings)
