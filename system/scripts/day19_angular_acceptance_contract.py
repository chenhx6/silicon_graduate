#!/usr/bin/env python3
"""Conditional RDDS rank2/rank4 geometry and calibration design, no data fit."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path


def legendre(k, x):
    if k == 0:
        return 1.
    if k == 1:
        return x
    a, b = 1., x
    for n in range(2, k + 1):
        a, b = b, ((2 * n - 1) * x * b - (n - 1) * a) / n
    return b


def rank(rows, tolerance=1e-11):
    m = [list(row) for row in rows]
    current = 0
    for column in range(len(m[0])):
        pivot = max(range(current, len(m)), key=lambda i: abs(m[i][column]), default=None)
        if pivot is None or abs(m[pivot][column]) < tolerance:
            continue
        m[current], m[pivot] = m[pivot], m[current]
        scale = m[current][column]
        m[current] = [x / scale for x in m[current]]
        for i in range(len(m)):
            if i != current:
                scale = m[i][column]
                m[i] = [x - scale * y for x, y in zip(m[i], m[current])]
        current += 1
        if current == len(m):
            break
    return current


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def basis(theta_degrees, beta=0.):
    mu = math.cos(math.radians(theta_degrees))
    rest_mu = (mu - beta) / (1 - beta * mu)
    jac = (1 - beta ** 2) / (1 - beta * mu) ** 2
    return [jac * legendre(k, rest_mu) for k in [0, 2, 4]]


def polar_band_mean(k, theta, half_width):
    """Uniform solid angle full azimuth polar band; a declared toy aperture."""
    lo = math.cos(math.radians(theta + half_width))
    hi = math.cos(math.radians(theta - half_width))
    primitive = lambda x: (legendre(k + 1, x) - legendre(k - 1, x)) / (2 * k + 1)
    return (primitive(hi) - primitive(lo)) / (hi - lo)


def cap_mean(k, theta, half_angle, rings=120, azimuths=240):
    """Numerical uniform circular cone acceptance about detector axis, beta=0."""
    c = math.cos(math.radians(half_angle))
    th = math.radians(theta)
    total = 0
    for i in range(rings):
        y = c + (1 - c) * (i + .5) / rings
        for j in range(azimuths):
            phi = 2 * math.pi * (j + .5) / azimuths
            mu = math.cos(th) * y + math.sin(th) * math.sqrt(1 - y * y) * math.cos(phi)
            total += legendre(k, mu)
    return total / (rings * azimuths)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    checks = []

    def check(name, ok):
        checks.append({'name': name, 'passed': bool(ok)})
        if not ok:
            raise AssertionError(name)

    magic = math.degrees(math.acos(1 / math.sqrt(3)))
    check('P2 exact magic angle null', abs(legendre(2, 1 / math.sqrt(3))) < 1e-14)
    check('P4 survives magic angle', math.isclose(legendre(4, 1 / math.sqrt(3)), -7 / 18))
    angles = [36.5, 46.5, 85., 95., 133.5, 143.5]
    us = [basis(a) for a in angles]
    sh = [basis(a, .045) for a in angles]
    for i, j in [(0, 5), (1, 4), (2, 3)]:
        check(f'US complementary even-angle equality {i} {j}', all(math.isclose(x, y, abs_tol=1e-14) for x, y in zip(us[i], us[j])))
        check(f'SH boost breaks complementary equality {i} {j}', max(abs(x - y) for x, y in zip(sh[i], sh[j])) > .01)
    calibrated_indices = [0, 1, 4, 5]
    selected = [us[i] for i in calibrated_indices]
    check('six US rings span A0 A2 A4', rank(us) == 3)
    check('four outer US rings alone have only two distinct shape rows', rank(selected) == 2)
    check('known normalization allows two anisotropy coefficients', rank([row[1:] for row in selected]) == 2)
    check('boosted three-coefficient design still rank three', rank(sh) == 3)
    check('four boosted outer rings span three coefficients when beta known', rank([sh[i] for i in calibrated_indices]) == 3)
    a, b = selected[:2]
    null = [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]
    check('explicit free-normalization null direction', all(abs(dot(row, null)) < 1e-13 for row in selected))
    original = [1., .25, .08]
    altered = [x + .2 * y for x, y in zip(original, null)]
    check('two free-normalization shapes agree at all four outer rings', all(math.isclose(dot(row, original), dot(row, altered), abs_tol=1e-13) for row in selected))
    response_ratio = dot(us[2], original) / dot(us[2], altered)
    check('unmeasured central efficiency can absorb different central shape', math.isclose(dot(us[2], altered) * response_ratio, dot(us[2], original)))
    check('conditional shapes remain positive over sphere', all(dot([1., legendre(2, x / 100), legendre(4, x / 100)], altered) > 0 for x in range(-100, 101)))
    aperture = []
    for k in [2, 4]:
        cap = cap_mean(k, magic, 10.)
        c = math.cos(math.radians(10))
        qk = (legendre(k - 1, c) - legendre(k + 1, c)) / ((2 * k + 1) * (1 - c))
        analytic = qk * legendre(k, math.cos(math.radians(magic)))
        check(f'independent cap numerical/addition-theorem k={k}', abs(cap - analytic) < 2e-7)
        aperture.append({'k': k, 'cap_half_angle_degrees': 10., 'cap_mean': cap, 'cap_analytic': analytic,
                         'full_azimuth_polar_band_half_width_degrees': 10., 'polar_band_mean': polar_band_mean(k, magic, 10.)})
    check('ideal symmetric circular cap preserves unboosted P2 null', abs(aperture[0]['cap_mean']) < 1e-12)
    check('different aperture can reintroduce P2 at same central angle', abs(aperture[0]['polar_band_mean']) > .001)
    mu_lab = 1 / math.sqrt(3)
    mu_rest = (mu_lab - .045) / (1 - .045 * mu_lab)
    check('lab magic angle is not rest-frame magic angle at beta .045', abs(legendre(2, mu_rest)) > .02)
    # Independent Jacobian derivative and Doppler-square checks.
    for angle in angles:
        mu = math.cos(math.radians(angle)); beta = .045; h = 1e-6
        transform = lambda x: (x - beta) / (1 - beta * x)
        jac_num = (transform(mu + h) - transform(mu - h)) / (2 * h)
        jac = basis(angle, beta)[0]
        doppler = math.sqrt(1 - beta * beta) / (1 - beta * mu)
        check(f'Jacobian finite difference at {angle}', math.isclose(jac_num, jac, rel_tol=1e-9))
        check(f'Jacobian equals Doppler energy ratio squared at {angle}', math.isclose(jac, doppler * doppler))
    # At a single distance shape sees products a_k G_k, not each separately.
    ak, gk, cscale = .3, .7, 1.1
    check('initial anisotropy and attenuation product ambiguity', math.isclose(ak * gk, (ak * cscale) * (gk / cscale)))
    result = {'created_at_utc': datetime.now(timezone.utc).isoformat(),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'scope': 'point-ring rank2/rank4 and two declared toy apertures; not full detector response or source fit/CI',
              'magic_angle_degrees': magic, 'at_55_degrees': {'P2': legendre(2, math.cos(math.radians(55))), 'P4': legendre(4, math.cos(math.radians(55)))},
              'lab_magic_angle_rest_frame_P2_beta045': legendre(2, mu_rest),
              'lab_magic_angle_rest_frame_theta_degrees_beta045': math.degrees(math.acos(mu_rest)),
              'angles_degrees': angles, 'US_basis': us, 'SH_beta045_basis': sh,
              'single_distance_free_normalization_control': {'A0_A2_A4_original': original, 'A0_A2_A4_altered': altered,
                  'null_direction': null, 'central_efficiency_rescale': response_ratio,
                  'boundary': 'outer four US rings only, free normalization, no prior relation/known A0; not actual Radeck identifiability verdict'},
              'aperture_controls': aperture,
              'required_inputs': ['crystal acceptance and efficiency at SH/US energies','recoil direction/velocity distribution',
                   'rest-frame angular correlation and initial normalization/coefficients', 'component-conditioned attenuation',
                   'independent central efficiency or declared theoretical calibration', 'shared event/calibration covariance'],
              'checks': checks, 'check_count': len(checks)}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ['check_count','magic_angle_degrees','at_55_degrees','lab_magic_angle_rest_frame_P2_beta045','single_distance_free_normalization_control','aperture_controls']}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
