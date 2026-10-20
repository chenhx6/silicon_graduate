#!/usr/bin/env python3
"""Audit printed In110 energy versus spacing and the lifetime coverage mask."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def main():
    contract_path = RUN / 'amr-review-energy-contract.json'
    data = json.loads(contract_path.read_text())
    rows = data['rows']
    residuals = []
    spacings = []
    for previous, current in zip(rows, rows[1:]):
        assert current[0] - previous[0] == 2
        residuals.append(current[1] - previous[1] - current[2])
        if previous[2] is not None:
            d = (current[2] - previous[2]) / 1000
            spacings.append({'spin_pair': [previous[0], current[0]],
                             'gamma_difference_keV': d * 1000,
                             'local_J2_hbar2_per_MeV': 4 / d,
                             'boundary': 'discrete difference, not a fitted rotor or new measurement'})
    assert max(abs(v) for v in residuals) < 1e-8
    measured = [r for r in rows if r[3] is not None]
    high = [r for r in rows if r[2] is not None and r[2] / 2000 > .70]
    assert len(measured) == 4 and all(r[3] is None for r in high)
    intervals = [(r[4] - r[5][0], r[4] + r[5][1]) for r in measured[-3:]]
    intersection = [max(i[0] for i in intervals), min(i[1] for i in intervals)]
    assert intersection[0] <= intersection[1]
    result = {'at': datetime.now(timezone.utc).isoformat(),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'contract_sha256': hashlib.sha256(contract_path.read_bytes()).hexdigest(),
              'level_energies_strictly_increase': all(b[1] > a[1] for a, b in zip(rows, rows[1:])),
              'level_gamma_residual_keV': residuals,
              'gamma_spacings_strictly_increase': all(b[2] > a[2] for a, b in zip(rows[1:], rows[2:])),
              'local_discrete_inertias': spacings,
              'measured_omega_MeV': [r[2] / 2000 for r in measured],
              'unmeasured_above_070_omega_MeV': [r[2] / 2000 for r in high],
              'last_three_marginal_BE2_boxes': intervals,
              'last_three_marginal_BE2_box_intersection': intersection,
              'intersection_is_not_joint_CI_or_test': True,
              'printed_level_energy_wording_does_not_literal_close': True,
              'no_new_independent_measurement_or_AMR_verdict': True,
              'no_actual_covariance_or_systematic_distribution_assumed': True,
              'ok': True}
    (RUN / 'amr-review-energy-result.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
