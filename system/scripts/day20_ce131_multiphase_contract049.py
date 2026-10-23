#!/usr/bin/env python3
"""Audits 131Ce multiphase collectivity across 6 orders of magnitude in lifetime.

Declared mathematical and model controls:
1. Laboratory spectroscopic quadrupole moment Qs to intrinsic Q0 mapping for I=9/2 with various K projections;
2. TDPAD 88-ns isomer moments in 129,131Ce (Ionescu-Bujor 1998) and EFG ratio invariance;
3. Normal-deformed band Qt=2.579(99) eb (Singh 2016) inversion to beta2;
4. Highly-deformed intruder band Q0=7.3(4) eb (Petrache 1998) inversion to beta2;
5. Collectivity jump factor and 6-order-of-magnitude lifetime hierarchy;
6. Rigorous decoupling of laboratory tensor observable Qs from body-fixed transition moment Qt.
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

from day20_shape_parameterization_contract047 import solve_beta2_quadratic, prefactor


def qs_to_q0_factor(spin_i: float, k_proj: float) -> float:
    """Axial rotor projection factor Qs = factor * Q0:
    factor = [3*K^2 - I*(I+1)] / [(I+1)*(2*I+3)]
    """
    num = 3.0 * (k_proj**2) - spin_i * (spin_i + 1.0)
    den = (spin_i + 1.0) * (2.0 * spin_i + 3.0)
    return num / den


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

    # -------------------------------------------------------------------------
    # 1. Axial rotor projection factors for I = 9/2
    # -------------------------------------------------------------------------
    # For I = 9/2: den = (11/2)*(12) = 66
    # K = 9/2: num = 3*(81/4) - (9/2)*(11/2) = 243/4 - 99/4 = 144/4 = 36. Factor = 36/66 = 6/11 ~ 0.545455
    # K = 1/2: num = 3*(1/4) - 99/4 = -96/4 = -24. Factor = -24/66 = -4/11 ~ -0.363636
    f_k92 = qs_to_q0_factor(4.5, 4.5)
    f_k12 = qs_to_q0_factor(4.5, 0.5)
    check("Axial rotor Qs/Q0 factor for I=9/2, K=9/2 is exactly 6/11 (~0.5455)",
          math.isclose(f_k92, 6.0 / 11.0, rel_tol=1e-6))
    check("Axial rotor Qs/Q0 factor for I=9/2, K=1/2 is exactly -4/11 (~-0.3636)",
          math.isclose(f_k12, -4.0 / 11.0, rel_tol=1e-6))

    # -------------------------------------------------------------------------
    # 2. Isomer Q0 extraction (Ionescu-Bujor 1998, |Qs| = 0.92(10) eb)
    # -------------------------------------------------------------------------
    qs_isomer = 0.92
    qs_err = 0.10
    q0_isomer_k92 = qs_isomer / f_k92  # 0.92 / (6/11) = 1.6867 eb
    # Pure axial rotor with K=9/2 under r0 = 1.20 fm yields beta2 ~ 0.100:
    beta2_isomer_axial = solve_beta2_quadratic(q0_isomer_k92, z=58, a=131, r0_fm=1.20, beta4=0.0)
    # In contrast, Ionescu-Bujor 1998 Table 1 PTR model includes K-mixing (K=9/2 and 7/2) and gamma=20-23 deg,
    # obtaining Qcal = +0.91 to +0.93 eb at epsilon2 = 0.14 - 0.18 (corresponding to beta2 ~ 0.15 - 0.20).
    check("Pure axial rotor K=9/2 inversion yields Q0~1.69 eb, beta2~0.100, underestimating PTR epsilon2=0.14-0.18 due to omitted K-mixing",
          math.isclose(q0_isomer_k92, 1.6867, abs_tol=0.01) and math.isclose(beta2_isomer_axial, 0.0998, abs_tol=0.005))

    # -------------------------------------------------------------------------
    # 3. Normal-deformed band (Singh 2016, Qt = 2.579(99) eb)
    # -------------------------------------------------------------------------
    qt_nd = 2.57894
    # Axial prolate (gamma=0 deg) quadratic inversion:
    beta2_nd_axial = solve_beta2_quadratic(qt_nd, z=58, a=131, r0_fm=1.20, beta4=0.0)
    # Under triaxial assumption gamma = -80 deg / +20 deg from TRS (geometric factor = cos(50)/cos(30) ~ 0.74223):
    geo_factor_20 = math.cos(math.radians(50)) / math.cos(math.radians(30))
    q20_nd_triaxial = qt_nd / geo_factor_20  # ~ 3.4746 eb
    beta2_nd_triaxial = solve_beta2_quadratic(q20_nd_triaxial, z=58, a=131, r0_fm=1.20, beta4=0.0)  # ~ 0.198
    # First-order linear inversion under gamma ~ 25 deg (geo_factor ~ 0.6623):
    geo_factor_25 = math.cos(math.radians(55)) / math.cos(math.radians(30))
    q20_nd_25 = qt_nd / geo_factor_25  # ~ 3.894 eb
    beta2_nd_linear_25 = q20_nd_25 / prefactor(58, 131, 1.20)  # ~ 0.239 ~ 0.24
    check("ND band Qt = 2.579 eb yields beta2 ~ 0.150 under axial prolate second-order inversion",
          math.isclose(beta2_nd_axial, 0.1500, abs_tol=0.005))
    check("ND band beta2 increases to ~0.198 under triaxial gamma=20 deg, and reaches ~0.24 only under linear gamma=25 deg assumption",
          math.isclose(beta2_nd_triaxial, 0.1983, abs_tol=0.005) and math.isclose(beta2_nd_linear_25, 0.2386, abs_tol=0.01))

    # -------------------------------------------------------------------------
    # 4. Highly-deformed band (Petrache 1998, Q0 = 7.3(4) eb)
    # -------------------------------------------------------------------------
    q0_hd = 7.30
    beta2_hd = solve_beta2_quadratic(q0_hd, z=58, a=131, r0_fm=1.20, beta4=0.0)
    check("HD band Q0 = 7.30 eb gives beta2 ~ 0.392 under second-order inversion (r0=1.20)",
          math.isclose(beta2_hd, 0.3922, abs_tol=0.005))

    # -------------------------------------------------------------------------
    # 5. Collectivity jump factor and lifetime hierarchy
    # -------------------------------------------------------------------------
    collectivity_jump_ratio = q0_hd / qt_nd  # 7.30 / 2.579 ~ 2.8306
    be2_jump_ratio = collectivity_jump_ratio**2  # ~ 8.01
    check("Collectivity jump Q0(HD)/Qt(ND) is ~ 2.83x, corresponding to ~ 8.0x jump in B(E2)",
          math.isclose(collectivity_jump_ratio, 2.8306, rel_tol=1e-3) and math.isclose(be2_jump_ratio, 8.012, rel_tol=1e-3))

    # Lifetime dynamic range
    tau_isomer = 88.0e-9   # 88 ns
    tau_nd_typ = 1.0e-12    # ~ 1 ps
    tau_hd_typ = 0.08e-12  # ~ 80 fs
    lifetime_span_orders = math.log10(tau_isomer / tau_hd_typ)  # log10(1.1e6) ~ 6.04
    check("Lifetime hierarchy spans > 6 orders of magnitude (88 ns to ~80 fs)",
          lifetime_span_orders > 6.0)

    # -------------------------------------------------------------------------
    # Output structured artifact
    # -------------------------------------------------------------------------
    out = {
        "checkpoint": "049",
        "audited_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "three_phase_systematics": {
            "nucleus": "131Ce",
            "phases": [
                {
                    "name": "88-ns Isomer",
                    "experimental_method": "TDPAD in CeSn3 host (Ionescu-Bujor 1998)",
                    "lifetime": "tau = 88 ns",
                    "primary_observable": "Spectroscopic quadrupole moment |Qs| = 0.92(10) eb",
                    "rotor_projection": "Qs/Q0 = 6/11 under K=9/2",
                    "inferred_Q0_eb": round(q0_isomer_k92, 3),
                    "inferred_beta2": round(beta2_isomer_axial, 3),
                    "ptr_model_epsilon2": "0.14 - 0.18 (gamma ~ 20 - 23 deg)",
                    "boundary": "Laboratory frame tensor observable; depends on host electric field gradient (EFG) and K-alignment assumption. Pure axial rotor severely underestimates deformation compared to PTR model with K-mixing."
                },
                {
                    "name": "Normal Deformed (ND) Yrast Band",
                    "experimental_method": "Plunger (RDM) + DSAM (Singh 2016 Table 1; Li 2004)",
                    "lifetime": "tau ~ 0.5 - 10 ps",
                    "primary_observable": "Transition quadrupole moment Qt = 2.579(99) eb (Present finite mean)",
                    "inferred_beta2_axial": round(beta2_nd_axial, 3),
                    "inferred_beta2_triaxial_gamma20": round(beta2_nd_triaxial, 3),
                    "inferred_beta2_linear_gamma25": round(beta2_nd_linear_25, 3),
                    "boundary": "Body-fixed frame E2 transition observable; axial prolate gives beta2~0.150, triaxial gamma~20-25 deg yields beta2~0.20-0.24."
                },
                {
                    "name": "Highly Deformed (HD) Intruder Band",
                    "experimental_method": "DSAM line-shape analysis (Petrache 1998 Table I)",
                    "lifetime": "tau ~ 0.05 - 0.20 ps",
                    "primary_observable": "Band-fitted intrinsic quadrupole moment Q0 = 7.3(4) eb",
                    "inferred_beta2": round(beta2_hd, 3),
                    "boundary": "Whole-band parameter fit assuming constant Q0; driven by intruder orbital nu i13/2 [660]1/2+."
                }
            ],
            "collectivity_jump": {
                "ratio_Q0_HD_over_Qt_ND": round(collectivity_jump_ratio, 2),
                "ratio_BE2_HD_over_BE2_ND": round(be2_jump_ratio, 2),
                "lifetime_span_ratio": round(tau_isomer / tau_hd_typ, 1),
                "lifetime_span_log10": round(lifetime_span_orders, 2)
            }
        },
        "physical_boundaries": [
            "Laboratory Qs vs body-fixed Qt: Qs depends on projection factor [3K^2 - I(I+1)]/[(I+1)(2I+3)] and lattice EFG, while Qt reflects transitional E2 matrix element.",
            "The 2.83x collectivity step reflects intruder quasiparticle configuration change (nu i13/2), not a continuous phase transition of the ground-state core.",
            "The three phases represent distinct excitation regimes and configurations, not an unparameterized closed proof of nuclear shape evolution."
        ],
        "checks": checks,
        "all_checks_passed": True,
        "boundary": "Mathematical and model sensitivity analysis for 131Ce multiphase collectivity. Does not certify unique nuclear interior shape without experimental covariance."
    }

    out_path = run_dir / "ce131-multiphase-result-049.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"artifact": str(out_path), "checks": len(checks), "all_passed": True}))


if __name__ == "__main__":
    main()
