#!/usr/bin/env python3
"""Point-gate Co60 joint photon density; no detector response or data fitting."""
from __future__ import annotations

import argparse
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day16_pdco_ambiguity_preview import small_d
from day16_ucgretina_stokes_oracle import cg_half, physical
from day16_co60_cascade_theory import intermediate_population


LINEAR_BASIS = np.array([[1, -1], [-1j, -1j]])/math.sqrt(2)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


@lru_cache(None)
def operators(ji2: int, jf2: int, parts: tuple, theta: float, phi: float, basis: str) -> np.ndarray:
    if basis not in ["native", "RB"]:
        raise ValueError("Unknown amplitude basis")
    norm = math.sqrt(sum(amp*amp for _, _, amp in parts))
    if norm == 0:
        raise ValueError("Zero transition amplitude")
    result = np.zeros((2, jf2+1, ji2+1), dtype=complex)
    for ih, helicity in enumerate([-1, 1]):
        for row, mf in enumerate(range(-jf2, jf2+1, 2)):
            for col, mi in enumerate(range(-ji2, ji2+1, 2)):
                mu = (mi-mf)//2
                for kind, ell, amplitude in parts:
                    if abs(mu) <= ell:
                        phase = (-1)**ell if basis == "native" else 1
                        result[ih, row, col] += (phase*amplitude/norm*math.sqrt((2*ell+1)/(8*math.pi))
                            *cg_half(jf2, mf, ell, mu, ji2, mi)*np.exp(1j*mu*phi)
                            *small_d(ell, mu, helicity, theta)*(helicity if kind == "M" else 1))
    return result


def joint(parts: tuple, first: tuple, last: tuple, basis: str = "native") -> np.ndarray:
    h1 = operators(8, 4, parts, *first, basis)
    h2 = operators(4, 0, (("E", 2, 1.),), *last, basis)
    return np.einsum("bj,aji->abi", h2[:, 0, :], h1)


def check_joint_density(amplitudes: np.ndarray) -> dict:
    vector = amplitudes.reshape(4, 9)
    matrix = vector@vector.conj().T/9
    trace = float(np.trace(matrix).real)
    assert trace > 0 and np.max(abs(matrix-matrix.conj().T))/trace < 1e-12
    normalized = matrix/trace
    eigenvalues = np.linalg.eigvalsh(normalized)
    assert eigenvalues.min() > -1e-12 and abs(np.trace(normalized)-1) < 1e-12
    return {"eigenvalues_normalized": eigenvalues.tolist(), "trace": trace}


def reduced_helicity(amplitudes: np.ndarray, role: str) -> np.ndarray:
    if role == "first":
        return np.einsum("abi,cbi->ac", amplitudes, amplitudes.conj())/9
    if role == "last":
        return np.einsum("abi,aci->bc", amplitudes, amplitudes.conj())/9
    raise ValueError("Unknown target photon role")


def stokes(helicity: np.ndarray, normalization: float) -> dict:
    linear = LINEAR_BASIS@helicity@LINEAR_BASIS.conj().T
    trace = float(np.trace(linear).real)
    assert trace >= 0
    scale = max(trace, np.finfo(float).tiny)
    assert np.max(abs(linear-linear.conj().T))/scale < 1e-12
    eigenvalues = np.linalg.eigvalsh(linear)
    assert eigenvalues.min() >= -1e-12*scale
    iquv = normalization*np.array([trace, (linear[0, 0]-linear[1, 1]).real,
                                   2*linear[0, 1].real, -2*linear[0, 1].imag])
    normalized = iquv[1:]/iquv[0] if trace > 0 else None
    if normalized is not None:
        assert np.dot(normalized, normalized) <= 1+1e-12
    return {"IQUV": iquv.tolist(), "normalized_Stokes": normalized.tolist() if trace > 0 else None,
            "linear_density_eigenvalues_over_trace": (eigenvalues/scale).tolist()}


def configuration(parts: tuple, angle: float, role: str, basis: str = "native", phi: float = 0) -> dict:
    target, reference = (angle, phi), (0., phi)
    first, last = (target, reference) if role == "first" else (reference, target)
    return stokes(reduced_helicity(joint(parts, first, last, basis), role), (4*math.pi)**2)


def ungated(parts: tuple, role: str, target_angle: float) -> dict:
    nodes, weights = np.polynomial.legendre.leggauss(12)
    rho = np.zeros((2, 2), dtype=complex)
    for cosine, weight in zip(nodes, weights):
        for phi in np.arange(16)*2*math.pi/16:
            reference, target = (math.acos(cosine), float(phi)), (target_angle, 0.)
            first, last = (target, reference) if role == "first" else (reference, target)
            rho += weight*2*math.pi/16*reduced_helicity(joint(parts, first, last), role)
    return stokes(rho, 4*math.pi)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.contract.read_text())
    assert cfg["identity"] == "CO60-JOINT-CONDITIONAL-STOKES-01"
    level = Path(cfg["leveldata"])
    assert sha(level) == cfg["leveldata_sha256"]
    delta = cfg["first_gamma"]["delta_native"]
    cases = {"pureE2first": ((("E", 2, 1.),), "native"),
             "actualmixednative": ((("E", 2, 1.), ("M", 3, delta)), "native"),
             "actualmixedRBsamephysics": ((("E", 2, 1.), ("M", 3, -delta)), "RB"),
             "pureM3upperpositive": ((("M", 3, 1.),), "native"),
             "pureM3uppernegativeglobalphasecontrol": ((("M", 3, -1.),), "native")}
    assert set(cases) == set(cfg["cases"])
    rows = []
    joint_controls = []
    maximum_scalar_role_error = maximum_rotation_error = maximum_last_density_error = 0.
    me = cfg["KNconditionaldesign"]["electron_rest_keV"]
    for name, (parts, basis) in cases.items():
        for degree in cfg["angles_deg"]:
            angle = math.radians(degree)
            for role in ["first", "last"]:
                first, last = ((angle, 0.), (0., 0.)) if role == "first" else ((0., 0.), (angle, 0.))
                joint_controls.append({"case": name, "target_photon": role,
                    "gamma_gamma_angle_deg": degree,
                    **check_joint_density(joint(parts, first, last, basis))})
            values = {}
            for role in ["first", "last"]:
                value = configuration(parts, angle, role, basis)
                rotated = configuration(parts, angle, role, basis, phi=.37)
                maximum_rotation_error = max(maximum_rotation_error,
                    float(np.max(abs(np.array(value["IQUV"])-rotated["IQUV"]))))
                energy = cfg["first_gamma" if role == "first" else "last_gamma"]["energy_keV"]
                r = 1/(1+energy/me)  # The frozen free-electron point example uses psi=90 degrees.
                sigma = 1/(r+1/r-1)
                value.update(case=name, target_photon=role, gamma_gamma_angle_deg=degree,
                             reference_plane_defined=degree not in [0, 180],
                             free_electron_point_KN_analyzing_power=sigma,
                             conditional_point_cos2_amplitude=sigma*value["normalized_Stokes"][0]
                             if degree not in [0, 180] else None)
                assert max(abs(value["normalized_Stokes"][1]), abs(value["normalized_Stokes"][2])) < 1e-12
                values[role] = value
                rows.append(value)
            maximum_scalar_role_error = max(maximum_scalar_role_error,
                abs(values["first"]["IQUV"][0]-values["last"]["IQUV"][0]))
            if name in ["pureE2first", "actualmixednative"]:
                population = intermediate_population(0 if name == "pureE2first" else delta, True)
                independent = physical({"Ji2": 4, "Jf2": 0, "MP": 4}, 0, angle, 0, population)
                maximum_last_density_error = max(maximum_last_density_error,
                    abs(independent["W"]-values["last"]["IQUV"][0]),
                    float(np.max(abs(np.array(independent["Stokes"])-values["last"]["normalized_Stokes"]))))
    def compare_cases(a, b):
        ra, rb = ([r for r in rows if r["case"] == name] for name in [a, b])
        return max(float(np.max(abs(np.array(x["IQUV"])-y["IQUV"]))) for x, y in zip(ra, rb))
    bridge = compare_cases("actualmixednative", "actualmixedRBsamephysics")
    global_phase = compare_cases("pureM3upperpositive", "pureM3uppernegativeglobalphasecontrol")
    pure_role_difference = max(abs(a["normalized_Stokes"][0]-b["normalized_Stokes"][0])
        for a, b in zip([r for r in rows if r["case"] == "pureE2first" and r["target_photon"] == "first"],
                        [r for r in rows if r["case"] == "pureE2first" and r["target_photon"] == "last"]))
    marginal = []
    for name in ["pureE2first", "actualmixednative"]:
        for role in ["first", "last"]:
            value = ungated(cases[name][0], role, math.pi/3)
            assert abs(value["IQUV"][0]-1) < 1e-12 and max(abs(x) for x in value["normalized_Stokes"]) < 1e-12
            marginal.append({"case": name, "target_photon": role, **value})
    spin2_controls = []
    maximum_spin2_error = 0.
    for name in ["pureE2first", "actualmixednative"]:
        parts, basis = cases[name]
        for role in ["first", "last"]:
            base = None
            for phi in [0., math.pi/4, math.pi/2]:
                target, reference = (0., 0.), (math.pi/3, phi)
                first, last = (target, reference) if role == "first" else (reference, target)
                value = stokes(reduced_helicity(joint(parts, first, last, basis), role), (4*math.pi)**2)
                z = complex(*value["IQUV"][1:3])
                if base is None:
                    base = z
                error = abs(z-base*np.exp(2j*phi))
                maximum_spin2_error = max(maximum_spin2_error, error)
                spin2_controls.append({"case": name, "target_photon": role,
                    "reference_phi_rad": phi, "IQUV_in_fixed_target_axes": value["IQUV"],
                    "spin2_relation_error": error})
    assert max(bridge, global_phase, maximum_scalar_role_error, maximum_rotation_error,
               maximum_last_density_error, maximum_spin2_error) < 1e-12
    result = {"identity": cfg["identity"], "contract_sha256": sha(args.contract),
        "script_sha256": sha(Path(__file__)), "leveldata_sha256": sha(level), "rows": rows,
        "control_residuals": {"native_RB_IQUV": bridge, "pureM3_global_phase": global_phase,
            "scalar_intensity_first_last_roles": maximum_scalar_role_error,
            "common_Rz_local_axes": maximum_rotation_error,
            "last_target_independent_population_route": maximum_last_density_error,
            "reference_plane_spin2_in_fixed_target_axes": maximum_spin2_error},
        "pureE2_first_last_Qnorm_difference_observed": pure_role_difference,
        "ungated_full_reference_solidangle_controls": marginal,
        "explicit_full_joint_density_controls": joint_controls,
        "reference_plane_spin2_controls": spin2_controls,
        "all_density_physicality_controls_passed": True,
        "new_MC_polarization_or_experimental_Q_delta_fit": False,
        "scope": "point reference/rest frame/real amplitudes; no finite-detector calibration or measured Stokes"}
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n")
    ninety = [{k: row[k] for k in ["case", "target_photon", "IQUV", "normalized_Stokes", "conditional_point_cos2_amplitude"]}
              for row in rows if row["gamma_gamma_angle_deg"] == 90]
    print(json.dumps({"90_degree_rows": ninety, "controls": result["control_residuals"],
                     "pureE2_role_Q_difference_observed": pure_role_difference,
                     "ungated_controls": marginal}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
