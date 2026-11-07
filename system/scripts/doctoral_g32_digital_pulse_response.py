#!/usr/bin/env python3
"""Controlled pulse/filter demonstration; no instrument or nuclear-data fit.

The exponential-tail trapezoid recursion follows the convention discussed in
Wu's thesis Eq.1.14-1.18. Its gain is normalized using an independently derived
ideal exponential response. CFD timestamps are compared to a root of the same
analytic pulse and delay/sum operator, never a hard-coded timestamp.
"""
from pathlib import Path
import csv
import datetime
import hashlib
import json
import platform
import sys

import numpy as np
import scipy
from scipy.optimize import brentq

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'outputs/l4/20261108-digital-pulse-response'


def pulse(t, arrival, rise, decay=50000.0, amplitude=1000.0):
    """Synthetic amplitude coefficient, time in ns; not collected-charge data."""
    dt = np.asarray(t, dtype=float) - arrival
    positive = np.maximum(dt, 0.0)
    front = np.ones_like(positive) if rise == 0 else -np.expm1(-positive/rise)
    return np.where(dt >= 0, amplitude*front*np.exp(-positive/decay), 0.0)


def shifted(v, lag):
    result = np.zeros_like(v)
    if lag < len(v):
        result[lag:] = v[:len(v)-lag]
    return result


def trapezoid(v, k, ell, pole, gain_pole=None):
    d = v-shifted(v, k)-shifted(v, ell)+shifted(v, k+ell)
    p = np.cumsum(d)
    # For v[n]=A alpha^n, alpha=M/(M+1), the ideal peak is
    # A*k*(M+1). Using k*M introduces a small gain bias.
    gain = k*((pole if gain_pole is None else gain_pole)+1.0)
    return np.cumsum(p+pole*d)/gain


def fast(v, step):
    length, gap = round(100.0/step), round(50.0/step)
    kernel = np.r_[np.ones(length), np.zeros(gap), -np.ones(length)]/length
    return np.convolve(v, kernel)[:len(v)]


def cfd_samples(v, step, fraction=0.4):
    ff = fast(v, step)
    return shifted(ff, round(80.0/step))-fraction*ff


def cfd_continuation(t, arrival, step, rise=100.0, amplitude=1000.0):
    """Analytic continuation of this discrete delay/sum filter to real t.

    This retains the same finite taps, so differences measure interpolation,
    rather than a difference between continuous and discrete box conventions.
    """
    length, gap, delay = round(100.0/step), round(50.0/step), 80.0
    taps = np.arange(length)*step
    def ff(tt):
        return np.mean(pulse(tt-taps, arrival, rise, amplitude=amplitude)
                       -pulse(tt-(length+gap)*step-taps, arrival, rise,
                              amplitude=amplitude))
    return float(ff(t-delay)-0.4*ff(t))


def reference_latency(step):
    grid = np.linspace(0.01, 1000.0, 2001)
    values = [cfd_continuation(t, 0.0, step) for t in grid]
    for i in range(len(grid)-1):
        if values[i] < 0 <= values[i+1]:
            return brentq(lambda t:cfd_continuation(t, 0.0, step),
                          grid[i], grid[i+1], xtol=1e-11)
    raise RuntimeError('No physical CFD crossing in analytic reference')


def timestamp(arrival, step, amplitude=1000.0):
    t = np.arange(0.0, 2000.0, step)
    wave = cfd_samples(pulse(t, arrival, 100.0, amplitude=amplitude), step)
    candidates = np.flatnonzero((wave[:-1] < 0) & (wave[1:] >= 0))
    candidates = candidates[t[candidates] >= arrival]
    if not len(candidates):
        raise RuntimeError('No CFD zero crossing')
    i = int(candidates[0])
    return float(t[i]-wave[i]*step/(wave[i+1]-wave[i]))


def write_csv(name, fields, rows):
    with (OUT/name).open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    step, decay, arrival = 10.0, 50000.0, 500.0
    t = np.arange(0.0, 8000.0, step)
    pole = 1.0/np.expm1(step/decay)
    raw = pulse(t, arrival, 100.0)
    shaped = [trapezoid(raw, 200, 250, pole*f, gain_pole=pole)
              for f in (1.0, 0.7, 1.3)]
    ff, cfd = fast(raw, step), cfd_samples(raw, step)
    response = [dict(zip(['time_ns','raw_pulse','trapezoid_opt',
                          'trapezoid_under','trapezoid_over','fast_filter','cfd_wave'],
                         [t[i], raw[i], *(a[i] for a in shaped), ff[i], cfd[i]]))
                for i in range(0, len(t), 2)]
    write_csv('pulse_filter_response.csv', list(response[0]), response)
    ballistic = []
    for rise in range(20, 420, 20):
        inp = pulse(t, arrival, rise)
        amps = [float(np.max(trapezoid(inp, 200, ell, pole)))
                for ell in (200, 210, 240)]
        ballistic.append(dict(zip(['rise_time_ns','flat_top_0ns_amp',
                                   'flat_top_100ns_amp','flat_top_400ns_amp',
                                   'deficit_flat0_pct','deficit_flat400_pct'],
                                  [rise,*amps, (1000-amps[0])/10,
                                   (1000-amps[2])/10])))
    write_csv('ballistic_deficit_study.csv', list(ballistic[0]), ballistic)
    phases, convergence = [], []
    for dt in (10.0, 5.0, 2.5, 1.25):
        ref = reference_latency(dt)
        errs = []
        for fraction in np.arange(0.0, 1.0, 0.05):
            phi = float(fraction*dt)
            measured = timestamp(arrival+phi, dt)
            err = measured-(arrival+phi+ref)
            errs.append(abs(err))
            if dt == step:
                amp = 100.0+float(fraction)*1000.0
                phases.append({'phase_ns':phi, 'true_t0_ns':arrival+phi,
                               'reference_zc_ns':arrival+phi+ref,
                               'extracted_zc_ns':measured,'timing_error_ns':err,
                               'amplitude_arb':amp,
                               'amplitude_scan_zc_ns':timestamp(arrival, dt, amp)})
        convergence.append({'sampling_interval_ns':dt,
                            'reference_latency_ns':ref,
                            'max_abs_interpolation_error_ns':max(errs)})
    write_csv('cfd_phase_walk_analysis.csv', list(phases[0]), phases)
    write_csv('sampling_convergence.csv', list(convergence[0]), convergence)
    ideal = trapezoid(pulse(t, arrival, 0.0), 200, 250, pole)
    expected = np.zeros_like(t)
    direct = np.convolve(np.ones(200), np.ones(250))*1000.0/200
    offset = round(arrival/step)
    expected[offset:offset+len(direct)] = direct
    amplitude_spread = max(r['amplitude_scan_zc_ns'] for r in phases)-min(
        r['amplitude_scan_zc_ns'] for r in phases)
    checks = {
        'ideal_exponential_matches_independent_box_convolution':
            bool(np.max(np.abs(ideal-expected)) < 1e-7),
        'ideal_exponential_gain_is_unity':bool(abs(np.max(ideal)-1000) < 1e-7),
        'noiseless_cfd_amplitude_invariance':bool(amplitude_spread < 1e-9),
        'integer_sample_translation':bool(abs(timestamp(510,10)-timestamp(500,10)-10)<1e-9),
        'analytic_reference_has_zero_residual':bool(abs(cfd_continuation(
            reference_latency(10),0,10)) < 1e-7),
        'fine_sampling_improves_interpolation':bool(
            convergence[-1]['max_abs_interpolation_error_ns']
            < convergence[0]['max_abs_interpolation_error_ns']),
        'flat_top_alleviates_but_does_not_remove_deficit':bool(all(
            r['deficit_flat0_pct'] > r['deficit_flat400_pct'] > 0 for r in ballistic)),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    artifacts = [{'path':p.relative_to(ROOT).as_posix(),
                  'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
                 for p in sorted(OUT.glob('*.csv'))]
    provenance = {
        'task_id':'doctoral-foundations-r1-G32',
        'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'command':'python3 system/scripts/doctoral_g32_digital_pulse_response.py',
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,
        'platform':platform.platform(),'random_seed':None,
        'units':'time ns; pulse amplitude arbitrary, not calibrated deposited energy',
        'model':'noiseless double-exponential pulse; exact finite-tap delays; linear zero-crossing interpolation',
        'boundaries':['No instrument calibration, nuclear decay fit or noise model',
                      'Rise parameter is not a finite maximum charge-collection time',
                      'CFD baseline reference is a numerically solved analytic continuation',
                      'Not a universal dead-time or detector-performance model'],
        'parameters':{'sampling_interval_ns':step,'decay_ns':decay,
                      'rise_ns':100,'slow_rise_ns':2000,'slow_flat_ns':500,
                      'fast_rise_ns':100,'fast_flat_ns':50,
                      'cfd_delay_ns':80,'cfd_fraction':0.4},
        'checks':checks,'amplitude_timestamp_spread_ns':amplitude_spread,
        'ideal_convolution_max_error':float(np.max(np.abs(ideal-expected))),
        'sampling_convergence':convergence,'artifacts':artifacts}
    (OUT/'run-provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')
    print(json.dumps({'checks':checks,'sampling_convergence':convergence,
                      'amplitude_timestamp_spread_ns':amplitude_spread,
                      'ideal_convolution_max_error':provenance['ideal_convolution_max_error']},indent=2))


if __name__ == '__main__':
    main()
