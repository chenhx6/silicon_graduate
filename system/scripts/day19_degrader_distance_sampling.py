#!/usr/bin/env python3
"""Degrader velocity labels and finite-distance derivative design.

Source velocities are printed Suzuki2008 central values. All lifetimes used
for controls, distance half-spacings and feeder waiting distributions are
declared inputs; this is not a reanalysis of its measured lifetime curves.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
from day19_ddcm_gate_contract import cascade


def central_derivative(fun, t, h):
    return (fun(t + h) - fun(t - h)) / (2 * h)


def unequal_derivative(fun, t, hleft, hright):
    return (-hright / (hleft * (hleft + hright)) * fun(t - hleft)
            + (hright - hleft) / (hleft * hright) * fun(t)
            + hleft / (hright * (hleft + hright)) * fun(t + hright))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    checks = []

    def check(name, ok):
        checks.append({'name': name, 'passed': bool(ok)})
        if not ok:
            raise AssertionError(name)

    beta_fast, beta_slow = .051, .031
    vfast = beta_fast * 299.792458
    tau, time = .72, 2.
    f = lambda t: -math.expm1(-t / tau)
    occupancy = math.exp(-time / tau)
    spacing_rows = []
    for distance_half_step in [1., 5., 10.]:
        h = distance_half_step / vfast
        numerical = occupancy / central_derivative(f, time, h)
        analytical = tau * (h / tau) / math.sinh(h / tau)
        check(f'central derivative exponential exact quotient at {distance_half_step} um', math.isclose(numerical, analytical, rel_tol=1e-12))
        check(f'prompt central finite-difference tau below true at {distance_half_step}', numerical < tau)
        spacing_rows.append({'synthetic_distance_half_step_um': distance_half_step,
                            'vacuum_time_half_step_ps': h, 'apparent_tau_ps': numerical,
                            'fractional_bias': numerical / tau - 1})
    # Delayed feeder changes the sign of curvature error at the chosen time.
    ta, tb, t = 2., 10., 2.
    cdf = lambda x: cascade(x, ta, tb)[2]
    occ = cascade(t, ta, tb)[1]
    delayed_rows = []
    for h in [.1, .2, .4]:
        apparent = occ / central_derivative(cdf, t, h)
        check(f'delayed feeding derivative curvature can raise tau h={h}', apparent > ta)
        delayed_rows.append({'time_half_step_ps': h, 'apparent_tau_ps': apparent})
    # Exactness on quadratic controls distinguishes uneven-grid formula from
    # the tempting endpoint chord, which is not the derivative at the center.
    poly = lambda x: 1. + 2. * x + 3. * x * x
    t, hl, hr = 2., .2, .5
    expected = 2 + 6 * t
    proper = unequal_derivative(poly, t, hl, hr)
    chord = (poly(t + hr) - poly(t - hl)) / (hl + hr)
    check('unequal-distance quadratic derivative exactly', math.isclose(proper, expected, abs_tol=1e-12))
    check('endpoint chord not centered at middle point', abs(chord - expected) > .1)
    # Richardson is a forward control, not permission to synthesize unmeasured
    # half-spacing data from sparse experimental distance scans.
    t = 2.;h = .4
    d1 = central_derivative(f, t, h)
    d2 = central_derivative(f, t, h / 2)
    rich = (4 * d2 - d1) / 3
    exact = math.exp(-t / tau) / tau
    check('derivative half-step improves finite-difference error', abs(d2 - exact) < abs(d1 - exact))
    check('Richardson forward control improves error again', abs(rich - exact) < abs(d2 - exact))
    # Shared-distance derivatives have covariance, even if original counts are
    # independent. For D0=(F1-F-1)/(2h), D2=(F3-F1)/(2h), shared F1 gives a
    # negative covariance. This is about derivatives, not a full tau CI.
    variance_each, h = .0001, .5
    var_d = variance_each / (2 * h * h)
    cov_d0_d2 = -variance_each / (4 * h * h)
    check('shared endpoint derivative correlation is minus one half', math.isclose(cov_d0_d2 / var_d, -.5))
    # Source 'unshifted' component is post-degrader motion, later Doppler
    # corrected; it is not a population stopped at beta=0.
    energy, theta = 234., 35.
    doppler = lambda beta: math.sqrt(1 - beta * beta) / (1 - beta * math.cos(math.radians(theta)))
    raw_fast, raw_slow = energy * doppler(beta_fast), energy * doppler(beta_slow)
    check('post-degrader u is Doppler shifted in lab', raw_slow > energy)
    check('two moving components remain separated at 35 degrees', raw_fast - raw_slow > 3.)
    wrong_delta_v_tau = tau * beta_fast / (beta_fast - beta_slow)
    wrong_slow_v_tau = tau * beta_fast / beta_slow
    check('using velocity difference as vacuum clock is wrong', math.isclose(wrong_delta_v_tau, 1.836))
    transit = .2
    conditional_foil_probability = -math.expm1(-transit / tau)
    check('short transit not identically zero decay probability', .24 < conditional_foil_probability < .25)
    raw = Path('raw/papers/2008_Suzuki et al_Lifetime measurement of candidate chiral doublet bands in the Rh 103 , 104.pdf')
    check('Suzuki raw hash', hashlib.sha256(raw.read_bytes()).hexdigest() == 'f9c421090b33da94206f9d1d4ebd36ad0f5be79ee1dcd6a19fe38b32a7ec5927')
    result = {'created_at_utc': datetime.now(timezone.utc).isoformat(),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'scope': 'synthetic spacing/feeding/foil controls using printed velocity scale; no event refit or source bias estimate',
              'inputs': {'beta_fast': beta_fast, 'beta_slow': beta_slow, 'synthetic_tau_ps': tau, 'synthetic_prompt_time_ps': time},
              'central_spacing_controls': spacing_rows, 'delayed_feeding_controls': delayed_rows,
              'unequal_grid_quadratic': {'derivative': expected,'proper_three_point': proper,'wrong_endpoint_chord': chord},
              'shared_derivative_covariance': {'synthetic_F_variance': variance_each,'D_variance': var_d,'Cov_D0_D2': cov_d0_d2,'correlation': cov_d0_d2 / var_d},
              'two_velocity_energy_control': {'E0_keV': energy,'theta_degrees': theta,'lab_fast_keV': raw_fast,'lab_slow_keV': raw_slow,
                  'lab_separation_keV': raw_fast - raw_slow,'tau_using_delta_v_wrong_ps': wrong_delta_v_tau,'tau_using_slow_v_wrong_ps': wrong_slow_v_tau},
              'conditional_transit_control': {'synthetic_transit_ps': transit,'probability_decay_inside_given_entered_alive': conditional_foil_probability,
                  'boundary': 'not source correction magnitude; excludes feeding/transport/energy cuts'},
              'required_inputs': ['actual distance grid and derivative/smoothing implementation','normalization per distance and shared Cov',
                 'two velocity distributions and component labels','finite target/degrader transport and ROI','direct/indirect gate purity'],
              'checks': checks,'check_count': len(checks)}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['check_count','central_spacing_controls','delayed_feeding_controls','two_velocity_energy_control','conditional_transit_control']},ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
