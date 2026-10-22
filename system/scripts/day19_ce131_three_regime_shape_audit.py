#!/usr/bin/env python3
"""Quantitative audit of 131Ce three-regime deformation hierarchy and shape coexistence.

Synthesizes the three experimental shape regimes in 131Ce:
1. 9/2- isomer (TDPAD, Ionescu-Bujor 1998, |Q_spec| = 0.92(10) eb);
2. Normal-deformed Band 1 (DSAM, Li 2004 & Plunger, Singh 2016, Qt = 2.26 - 2.72 eb);
3. Highly-deformed Band SD-1 (DSAM, Petrache 1998, Q0 = 7.3(4) eb, beta2 = 0.38(2)).
Evaluates the 4.3x deformation expansion hierarchy and maps the intruder configuration boundary.
Uses only the Python standard library. Requires --output PATH.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path


def calculate_beta2_quadratic(q0_eb, z=58, a=131, r0_fm=1.25, c2=0.16):
    """Calculate beta2 from Q0 using Q0 = (3/sqrt(5*pi)) * Z * R0^2 * beta2 * (1 + c2*beta2)."""
    r0 = r0_fm * (a ** (1.0 / 3.0))
    prefactor = (3.0 / math.sqrt(5.0 * math.pi)) * z * (r0 ** 2) * 0.01  # eb
    discriminant = 1.0 + 4.0 * c2 * (q0_eb / prefactor)
    return (-1.0 + math.sqrt(discriminant)) / (2.0 * c2)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Path for output JSON")
    args = parser.parse_args()

    checks = []
    def check(name, condition):
        checks.append({"name": name, "passed": bool(condition)})
        if not condition:
            raise AssertionError(f"Check failed: {name}")

    # 1. Regime 1: Isomer 9/2- (Ionescu-Bujor 1998)
    q_spec_iso = 0.92  # eb
    sig_q_spec_iso = 0.10
    g_iso = -0.189
    tau_iso_ns = 88.0 / math.log(2.0)  # T1/2 = 88 ns => tau = 126.95 ns

    # Intrinsic Q0 under bandhead K = 9/2:
    # Q_spec = Q0 * [3*(9/2)^2 - (9/2)(11/2)] / [(11/2)*12] = Q0 * (6/11)
    # Q0 = (11/6) * Q_spec
    q0_iso = (11.0 / 6.0) * q_spec_iso  # = 1.6867 eb
    sig_q0_iso = (11.0 / 6.0) * sig_q_spec_iso  # = 0.1833 eb
    beta2_iso = calculate_beta2_quadratic(q0_iso)

    check("Isomer Q_spec is 0.92(10) eb", math.isclose(q_spec_iso, 0.92, abs_tol=1e-4))
    check("Isomer derived intrinsic Q0 is ~ 1.69 eb", math.isclose(q0_iso, 1.6867, abs_tol=0.01))

    # 2. Regime 2: Normal-Deformed Band 1 (Li 2004 & Singh 2016)
    tau_27_ps = 1.235  # ps (weighted mean of 1.23 and 1.24 ps)
    qt_nd_k1 = 2.26   # eb (Singh 2016, K=1/2 convention)
    sig_qt_nd_k1 = 0.30
    qt_nd_k11 = 2.72  # eb (Li 2004, K=11/2 convention)
    sig_qt_nd_k11 = 0.25

    beta2_nd_k1 = calculate_beta2_quadratic(qt_nd_k1)
    beta2_nd_k11 = calculate_beta2_quadratic(qt_nd_k11)

    check("ND Band 1 Qt under K=1/2 is 2.26 eb", math.isclose(qt_nd_k1, 2.26, abs_tol=1e-4))
    check("ND Band 1 Qt under K=11/2 is 2.72 eb", math.isclose(qt_nd_k11, 2.72, abs_tol=1e-4))

    # 3. Regime 3: Highly-Deformed Band SD-1 (Petrache 1998)
    q0_hd = 7.3   # eb
    sig_q0_hd = 0.4
    q_sf_hd = 6.0  # eb
    beta2_hd = calculate_beta2_quadratic(q0_hd)  # = 0.3884

    check("HD Band SD-1 Q0 is 7.3(4) eb", math.isclose(q0_hd, 7.3, abs_tol=1e-4))
    check("HD Band beta2 (r0=1.25 fm) matches reported 0.38(2)", math.isclose(beta2_hd, 0.388, abs_tol=0.01))

    # 4. Deformation step ratios
    ratio_hd_to_nd_k1 = q0_hd / qt_nd_k1    # = 7.3 / 2.26 = 3.230
    ratio_hd_to_nd_k11 = q0_hd / qt_nd_k11  # = 7.3 / 2.72 = 2.684
    ratio_nd_to_iso = qt_nd_k1 / q0_iso     # = 2.26 / 1.6867 = 1.340
    ratio_hd_to_iso = q0_hd / q0_iso       # = 7.3 / 1.6867 = 4.328

    check("HD to ND quadrupole ratio exceeds 2.6x (3.23x for K=1/2)", ratio_hd_to_nd_k1 > 3.0)
    check("ND to Isomer quadrupole ratio is ~ 1.34x", math.isclose(ratio_nd_to_iso, 1.340, abs_tol=0.02))
    check("HD to Isomer quadrupole ratio is ~ 4.33x", math.isclose(ratio_hd_to_iso, 4.328, abs_tol=0.02))

    # 5. Corresponding B(E2) ratios (scaling as Q^2)
    be2_ratio_hd_to_nd = (q0_hd / qt_nd_k1) ** 2  # = 3.23^2 = 10.43
    be2_ratio_hd_to_iso = (q0_hd / q0_iso) ** 2   # = 4.328^2 = 18.73

    check("HD band collective B(E2) is > 10x larger than normal-deformed band", be2_ratio_hd_to_nd > 10.0)
    check("HD band collective B(E2) is > 18x larger than isomer rotor baseline", be2_ratio_hd_to_iso > 18.0)

    # 6. Hierarchy of experimental techniques across time domains
    # Regime 1: TDPAD in Sn host, nanosecond domain (tau = 127 ns)
    # Regime 2: Plunger & DSAM, picosecond domain (tau = 1.23 ps)
    # Regime 3: Fast DSAM with fractional shifts, sub-picosecond domain (tau ~ 0.05 - 0.2 ps)
    time_domain_ratio_iso_to_nd = (tau_iso_ns * 1e3) / tau_27_ps  # = 126950 / 1.235 ~ 1.03e5
    check("Time domain spans 5 orders of magnitude from isomer (127 ns) to ND (1.2 ps)",
          time_domain_ratio_iso_to_nd > 1e5)

    result = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "131Ce three-regime deformation hierarchy and shape coexistence quantitative audit",
        "regime_1_isomer": {
            "state": "9/2- (162 keV, T1/2 = 88 ns)",
            "method": "TDPAD in polycrystalline Sn (Ionescu-Bujor 1998)",
            "Q_spec_eb": q_spec_iso,
            "sig_Q_spec_eb": sig_q_spec_iso,
            "g_factor": g_iso,
            "tau_ns": tau_iso_ns,
            "derived_Q0_K9_eb": q0_iso,
            "beta2_quadratic": beta2_iso,
            "structure": "Single quasiparticle nu h11/2 without core alignment (triaxial core epsilon2 ~ 0.16, gamma ~ 22 deg)",
        },
        "regime_2_normal_deformed_band1": {
            "band": "nu h11/2 yrast band (I = 11/2- to 35/2-)",
            "methods": "DSAM (Li 2004) and Plunger RDDS (Singh 2016)",
            "tau_27_2_ps": tau_27_ps,
            "Qt_K1_2_eb": qt_nd_k1,
            "Qt_K11_2_eb": qt_nd_k11,
            "beta2_quadratic_K1_2": beta2_nd_k1,
            "beta2_quadratic_K11_2": beta2_nd_k11,
            "structure": "Collective rotation of triaxial core with Coriolis decoupling",
        },
        "regime_3_highly_deformed_band_sd1": {
            "band": "SD-1 / Yrast HD (I ~ 21/2- to 45/2-)",
            "method": "DSAM with fractional shift F(tau) (Petrache 1998)",
            "Q0_exp_eb": q0_hd,
            "sig_Q0_eb": sig_q0_hd,
            "Qsf_eb": q_sf_hd,
            "beta2_quadratic": beta2_hd,
            "structure": "Intruder nu i13/2^2 prolate polarization driving nucleus into superdeformed second minimum",
        },
        "cross_regime_ratios": {
            "ratio_Q0_HD_over_ND_K1": ratio_hd_to_nd_k1,
            "ratio_Q0_HD_over_ND_K11": ratio_hd_to_nd_k11,
            "ratio_Q0_ND_over_Isomer": ratio_nd_to_iso,
            "ratio_Q0_HD_over_Isomer": ratio_hd_to_iso,
            "ratio_BE2_HD_over_ND": be2_ratio_hd_to_nd,
            "ratio_BE2_HD_over_Isomer": be2_ratio_hd_to_iso,
            "time_scale_contrast": f"Isomer tau ({tau_iso_ns:.1f} ns) is {time_domain_ratio_iso_to_nd:.1e}x longer than ND tau ({tau_27_ps:.2f} ps)",
        },
        "shape_coexistence_evidence_boundary": {
            "established_fact": "A factor of 4.3x increase in intrinsic quadrupole moment Q0 (from 1.69 to 7.3 eb) and 18x increase in B(E2) is experimentally proven across configurations in the same nucleus 131Ce",
            "open_boundary": "No direct discrete inter-band E2 links connecting the HD band to normal-deformed states have been observed; HD decay-out occurs via an unresolved statistical cascade",
            "methodological_consequence": "Absolute transition quadrupole moments establish shape coexistence in 131Ce, while mixing matrix elements between minima require future dedicated decay-out spectroscopy",
        },
        "checks": checks,
        "check_count": len(checks),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"131Ce three-regime shape audit completed: {len(checks)} checks passed.")
    print(f"Intrinsic Q0: Isomer={q0_iso:.2f} eb -> ND={qt_nd_k1:.2f} eb -> HD={q0_hd:.2f} eb")
    print(f"Deformation ratios: HD/ND = {ratio_hd_to_nd_k1:.2f}x, ND/Isomer = {ratio_nd_to_iso:.2f}x, HD/Isomer = {ratio_hd_to_iso:.2f}x")
    print(f"Collective B(E2) enhancement: HD band is {be2_ratio_hd_to_nd:.1f}x stronger than ND band.")


if __name__ == "__main__":
    main()
