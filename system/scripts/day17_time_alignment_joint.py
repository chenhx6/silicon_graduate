#!/usr/bin/env python3
"""Conditional exact two-path time/alignment non-identifiability design."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from scipy.integrate import quad

from day17_draper1970_gaussian_audit import coefficients, transfer

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def angular(a, theta):
    x = np.cos(np.deg2rad(theta))
    return float(a[0] + a[1] * (3*x*x-1)/2 + a[2]*(35*x**4-30*x*x+3)/8)


def kernels(t, tau, feed):
    direct = np.exp(-t/tau)/tau
    if feed == 0:
        delayed = direct
    elif feed == tau:
        delayed = t*np.exp(-t/tau)/(tau*tau)
    else:
        delayed = (np.exp(-t/feed)-np.exp(-t/tau))/(feed-tau)
    return direct, delayed


def main():
    contract_path = RUN / 'time-alignment-joint-contract.json'
    c = json.loads(contract_path.read_text())
    jp, j = c['parent_J'], c['target_J']
    parent = np.zeros(2*jp+1)
    parent[jp] = 1
    pa = transfer(jp)[0] @ parent
    pb = transfer(jp)[0] @ (np.ones(2*jp+1)/(2*jp+1))
    assert np.min(pa) >= 0 and abs(pa.sum()-1) < 1e-14
    assert np.max(abs(pb - np.ones(2*j+1)/(2*j+1))) < 1e-14
    aa, ab = coefficients(j, pa), coefficients(j, pb)
    assert np.max(abs(np.array(aa)-coefficients(j, pa, 32))) < 1e-13
    tau, feed, stop = c['lifetime_target'], c['lifetime_feeder'], c['slowing_time']
    ld, lf = 1/(1+tau/stop), 1/((1+tau/stop)*(1+feed/stop))
    for n, expected in [(0, ld), (1, lf)]:
        value = quad(lambda t: kernels(t, tau, feed)[n]*np.exp(-t/stop), 0, np.inf,
                     epsabs=1e-12, epsrel=1e-12)[0]
        assert abs(value-expected) < 1e-12
        assert abs(quad(lambda t: kernels(t, tau, feed)[n], 0, np.inf)[0]-1) < 1e-12
    rows = []
    for theta in c['point_angles_degrees']:
        wa, wb = angular(aa, theta), angular(ab, theta)
        denom = wa+wb
        fa, fb = (wa*ld+wb*lf)/denom, (wb*ld+wa*lf)/denom
        numerical_a = quad(lambda t: .5*(wa*kernels(t,tau,feed)[0]
                                          +wb*kernels(t,tau,feed)[1])*np.exp(-t/stop),
                           0, np.inf, epsabs=1e-12)[0]/(.5*denom)
        numerical_b = quad(lambda t: .5*(wb*kernels(t,tau,feed)[0]
                                          +wa*kernels(t,tau,feed)[1])*np.exp(-t/stop),
                           0, np.inf, epsabs=1e-12)[0]/(.5*denom)
        assert abs(numerical_a-fa) < 1e-12 and abs(numerical_b-fb) < 1e-12
        rows.append({'theta_degrees': theta, 'W_A': wa, 'W_B': wb,
                     'integrated_W_both_models': .5*denom,
                     'F_model_A': fa, 'F_model_B_swapped': fb,
                     'difference': fa-fb,
                     'actual_projected_centroid_difference_over_E0_beta0': (fa-fb)*np.cos(np.deg2rad(theta)),
                     'at_90_degrees_shift_is_zero_and_F_not_centroid_estimable': theta==90})
    assert abs(rows[1]['difference']) > 1e-3
    # Equal-time and equal-density controls cancel analytically at every angle.
    for row in rows:
        wa, wb = row['W_A'], row['W_B']
        assert abs((wa*ld+wb*ld)/(wa+wb)-ld) < 1e-14
        assert abs((wa*ld+wa*lf)/(2*wa)-(ld+lf)/2) < 1e-14
    for t in [0, .1, 1, 3, 10]:
        gd0, gf0 = kernels(t, tau, 0)
        assert gd0 == gf0
        gd, gf = kernels(t, tau, feed)
        rho1 = .5*(gd*pa+gf*pb)
        rho2 = .5*(gd*pb+gf*pa)
        assert abs(rho1.sum()-rho2.sum()) < 1e-14
    # Full angle average of each W is unity, so both yield (Ld+Lf)/2.
    x, wt = np.polynomial.legendre.leggauss(16)
    wa = np.array([angular(aa, np.rad2deg(np.arccos(v))) for v in x])
    wb = np.array([angular(ab, np.rad2deg(np.arccos(v))) for v in x])
    integrated1 = np.dot(wt, wa*ld+wb*lf)/np.dot(wt,wa+wb)
    integrated2 = np.dot(wt, wb*ld+wa*lf)/np.dot(wt,wa+wb)
    assert abs(integrated1-integrated2) < 1e-13
    # Slowing limits: no slowing -> one; instantaneous stopping -> zero.
    limits = []
    for ts in [1e-9, 1e9]:
        d, f = 1/(1+tau/ts), 1/((1+tau/ts)*(1+feed/ts))
        limits.append({'ts':ts, 'direct_Laplace':d, 'delayed_Laplace':f})
    assert limits[0]['direct_Laplace'] < 2e-9
    assert limits[0]['delayed_Laplace'] < 2e-9
    assert limits[1]['direct_Laplace'] > 1-3e-9
    assert limits[1]['delayed_Laplace'] > 1-3e-9
    result = {'at':datetime.now(timezone.utc).isoformat(),
              'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'CG_dependency_sha256':hashlib.sha256((ROOT/'system/scripts/day17_draper1970_gaussian_audit.py').read_bytes()).hexdigest(),
              'contract_sha256':hashlib.sha256(contract_path.read_bytes()).hexdigest(),
              'target_population_A':pa.tolist(), 'target_population_B':pb.tolist(),
              'angular_coefficients_A':aa, 'angular_coefficients_B':ab,
              'same_time_integrated_target_density_both_models':(.5*(pa+pb)).tolist(),
              'same_total_time_density':'.5*(g_direct+g_delayed)',
              'Ld':ld,'Lf':lf,'point_results':rows,
              'full_angle_average_F_both':integrated1,
              'full_angle_F_is_speed_weight_moment_not_an_angle_integrated_Doppler_centroid':True,
              'slowing_limits':limits,
              'equal_time_equal_density_zero_feeding_controls':True,
              'positive_density_normalization_and_independent_quadrature':True,
              'same_time_and_angular_marginals_do_not_determine_joint_response':True,
              'not_actual_nuclear_tau_bias_or_new_P_Q_CI':True,'ok':True}
    (RUN/'time-alignment-joint-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
