#!/usr/bin/env bash
# ==============================================================================
# KRONOS V12 MASTER PIPELINE (LINUX / AWS EC2 PRODUCTION)
# Clean 6-Core Universal Multi-Tier Architecture
# ==============================================================================
set -eo pipefail

# 1. Thread-Contention Firewall (Prevents OpenBLAS/NumPy CPU deadlocks)
export OMP_NUM_THREADS="1"
export OPENBLAS_NUM_THREADS="1"
export SCIPY_OPENBLAS64_NUM_THREADS="1"
export MKL_NUM_THREADS="1"
export VECLIB_MAXIMUM_THREADS="1"
export NUMEXPR_NUM_THREADS="1"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# 1b. Single-Run File Lock Firewall (Prevents concurrent manual & timer executions)
LOCK_FILE="/tmp/kronos_v12_hourly.lock"
if command -v flock &>/dev/null; then
    exec 200>"$LOCK_FILE"
    if ! flock -n 200; then
        echo "=================================================================="
        echo "[Notice] Another Kronos V12 pipeline run is currently in progress."
        echo "Exiting cleanly without overlap (Exit code 3)."
        echo "=================================================================="
        exit 3
    fi
fi

# 2. Virtual Environment & Python Executable Detection
if [ -f "$SCRIPT_DIR/.venv/bin/activate" ]; then
    source "$SCRIPT_DIR/.venv/bin/activate"
fi

PYTHON="python"
if ! command -v python &>/dev/null && command -v python3 &>/dev/null; then
    PYTHON="python3"
fi

# 3. Load Environment Variables (.env)
if [ -f ".env" ]; then
    set -a
    source .env
    set +a
fi

export KRONOS_PROFILE="${KRONOS_PROFILE:-book3_flush}"
if [ -z "$KRONOS_TAPE_DIR" ]; then
    if [ "$KRONOS_PROFILE" = "book3_flush" ]; then
        export KRONOS_TAPE_DIR="data/all_tapes/v12_book3_flush_reclaim_arm"
    else
        export KRONOS_TAPE_DIR="data/all_tapes/v12_production"
    fi
fi

echo "=========================================="
echo "   KRONOS V12 MASTER PIPELINE EXECUTION    "
echo "   Clean 6-Core Universal Production Engine"
echo "=========================================="
date -u +"[Timestamp UTC] %Y-%m-%d %H:%M:%SZ"

# 3. Pre-Flight Region & API Connectivity Check
echo ""
echo "[0/6] Running Binance API Pre-Flight Connectivity Check..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 https://fapi.binance.com/fapi/v1/ping || echo "000")

if [ "$HTTP_CODE" = "451" ]; then
    echo "=================================================================="
    echo "CRITICAL ERROR: Binance Futures returned HTTP 451 (Geo-Blocked)!"
    echo "This instance is hosted in a US IP range (e.g. us-east-1 / us-west-2)."
    echo "Binance API strictly forbids US requests."
    echo "Please relaunch this EC2 instance in eu-central-1 (Frankfurt) or ap-northeast-1 (Tokyo)."
    echo "=================================================================="
    exit 1
elif [ "$HTTP_CODE" != "200" ]; then
    echo "Warning: Binance ping returned HTTP $HTTP_CODE (Network latency or temporary hiccup). Continuing..."
else
    echo "Pre-Flight Passed: Binance Futures connectivity confirmed (HTTP 200)."
fi

# 4. PRE-PIPELINE HEALTH CHECKS (Fix #1 Stale Data, #2 Disk Guard, #9 Dependency Integrity)
echo ""
echo "[PRE] Running Production Health Checks (Disk / Stale Data / Dependencies)..."
$PYTHON scripts/health_monitor.py || true   # warnings do not abort; disk CRITICAL exits inside

# 5. Step 1: CCXT & Hyper-Fast REST Ingestion
echo ""
echo "[1/6] Running Live Ingestion & Gap Filling (Atomic & Rate-Limited)..."
$PYTHON config/ingestion/live_bridger.py || echo "[Notice] Bridger finished with non-fatal warnings."

# Sync state file alignment
if [ -f "data/sync_state.json" ]; then
    cp -f data/sync_state.json config/ingestion/sync_state.json || true
fi

# 6. Step 2: Multi-Worker Matrix Backtest & Telemetry
echo ""
echo "[2/6] Executing Clean 6-Core Matrix & Counterfactual Telemetry..."
$PYTHON build_v12_tape.py

# 7. Step 3: Strict Compounding Log Tapes & Precomputed Scorecard
echo ""
echo "[3/6] Exporting Strict Log-Compounding Tapes & Precomputed Scorecard..."
$PYTHON momentum_v12/build_csv.py

# 8. Step 4: Executive Markdown Summaries (v12_tear_tape.md & All Symbol Tear Sheets)
echo ""
echo "[4/6] Generating Institutional Executive Artifacts & All Symbol Tear Sheets..."
$PYTHON momentum_v12/generate_artifacts.py
$PYTHON scripts/generate_symbol_tearsheets.py --all

# 9. Step 5: Offsite S3 Backup (Graceful fallback on local)
echo ""
echo "[5/6] Synchronizing State & Ledgers to AWS S3..."
$PYTHON scripts/backup_to_s3.py

# Fix #7: Validate S3 uploads are non-zero after backup
echo ""
echo "[5b] Validating S3 Upload Integrity (non-zero bytes check)..."
$PYTHON scripts/health_monitor.py --validate-s3 || true

# 10. Step 6: Heartbeat Ping (Dead-Man's Switch)
echo ""
echo "[6/7] Emitting Pipeline Liveness Heartbeat..."
$PYTHON scripts/send_heartbeat.py

# 11. Step 7: AWS SNS Trade Signal Email Alerts (Optional)
echo ""
echo "[7/7] Dispatching Trade Signal Alerts (AWS SNS / Email)..."
$PYTHON scripts/notify_signals_sns.py || echo "[Notice] SNS alert dispatcher completed with non-fatal status."

echo ""
echo "=========================================="
echo "   KRONOS V12 PIPELINE COMPLETE: SUCCESS   "
echo "=========================================="
date -u +"[Completed UTC] %Y-%m-%d %H:%M:%SZ"

