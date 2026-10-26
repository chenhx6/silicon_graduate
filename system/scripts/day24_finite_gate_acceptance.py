#!/usr/bin/env python3
"""Conditional finite-acceptance exercise; never a replay of AFRODITE data.

The two polar layouts are literal publication descriptions, not selected as
the actual run geometry. Equal weights, point detectors, azimuth-averaged
rings and an unoriented two-photon kernel are declared mathematical controls.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import re

import numpy as np


def p2(x):
    return (3*x*x-1)/2


def p4(x):
    return (35*x**4-30*x*x+3)/8


def moments(rings):
    total = sum(w for _, w in rings)
    return [sum(w*p(np.cos(np.deg2rad(t))) for t, w in rings)/total
            for p in (p2, p4)]


def average_kernel(theta, rings, nphi):
    phi = 2*np.pi*np.arange(nphi)/nphi
    t = np.deg2rad(theta)
    result = 0.
    for gate, weight in rings:
        g = np.deg2rad(gate)
        x = np.cos(t)*np.cos(g)+np.sin(t)*np.sin(g)*np.cos(phi)
        result += weight*np.mean(1+.2*p2(x)+.1*p4(x))
    return result/sum(w for _, w in rings)


def run(root):
    sources = []
    for slug in ['wakudyanaye-2022-triaxiality-rotational-bands-133ce',
                 'ding-2021-131ba-133ce-signature-splitting']:
        source = Path('knowledge/sources')/(slug+'.md')
        text = (root/source).read_text()
        raw = re.search(r'^raw_file: "(.*)"', text, re.M).group(1)
        expected = re.search(r'^raw_sha256: "?([0-9a-fA-F]{64})', text, re.M).group(1).lower()
        actual = hashlib.sha256((root/raw).read_bytes()).hexdigest()
        if actual != expected:
            raise ValueError(f'Raw version mismatch: {source}')
        sources.append({'source': str(source), 'raw': raw, 'sha256': actual,
                        'locator': 'PDF61 §5.2.1; PDF59 Eq4.6' if 'wakudyanaye' in slug else 'manuscript PDF2 §II.A'})
    layouts = {'published_8_description': [(90.,4.),(135.,4.)],
               'thesis_13_description': [(45.,1.),(90.,8.),(135.,4.)]}
    # Independent exact rational benchmarks from cos²45=cos²135=1/2.
    exact = {'published_8_description': [F(-1,8),F(-1,64)],
             'thesis_13_description': [F(-11,52),F(31,416)]}
    checks = []
    def check(name, ok):
        checks.append({'name': name, 'passed': bool(ok)})
    rows = {}
    for name, rings in layouts.items():
        m = moments(rings)
        check(name+'_exact_polar_moments', np.max(np.abs(np.array(m)-[float(x) for x in exact[name]]))<2e-15)
        check(name+'_weight_scale_invariance', np.max(np.abs(np.array(m)-moments([(t,7*w) for t,w in rings])))<2e-15)
        check(name+'_order_invariance', np.max(np.abs(np.array(m)-moments(list(reversed(rings)))))<2e-15)
        check(name+'_even_rank_mirror', np.max(np.abs(np.array(m)-moments([(180-t,w) for t,w in rings])))<2e-15)
        values = []
        for theta in [0.,45.,90.,135.,180.]:
            x = np.cos(np.deg2rad(theta))
            factored = 1+.2*p2(x)*m[0]+.1*p4(x)*m[1]
            # Direct relative-angle kernel integration is a separate route.
            direct = average_kernel(theta, rings, 128)
            check(name+f'_addition_theorem_{theta:g}', abs(direct-factored)<2e-15)
            check(name+f'_azimuth_convergence_{theta:g}', abs(direct-average_kernel(theta,rings,256))<2e-15)
            values.append({'theta_degrees':theta,'conditional_kernel_integral':float(direct)})
        rows[name] = {'polar_moments':m,'polar_moments_exact':[str(x) for x in exact[name]],
                      'synthetic_kernel_values':values,
                      'synthetic_kernel_ratio_135_over_90':values[3]['conditional_kernel_integral']/values[2]['conditional_kernel_integral']}
    # Full-sphere quadrature, including the polar integral absent in finite rings.
    x,w = np.polynomial.legendre.leggauss(8)
    check('full_sphere_P2_P4_vanish', abs(np.dot(w,p2(x))/2)<2e-15 and abs(np.dot(w,p4(x))/2)<2e-15)
    check('full_sphere_rank0_normalization', abs(sum(w)/2-1)<2e-15)
    check('synthetic_kernel_positive_lower_bound', 1-.2-.1>0)
    check('finite_moments_are_not_full_sphere', all(abs(float(v))>0 for ms in exact.values() for v in ms))
    return {'status':'conditional-mathematical-exercise','sources':sources,
            'dimensionless':True,'actual_run_geometry_selected':False,
            'assumptions':['equal detector weights independent of energy',
                           'point detector polar angles; each ring azimuth averaged',
                           'unoriented initial ensemble with W=1+0.2P2(cos opening)+0.1P4(cos opening)',
                           'coefficients are task-chosen positive kernel, not an assigned physical cascade'],
            'layouts':rows,'controls':checks,'all_controls_pass':all(x['passed'] for x in checks),
            'limits':['No real active mask, azimuths, finite solid angle, efficiency, self-pair veto, addback or sorting geometry.',
                      'No reaction alignment or real gate-spin/multipole/feeding response is fitted.',
                      'Ratios are not measured or predicted experimental RAD/DCO/Rac values; no delta or beamtime is derived.',
                      'Nonzero moments disprove automatic full-sphere cancellation in this declared family, not the empirical calibration of the paper.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[2])
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    result = run(args.root)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'all_controls_pass':result['all_controls_pass'],'checks':len(result['controls']),
                      'layouts':result['layouts']},ensure_ascii=False))
    return 0 if result['all_controls_pass'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
