#!/usr/bin/env python3
"""Replay declared native two-step controls and diagnostics; never fit DSAM data."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
from day17_geant4_stopping_trace import strict_patch

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'
WORK = ROOT/'tmp/day17-geant4-stopping/component'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    initial = json.loads((RUN/'geant4-alongstep-native-result.json').read_text())
    summary = json.loads((RUN/'geant4-alongstep-native-summary.json').read_text())
    fixture = RUN/'geant4-alongstep-fixture.cc'
    assert sha(fixture) == summary['fixture_sha256']
    work = Path(tempfile.mkdtemp(prefix='native-replay-', dir=WORK))
    env = dict(os.environ)
    for line in subprocess.check_output(['geant4-config', '--datasets'], text=True).splitlines():
        _, name, path = line.split(maxsplit=2)
        env[name] = path
    env['TMPDIR'], env['G4WORKDIR'] = str(work), str(work)
    receipt = {'fixture_sha256': sha(fixture), 'script_sha256': sha(__file__), 'commands': []}

    def run(command):
        p = subprocess.run(command, cwd=ROOT, env=env, capture_output=True, text=True, timeout=180)
        receipt['commands'].append({'command': command, 'exit_code': p.returncode,
                                    'stdout': p.stdout, 'stderr': p.stderr})
        (RUN/'geant4-alongstep-replay.json').write_text(json.dumps(receipt, indent=2)+'\n')
        assert p.returncode == 0, p.stderr
        return p.stdout

    def steps(output):
        return [x for x in output.splitlines() if x.startswith('NATIVE_STEP,')]

    native_exe = work/'native'
    command = list(initial['commands'][0]['command'])
    command[command.index('-o')+1] = str(native_exe)
    run(command)
    for frozen in initial['commands'][1:]:
        output = run([str(native_exe), *frozen['command'][1:]])
        assert steps(output) == steps(frozen['stdout'])
    source = ROOT/'tmp/day17-geant4-stopping/G4IonParametrisedLossModel_lowenergy.cc'
    for name, oldpath in [('geant4-alongstep-trace.json', 'ParamNativeTrace.cc'),
                          ('geant4-alongstep-qtrace.json', 'ParamNativeQTrace.cc')]:
        frozen = json.loads((RUN/name).read_text())
        assert sha(source) == frozen['source_sha256']
        target = work/oldpath
        target.write_text(strict_patch(source.read_text(), frozen['diff']))
        assert sha(target) == frozen['trace_source_sha256']
        command = list(frozen['commands'][0]['command'])
        old = str(Path('tmp/day17-geant4-stopping/component')/oldpath)
        command[command.index(old)] = str(target)
        exe = work/oldpath.replace('.cc', '')
        command[command.index('-o')+1] = str(exe)
        run(command)
        for oldrun in frozen['commands'][1:]:
            output = run([str(exe), *oldrun['command'][1:]])
            assert steps(output) == steps(oldrun['stdout'])
            diagnostic = lambda x: [s for s in x.splitlines() if s.startswith('TRACE_')]
            assert diagnostic(output) == diagnostic(oldrun['stdout'])
    receipt.update({'native_steps_exactly_equal': True, 'diagnostic_steps_and_trace_equal': True,
                    'SDK_not_modified': True, 'ok': True})
    (RUN/'geant4-alongstep-replay.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print('native/diagnostic control replay passed')


if __name__ == '__main__':
    main()
