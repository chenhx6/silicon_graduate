#!/usr/bin/env python3
"""Read-only arithmetic on literal thesis Ch5 inputs; no experimental refit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def polynomial(coefficients, energy):
    return sum(v * energy**k for k, v in enumerate(coefficients))


def main():
    cp = RUN / 'fougeres2022-thesis-ch5-exercise-contract.json'
    c = json.loads(cp.read_text())
    assert sha(ROOT / c['pdf']) == c['pdf_sha256']
    assert len(c['Table5p1']) == 22
    key = next(x for x in c['Table5p1'] if x['Ex_MeV'] == 7.785)
    lo, hi = key['experiment_gate_MeV']
    overlaps = []
    for row in c['Table5p1']:
        a, b = row['experiment_gate_MeV']
        width = max(0, min(hi, b) - max(lo, a))
        if width:
            overlaps.append({'Ex_MeV': row['Ex_MeV'], 'Egamma0_MeV': row['Egamma0_MeV'],
                             'overlap_width_MeV': width,
                             'fraction_of_key_interval_length': width / (hi - lo),
                             'boundary': 'interval length only; not event contamination or probability'})
    mappings = {}
    for label, coeff in c['Eq5p8'].items():
        at = [(e, polynomial(coeff, e)) for e in [lo, (lo + hi) / 2, hi]]
        root = (-coeff[1] - math.sqrt(coeff[1]**2 - 4 * coeff[2] * (coeff[0] - key['Ex_MeV']))) / (2 * coeff[2])
        assert abs(polynomial(coeff, root) - key['Ex_MeV']) < 1e-12
        mappings[label] = {'at_Ealpha_gate_edges_and_center_MeV': at,
                           'Ealpha_for_key_Ex_MeV': root,
                           'boundary': 'literal model polynomial, not event-level measured Ex or CI'}
    losses = {label: [{'Ealpha_MeV': e, 'printed_loss_MeV': polynomial(coeff, e)}
                       for e in c['loss_probe_Ealpha_MeV']]
              for label, coeff in c['Eq5p5_literal'].items()}
    beta = c['Fig5p8_mean_beta']
    ratio = c['contaminant_E_MeV'] / key['Egamma0_MeV']
    cosine = (1 - math.sqrt(1 - beta**2) / ratio) / beta
    assert -1 < cosine < 0
    angle = math.degrees(math.acos(cosine))
    inverse = (ratio**2 * cosine + math.sqrt(1 + ratio**2 * cosine**2 - ratio**2)) / (1 + ratio**2 * cosine**2)
    assert abs(inverse - beta) < 1e-12
    residuals = []
    for b in [.01, .04, beta]:
        for deg in [120, 145, 170]:
            co = math.cos(math.radians(deg))
            r = math.sqrt(1 - b*b) / (1 - b*co)
            back = (r*r*co + math.sqrt(1 + r*r*co*co - r*r)) / (1 + r*r*co*co)
            residuals.append(abs(back - b))
    assert max(residuals) < 1e-12
    out = {'at': datetime.now(timezone.utc).isoformat(), 'script_sha256': sha(Path(__file__)),
           'contract_sha256': sha(cp), 'Table5p1_rows': len(c['Table5p1']),
           'key_gate_MeV': [lo, hi], 'nonzero_gate_intersections': overlaps,
           'Eq5p8_key_gate_mappings': mappings, 'Eq5p5_literal_probes': losses,
           'Doppler_line_crossing': {'Egamma0_MeV': key['Egamma0_MeV'],
                'stationary_contaminant_E_MeV': c['contaminant_E_MeV'], 'mean_beta': beta,
                'theta_DS_degrees': angle, 'Eq5p11_recovered_beta': inverse,
                'boundary': 'single mean beta; theta_DS is not lab theta_gamma; no rejection-mask inference'},
           'Eq5p11_forward_inverse_max_abs_residual': max(residuals),
           'literal_inputs_preserved': True, 'no_new_experimental_lifetime_response_or_CI': True, 'ok': True}
    (RUN / 'fougeres2022-thesis-ch5-exercise-result.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
