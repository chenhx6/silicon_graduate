#!/usr/bin/env python3
"""Day21 structural writeback check; no scientific certification."""
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT = 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam.md'
BASELINE = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/baseline-001.json'


def knowledge_path(name):
    if not isinstance(name, str):
        raise ValueError('path must be a string')
    p = (ROOT / name).resolve()
    if not p.is_relative_to(ROOT / 'knowledge') or p.suffix != '.md':
        raise ValueError(f'knowledge path boundary: {name}')
    return p


def check(report):
    errors = []
    blocks = re.findall(r'^```knowledge-writeback\s*\n(.*?)^```\s*$', report, re.M | re.S)
    if len(blocks) != 1:
        return {'valid':False,'scope':'structure only',
                'errors':[f'exactly one knowledge-writeback block required; found {len(blocks)}']}
    try:
        data = json.loads(blocks[0])
        if data.get('status') not in ('updated', 'verified-no-op'):
            raise ValueError('invalid writeback status')
        items = data.get('items')
        if not isinstance(items, list) or not items:
            raise ValueError('nonempty item list required')
        before = json.loads(BASELINE.read_text())['knowledge_sha256']
        changed = []
        for index, item in enumerate(items):
            p = knowledge_path(item['knowledge'])
            body = p.read_text()
            anchor = item.get('anchor')
            if not isinstance(anchor, str) or not anchor.strip() or anchor not in body:
                errors.append(f'item {index}: missing exact anchor')
            if not isinstance(item.get('summary'), str) or not item['summary'].strip():
                errors.append(f'item {index}: missing summary')
            changed.append(hashlib.sha256(p.read_bytes()).hexdigest() != before.get(item['knowledge']))
            sources = item.get('sources')
            if not isinstance(sources, list) or not sources:
                errors.append(f'item {index}: sources required')
                continue
            for source in sources:
                sp = knowledge_path(source['path'])
                if not sp.is_relative_to(ROOT/'knowledge/sources'):
                    errors.append(f'item {index}: reference is not a source page')
                locator = source.get('locator')
                if not isinstance(locator, str) or not re.fullmatch(r'[A-Za-z0-9]+(?:-[A-Za-z0-9]+)+', locator):
                    errors.append(f'item {index}: expected one atomic claim ID')
                    continue
                rows = [line for line in sp.read_text().splitlines()
                        if line.startswith('| '+locator+' |')]
                if len(rows) != 1:
                    errors.append(f'item {index}: atomic source row missing or duplicated: {locator}')
                elif re.search(r'superseded|withdrawn|旧认证撤回', rows[0], re.I):
                    errors.append(f'item {index}: superseded reference: {locator}')
        if data['status'] == 'updated' and not any(changed):
            errors.append('updated requires an actual knowledge change from the run baseline')
        return {'valid':not errors, 'items':len(items),'status':data['status'],
                'scope':'structure, atomic references and changed-page presence only; not source truth or experimental CI',
                'errors':errors}
    except (ValueError, TypeError, KeyError, OSError) as exc:
        return {'valid':False,'errors':[str(exc)],'scope':'structure only'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report',default=DEFAULT)
    args=parser.parse_args()
    p=(ROOT/args.report).resolve()
    if not p.is_relative_to(ROOT):
        parser.error('report must be inside Wiki')
    result=check(p.read_text())
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0 if result['valid'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
