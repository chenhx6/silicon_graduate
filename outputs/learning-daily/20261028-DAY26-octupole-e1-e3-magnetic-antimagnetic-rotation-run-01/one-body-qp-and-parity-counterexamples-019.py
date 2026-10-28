#!/usr/bin/env python3
"""Conditional algebra examples; no nuclear fit, raw events, or SCCM replay.

The first example restricts a time-even one-body quadrupole component to
a time-reversed pair with equal diagonal matrix elements q. Three spectator
quasiparticles distinguish 3qp and 5qp sectors of a BCS vacuum. Angular
momentum projection can impose additional selection rules in a real nucleus.
"""

import json
import math
from pathlib import Path

import numpy as np


def main():
    u, v = 0.8, 0.6
    state3 = np.zeros(32)
    state5 = np.zeros(32)
    # Bits 2, 3, 4 are occupied spectators; bits 0, 1 are the active pair.
    state3[28], state3[31] = u, v
    state5[28], state5[31] = -v, u
    q = np.diag([(mask & 1) + ((mask >> 1) & 1) for mask in range(32)])
    overlap = float(state3 @ state5)
    pair_transfer_me = float(state3 @ q @ state5)

    # A rigid rotor must have zero parity displacement with this interpolation.
    rotational_constant_keV, spin = 12.0, 5
    energy = lambda i: rotational_constant_keV * i * (i + 1)
    midpoint = energy(spin) - (energy(spin - 1) + energy(spin + 1)) / 2
    weighted = energy(spin) - (
        (spin + 1) * energy(spin - 1) + spin * energy(spin + 1)
    ) / (2 * spin + 1)

    results = {
        "evidence_status": "conditional-algebra-not-experiment",
        "qp_counterexample": {
            "u": u, "v": v,
            "orthogonal_state_overlap": overlap,
            "one_body_matrix_element_in_q_units": pair_transfer_me,
            "analytic_2uv": 2 * u * v,
            "scope": "Disproves a universal one-body 3qp-5qp zero; not a Pr E2 matrix element."
        },
        "parity_rotor_control": {
            "A_keV": rotational_constant_keV, "I": spin,
            "unweighted_displacement_keV": midpoint,
            "spin_weighted_displacement_keV": weighted,
            "scope": "A nonzero unweighted midpoint is not by itself octupole stiffness."
        },
        "E3_reported_intervals_Wu": {
            "144Ba_Bucher2016": [14, 73],
            "146Ba_Bucher2017": [19, 69],
            "interval_jaccard": 50 / 59,
            "scope": "Descriptive interval geometry; no posterior or model odds."
        },
        "E1_146Ba_TableI": {
            "measured_eb_half": 0.000223,
            "SCCM_eb_half": 0.00474,
            "amplitude_ratio_model_over_reported": 0.00474 / 0.000223,
            "strength_ratio_model_over_reported": (0.00474 / 0.000223) ** 2,
            "scope": "Printed centers; no experimental likelihood or fitted shell decomposition."
        },
        "ideal_AMR_magnetic_geometry": {
            "j_h": 4.5, "j_p": 10.0, "g_h": 1.0, "g_p": -0.2,
            "theta_degrees": 60,
            "transverse_moment": 0.0,
            "longitudinal_moment": 2 * 4.5 * math.cos(math.pi / 3) - 0.2 * 10,
            "scope": "Equal blades cancel transverse moment; total moment need not vanish."
        }
    }
    out = Path(__file__).with_suffix('.json')
    out.write_text(json.dumps(results, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
