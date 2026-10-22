#!/usr/bin/env python3
"""Day 20 uncredited preview: weighted regression trends and cross-configuration boundaries."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path


def weighted_linear_regression(x_list, y_list, sigma_list, scale_cov_by_chi2=False):
    """Weighted linear regression. If scale_cov_by_chi2=True, mimics np.polyfit cov=True."""
    w = [1. / (s * s) for s in sigma_list]
    sw = sum(w)
    swx = sum(wi * xi for wi, xi in zip(w, x_list))
    swy = sum(wi * yi for wi, yi in zip(w, y_list))
    swxx = sum(wi * xi * xi for wi, xi in zip(w, x_list))
    swxy = sum(wi * xi * yi for wi, xi, yi in zip(w, x_list, y_list))
    delta = sw * swxx - swx * swx
    if delta <= 0:
        raise ValueError("Ill-conditioned regression matrix")
    slope = (sw * swxy - swx * swy) / delta
    intercept = (swxx * swy - swx * swxy) / delta
    # Compute goodness-of-fit chi2
    chi2 = sum(wi * ((yi - (intercept + slope * xi)) ** 2) for wi, xi, yi in zip(w, x_list, y_list))
    ndof = len(x_list) - 2
    scale_factor = math.sqrt(chi2 / ndof) if (scale_cov_by_chi2 and ndof > 0) else 1.0
    slope_err = math.sqrt(sw / delta) * scale_factor
    intercept_err = math.sqrt(swxx / delta) * scale_factor
    z_score = slope / slope_err
    return {
        'slope': slope,
        'slope_err': slope_err,
        'intercept': intercept,
        'intercept_err': intercept_err,
        'z_score': z_score,
        'chi2': chi2,
        'ndof': ndof,
        'scale_cov_by_chi2': scale_cov_by_chi2,
        'covariance_multiplier': scale_factor**2,
        'boundary': 'known absolute sigma -> Gaussian control; estimated common scale -> Student t, not a Gaussian sigma count'
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    checks = []

    def check(name, ok):
        checks.append({'name': name, 'passed': bool(ok)})
        if not ok:
            raise AssertionError(name)

    # 1. Singh 2016 Table 1 ND sequence: 4 finite points
    # Table 1 lists 15/2-, 27/2-, 31/2-, 35/2- (hbar)
    # Spins I = 7.5, 13.5, 15.5, 17.5 (hbar)
    # Qt = 2.93(45), 2.26(30), 2.66(125), 2.43(21) eb (symmetrized mean errors)
    spins_singh = [7.5, 13.5, 15.5, 17.5]
    qt_singh = [2.93, 2.26, 2.66, 2.43]
    sig_singh = [0.45, 0.30, 0.125, 0.21]
    fit_singh = weighted_linear_regression(spins_singh, qt_singh, sig_singh, scale_cov_by_chi2=False)
    check('Singh slope is negative', fit_singh['slope'] < 0)
    check('Singh slope around -0.0302 eb/hbar', math.isclose(fit_singh['slope'], -0.030175, rel_tol=1e-3))
    check('Singh z-score around -0.639', math.isclose(fit_singh['z_score'], -0.6391, rel_tol=1e-3))

    # 2. Babra 2019 136Sm Table 1: 6 finite yrast states 8+ to 18+
    # Spins I = 8, 10, 12, 14, 16, 18 (hbar)
    # Qt = 5.66(19), 5.59(785), 5.70(205), 5.38(335), 4.85(33), 5.05(35) eb
    spins_babra = [8.0, 10.0, 12.0, 14.0, 16.0, 18.0]
    qt_babra = [5.66, 5.59, 5.70, 5.38, 4.85, 5.05]
    sig_babra = [0.19, 0.785, 0.205, 0.335, 0.33, 0.35]
    fit_babra = weighted_linear_regression(spins_babra, qt_babra, sig_babra)
    babra_scaled = weighted_linear_regression(spins_babra, qt_babra, sig_babra, scale_cov_by_chi2=True)
    check('residual-scaled covariance follows explicit chi2/df multiplier', math.isclose(babra_scaled['slope_err']**2 / fit_babra['slope_err']**2, fit_babra['chi2']/fit_babra['ndof']))
    check('Babra slope around -0.0716 eb/hbar', math.isclose(fit_babra['slope'], -0.071648, rel_tol=1e-3))

    # An arbitrary output-Q scale proves an algebraic invariance. It does NOT
    # imply a universal stopping-power -> Q transfer function.
    scale = math.sqrt(1.15)
    qt_scaled = [q * scale for q in qt_babra]
    sig_scaled = [s * scale for s in sig_babra]
    fit_scaled = weighted_linear_regression(spins_babra, qt_scaled, sig_scaled)
    check('Overall scaling leaves z-score unchanged', math.isclose(fit_scaled['z_score'], fit_babra['z_score'], rel_tol=1e-6))
    check('Overall scaling changes slope by exactly the scale factor', math.isclose(fit_scaled['slope'], fit_babra['slope'] * scale, rel_tol=1e-6))

    t_abs = abs(babra_scaled['z_score'])
    s = t_abs / math.sqrt(t_abs*t_abs+4)
    student_p_df4 = 1-1.5*s+.5*s**3
    known_p = math.erfc(abs(fit_babra['z_score'])/math.sqrt(2))
    check('estimated-scale Student control is not Gaussian tail', student_p_df4 > .05 and known_p < .05)
    result = {
        'created_at_utc': datetime.now(timezone.utc).isoformat(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope': 'printed finite centers, symmetrized errors: parallel known-error Gaussian and estimated-scale controls; no real joint covariance/CI',
        'singh_2016_nd_regression': fit_singh,
        'babra_2019_yrast_regression': fit_babra,
        'babra_residual_scaled_sensitivity': babra_scaled,
        'babra_two_sided_tail_controls': {'known_sigma_Gaussian':known_p, 'estimated_common_scale_Student_df4':student_p_df4},
        'withdrawn_cross_configuration_fit': 'invented spins21.5/25.5 with duplicated band mean7.3(4) were not two measured states; old chi2 proves no experimental configuration jump',
        'stopping_scale_invariance_test': {
            'scale_factor': scale,
            'scaled_slope': fit_scaled['slope'],
            'scaled_z_score': fit_scaled['z_score'],
            'original_z_score': fit_babra['z_score']
        },
        'methodological_boundary': [
            'Actual point-to-point covariance, asymmetric likelihood and censored rows are missing',
            'A non-significant slope (Singh z=-0.64) does not prove constant deformation; it only indicates insufficient evidence against flat trend',
            'Do not choose residual rescaling only to reproduce an old statistic; its stochastic model and degrees of freedom differ',
            'A common output scale leaves conditional standardized slope invariant; stopping response need not be such a scale'
        ],
        'checks': checks,
        'check_count': len(checks)
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'check_count':len(checks),'singh_z':fit_singh['z_score'],'babra_known_sigma_z':fit_babra['z_score'],'babra_residual_scaled_t':babra_scaled['z_score'],'tail_controls':result['babra_two_sided_tail_controls']},ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
