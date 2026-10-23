"""
Verification Test for Kronos V15.2 Quant Workstation Integration
"""

import sys
import os
import time
import urllib.request
import json
from pathlib import Path

# Add standalone path
sys.path.insert(0, os.path.abspath('v15_standalone'))

from momentum_v15.workstation_bridge import (
    build_workstation_payload,
    get_available_workstation_symbols,
)

def run_tests():
    print("=" * 70)
    print("STEP 1: Testing Symbol Discovery")
    symbols = get_available_workstation_symbols()
    print(f"Total available symbols: {len(symbols)}")
    assert len(symbols) >= 600, f"Expected >= 600 symbols, got {len(symbols)}"
    jct_match = [s for s in symbols if s['symbol'] == 'JCT']
    assert len(jct_match) > 0, "JCT not found in symbols"
    print(f"JCT found: {jct_match[0]}")

    print("\nSTEP 2: Testing Payload Serializer for JCT")
    t0 = time.time()
    payload = build_workstation_payload('JCT', lookback_bars=500)
    elapsed = time.time() - t0
    print(f"Payload built in {elapsed:.3f}s")
    assert 'candles' in payload and len(payload['candles']) == 500
    assert 'volume' in payload and len(payload['volume']) == 500
    assert 'open_interest' in payload and len(payload['open_interest']) == 500
    assert 'toptrader_ls' in payload and len(payload['toptrader_ls']) == 500
    assert 'funding_rate' in payload and len(payload['funding_rate']) == 500
    assert 'donchian_floor' in payload
    assert 'compression_shelf' in payload
    assert 'resting_stop' in payload
    assert 'markers' in payload
    assert 'events' in payload
    assert 'inspection_index' in payload
    assert 'summary' in payload
    print(f"Markers count: {len(payload['markers'])}, Events count: {len(payload['events'])}")

    print("\nSTEP 3: Testing Payload Serializer for MAGIC")
    t0 = time.time()
    magic_payload = build_workstation_payload('MAGIC', lookback_bars=500)
    elapsed = time.time() - t0
    print(f"MAGIC payload built in {elapsed:.3f}s, candles: {len(magic_payload['candles'])}")
    assert len(magic_payload['candles']) == 500

    print("\nSTEP 4: Testing Static Files On Disk")
    js_lib = Path('v15_standalone/momentum_v15/static/js/lightweight-charts.standalone.production.js')
    assert js_lib.exists() and js_lib.stat().st_size > 100000, "Lightweight charts JS missing or too small"
    print(f"Vendor JS: {js_lib.stat().st_size:,} bytes - OK")

    js_wk = Path('v15_standalone/momentum_v15/static/js/quant_workstation.js')
    assert js_wk.exists() and js_wk.stat().st_size > 5000, "quant_workstation.js missing or too small"
    print(f"Workstation JS: {js_wk.stat().st_size:,} bytes - OK")

    css_wk = Path('v15_standalone/momentum_v15/static/css/workstation.css')
    assert css_wk.exists() and css_wk.stat().st_size > 2000, "workstation.css missing or too small"
    print(f"Workstation CSS: {css_wk.stat().st_size:,} bytes - OK")

    print("\nALL VERIFICATION TESTS PASSED SUCCESSFULLY!")
    print("=" * 70)

if __name__ == '__main__':
    run_tests()
