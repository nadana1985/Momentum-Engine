# Version 10.2 (frozen closed-book)
"""momentum_v10 — unified drift-free ignition + CTA tooling.

V10.2 freeze: lottery scanner. Take every CONTINUATION, Donchian the
winners (21d floor, arm MFE>=0.50, CLOSE trigger, CONTINUATION only),
eat the ~-6% structural-stop tax. No rise-veto, no early-path flatten,
no Donchian on IGNITION/PHOENIX. Score closed trades only (no open_at_end).

Consumers: scan.py, tape.py, cta.py, cta_dual.py, live_runner.py.
Canonical knobs: config.py (DONCHIAN_*).
"""




