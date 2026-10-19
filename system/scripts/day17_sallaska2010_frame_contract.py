#!/usr/bin/env python3
"""Literal version checks and NR resonance frame algebra; no experimental rescale."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import io
import json
import re
import tarfile
from scipy.integrate import quad

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'
TMP = ROOT / 'tmp/day17-sallaska2010'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    c = json.loads((RUN / 'sallaska2010-frame-exercise-contract.json').read_text())
    assert c['identity'] == 'S10-LITERAL-FRAME-BRIDGE-01'
    for path, value in c['hashes'].items():
        assert sha(ROOT / path) == value
    texts = [(TMP / f'v{v}-shortpaper_final1.tex').read_text() for v in [1, 2]]
    equation = [re.search(r'\\begin\{equation\}(.*?)\\end\{equation\}', s, re.S).group(1) for s in texts]
    assert equation[0] == equation[1] and r'lambdabar^2_{\textrm{lab}}' in equation[0]
    # The actual source table environment is identical across the two submissions.
    tables = [re.findall(r'\\begin\{table\*?\}.*?\\end\{table\*?\}', s, re.S) for s in texts]
    assert len(tables[0]) == len(tables[1]) == 1 and tables[0] == tables[1]
    members = []
    for v in [1, 2]:
        a = tarfile.open(fileobj=io.BytesIO((TMP / f'source-v{v}.payload').read_bytes()), mode='r:*')
        members.append({m.name: hashlib.sha256(a.extractfile(m).read()).hexdigest() for m in a.getmembers() if m.isfile()})
    assert members[0]['reactionrate_prl_MC.eps'] == members[1]['reactionrate_prl_MC.eps']
    assert members[0]['data_spectra.eps'] != members[1]['data_spectra.eps']
    m, target = c['declared_projectile_mass_units'], c['declared_target_mass_units']
    ratio = (m + target) / target
    mu = m * target / (m + target)
    elab = c['declared_lab_energy_units']
    ecm = elab / ratio
    lambda_lab_sq = 1 / (2 * m * elab)  # declared hbar=1
    lambda_cm_sq = 1 / (2 * mu * ecm)
    numeric_integral, numeric_error = quad(lambda x: 1/(1+x*x), -float('inf'), float('inf'), epsabs=1e-12)
    assert abs(numeric_integral - 3.141592653589793) < 1e-12
    assert abs(lambda_cm_sq / lambda_lab_sq - ratio**2) < 1e-14
    result = {'at': datetime.now(timezone.utc).isoformat(), 'script_sha256': sha(Path(__file__)),
              'hashes': c['hashes'], 'exact_Eq1_unchanged_v1_v2': True,
              'exact_TableI_source_unchanged_v1_v2': True,
              'rate_figure_EPS_unchanged_v1_v2': True, 'spectra_figure_EPS_changed': True,
              'NR_declared_control': {'m': m, 'M': target, 'r': ratio,
                   'Ecm_over_Elab': 1/ratio, 'lambda_cm_squared_over_lambda_lab_squared': ratio**2,
                   'lab_coefficient_relative_to_lambda_lab_squared': ratio**3,
                   'literal_Letter_coefficient_relative_to_lambda_lab_squared': ratio,
                   'literal_versus_CM_strength_factor_if_other_inputs_fixed': ratio**2,
                   'Lorentz_full_line_numeric_integral': numeric_integral,
                   'quad_error_estimate': numeric_error,
                   'boundary': 'narrow isolated NR resonance, full mathematical line, wavelength frozen; not original experimental producer/mass/CI'},
              'official_erratum_body_not_obtained': True,
              'no_claim_that_erratum_corrects_frame': True,
              'no_experimental_strengths_rescaled': True,
              'ok': True}
    (RUN / 'sallaska2010-frame-exercise-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='hashes'},ensure_ascii=False,indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
