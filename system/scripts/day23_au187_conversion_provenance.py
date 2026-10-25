"""Read frozen official ENSDF annotations; no mixing-ratio or likelihood fit."""
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path


class PreText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.parts = []
        self.blocks = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'pre':
            self.depth += 1
            self.blocks += 1

    def handle_endtag(self, tag):
        if tag == 'pre':
            self.depth -= 1

    def handle_data(self, data):
        if self.depth:
            self.parts.append(data)


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load_records(path):
    parser = PreText()
    parser.feed(path.read_text())
    assert parser.blocks == 1 and parser.depth == 0
    text = ''.join(parser.parts)
    lines = text.splitlines()
    assert all(not s or s.startswith(('187AU', '187HG')) for s in lines)
    parent = None
    groups = []
    for i, line in enumerate(lines):
        if line[5:9] == '  L ':
            parent = {'energy_string': line[9:19].strip(),
                      'jp_string': line[21:39].strip(),
                      'half_life_string': line[39:49].strip(),
                      'line': i + 1, 'raw': line}
        if line[5:9] == '  G ' and line[9:19].strip() in ('376.3', '462.1'):
            assert parent is not None
            end = i + 1
            while end < len(lines) and lines[end][5:9] not in ('  L ', '  G '):
                end += 1
            groups.append({'parent': dict(parent), 'gamma_energy_string': line[9:19].strip(),
                           'MR_string': line[41:49].strip(),
                           'DMR_string': line[49:55].strip(),
                           'total_CC_string': line[55:62].strip(),
                           'DCC_string': line[62:64].strip(),
                           'line': i + 1,
                           'records': [{'line': j + 1, 'raw': lines[j]} for j in range(i, end)]})
    return {'input': str(path), 'input_sha256': digest(path),
            'pre_text_sha256': hashlib.sha256(text.encode()).hexdigest(),
            'pre_text_lines': len(lines),
            'headers': [{'line': i + 1, 'raw': s} for i, s in enumerate(lines[:52])],
            'targets': groups}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--contract', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    contract = json.loads(args.contract.read_text())
    for name, expected in contract['inputs'].items():
        assert digest(Path(name)) == expected
    result = {name: load_records(Path('tmp/day23-originals') / f'au187-{name}-029.ens')
              for name in ['adopted', 'hg24', 'hg19']}
    ad, hg, low = (result[n] for n in ['adopted', 'hg24', 'hg19'])
    all_raw = {n: '\n'.join(v['raw'] for v in r['headers']) for n, r in result.items()}
    pair = {(r['parent']['energy_string'], r['gamma_energy_string']): r for r in hg['targets']}
    exp = [r for t in hg['targets'] for r in t['records'] if '|a(K)exp=' in r['raw']]
    controls = {
        'all_frozen_response_hashes_match': True,
        'HTML_pre_extracted_instead_of_treating_HTTP200_as_plain_ENSDF': True,
        'all_extracted_nonblank_lines_have_nuclide_prefix': True,
        'full2009_cutoff2008_and2013_errata_preserved': all('09NDS' in s and 'CUT=1-Nov-2008' in s and '7-Nov-2013' in s for s in all_raw.values()),
        'target_parent_and_gamma_identity_frozen': set(pair) == {('496.79', '376.3'), ('815.89', '462.1')},
        'adopted_energies_kept_separate': {r['parent']['energy_string'] for r in ad['targets']} == {'496.73', '815.81'},
        'disputed_parent_half_lives_not_filled': all(not r['parent']['half_life_string'] for r in ad['targets'] + hg['targets']),
        'four_experimental_alpha_quotes_keep_attributions': len(exp) == 2 and all('1998Ru04' in r['raw'] and '1978Bo05' in r['raw'] for r in exp),
        '376_exp_comment_not_SG_KC_or_total': '0.119 {I15}' in exp[0]['raw'] and '0.11 {I3}' in exp[0]['raw'] and any('KC=0.119 21' in r['raw'] for r in hg['targets'][0]['records']) and hg['targets'][0]['total_CC_string'] == '0.147',
        '462_exp_comment_not_SG_KC_or_total': '0.050 {I9}' in exp[1]['raw'] and '0.08 {I2}' in exp[1]['raw'] and any('KC=0.051 10' in r['raw'] for r in hg['targets'][1]['records']) and hg['targets'][1]['total_CC_string'] == '0.064',
        'MR_evaluator_derived_not_new_experiment': 'MR$Calculated by the evaluator' in all_raw['hg24'],
        'historical_report_versions_grouped_not_independent_runs': '1998Ru04,1994RuZX,1995Ru07' in all_raw['hg24'],
        '1978_combined_parent_warning_preserved': 'states decay data together' in all_raw['hg19'],
        'parent_clocks_shift_and_private_correction_not_gamma_tau': '13/2(+)' in all_raw['hg24'] and '0.0+X' in all_raw['hg24'] and '3/2(-)' in all_raw['hg19'] and 'not measured (e-mail communication' in all_raw['hg24'],
        'low_parent_dataset_not_new_negative_observation': not low['targets'],
    }
    x = {'scope': contract['scope'], 'formal_day_index': 23, 'records': result,
         'experimental_quotes_as_evaluation_reports': exp,
         'controls': controls, 'all_controls_pass': all(controls.values()),
         'implementation_sha256': digest(Path(__file__)),
         'limitations': ['Primary Rupnik1998/Bourgeois1978 full texts remain unread/unavailable in this route.',
                        'Adopted/API/evaluator MR and quoted experimental alpha are not independent new acquisitions.',
                        'No new delta, sign, CI, theoretical ICC, count rate, lifetime or beamtime was inferred.',
                        'No raw archival mutation; public HTML/text snapshots remain tmp staging.']}
    args.output.write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'all_controls_pass': x['all_controls_pass'], 'controls': controls,
                      'line_counts': {n: r['pre_text_lines'] for n, r in result.items()},
                      'target_fields': {n: [{k: r[k] for k in ['parent', 'gamma_energy_string', 'MR_string', 'total_CC_string']} for r in v['targets']] for n, v in result.items()}}))
    raise SystemExit(0 if x['all_controls_pass'] else 1)


if __name__ == '__main__':
    main()
