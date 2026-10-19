#!/usr/bin/env python3
"""Build/query the existing SDK with declared materials, cuts and model modes."""
import csv
import hashlib
import json
import os
from pathlib import Path
import shlex
import subprocess

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'
WORK = ROOT/'tmp/day17-geant4-stopping/component'


def main():
    WORK.mkdir(exist_ok=True, parents=True)
    rows = []
    for pair in ['S-Au', 'O-Ta']:
        for x in csv.DictReader((RUN/f'stopping-{pair}-frozen.csv').open()):
            if x['ref_id'] != 'SRIM2013':
                rows.append(x)
    inputs = []
    for i, x in enumerate(rows):
        z = 16 if x['projectile_name'] == 'S' else 8
        inputs.append(f"{i} {z} {int(float(x['ion_isotope']))} G4_{x['target_name']} {x['energy']}")
    inputs += ['1000 16 31 G4_Au 0.0168', '1001 8 15 G4_Ta 0.0014236174061517356',
               '1002 8 15 G4_Ta 0.0025087379886612874']
    source = RUN/'geant4-stopping-fixture.cc'
    contract = {'input_rows': rows, 'input_text': '\n'.join(inputs)+'\n',
                'fixture_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                'modes': ['standard', 'option4', 'external'],
                'scope': 'actualexistingSDKcomponent; nocollisionhistories/fit, nopaperproducer',
                'units': 'E/A times massnumber A; output MeV/(mg/cm2)',
                'cut': 'DBL_MAX electronic total x3, then 1keV restricted x3; allcalls retained; no nuclear added',
                'output_value_order': ['totalfirst','totalsecond','totalthird','restrictedfirst','restrictedsecond','restrictedthird']}
    (RUN/'geant4-stopping-component-contract.json').write_text(json.dumps(contract, indent=2)+'\n')
    result = {'commands': [], 'status': 'started'}

    def run(cmd, **kwargs):
        p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, **kwargs)
        result['commands'].append({'command': cmd, 'exit_code': p.returncode,
                                  'stdout': p.stdout, 'stderr': p.stderr})
        (RUN/'geant4-stopping-component-result.json').write_text(json.dumps(result, indent=2)+'\n')
        print(' '.join(cmd), p.returncode, flush=True)
        if p.returncode:
            raise RuntimeError('component command failed; see receipt')
        return p.stdout

    result['SDK_version'] = run(['geant4-config', '--version']).strip()
    if result['SDK_version'] != '11.4.2':
        raise RuntimeError('unexpected SDK version')
    flags = shlex.split(run(['geant4-config', '--cflags']))
    libflags = shlex.split(run(['geant4-config', '--libs']))
    keep = {'G4physicslists', 'G4run', 'G4event', 'G4tracking', 'G4parmodels',
            'G4processes_hadronic', 'G4processes_core', 'G4digits_hits', 'G4track',
            'G4particles', 'G4geometry', 'G4materials', 'G4graphics_reps',
            'G4intercoms', 'G4global', 'G4clhep', 'G4ptl'}
    libs = [x for x in libflags if x.startswith('-L') or (x.startswith('-l') and x[2:] in keep)]
    exe = WORK/'stopping-fixture'
    run(['c++', *flags, '-O2', str(source), '-o', str(exe), *libs,
         '-Wl,-rpath,/opt/geant4/11.4.2/lib'])
    env = dict(os.environ)
    dataset_lines = run(['geant4-config', '--datasets'])
    result['datasets'] = dataset_lines.splitlines()
    for line in dataset_lines.splitlines():
        _, name, path = line.split(maxsplit=2)
        env[name] = path
    env['TMPDIR'] = str(WORK)
    env['G4WORKDIR'] = str(WORK)
    for mode in contract['modes']:
        out = run([str(exe), mode], input=contract['input_text'], env=env, timeout=180)
        (WORK/f'{mode}.stdout.txt').write_text(out)
        count = sum(x.startswith('STOPPING,') for x in out.splitlines())
        if count != len(inputs):
            raise RuntimeError('incomplete component rows')
    result['status'] = 'component-passed-interpretation-pending'
    (RUN/'geant4-stopping-component-result.json').write_text(json.dumps(result, indent=2)+'\n')


if __name__ == '__main__':
    main()
