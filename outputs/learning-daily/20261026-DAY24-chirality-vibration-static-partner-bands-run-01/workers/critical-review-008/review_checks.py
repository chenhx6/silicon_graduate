"""Independent fixed-gyro checks of OL02 v1, not an HF/quantum replay."""
from pathlib import Path
import json
import math
import numpy as np
from scipy.optimize import brentq, minimize_scalar

OUT = Path(__file__).resolve().parent
J = np.array([8.5, 31.0, 20.0])  # hbar^2/MeV, order s,m,l
s = np.array([5.43, 0.0, 5.00])  # hbar
ws = s[0] / (J[1] - J[0])
wl = s[2] / (J[1] - J[2])
wc = math.hypot(ws, wl)  # MeV/hbar
Icrit = J[1] * wc
checks = []


def check(name, condition, **evidence):
    assert bool(condition), (name, evidence)
    checks.append(dict(name=name, passed=True, **evidence))


def planar_radius(mu):
    return math.hypot(s[0] / (mu - J[0]), s[2] / (mu - J[2]))


def tangent_basis(v):
    # Independent SVD nullspace of the radius constraint gradient.
    return np.linalg.svd(np.asarray(v).reshape(1, 3))[2][1:].T


def reduced_hessian(v, h):
    T = tangent_basis(v)
    return np.linalg.eigvalsh(T.T @ np.diag(h) @ T)


# Eq5 independently: minimize the direct planar radius inside (Js,Jl).
q = minimize_scalar(planar_radius, bounds=(J[0] + 1e-6, J[2] - 1e-6), method="bounded")
wthr_formula = (s[0] ** (2 / 3) + s[2] ** (2 / 3)) ** (3 / 2) / abs(J[2] - J[0])
check("direct-planar-minimum-versus-Eq5", abs(q.fun - wthr_formula) < 2e-12,
      optimizer_mu=float(q.x), direct_omega=float(q.fun), formula_omega=float(wthr_formula))
check("planar-threshold-distinct-from-aplanar-onset", wthr_formula > wc,
      omega_planar_threshold=wthr_formula, omega_aplanar_onset=wc)

# Independent direct Euler-vector / fixed-I Hamiltonian route.
aplanar = []
for omega in [wc, 0.6, 0.75]:
    wmabs = math.sqrt(max(0.0, omega * omega - wc * wc))
    for sign in ([1] if omega == wc else [-1, 1]):
        w = np.array([ws, sign * wmabs, wl])
        I = J * w + s
        cross = np.cross(w, I)
        H_velocity = float(np.sum(J * w * w) / 2)
        H_momentum = float(np.sum((I - s) ** 2 / J) / 2)
        rcurv = reduced_hessian(w, J[1] - J)
        ecurv = reduced_hessian(I, 1 / J - 1 / J[1])
        check(f"Euler-and-Legendre-omega{omega:.9f}-sign{sign}",
              np.linalg.norm(cross) < 2e-15 and np.max(abs(I - J[1] * w)) < 2e-15
              and abs(H_velocity - H_momentum) < 2e-15,
              cross_norm=float(np.linalg.norm(cross)), I_norm=float(np.linalg.norm(I)),
              H_from_velocity=H_velocity, H_from_momentum=H_momentum)
        if omega == wc:
            check("threshold-has-one-zero-tangent-curvature",
                  abs(rcurv[0]) < 1e-12 and rcurv[1] > 0 and abs(ecurv[0]) < 1e-12,
                  routhian_curvatures=rcurv.tolist(), energy_curvatures=ecurv.tolist())
        else:
            check(f"positive-tangent-curvatures-omega{omega}-sign{sign}",
                  min(rcurv) > 0 and min(ecurv) > 0,
                  routhian_curvatures=rcurv.tolist(), energy_curvatures=ecurv.tolist())
        Hred = H_momentum - np.dot(I, I) / (2 * J[1])
        constant = -.5 * (s[0] ** 2 / (J[1] - J[0]) + s[2] ** 2 / (J[1] - J[2]))
        check(f"Fig6-reference-subtraction-omega{omega:.9f}-sign{sign}",
              abs(Hred - constant) < 4e-15,
              H_minus_I2_over_2Jm=float(Hred), analytic_constant=float(constant))
        aplanar.append(dict(omega=omega, sign=sign, omega_vector=w.tolist(),
                            I_vector=I.tolist(), I_norm=float(np.linalg.norm(I)),
                            routhian_curvatures=rcurv.tolist(), energy_curvatures=ecurv.tolist()))

check("below-threshold-no-real-medium-component", .5 ** 2 - wc ** 2 < 0,
      radicand=float(.5 ** 2 - wc ** 2))

# Planar A continuation: crossing Jm changes its m-direction curvature.
for omega in [.5, .6]:
    mu = brentq(lambda x: planar_radius(x) - omega, J[2] + 1e-6, 1000)
    w = np.array([s[0] / (mu - J[0]), 0.0, s[2] / (mu - J[2])])
    eig = reduced_hessian(w, mu - J)
    check(f"planar-A-tangent-sign-omega{omega}",
          (eig[0] > 0 if omega < wc else eig[0] < 0 < eig[1]),
          mu=float(mu), curvatures=eig.tolist())

# Source's lower-level ambiguities do not change this declared parameter model.
check("inertia-rescaling-limit", abs(math.hypot(s[0] / (2 * (J[1] - J[0])),
                                                        s[2] / (2 * (J[1] - J[2]))) - wc / 2) < 1e-15)
check("gyro-rescaling-limit", abs(math.hypot(2 * ws, 2 * wl) - 2 * wc) < 1e-15)
check("reduced-positive-inertia-gaps-raise-threshold", math.hypot(ws / .9, wl / .9) > wc)
check("enlarged-positive-inertia-gaps-lower-threshold", math.hypot(ws / 1.1, wl / 1.1) < wc)
check("zero-one-gyro-does-not-give-three-nonzero-components", 0.0 / (J[1] - J[0]) == 0.0)

result = dict(
    source_body="tmp/day24-critical-tac-007/arxiv-0211075v1.response",
    scope="Fixed positive diagonal inertias and two frozen nonzero s/l gyros; hbar units retained symbolically. No HF/RPA/quantum or nuclear fit.",
    scalar_results=dict(omega_s=ws, omega_l=wl, omega_critical=wc,
                        continuous_Icrit=Icrit, omega_planar_threshold=wthr_formula,
                        medium_component_at_omega_06=math.sqrt(.6**2-wc**2),
                        Fig6_reduced_energy_constant=constant),
    ap_branches=aplanar, checks=checks, passed=len(checks),
    units=dict(omega="MeV/hbar", I="hbar", J_and_mu="hbar^2/MeV", energy="MeV"),
    boundaries=["Numerical tolerances are floating-point checks, not physical uncertainty.",
                "Threshold zero curvature is not a calculated quantum/RPA zero mode.",
                "Conditional Icrit is not a quantum-spin assignment.",
                "Gyro/mass deformation variation and singular equal-inertia limits require their own model."])
(OUT / "review-checks.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(dict(passed=len(checks), scalar_results=result["scalar_results"]), indent=2))
