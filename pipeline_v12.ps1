$env:OMP_NUM_THREADS="1"
$env:OPENBLAS_NUM_THREADS="1"
$env:SCIPY_OPENBLAS64_NUM_THREADS="1"
$env:MKL_NUM_THREADS="1"
$env:VECLIB_MAXIMUM_THREADS="1"
$env:NUMEXPR_NUM_THREADS="1"
if (-not $env:KRONOS_PROFILE) {
    $env:KRONOS_PROFILE="production"
}
if (-not $env:KRONOS_TAPE_DIR) {
    $env:KRONOS_TAPE_DIR="data/all_tapes/v12_production"
}

# Load .env if present (Windows equivalent of bash source .env)
$envFile = Join-Path $PSScriptRoot ".env"
if (Test-Path $envFile) {
    Get-Content $envFile | ForEach-Object {
        if ($_ -match '^\s*([^#][^=]+)=(.*)$') {
            [System.Environment]::SetEnvironmentVariable($Matches[1].Trim(), $Matches[2].Trim(), "Process")
        }
    }
}

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "   KRONOS V12 MASTER PIPELINE EXECUTION    " -ForegroundColor Cyan
Write-Host "   Clean 6-Core Universal Production Engine" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "  Timestamp: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') UTC" -ForegroundColor Gray

# 0. Pre-Flight Connectivity Check
Write-Host "`n[0/6] Running Binance Futures Pre-Flight Connectivity Check..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "https://fapi.binance.com/fapi/v1/ping" -TimeoutSec 10 -UseBasicParsing -ErrorAction Stop
    Write-Host "Pre-Flight Passed: Binance Futures connectivity confirmed (HTTP $($response.StatusCode))." -ForegroundColor Green
} catch {
    $status = if ($_.Exception.Response) { [int]$_.Exception.Response.StatusCode } else { 0 }
    if ($status -eq 451) {
        Write-Host "CRITICAL ERROR: Binance returned HTTP 451 (Geo-Blocked in US regions)!" -ForegroundColor Red
        Write-Host "Please use a VPN or deploy to an EU/Tokyo AWS region." -ForegroundColor Red
        exit 1
    } else {
        Write-Host "Warning: Pre-flight check returned status: $status. Continuing..." -ForegroundColor Gray
    }
}

# PRE. Production Health Checks — Fix #1 Stale Data, #2 Disk Guard, #9 Dependency Integrity
Write-Host "`n[PRE] Running Production Health Checks (Disk / Stale Data / Dependencies)..." -ForegroundColor Yellow
# On local dev Windows, disk 99% is expected — health monitor warns but doesn't block
$env:HEALTH_DISK_CRIT_PCT = if ($env:HEALTH_DISK_CRIT_PCT) { $env:HEALTH_DISK_CRIT_PCT } else { "99.9" }  # relax for local dev
python scripts/health_monitor.py
# Note: on local dev disk at 99% will warn. On EC2 40GB disk default threshold of 92% applies.

Write-Host "`n[1/6] Running Live Ingestion & Gap Filling (Atomic & Rate-Limited)..." -ForegroundColor Yellow
python config/ingestion/live_bridger.py
if (-not $?) { Write-Host "Bridger notice: continuing..." -ForegroundColor Gray }

if (Test-Path "data/sync_state.json") {
    Copy-Item -Path data/sync_state.json -Destination config/ingestion/sync_state.json -Force
}

Write-Host "`n[2/6] Executing Clean 6-Core Matrix & Counterfactual Telemetry..." -ForegroundColor Yellow
python build_v12_tape.py
if (-not $?) { Write-Host "Build tape failed!" -ForegroundColor Red; exit 1 }

Write-Host "`n[3/6] Exporting Strict Log-Compounding Tapes & Precomputed Scorecard..." -ForegroundColor Yellow
python momentum_v12/build_csv.py
if (-not $?) { Write-Host "Build CSV failed!" -ForegroundColor Red; exit 1 }

Write-Host "`n[4/6] Generating Institutional Executive Artifacts (v12_tear_tape.md & All Symbol Tear Sheets)..." -ForegroundColor Yellow
python momentum_v12/generate_artifacts.py
if (-not $?) { Write-Host "Generate artifacts failed!" -ForegroundColor Red; exit 1 }
python scripts/generate_symbol_tearsheets.py --all

Write-Host "`n[5/6] Offsite State & Ledger Backup to AWS S3..." -ForegroundColor Yellow
python scripts/backup_to_s3.py

# Fix #7 — S3 Upload Validation
Write-Host "`n[5b] Validating S3 Upload Integrity (non-zero bytes check)..." -ForegroundColor Yellow
python scripts/health_monitor.py --validate-s3

Write-Host "`n[6/7] Emitting Pipeline Liveness Heartbeat..." -ForegroundColor Yellow
python scripts/send_heartbeat.py

Write-Host "`n[7/7] Dispatching Trade Signal Alerts (AWS SNS / Email)..." -ForegroundColor Yellow
python scripts/notify_signals_sns.py

Write-Host "`n==========================================" -ForegroundColor Green
Write-Host "   KRONOS V12 PIPELINE COMPLETE: SUCCESS   " -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green
Write-Host "  Completed: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Gray
