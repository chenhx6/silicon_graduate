#!/usr/bin/env python3
"""Causal TDPAD response and published-period arithmetic; no experimental fit.

Synthetic exponential populations, rank-two magnetic modulation, Gaussian
time resolution. Source central values are compared without inventing a
missing local-field correction or raw-data covariance.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path


def simpson(fun, lo, hi, step):
    n = max(2, 2 * math.ceil((hi - lo) / step / 2))
    h = (hi - lo) / n
    return h / 3 * (fun(lo) + fun(hi) + sum(
        (4 if i % 2 else 2) * fun(lo + i * h) for i in range(1, n)))


def observed(t, tau, relaxation, kappa, phase, amplitude, sigma, step):
    """Ratio of convolved difference and sum, with causal true time >= 0."""
    upper = max(t + 10 * sigma, 10 * sigma)
    gaussian = lambda u: math.exp(-0.5 * ((t - u) / sigma) ** 2)
    total = lambda u: math.exp(-u / tau) * gaussian(u)
    difference = lambda u: total(u) * amplitude * math.exp(-u / relaxation) * math.sin(phase + kappa * u)
    den = simpson(total, 0, upper, step)
    num = simpson(difference, 0, upper, step)
    return num / den


def late_ratio(t, tau, relaxation, kappa, phase, amplitude, sigma):
    """Full-line analytic approximation valid when causal-boundary tail is tiny."""
    a = 1 / tau
    b = a + 1 / relaxation
    scale = math.exp(0.5 * sigma ** 2 * (b * b - kappa * kappa - a * a))
    return amplitude * scale * math.exp(-t / relaxation) * math.sin(phase + kappa * t - b * kappa * sigma ** 2)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    checks = []

    def check(name, ok):
        checks.append({'name': name, 'passed': bool(ok)})
        if not ok:
            raise AssertionError(name)

    # Published QI central values, using the actual half-integer J = 9/2.
    j = 9 / 2
    factor = 2 * j * (2 * j - 1) / 3
    frequencies = [52.6, 36.4]  # MHz; quoted SEs below
    periods = [factor / f * 1000 for f in frequencies]  # ns
    check('half-integer QI period factor is 24', factor == 24)
    check('129Ce period matches printed 456(12) ns central rounding', abs(periods[0] - 456) < 1)
    freq_ratio = frequencies[0] / frequencies[1]
    ratio_se = freq_ratio * math.hypot(1.4 / frequencies[0], 1.6 / frequencies[1])
    naive_q_ratio_se = (1.32 / .92) * math.hypot(.13 / 1.32, .10 / .92)
    check('frequency ratio matches common-EFG-free 1.44(7)', abs(freq_ratio - 1.44) < .01 and abs(ratio_se - .07) < .01)
    check('treating both absolute Q errors independent loses common calibration cancellation', naive_q_ratio_se > 2 * ratio_se)
    # Neither this ratio nor the QI frequency fixes Q sign.
    q, efg = 1.32, 52.6 / 1.32
    check('QI absolute sign degeneracy', math.isclose((-q) * (-efg), q * efg))
    check('QI Q and EFG scale ridge', math.isclose((q * 1.1) * (efg / 1.1), q * efg))

    tau, relaxation, kappa, phase, amplitude, sigma = 80., 300., .125, .3, .2, 5.
    rows = []
    for t in [0., 5., 10., 25., 50., 100.]:
        coarse = observed(t, tau, relaxation, kappa, phase, amplitude, sigma, .1)
        fine = observed(t, tau, relaxation, kappa, phase, amplitude, sigma, .05)
        late = late_ratio(t, tau, relaxation, kappa, phase, amplitude, sigma)
        check(f'Simpson step convergence at {t} ns', abs(coarse - fine) < 1e-8)
        check(f'physical asymmetry bound at {t} ns', abs(fine) <= amplitude)
        if t >= 50:
            check(f'late analytic convolution at {t} ns', abs(late - fine) < 1e-10)
        rows.append({'observed_time_ns': t, 'causal_convolution_ratio': fine,
                     'unconvolved_ratio': amplitude * math.exp(-t / relaxation) * math.sin(phase + kappa * t),
                     'late_full_line_approximation': late})
    check('causal boundary must be modeled near zero', abs(rows[0]['causal_convolution_ratio'] - rows[0]['late_full_line_approximation']) > .01)
    for t in [0, 10, 35, 100]:
        a = amplitude * math.exp(-t / relaxation) * math.sin(phase + kappa * t)
        b = amplitude * math.exp(-t / relaxation) * math.sin(math.pi - phase - kappa * t)
        check(f'free phase makes frequency-sign ambiguity at {t}', math.isclose(a, b, abs_tol=1e-14))
    scale = 1.02
    for t in [10, 35, 100]:
        true = amplitude * math.exp(-t / relaxation) * math.sin(phase + kappa * t)
        wrong_clock = amplitude * math.exp(-(scale * t) / (scale * relaxation)) * math.sin(phase + (kappa / scale) * (scale * t))
        check(f'time calibration ridge at {t}', math.isclose(true, wrong_clock, abs_tol=1e-14))
    check('population cancels from ideal instantaneous ratio', math.isclose(
        (.4 * math.exp(-100 / 80)) / (2 * math.exp(-100 / 80)), .2))
    omega_l = .0625  # ns^-1, printed 114-keV row
    period_modulation = math.pi / omega_l
    period_larmor = 2 * math.pi / omega_l
    check('rank-two modulation frequency is twice Larmor angular frequency', math.isclose(period_larmor, 2 * period_modulation))
    # Approximate standard mu_N/hbar; limited central-value arithmetic only.
    magneton_over_hbar = 4.789e7  # s^-1 T^-1, rounded background constant
    direct_g = [62.5e6 / (2.145 * magneton_over_hbar), 41.3e6 / (1.4 * magneton_over_hbar)]
    check('printed external-field arithmetic does not exactly reconstruct reported g', all(abs(g - .59) > .01 for g in direct_g))
    hashes = {}
    for path, expected in [
        ('raw/papers/gpt/high-spin-20260920/g-factor/2018_Grodner et al_First Measurement of the g Factor in the Chiral Band.pdf', 'c71ec59160c444c34ab7f340db5f045c1f26456bc1741197ec62caea7f4efbf2'),
        ('raw/papers/gpt/high-spin-20260920/形变/1998_Ionescu-Bujor et al_Static electromagnetic moments and nuclear shapes in 129,131Ce.pdf', '2735874b2be1116741f421a114ffa5995be93c99891ed284d962b53f0446484b')]:
        actual = hashlib.sha256(Path(path).read_bytes()).hexdigest()
        hashes[path] = actual
        check('source raw hash ' + Path(path).name, actual == expected)
    result = {
        'created_at_utc': datetime.now(timezone.utc).isoformat(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope': 'published period arithmetic + synthetic causal response; no source fit/CI, no inferred local-field correction',
        'published_QI_controls': {'J': j, 'period_factor': factor, 'frequencies_MHz': frequencies, 'periods_ns': periods,
            'frequency_ratio': freq_ratio, 'ratio_independent_frequency_SE_control': ratio_se,
            'incorrect_independent_absolute_Q_ratio_SE': naive_q_ratio_se,
            'mean_lives_ns_from_half_lives_60_88': [60 / math.log(2), 88 / math.log(2)]},
        'published_Cs_controls': {'omega_L_ns_inv_114keV': omega_l, 'modulation_period_ns': period_modulation,
            'Larmor_period_ns': period_larmor, 'mean_life_ns_from_half_life_56': 56 / math.log(2),
            'rounded_muN_over_hbar_s_inv_T_inv': magneton_over_hbar,
            'external_B_only_g_central_Orsay_Stony': direct_g,
            'boundary': 'not equal to reported 0.59; local-field/calibration bridge not supplied here; do not invent correction'},
        'synthetic_inputs': {'tau_ns': tau, 'relaxation_ns': relaxation, 'modulation_angular_frequency_ns_inv': kappa,
                            'phase_rad': phase, 'amplitude': amplitude, 'Gaussian_sigma_ns': sigma},
        'synthetic_convolution': rows,
        'simple_sinusoid_only_Gaussian_attenuation': math.exp(-.5 * (kappa * sigma) ** 2),
        'required_inputs': ['time-scale and phase/field direction', 'effective local B or EFG with host calibration',
                            'causal response and pulse repetition', 'population lifetime versus alignment relaxation',
                            'background/normalization per detector and field reversal', 'feeding and level/spin identity',
                            'joint calibration and time-bin covariance'],
        'source_sha256': hashes, 'checks': checks, 'check_count': len(checks)}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ['check_count', 'published_QI_controls', 'published_Cs_controls', 'simple_sinusoid_only_Gaussian_attenuation']}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
