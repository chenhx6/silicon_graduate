#!/usr/bin/env python3
"""Source-bounded odd-A octupole systematics and transparent rotor calculations.

Run with Python 3 standard library. The JSON is recreated beside this script.
Missing odd-actinide transition measurements stay null: no model point is data.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


OUT = Path(__file__).with_suffix(".json")


def clebsch_sq_e1(spin: float, k: float) -> float:
    """|<I K 1 0 | I-1 K>|^2 for an axial strong-coupling rotor."""
    if spin <= k or spin < 1:
        raise ValueError("E1 I->I-1 forbidden for this I,K")
    return (spin * spin - k * k) / (spin * (2 * spin + 1))


def clebsch_sq_e2(spin: float, k: float) -> float:
    """|<I K 2 0 | I-2 K>|^2; final spin must support K."""
    if spin - 2 < k or spin <= 1:
        raise ValueError("E2 I->I-2 forbidden for this I,K")
    return (3 * (spin * spin - k * k) * ((spin - 1) ** 2 - k * k)
            / (2 * spin * (spin - 1) * (2 * spin - 1) * (2 * spin + 1)))


def rotor_ratio(spin: float, k: float, d0_efm: float, q0_efm2: float) -> dict:
    """E1/E2 in fm^-2; D0 and Q0 are rotor intrinsic moments, not measured here."""
    c1, c2 = clebsch_sq_e1(spin, k), clebsch_sq_e2(spin, k)
    be1 = 3 / (4 * math.pi) * d0_efm**2 * c1
    be2 = 5 / (16 * math.pi) * q0_efm2**2 * c2
    return {"spin": spin, "K": k, "CG_E1_sq": c1, "CG_E2_sq": c2,
            "B_E1_e2fm2": be1, "B_E2_e2fm4": be2,
            "B_E1_over_B_E2_fm_minus2": be1 / be2}


def parity_and_coriolis(spin: float, k: float, base_keV: float,
                        tunnel_keV: float, a_plus: float, a_minus: float,
                        rotor_A_keV: float) -> dict:
    """Illustrative two-well rotor; K=1/2 staggering uses (-1)^(I+1/2)."""
    if k != 0.5 or int(spin + 0.5) != spin + 0.5:
        raise ValueError("This decoupling expression requires K=1/2")
    signature = (-1) ** int(spin + 0.5)
    rotational = rotor_A_keV * (spin * (spin + 1) - k * k)
    e_plus = base_keV - tunnel_keV + rotational + rotor_A_keV * a_plus * signature * (spin + 0.5)
    e_minus = base_keV + tunnel_keV + rotational + rotor_A_keV * a_minus * signature * (spin + 0.5)
    return {"spin": spin, "E_plus_keV": e_plus, "E_minus_keV": e_minus,
            "same_spin_delta_keV": e_minus - e_plus,
            "analytic_delta_keV": 2 * tunnel_keV + rotor_A_keV * (a_minus - a_plus) * signature * (spin + 0.5)}


def ph_proxy(low: dict, high: dict) -> float:
    """Independent-particle occupation/gap proxy per unit |<i||Q3||j>|^2.

    This is not BCS/QRPA response: degeneracies, angular matrix elements,
    residual interaction and odd-state self-consistent polarization are absent.
    """
    gap = high["eps_MeV"] - low["eps_MeV"]
    if gap <= 0:
        raise ValueError("Require an ordered positive gap")
    return (low["v2"] - high["v2"]) / gap


def weisskopf_e1_e2fm2(mass: int) -> float:
    """1 W.u. E1 for radius 1.2 A^(1/3) fm; convention stated explicitly."""
    radius_fm = 1.2 * mass ** (1 / 3)
    return (3 / 4) ** 2 * radius_fm**2 / (4 * math.pi)


def build() -> dict:
    # Nomura et al., PRC 97, 024317 (2018), PDF p.3 Table II: spherical
    # constrained SCMF input for odd Ba. These are calculated occupations.
    ba_orbitals = {
        "143Ba": {"2f7/2": {"eps_MeV": 0.443, "v2": 0.173},
                  "1i13/2": {"eps_MeV": 3.333, "v2": 0.020}},
        "145Ba": {"2f7/2": {"eps_MeV": 0.552, "v2": 0.243},
                  "1i13/2": {"eps_MeV": 3.378, "v2": 0.028}},
    }
    ba_proxy = {}
    for nucleus, orbitals in ba_orbitals.items():
        ba_proxy[nucleus] = {"f7_to_i13_gap_MeV": round(orbitals["1i13/2"]["eps_MeV"] - orbitals["2f7/2"]["eps_MeV"], 3),
                             "occupancy_difference": round(orbitals["2f7/2"]["v2"] - orbitals["1i13/2"]["v2"], 3),
                             "ph_proxy_per_unit_Q3_sq_MeV_minus1": round(ph_proxy(orbitals["2f7/2"], orbitals["1i13/2"]), 6)}

    # The following values are explicit scenario inputs, not actinide data.
    scenario = {"name": "illustrative two-channel actinide sensitivity only",
                "input_pairs": [{"kind": "proton f7/2-i13/2", "gap_MeV": 1.5, "occupation_difference": 0.5, "Q3_sq_arbitrary": 1.0},
                                {"kind": "neutron g9/2-j15/2", "gap_MeV": 1.2, "occupation_difference": 0.5, "Q3_sq_arbitrary": 1.0}]}
    scenario["ph_proxy_arbitrary_MeV_minus1"] = round(sum(p["occupation_difference"] * p["Q3_sq_arbitrary"] / p["gap_MeV"] for p in scenario["input_pairs"]), 6)
    scenario["comparison_to_145Ba_single_pair_proxy"] = round(scenario["ph_proxy_arbitrary_MeV_minus1"] / ba_proxy["145Ba"]["ph_proxy_per_unit_Q3_sq_MeV_minus1"], 2)

    nuclei = {}
    for isotope in ["223Ra", "225Ra", "225Ac", "227Ac", "223Th", "221Fr", "223Fr", "143Ba", "145Ba", "143Ce", "145Ce"]:
        nuclei[isotope] = {"same_spin_parity_splitting_keV": None,
                            "B_E1_Wu": None, "D0_efm": None,
                            "status": "primary odd-A level/transition table not established in this audit"}
    # NNDC ENSDF 225088001 ADOPTED LEVELS, GAMMAS, L records and B/G records.
    # This is an evaluated object with original-experiment citations, not a
    # newly measured or independently repeated spectrum. Parentheses matter.
    ra225_levels = [
        {"spin": 0.5, "positive_keV": 0.0, "negative_keV": 55.16, "negative_Jpi_tentative": True},
        {"spin": 1.5, "positive_keV": 42.77, "negative_keV": 31.56, "negative_Jpi_tentative": False},
        {"spin": 2.5, "positive_keV": 25.41, "negative_keV": 120.36, "negative_Jpi_tentative": False},
        {"spin": 3.5, "positive_keV": 111.60, "negative_keV": 69.36, "negative_Jpi_tentative": True},
    ]
    for row in ra225_levels:
        row["same_spin_Eminus_minus_Eplus_keV"] = round(row["negative_keV"] - row["positive_keV"], 2)
    be1_wu, be1_unc_wu = 0.00081, 0.00020
    be1_e2fm2 = be1_wu * weisskopf_e1_e2fm2(225)
    # 3/2- -> 1/2+; both adopted bands carry K=1/2 in the rotor estimate.
    # CG^2=1/3, hence D0^2=4*pi*B(E1). This is model extraction.
    d0 = math.sqrt(be1_e2fm2 * 4 * math.pi / (3 * clebsch_sq_e1(1.5, 0.5)))
    nuclei["225Ra"] = {
        "status": "NNDC ENSDF evaluated-object values; original 1985Is03 experiment not independently reread",
        "source": "NNDC 225088001 ADOPTED LEVELS, GAMMAS, L/G/B records, NDS 110, 1409 (2009)",
        "paired_levels": ra225_levels,
        "B_E1_3over2minus_to_1over2plus_Wu": {"value": be1_wu, "uncertainty": be1_unc_wu,
                                              "gamma_keV": 31.50, "ENSDF_record": "L31.56/G31.50/B"},
        "D0_efm_conditional_rotor": {"value": round(d0, 4),
                                        "linearized_uncertainty": round(d0 * be1_unc_wu / (2 * be1_wu), 4),
                                        "K": 0.5, "Weisskopf_E1_e2fm2": round(weisskopf_e1_e2fm2(225), 6),
                                        "assumption": "axial K=1/2 rotor; same intrinsic D0 for cross-parity transition"},
        "B_E1_over_B_E2": None,
        "ratio_note": "No matched E2 transition from the same 31.56-keV initial level in extracted records."
    }

    return {
        "title": "Odd-A reflection asymmetry: bounded source data and conditional calculations",
        "classification_note": "Ba and Ra are alkaline-earth elements, Fr is alkali, Ce is lanthanide, and Ac/Th are actinides. Comparisons are by mass region.",
        "theory": {
            "two_well_hamiltonian": "H_I = [E_rot(I)+epsilon_q, -t_I; -t_I, E_rot(I)+epsilon_q] in mirror-localized states; parity projection gives E_±=E_rot+epsilon_q∓t_I if overlap is neglected.",
            "finite_overlap": "For normalized mirror states with overlap s_I and Hamiltonian diagonal h_I, off-diagonal v_I: E_±=(h_I±v_I)/(1±s_I); these replace a universal 2t_I splitting.",
            "decoupling": "For K=1/2, E_p(I)=E0_p+A_p[I(I+1)-1/4+a_p(-1)^(I+1/2)(I+1/2)]. Generalized a_p uses parity-projected Coriolis matrix elements and overlap normalization; the bare intrinsic expression alone is not an observable.",
            "splitting": "At identical I and common A, ΔE(I)=2t_I+A(a_−−a_+)(-1)^(I+1/2)(I+1/2); with differing A or bandheads include their differences. If parity branches have different observed I, use an interpolated parity displacement instead.",
            "rotor_strengths": "B(E1)=3D0²/(4π)|<I K 1 0|I−1 K>|²; B(E2)=5Q0²/(16π)|<I K 2 0|I−2 K>|²; ratio=(12/5)(D0/Q0)²(CG1²/CG2²), in fm^−2 for D0[e fm], Q0[e fm²].",
            "BCS_response": "χ3(0)∝Σ_ij 2|Q3_ij|²(u_i v_j+v_i u_j)²/(E_i+E_j), with convention-dependent degeneracy factors; blocking must remove or modify specific magnetic-substate channels and recompute pairing/mean field."
        },
        "source_benchmarks": {
            "144Ba": {"B_E3_down_Wu": 48, "lower": 34, "upper": 25, "kind": "experiment", "source": "Bucher et al. PRL 116, 112503 (2016), Table I"},
            "146Ba": {"B_E3_down_Wu": 48, "lower": 29, "upper": 21, "kind": "experiment", "source": "Bucher et al. PRL 118, 152504 (2017), Table I"},
            "odd_Ba": {"kind": "model", "source": "Nomura et al. PRC 97, 024317 (2018), PDF pp.7–10 Tables V–IX", "result": "Most low-lying odd-Ba states have small f-boson content; selected higher states carry E3 strength. No measured universal blocking factor."}
        },
        "odd_A_nucleus_audit": nuclei,
        "ba_model_orbitals": ba_orbitals,
        "ba_ph_proxy": ba_proxy,
        "actinide_sensitivity_scenario": scenario,
        "rotor_ratio_example": rotor_ratio(4.5, 0.5, 0.1, 600.0),
        "parity_staggering_example": [parity_and_coriolis(i, 0.5, 0.0, 25.0, -0.20, 0.10, 5.0) for i in [2.5, 3.5, 4.5, 5.5]],
        "inference_limits": ["B(E1)/B(E2) depends on D0 cancellation, Q0, K mixing, branching, conversion and lifetimes; no universal static-shape threshold.",
                             "Strong E3 in even Ba cannot determine the odd-neighbor ground-state parity structure.",
                             "No empirical actinide/lanthanide response ratio can be obtained without matched quasiparticle spectra, pairing and octupole matrix elements."]
    }


if __name__ == "__main__":
    OUT.write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT)
