# Kronos V15.0 Production Pipeline Runner
# Master Execution Script for 652 Liquid Shards
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "       KRONOS V15.0 MASTER UNIFIED PRODUCTION PIPELINE    " -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Cyan

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

# 1. Run Cold Build across 652 shards
Write-Host "`n[1/3] Executing V15.0 Cold Ground-Up Tape Build..." -ForegroundColor Yellow
python v15_standalone/run_v15_0_fresh_build.py

if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] V15.0 build failed with exit code $LASTEXITCODE" -ForegroundColor Red
    exit $LASTEXITCODE
}

# 2. Generate CSV exports & Performance Reports
Write-Host "`n[2/3] Generating V15.0 Performance Artifacts & Metrics..." -ForegroundColor Yellow
python -c "import sys; sys.path.insert(0, 'v15_standalone'); from momentum_v15 import build_csv; build_csv.main()"

# 3. Complete
Write-Host "`n[3/3] V15.0 Pipeline Run Complete! Canonical tape updated at data/canonical/canonical_v15_0_tape.parquet" -ForegroundColor Green
Write-Host "To launch the Interactive Production Dashboard, run: python v15_standalone/momentum_v15/dashboard_nicegui.py" -ForegroundColor Cyan
