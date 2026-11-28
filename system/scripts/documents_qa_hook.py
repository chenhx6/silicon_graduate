#!/usr/bin/env python3
"""Codex turn-scoped adapter for documents_qa. It never edits documents."""

from dataclasses import asdict
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
from tempfile import NamedTemporaryFile

from documents_qa import PATHSPECS, ROOT, changed_paths, eligible, git, git_paths, scan

MAX_REPAIRS = 2


def fingerprints(root, names):
    return {name: sha256((root / name).read_bytes()).hexdigest()
            for name in sorted(names) if eligible(root, name)}


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile(mode='w', dir=path.parent, encoding='utf-8', delete=False) as handle:
        json.dump(value, handle, ensure_ascii=True)
        handle.write('\n')
    Path(handle.name).replace(path)


def git_head(root):
    return git(root, 'rev-parse', 'HEAD').decode('ascii').strip()


def handle(root, payload):
    event = payload.get('hook_event_name')
    if event not in {'UserPromptSubmit', 'Stop'}:
        return {}
    session, turn = payload.get('session_id'), payload.get('turn_id')
    if not isinstance(session, str) or not isinstance(turn, str) or not session or not turn:
        return {'systemMessage': 'documents_QA did not receive Codex session and turn identifiers; run QA manually.'}
    key = sha256(json.dumps([session, turn]).encode()).hexdigest()
    cache = root / 'tmp' / 'documents-qa' / 'hooks'
    if not cache.resolve().is_relative_to(root):
        return {'systemMessage': 'documents_QA hook scratch directory resolves outside the project.'}
    state_path = cache / f'{key}.json'
    if event == 'UserPromptSubmit':
        if not state_path.exists():
            save(state_path, {'head': git_head(root), 'before': fingerprints(root, changed_paths(root)), 'repairs': 0})
        return {}
    if not state_path.is_file():
        return {'systemMessage': 'documents_QA has no baseline for this turn; run the checker on this turn’s edited documents.'}
    state = json.loads(state_path.read_text(encoding='utf-8'))
    current_head = git_head(root)
    candidates = changed_paths(root) | state['before'].keys()
    if current_head != state['head']:
        candidates |= set(git_paths(root, 'diff', '--name-only', '--no-renames', '-z',
                                    state['head'], current_head, '--', *PATHSPECS))
    after = fingerprints(root, candidates)
    paths = [name for name, digest in after.items() if state['before'].get(name) != digest]
    if not paths:
        return {}
    result = scan(root, paths)
    if not result['issues']:
        return {}
    receipt = cache / f'{key}-issues.json'
    save(receipt, {'files': result['files'], 'issues': [asdict(issue) for issue in result['issues']]})
    diagnostics = '\n'.join(f'{i.path}:{i.line} {i.code} {i.reason}' for i in result['issues'][:12])
    details = f"{len(result['issues'])} issue(s). Checklist: {receipt.relative_to(root)}\n{diagnostics}"
    active = payload.get('stop_hook_active') is True
    if state['repairs'] >= MAX_REPAIRS or (active and state['repairs'] == 0):
        return {'systemMessage': 'documents_QA stopped automatic retries. Report this review checklist.\n' + details}
    state['repairs'] += 1
    save(state_path, state)
    return {'decision': 'block', 'reason': (
        f"documents_QA repair pass {state['repairs']}/{MAX_REPAIRS}. Fix only clear document syntax. "
        'Keep scientific content intact. List ambiguous items for manual review and rerun QA.\n' + details
    )}


def main():
    try:
        response = handle(ROOT, json.load(sys.stdin))
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as exc:
        response = {'systemMessage': f'documents_QA hook failed ({type(exc).__name__}); run the checker manually.'}
    print(json.dumps(response, ensure_ascii=True))


if __name__ == '__main__':
    main()
