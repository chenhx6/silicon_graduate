#!/usr/bin/env python3
"""Audit of A≈130 collectivity systematics: ND vs HD bands, band crossings, and rate compensation.

Audits:
1. Ground/normal-deformed (ND) vs intruder-driven highly deformed (HD) collectivity in 131Ce and 134Nd;
2. Universal prolate polarization by nu i13/2 across Ce and Nd isotopes (Petrache 1998, Singh 2016);
3. Wave-function fragmentation vs static collapse at band crossings (134Nd Klemme 1999, 136Sm Babra 2019);
4. Chiral partner collectivity vs lifetime divergence and rate compensation (135Nd Mukhopadhyay 2007);
5. Mathematical boundaries of rotor geometry and the two-fold ambiguity in gamma extraction.

Requires --output PATH. Uses only Python standard library.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path


def weighted_mean_and_error(values, errors):
    weights = [1.0 / (e ** 2) for e in errors]
    sum_w = sum(weights)
    mean_val = sum(w * v for w, v in zip(weights, values)) / sum_w
    mean_err = 1.0 / math.sqrt(sum_w)
    return mean_val, mean_err


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Output JSON path")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    checks = []

    def check(name, ok):
        checks.append({"name": name, "passed": bool(ok)})
        if not ok:
            raise AssertionError(f"Check failed: {name}")

    # 1. Verify source raw files
    raw_singh = root / "raw/papers/2016_Singh et al_Lifetime measurements in the yrast band of the gamma-soft nuclei 131Ce and 133Pr.pdf"
    raw_petrache = root / "raw/papers/1998_Petrache et al_Lifetime measurements of highly deformed bands in 1 3 4 , 1 3 5 Nd and 131 Ce.pdf"
    raw_babra = root / "raw/papers/2019_Babra et al_Investigation of a large change in deformation for the γ -soft nucleus Sm 136.pdf"
    raw_klemme = root / "raw/papers/1999_Klemme et al_Lifetimes measurements for 134 Nd and neighboring nuclei with the.pdf"
    raw_mukhopadhyay = root / "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/三轴/手征/2007_Mukhopadhyay et al_From Chiral Vibration to Static Chirality in Nd 135.pdf"

    check("Singh 2016 raw verified", hashlib.sha256(raw_singh.read_bytes()).hexdigest() == "95e0831b9864a58fd1a896a1b20e227d88d9b7aa5de56c738c3792441caa1a30")
    check("Petrache 1998 raw verified", hashlib.sha256(raw_petrache.read_bytes()).hexdigest() == "9d2297ed085012d2f8633a5faecfa7020cbca96ac06cf2eb5e88d97a24b90e5f")
    check("Babra 2019 raw verified", hashlib.sha256(raw_babra.read_bytes()).hexdigest() == "a26149bff0e7b3bdb5459ba5897b69bc7f8ed17a646f13ed59dd5b38ae425ba6")
    check("Klemme 1999 raw verified", hashlib.sha256(raw_klemme.read_bytes()).hexdigest() == "2a6dfcdac12de9dbf61b2a63c274aed8e286249a3dd28d1a2c6c5a46f1c00604")
    check("Mukhopadhyay 2007 raw verified", hashlib.sha256(raw_mukhopadhyay.read_bytes()).hexdigest() == "9eccc9c2ad02cc10735d1aad0d76eb2fd8af0a4acc814bcaab8099f50e748425")

    # 2. 131Ce: ND collectivity vs HD collectivity step
    # ND yrast band (Singh 2016 Table 1, 4 finite points: 15/2-, 27/2-, 31/2-, 35/2-)
    ce131_nd_spins = [7.5, 13.5, 15.5, 17.5]
    ce131_nd_qt = [2.93, 2.26, 2.66, 2.43] # eb
    ce131_nd_qt_err = [(0.3 + 0.6) / 2.0, (0.23 + 0.37) / 2.0, (0.12 + 0.13) / 2.0, (0.20 + 0.22) / 2.0] # [0.45, 0.30, 0.125, 0.21]
    ce131_nd_mean, ce131_nd_mean_err = weighted_mean_and_error(ce131_nd_qt, ce131_nd_qt_err)
    check("131Ce ND weighted mean Qt is ~2.58 eb", math.isclose(ce131_nd_mean, 2.579, abs_tol=0.01))

    # HD yrast band (Petrache 1998 Table I)
    ce131_hd_q0 = 7.3 # eb
    ce131_hd_q0_err = 0.4 # eb
    ce131_hd_beta2 = 0.38
    ce131_hd_beta2_err = 0.02
    step_ratio_ce131 = ce131_hd_q0 / ce131_nd_mean
    check("131Ce HD/ND collectivity step ratio is ~2.83", math.isclose(step_ratio_ce131, 2.831, abs_tol=0.02))

    # 3. 134Nd: ND ground-state collectivity vs HD collectivity
    # Klemme 1999 Table II: 2+ -> 0+
    nd134_2plus_qt = 4.32 # eb
    nd134_2plus_qt_err = 0.07 # eb
    # Petrache 1998 Table I: 134Nd yrast HD
    nd134_hd_q0 = 6.8 # eb
    nd134_hd_q0_err = 0.3 # eb
    step_ratio_134nd = nd134_hd_q0 / nd134_2plus_qt
    check("134Nd HD / ND(2+) collectivity step ratio is ~1.57", math.isclose(step_ratio_134nd, 1.574, abs_tol=0.02))

    # 4. Universal HD band quadrupole moment across A~130 (Petrache 1998 Table I)
    hd_bands = [
        {"nucleus": "131Ce", "Z": 58, "N": 73, "band": "yrast_HD", "Q0": 7.3, "Q0_err": 0.4, "beta2": 0.38},
        {"nucleus": "132Ce", "Z": 58, "N": 74, "band": "yrast_HD", "Q0": 7.4, "Q0_err": 0.3, "beta2": 0.38},
        {"nucleus": "134Nd", "Z": 60, "N": 74, "band": "yrast_HD", "Q0": 6.8, "Q0_err": 0.3, "beta2": 0.35},
        {"nucleus": "135Nd", "Z": 60, "N": 75, "band": "yrast_HD", "Q0": 7.3, "Q0_err": 1.0, "beta2": 0.37},
    ]
    hd_q0_values = [b["Q0"] for b in hd_bands]
    hd_q0_mean = sum(hd_q0_values) / len(hd_q0_values)
    check("Universal intruder-driven HD quadrupole moment across Ce and Nd is ~7.2 eb",
          math.isclose(hd_q0_mean, 7.20, abs_tol=0.05))

    # 5. Band-crossing transition quadrupole moment suppression: 134Nd and 136Sm
    # 134Nd 10S2 -> 8g crossing (Klemme 1999 Table II)
    qt_134nd_crossing = 0.51 # eb
    drop_factor_134nd = qt_134nd_crossing / nd134_2plus_qt
    check("134Nd 10S2->8g crossing drops apparent Qt by factor of ~8.5",
          math.isclose(drop_factor_134nd, 0.51 / 4.32, rel_tol=1e-3) and drop_factor_134nd < 0.15)

    # 136Sm band crossing step (Babra 2019 Table I)
    sm136_pre_qt = [5.66, 5.59, 5.70] # 8+, 10+, 12+
    sm136_pre_err = [0.19, 0.785, 0.205]
    sm136_post_qt = [5.38, 4.85, 5.05] # 14+, 16+, 18+
    sm136_post_err = [0.335, 0.33, 0.35]
    sm136_mean_pre, _ = weighted_mean_and_error(sm136_pre_qt, sm136_pre_err)
    sm136_mean_post, _ = weighted_mean_and_error(sm136_post_qt, sm136_post_err)
    sm136_delta_pct = (sm136_mean_post - sm136_mean_pre) / sm136_mean_pre * 100.0
    check("136Sm post-crossing Qt drops by ~10.3%", math.isclose(sm136_delta_pct, -10.28, abs_tol=0.1))

    # 6. 135Nd chiral partner rate compensation (Mukhopadhyay 2007 Table I)
    mu07_spins = ["31/2-", "33/2-", "35/2-", "37/2-", "39/2-"]
    mu07_tau_a = [0.75, 0.44, 0.28, 0.23, 0.22] # ps
    mu07_tau_b = [1.46, 0.87, 0.64, 0.48, 0.24] # ps (Table I)
    mu07_be2_a = [0.32, 0.32, 0.32, 0.32, 0.13] # e^2 b^2
    mu07_be2_b = [0.28, 0.28, 0.28, 0.29, 0.11] # e^2 b^2
    tau_ratios_b_over_a = [tb / ta for ta, tb in zip(mu07_tau_a, mu07_tau_b)]
    be2_ratios_b_over_a = [eb / ea for ea, eb in zip(mu07_be2_a, mu07_be2_b)]
    check("135Nd Band B/A lifetime ratio is ~2.0 in 31/2- to 37/2-",
          all(1.90 <= r <= 2.35 for r in tau_ratios_b_over_a[:4]))
    check("135Nd Band B/A B(E2) ratio is ~0.88-0.91",
          all(0.85 <= r <= 0.92 for r in be2_ratios_b_over_a[:4]))

    # 7. Rotor geometry and two-fold ambiguity in gamma extraction (Singh Eq. 5)
    def gamma_factor(gamma_deg):
        return math.cos(math.radians(gamma_deg + 30.0)) / math.cos(math.radians(30.0))

    check("gamma = +20 deg and -80 deg yield identical factor 0.7422",
          math.isclose(gamma_factor(20.0), gamma_factor(-80.0), rel_tol=1e-12)
          and math.isclose(gamma_factor(20.0), 0.742227, abs_tol=1e-5))

    # Formulate output artifact
    result = {
        "kind": "A~130 nuclear collectivity systematics and boundary audit",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "normal_vs_highly_deformed_collectivity": {
            "131Ce": {
                "ND_yrast_mean_Qt_eb": round(ce131_nd_mean, 3),
                "ND_yrast_mean_Qt_err_eb": round(ce131_nd_mean_err, 3),
                "HD_yrast_Q0_eb": ce131_hd_q0,
                "HD_yrast_Q0_err_eb": ce131_hd_q0_err,
                "step_ratio_HD_over_ND": round(step_ratio_ce131, 3),
                "microscopic_origin": "Occupation of nu i13/2 intruder orbital [660]1/2+ induces strong prolate core polarization",
            },
            "134Nd": {
                "ND_ground_2+_Qt_eb": nd134_2plus_qt,
                "ND_ground_2+_Qt_err_eb": nd134_2plus_qt_err,
                "HD_yrast_Q0_eb": nd134_hd_q0,
                "HD_yrast_Q0_err_eb": nd134_hd_q0_err,
                "step_ratio_HD_over_ND_2plus": round(step_ratio_134nd, 3),
            },
            "universal_HD_Q0_plateau": {
                "bands": hd_bands,
                "mean_Q0_eb": round(hd_q0_mean, 2),
                "interpretation": "A~130 HD bands exhibit a remarkably constant Q0 ~ 7.2 eb across Z=58-60, stabilizing high deformation",
            },
        },
        "band_crossing_matrix_element_attenuation": {
            "134Nd_10S2_to_8g": {
                "crossing_Qt_eb": qt_134nd_crossing,
                "ground_2+_Qt_eb": nd134_2plus_qt,
                "attenuation_factor": round(drop_factor_134nd, 3),
                "mechanism": "Wave-function mismatch between ground band and aligned S-band fragments E2 strength",
            },
            "136Sm_yrast_crossing": {
                "mean_pre_crossing_Qt_eb": round(sm136_mean_pre, 3),
                "mean_post_crossing_Qt_eb": round(sm136_mean_post, 3),
                "drop_pct": round(sm136_delta_pct, 1),
                "mechanism": "Moderate two-band mixing across crossing explains step without static shape collapse",
            },
        },
        "chiral_partner_collectivity_and_rate_compensation": {
            "nucleus": "135Nd",
            "source": "Mukhopadhyay 2007 Table I",
            "spins": mu07_spins,
            "tau_ratios_B_over_A": [round(r, 3) for r in tau_ratios_b_over_a],
            "be2_ratios_B_over_A": [round(r, 3) for r in be2_ratios_b_over_a],
            "physical_law": "Electromagnetic collectivity symmetry (B(E2) ~ 0.88-0.91) is compatible with level lifetime asymmetry (tau_B/tau_A ~ 2.0) via branching ratio and E_gamma^5 compensation",
        },
        "rotor_geometry_and_ambiguity_boundary": {
            "Lund_convention_formula": "Qt = Q20 * cos(gamma + 30 deg) / cos(30 deg)",
            "two_fold_gamma_ambiguity": {
                "example_solutions": ["gamma = +20 deg", "gamma = -80 deg"],
                "identical_geometric_factor": round(gamma_factor(20.0), 4),
                "boundary": "Single transition quadrupole moment Qt cannot distinguish prolate-triaxial from oblate-triaxial without spectroscopic Qs or interband rates",
            },
        },
        "checks": checks,
        "all_checks_passed": all(c["passed"] for c in checks),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"output": str(args.output), "controls": len(checks), "all_passed": result["all_checks_passed"]}))


if __name__ == "__main__":
    raise SystemExit("Retired checkpoint039: use day20_crossband_attribution039.py; legacy scientific certification withdrawn.")
