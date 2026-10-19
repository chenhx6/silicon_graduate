#!/usr/bin/env python3
"""Actual ROOT option and literal producer-expression controls; no data fit."""
from pathlib import Path
from datetime import datetime, timezone
from array import array
import hashlib
import json
import math
import ctypes
import ROOT as R

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def deviance(d, m, first=1, last=None):
    out = 0.0
    for o, s in zip(d[first-1:last], m[first-1:last]):
        if o > 0 and s == 0:
            return 'infinity'
        if o == 0:
            out += 2*s
        else:
            out += 2*(s-o+o*math.log(o/s))
    return out


def main():
    assert R.gROOT.GetVersion() == '6.40.04'
    cp = RUN / 'root-chi2-ll-exercise-contract.json'
    c = json.loads(cp.read_text())
    manifest = json.loads((RUN / 'root-chi2-ll-source-manifest.json').read_text())
    source_checks = []
    for x in manifest['rows']:
        p = ROOT / x['path']
        assert sha(p) == x['sha256']
        s = p.read_text()
        a = s.index('Double_t TH1::Chi2Test(')
        b = s.index('Double_t TH1::Chisquare(', a)
        body = s[a:b]
        assert 'Contains("LL")' not in body and 'Contains("L")' not in body
        assert all(f'Contains("{opt}")' in body for opt in ['UU', 'UW', 'WW', 'NORM', 'OF', 'UF'])
        source_checks.append({'tag': x['tag'], 'LL_not_consumed_in_test_functions': True})
    e = json.loads((RUN / 'root-chi2-ll-expression-manifest.json').read_text())
    assert sha(ROOT / e['source']) == e['sha256']
    fragment = ROOT / e['extracted_path']
    assert sha(fragment) == e['extracted_normalized_line_endings_sha256']
    code = '#include <TH1F.h>\n#include <TAxis.h>\n#include <cmath>\n' + fragment.read_text()
    assert R.gInterpreter.Declare(code)
    outputs = []
    kept = []
    for index, fixture in enumerate(c['fixtures']):
        d, m = fixture['D'], fixture['M']
        o = R.TH1F(f'day17_o{index}', '', len(d), 0, len(d))
        h = R.TH1F(f'day17_m{index}', '', len(m), 0, len(m))
        kept += [o, h]
        for i, (v, w) in enumerate(zip(d, m), 1):
            o.SetBinContent(i, v)
            h.SetBinContent(i, w)
        if fixture.get('stored_model_variance_scale') is not None:
            h.Sumw2()
            for i, w in enumerate(m, 1):
                h.SetBinError(i, math.sqrt(w*fixture['stored_model_variance_scale']))
        if fixture.get('axis_range'):
            o.SetAxisRange(*fixture['axis_range'], 'X')
            h.SetAxisRange(*fixture['axis_range'], 'X')
        options = {}
        for opt in ['LL CHI2', 'CHI2', 'UU CHI2', 'UW CHI2', 'WW CHI2', 'LL CHI2/NDF', 'CHI2/NDF']:
            options[opt] = float(o.Chi2Test(h, opt))
        chi, ndf, igood = ctypes.c_double(), ctypes.c_int(), ctypes.c_int()
        pvalue = float(o.Chi2TestX(h, chi, ndf, igood, 'LL'))
        assert chi.value == options['CHI2']
        manual = float(R.log_likelihood(o, h, array('d', fixture['manual_range'])))
        assert options['LL CHI2'] == options['CHI2']
        assert options['LL CHI2/NDF'] == options['CHI2/NDF']
        if options['CHI2/NDF']:
            inferred_ndf = options['CHI2']/options['CHI2/NDF']
        else:
            inferred_ndf = None
        first, last = [o.GetXaxis().FindBin(x) for x in fixture['manual_range']]
        outputs.append({'label': fixture['label'], 'D': d, 'M': m,
                        'stored_model_variance_scale': fixture.get('stored_model_variance_scale'),
                        'options': options, 'inferred_ndf_without_physics_fit_subtraction': inferred_ndf,
                        'Chi2TestX': {'chi2': chi.value, 'ndf': ndf.value, 'igood': igood.value,
                                     'p_value': pvalue},
                        'original_manual_log_likelihood': manual,
                        'manual_first_bin_inclusive': first, 'manual_end_bin_exclusive': last,
                        'proper_fixed_model_deviance_on_same_manual_bins': deviance(d, m, first, last-1),
                        'boundary': 'declared component fixture; not original spectrum or inferred paper statistic'})
    base, stored, zero_model, edge = outputs
    assert base['options']['CHI2'] == base['options']['UU CHI2']
    assert abs(stored['options']['CHI2'] - stored['options']['UW CHI2']) < 1e-12
    assert abs(base['options']['CHI2'] - stored['options']['CHI2']) > .1
    assert zero_model['proper_fixed_model_deviance_on_same_manual_bins'] == 'infinity'
    assert math.isfinite(zero_model['original_manual_log_likelihood'])
    assert abs(base['proper_fixed_model_deviance_on_same_manual_bins'] - base['original_manual_log_likelihood'] - 6) < 1e-12
    assert edge['manual_end_bin_exclusive'] == 3
    out = {'at': datetime.now(timezone.utc).isoformat(), 'ROOT_version': R.gROOT.GetVersion(),
           'ROOT_git_commit': R.gROOT.GetGitCommit(), 'script_sha256': sha(Path(__file__)),
           'contract_sha256': sha(cp), 'source_checks': source_checks, 'native_cases': outputs,
           'LL_is_ignored_in_test_not_likelihood_switch': True,
           'manual_zero_bin_and_endpoint_boundaries_demonstrated': True,
           'not_original_thesis_ROOT_binary_or_paper_job': True,
           'no_new_experimental_tau_branch_or_CI': True, 'ok': True}
    (RUN / 'root-chi2-ll-exercise-result.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
