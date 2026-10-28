#!/usr/bin/env python3
"""
nomura-2018-odd-ba-audit-006.py

Auditing Single-Particle Occupations, Odd-Neutron Blocking,
and Octupole Phonon Collectivity in 143,145,147Ba (Nomura et al. 2018).
"""

import json

def audit_nomura_data():
    # Data from Table II: single-particle energies (MeV) and occupation v^2
    sp_data = {
        "143Ba": {
            "3p1/2": {"eps": 3.374, "v2": 0.012},
            "3p3/2": {"eps": 2.732, "v2": 0.017},
            "2f5/2": {"eps": 2.464, "v2": 0.032},
            "2f7/2": {"eps": 0.443, "v2": 0.173},
            "1h9/2": {"eps": 0.000, "v2": 0.319},
            "1i13/2": {"eps": 3.333, "v2": 0.020}
        },
        "145Ba": {
            "3p1/2": {"eps": 3.421, "v2": 0.018},
            "3p3/2": {"eps": 2.797, "v2": 0.024},
            "2f5/2": {"eps": 2.537, "v2": 0.045},
            "2f7/2": {"eps": 0.552, "v2": 0.243},
            "1h9/2": {"eps": 0.000, "v2": 0.441},
            "1i13/2": {"eps": 3.378, "v2": 0.028}
        },
        "147Ba": {
            "3p1/2": {"eps": 3.461, "v2": 0.023},
            "3p3/2": {"eps": 2.856, "v2": 0.033},
            "2f5/2": {"eps": 2.605, "v2": 0.059},
            "2f7/2": {"eps": 0.652, "v2": 0.319},
            "1h9/2": {"eps": 0.000, "v2": 0.556},
            "1i13/2": {"eps": 3.417, "v2": 0.036}
        }
    }

    # Octupole driving pairs Delta l = Delta j = 3:
    # 1. 2f7/2 <-> 1i13/2 (l: 3->6, j: 7/2->13/2)
    # 2. 1h9/2 <-> 1i13/2 is Delta l = 1, Delta j = 2 (not octupole)
    # 3. 1h9/2 <-> 2f7/2 is Delta l = 2, Delta j = 1 (quadrupole)
    # The primary octupole driving matrix element involves u_i * v_j - v_i * u_j or u_i * v_j + v_i * u_j

    # Octupole phonon expectation value <n_f> in bandheads (Tables V, VII, IX)
    bandhead_nf = {
        "143Ba": {
            "negative_parity_yrast": {"J": "5/2-", "n_f": 0.000, "config": "nu(pfh) x sd_boson"},
            "positive_parity_octupole": {"J": "11/2+", "n_f": 0.95, "config": "nu(pfh) x (sd + f_boson)", "BE3_to_yrast_Wu": 13.0}
        },
        "145Ba": {
            "5/2-_1": {"J": "5/2-", "n_f": 0.000, "h9/2_pct": 92, "config": "nu(1h9/2) x sd_boson"},
            "7/2-_1": {"J": "7/2-", "n_f": 0.000, "h9/2_pct": 95, "config": "nu(1h9/2) x sd_boson"},
            "9/2+_1": {"J": "9/2+", "n_f": 0.000, "i13/2_pct": 88, "config": "nu(1i13/2) x sd_boson"},
            "11/2+_1_octupole": {"J": "11/2+", "Ex_calc_keV": 705, "Ex_exp_keV": 670, "n_f": 0.82, "BE3_Wu": 4.7},
            "15/2-_4_octupole": {"J": "15/2-", "Ex_calc_keV": 1167, "Ex_exp_keV": 1226, "n_f": 0.89, "BE3_Wu": 25.0}
        },
        "147Ba": {
            "3/2-_1": {"J": "3/2-", "n_f": 0.002, "config": "nu(pf) x sd_boson"},
            "1/2-_1": {"J": "1/2-", "n_f": 0.000, "config": "nu(pf) x sd_boson"},
            "7/2-_2": {"J": "7/2-", "n_f": 0.000, "h9/2_pct": 98, "config": "nu(1h9/2) x sd_boson"}
        }
    }

    # Contrast with even-even core
    even_core_BE3 = {
        "142Ba": {"B(E3; 3- -> 0+)": "weak vibration", "beta3_min": 0.0},
        "144Ba": {"B(E3; 3- -> 0+)": 23.0, "exp_Wu": "48(+25/-29) (Bucher 2016)", "beta3_soft": 0.11},
        "146Ba": {"B(E3; 3- -> 0+)": 27.0, "exp_Wu": "48(+9/-10) (Bucher 2017)", "beta3_soft": 0.12}
    }

    report = {
        "single_particle_data": sp_data,
        "bandhead_nf": bandhead_nf,
        "even_core_BE3": even_core_BE3,
        "blocking_mechanism": {
            "finding": "Odd neutron occupies nu(1h9/2) or nu(2f7/2) in 143,145,147Ba, blocking octupole virtual pair scattering between 2f7/2 and 1i13/2.",
            "consequence": "Low-lying states have <n_f> ~ 0.0; octupole states pushed up to Ex > 0.7-1.2 MeV.",
            "contrast_with_actinides": "In 225Ra, strong octupole deformation produces parity doublets right at ground state; in odd Ba, octupole correlations are purely vibrational and decoupled from ground states."
        }
    }

    out_path = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/nomura-2018-odd-ba-systematics-006.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print("SUCCESS: wrote", out_path)

if __name__ == "__main__":
    audit_nomura_data()
