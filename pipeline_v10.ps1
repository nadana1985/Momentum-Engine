$env:OMP_NUM_THREADS="1"
$env:OPENBLAS_NUM_THREADS="1"
$env:MKL_NUM_THREADS="1"
$env:VECLIB_MAXIMUM_THREADS="1"
$env:NUMEXPR_NUM_THREADS="1"

# Research rebuild plus the live book. Hourly production remains:
#   python -m momentum_v10.hourly_job
# Step 2 persists engine_state.json, the CSV ledgers, trades.parquet, and scorecard.parquet.
# Per-symbol Markdown tear sheets are not written. One sheet:
#   python -m momentum_v10.book_store ASSET
Write-Host "=========================================="
Write-Host "   KRONOS V10 RESEARCH PIPELINE            "
Write-Host "=========================================="

Write-Host "`n[1/5] Running Live Ingestion & Gap Filling..."
python config/ingestion/live_bridger.py
if (-not $?) { Write-Host "Bridger notice: continuing..." }

Write-Host "`n[2/5] Saving the live book through the last closed hour..."
python -m momentum_v10.live_runner
if (-not $?) { Write-Host "Live runner failed!"; exit 1 }

Write-Host "`n[3/5] Executing Master V10 Matrix Backtest (master_raw_tape.csv only)..."
python build_v10_tape.py
if (-not $?) { Write-Host "Build tape failed!"; exit 1 }

Write-Host "`n[4/5] Building Dashboard CSV Tapes..."
python -m momentum_v10.build_csv
if (-not $?) { Write-Host "Build CSV failed!"; exit 1 }

Write-Host "`n[5/5] Generating Summary Markdown Artifacts..."
python momentum_v10/generate_artifact.py
python momentum_v10/build_open_artifact.py
if (-not $?) { Write-Host "Generate artifact failed!"; exit 1 }

Write-Host "`n=========================================="
Write-Host "   V10 PIPELINE COMPLETE   "
Write-Host "=========================================="
