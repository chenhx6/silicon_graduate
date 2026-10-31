#!/usr/bin/env python3
"""Declared beta+ sensitivity controls; NOT a LOGFT replay or experimental CI.

Inputs are 2010/2016 thesis central values, not the later journal publications.
The Sommerfeld factor used in checkpoint078 is a nonrelativistic point-Coulomb
approximation. A separate finite-radius Dirac Fermi function is a model control.
Neither calculation includes electron capture, screening, or a detector fit.
"""
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad, simpson
from scipy.special import loggamma

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01"
ME = 0.51099895  # MeV, declared fixed numerical input (not a new measurement)
ALPHA = 1 / 137.035999
Z = 49
R = 1.2 * 100 ** (1 / 3) / (197.3269804 / ME)  # dimensionless radius


def factor(w, convention):
    p = math.sqrt(w * w - 1)
    y = -ALPHA * Z * w / p  # repulsion for beta+
    if convention == "sommerfeld":
        x = 2 * math.pi * y
        return -x * math.exp(x) if x < -50 else x / (-math.expm1(-x))
    gamma = math.sqrt(1 - (ALPHA * Z) ** 2)
    return math.exp(
        math.log(2 * (1 + gamma))
        + (2 * gamma - 2) * math.log(2 * p * R)
        + math.pi * y
        + 2 * loggamma(complex(gamma, y)).real
        - 2 * math.lgamma(2 * gamma + 1)
    )


def spectrum(w, w0, convention):
    if w <= 1 or w >= w0:
        return 0.0
    return math.sqrt(w * w - 1) * w * (w0 - w) ** 2 * factor(w, convention)


def integrate(endpoint, convention):
    w0 = 1 + endpoint / ME
    q, err = quad(spectrum, 1, w0, args=(w0, convention), epsabs=1e-9, epsrel=1e-10)
    checks = []
    for n in (2000, 4000, 8000):
        x = np.linspace(1, w0, n + 1)
        val = float(simpson([spectrum(t, w0, convention) for t in x], x=x))
        checks.append({"intervals": n, "integral": val, "relative_to_quad": val / q - 1})
    assert abs(checks[-1]["relative_to_quad"]) < 1e-7
    return {"quad": q, "quadrature_error_estimate": err, "simpson": checks}


def audit():
    sources = []
    for path, pages in [
        ("raw/theses/degree-dissertation/Spectroscopy of the doubly magic nucleus 100Sn and its decay.pdf", [74, 75, 86, 87]),
        ("raw/theses/degree-dissertation/Decay Spectroscopy of 100 Sn and Neighboring Nuclei.pdf", [88, 89, 91, 92]),
    ]:
        sources.append({"path": path, "sha256": hashlib.sha256((ROOT / path).read_bytes()).hexdigest(), "targeted_pdf_pages": pages})
    models = {}
    for convention in ("sommerfeld", "dirac_finite_radius"):
        low = integrate(3.29, convention)
        high = integrate(3.74, convention)
        ratio = high["quad"] / low["quad"]
        models[convention] = {
            "f_beta_plus_at_3_29": low,
            "f_beta_plus_at_3_74": high,
            "ratio": ratio,
            "secant_log_sensitivity": math.log(ratio) / math.log(3.74 / 3.29),
            "conditional_B_ratio_if_same_branch": ratio * 1.17 / 1.16,
            "ratio_to_reported_B_ratio": ratio * 1.17 / 1.16 / (9.1 / 5.26),
            "is_explained_fraction": False,
        }
    inferred = {"hinke": 3811.5 / (1.16 * 9.1), "lubos": 3811.5 / (1.17 * 5.26)}
    assert abs(inferred["lubos"] - 619.33) < .01
    assert abs(models["sommerfeld"]["f_beta_plus_at_3_74"]["quad"] / inferred["lubos"] - 1) > .4
    return {
        "scope": "targeted primary-source identity and declared L2 integral controls",
        "sources": sources,
        "units": "E0 is maximum positron kinetic energy; W0=1+E0/me; f dimensionless",
        "approximation_contract": {"Z_daughter": Z, "A_for_radius": 100, "r0_fm": 1.2, "EC_included": False, "screening_included": False, "detector_response_fit": False},
        "models": models,
        "f_algebraically_implied_by_thesis_B_and_single_state_equation": inferred,
        "independence": "Back-solving f from B and T is an identity, not independent confirmation of the source calculator",
        "primary_source_corrections": [
            "Hinke printed76 Eq6.3 and printed77 name LOGFT; Appendix A.8 belongs to Lubos, not Hinke",
            "Lubos printed77 Q-spectrum has 1070 events after daughter/background subtraction; 2525 is identified 100Sn inventory",
            "Lubos printed80 Eq4.25/26/27 uses NNDC LOGFT; 304.25 is not the reported phase-space factor",
            "Lubos printed77 has 24 daughter beta+ components, not evidence for 24 parent GT final states",
            "Super GT is a strength-concentration label; it is not equivalent to an absence of quenching",
        ],
        "missing": ["original LOGFT version/options and EC convention", "matched parent branching", "original joint response/endpoint/half-life covariance", "later journal versions separately verified"],
        "experimental_CI": None,
        "quenching_verdict": None,
        "scientific_certification": False,
    }


if __name__ == "__main__":
    result = audit()
    out = RUN / "phase-space-scope-099.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"output": str(out.relative_to(ROOT)), "model_ratios": {k: v["ratio"] for k, v in result["models"].items()}, "implied_f": result["f_algebraically_implied_by_thesis_B_and_single_state_equation"], "experimental_CI": None}, ensure_ascii=False))
