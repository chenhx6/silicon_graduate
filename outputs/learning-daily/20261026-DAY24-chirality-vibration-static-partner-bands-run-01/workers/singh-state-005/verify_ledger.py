"""Read-only checks of the worker transcription; not experimental validation."""
from pathlib import Path
import hashlib
import json

here = Path(__file__).resolve().parent
root = next(p for p in here.parents if (p / 'knowledge/index.md').is_file())
ledger = json.loads((here / 'ce131-table1-state-ledger.json').read_text())
raw = root / ledger['raw_check']['raw_file']
assert hashlib.sha256(raw.read_bytes()).hexdigest() == ledger['raw_check']['sha256']
rows = ledger['present']
assert len(rows) == 7
assert sum(r['mean_tau_ps']['kind'] == 'finite' for r in rows) == 4
assert sum(r['mean_tau_ps']['kind'] != 'finite' for r in rows) == 3
energy = sum(ledger['energy_anchor']['path_to_first_final_state_keV'])
for row in rows:
    assert int(row['Ji'].split('/')[0]) - int(row['Jf'].split('/')[0]) == 4
    assert row['parity_i'] == row['parity_f'] == 'negative'
    assert row['Ex_final_derived_keV'] == energy
    energy += row['Egamma_keV']
    assert row['Ex_initial_derived_keV'] == energy
assert len(ledger['comparison']) == 5
assert all(not r['original_pdf_crosscheck_in_this_worker'] for r in ledger['comparison'])
assert [r['reference'] for r in ledger['comparison']] == [31, 32, 32, 32, 32]
print('PASS: raw SHA, 7 rows (4 finite/3 limits), delta-I/parity, rounded-energy closure, old-row dependency labels.')
