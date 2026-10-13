#!/usr/bin/env python3
"""Day13 synthetic Voigt/gate exercise; source widths are not refitted data.

Energy units: keV. Natural Lorentz FWHM L=2*gamma and detector Gaussian
FWHM G=2*sqrt(2*log(2))*sigma are distinct parameters. The Voigt function
uses scipy.special.voigt_profile; independent convolution, normalization,
zero-kernel limits and finite-gate integrals check its interpretation.
https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.voigt_profile.html
No measured response, background, feeding, resonance interference or selection
packet is included. Broad illustrative L values are declared parameter choices.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import voigt_profile


GAUSSIAN_FWHM_FACTOR = 2 * math.sqrt(2 * math.log(2))


def profile(x: float, gaussian_fwhm: float, lorentz_fwhm: float) -> float:
    return float(voigt_profile(x, gaussian_fwhm / GAUSSIAN_FWHM_FACTOR,
                               lorentz_fwhm / 2))


def half_height_width(gaussian_fwhm: float, lorentz_fwhm: float) -> float:
    peak = profile(0., gaussian_fwhm, lorentz_fwhm)
    return 2 * brentq(lambda x: profile(x, gaussian_fwhm, lorentz_fwhm) - peak / 2,
                     0., 5 * (gaussian_fwhm + lorentz_fwhm), xtol=1e-11)


def gate_fraction(half_width: float, gaussian_fwhm: float, lorentz_fwhm: float) -> float:
    return 2 * quad(lambda x: profile(x, gaussian_fwhm, lorentz_fwhm),
                    0., half_width, epsabs=1e-11, epsrel=1e-11)[0]


def independent_convolution(x: float, gaussian_fwhm: float,
                            lorentz_fwhm: float) -> float:
    # Substitute a Lorentz-distributed displacement y=gamma*tan(t), so
    # L(y)dy=dt/pi. This computes the convolution without Faddeeva code.
    sigma = gaussian_fwhm / GAUSSIAN_FWHM_FACTOR
    gamma = lorentz_fwhm / 2
    return quad(lambda t: math.exp(-.5 * ((x - gamma * math.tan(t)) / sigma)**2)
                / (math.pi * math.sqrt(2 * math.pi) * sigma),
                -math.pi / 2, math.pi / 2, epsabs=1e-12, epsrel=1e-11,
                limit=200)[0]


def calculate() -> dict:
    # 0.0436 is the TUNL 15.11-MeV total-width central value in keV.
    # 119 is a Gaussian comparator inspired by Crespi's observed FWHM,
    # not a measured decomposition of that spectrum into kernels.
    choices = [(.0436, 119.), (20., 20.), (46., 5.), (0., 20.), (20., 0.)]
    cases = []
    normalization_error = 0.
    for lorentz, gaussian in choices:
        width = half_height_width(gaussian, lorentz)
        total = 2 * quad(lambda x: profile(x, gaussian, lorentz), 0., np.inf,
                         epsabs=2e-10, epsrel=2e-10, limit=200)[0]
        normalization_error = max(normalization_error, abs(total - 1))
        root_sum_square = math.hypot(gaussian, lorentz)
        cases.append({"lorentz_fwhm_keV": lorentz, "gaussian_fwhm_keV": gaussian,
                      "voigt_fwhm_keV": width, "incorrect_fwhm_quadrature_keV": root_sum_square,
                      "quadrature_relative_error": (root_sum_square - width) / width,
                      "normalization_integral": total,
                      "gates": [{"half_width_keV": h,
                                 "voigt_fraction": gate_fraction(h, gaussian, lorentz),
                                 "same_actual_FWHM_Gaussian_fraction":
                                 math.erf(h / (math.sqrt(2) * width / GAUSSIAN_FWHM_FACTOR))}
                                for h in (width / 2, width, 2 * width)]})
    convolution_errors = []
    for x in (0., 5., 20., 80.):
        direct = profile(x, 20., 20.)
        convolution_errors.append(abs(direct - independent_convolution(x, 20., 20.)))
    # A Cauchy line has no ordinary mean or finite variance. These are
    # unnormalized symmetric cutoff moments, not a measured sigma.
    gamma = 10.
    tail_moments = []
    for cutoff in (100., 1000., 10000.):
        exact = 2 * gamma / math.pi * (cutoff - gamma * math.atan(cutoff / gamma))
        numerical = 2 * quad(lambda x: x*x * profile(x, 0., 2*gamma),
                             0., cutoff, epsabs=1e-9, epsrel=1e-10)[0]
        assert abs(numerical - exact) / exact < 1e-10
        tail_moments.append({"symmetric_cutoff_keV": cutoff,
                             "unnormalized_second_moment_keV2": exact})
    assert normalization_error < 1e-8
    assert max(convolution_errors) < 1e-10
    assert abs(cases[3]["voigt_fwhm_keV"] - 20.) < 1e-9
    assert abs(cases[4]["voigt_fwhm_keV"] - 20.) < 1e-9
    assert abs(cases[1]["quadrature_relative_error"]) > .1
    assert tail_moments[2]["unnormalized_second_moment_keV2"] > 9 * tail_moments[1]["unnormalized_second_moment_keV2"]
    return {"schema_version": 1, "kind": "synthetic normalized lineshape/gate exercise; no experimental fit",
            "source_boundary": "TUNL total width and Crespi observed FWHM supply scales only; chosen Gaussian comparator is not the measured response",
            "cases": cases, "lorentz_cutoff_second_moments": tail_moments,
            "verification": {"normalization_max_error": normalization_error,
                             "independent_convolution_max_error_per_keV": max(convolution_errors),
                             "Gaussian_and_Lorentz_limits_passed": True,
                             "FWHM_quadrature_counterexample_passed": True,
                             "divergent_second_moment_check_passed": True, "passed": True},
            "dependencies": {"numpy": np.__version__, "scipy": scipy.__version__}}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = calculate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "verification": result["verification"],
                      "FWHM_cases_keV": [c["voigt_fwhm_keV"] for c in result["cases"]]}))


if __name__ == "__main__":
    main()
