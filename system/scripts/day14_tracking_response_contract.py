#!/usr/bin/env python3
"""Source-to-beam response/measure controls; no GRETINA reanalysis.

Published beta, line energy and angular coverage provide a conditional photon
kinematics example. Source histograms/interpolation below are explicitly chosen
and do not reproduce the author's response construction or covariance.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from math import atanh, cos, pi, radians, sin, sqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02"


def aberration(x, beta):
    return (x-beta)/(1-beta*x)


def jacobian(x, beta):
    return (1-beta*beta)/(1-beta*x)**2


def photon_energy(rest_energy, x, beta):
    return rest_energy*sqrt(1-beta*beta)/(1-beta*x)


def simpson(f, lo, hi, n=10000):
    h = (hi-lo)/n
    return h/3*(f(lo)+f(hi)+sum((4 if i % 2 else 2)*f(lo+i*h) for i in range(1, n)))


def normalization_cov(counts):
    """First-order propagation for independent Poisson means, exact arithmetic.

    The same expression is exact conditional on a fixed multinomial total;
    it is not the exact unconditional finite-count ratio covariance.
    """
    n = [F(x) for x in counts]
    t = sum(n)
    p = [x/t for x in n]
    jac = [[(F(i == k)*t-n[i])/t**2 for k in range(len(n))] for i in range(len(n))]
    propagated = [[sum((jac[i][k]*n[k]*jac[j][k] for k in range(len(n))), F(0))
                   for j in range(len(n))] for i in range(len(n))]
    closed = [[(F(i == j)*p[i]-p[i]*p[j])/t for j in range(len(n))] for i in range(len(n))]
    assert propagated == closed
    return p, closed


def mix(a, b, weight):
    return [(1-weight)*x+weight*y for x, y in zip(a, b)]


def covariance_mix(a, b, w, z=None):
    z = w if z is None else z
    return [[(1-w)*(1-z)*x+w*z*y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def safe_ratio(n, r):
    if r <= 0:
        raise ValueError("response has no positive support; exclude/model this bin")
    return n/r


def determinant3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            - a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            + a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=RUN / "tracking-response-contract-audit.json")
    args = parser.parse_args()
    path = RUN / "tracking-response-contract-input.json"
    data = json.loads(path.read_text())
    checks = {}
    def check(name, value):
        checks[name] = bool(value)
        if not value:
            raise AssertionError(name)
    for role in ["local_manuscript", "publisher_pdf"]:
        p = ROOT/data[role]["path"]
        check(role+"_sha256", hashlib.sha256(p.read_bytes()).hexdigest() == data[role]["sha256"])
    beta, e0 = float(data["beta"]), float(data["line_rest_energy_keV"])
    rows = []
    for angle in data["chosen_angles_within_published_coverage_deg"]:
        x = cos(radians(angle))
        u = aberration(x, beta)
        elab = photon_energy(e0, x, beta)
        gamma = 1/sqrt(1-beta*beta)
        energy_prime = gamma*elab*(1-beta*x)
        pz_prime = gamma*elab*(x-beta)
        pt_prime = elab*sqrt(1-x*x)
        check(f"photon_boost_inverse_{angle}", abs(energy_prime-e0) < 1e-9
              and abs(pz_prime/energy_prime-u) < 1e-12
              and abs((pz_prime*pz_prime+pt_prime*pt_prime)/energy_prime**2-1) < 1e-12)
        j = jacobian(x, beta)
        check(f"CM_and_lab_jacobian_{angle}", abs(j-(1+beta*u)**2/(1-beta*beta)) < 1e-12)
        rows.append(dict(lab_angle_deg=angle, CM_cosine=u, lab_energy_keV=elab,
                         solid_angle_jacobian=j,
                         literal_Eq19_using_CM_theta=jacobian(u, beta)))
    check("zero_beta_limit", aberration(.3, 0) == .3 and jacobian(.3, 0) == 1
          and photon_energy(e0, .3, 0) == e0)
    check("full_solid_angle_number_normalization", abs(simpson(lambda x: jacobian(x, beta), -1, 1)/2-1) < 1e-12)
    for x in [-.75, 0, .25]:
        h = 1e-6
        check(f"independent_finite_difference_at_{x}", abs((aberration(x+h, beta)-aberration(x-h, beta))/(2*h)-jacobian(x, beta)) < 2e-10)
    # If the theta in Eq19 is literally CM as defined before Eq18, this is
    # the factor integrated over lab solid angle. It is not the author's code.
    wrong_integral = simpson(lambda x: jacobian(aberration(x, beta), beta), -1, 1)/2
    analytic_wrong = (1-beta*beta)/2+(1-beta*beta)**2*atanh(beta)/(2*beta)
    check("literal_CM_factor_integral_independent_formula", abs(wrong_integral-analytic_wrong) < 1e-12)
    check("literal_CM_factor_is_not_number_normalized", abs(wrong_integral-1) > 1e-5)
    check("theta_histogram_measure_needs_sine", abs(simpson(sin, 0, pi)-2) < 1e-12)
    p0, v0 = normalization_cov(data["chosen_source_counts"][0])
    p1, v1 = normalization_cov(data["chosen_source_counts"][1])
    w, z = map(F, data["chosen_interpolation_weights"])
    response = mix(p0, p1, w)
    vr = covariance_mix(v0, v1, w)
    cross = covariance_mix(v0, v1, w, z)
    check("normalized_source_covariance_rows_zero", all(sum(row) == 0 for v in [v0, v1, vr, cross] for row in v))
    check("normalization_induces_negative_offdiagonal", all(vr[i][j] < 0 for i in range(3) for j in range(3) if i != j))
    check("source_interpolation_preserves_normalization", sum(response) == 1 and min(response) > 0)
    naive = (1-w)*v0[0][0]+w*v1[0][0]
    check("linear_variance_interpolation_is_not_independent_linear_estimator_variance", naive != vr[0][0])
    check("different_target_energies_share_source_covariance", cross[0][0] > 0)
    counts = list(map(F, data["chosen_independent_beam_counts"]))
    ratio = [safe_ratio(n, r) for n, r in zip(counts, response)]
    vy = [[(counts[i]/response[i]**2 if i == j else F(0))
           + counts[i]*counts[j]*vr[i][j]/(response[i]**2*response[j]**2)
           for j in range(3)] for i in range(3)]
    # Diagonal-only storage cannot determine the uncertainty of a contrast.
    contrast_full = vy[0][0]+vy[1][1]-2*vy[0][1]
    contrast_diagonal = vy[0][0]+vy[1][1]
    check("ratio_retains_source_covariance", vy[0][1] < 0 and contrast_full > contrast_diagonal)
    check("ratio_covariance_positive_definite_all_principal_minors", min(vy[i][i] for i in range(3)) > 0
          and all(vy[i][i]*vy[j][j]-vy[i][j]**2 > 0 for i in range(3) for j in range(i))
          and determinant3(vy) > 0)
    try:
        safe_ratio(F(1), F(0))
    except ValueError:
        check("zero_response_not_divided", True)
    else:
        check("zero_response_not_divided", False)
    check("actual_inputs_not_invented", data["actual_response_matrix"] is None
          and data["actual_full_covariance"] is None and data["actual_author_code"] is None)
    output = dict(kind="conditional photon kinematics and explicitly chosen response-statistics contract",
                  checks=checks, check_count=len(checks), passed=all(checks.values()), inputs=data,
                  conditional_991_keV_kinematics=rows,
                  isotropic_normalization=dict(correct=1, literal_CM_theta_Eq19=wrong_integral,
                                               maximum_pointwise_fractional_difference=1-(1-beta*beta)**2),
                  chosen_response=response, chosen_normalized_source_covariances=[v0, v1],
                  chosen_interpolated_response_covariance=vr, chosen_cross_energy_covariance=cross,
                  chosen_naively_interpolated_variance00=naive,
                  chosen_ratio=ratio, chosen_ratio_covariance=vy,
                  chosen_contrast_variance=dict(full=contrast_full, diagonal_only=contrast_diagonal),
                  statistics_scope="delta-method covariance at chosen Poisson means; exact Fraction arithmetic, no finite-count coverage assertion",
                  input_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                  actual_response_matrix=None, actual_full_covariance=None, actual_author_code=None,
                  limitations=["fixed collinear beta, no recoil spread, lifetime or actual data fit",
                               "preserve Eq19 literal; no assertion about author's implementation or official erratum",
                               "rest/lab response-axis and energy-gate definitions are not recovered",
                               "chosen histogram normalization/interpolation is not the author's algorithm",
                               "joint source/beam nuisance covariance and raw event selection remain unavailable"])
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2, default=str)+"\n")
    print(json.dumps({k:output[k] for k in ["kind", "check_count", "passed", "isotropic_normalization", "chosen_contrast_variance"]}, default=str))


if __name__ == "__main__":
    main()
