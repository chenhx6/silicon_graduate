#!/usr/bin/env python3
"""Two-cluster E1/E3 geometry and a parity/GDR mixing counterexample.

This is an analytic benchmark, not an antisymmetrized microscopic cluster
calculation, a fitted spectrum, or a reanalysis of experimental yields.
Distances and mixing parameters below are illustrative unless explicitly
tagged as a published matrix element. Only the Python standard library is used.

With r1-r2=R and A1*r1+A2*r2=0, r1=A2*R/A and r2=-A1*R/A.
Consequently D/e=(Z1*A2-Z2*A1)*R/A. The point-cluster E3 operator is
M30=e*sqrt(7/4pi)*[Z1*(A2/A)^3-Z2*(A1/A)^3]*R^3.
The K=0 rotor convention Q3=sqrt(16pi/7)*M30 gives Q3=2e*c3*R^3.
This E3 normalization reproduces B(E3;0+->3-)=7*Q3^2/(16pi).

For a two-state low mode/GDR Hamiltonian [[Elow,v],[v,EGDR]],
|low'>=cos(theta)|low>-sin(theta)|GDR>, theta=atan(2v/Delta)/2.
The E1 amplitude is coherent only because the states mix into one final
eigenstate; an extrapolated GDR strength cannot itself be subtracted from
an unrelated observed B(E1).
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


CASES = (
    ("20Ne", 16, 8, 4, 2),
    ("144Ba", 140, 54, 4, 2),
    ("146Ba", 142, 54, 4, 2),
    ("224Ra", 220, 86, 4, 2),
    ("226Ra", 222, 86, 4, 2),
)


def cluster_geometry(label: str, a1: int, z1: int, a2: int, z2: int) -> dict:
    """Dimensionless E1 and E3 coefficients for two point charges."""
    a = a1 + a2
    c1 = (z1 * a2 - z2 * a1) / a
    c3 = z1 * (a2 / a) ** 3 - z2 * (a1 / a) ** 3
    r1, r2 = a2 / a, -a1 / a
    assert math.isclose(a1 * r1 + a2 * r2, 0, abs_tol=1e-12)
    assert math.isclose(z1 * r1 + z2 * r2, c1, abs_tol=1e-12)
    assert (c1 == 0) == (z1 * a2 == z2 * a1)
    return {
        "nucleus": label,
        "core": {"A": a1, "Z": z1},
        "alpha": {"A": a2, "Z": z2},
        "Z_over_A_core": z1 / a1,
        "Z_over_A_alpha": z2 / a2,
        "c1_D0_per_eR": c1,
        "c3_Q3_per_2eR3": c3,
        "D0_at_R8_fm_efm": 8 * c1,
        "Q3_at_R8_fm_efm3": 2 * c3 * 8**3,
    }


def e1_e3_from_published_matrix_elements() -> dict:
    """146Ba Table I central rounded amplitudes; same upward direction."""
    m1_eb_half = 0.000223  # Bucher 2017, Table I, 0+ -> 1-.
    m3_eb_three_halves = 0.65  # Bucher 2017, Table I, 0+ -> 3-.
    m1_efm = m1_eb_half * 10  # sqrt(b)=10 fm.
    m3_efm3 = m3_eb_three_halves * 1000  # b^(3/2)=1000 fm^3.
    b1_up = m1_efm**2  # Ji=0.
    b3_up = m3_efm3**2  # Ji=0.
    d0_k0 = m1_efm * math.sqrt(4 * math.pi / 3)
    q3_k0 = m3_efm3 * math.sqrt(16 * math.pi / 7)
    row = cluster_geometry("146Ba", 142, 54, 4, 2)
    r_from_q3 = (abs(q3_k0 / (2 * row["c3_Q3_per_2eR3"]))) ** (1 / 3)
    pure_cluster_d = abs(row["c1_D0_per_eR"] * r_from_q3)
    # If one point-cluster channel had the same nonnegative matrix-element
    # overlap weight w for both operators, Dobs=w*c1*R and Qobs=2*w*c3*R^3.
    # At R fixed by the E3 value with w=1, E1 asks for a much smaller w.
    w_at_fixed_r = d0_k0 / pure_cluster_d
    b3_if_same_weight = (w_at_fixed_r * m3_efm3) ** 2
    # If R and w are both free, there IS an exact algebraic solution.
    # It must be checked against nuclear-scale localization separately.
    r_joint = math.sqrt(q3_k0 * abs(row["c1_D0_per_eR"])
                        / (2 * abs(row["c3_Q3_per_2eR3"]) * d0_k0))
    w_joint = d0_k0 / (abs(row["c1_D0_per_eR"]) * r_joint)
    contact_r = 1.2 * (142 ** (1 / 3) + 4 ** (1 / 3))
    assert math.isclose(w_joint * abs(row["c1_D0_per_eR"]) * r_joint,
                        d0_k0, rel_tol=1e-12)
    assert math.isclose(2 * w_joint * abs(row["c3_Q3_per_2eR3"])
                        * r_joint**3, q3_k0, rel_tol=1e-12)
    assert b1_up >= 0 and b3_up > 0
    return {
        "source": "Bucher_2017, PRL 118 152504, PDF p.3 Table I; rounded central values",
        "observables": {
            "M_E1_0_to_1_eb_half": m1_eb_half,
            "M_E3_0_to_3_eb_three_halves": m3_eb_three_halves,
            "B_E1_0_to_1_e2fm2": b1_up,
            "B_E3_0_to_3_e2fm6": b3_up,
            "B_E1_over_B_E3_same_upward_fm_minus4": b1_up / b3_up,
            "D0_abs_K0_rotor_efm": d0_k0,
            "Q3_abs_K0_rotor_efm3": q3_k0,
        },
        "conditional_point_cluster_example": {
            "R_from_E3_fm": r_from_q3,
            "pure_cluster_D0_abs_efm": pure_cluster_d,
            "w_E1_required_at_E3_fixed_R": w_at_fixed_r,
            "B_E3_up_if_same_weight_e2fm6": b3_if_same_weight,
            "B_E3_up_observed_over_that_prediction": b3_up / b3_if_same_weight,
            "joint_solution_R_if_R_and_w_free_fm": r_joint,
            "joint_solution_common_transition_weight_w": w_joint,
            "illustrative_contact_R_fm_r0_1p2": contact_r,
            "joint_R_over_contact_R": r_joint / contact_r,
            "status": "the algebra has a joint solution at a far-separated R; w is a common transition overlap assumption, not measured S_alpha or a general spectroscopic factor",
        },
    }


def ra224_published_e3_comparison() -> dict:
    """Gaffney 2013 E3 central value versus point-cluster geometry."""
    m3_up = 940.0  # e fm^3, 0+ -> 3-, Gaffney Table 1.
    q3 = m3_up * math.sqrt(16 * math.pi / 7)
    row = cluster_geometry("224Ra", 220, 86, 4, 2)
    r = (q3 / abs(2 * row["c3_Q3_per_2eR3"])) ** (1 / 3)
    return {
        "source": "Gaffney_2013, Nature 497 199-204, Table 1; rounded central value",
        "M_E3_0_to_3_efm3": m3_up,
        "Q3_abs_K0_rotor_efm3": q3,
        "R_if_point_cluster_only_fm": r,
        "point_cluster_D0_abs_at_that_R_efm": abs(row["c1_D0_per_eR"] * r),
        "status": "E3-matched geometric illustration; no E1 or alpha probability inference",
    }


def parity_displacement(rot_a_mev: float, offset_mev: float) -> dict:
    """E+(I)=a I(I+1); E-(I)=a I(I+1)+offset, odd I sampled."""
    levels = []
    displacements = []
    for spin in range(10):
        parity = "+" if spin % 2 == 0 else "-"
        levels.append({"I": spin, "parity": parity,
                       "E_MeV": rot_a_mev * spin * (spin + 1)
                       + (offset_mev if spin % 2 else 0)})
    for spin in (1, 3, 5, 7):
        e = levels[spin]["E_MeV"]
        delta = e - (levels[spin - 1]["E_MeV"]
                     + levels[spin + 1]["E_MeV"]) / 2
        assert math.isclose(delta, offset_mev - rot_a_mev, abs_tol=1e-12)
        displacements.append({"I_odd": spin, "delta_E_MeV": delta})
    return {
        "status": "illustrative parity-projected two-well rotor; not fitted levels",
        "a_rot_MeV": rot_a_mev,
        "odd_parity_offset_MeV": offset_mev,
        "levels": levels,
        "delta_E_odd_relative_to_neighbor_even_MeV": displacements,
        "analytic_delta_E_MeV": offset_mev - rot_a_mev,
    }


def coherent_gdr_example() -> dict:
    """Explicit conditional interference in one eigenstate, not GDR tail data."""
    e_low, e_gdr = 1.0, 13.0
    d_low, d_gdr = 0.1, 1.0  # illustrative E1 amplitudes, e fm.
    ratio = d_low / d_gdr
    v_cancel = (e_gdr - e_low) * ratio / (1 - ratio**2)
    theta = 0.5 * math.atan2(2 * v_cancel, e_gdr - e_low)
    amp = math.cos(theta) * d_low - math.sin(theta) * d_gdr
    assert math.isclose(amp, 0, abs_tol=1e-13)
    return {
        "status": "two-level toy mixing; no claim of measured IVGDR cancellation",
        "E_low_MeV": e_low,
        "E_GDR_MeV": e_gdr,
        "unmixed_D_low_efm": d_low,
        "unmixed_D_GDR_efm": d_gdr,
        "mixing_v_for_exact_amplitude_zero_MeV": v_cancel,
        "theta_rad": theta,
        "mixed_low_D_efm": amp,
        "unmixed_low_B_E1_e2fm2": d_low**2,
        "mixed_low_B_E1_e2fm2": amp**2,
        "required_evidence": ["signed E1 transition amplitudes or phase-sensitive interference",
                              "state mixing and IVGDR strength distribution",
                              "same final-state and multipolarity coherence"],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_suffix(".json"))
    args = parser.parse_args()
    result = {
        "schema": "octupole-vs-cluster-dipole-dynamics-018/v1",
        "scope": "analytic point-cluster and two-level toy benchmark",
        "units": "A,Z dimensionless; R fm; D e fm; Q3 e fm^3",
        "geometry": [cluster_geometry(*case) for case in CASES],
        "ba146_published_amplitude_comparison": e1_e3_from_published_matrix_elements(),
        "ra224_published_e3_comparison": ra224_published_e3_comparison(),
        "parity_rotor_example": parity_displacement(0.012, 0.300),
        "gdr_mixing_example": coherent_gdr_example(),
        "S_alpha_boundary": {
            "normalized_projector_probability": "0 <= S_alpha <= 1",
            "empirical_values_20Ne_Ba_Ra": None,
            "why_not_inferred": "E3 and E1 can be reproduced by coherent non-cluster terms; antisymmetrization and channel normalization are unspecified",
            "reaction_spectroscopic_factor_warning": "Convention-dependent extracted factors need not equal a projector probability",
        },
        "validation": {
            "exact_charge_mass_match_20Ne": True,
            "center_of_mass_identity_all_cases": True,
            "parity_displacement_identity": True,
            "two_level_cancellation_identity": True,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n",
                           encoding="utf-8")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
