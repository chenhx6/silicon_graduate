#!/usr/bin/env python3
"""Day 20 uncredited preview: B(E2), Qt, Q_spec and beta2 model boundaries."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path


def cg_rotor_e2_square(i, k):
    """Square of <I K 2 0 | I-2 K>^2 for fixed K rotor."""
    if i < 2 or abs(k) > i - 2:
        return 0.
    num = 3. * (i + k - 1) * (i + k) * (i - k - 1) * (i - k)
    den = 2. * i * (i - 1) * (2 * i - 1) * (2 * i + 1)
    return num / den


def q_spec_rotor(i, k, q0):
    """Axial rotor spectroscopic quadrupole moment <I K 2 0 | I K> Q0."""
    factor = (3. * k * k - i * (i + 1)) / ((i + 1) * (2 * i + 3))
    return factor * q0


def beta2_axial_first_order(q0_eb, z, a):
    """Linear approximation Q0 = 3/sqrt(5pi) * Z * R0^2 * beta2."""
    r0 = 1.2 * (a ** (1. / 3.))  # fm
    constant = (3. / math.sqrt(5. * math.pi)) * z * (r0 ** 2) / 100.  # eb
    return q0_eb / constant, constant


def beta2_axial_second_order(q0_eb, z, a):
    """Declared polynomial control, c=.16; NOT source deformation producer."""
    _, constant = beta2_axial_first_order(q0_eb, z, a)
    c = q0_eb / constant
    disc = 1. + 4. * 0.16 * c
    if disc < 0:
        return None
    return (-1. + math.sqrt(disc)) / (2. * 0.16)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    checks = []

    def check(name, ok):
        checks.append({'name': name, 'passed': bool(ok)})
        if not ok:
            raise AssertionError(name)

    g_half = cg_rotor_e2_square(13.5, 0.5)
    g_eleven = cg_rotor_e2_square(13.5, 5.5)
    check('CG square K=1/2 matches 26/75', math.isclose(g_half, 26. / 75., rel_tol=1e-12))
    check('CG square K=11/2 matches 76/325', math.isclose(g_eleven, 76. / 325., rel_tol=1e-12))
    b_unit = 0.1723
    qt_half = math.sqrt(b_unit / ((5. / (16. * math.pi)) * g_half))
    qt_eleven = math.sqrt(b_unit / ((5. / (16. * math.pi)) * g_eleven))
    check('Qt K=1/2 matches 2.2353 eb', math.isclose(qt_half, 2.235300, rel_tol=1e-5))
    check('Qt K=11/2 matches 2.7216 eb', math.isclose(qt_eleven, 2.721616, rel_tol=1e-5))
    ratio = qt_eleven / qt_half
    check('Ratio exactly matches theoretical sqrt(169/114)', math.isclose(ratio, math.sqrt(169. / 114.), rel_tol=1e-6))
    rounding_interval = [(2.72-.005)/(2.28+.005), (2.72+.005)/(2.28-.005)]
    check('printing to nearest .01 cannot explain candidate-ratio gap', ratio > rounding_interval[1])
    q_axial_k0 = q_spec_rotor(2, 0, 1.0)
    check('I=2 K=0 spectroscopic quadrupole moment matches -2/7 Q0', math.isclose(q_axial_k0, -2. / 7., rel_tol=1e-12))
    q_axial_k2 = q_spec_rotor(3, 2, 1.0)
    check('I=3 K=2 spectroscopic quadrupole moment is identically zero', math.isclose(q_axial_k2, 0., abs_tol=1e-14))
    z_ce, a_ce, q0_hd = 58, 131, 7.30
    b1, c0 = beta2_axial_first_order(q0_hd, z_ce, a_ce)
    b2 = beta2_axial_second_order(q0_hd, z_ce, a_ce)
    check('131Ce HD beta2 linear approximation around 0.448', math.isclose(b1, 0.4477, rel_tol=1e-3))
    check('131Ce HD beta2 second order around 0.419', math.isclose(b2, 0.4195, rel_tol=1e-3))
    check('declared polynomial is internally inverted', math.isclose(c0*(b2+.16*b2*b2), q0_hd, rel_tol=1e-12))

    result = {
        'created_at_utc': datetime.now(timezone.utc).isoformat(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope': 'fixed-K CG and axial static moment; declared radius/polynomial control, no source deformation reproduction or DF claim',
        'withdrawn': 'previous DF function gives zero at axial gamma=0 where its stated normalized B should be 1; removed; original DF body still needed',
        'rotor_cg_27_2_minus': {
            'G_K_half': g_half, 'G_K_eleven_half': g_eleven,
            'Qt_K_half_eb': qt_half, 'Qt_K_eleven_half_eb': qt_eleven, 'ratio': ratio,
            'printed_2_72_over_2_28_rounding_interval': rounding_interval,
            'boundary': 'hypothetical K values do not identify original author K or resolve actual producer'
        },
        'axial_q_spec_controls': {
            'I2_K0_over_Q0': q_axial_k0, 'I3_K2_over_Q0': q_axial_k2
        },
        'deformation_expansion_131ce_hd': {
            'Q0_eb': q0_hd, 'Z': z_ce, 'A': a_ce, 'linear_beta2': b1,
            'second_order_beta2': b2, 'overestimate_ratio': b1 / b2 - 1.,
            'model_inputs': 'R0=1.2 A^(1/3) fm, c=.16; conditional difference, not experimental bias or Petrache beta=.38 reconstruction'
        },
        'checks': checks, 'check_count': len(checks)
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'check_count': len(checks), 'checks': [c['name'] for c in checks]}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
