#!/usr/bin/env python3
"""Day16 uncredited preview: a D96 point-response 5->4->2 ambiguity witness.

The calculation is ours, not the authors' FORTRAN or an experiment replay.
CG coefficients use an exact rational Racah sum; source F coefficients use an
explicit six-CG recoupling definition of the Wigner 9j symbol. The photon kernel
is a separate calculation. No SymPy, detector simulation or private input is used.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

import numpy as np


@lru_cache(None)
def cg(j1: int, m1: int, j2: int, m2: int, j: int, m: int) -> float:
    """Condon-Shortley CG; integer spins only in this fixed source example."""
    if m1+m2 != m or abs(m1)>j1 or abs(m2)>j2 or abs(m)>j or not abs(j1-j2)<=j<=j1+j2:
        return 0.
    fac = math.factorial
    radicand = Fraction((2*j+1)*fac(j+j1-j2)*fac(j-j1+j2)*fac(j1+j2-j)*fac(j+m)*fac(j-m)
                        *fac(j1-m1)*fac(j1+m1)*fac(j2-m2)*fac(j2+m2), fac(j1+j2+j+1))
    total = Fraction(0)
    for k in range(j1+j2-j+1):
        args = (k, j1+j2-j-k, j1-m1-k, j2+m2-k, j-j2+m1+k, j-j1-m2+k)
        if min(args) >= 0:
            total += Fraction((-1)**k, math.prod(fac(v) for v in args))
    return math.sqrt(float(radicand))*float(total)


@lru_cache(None)
def small_d(j: int, mp: int, m: int, theta: float) -> float:
    """exp(-i theta Jy); d^1_(0,+1)=+sin(theta)/sqrt(2)."""
    fac = math.factorial
    prefactor = math.sqrt(fac(j+m)*fac(j-m)*fac(j+mp)*fac(j-mp))
    total = 0.
    for k in range(2*j+1):
        args = (j+m-k, k, mp-m+k, j-mp-k)
        if min(args) < 0:
            continue
        total += ((-1.)**(mp-m+k)*prefactor/math.prod(fac(v) for v in args)
                  *math.cos(theta/2)**(2*j+m-mp-2*k)*math.sin(theta/2)**(mp-m+2*k))
    return total


@lru_cache(None)
def nine_j(a: int, b: int, c: int, d: int, e: int, f: int, g: int, h: int, i: int) -> float:
    """Overlap of ((a,b)c,(d,e)f)i and ((a,d)g,(b,e)h)i."""
    total, projection = 0., i
    for ma in range(-a, a+1):
        for mb in range(-b, b+1):
            mc = ma+mb
            if abs(mc)>c:
                continue
            first = cg(a, ma, b, mb, c, mc)
            if abs(first)<1e-16:
                continue
            for md in range(-d, d+1):
                me = projection-ma-mb-md
                if abs(me)>e:
                    continue
                mf, mg, mh = md+me, ma+md, mb+me
                if abs(mf)>f or abs(mg)>g or abs(mh)>h:
                    continue
                total += (first*cg(d, md, e, me, f, mf)*cg(c, mc, f, mf, i, projection)
                          *cg(a, ma, d, md, g, mg)*cg(b, mb, e, me, h, mh)*cg(g, mg, h, mh, i, projection))
    return total/math.sqrt((2*c+1)*(2*f+1)*(2*g+1)*(2*h+1))


def source_f(k: int, outgoing: int, incoming: int, ell: int, ellp: int, ji: int, jf: int) -> float:
    # D96 printed520 Eq7, including its L-1 phase and I_f,I_i argument order.
    photon_cg = cg(ell, -1, ellp, 1, k, 0)
    if photon_cg == 0:
        return 0.
    return ((-1)**(ell-1)*math.sqrt((2*ji+1)*(2*jf+1)*(2*ell+1)*(2*ellp+1)
                                   *(2*outgoing+1)*(2*incoming+1))*photon_cg
            *nine_j(ji, ji, incoming, ell, ellp, k, jf, jf, outgoing))


def orientation(j: int, rho: np.ndarray, k: int) -> float:
    return math.sqrt(2*j+1)*sum((-1)**(j+m)*cg(j, m, j, -m, k, 0)*rho[m+j, m+j].real for m in range(-j, j+1))


@lru_cache(None)
def pure_operator(ji: int, jf: int, ell: int, kind: str, theta: float, phi: float, helicity: int) -> np.ndarray:
    result = np.zeros((2*jf+1, 2*ji+1), dtype=complex)
    for row, mf in enumerate(range(-jf, jf+1)):
        for col, mi in enumerate(range(-ji, ji+1)):
            mu = mi-mf
            if abs(mu)>ell:
                continue
            result[row, col] = (math.sqrt((2*ell+1)/(8*math.pi))*cg(jf, mf, ell, mu, ji, mi)
                                *np.exp(1j*mu*phi)*small_d(ell, mu, helicity, theta)
                                *(helicity if kind == "M" else 1))
    result.setflags(write=False)
    return result


def operators(ji: int, jf: int, parts: tuple, theta_deg: float, phi_deg: float, psi: float | None = None) -> list[np.ndarray]:
    theta, phi = map(float, np.deg2rad([theta_deg, phi_deg]))
    helicities = {lam: sum(amp*pure_operator(ji, jf, ell, kind, theta, phi, lam)
                           for kind, ell, amp in parts) for lam in (1, -1)}
    if psi is None:
        return list(helicities.values())
    # Standard circular polarization basis: psi=0 means electric field in emission plane.
    return [(-np.exp(1j*psi)*helicities[1]+np.exp(-1j*psi)*helicities[-1])/math.sqrt(2)]


def source_parts(angle: float) -> tuple:
    """angle=atan(d_source), with d_source=a(E2)/a(M1) in D96 Eq3.

    The frozen probe basis has eta_M=lambda. Source F comparison derives
    delta_probe=-d_source; the relative phase is explicit, not fitted to Fig7.
    """
    return (("M", 1, math.cos(angle)), ("E", 2, -math.sin(angle)))


def density(parts: tuple, rho: np.ndarray, first: tuple, second: tuple,
            psi1: float | None = None, psi2: float | None = None) -> float:
    result = 0.
    for t1 in operators(5, 4, parts, *first, psi1):
        for t2 in operators(4, 2, (("E", 2, 1.),), *second, psi2):
            amplitude = t2@t1
            value = np.trace(amplitude@rho@amplitude.conj().T)
            assert abs(value.imag)<1e-13
            result += value.real
    assert result>=-1e-14
    return float(result)


def singles(parts: tuple, rho: np.ndarray, theta: float = 90., psi: float | None = None) -> float:
    return float(sum(np.trace(t@rho@t.conj().T).real for t in operators(5, 4, parts, theta, 0., psi)))


def polarization(parts: tuple, rho: np.ndarray, mode: int, geometry: tuple = ((90., 0.), (90., 180.))) -> float:
    if mode == 0:
        values = [singles(parts, rho, psi=psi) for psi in (0., math.pi/2)]
    else:
        values = [density(parts, rho, *geometry, psi1=psi if mode == 1 else None,
                          psi2=psi if mode == 2 else None) for psi in (0., math.pi/2)]
    if sum(values)<=0:
        raise ValueError("Undefined polarization denominator")
    return (values[0]-values[1])/sum(values)


def case(parts: tuple, rho: np.ndarray) -> dict:
    denominator = density(parts, rho, (90., 0.), (0., 0.))
    if denominator<=0:
        raise ValueError("Undefined DCO denominator")
    return {"R_star": density(parts, rho, (0., 0.), (90., 0.))/denominator,
            "P_singles_gamma1": polarization(parts, rho, 0),
            "P_POL_DIR_gamma1": polarization(parts, rho, 1),
            "P_DIR_POL_gamma2": polarization(parts, rho, 2)}


def integrate_channel(ji: int, jf: int, parts: tuple, nt: int, np_: int, rho: np.ndarray | None = None) -> np.ndarray:
    xs, ws = np.polynomial.legendre.leggauss(nt)
    result = np.zeros((2*ji+1, 2*ji+1), complex) if rho is None else np.zeros((2*jf+1, 2*jf+1), complex)
    for x, w in zip(xs, ws):
        for phi in np.arange(np_)*360/np_:
            for op in operators(ji, jf, parts, float(np.rad2deg(np.arccos(x))), float(phi)):
                result += w*(2*math.pi/np_)*(op.conj().T@op if rho is None else op@rho@op.conj().T)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.input.read_text(encoding="utf-8"))
    assert cfg["spins"] == [5, 4, 2] and cfg["sigma"] == 1.5
    pop = np.exp(-np.arange(-5, 6)**2/(2*cfg["sigma"]**2))
    pop /= pop.sum()
    rho = np.diag(pop)
    b = {k: orientation(5, rho, k) for k in (0, 2, 4)}
    source_matrices = {k: np.array([[source_f(k, 0, k, ell, ellp, 5, 4)
                                   for ellp in (1, 2)] for ell in (1, 2)]) for k in (0, 2, 4)}
    assert np.allclose(source_matrices[0], np.eye(2), atol=2e-13)
    # Independent angular projection of the direct photon kernel into normalized coefficients.
    theta = np.array([0., 45., 90.])
    leg = np.array([[1., np.polynomial.legendre.legval(x, [0, 0, 1]),
                     np.polynomial.legendre.legval(x, [0, 0, 0, 0, 1])] for x in np.cos(np.deg2rad(theta))])
    coefficient_comparisons = []
    for delta in (0., .3, 1., -math.tan(math.radians(70)), 10.):
        amplitudes = np.array([1., delta])/math.sqrt(1+delta*delta)
        expected = np.array([b[k]*(amplitudes@source_matrices[k]@amplitudes) for k in (0, 2, 4)])
        source_ops = source_parts(math.atan(delta))
        observed = np.linalg.solve(leg, [singles(source_ops, rho, t) for t in theta])
        observed /= observed[0]
        wrong_ops = (("M", 1, amplitudes[0]), ("E", 2, amplitudes[1]))
        wrong = np.linalg.solve(leg, [singles(wrong_ops, rho, t) for t in theta])
        wrong /= wrong[0]
        assert np.max(abs(expected-observed))<2e-12
        coefficient_comparisons.append({"d_source": delta, "source_F_coefficients": expected.tolist(),
                                        "mapped_kernel_coefficients": observed.tolist(),
                                        "mapped_max_error": float(np.max(abs(expected-observed))),
                                        "unmapped_max_error": float(np.max(abs(expected-wrong)))})
    # Quadratic inverse witness: R_star fixed to a pure-dipole prediction, not a measured datum.
    pure_m, pure_q = (("M", 1, 1.),), (("E", 2, 1.),)
    both = (("M", 1, 1.), ("E", 2, -1.))
    def coefficients(first: tuple, second: tuple) -> np.ndarray:
        aa, cc = density(pure_m, rho, first, second), density(pure_q, rho, first, second)
        return np.array([aa, density(both, rho, first, second)-aa-cc, cc])
    numerator, denominator = coefficients((0., 0.), (90., 0.)), coefficients((90., 0.), (0., 0.))
    target = numerator[0]/denominator[0]
    root = -(numerator[1]-target*denominator[1])/(numerator[2]-target*denominator[2])
    roots = [0., float(root)]
    cases = {"E1_parity_changing": case((("E", 1, 1.),), rho),
             "M1_d0_same_parity": case(pure_m, rho),
             "M1_E2_exact_same_R": case(source_parts(math.atan(root)), rho),
             "source_minus70_degrees_illustration": case(source_parts(math.radians(-70.)), rho)}
    assert all(abs(cases[name]["R_star"]-target)<1e-12 for name in list(cases)[:3])
    # Source values are rounded author-model outputs; their rounding is not an error bar.
    printed = {"E1_parity_changing": (.34, .56, .56), "source_minus70_degrees_illustration": (.27, .44, .17)}
    for name, values in printed.items():
        assert all(abs(cases[name][key]-v)<.005 for key, v in zip(
            ("P_singles_gamma1", "P_POL_DIR_gamma1", "P_DIR_POL_gamma2"), values))
        assert abs(cases[name]["R_star"]-.4)<.05
    controls = []
    assert abs(small_d(1, 0, 1, math.pi/2)-1/math.sqrt(2))<1e-14
    for delta in (0., .3, root):
        parts = source_parts(math.atan(delta))
        closure = [float(np.max(abs(integrate_channel(5, 4, parts, nt, np_)-np.eye(11))))
                   for nt, np_ in ((6, 12), (12, 24))]
        assert max(closure)<2e-12
        identity_reference = integrate_channel(4, 2, (("E", 2, 1.),), 6, 12)
        assert np.max(abs(identity_reference-np.eye(9)))<2e-12
        isotropic = np.eye(11)/11
        random_case = case(parts, isotropic)
        assert abs(random_case["R_star"]-1)<1e-12 and abs(random_case["P_singles_gamma1"])<1e-12
        random_phi90 = polarization(parts, isotropic, 1, ((90., 0.), (90., 90.)))
        if delta == 0:
            assert abs(random_phi90)>1e-3  # No alignment does not imply zero conditional PDCO.
        opposite = density(parts, rho, (90., 0.), (90., 180.))
        parallel = density(parts, rho, (90., 0.), (90., 0.))
        assert abs(opposite-parallel)<1e-13
        for mode in (1, 2):
            assert abs(polarization(parts, rho, mode)-polarization(parts, rho, mode, ((90., 0.), (90., 0.))))<1e-12
            a0 = density(parts, rho, (90., 0.), (90., 180.), psi1=0. if mode == 1 else None, psi2=0. if mode == 2 else None)
            a90 = density(parts, rho, (90., 0.), (90., 180.), psi1=math.pi/2 if mode == 1 else None, psi2=math.pi/2 if mode == 2 else None)
            assert abs(a0+a90-opposite)<1e-13
        daughter = integrate_channel(5, 4, parts, 8, 16, rho)
        a2 = delta*delta/(1+delta*delta)
        feeding_checks = []
        for rank in (0, 2, 4):
            u = sum(weight*source_f(0, rank, rank, ell, ell, 5, 4)/math.sqrt(2*rank+1)
                    for ell, weight in ((1, 1-a2), (2, a2)))
            actual = orientation(4, daughter, rank)
            assert abs(actual-b[rank]*u)<2e-12
            feeding_checks.append({"rank": rank, "U": u, "daughter_B": actual, "source_B_times_U": b[rank]*u})
        controls.append({"d_source": delta, "channel_identity_max_errors": closure,
                         "isotropic_R": random_case["R_star"], "isotropic_singles_P": random_case["P_singles_gamma1"],
                         "isotropic_conditional_P1": random_case["P_POL_DIR_gamma1"],
                         "isotropic_conditional_P1_phi90": random_phi90,
                         "phi0_pi_density_difference": opposite-parallel, "daughter_tensor_checks": feeding_checks})
    result = {"data_identity": cfg["data_identity"], "data_kind": cfg["kind"],
              "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "source_scope": "Droste1996 printed519–524 Eqs2–7/12–21 and Fig7; model output only, not an experimental RDCO",
              "phase_map": {"d_source_definition": "a(E2)/a(M1) in D96 Eq3, for real amplitudes in this example",
                            "frozen_probe_definition": "same positive CG/Wigner basis with eta_M=lambda",
                            "derived_relation": "delta_probe=-d_source", "basis_order": ["M1", "E2"],
                            "relative_basis_matrix": [1, -1], "source_F": {str(k): a.tolist() for k, a in source_matrices.items()},
                            "comparison": coefficient_comparisons,
                            "not_yet_established": "No global KS70/Rose–Brink/D96 symbol conversion is claimed from this internal basis comparison"},
              "initial_population": pop.tolist(), "source_B": b, "R_star_definition": cfg["dco_chosen_convention"],
              "R_star_model_target": target, "source_coordinate_roots": roots,
              "root_atan_degrees": list(map(lambda x: math.degrees(math.atan(x)), roots)),
              "R_numerator_coefficients": numerator.tolist(), "R_denominator_coefficients": denominator.tolist(),
              "cases": cases, "controls": controls,
              "benchmark_rounding": "P compared at0.005 rounding halfwidth and R at0.05; these are printed precision checks, never experimental uncertainties",
              "boundaries": cfg["boundaries"]+["Full inter-source phase mapping and original Ref1 DCO numerator check remain separate tasks"]}
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir/"day16-pdco-ambiguity-preview.json").write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"R_star": target, "roots_d_source": roots, "atan_roots_degrees": result["root_atan_degrees"],
                      "cases": cases, "mapped_F_max_error": max(x["mapped_max_error"] for x in coefficient_comparisons),
                      "quadrature_identity_max_error": max(max(x["channel_identity_max_errors"]) for x in controls),
                      "status": "uncredited Day16 preview; source-model conditional calculation only"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
