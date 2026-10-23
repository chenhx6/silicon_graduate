#!/usr/bin/env python3
"""Run unmodified, hash-identified public SIGMA on declared rotor inputs.

No nuclear measurements or experimental errors are generated. The source and
executable remain in tmp. Requires gfortran; source hash is mandatory.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from math import factorial as f
from pathlib import Path
import re
import subprocess

SOURCE_SHA = '9e8cd64b844c75fe49c5b7994f500668284ca7390df45ccb2c2e0fb97ae3af6c'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def tri_2(a2, b2, c2):
    if a2 + b2 < c2 or a2 + c2 < b2 or b2 + c2 < a2:
        return 0.0
    if (a2 + b2 + c2) % 2 != 0:
        return 0.0
    num = f((a2+b2-c2)//2) * f((a2-b2+c2)//2) * f((-a2+b2+c2)//2)
    den = f((a2+b2+c2)//2 + 1)
    return math.sqrt(num / den)

def w3j(j1, j2, j3, m1, m2, m3):
    j1_2, j2_2, j3_2 = int(round(2*j1)), int(round(2*j2)), int(round(2*j3))
    m1_2, m2_2, m3_2 = int(round(2*m1)), int(round(2*m2)), int(round(2*m3))
    if m1_2 + m2_2 + m3_2 != 0:
        return 0.0
    if abs(m1_2) > j1_2 or abs(m2_2) > j2_2 or abs(m3_2) > j3_2:
        return 0.0
    if (j1_2 + abs(m1_2)) % 2 != 0 or (j2_2 + abs(m2_2)) % 2 != 0 or (j3_2 + abs(m3_2)) % 2 != 0:
        return 0.0
    tr = tri_2(j1_2, j2_2, j3_2)
    if tr == 0.0:
        return 0.0
    zmin = max(0, (j2_2 - j3_2 - m1_2)//2, (j1_2 - j3_2 + m2_2)//2)
    zmax = min((j1_2 + j2_2 - j3_2)//2, (j1_2 - m1_2)//2, (j2_2 + m2_2)//2)
    s = 0.0
    for z in range(zmin, zmax + 1):
        den = (f(z) *
               f((j1_2 + j2_2 - j3_2)//2 - z) *
               f((j1_2 - m1_2)//2 - z) *
               f((j2_2 + m2_2)//2 - z) *
               f((j3_2 - j2_2 + m1_2)//2 + z) *
               f((j3_2 - j1_2 - m2_2)//2 + z))
        s += ((-1)**z) / den
    pref = math.sqrt(f((j1_2+m1_2)//2) * f((j1_2-m1_2)//2) *
                     f((j2_2+m2_2)//2) * f((j2_2-m2_2)//2) *
                     f((j3_2+m3_2)//2) * f((j3_2-m3_2)//2))
    return (-1)**((j1_2-j2_2-m3_2)//2) * tr * pref * s

def w6j(j1, j2, j3, j4, j5, j6):
    j1_2, j2_2, j3_2 = int(round(2*j1)), int(round(2*j2)), int(round(2*j3))
    j4_2, j5_2, j6_2 = int(round(2*j4)), int(round(2*j5)), int(round(2*j6))
    t1 = tri_2(j1_2, j2_2, j3_2)
    t2 = tri_2(j1_2, j5_2, j6_2)
    t3 = tri_2(j4_2, j2_2, j6_2)
    t4 = tri_2(j4_2, j5_2, j3_2)
    if t1 == 0.0 or t2 == 0.0 or t3 == 0.0 or t4 == 0.0:
        return 0.0
    zmin = max((j1_2 + j2_2 + j3_2)//2,
               (j1_2 + j5_2 + j6_2)//2,
               (j4_2 + j2_2 + j6_2)//2,
               (j4_2 + j5_2 + j3_2)//2)
    zmax = min((j1_2 + j2_2 + j4_2 + j5_2)//2,
               (j2_2 + j3_2 + j5_2 + j6_2)//2,
               (j3_2 + j1_2 + j6_2 + j4_2)//2)
    s = 0.0
    for z in range(zmin, zmax + 1):
        num = ((-1)**z) * f(z + 1)
        den = (f(z - (j1_2 + j2_2 + j3_2)//2) *
               f(z - (j1_2 + j5_2 + j6_2)//2) *
               f(z - (j4_2 + j2_2 + j6_2)//2) *
               f(z - (j4_2 + j5_2 + j3_2)//2) *
               f((j1_2 + j2_2 + j4_2 + j5_2)//2 - z) *
               f((j2_2 + j3_2 + j5_2 + j6_2)//2 - z) *
               f((j3_2 + j1_2 + j6_2 + j4_2)//2 - z))
        s += num / den
    return t1 * t2 * t3 * t4 * s

def table_text():
    # Official OP,SIXJ: {top_j, 2, 2; base_s, base_s+k-3, base_s+m-3}.
    # gosia_20081208.10.f lines2245–2261; arguments therein are doubled.
    lines = []
    for top_j in (2, 4):
        for l in range(1, 81):
            s = (l - 1) / 2.0
            for k in range(1, 6):
                r = s + k - 3
                row = []
                for m in range(1, 6):
                    v = s + m - 3
                    if min(s, r, v) < 0:
                        row.append(0.0)
                    else:
                        row.append(w6j(top_j, 2, 2, s, r, v))
                lines.append(' '.join(f'{val:.17g}' for val in row))
    return '\n'.join(lines) + '\n'

def rotor_network(jmax, amplitudes, probability):
    n = len(amplitudes)
    if n == 1:
        u = [[1.0]]
    elif n == 2:
        u = [[math.sqrt(probability), math.sqrt(1 - probability)],
             [-math.sqrt(1 - probability), math.sqrt(probability)]]
    else:
        raise ValueError('Only 1 or 2 declared axial rotors supported')
    states = [(j, b) for j in range(0, jmax + 1, 2) for b in range(n)]
    elements = []
    for i, (j, b) in enumerate(states):
        for k, (jp, bp) in enumerate(states[i:], i):
            angular = float((-1)**j * math.sqrt((2 * j + 1) * (2 * jp + 1))
                            * w3j(j, 2, jp, 0, 0, 0))
            if angular == 0.0:
                continue
            value = 0.0
            for a, q in enumerate(amplitudes):
                left = u[b][a] if j == 0 else float(b == a)
                right = u[bp][a] if jp == 0 else float(bp == a)
                value += left * right * q * angular
            if abs(value) > 1e-15:
                elements.append((i + 1, k + 1, value))
    lines = [f'{len(states)} {len(elements)} 1 {len(elements)}']
    lines += [f'{i+1} {j} {j*(j+1)/100:.17g}' for i, (j, b) in enumerate(states)]
    lines += [f'{m+1} {i} {k}' for m, (i, k, x) in enumerate(elements)]
    lines += [f'{m+1} {x:.17g}' for m, (i, k, x) in enumerate(elements)]
    lines += ['0 0']
    return states, elements, '\n'.join(lines) + '\n'

def first_state_rows(output):
    blocks = re.split(r'INDEX=\s*', output)
    if len(blocks) < 2:
        return {'parse_error': 'No INDEX block'}
    lines = blocks[1].splitlines()
    rows = []
    for i, line in enumerate(lines):
        if not re.fullmatch(r'\s*[-+0-9.EeDd\s]+', line) or not re.search(r'\d', line):
            continue
        try:
            values = [float(x.replace('D', 'E')) for x in line.split()]
        except ValueError:
            continue
        rows.append({'preceding_label': lines[i-1].strip() if i > 0 else '', 'printed_values': values})
    return {'rows_in_printed_order': rows, 'note': 'Four-decimal formatted values; raw output retained. No errors requested.'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--workdir', type=Path, required=True)
    parser.add_argument('--result', type=Path, required=True)
    args = parser.parse_args()
    source = args.source.resolve()
    if digest(source) != SOURCE_SHA:
        raise SystemExit('Public source hash mismatch; no execution')
    work = args.workdir.resolve()
    work.mkdir(parents=True, exist_ok=True)
    executable = work / 'sigma'
    compiler = subprocess.run(['gfortran', '--version'], text=True, capture_output=True)
    command = ['gfortran', '-std=legacy', '-O0', '-fcheck=all', '-fbacktrace', str(source), '-o', str(executable)]
    compile_run = subprocess.run(command, text=True, capture_output=True, timeout=120)
    result = {'observed_at_utc': datetime.now(timezone.utc).isoformat(),
              'scope': 'Declared one/two axial rigid rotor controls only; no experimental data, fit, CI or actual producer identity.',
              'source_sha256': SOURCE_SHA, 'compiler': compiler.stdout.splitlines()[0],
              'compile': {'argv': command, 'exit_code': compile_run.returncode, 'stdout': compile_run.stdout, 'stderr': compile_run.stderr},
              'rme_convention': '<Jb||E2||Jpbp>=(-1)^J sqrt((2J+1)(2Jp+1))*3j(J,2,Jp;0,0,0)*sum_a U_J[b,a] Qa U_Jp[bp,a]; U_J=identity unless J=0.',
              'units': 'Arbitrary declared E20 reference unit; all Q positive, delta=0 on every rotor.',
              'cases': []}
    if compile_run.returncode == 0:
        table = table_text()
        result['sixj_table_sha256'] = hashlib.sha256(table.encode()).hexdigest()
        cases = [('rigid_j2', 2, [1.0], 1.0), ('rigid_j4', 4, [1.0], 1.0),
                 ('rigid_j6', 6, [1.0], 1.0), ('amplitude_mix_j6', 6, [1.0, 2.0], 0.5)]
        for name, jmax, amps, p in cases:
            folder = work / name
            folder.mkdir(exist_ok=True)
            if (folder / 'sigma.out').exists():
                raise SystemExit('Refuse to overwrite existing execution: ' + str(folder))
            states, els, smr = rotor_network(jmax, amps, p)
            (folder / 'test.smr').write_text(smr)
            (folder / 'dummy.err').write_text('')
            (folder / 'sixj.tab').write_text(table)
            (folder / 'sigma.inp').write_text('0\n-1\ntest.smr\ndummy.err\nsixj.tab\n')
            execution = subprocess.run([str(executable)], cwd=folder, text=True, capture_output=True, timeout=60)
            output = (folder / 'sigma.out').read_text() if (folder / 'sigma.out').exists() else ''
            probs = [1.0] if len(amps) == 1 else [p, 1 - p]
            moments = {f'M{k}': sum(w * q**k for w, q in zip(probs, amps)) for k in range(2, 7)}
            m3hat = ((math.sqrt(moments['M2']) + moments['M4']**0.25) / 2)**3
            m5hat = ((moments['M4']**0.25 + moments['M6']**(1/6)) / 2)**5
            result['cases'].append({'name': name, 'jmax': jmax, 'state_list': states, 'elements': els,
              'source_and_input_hashes': {f: digest(folder / f) for f in ('test.smr', 'dummy.err', 'sixj.tab', 'sigma.inp')},
              'exit_code': execution.returncode, 'stdout': execution.stdout, 'stderr': execution.stderr,
              'raw_output': output, 'first_state': first_state_rows(output),
              'full_axial_model_ground_moments': moments,
              'full_axial_model_true_cos_mean': 1.0, 'full_axial_model_true_cos_variance': 0.0,
              'full_axial_model_var_Q2': moments['M4'] - moments['M2']**2,
              'manual_interpolation': {'M3_hat': m3hat, 'M5_hat': m5hat,
                'cos3_from_third_proxy': moments['M3'] / m3hat,
                'cos3_from_fifth_proxy': moments['M5'] / m5hat,
                'sixth_normalized_width_proxy': 1 - (moments['M3'] / m3hat)**2},
              'boundary': 'Exact full model moments do not assert a truncated ladder is converged. jmax6 suffices all ground-state paths through six rank2 operators for these axial models. Printed precision is not numerical accuracy or experimental uncertainty.'})
    args.result.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'compile_exit': compile_run.returncode,
                      'cases': [{'name': x['name'], 'exit_code': x['exit_code'],
                                 'interpolation': x['manual_interpolation']} for x in result['cases']]}, indent=2))

if __name__ == '__main__':
    main()
