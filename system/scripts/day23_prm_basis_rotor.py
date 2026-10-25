#!/usr/bin/env python3
"""ST18 K/R basis and Hcoll component controls; no full PRM/electromagnetic fit."""
import argparse
import json
import math
from pathlib import Path

import numpy as np


def factorial_integer(x):
    value = int(round(x))
    if value < 0 or abs(x-value) > 1e-9:
        raise ValueError("Angular momentum factorial argument is not a nonnegative integer")
    return math.factorial(value)


def clebsch_gordan(j1, m1, j2, m2, total, projection):
    if (abs(m1+m2-projection) > 1e-9 or total > j1+j2 or total < abs(j1-j2)
            or abs(m1) > j1 or abs(m2) > j2 or abs(projection) > total):
        return 0.0
    f = factorial_integer
    front = math.sqrt((2*total+1)*f(total+j1-j2)*f(total-j1+j2)*f(j1+j2-total)
                      / f(j1+j2+total+1))
    front *= math.sqrt(f(total+projection)*f(total-projection)*f(j1-m1)*f(j1+m1)
                       * f(j2-m2)*f(j2+m2))
    lo = int(round(max(0, j2-total-m1, j1+m2-total)))
    hi = int(round(min(j1+j2-total, j1-m1, j2+m2)))
    return front*sum((-1)**k/(f(k)*f(j1+j2-total-k)*f(j1-m1-k)*f(j2+m2-k)
                               * f(total-j2+m1+k)*f(total-j1-m2+k))
                     for k in range(lo, hi+1))


def transformation(two_i, two_j):
    if min(two_i, two_j) < 1 or two_i % 2 != 1 or two_j % 2 != 1:
        raise ValueError("This component implements odd-mass half-integer I and j only")
    strong = [(k/2, o/2) for k in range(-two_i, two_i+1, 2)
              for o in range(-two_j, two_j+1, 2)
              if k-o >= 0 and (k-o) % 4 == 0 and (k != o or k > 0)]
    weak = [(r, kr) for r in range(abs(two_i-two_j)//2, (two_i+two_j)//2+1)
            for kr in range(0, r+1, 2) if kr or r % 2 == 0]
    u = np.array([[math.sqrt((2*r+1)/(two_i+1))
                   * clebsch_gordan(two_j/2, o, r, kr, two_i/2, k)
                   * math.sqrt(1+(kr == 0)) if abs(k-o-kr) < 1e-9 else 0
                   for r, kr in weak] for k, o in strong])
    return strong, weak, u


def spin_matrices(two_j):
    j = two_j/2
    m = np.arange(-two_j, two_j+1, 2)/2
    plus = np.zeros((two_j+1, two_j+1), complex)
    for n, value in enumerate(m[:-1]):
        plus[n+1, n] = math.sqrt((j-value)*(j+value+1))
    return [(plus+plus.T.conj())/2, (plus-plus.T.conj())/(2j), np.diag(m)]


def direct_rotor(two_i, two_j, strong, inertia):
    # Eq6 symmetrized |K,Omega> and |-K,-Omega> embedding.
    embed = np.zeros(((two_i+1)*(two_j+1), len(strong)))
    phase = (-1)**((two_i-two_j)//2)
    for col, (k, o) in enumerate(strong):
        a, b = int(round(k+two_i/2)), int(round(o+two_j/2))
        embed[a*(two_j+1)+b, col] = 1/math.sqrt(2)
        embed[(two_i-a)*(two_j+1)+(two_j-b), col] = phase/math.sqrt(2)
    body_i, particle_j = spin_matrices(two_i), spin_matrices(two_j)
    # Body-fixed total I has anomalous commutators; simply using three
    # ordinary spin matrices here would give the wrong Coriolis terms.
    body_i[1] *= -1
    h = np.zeros((embed.shape[0], embed.shape[0]), complex)
    for ik, jk, moment in zip(body_i, particle_j, inertia):
        r = np.kron(ik, np.eye(two_j+1))-np.kron(np.eye(two_i+1), jk)
        h += r@r/(2*moment)
    return embed.T@h@embed, embed


def rotor_blocks(weak, inertia):
    h = np.zeros((len(weak), len(weak)), complex)
    for r in sorted({r for r, _ in weak}):
        indices = [n for n, (rr, _) in enumerate(weak) if rr == r]
        project = np.zeros((2*r+1, len(indices)))
        for col, index in enumerate(indices):
            kr = weak[index][1]
            denominator = math.sqrt(2*(1+(kr == 0)))
            project[r+kr, col] += 1/denominator
            project[r-kr, col] += (-1)**r/denominator
        hr = sum(x@x/(2*moment) for x, moment in zip(spin_matrices(2*r), inertia))
        h[np.ix_(indices, indices)] = project.T@hr@project
    return h


def verify():
    inertia = [13.0, 21.0, 4.0]  # ST18 SecIII, axes s/i/l, hbar^2/MeV.
    rows, controls = [], {}
    controls["CG_half_spin_singlet_phase"] = math.isclose(
        clebsch_gordan(.5, .5, .5, -.5, 0, 0), 1/math.sqrt(2), abs_tol=1e-14)
    controls["CG_stretched_state"] = math.isclose(
        clebsch_gordan(1.5, 1.5, 2, 2, 3.5, 3.5), 1, abs_tol=1e-14)
    for two_i, two_j in [(1, 1), (3, 1), (11, 11), (13, 11), (17, 11), (25, 11)]:
        strong, weak, u = transformation(two_i, two_j)
        h_direct, embed = direct_rotor(two_i, two_j, strong, inertia)
        h_weak = rotor_blocks(weak, inertia)
        ortho = max(float(np.max(abs(u.T@u-np.eye(len(weak))))),
                    float(np.max(abs(u@u.T-np.eye(len(strong))))))
        matrix_error = float(np.max(abs(h_direct-u@h_weak@u.T)))
        spherical = rotor_blocks(weak, [10.0]*3)
        exact_spherical = np.diag([r*(r+1)/20 for r, kr in weak])
        spherical_error = float(np.max(abs(spherical-exact_spherical)))
        tag = f"I2_{two_i}_j2_{two_j}"
        controls[tag+"_orthogonal_complete_bases"] = u.shape[0] == u.shape[1] and ortho < 1e-12
        controls[tag+"_two_route_rotor_H"] = matrix_error < 1e-11
        controls[tag+"_spherical_rotor_limit"] = spherical_error < 1e-11
        rows.append({"two_I": two_i, "two_j": two_j, "dimension": len(strong),
                     "orthogonality_error": ortho, "Hcoll_two_route_error_MeV": matrix_error,
                     "spherical_limit_error_MeV": spherical_error})
    strong, weak, u = transformation(13, 11)
    odd = np.array([r % 2 == 1 for r, kr in weak])
    chosen_strong = np.zeros(len(strong)); chosen_strong[0] = 1
    missing_norm = float(sum(abs(u[:, odd].T@chosen_strong)**2))
    a, b = weak.index((2, 0)), weak.index((2, 2))
    chosen_coherent = (u[:, a]+u[:, b])/math.sqrt(2)
    probabilities = abs(u.T@chosen_coherent)**2
    expected = np.zeros(len(weak)); expected[a] = expected[b] = .5
    incoherent = (abs(u)**2).T@(abs(chosen_coherent)**2)
    controls["D2_excludes_R1_but_permits_higher_oddR"] = all(r != 1 for r, kr in weak) and int(sum(odd)) == 15
    controls["amplitudes_preserve_coherent_probability"] = bool(np.allclose(probabilities, expected, atol=1e-12))
    return {"status": "source_component_controls", "source": "knowledge/sources/streck-2018-behavior-collective-rotor-wobbling.md",
            "locators": ["ST18-D23-001", "ST18-D23-002"],
            "scope": "Source K/R representation and Hcoll only. No intrinsic C, pairing, EM operators, full PRM eigenstates or experimental fit/mode assignment.",
            "units": {"angular_momentum": "hbar", "inertia": "hbar2/MeV", "Hcoll": "MeV"},
            "source_inertias_s_i_l": inertia, "results": rows,
            "chosen_state_controls": {"label": "declared basis/algebra controls, no nuclear eigenstate identity",
                "I": 6.5, "j": 5.5, "strong_dimension": len(strong), "oddR_components": int(sum(odd)),
                "first_strong_basis_K_Omega": strong[0], "evenR_only_discarded_norm": missing_norm,
                "coherent_weak_components": [[2, 0, .5], [2, 2, .5]],
                "incoherent_probability_L1_difference": float(sum(abs(incoherent-probabilities)))},
            "controls": controls, "all_controls_pass": all(controls.values()),
            "readiness": {"complete_for": ["basis transformation", "rotor Hamiltonian component"],
                          "missing_for_original_model_replay": ["explicit selection and verification of cited C(beta) prescription/value", "pairing implementation/occupation", "complete E2/M1 operator inputs", "original code and data response/Cov"]}}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    result = verify()
    a.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"all_controls_pass": result["all_controls_pass"], "checks": len(result["controls"]),
                      "max_Hcoll_two_route_error_MeV": max(x["Hcoll_two_route_error_MeV"] for x in result["results"])}))
    return 0 if result["all_controls_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
