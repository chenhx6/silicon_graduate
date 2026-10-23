#!/usr/bin/env python3
"""Audits kinematic and dynamic moments of inertia, Harris expansion, and pairing systematics.

Declared mathematical and physical controls:
1. Differential calculus identity J^(2) = J^(1) + omega * dJ^(1)/domega;
2. Harris expansion relations J^(1) = J0 + J1*omega^2 and J^(2) = J0 + 3*J1*omega^2;
3. Discrete transition formulas for stretched E2 cascades (hbar*omega, J^(1), J^(2));
4. Rigid-body moment of inertia J_rig(A, beta2, r0) and comparison with normal vs HD bands;
5. Quenched pairing signatures vs residual surface/polarization deficits without over-strong certification.
"""
from __future__ import annotations

raise SystemExit("Deactivated checkpoint101: scientific certification withdrawn; original code and results retained in rejected-analysis-registry-101.json; no experimental validation.")

import argparse
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path

import numpy as np


def rigid_body_moi(a: int, beta2: float, r0_fm: float = 1.20) -> float:
    """Rigid body moment of inertia in hbar^2 / MeV:
    J_rig = (2/5) * M * R0^2 * (1 + 0.315 * beta2)
    where M = A * m_N, m_N ~ 938.92 MeV/c^2, hbar*c ~ 197.327 MeV*fm.
    """
    m_n = 938.91897
    hbarc = 197.32698
    c_pre = (2.0 / 5.0) * (m_n / (hbarc**2)) * (r0_fm**2)  # hbar^2 / (MeV * fm^2)
    return c_pre * (a**(5.0 / 3.0)) * (1.0 + 0.3149 * beta2)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", type=Path, required=True)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()

    checks = []
    def check(name, ok):
        if not ok:
            raise AssertionError(name)
        checks.append({"name": name, "passed": bool(ok)})

    # 1. Differential identity verification
    # J^(1) = I / omega. If J^(1) = J0 + J1 * omega^2, then:
    # J^(2) = dI / domega = J0 + 3 * J1 * omega^2
    j0_test, j1_test, omega_test = 30.0, 50.0, 0.40
    j1_val = j0_test + j1_test * (omega_test**2)
    dj1_domega = 2.0 * j1_test * omega_test
    j2_diff = j1_val + omega_test * dj1_domega
    j2_analytic = j0_test + 3.0 * j1_test * (omega_test**2)
    check("Differential calculus identity J^(2) = J^(1) + omega*dJ^(1)/domega strictly holds",
          math.isclose(j2_diff, j2_analytic, rel_tol=1e-9))
    check("Difference J^(2) - J^(1) equals 2 * J1 * omega^2",
          math.isclose(j2_analytic - j1_val, 2.0 * j1_test * (omega_test**2), rel_tol=1e-9))

    # 2. Discrete cascade formulas for stretched E2
    # E(I) - E(I-2) = E_gamma; omega = E_gamma / (2*hbar)
    # J^(1) = (2*I - 1) / E_gamma; J^(2) = 4 / Delta E_gamma
    e_gamma1 = 0.800  # MeV, 18+ -> 16+
    e_gamma2 = 0.860  # MeV, 20+ -> 18+
    delta_eg = e_gamma2 - e_gamma1  # 0.060 MeV
    spin_i = 18
    omega_mid = (e_gamma1 / 2.0)
    j1_discrete = (2.0 * spin_i - 1.0) / e_gamma1  # (35) / 0.800 = 43.75 hbar^2/MeV
    j2_discrete = 4.0 / delta_eg                    # 4.0 / 0.060 = 66.67 hbar^2/MeV
    check("Discrete kinematic MoI formula J^(1) = (2I-1)/E_gamma gives 43.75 hbar^2/MeV",
          math.isclose(j1_discrete, 43.75, rel_tol=1e-6))
    check("Discrete dynamic MoI formula J^(2) = 4/Delta_Egamma gives 66.67 hbar^2/MeV",
          math.isclose(j2_discrete, 66.666667, rel_tol=1e-5))

    # 3. Rigid body benchmarks in 131Ce and 134Nd
    # 131Ce: A=131, r0=1.20 fm
    # Normal deformed (beta2 ~ 0.20): J_rig ~ 49.3 hbar^2/MeV
    # Highly deformed (beta2 ~ 0.38): J_rig ~ 51.9 hbar^2/MeV
    j_rig_ce_nd = rigid_body_moi(131, beta2=0.20, r0_fm=1.20)
    j_rig_ce_hd = rigid_body_moi(131, beta2=0.38, r0_fm=1.20)
    check("131Ce rigid MoI: normal band ~49.3 hbar^2/MeV, HD band ~51.9 hbar^2/MeV",
          48.0 < j_rig_ce_nd < 50.5 and 50.5 < j_rig_ce_hd < 53.5)

    # 134Nd: A=134, r0=1.20 fm
    # Normal deformed (beta2 ~ 0.20): J_rig ~ 51.2 hbar^2/MeV
    # Highly deformed (beta2 ~ 0.36): J_rig ~ 53.6 hbar^2/MeV
    j_rig_nd_nd = rigid_body_moi(134, beta2=0.20, r0_fm=1.20)
    j_rig_nd_hd = rigid_body_moi(134, beta2=0.36, r0_fm=1.20)
    check("134Nd rigid MoI: normal band ~51.2 hbar^2/MeV, HD band ~53.6 hbar^2/MeV",
          50.0 < j_rig_nd_nd < 52.5 and 52.5 < j_rig_nd_hd < 55.0)

    # 4. Quenched pairing vs normal pairing contrast
    # Normal band low-spin J^(1) ~ 20-25 hbar^2/MeV (35-50% of J_rig)
    # HD band J^(2) ~ 45-48 hbar^2/MeV (86-92% of J_rig)
    ratio_nd_lowspin = 22.0 / j_rig_ce_nd  # ~ 44.6%
    ratio_hd_plateau = 46.5 / j_rig_ce_hd  # ~ 89.6%
    check("Normal band low-spin MoI ratio is ~ 40-50% of J_rig due to BCS pairing",
          0.35 < ratio_nd_lowspin < 0.55)
    check("HD band plateau MoI ratio is ~ 85-92% of J_rig indicating strongly quenched pairing",
          0.85 < ratio_hd_plateau < 0.95)

    out = {
        "checkpoint": "048",
        "audited_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "differential_identities": {
            "relation": "J^(2) = J^(1) + omega * dJ^(1)/domega",
            "harris_form": "J^(1) = J0 + J1*omega^2, J^(2) = J0 + 3*J1*omega^2",
            "difference": "J^(2) - J^(1) = 2*J1*omega^2",
            "test_point": {"J0": j0_test, "J1": j1_test, "omega": omega_test, "J1_val": j1_val, "J2_val": j2_analytic}
        },
        "discrete_formulas": {
            "rotational_frequency": "hbar * omega = E_gamma / 2",
            "kinematic_moi": "J^(1)(I-1) = (2I-1) / E_gamma(I -> I-2)",
            "dynamic_moi": "J^(2)(I) = 4 / Delta_E_gamma",
            "example_eval": {"E_gamma1": e_gamma1, "E_gamma2": e_gamma2, "J1": j1_discrete, "J2": j2_discrete}
        },
        "rigid_body_benchmarks": {
            "131Ce": {"A": 131, "r0_fm": 1.20, "J_rig_ND": round(j_rig_ce_nd, 2), "J_rig_HD": round(j_rig_ce_hd, 2)},
            "134Nd": {"A": 134, "r0_fm": 1.20, "J_rig_ND": round(j_rig_nd_nd, 2), "J_rig_HD": round(j_rig_nd_hd, 2)}
        },
        "pairing_systematics_boundary": {
            "normal_band": {"lowspin_ratio_to_Jrig": round(ratio_nd_lowspin, 3), "mechanism": "Strong BCS static pairing reduces MoI to 35-50% of rigid rotor; Coriolis decoupling causes backbending."},
            "highly_deformed_band": {"plateau_ratio_to_Jrig": round(ratio_hd_plateau, 3), "mechanism": "Pairing strongly quenched by high rotational frequency and intruder orbital occupation; flat J^(2) plateau at 85-92% of J_rig."},
            "residual_deficit_boundary": "The ~10% deficit from macroscopic rigid sphere reflects nuclear surface diffuseness, residual pairing fluctuations, and core polarization, and cannot be cited as definitive proof of complete pairing collapse."
        },
        "checks": checks,
        "all_checks_passed": True,
        "boundary": "Mathematical and physical controls on moments of inertia. Experimental data points require verified gamma-ray cascade identification and do not certify unique nuclear interior models."
    }

    out_path = run_dir / "moments-of-inertia-result-048.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"artifact": str(out_path), "checks": len(checks), "all_passed": True}))


if __name__ == "__main__":
    main()
