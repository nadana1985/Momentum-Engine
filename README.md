# Kronos V12.9: Production Execution Guide & Architecture Manual

This directory contains the canonical **V12.9 Master Unified Production Architecture** for the Kronos Altcoin Momentum Engine.

---

## 1. Production Architecture Overview (V12.9)

Kronos V12.9 operates an institutional 4-Book multi-strategy execution stack across all 652 liquid perpetual shards, powered by the Continuous Anti-Chase Sizing Multiplier Engine for Book 4 (Study S-BF), Two-Tranche Trajectory Exits (Study S-BE), Book 2 Sub-200d EMA Specialization (Study S-BC), and the Unified Compensatory Squeeze & Momentum Index (CSMI - Study S-BD):

| Book | Name | Methodology | Primary Tiers | Performance Lift |
| :--- | :--- | :--- | :--- | :--- |
| **Book 1** | **Continuation Breakouts** | 21d rolling highs, flagpole clamped $\le 25\%$, Two-Tier target routing (Study S-AY), CSMI continuous sizing | Tier 1 (Macro) & Tier 2 (Mid-Cap) | **+823.4% Net Log** (Log PF 1.995 / PnL PF 2.500) |
| **Book 2** | **Coiled Squeezes** | 72h compression shelves ($\le 25\%$), sub-200d EMA gate, CSMI sizing overlay, -1.5% cushion ratchet | Tier 1, Tier 2, Tier 3 (Micro-Cap) | **+1,436.2% Net Log** (Log PF 2.254 / PnL PF 2.568) |
| **Book 3** | **Bull Flush Absorption** | Passive $-8.0\%$ discount limit bids on bull-regime defensive vetoes, $+8.70\%$ entry reclaim target | Tier 1 (Macro) & Tier 3 (Micro-Cap) | **+2,403.9% Net Log** (Log PF 1.349 / PnL PF 1.480) |
| **Book 4** | **Two-Tranche Reclaim + Anti-Chase Sleeve** | $\ge 30\text{d}$ base below 200d EMA $\to$ touch $\to$ $-10\%$ to $-20\%$ retest dip $\to$ reclaim; Two-Tranche exits; Continuous Anti-Chase Sizing | Universal (Tiers 1, 2, 3) | **+6,539.1% Net Log** (Log PF 6.313 / PnL PF 7.960 / 75.8% WR) |

**Total Production Stack Performance:** **+11,202.6% Cumulative Net Log Return ($4.49 \times 10^{48}\times$ Capital Multiple / 1,952x wealth expansion over V12.8)**, **Log PF 2.110**, **Win Rate 57.97%**, across **3,462 trades (3,443 closed)**.

---

## 2. Quick Start: Running the Master Pipeline

### Prerequisites
- Python 3.11+ with packages installed (`pip install -r requirements.txt`).
- Network access to Binance Futures API (`https://fapi.binance.com`). *Note: US IP addresses receive HTTP 451 geo-blocks and require a VPN or EU/Tokyo proxy/instance.*

### Running via PowerShell (`pipeline_v12.ps1`)
Because the pipeline uses relative paths for internal modules, shards, and scripts, **you must execute it with the current directory set to `v12_standalone`**:

```powershell
# 1. Navigate to the v12_standalone directory
cd f:\kronos_v1_alt\v12_standalone

# 2. Permit script execution for the current session (if restricted)
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# 3. Launch the master pipeline
.\pipeline_v12.ps1
```

Or execute directly in a single one-liner from any terminal:
```powershell
powershell.exe -ExecutionPolicy Bypass -Command "cd f:\kronos_v1_alt\v12_standalone; .\pipeline_v12.ps1"
```

### Running on Linux / Bash (`pipeline_v12.sh`)
```bash
cd /path/to/kronos_v1_alt/v12_standalone
chmod +x pipeline_v12.sh
./pipeline_v12.sh
```

---

## 3. End-to-End Pipeline Stages

The pipeline script automates the full operational sequence:

| Stage | Step Name | Executable / Script | Description |
| :---: | :--- | :--- | :--- |
| **0** | **Pre-Flight Firewall** | `Invoke-WebRequest` | Pings Binance Futures API (`/fapi/v1/ping`). Halts immediately if blocked (HTTP 451). |
| **PRE** | **Production Health Checks** | `scripts/health_monitor.py` | Validates disk space, data freshness, and package dependency integrity. |
| **1/6** | **Live Ingestion & Gap Filling** | `config/ingestion/live_bridger.py` | Syncs latest 1h OHLCV and derivative funding/OI data via CCXT with HTTP connection pooling. |
| **2/6** | **Clean Matrix Execution** | `build_v12_tape.py` | Executes the 4-Book production engine across all 652 liquid shards with single-thread CPU isolation. |
| **3/6** | **Strict Compounding Tapes** | `momentum_v12/build_csv.py` | Exports canonical trade ledgers (`trades.parquet`, `closed_trades.csv`, `open_trades.csv`, and scorecards). |
| **4/6** | **Institutional Artifacts** | `momentum_v12/generate_artifacts.py`<br>`scripts/generate_symbol_tearsheets.py --all` | Generates `v12_tear_tape.md`, open trade summaries, and asset-specific tear sheets. |
| **5/6** | **Cloud S3 Backup** | `scripts/backup_to_s3.py` | Uploads trade tapes and state snapshots to AWS S3 (graceful localhost bypass if unconfigured). |
| **5b** | **S3 Upload Validation** | `scripts/health_monitor.py --validate-s3` | Confirms non-zero payload bytes in cloud storage. |
| **6/7** | **Liveness Heartbeat** | `scripts/send_heartbeat.py` | Pings Dead-Man's Switch (`HEARTBEAT_URL` / CloudWatch). |
| **7/7** | **Trade Alerts** | `scripts/notify_signals_sns.py` | Dispatches new trade signal notifications via AWS SNS / Email. |

---

## 4. Launching the Live Command Center (Dashboard)

To inspect active positions, execution statistics, counterfactual telemetry, and individual symbol tear sheets in the web UI:

```powershell
cd f:\kronos_v1_alt\v12_standalone
python momentum_v12/dashboard_nicegui.py
```

Access locally in your browser at **`http://localhost:8056`**.

---

## 5. Key Configuration & Environment Variables

Copy `.env.example` to `.env` to customize settings:
```env
# Execution Profile (production, no_book4, legacy_3_books, baseline_no_book3)
KRONOS_PROFILE=production
KRONOS_TAPE_DIR=data/all_tapes/v14_production
# paper (default): fill Book 3/5 limits at the bid when the bar low trades through.
# live | live_limit: gap-through fills at the open; rebase Book 3 stop from the fill.
# This is a fill model, not an exchange order placer. Book 4 stays market-on-close.
KRONOS_EXECUTION=paper

# Cloud Backups & Dead-Man's Switch
AWS_DEFAULT_REGION=eu-central-1
S3_BUCKET=your-s3-bucket-name
HEARTBEAT_URL=https://hc-ping.com/your-uuid

# Alerts
SNS_TOPIC_ARN=arn:aws:sns:eu-central-1:123456789012:kronos-signals
NOTIFY_ONLY_ON_NEW_SIGNALS=1

# NiceGUI Dashboard Port
NICEGUI_HOST=0.0.0.0
NICEGUI_PORT=8056
```

---

## 6. Troubleshooting & Safety Guardrails

- **CPU Deadlocks / OpenBLAS Contention:** `pipeline_v12.ps1` automatically enforces `OMP_NUM_THREADS=1`, `OPENBLAS_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, etc. Never run Python matrix workers without these thread clamps.
- **PowerShell `UnauthorizedAccess`:** Run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` before running `.ps1` scripts.
- **Binance HTTP 451 Geo-Block:** If running in a US region, the pre-flight check will stop the pipeline. Use a non-US proxy or deploy to an EU/Tokyo AWS instance.
- **Disk Space Warning:** On local development drives >80% capacity, `health_monitor.py` logs a warning but proceeds normally.

---

## 7. AWS Deployment & Upgrading: Mandatory State Flush Guide

When deploying or upgrading an existing EC2 instance to **V12.7**:
> [!IMPORTANT]
> Because V12.7 introduced Book 2 Sub-200d EMA specialization (purging 299 drag trades) and continuous CSMI log-odds sizing, **you must safely archive and flush old runtime files** (`data/all_tapes/`, `data/v12_live_state.json`, and `telemetry/`) before launching the new engine.
>
> **DO NOT delete `data/raw_shards/` or `data/exotic_shards/`** (historical market data).

Run this on your AWS EC2 instance:
```bash
cd /home/ubuntu/kronos_v12

# 1. Stop hourly timer during upgrade
sudo systemctl stop kronos-v12.timer

# 2. Archive old runtime files safely (preserves raw_shards intact!)
BACKUP_DIR="data/archive_pre_v12_7_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"
mv data/all_tapes data/v12_live_state.json telemetry reports/symbols "$BACKUP_DIR/" 2>/dev/null || true
rm -f v12_tear_tape.md v12_open_trades.md

# 3. Bootstrap clean V12.7 canonical state (takes ~20-25 min once on EC2)
KRONOS_FULL_REBUILD=1 ./pipeline_v12.sh

# 4. Resume the hourly pipeline timer
sudo systemctl start kronos-v12.timer
```
For the full cloud provisioning guide, see [AWS_EC2_DEPLOYMENT_RUNBOOK.md](AWS_EC2_DEPLOYMENT_RUNBOOK.md).
