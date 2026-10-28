#!/usr/bin/env python3
"""Reproducible conditional AMR double-shears/core-coupling calculation.

This is a semi-classical audit, not an EDF or projected many-body calculation.
It regenerates the tensor identities, the literal particle-plus-rotor mapping
used for 110Cd and 104Pd, the reported lifetime-derived data tables, and an
independent beta2 -> high-spin K=0 core B(E2) scale estimate.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PDF_ROY = ROOT / "raw/papers/gpt/day26-20261028/roy-2011-cd110-systematics-plb.pdf"
PDF_PD = ROOT / "raw/papers/gpt/day26-20261028/rather-2014-104pd-antimagnetic-arxiv1402.3422v1.pdf"


def blades(theta: float, phi: float = 0.0):
    s, c = math.sin(theta), math.cos(theta)
    x, y = s * math.cos(phi), s * math.sin(phi)
    return (x, y, c), (-x, -y, c)


def c2(n):
    x, y, z = n
    return {
        "C21": -math.sqrt(1.5) * z * complex(x, y),
        "C22": math.sqrt(3.0 / 8.0) * complex(x, y) ** 2,
    }


def tensor_pair(theta, phi=0.0, q1=1.0, q2=1.0):
    a, b = (c2(v) for v in blades(theta, phi))
    return {key: q1 * a[key] + q2 * b[key] for key in a}


def mu_pair(theta, phi=0.0, g1=1.0, g2=1.0, j1=4.5, j2=4.5):
    a, b = blades(theta, phi)
    return tuple(g1 * j1 * a[k] + g2 * j2 * b[k] for k in range(3))


def core_q0_eb(A: int, Z: int, beta2: float, r0: float = 1.2) -> float:
    """Uniform-charge axial rotor Q0 in e b, with R=r0 A^(1/3) fm."""
    radius_fm = r0 * A ** (1.0 / 3.0)
    return 3.0 / math.sqrt(5.0 * math.pi) * Z * radius_fm**2 * beta2 / 100.0


def rotor_cg2(I: int) -> float:
    """|<I 0, 2 0 | I-2 0>|^2 for a K=0 rotor."""
    return 3.0 * I * (I - 1.0) / (2.0 * (2.0 * I - 1.0) * (2.0 * I + 1.0))


def core_be2_high_spin(A: int, Z: int, beta2: float, I: int) -> float:
    q0 = core_q0_eb(A, Z, beta2)
    return 5.0 / (16.0 * math.pi) * q0**2 * rotor_cg2(I)


def omega_shears(c, j, vpn, vhh, n):
    return 1.5 * vpn / j * c - 6.0 * vhh / (n * j) * (2.0 * c * c - 1.0) * c


def spin_from_c(c, jh, jn, inertia, vpn, vhh, n):
    return jn + 2.0 * jh * c + inertia * omega_shears(c, jh, vpn, vhh, n)


def solve_cos(I, jh, jn, inertia, vpn, vhh, n):
    lo, hi = 0.0, 1.0
    flo = spin_from_c(lo, jh, jn, inertia, vpn, vhh, n) - I
    fhi = spin_from_c(hi, jh, jn, inertia, vpn, vhh, n) - I
    if flo * fhi > 0.0:
        return None
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        fm = spin_from_c(mid, jh, jn, inertia, vpn, vhh, n) - I
        if flo * fm <= 0.0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return 0.5 * (lo + hi)


def amr_be2(c, qeff_eb):
    return 15.0 / (32.0 * math.pi) * qeff_eb**2 * (1.0 - c * c) ** 2


def pdf_fingerprint(path, coverage):
    blob = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)), "sha256": hashlib.sha256(blob).hexdigest(),
            "bytes": len(blob), "coverage": coverage}


CD = [
    {"I": 16, "Egamma_keV": 1075, "tau_ps": 0.36, "tau_err_ps": 0.03, "BE2_e2b2": 0.14, "BE2_err": 0.01},
    {"I": 18, "Egamma_keV": 1224, "tau_ps": 0.23, "tau_err_ps": 0.03, "BE2_e2b2": 0.12, "BE2_err": 0.02},
    {"I": 20, "Egamma_keV": 1323, "tau_ps": 0.17, "tau_err_ps": 0.03, "BE2_e2b2": 0.11, "BE2_err": 0.02},
    {"I": 22, "Egamma_keV": 1314, "tau_ps": 0.21, "tau_err_ps": 0.07, "BE2_e2b2": 0.09, "BE2_err": 0.03},
    {"I": 24, "Egamma_keV": 1358, "tau_ps": 0.27, "tau_err_ps": 0.07, "BE2_e2b2": 0.06, "BE2_err": 0.02},
]
PD = [
    {"I": 16, "Egamma_keV": 927, "tau_ps": 0.45, "tau_err_ps": 0.03, "BE2_e2b2": 0.26, "BE2_err": 0.02, "ratio": 112.3},
    {"I": 18, "Egamma_keV": 1064, "tau_ps": 0.27, "tau_err_ps": 0.02, "BE2_e2b2": 0.22, "BE2_err": 0.02, "ratio": 140.9},
    {"I": 20, "Egamma_keV": 1193, "tau_ps": 0.18, "tau_err_ps": 0.01, "BE2_e2b2": 0.19, "BE2_err": 0.01, "ratio": 334.2},
    {"I": 22, "Egamma_keV": 1256, "tau_ps": 0.20, "tau_err_ps": 0.01, "BE2_e2b2": 0.13, "BE2_err": 0.01, "ratio": 282.3},
    {"I": 24, "Egamma_keV": 1365, "tau_ps": 0.24, "tau_err_ps": 0.02, "BE2_e2b2": 0.07, "BE2_err": 0.01, "ratio": 554.3},
    {"I": 26, "Egamma_keV": 1468, "tau_ps": 0.66, "tau_err_ps": 0.03, "BE2_e2b2": 0.02, "BE2_err": 0.01},
]


def main():
    max_c21 = max_mu = max_t22 = 0.0
    for it in range(181):
        theta = math.pi * it / 360.0
        for ip in range(73):
            phi = 2.0 * math.pi * ip / 73.0
            pair = tensor_pair(theta, phi)
            max_c21 = max(max_c21, abs(pair["C21"]))
            t22 = pair["C22"] / math.sqrt(3.0 / 8.0)
            max_t22 = max(max_t22, abs(t22 - 2.0 * math.sin(theta) ** 2 * complex(math.cos(2 * phi), math.sin(2 * phi))))
            m = mu_pair(theta, phi)
            max_mu = max(max_mu, math.hypot(m[0], m[1]))

    angle_rows = []
    for deg in (90, 70, 60, 45, 30, 15, 0):
        theta = math.radians(deg)
        angle_rows.append({"theta_deg": deg, "T22_abs_normalized": 2.0 * math.sin(theta) ** 2,
                           "BE2_over_B90": math.sin(theta) ** 4,
                           "drop_factor_from_90": None if deg == 0 else 1.0 / math.sin(theta) ** 4})

    model_rows = []
    for nucleus, levels, pars in [
        ("110Cd", CD, dict(jh=4.5, jn=10.0, inertia=19.5, vpn=1.2, vhh=.15, n=4, qeff=1.1)),
        ("104Pd", PD, dict(jh=4.5, jn=16.0, inertia=5.0, vpn=1.2, vhh=.2, n=8, qeff=1.3)),
    ]:
        for row in levels:
            c = solve_cos(row["I"], **{k: pars[k] for k in ("jh", "jn", "inertia", "vpn", "vhh", "n")})
            if c is None:
                continue
            model_rows.append({"nucleus": nucleus, "I": row["I"], "theta_deg": math.degrees(math.acos(c)),
                               "I_shears": pars["jn"] + 2 * pars["jh"] * c,
                               "R_core": pars["inertia"] * omega_shears(c, pars["jh"], pars["vpn"], pars["vhh"], pars["n"]),
                               "BE2_literal_model": amr_be2(c, pars["qeff"]),
                               "BE2_reported": row["BE2_e2b2"]})

    beta_rows = []
    for nucleus, A, Z in (("110Cd", 110, 48), ("104Pd", 104, 46)):
        for beta in (0.10, 0.12, 0.14):
            for I in (16, 20, 24):
                beta_rows.append({"nucleus": nucleus, "A": A, "Z": Z, "beta2": beta, "I": I,
                                  "Q0_eb": core_q0_eb(A, Z, beta),
                                  "B_E2_core_K0_e2b2": core_be2_high_spin(A, Z, beta, I)})

    result = {
        "status": "conditional-semiclassical-reproduction",
        "scope": "Geometry identities and particle-plus-rotor estimates; not an EDF or projected many-body wavefunction calculation.",
        "tensor_checks": {"theta_points": 181, "phi_points": 73, "max_abs_C21": max_c21,
                          "max_abs_T22_identity_residual": max_t22, "max_abs_mu_perp": max_mu},
        "angle_rows": angle_rows,
        "reported_data": {"110Cd": CD, "104Pd": PD},
        "literal_model_rows": model_rows,
        "beta2_core_scale_rows": beta_rows,
        "interpretation": {
            "mu_perp": "Zero requires equal blade magnetic weights; mismatch restores mu_perp linearly and B(M1) quadratically.",
            "B_E2": "The sin^4 law is the shears angular factor. A beta2=0.12 uniform-charge K=0 core gives roughly 0.07 e2 b2 for high-spin Delta-I=2 transitions, close to the 110Cd endpoint, but this is a scale estimate rather than an extracted core fraction.",
            "platform": "Core angular-momentum response slows theta closure; a core E2 amplitude must be added coherently if it is present. B values cannot be added incoherently without a phase convention.",
            "ratio": "Reported J(2)/B(E2) values are large because B(E2) decreases while J(2) remains finite; the ratio is diagnostic in context, not a universal exclusive threshold."
        },
        "sources": [
            pdf_fingerprint(PDF_ROY, "Roy 2011 PDF 5/5 pages; p.324 Table 1; pp.325-326 Eqs.3-6 and Fig.4"),
            pdf_fingerprint(PDF_PD, "Rather 2014 arXiv v1 11/11 PDF pages; pp.1-5 model/data text; p.11 Table I")
        ]
    }
    (HERE / "amr_double_shears_core.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    with (HERE / "angle_and_core_scale.csv").open("w", newline="") as fh:
        fields = list(angle_rows[0])
        writer = csv.DictWriter(fh, fieldnames=fields); writer.writeheader(); writer.writerows(angle_rows)
    with (HERE / "beta2_core_scale.csv").open("w", newline="") as fh:
        fields = list(beta_rows[0])
        writer = csv.DictWriter(fh, fieldnames=fields); writer.writeheader(); writer.writerows(beta_rows)
    print(json.dumps({"tensor_checks": result["tensor_checks"], "files": ["amr_double_shears_core.json", "angle_and_core_scale.csv", "beta2_core_scale.csv"]}, indent=2))


if __name__ == "__main__":
    main()
