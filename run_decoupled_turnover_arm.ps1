$env:OMP_NUM_THREADS="1"
$env:OPENBLAS_NUM_THREADS="1"
$env:SCIPY_OPENBLAS64_NUM_THREADS="1"
$env:MKL_NUM_THREADS="1"
$env:VECLIB_MAXIMUM_THREADS="1"
$env:NUMEXPR_NUM_THREADS="1"
$env:KRONOS_TAPE_DIR="data/all_tapes/v12_decoupled_turnover_arm"

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host " KRONOS V12: DECOUPLED TURNOVER MATRIX    " -ForegroundColor Cyan
Write-Host " Book 1: <= 15.0x | Book 2: <= 5.0x       " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

Write-Host "`n[1/3] Executing Matrix with Decoupled Turnover Architecture..." -ForegroundColor Yellow
python build_v12_tape.py
if (-not $?) { Write-Host "Build tape failed!" -ForegroundColor Red; exit 1 }

Write-Host "`n[2/3] Exporting Strict Log-Compounding Tapes & Precomputed Scorecard..." -ForegroundColor Yellow
python momentum_v12/build_csv.py
if (-not $?) { Write-Host "Build CSV failed!" -ForegroundColor Red; exit 1 }

Write-Host "`n[3/3] Generating Institutional Executive Artifacts..." -ForegroundColor Yellow
python momentum_v12/generate_artifacts.py
if (-not $?) { Write-Host "Generate artifacts failed!" -ForegroundColor Red; exit 1 }

Write-Host "`n==========================================" -ForegroundColor Green
Write-Host " SIMULATION COMPLETE: SUCCESS             " -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green
