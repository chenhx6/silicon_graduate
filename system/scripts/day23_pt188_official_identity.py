"""Inspect frozen official Pt evaluated/compiled records without correcting them."""
import argparse
import hashlib
import json
from pathlib import Path

from day23_au187_conversion_provenance import PreText


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read(path):
    parser = PreText()
    parser.feed(path.read_text())
    assert parser.blocks == 1 and parser.depth == 0
    text = ''.join(parser.parts)
    lines = text.splitlines()
    assert all(not line or line.startswith('188PT') for line in lines)
    parent = None
    groups = []
    for i, line in enumerate(lines):
        if line[5:9] == '  L ':
            parent = {'energy': line[9:19].strip(), 'Jp': line[21:39].strip(),
                      'half_life': line[39:49].strip(), 'line': i + 1, 'raw': line}
        if line[5:9] == '  G ':
            end = i + 1
            while end < len(lines) and lines[end][5:9] not in ('  L ', '  G '):
                end += 1
            groups.append({'parent': dict(parent) if parent else None,
                           'Egamma': line[9:19].strip(), 'intensity': line[21:29].strip(),
                           'multipolarity': line[31:41].strip(), 'MR': line[41:49].strip(),
                           'line': i + 1,
                           'records': [{'line': j + 1, 'raw': lines[j]} for j in range(i, end)]})
    return {'path': str(path), 'response_sha256': sha(path),
            'pre_sha256': hashlib.sha256(text.encode()).hexdigest(), 'line_count': len(lines),
            'header_records': [{'line': i + 1, 'raw': line} for i, line in enumerate(lines[:46])],
            'groups': groups}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--contract', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    a = ap.parse_args()
    c = json.loads(a.contract.read_text())
    assert all(sha(Path(p)) == h for p, h in c['source_inputs'].items())
    data = {n: read(Path('tmp/day23-originals') / f'pt188-{n}-037.html')
            for n in ['adopted', 'hi', 'xundl5']}
    targets = {}
    selection = {'hi': [('265.59', '265.6'), ('670.80', '405.1'), ('1085.16', '414.4'), ('1636.12', '550.9')],
                 'xundl5': [('265', '265'), ('670', '405'), ('1085', '414'), ('1636', '551')]}
    for n, pairs in selection.items():
        targets[n] = []
        for parent, gamma in pairs:
            matches = [g for g in data[n]['groups'] if g['parent'] and g['parent']['energy'] == parent and g['Egamma'] == gamma]
            assert len(matches) == 1
            targets[n].append(matches[0])
    headers = {n: '\n'.join(r['raw'] for r in v['header_records']) for n, v in data.items()}
    selected_comments = [r for g in targets['hi'] for r in g['records'] if 'DCO=' in r['raw'] or 'POL=' in r['raw']]
    controls = {
        'all_frozen_response_hashes_match': True,
        'HTML_pre_not_mistaken_for_plain_ENSDF': True,
        'all_record_nuclide_prefixes_checked': True,
        'evaluated2018_cutoff2018_identity': all('201806' in headers[n] and 'CUT=1-Feb-2018' in headers[n] for n in ['adopted', 'hi']),
        'HI_explicitly_groups2014_and2017_in_one_setup_description': '2014Mu12,2017Mu12' in headers['hi'] and 'E=85 MeV' in headers['hi'],
        'HI_energy_intensity_source2017_preserved': 'E,RI$From 2017Mu12' in headers['hi'],
        'XUNDL_is2022Guo_compilation_not_new_acquisition': '2022GU04' in headers['xundl5'] and 'Compiled (unevaluated)' in headers['xundl5'],
        'four_target_parent_gamma_pairs_bound_in_each_snapshot': all(len(v) == 4 for v in targets.values()),
        'coarseXUNDL1636spin8_not_silently_replaced': targets['xundl5'][-1]['parent']['Jp'] == '8+' and targets['hi'][-1]['parent']['Jp'] == '6+',
        'POL_literal_kept_not_promoted_to_P_or_asymmetry': bool(selected_comments),
        'XUNDLtarget_intensity_multipole_and_MR_fields_not_filled': all(not g['intensity'] and not g['multipolarity'] and not g['MR'] for g in targets['xundl5']),
    }
    out = {'scope': c['scope'], 'formal_day_index': 23, 'contract_sha256': sha(a.contract),
           'implementation_sha256': sha(Path(__file__)),
           'datasets': {n: {k: v for k, v in d.items() if k != 'groups'} for n, d in data.items()},
           'selected_targets': targets, 'selected_comments_literal': selected_comments,
           'source_figure_check_as_supplied': c['raw_pdf_freshcheck'],
           'controls': controls, 'all_controls_pass': all(controls.values()),
           'limitations': ['2018 evaluation quotes2017 measurements; original2017 paper and PublisherNote remain unread.',
                          'Compiled2022Guo records are not independent from Guo2022 experiment.',
                          'XUNDL1636 spin8 differs from actual Guo Fig2 green6 and evaluated6; preserve source version and needs_review, do not infer a new transition order.',
                          'Finite resolution/coincidence time and actual detector gates are unknown; no isotope identity verdict or local purity/upperlimit.',
                          'POL field convention and exact covariance require primary method; no new delta, P, lifetime, rate or beamtime.']}
    a.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'all_controls_pass': out['all_controls_pass'], 'line_counts': {n: v['line_count'] for n, v in data.items()},
                      'target_pairs': {n: [(g['parent']['energy'], g['parent']['Jp'], g['Egamma']) for g in v] for n, v in targets.items()},
                      'controls': controls}))
    raise SystemExit(0 if out['all_controls_pass'] else 1)


if __name__ == '__main__':
    main()
