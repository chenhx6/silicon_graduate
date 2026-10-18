#!/usr/bin/env python3
"""Source-defined L26/M22 printed-summary and convention audit.

Requires SymPy (this run installs it only under tmp/day16-jt74/python-deps).
This does not reconstruct experimental events, response matrices or covariance.
"""
from __future__ import annotations

import argparse
from functools import lru_cache
import hashlib
import itertools
import json
import math
from pathlib import Path
import re

import numpy as np
import sympy as sp
from sympy.physics.wigner import clebsch_gordan, racah

from day16_d96_eq4_erratum_audit import direct_operators


def quoted(value: str) -> tuple[float, float, float]:
    match = re.fullmatch(r"([+-]?\d+(?:\.\d+)?)\((\d+)\)", value)
    if match is None:
        raise ValueError(value)
    v, err = match.groups()
    unit = 10.0 ** -(len(v.split(".")[1]) if "." in v else 0)
    return float(v), int(err)*unit, unit


@lru_cache(None)
def source_r(ji2: int, jf2: int, low: int, high: int, rank: int) -> float:
    ji, jf = sp.Rational(ji2, 2), sp.Rational(jf2, 2)
    photon_cg = clebsch_gordan(low, high, rank, 1, -1, 0)
    if photon_cg == 0:
        return 0.0
    exponent = 1 + ji - jf + high - low - rank
    assert exponent.is_integer
    return float((-1)**exponent * photon_cg
                 * sp.sqrt((2*ji+1)*(2*low+1)*(2*high+1))
                 * racah(ji, ji, low, high, rank, jf))


def tensor_b(ji2: int, rank: int, population: np.ndarray) -> float:
    ji = sp.Rational(ji2, 2)
    projections = [sp.Rational(m2, 2) for m2 in range(-ji2, ji2+1, 2)]
    assert len(population) == len(projections)
    return sum(float((-1)**(ji-m)*sp.sqrt(2*ji+1)
                     * clebsch_gordan(ji, ji, rank, m, -m, 0))*p
               for m, p in zip(projections, population))


def gaussian(ji2: int, sigma_over_j: float) -> np.ndarray:
    sigma = sigma_over_j*ji2/2
    assert sigma > 0
    m = np.arange(-ji2, ji2+1, 2)/2
    p = np.exp(-m*m/(2*sigma*sigma))
    return p/p.sum()


def coefficients(ji2: int, jf2: int, population: np.ndarray,
                 delta: float | None) -> dict:
    # None denotes pure E2, keeping Table1's pure-E2 zero distinct from M1/E2 delta0.
    def ak(rank: int, polarized: bool = False) -> float:
        if delta is None:
            r = source_r(ji2, jf2, 2, 2, rank)
            if polarized:
                r *= .5 if rank == 2 else -1/12
            return r*tensor_b(ji2, rank, population)
        values = [source_r(ji2, jf2, a, b, rank) for a, b in [(1, 1), (1, 2), (2, 2)]]
        if polarized:
            factors = [.5, -1/6, .5] if rank == 2 else [0.0, 0.0, -1/12]
            values = [a*b for a, b in zip(values, factors)]
        return (values[0]+2*delta*values[1]+delta*delta*values[2])/(1+delta*delta)*tensor_b(ji2, rank, population)
    a0, a2, a4, a2p, a4p = ak(0), ak(2), ak(4), ak(2, True), ak(4, True)
    assert abs(a0-1) < 1e-12
    w90 = 1-a2/2+3*a4/8
    h90 = 3*a2p-7.5*a4p  # parity +; an E1/M2 branch reverses the sign.
    return {"a0": a0, "a2": a2, "a4": a4, "H90_parity_plus": h90,
            "W90": w90, "P90_parity_plus": h90/w90 if w90 > 1e-13 else None}


def trace_coefficients(ji: int, jf: int, population: np.ndarray, native: tuple) -> dict:
    angles = np.array([0.0, 45.0, 90.0])
    x = np.cos(np.deg2rad(angles))
    design = np.column_stack([np.ones(3), (3*x*x-1)/2, (35*x**4-30*x*x+3)/8])
    def rate(theta: float, psi: float | None = None) -> float:
        return float(sum(np.sum(abs(op)**2*population[None, :]).real
                         for op in direct_operators(ji, jf, native, math.radians(theta), 0.0, psi)))
    beta = np.linalg.solve(design, [4*math.pi*rate(t) for t in angles])
    assert abs(beta[0]-1) < 1e-12
    para, perp = rate(90.0, 0.0), rate(90.0, math.pi/2)
    return {"a2": float(beta[1]), "a4": float(beta[2]),
            "P90_parity_plus": (para-perp)/(para+perp) if para+perp > 1e-13 else None}


def q_curve(energy: float, p0: float = .131, p1: float = 3.25e-4) -> float:
    assert energy > 0
    return (p0+p1*energy)/(energy/511+511/(energy+511))


def pure_e2_p90(a2: float, a4: float) -> float:
    return (12*a2+5*a4)/(8-4*a2+3*a4)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--l26-input", type=Path, required=True)
    parser.add_argument("--m22-input", type=Path, required=True)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    lc, mc, contract = [json.loads(p.read_text()) for p in [args.l26_input, args.m22_input, args.contract]]
    assert contract["identity"] == "GRETINA-L26-M22-DECLARED-REPLAY-CONTRACT-01"
    for path in [args.l26_input, args.m22_input]:
        assert hashlib.sha256(path.read_bytes()).hexdigest() == contract["inputs_sha256"][path.name]
    for path, sha in contract["helper_hashes"].items():
        assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == sha
    rows = []
    for row in lc["rows"]:
        sigma, _, sigma_unit = quoted(row["sigma_over_J"])
        delta = None if row["upper"] is None else quoted(row["delta_RB"])[0]
        central = coefficients(row["Ji2"], row["Jf2"], gaussian(row["Ji2"], sigma), delta)
        central["P90_with_declared_photon_parity"] = row["parity_product"]*central["P90_parity_plus"]
        assert abs(central["P90_with_declared_photon_parity"]) <= 1+1e-12
        corners = []
        for sign_sigma, sign_delta in itertools.product([-1, 1], repeat=2):
            d = None if delta is None else delta+sign_delta*quoted(row["delta_RB"])[2]/2
            corners.append(coefficients(row["Ji2"], row["Jf2"], gaussian(row["Ji2"], sigma+sign_sigma*sigma_unit/2), d))
        qq = q_curve(row["E_keV"])
        afit, _, _ = quoted(row["A0_fit"])
        apred, _, _ = quoted(row["A0_pred"])
        rows.append({"nucleus": row["nucleus"], "E_keV": row["E_keV"],
                     "recomputed_from_printed_delta_sigma_Qgeometry1": central,
                     "source_printing_box_coefficient_images": {k: [min(c[k] for c in corners), max(c[k] for c in corners)] for k in ["a2", "a4"]},
                     "Q_adopted_curve": qq,
                     "Pbar_implied_by_source_A0pred_not_independent_calibration": 2*apred/qq,
                     "Pbar_diagnostic_if_using_A0fit_and_same_adoptedQ_not_remeasurement": 2*afit/qq,
                     "A0fit_minus_pred": afit-apred,
                     "no_independent_residual_chi2": True,
                     "outside_Morse_GRETA_simulated_energy_range": not 500 <= row["E_keV"] <= 2000})

    # An independently identified photon kernel fixes a mathematical basis bridge;
    # no experimental coefficient or desired delta branch is fitted here.
    p3 = np.zeros(7); p3[3] = .5; p3[2] = p3[4] = .25
    bridge_errors, wrong_errors = [], []
    for drb in [-2.0, -.4, 0.0, .5, 3.0]:
        source = coefficients(6, 4, p3, drb)
        proper = trace_coefficients(3, 2, p3, (("M", 1, 1.0), ("E", 2, -drb)))
        wrong = trace_coefficients(3, 2, p3, (("M", 1, 1.0), ("E", 2, drb)))
        for key in ["a2", "a4", "P90_parity_plus"]:
            bridge_errors.append(abs(source[key]-proper[key]))
            wrong_errors.append(abs(source[key]-wrong[key]))
    assert max(bridge_errors) < 2e-12
    assert max(wrong_errors) > .1
    pure_e = coefficients(6, 4, p3, None)
    direct_e = trace_coefficients(3, 2, p3, (("E", 2, 1.0),))
    assert all(abs(pure_e[k]-direct_e[k]) < 2e-12 for k in ["a2", "a4", "P90_parity_plus"])

    # Source Fig7's actual spin path and width: parity reversal distinguishes
    # nonstretched E1+M2 from M1+E2 without changing its AD coefficients.
    fig7 = coefficients(9, 9, gaussian(9, .3), 0.0)
    assert fig7["P90_parity_plus"] > 0
    sign_example = {"M1_E2_delta0_P90": fig7["P90_parity_plus"],
                    "E1_M2_delta0_P90": -fig7["P90_parity_plus"],
                    "Table3_agrees_with_these_signs": True,
                    "Appendix_prose_positive_E1_M2_example_conflicts": True}
    pure_m1_morse = 1.5*fig7["a2"]/fig7["W90"]  # Pi_photon(M1)=+1
    pure_m1_l26_type = -(-1)*1.5*fig7["a2"]/fig7["W90"]  # tau_EM(M1)=-1
    assert abs(pure_m1_morse-fig7["P90_parity_plus"]) < 1e-12
    assert abs(pure_m1_l26_type-pure_m1_morse) < 1e-12
    zero_controls = []
    for ji2, jf2 in [(9, 9), (7, 5)]:
        aa, bb, cc = [source_r(ji2, jf2, a, b, 2) for a, b in [(1, 1), (1, 2), (2, 2)]]
        for root in np.roots([cc, 2*bb, aa]):
            assert abs(root.imag) < 1e-12
            d = float(root.real)
            values = coefficients(ji2, jf2, gaussian(ji2, .3), d)
            assert abs(values["a2"]) < 2e-12 and values["P90_parity_plus"] is not None
            zero_controls.append({"Ji2": ji2, "Jf2": jf2, "delta_RB_at_A2zero": d,
                                  "physical_P90_by_undivided_products": values["P90_parity_plus"],
                                  "ratio_A2prime_over_A2_times_a2_is_naive_0over0": True})
    cg_odd = clebsch_gordan(1, 1, 1, 1, -1, 0)
    odd_tensors = {str(k): tensor_b(9, k, gaussian(9, .56)) for k in [1, 3, 5, 7, 9]}
    assert cg_odd != 0 and max(abs(v) for v in odd_tensors.values()) < 2e-14

    # Exact physical population coordinates for M22's pure 2->0 E2 transition.
    basis = []
    for pop in [np.array([0, 0, 1, 0, 0.]), np.array([0, .5, 0, .5, 0.]), np.array([.5, 0, 0, 0, .5])]:
        a = trace_coefficients(2, 0, pop, (("E", 2, 1.0),))
        independent = coefficients(4, 0, pop, None)
        assert all(abs(a[k]-independent[k]) < 2e-12 for k in ["a2", "a4"])
        basis.append(a)
    matrix = np.array([[1, 1, 1], [a["a2"] for a in basis], [a["a4"] for a in basis]])
    a2, e2, _ = quoted(mc["calibration_data"]["a2"])
    a4, e4, _ = quoted(mc["calibration_data"]["a4"])
    inferred_groups = np.linalg.solve(matrix, [1, a2, a4])
    p0_interval_a2 = [14*(a2-e2)/5-1, 14*(a2+e2)/5-1]
    p0_interval_a4 = [(8-7*(a4+e4))/20, (8-7*(a4-e4))/20]
    feasible_p0 = [max(p0_interval_a2[0], p0_interval_a4[0]), min(p0_interval_a2[1], p0_interval_a4[1])]
    assert feasible_p0[0] <= feasible_p0[1]
    printed_pop = np.array([0., .24, .52, .24, 0.])
    print_model = trace_coefficients(2, 0, printed_pop, (("E", 2, 1.0),))
    isotropic = trace_coefficients(2, 0, np.ones(5)/5, (("E", 2, 1.0),))
    assert max(abs(isotropic[k]) for k in ["a2", "a4", "P90_parity_plus"]) < 2e-12
    assert basis[0]["P90_parity_plus"] is None  # zero photons at that angle, not P=0
    pbar = quoted(mc["calibration_data"]["Pbar_whole_array"])[0]
    qm = quoted(mc["calibration_data"]["Q_whole_array"])[0]
    acut = quoted(mc["calibration_data"]["A0_Fig6_80_to100deg"])[0]
    cuts = []
    base_f = mc["Table2_cuts"][0]["F"][0]
    base_q = mc["Table2_cuts"][0]["Q"][0]
    base_eff = base_f/base_q**2
    for row in mc["Table2_cuts"]:
        qv, fv = row["Q"][0], row["F"][0]
        eff = fv/qv**2
        cuts.append({**row, "efficiency_implied_central": eff,
                     "relative_efficiency_to_None": eff/base_eff,
                     "relative_F_to_None": fv/base_f,
                     "relative_statistical_error_if_common_model": math.sqrt(base_f/fv),
                     "epsilon_error_not_inferred_without_Q_F_covariance": True})

    # Same-P normalization translation preserves both observables and information.
    q_alt = qm/2
    assert abs(.5*qm*pbar-q_alt*pbar) < 1e-15
    assert abs(base_f/8 - ((q_alt**2*base_eff)/2)) < 1e-15
    two_hit = []
    for row in lc["rows"]:
        beta = lc["beta_Fig1"][row["nucleus"]]
        points = []
        for center in [90., 122., 148.]:
            lab_energy = row["E_keV"]*math.sqrt(1-beta*beta)/(1-beta*math.cos(math.radians(center)))
            threshold = math.degrees(math.acos(1-511/lab_energy)) if lab_energy > 255.5 else None
            points.append({"quad_center_deg": center, "lab_incident_energy_keV": lab_energy,
                           "true_first_deposit_is_larger_if_psi_above_deg": threshold})
        two_hit.append({"nucleus": row["nucleus"], "rest_energy_keV": row["E_keV"], "conditional_quad_center_examples": points})
    x, y = sp.Matrix(sp.symbols("x1 x2 x3")), sp.Matrix(sp.symbols("y1 y2 y3"))
    assert (x.cross(y-x)-x.cross(y)).applyfunc(sp.simplify) == sp.zeros(3, 1)
    assert (y.cross(x-y)+x.cross(y)).applyfunc(sp.simplify) == sp.zeros(3, 1)
    result = {"identity": contract["identity"], "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "input_sha256": contract["inputs_sha256"], "L26_printed_table_replay": rows,
              "emission_basis_bridge": {"delta_D96_native": "-delta_L26_RB", "max_observable_error": max(bridge_errors),
                                        "wrong_sign_max_error": max(wrong_errors), "pure_M1_E2_controls_passed": True,
                                        "scope": "Specified single-emitter spin/state ordering and Jones-axis convention; not every cascade-role delta."},
              "L26_sign_example": sign_example, "A2zero_controls": zero_controls,
              "Pi_working_contract_control": {"mixed_M1_limit": fig7["P90_parity_plus"],
                                                "Morse_pure_with_photon_parity": pure_m1_morse,
                                                "L26_pure_with_EM_type_sign": pure_m1_l26_type,
                                                "holding_photon_parity_in_L26_pure_formula_would_flip_sign": True,
                                                "author_Pi_definition_not_authenticated": True},
              "odd_CG_counterexample": str(cg_odd), "odd_B_for_symmetric_source_Gaussian": odd_tensors,
              "M22_physical_density_check": {"basis_group_a2_a4": basis,
                                            "central_group_populations_not_physical_measurement": inferred_groups.tolist(),
                                            "P90_from_printed_a2_a4": pure_e2_p90(a2, a4),
                                            "physical_pabs2zero_feasibility_from_literal_marginal_boxes_not_CI": feasible_p0,
                                            "source_rounded_MC_population_intrinsic_coefficients": print_model,
                                            "zero_intensity_m0_P90": None,
                                            "note": "A slightly unphysical central fit is not a negative nuclear population. Source detector-fit coefficients and intrinsic moments are different replay objects; no original response/fit covariance is supplied."},
              "M22_selection_identity_control": {"Q_if_mixing_Fig6_cut_A0_with_array_Pbar": 2*acut/pbar,
                                                 "A0_implied_by_array_Q_Pbar_identity_not_new_measurement": .5*qm*pbar,
                                                 "conclusion": "Do not combine these selections as a source-error test; matching full-array xi fit not explicitly supplied."},
              "M22_cut_tradeoffs": cuts,
              "normalization_translation": {"source_kappa": .5, "source_Q": qm, "sameP_kappa1_Q": q_alt,
                                             "observable_invariant": True, "information_per_emitted_photon_at_P0": base_f/8,
                                             "information_contract": "For declared p(xi|P)=(1-kappa Q P cos2xi)/(2pi), knownQ/backgroundfree and uniformreference, I_P(0)/yield=kappa^2 Q^2 epsilon/2. Not measured beam-time precision."},
              "two_hit_kinematic_design": two_hit,
              "two_hit_plane_identity": "x1 cross(x2-x1)=x1 cross x2; reversal changes only normal sign. Reaction-plane beam cross x_first generally changes, so xi/Doppler angles need not remain equal.",
              "scope": "Actual printed summaries and declared physical/theoretical checks. No event data, actual response/selection covariance, original producer fit, new delta or confidence interval.",
              "day_index": 16, "partial_day_indices": [17], "formal_day17_credit": False,
              "all_internal_checks_passed": True}
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False)+"\n")
    print(json.dumps({"output": str(args.output), "basis_bridge": result["emission_basis_bridge"],
                      "sign_example": sign_example, "M22_density": result["M22_physical_density_check"],
                      "cut_tradeoffs": cuts, "normalization": result["normalization_translation"],
                      "all_internal_checks_passed": True}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
