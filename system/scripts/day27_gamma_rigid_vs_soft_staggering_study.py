#!/usr/bin/env python3
"""Reproduce source-defined S(4) limits; quarantine unverified isotope inputs."""

import argparse
import hashlib
import json
from datetime import datetime
from fractions import Fraction
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np

# Historical inputs are preserved for arithmetic replay only. Their isotope
# energies, band assignments and shape labels have not been verified here.
# Nucleus, Z, A, regime, E(2+_1), E(2+_gamma), E(3+_gamma), E(4+_gamma), Coulex_proven_triaxial
# Historical citation attributions below are not verified input locators:
# 76Ge: Ayangeakaa et al. PRL 123, 102501 (2019); NNDC ENSDF
# 76Se: NNDC ENSDF; McCutchan et al. PRC 76, 024306 (2007)
# 104Ru, 106Ru, 108Ru, 110Ru: NNDC ENSDF; Srebrny et al. NPA 766, 25 (2006)
# 134Ba: Casten & von Brentano PLB 152, 22 (1985); NNDC ENSDF
# 196Pt: Cizewski et al. PRL 40, 167 (1978); NNDC ENSDF
LEGACY_UNVERIFIED_INPUTS = [
    {
        "nucleus": "76Ge", "Z": 32, "A": 76, "region": "A~76 Germanium-Selenium",
        "E_2p_1_keV": 562.9, "E_2p_g_keV": 1108.3, "E_3p_g_keV": 1911.2, "E_4p_g_keV": 2026.0,
        "gamma_coulex_deg": 28.0, "coulex_nature": "Rigid Triaxial (CH88 invariant analysis)"
    },
    {
        "nucleus": "76Se", "Z": 34, "A": 76, "region": "A~76 Germanium-Selenium",
        "E_2p_1_keV": 559.1, "E_2p_g_keV": 1216.1, "E_3p_g_keV": 1787.6, "E_4p_g_keV": 2383.5,
        "gamma_coulex_deg": 25.0, "coulex_nature": "Gamma-Soft / Transitional"
    },
    {
        "nucleus": "104Ru", "Z": 44, "A": 104, "region": "A~104-110 Ruthenium Chain",
        "E_2p_1_keV": 358.0, "E_2p_g_keV": 888.5, "E_3p_g_keV": 1242.0, "E_4p_g_keV": 1515.2,
        "gamma_coulex_deg": 26.5, "coulex_nature": "Rigid-Leaning Triaxial Rotor"
    },
    {
        "nucleus": "106Ru", "Z": 44, "A": 106, "region": "A~104-110 Ruthenium Chain",
        "E_2p_1_keV": 270.1, "E_2p_g_keV": 792.2, "E_3p_g_keV": 1097.0, "E_4p_g_keV": 1390.0,
        "gamma_coulex_deg": 25.0, "coulex_nature": "Critical Phase Boundary (S(4) ~ 0)"
    },
    {
        "nucleus": "108Ru", "Z": 44, "A": 108, "region": "A~104-110 Ruthenium Chain",
        "E_2p_1_keV": 242.2, "E_2p_g_keV": 707.9, "E_3p_g_keV": 975.0, "E_4p_g_keV": 1380.0,
        "gamma_coulex_deg": 24.0, "coulex_nature": "Gamma-Soft Vibrator"
    },
    {
        "nucleus": "110Ru", "Z": 44, "A": 110, "region": "A~104-110 Ruthenium Chain",
        "E_2p_1_keV": 240.8, "E_2p_g_keV": 613.2, "E_3p_g_keV": 989.4, "E_4p_g_keV": 1475.0,
        "gamma_coulex_deg": 23.0, "coulex_nature": "Gamma-Soft Vibrator"
    },
    {
        "nucleus": "134Ba", "Z": 56, "A": 134, "region": "A~130-138 Barium-Xenon",
        "E_2p_1_keV": 604.7, "E_2p_g_keV": 1167.9, "E_3p_g_keV": 1643.3, "E_4p_g_keV": 2371.3,
        "gamma_coulex_deg": 27.0, "coulex_nature": "Prototypical O(6) Gamma-Soft Rotor"
    },
    {
        "nucleus": "196Pt", "Z": 78, "A": 196, "region": "A~196 Platinum Benchmark",
        "E_2p_1_keV": 355.7, "E_2p_g_keV": 688.7, "E_3p_g_keV": 1015.0, "E_4p_g_keV": 1604.5,
        "gamma_coulex_deg": 30.0, "coulex_nature": "Textbook O(6) Dynamical Symmetry (Wilets-Jean)"
    }
]

def calculate_s4(e_2p1, e_2pg, e_3pg, e_4pg):
    """
    Signature staggering parameter S(4):
    S(4) = {[E(4+_gamma) - E(3+_gamma)] - [E(3+_gamma) - E(2+_gamma)]} / E(2+_1)
    """
    diff_43 = e_4pg - e_3pg
    diff_32 = e_3pg - e_2pg
    return (diff_43 - diff_32) / e_2p1

def rotor_levels(spin, gamma_deg):
    """Diagonalize sum(I_k**2 / J_k) in the even-even D2 symmetric basis.

    J_k = sin(gamma - 2*pi*k/3)**2. A common energy scale cancels in S(4).
    Even K is used; K=0 exists only for even spin, while K>0 uses
    (|K> + (-1)**I |-K>)/sqrt(2). No actual nucleus is fitted.
    """
    if spin < 0 or int(spin) != spin:
        raise ValueError("spin must be a nonnegative integer")
    if not 0.0 < gamma_deg < 60.0:
        raise ValueError("axial endpoints have singular irrotational inertias")
    m_values = np.arange(-spin, spin + 1)
    raising = np.zeros((2 * spin + 1, 2 * spin + 1))
    for i, m in enumerate(m_values[:-1]):
        raising[i + 1, i] = np.sqrt(spin * (spin + 1) - m * (m + 1))
    ix = (raising + raising.T) / 2.0
    iy = (raising - raising.T) / (2.0j)
    iz = np.diag(m_values)
    gamma = np.radians(gamma_deg)
    inertias = np.sin(gamma - 2.0 * np.pi * np.arange(3) / 3.0) ** 2
    hamiltonian = ix @ ix / inertias[0] + iy @ iy / inertias[1] + iz @ iz / inertias[2]
    basis = []
    for k in range(0, spin + 1, 2):
        if k == 0 and spin % 2:
            continue
        state = np.zeros(2 * spin + 1)
        if k == 0:
            state[spin] = 1.0
        else:
            state[spin + k] = 1.0 / np.sqrt(2.0)
            state[spin - k] = (-1) ** spin / np.sqrt(2.0)
        basis.append(state)
    if not basis:
        raise ValueError("no even-even D2 symmetric state at this spin")
    transform = np.array(basis).T
    reduced = transform.conj().T @ hamiltonian @ transform
    if not np.allclose(reduced, reduced.conj().T, atol=1e-12):
        raise ArithmeticError("rotor Hamiltonian is not Hermitian")
    return np.linalg.eigvalsh(reduced)


def davydov_filippov_analytical_s4(gamma_deg):
    """Compatibility entry: numerical D2 rotor, replacing the old fitted curve."""
    e2 = rotor_levels(2, gamma_deg)
    e3 = rotor_levels(3, gamma_deg)
    e4 = rotor_levels(4, gamma_deg)
    return float(calculate_s4(e2[0], e2[1], e3[0], e4[1]))


def wilets_jean_o6_s4(c_over_b=0.0):
    """Eq.(4): E=B*tau*(tau+3)+C*I*(I+1); gamma band tau=2,3,3."""
    if c_over_b < 0.0:
        raise ValueError("this demonstration restricts C/B to nonnegative values")
    e21 = 4.0 + 6.0 * c_over_b
    e2g = 10.0 + 6.0 * c_over_b
    e3g = 18.0 + 12.0 * c_over_b
    e4g = 18.0 + 20.0 * c_over_b
    return float(calculate_s4(e21, e2g, e3g, e4g))


def run_study(output_path=None):
    root = Path(__file__).resolve().parents[2]
    source_page = root / "knowledge/sources/zamfir-casten-1991-gamma-softness-triaxiality.md"
    import re
    source_text = source_page.read_text(encoding="utf-8-sig")
    raw_match = re.search(r'^raw_file: "([^"\n]+)"', source_text, re.MULTILINE)
    hash_match = re.search(r"^raw_sha256: ([A-Fa-f0-9]+)", source_text, re.MULTILINE)
    if raw_match is None or hash_match is None:
        raise ValueError("source raw identity is missing")
    raw = root / raw_match.group(1)
    observed_hash = hashlib.sha256(raw.read_bytes()).hexdigest()
    if observed_hash.lower() != hash_match.group(1).lower():
        raise ValueError("source raw hash differs from the recorded identity")

    e2 = rotor_levels(2, 30.0)
    e3 = rotor_levels(3, 30.0)
    e4 = rotor_levels(4, 30.0)
    numeric_rigid = davydov_filippov_analytical_s4(30.0)
    numeric_soft = wilets_jean_o6_s4()
    rigid_exact = Fraction(17, 3) - 2 * Fraction(3) + Fraction(2)
    soft_exact = Fraction(9, 2) - 2 * Fraction(9, 2) + Fraction(5, 2)
    checks = {
        "d2_rotor_vs_source_normalized_energies": bool(np.allclose(
            [e2[1] / e2[0], e3[0] / e2[0], e4[1] / e2[0]], [2, 3, 17 / 3], atol=1e-12)),
        "rigid_s4_vs_exact_5_over_3": abs(numeric_rigid - float(rigid_exact)) < 1e-12,
        "soft_s4_vs_exact_minus_2": abs(numeric_soft - float(soft_exact)) < 1e-12,
        "o5_plus_o3_zero_at_c_over_b_4": abs(wilets_jean_o6_s4(4)) < 1e-12,
        "o5_plus_o3_positive_at_c_over_b_6": wilets_jean_o6_s4(6) > 0,
    }
    if not all(checks.values()):
        raise ArithmeticError(f"independent model-limit checks failed: {checks}")

    legacy_rows = []
    for d in LEGACY_UNVERIFIED_INPUTS:
        legacy_rows.append({
            "nucleus": d["nucleus"],
            "input_status": "legacy-unverified-no-experimental-certification",
            "input_energies_keV": {k: d[k] for k in [
                "E_2p_1_keV", "E_2p_g_keV", "E_3p_g_keV", "E_4p_g_keV"]},
            "s4_arithmetic_only": calculate_s4(
                d["E_2p_1_keV"], d["E_2p_g_keV"], d["E_3p_g_keV"], d["E_4p_g_keV"]),
            "shape_classification": None,
            "band_assignments_verified": False,
            "coulex_gamma_verified": False,
        })

    results = {
        "schema_version": 2,
        "observed_at": datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(),
        "investigation": "Source correction of S(4) signs and model limits",
        "scientific_status": "source-limit-reproduced; isotope-classifications-withdrawn",
        "source": {"knowledge": source_page.relative_to(root).as_posix(),
                   "claim_ids": ["ZC91-1", "ZC91-2", "ZC91-4", "ZC91-D22-R091-1"],
                   "raw_file": raw.relative_to(root).as_posix(), "raw_sha256": observed_hash,
                   "reading_scope": "PDF1-4 text, PDF3 visual; printed265-268, Eq2/Eq4/Fig1/Fig2"},
        "formula": "(E4_gamma - 2*E3_gamma + E2_gamma)/E2_ground",
        "model_limits": {
            "wilets_jean_C_equals_0": {"normalized_E2g_E3g_E4g": [2.5, 4.5, 4.5],
                                     "s4_exact": str(soft_exact), "s4_numeric": numeric_soft,
                                     "grouping": "(2),(3,4),(5,6)"},
            "davydov_gamma_30": {"normalized_E2g_E3g_E4g": [2.0, 3.0, 17 / 3],
                                 "s4_exact": str(rigid_exact), "s4_numeric": numeric_rigid,
                                 "grouping": "(2,3),(4,5),(6,7)"},
        },
        "rotor_angle_scan_model_only": [{"gamma_deg": g,
            "s4": davydov_filippov_analytical_s4(g)} for g in [5, 10, 15, 20, 25, 30]],
        "gamma_independent_o5_plus_o3_demonstration": {
            "derivation_kind": "task-derived from source Eq4; not an isotope fit",
            "formula": "S4=(-8+2*C/B)/(4+6*C/B)",
            "rows": [{"c_over_b": c, "s4": wilets_jean_o6_s4(c)} for c in [0, 0.25, 1, 4, 6]],
            "boundary": "large C/B is synthetic; source says empirical C is small; zero S4 is no universal phase boundary",
        },
        "legacy_unverified_inputs_arithmetic_replay": legacy_rows,
        "withdrawn": ["negative S4 certifies rigid triaxiality", "positive S4 certifies gamma softness",
                      "S4=0 certifies a Ru-chain phase transition", "legacy isotope inputs are verified ENSDF data"],
        "checks": checks,
        "no_experimental_confidence_or_curriculum_credit": True,
    }
    if output_path is None:
        output_path = root / (
            "outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/"
            "continuation-studies/gamma-rigid-vs-soft/gamma_rigid_vs_soft_corrected_results.json")
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(results, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(output_path), "rigid_s4": numeric_rigid,
                      "soft_s4": numeric_soft, "checks": checks,
                      "legacy_isotope_rows": len(legacy_rows),
                      "isotope_classifications": "withdrawn"}, indent=2))
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    run_study(parser.parse_args().output)
