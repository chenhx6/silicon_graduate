#!/usr/bin/env python3
"""Audit KF89's printed 921-keV gate roles using an explicit point design.

This is neither DCOMAP nor an experimental refit. The quantum primitives are
reused from the uncredited Day15 preview; all inputs, inversions and gate-role
checks here belong to the independent Day16 run. Real amplitudes, integer spins,
no intermediate deorientation and L<=2 are the stated scope.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import eigh

from day16_d96_eq4_erratum_audit import coefficient, direct_density, direct_operators
from day16_pdco_ambiguity_preview import cg, orientation, small_d, source_f


def population(j: int, width: float) -> np.ndarray:
    p = np.exp(-np.arange(-j, j + 1, dtype=float) ** 2 / (2 * width**2))
    return p / p.sum()


def parts(delta: float | None) -> tuple:
    return (("E", 2, 1.0),) if delta is None else (("M", 1, 1.0), ("E", 2, delta))


def density(spins: tuple, pop: np.ndarray, target: tuple, reference: tuple,
            angles: list, psi: float | None = None) -> float:
    return direct_density(spins, target, reference, pop, angles,
                          {"q1": int(psi is not None), "q2": 0,
                           "psi1_deg": psi or 0.0, "psi2_deg": 0.0})


def gram(spins: tuple, pop: np.ndarray, reference: tuple,
         angles: list, psi: float | None = None) -> np.ndarray:
    a = density(spins, pop, (("M", 1, 1.0),), reference, angles, psi)
    c = density(spins, pop, (("E", 2, 1.0),), reference, angles, psi)
    b = density(spins, pop, parts(1.0), reference, angles, psi) - (a + c) / 2
    return np.array([[a, b], [b, c]])


def value(matrix: np.ndarray, alpha: float) -> float:
    v = np.array([math.cos(alpha), math.sin(alpha)])
    return float(v @ matrix @ v)


def roots(matrix: np.ndarray) -> list[float]:
    """All real projective roots v(alpha)^T matrix v(alpha)=0, radians."""
    a = float(np.trace(matrix) / 2)
    b = float((matrix[0, 0] - matrix[1, 1]) / 2)
    c = float(matrix[0, 1])
    h = math.hypot(b, c)
    scale = max(float(np.max(abs(matrix))), 1e-300)
    if h < 1e-12 * scale:
        if abs(a) < 1e-12 * scale:
            raise ValueError("All projective amplitudes are roots; no isolated inverse")
        return []
    if abs(a / h) > 1 + 1e-11:
        return []
    phase, shift = math.atan2(c, b), math.acos(float(np.clip(-a / h, -1, 1)))
    result = []
    for sign in (-1, 1):
        alpha = ((phase + sign * shift) / 2 + math.pi / 2) % math.pi - math.pi / 2
        if not any(abs(math.sin(alpha - old)) < 1e-10 for old in result):
            result.append(alpha)
    return sorted(result)


def preimage(a: np.ndarray, b: np.ndarray, lower: float, upper: float) -> list:
    cuts = [-math.pi / 2, math.pi / 2]
    for level in (lower, upper):
        cuts += roots(a - level * b)
    cuts = sorted(set(round(x, 13) for x in cuts))
    result = []
    for lo, hi in zip(cuts[:-1], cuts[1:]):
        mid = (lo + hi) / 2
        r = value(a, mid) / value(b, mid)
        if lower - 1e-12 <= r <= upper + 1e-12:
            result.append([math.degrees(lo), math.degrees(hi)])
    return result


def intersection(first: list, second: list) -> list:
    return [[max(a, c), min(b, d)] for a, b in first for c, d in second
            if max(a, c) <= min(b, d)]


def finite_delta(alpha: float) -> float | str:
    return "pure-quadrupole" if abs(math.cos(alpha)) < 1e-10 else math.tan(alpha)


def analyze(cfg: dict, width: dict, ref_delta: float) -> dict:
    p = population(11, 11 * width["sigma_std_over_J"])
    design = cfg["design"]
    ab = [design["polar_angle_A_deg"], design["polar_angle_B_deg"], design["relative_azimuth_deg"]]
    ba = [ab[1], ab[0], ab[2]]
    matrices = []
    for row in cfg["printed_rows"]:
        spins = tuple(row["physical_spins"])
        reference = parts(None if spins[-1] == 8 else ref_delta)
        a, b = [gram(spins, p, reference, angles) for angles in (ab, ba)]
        assert min(np.linalg.eigvalsh(a)) > 0 and min(np.linalg.eigvalsh(b)) > 0
        matrices.append((a, b, spins, reference))
    rows, inverse_intervals = [], []
    for index, (row, (a, b, spins, reference)) in enumerate(zip(cfg["printed_rows"], matrices)):
        # A source row whose gate is the physical first gamma reverses our target ratio.
        ra, rb = (b, a) if index == 0 else (a, b)
        measured, margin = row["raw_RDCO"], row["quoted_margin"]
        central_roots = roots(ra - measured * rb)
        allowed = preimage(ra, rb, measured - margin, measured + margin)
        inverse_intervals.append(allowed)
        pol_in, pol_out = [gram(spins, p, reference, ab, psi) for psi in (0.0, 90.0)]
        assert np.max(abs(pol_in + pol_out - a)) < 1e-13
        predictions = []
        for alpha in central_roots:
            r = value(ra, alpha) / value(rb, alpha)
            assert abs(r - measured) < 1e-10
            predictions.append({"d_D96": finite_delta(alpha), "atan_d_deg": math.degrees(alpha),
                                "raw_row_prediction": r,
                                "common_target_prediction": value(a, alpha) / value(b, alpha),
                                "other_raw_row_prediction": value(matrices[1-index][1 if index == 1 else 0], alpha)
                                / value(matrices[1-index][0 if index == 1 else 1], alpha),
                                "ideal_target_P_same_gate": value(pol_in - pol_out, alpha) / value(a, alpha)})
        rows.append({"id": row["id"], "common_target_numerator_gram": a.tolist(),
                     "common_target_denominator_gram": b.tolist(),
                     "raw_ratio_range_generalized_eigenvalues": eigh(ra, rb, eigvals_only=True).tolist(),
                     "central_all_roots": predictions,
                     "quoted_margin_preimage_atan_deg": allowed,
                     "pure_dipole_raw_ratio": float(ra[0, 0] / rb[0, 0]),
                     "pure_quadrupole_raw_ratio": float(ra[1, 1] / rb[1, 1])})
    # Simultaneous convention changes, unlike changing a coordinate alone, preserve W/R/P.
    s = np.diag([1.0, -1.0])
    errors, wrong_errors, closure_errors, reciprocal_errors = [], [], [], []
    for alpha in np.linspace(-math.pi / 2, math.pi / 2, 53):
        v = np.array([math.cos(alpha), math.sin(alpha)])
        vp = s @ v
        for a, b, spins, reference in matrices:
            original = float(v @ a @ v / (v @ b @ v))
            converted = float(vp @ (s @ a @ s) @ vp / (vp @ (s @ b @ s) @ vp))
            wrong = float(vp @ a @ vp / (vp @ b @ vp))
            errors.append(abs(original - converted)); wrong_errors.append(abs(original - wrong))
            reciprocal_errors.append(abs(original * float(v @ b @ v / (v @ a @ v)) - 1))
            direct = density(spins, p, (("M", 1, v[0]), ("E", 2, v[1])), reference, ab)
            closure_errors.append(abs(value(a, alpha) - direct))
    assert max(errors) < 1e-12 and max(closure_errors) < 1e-12
    assert max(reciprocal_errors) < 1e-12 and max(wrong_errors) > 1e-3
    # A pure reference can test diagonals without testing the mixed-term sign.
    a, b, _, _ = matrices[0]
    assert all(abs(value(a, alpha) - value(s @ a @ s, alpha)) < 1e-13
               for alpha in (0.0, math.pi / 2, -math.pi / 2))
    return {"width_choice": width, "ref169_d_D96_diagnostic": ref_delta, "rows": rows,
            "two_printed_margin_intersection_atan_deg": intersection(*inverse_intervals),
            "checks": {"simultaneous_phase_map_max_ratio_error": max(errors),
                       "wrong_phase_map_max_ratio_change": max(wrong_errors),
                       "direct_vs_quadratic_max_density_error": max(closure_errors),
                       "same_cells_reciprocal_max_error": max(reciprocal_errors)}}


def source_f_check() -> dict:
    """Independent F contraction checks mixed signs for this new spin pair."""
    p = population(11, 3.3); rho = np.diag(p)
    angles = np.array([0.0, 45.0, 90.0]); xs = np.cos(np.deg2rad(angles))
    leg = np.column_stack([np.polynomial.legendre.legval(xs, [0]*k + [1]) for k in (0, 2, 4)])
    f = {k: np.array([[source_f(k, 0, k, ell, ellp, 11, 10) for ellp in (1, 2)]
                     for ell in (1, 2)]) for k in (0, 2, 4)}
    assert np.max(abs(f[0] - np.eye(2))) < 1e-12
    errors = []
    for d in (-2.3, -0.3, 0.0, 0.07, 0.4, 1.0, 86.0):
        v = np.array([1.0, d]) / math.hypot(1.0, d)
        expected = np.array([orientation(11, rho, k) * (v @ f[k] @ v) for k in (0, 2, 4)])
        singles = [sum(float(np.sum(abs(op)**2 * p[None, :]))
                       for op in direct_operators(11, 10, parts(d), math.radians(t), 0.0, None))
                   for t in angles]
        measured = np.linalg.solve(leg, singles); measured /= measured[0]
        errors.append(float(max(abs(expected - measured))))
    assert max(errors) < 1e-11
    return {"F_matrices_11_to_10": {str(k): a.tolist() for k, a in f.items()},
            "source_F_vs_photon_single_distribution_max_error": max(errors),
            "independence_boundary": "Different contractions share CG/Wigner primitives; no independent experiment or producer replay."}


def full_tensor_check() -> dict:
    """D96 Eq1/3/7 unpolarized contraction, separately from photon trace."""
    p=population(11,3.3); rho=np.diag(p); differences=[]
    for spins,reference in [((11,10,8),parts(None)),((11,10,9),parts(-1.9))]:
        for target in [parts(0.0),parts(.09186003498052088),parts(2.0),parts(None)]:
            terms=[]
            # Second L<=2 permits outgoing<=4; first L<=2 then incoming<=8.
            for incoming in range(0,min(2*spins[0],8)+1,2):
                orient=orientation(spins[0],rho,incoming)
                for outgoing in range(0,min(2*spins[1],4)+1,2):
                    g=coefficient(spins[1],spins[2],reference,0,outgoing,outgoing,False)
                    if abs(g)<1e-15: continue
                    for rank in range(abs(incoming-outgoing),min(incoming+outgoing,4)+1):
                        f=coefficient(spins[0],spins[1],target,outgoing,incoming,rank,False)
                        for mu in range(min(rank,outgoing)+1):
                            weight=orient*f*g*cg(incoming,0,outgoing,mu,rank,mu)/(1+(mu==0))
                            if abs(weight)>1e-15: terms.append((rank,outgoing,mu,weight))
            for angles in [[90.,38.,18.],[38.,90.,18.],[47.,71.,53.]]:
                t1,t2,phi=np.deg2rad(angles)
                expected=sum(w*small_d(k,mu,0,t1)*small_d(k1,mu,0,t2)*math.cos(mu*phi)
                             for k,k1,mu,w in terms)/(8*math.pi**2)
                actual=density(spins,p,target,reference,angles)
                differences.append(abs(expected-actual))
    assert max(differences)<1e-12
    return {"max_density_error_sr_minus2":max(differences),"comparisons":len(differences),
            "rank_truncation":"algebraic: second rank<=4, first rank<=4 hence initial rank<=8",
            "scope":"integer spins 11/10/8 and 11/10/9; real amplitudes; same CG/Wigner primitives"}


def pure_table_diagnostic() -> list:
    # Printed334 Table1, gate is physical second photon. No mixed sign fit is used.
    table = [([10,8,6],2,2,1.00),([10,8,7],2,1,.56),([10,8,7],2,2,.66),
             ([10,8,8],2,1,1.07),([10,8,8],2,2,.57),([9,8,6],1,2,1.81),
             ([9,8,7],1,2,.92),([9,8,7],1,1,1.00),([9,8,8],1,1,1.79),([9,8,8],1,2,1.12)]
    result=[]
    for spins,l1,l2,printed in table:
        p=population(spins[0],.3*spins[0]); first=(("E",l1,1.0),); second=(("E",l2,1.0),)
        a=density(tuple(spins),p,first,second,[90.,38.,18.])
        b=density(tuple(spins),p,first,second,[38.,90.,18.])
        result.append({"spins":spins,"ranks":[l1,l2],"printed":printed,
                       "conditional_point_std_prediction":a/b,"difference":a/b-printed})
    return result


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args(); cfg=json.loads(args.input.read_text())
    assert cfg["identity"]=="DAY16-KF89-W178-921-GATE-CROSSWALK-01"
    raw=cfg["printed_rows"][0]["raw_RDCO"]; err=cfg["printed_rows"][0]["quoted_margin"]
    cases=[analyze(cfg,w,d) for w in cfg["design"]["sigma_choices"]
           for d in cfg["design"]["reference_delta_D96_diagnostic_choices"]]
    result={"identity":cfg["identity"],"input_sha256":hashlib.sha256(args.input.read_bytes()).hexdigest(),
            "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "boundary":"Conditional point design with no experimental likelihood, detector response or covariance; source candidates are not refitted.",
            "role_reciprocal":{"central":1/raw,"literal_margin_image":[1/(raw+err),1/(raw-err)],
                               "first_order_sigma_if_small_error":err/raw**2,
                               "cross_covariance_jacobian_multiplier":-1/raw**2,
                               "confidence_label":None},
            "source_phase_crosscheck":source_f_check(),"full_tensor_check":full_tensor_check(),"cases":cases,
            "pure_table_diagnostic":pure_table_diagnostic(),
            "all_checks_passed":True}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    print(json.dumps({"output":str(args.output),"all_checks_passed":True,
                      "role_reciprocal":result["role_reciprocal"],
                      "cases":[{"width":c["width_choice"]["label"],"reference_delta":c["ref169_d_D96_diagnostic"],
                                "intersection":c["two_printed_margin_intersection_atan_deg"],
                                "central_roots":[r["central_all_roots"] for r in c["rows"]],
                                "checks":c["checks"]} for c in cases],
                      "F_max_error":result["source_phase_crosscheck"]["source_F_vs_photon_single_distribution_max_error"]},ensure_ascii=False))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
