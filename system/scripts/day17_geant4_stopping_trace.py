#!/usr/bin/env python3
"""Replay the saved diagnostics-only patch on a verified public source copy."""
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'
WORK = ROOT/'tmp/day17-geant4-stopping/component'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def strict_patch(original, diff):
    source = original.splitlines(keepends=True)
    lines = diff.splitlines(keepends=True)
    output, cursor, i = [], 0, 0
    while i < len(lines):
        hunk = re.match(r'^@@ -(\d+)(?:,\d+)? \+\d+(?:,\d+)? @@', lines[i])
        if not hunk:
            i += 1
            continue
        start = int(hunk.group(1))-1
        assert start >= cursor
        output.extend(source[cursor:start])
        i += 1
        old, new = [], []
        while i < len(lines) and not lines[i].startswith('@@ '):
            line = lines[i]
            assert line[:1] in [' ', '+', '-']
            if line[:1] in [' ', '-']: old.append(line[1:])
            if line[:1] in [' ', '+']: new.append(line[1:])
            i += 1
        assert source[start:start+len(old)] == old
        output.extend(new)
        cursor = start+len(old)
    output.extend(source[cursor:])
    return ''.join(output)


def main():
    frozen = json.loads((RUN/'geant4-stopping-param-trace.json').read_text())
    source = ROOT/'tmp/day17-geant4-stopping/G4IonParametrisedLossModel_lowenergy.cc'
    assert sha(source) == frozen['source_sha256']
    target = Path(tempfile.mkdtemp(prefix='trace-replay-', dir=WORK))/'ParamTrace.cc'
    target.write_text(strict_patch(source.read_text(), frozen['diff']))
    assert sha(target) == frozen['trace_source_sha256']
    cmd = list(frozen['commands'][0]['command'])
    cmd[cmd.index('tmp/day17-geant4-stopping/component/ParamTrace.cc')] = str(target)
    index = cmd.index('-o')+1
    exe = target.parent/'stopping-trace'
    cmd[index] = str(exe)
    compile_result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert compile_result.returncode == 0, compile_result.stderr
    env = dict(os.environ)
    for line in subprocess.check_output(['geant4-config', '--datasets'], text=True).splitlines():
        _, name, path = line.split(maxsplit=2)
        env[name] = path
    env['TMPDIR'] = str(WORK)
    env['G4WORKDIR'] = str(WORK)
    run = subprocess.run([str(exe), 'external'], cwd=ROOT, env=env,
                         input=frozen['commands'][1]['input'], capture_output=True,
                         text=True, timeout=90)
    assert run.returncode == 0, run.stderr
    lines = [x for x in run.stdout.splitlines() if x.startswith(('TRACE_', 'STOPPING,'))]
    old = [x for x in frozen['commands'][1]['stdout'].splitlines() if x.startswith(('TRACE_', 'STOPPING,'))]
    assert lines == old
    receipt = {'patch_applied_with_exact_context': True, 'compile_exit_code': compile_result.returncode,
               'run_exit_code': run.returncode, 'physics_trace_exactly_equal': True,
               'script_sha256': sha(__file__), 'trace_source_sha256': sha(target),
               'public_source_unchanged': sha(source) == frozen['source_sha256'],
               'matching_lines': lines, 'SDK_not_modified': True}
    (RUN/'geant4-stopping-param-trace-replay.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
