#!/usr/bin/env python3
"""Compare F14 HFA with finite-spin quantization of its frozen-j Hamiltonian.

This is a conditional model reconstruction, not the paper's full QTR/CQM
calculation, a fit, or an experimental confidence interval. Angular momenta
are dimensionless in hbar units; A_k and energies are in MeV. Only the fixed
spin representation is diagonalized; quasiparticle reorientation is absent.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


def frozen_matrix(spin: float, aligned_j: float, a: tuple[float, float, float]):
    if spin < 0 or not math.isclose(2 * spin, round(2 * spin)):
        raise ValueError("spin must be a nonnegative integer or half-integer")
    a1, a2, a3 = a
    m = np.arange(-spin, spin + 1.0)
    jj = spin * (spin + 1)
    diagonal = a3 * (m - aligned_j) ** 2 + (a1 + a2) * (jj - m**2) / 2
    h = np.diag(diagonal)
    for k, projection in enumerate(m[:-2]):
        factor = math.sqrt(
            (spin - projection) * (spin + projection + 1)
            * (spin - projection - 1) * (spin + projection + 2)
        )
        h[k, k + 2] = h[k + 2, k] = (a1 - a2) * factor / 4
    return m, h


def hfa_at_j(angular_momentum: float, aligned_j: float, a):
    a1, a2, a3 = a
    abar = a3 * (1 - aligned_j / angular_momentum)
    c1, c2 = a1 - abar, a2 - abar
    # A positive product alone also admits an energy maximum. We require
    # both positive curvatures for the yrast expansion around the 3-axis.
    stable_minimum = c1 > 0 and c2 > 0
    frequency = 2 * angular_momentum * math.sqrt(c1 * c2) if stable_minimum else None
    smallness = (
        3 * (c1 + c2) / (2 * angular_momentum * math.sqrt(c1 * c2))
        if stable_minimum else None
    )
    return {
        "J": angular_momentum, "c1_MeV": c1, "c2_MeV": c2,
        "stable_yrast_expansion": stable_minimum,
        "hfa_quantum_MeV": frequency,
        "eq23_lhs_over_J": smallness,
    }


def analytic_controls():
    # Axial limit is diagonal for every m, not merely the lowest gap.
    spin, aligned_j, a = 8.5, 5.5, (0.08, 0.08, 0.025)
    m, h = frozen_matrix(spin, aligned_j, a)
    exact = a[0] * (spin * (spin + 1) - m**2) + a[2] * (m - aligned_j) ** 2
    axial_error = float(np.max(np.abs(np.linalg.eigvalsh(h) - np.sort(exact))))

    # Independent construction with angular momentum operators, including
    # their commutator/Casimir, checks off-diagonal signs and factors.
    spin, aligned_j, a = 7.5, 3.5, (0.12, 0.04, 0.07)
    m, h = frozen_matrix(spin, aligned_j, a)
    jp = np.zeros_like(h, dtype=complex)
    for k, projection in enumerate(m[:-1]):
        jp[k + 1, k] = math.sqrt((spin - projection) * (spin + projection + 1))
    jm = jp.conj().T
    jx, jy, jz = (jp + jm) / 2, (jp - jm) / (2j), np.diag(m)
    dense = a[0] * jx @ jx + a[1] * jy @ jy + a[2] * (jz - aligned_j * np.eye(len(m))) ** 2
    operator_error = float(np.max(np.abs(h - dense)))
    casimir_error = float(np.max(np.abs(jx @ jx + jy @ jy + jz @ jz - spin * (spin + 1) * np.eye(len(m)))))
    commutator_error = float(np.max(np.abs(jx @ jy - jy @ jx - 1j * jz)))

    # H03 Eq.(15) tests adjacent m=I,I-1,I-2 branches, not sorted levels
    # which are +/-m degenerate for j=0 in this axial limit.
    a1, a2 = 0.02, 0.05
    def energy(projection):
        return a2 * spin * (spin + 1) + (a1 - a2) * projection**2
    second = energy(spin - 2) - 2 * energy(spin - 1) + energy(spin)
    nonharmonic_error = abs(second - (-2 * (a2 - a1)))
    errors = [axial_error, operator_error, casimir_error, commutator_error, nonharmonic_error]
    assert max(errors) < 1e-10, errors
    return dict(zip(
        ["axial_spectrum_max_error_MeV", "independent_operator_max_error_MeV",
         "casimir_max_error", "commutator_max_error", "H03_eq15_error_MeV"], errors
    ))


def parameter_contracts():
    """Keep LAW20's literal table inputs separate from earlier fit versions."""
    cases = [
        ("LAW20 iii", (1.0, 1.6, 4.0), 5.5, 14.5),
        ("LAW20 iv", (0.024, 0.039, 0.125), 5.5, 13.5),
        ("LAW20 v literal", (0.068, 0.093, 0.278), 5.5, 22.5),
        ("M15 reciprocals of 7.4/5.6/1.8", (1/14.8, 1/11.2, 1/3.6), 5.5, None),
        ("LAW20 vi", (0.085, 0.134, 0.394), 5.5, 14.5),
        ("LAW20 vii", (0.0078, 0.0089, 0.0385), 6.5, 42.5),
    ]
    rows = []
    for label, law_a, aligned_j, reported_max in cases:
        # LAW20: 1=m,2=s,3=l. F14 frozen function: 1=l,2=m,3=s.
        a = (law_a[2], law_a[0], law_a[1])
        boundary = aligned_j * law_a[1] / (law_a[1] - law_a[0])
        grid = [hfa_at_j(float(i), aligned_j, a)
                for i in np.arange(aligned_j, min(100, boundary), 1)]
        valid = [r for r in grid if r["stable_yrast_expansion"]]
        minimum = min(valid, key=lambda r: r["eq23_lhs_over_J"])
        j_test = minimum["J"]
        original = hfa_at_j(j_test, aligned_j, a)
        scaled = hfa_at_j(j_test, aligned_j, tuple(x / (1 + 0.116*j_test) for x in a))
        assert abs(original["eq23_lhs_over_J"] - scaled["eq23_lhs_over_J"]) < 1e-12
        rows.append({
            "label": label, "A_LAW_axes123": law_a, "j": aligned_j,
            "reported_Imax_table": reported_max,
            "positive_curvature_boundary_using_I_not_sqrtI_Iplus1": boundary,
            "last_stable_half_integer_in_grid": valid[-1]["J"],
            "n1_min_on_half_integer_grid": minimum["eq23_lhs_over_J"],
            "n1_grid_min_at_I": minimum["J"],
            "n2_min_on_same_grid": minimum["eq23_lhs_over_J"] * 5 / 3,
            "common_spin_scale_f_change": scaled["eq23_lhs_over_J"] - original["eq23_lhs_over_J"],
        })
    # A conditional longitudinal example: common spin-dependent inertia can
    # change the energy slope without changing geometry or the smallness f.
    a_long = (0.10, 0.12, 0.04)
    example = []
    for angular_momentum in [10, 20, 40, 80]:
        unscaled = hfa_at_j(angular_momentum, 6.5, a_long)
        scaled = hfa_at_j(angular_momentum, 6.5, tuple(x / (1 + 0.5*angular_momentum) for x in a_long))
        example.append({"I_used_as_large_spin_J": angular_momentum,
                        "longitudinal_fixed_MoI_quantum_MeV": unscaled["hfa_quantum_MeV"],
                        "longitudinal_scaled_MoI_quantum_MeV": scaled["hfa_quantum_MeV"],
                        "smallness_unchanged": scaled["eq23_lhs_over_J"]})
    assert all(example[i+1]["longitudinal_scaled_MoI_quantum_MeV"] < example[i]["longitudinal_scaled_MoI_quantum_MeV"] for i in range(3))
    return {"LAW20_TableI_reconstruction": rows,
            "notation": "LAW20 uses I in its alpha/f equations; this control does not silently substitute F14 sqrtI(I+1)",
            "table_boundary": "Literal printed Imax and analytic positive-curvature endpoint are retained separately; mismatches do not identify the original code inputs",
            "longitudinal_slope_control": example,
            "slope_control_boundary": "arbitrary illustrative spin dependence, not a fit or evidence for an actual nucleus"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    controls = analytic_controls()
    moi = (4.0, 21.0, 13.0)  # F14 Table I: axes 1=l, 2=m, 3=s.
    a = tuple(1 / (2 * x) for x in moi)
    aligned_j = 5.5  # Explicit frozen-j assumption; not a measured alignment.
    jc = aligned_j * a[2] / (a[2] - a[1])
    ic = (-1 + math.sqrt(1 + 4 * jc**2)) / 2
    rows = []
    for spin in np.arange(5.5, 22, 1):
        m, h = frozen_matrix(float(spin), aligned_j, a)
        values, vectors = np.linalg.eigh(h)
        residual = float(np.max(np.abs(h @ vectors - vectors * values)))
        transverse = [float(1 - np.sum(np.abs(vectors[:, k])**2 * m**2) / (spin * (spin + 1))) for k in range(3)]
        row = {"I": float(spin), "dimension": len(m), "finite_gap01_MeV": float(values[1] - values[0]),
               "finite_gap12_MeV": float(values[2] - values[1]),
               "finite_transverse_fraction_states012": transverse,
               "eigensystem_max_residual_MeV": residual,
               **hfa_at_j(math.sqrt(spin * (spin + 1)), aligned_j, a)}
        rows.append(row)
    assert max(r["eigensystem_max_residual_MeV"] for r in rows) < 1e-10
    # Inspect curvature/domain arbitrarily close to the classical instability.
    near = [hfa_at_j(jc * (1 - eps), aligned_j, a) for eps in [0.1, 0.01, 0.001, 0.0001]]
    result = {
        "model": "finite-spin frozen-j Hamiltonian, F14 Eq11; NOT full QTR/CQM",
        "provenance": {"source": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
                       "locator": "014322-4 Table I; 014322-6 Eqs11-15,23-24",
                       "raw_modified": False, "empirical_fit": False},
        "inputs": {"moi_axes123_hbar2_per_MeV": moi, "A_axes123_MeV": a, "assumed_j_hbar": aligned_j},
        "critical": {"Jc_hbar": jc, "Ic_from_sqrtI_Iplus1": ic},
        "analytic_controls": controls,
        "parameter_contracts": parameter_contracts(),
        "spin_grid": rows,
        "approach_to_instability": near,
        "boundaries": ["HFA smallness must be much less than 1; no universal numerical cutoff imposed",
                       "Finite gap01 is an eigenvalue difference at fixed I, not an observed band-spacing estimator",
                       "No quasiparticle reorientation, intrinsic Hamiltonian, transition operator or detector response",
                       "Nonzero finite gap does not certify wobbling or a phase transition"],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"output": str(args.output), "controls": controls, "critical": result["critical"],
                      "selected": [r for r in rows if r["I"] in [9.5, 12.5, 13.5, 14.5]]}))


if __name__ == "__main__":
    main()
