"""Adversarial record checks; these do not certify scientific conclusions."""
import contextlib
from copy import deepcopy
import io
import json
from pathlib import Path
import subprocess
import tempfile
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))

from system.scripts.wiki_research_cycle import load_records, main, validate_record
from system.scripts.wiki_automation_preflight import git_directories, probe

ROOT = Path(__file__).resolve().parents[2]


def planned():
    return deepcopy(load_records(ROOT / 'knowledge/methods/evidence-driven-research-cycle.md')[0])


def executed():
    r = planned()
    c = r['cycles'][0]
    c['action'].update(state='executed', artifact='knowledge/methods/example.md#check')
    c.update(outcome='limits', evidence=[dict(source_id='source-a', locator='p. 2', lineage='experiment-a', kind='direct-report')],
             verification=dict(basis='direct-source', scope='definition only'), independent_lineages_claimed=1)
    return r


def validation():
    return dict(input_sha256='a'*64, evaluator_sha256='b'*64, baseline_evaluator_sha256='b'*64,
                development_ids=['dev'], confirmation_ids=['confirm'], confirmation_used_for_selection=False,
                scope='independent-check', independence_basis='separate measurement; physical assumptions still shared')


class RecordTests(unittest.TestCase):
    def test_valid_plan_and_execution(self):
        self.assertEqual(validate_record(planned()), [])
        self.assertEqual(validate_record(executed()), [])

    def test_plan_cannot_complete_or_promote(self):
        for change in ({'promote': True}, {'outcome': 'supports'}):
            r = planned(); r['cycles'][0].update(change)
            self.assertTrue(validate_record(r))

    def test_execution_requires_artifact_and_locator(self):
        for key in ('artifact',):
            r = executed(); del r['cycles'][0]['action'][key]
            self.assertTrue(validate_record(r))
        r = executed(); r['cycles'][0]['evidence'][0]['locator'] = ''
        self.assertTrue(validate_record(r))

    def test_duplicate_reports_do_not_add_independence(self):
        r = executed(); c = r['cycles'][0]
        c['evidence'].append(dict(c['evidence'][0], source_id='thesis-a'))
        c['independent_lineages_claimed'] = 2
        self.assertTrue(validate_record(r))

    def test_novelty_boundary(self):
        r = planned(); n = r['hypotheses'][0]['novelty']
        n['status'] = 'world-first'
        self.assertTrue(validate_record(r))
        n['status'] = 'bounded-search'
        self.assertTrue(validate_record(r))
        n.update(queries=['query'], closest_work=['source-a'], searched_at='2026-11-27')
        self.assertEqual(validate_record(r), [])

    def test_tree_unknown_parent_and_cycle(self):
        r = planned(); h = r['hypotheses'][0]
        h['parent'] = 'absent'
        self.assertTrue(validate_record(r))
        h['parent'] = h['id']
        self.assertTrue(validate_record(r))
        r['hypotheses'].append(dict(h, id='H2', parent=h['id']))
        h['parent'] = 'H2'
        self.assertTrue(validate_record(r))

    def test_failed_branches_need_revival_condition(self):
        r = planned(); h = r['hypotheses'][0]
        h['disposition'] = 'rejected'
        self.assertTrue(validate_record(r))
        h.update(rejection_reason='condition absent', revival_condition='new sensitivity measurement')
        self.assertEqual(validate_record(r), [])
        c = r['cycles'][0]; c['outcome'] = 'refutes'
        self.assertTrue(validate_record(r))

    def test_absent_signal_needs_sensitivity(self):
        r = executed(); c = r['cycles'][0]
        c['absent_companion'] = dict(used_as_falsifier=True, sensitivity='unknown')
        self.assertTrue(validate_record(r))
        c['absent_companion'].update(sensitivity='adequate', sensitivity_evidence='injection sensitivity, locator')
        self.assertEqual(validate_record(r), [])

    def test_independent_confirmation_and_evaluator(self):
        r = executed(); c = r['cycles'][0]; c['validation'] = validation()
        self.assertEqual(validate_record(r), [])
        for field, value in [('scope', []), ('confirmation_ids', ['dev']),
                             ('confirmation_used_for_selection', True), ('evaluator_sha256', 'c'*64),
                             ('independence_basis', '')]:
            bad = deepcopy(r); bad['cycles'][0]['validation'][field] = value
            self.assertTrue(validate_record(bad), field)
        c['verification']['basis'] = 'same-implementation'
        self.assertTrue(validate_record(r))
        c['validation']['scope'] = 'internal-recovery'
        self.assertEqual(validate_record(r), [])

    def test_unverified_execution_cannot_promote(self):
        r = executed(); c = r['cycles'][0]
        c['promote'] = True
        c['verification']['basis'] = 'not-performed'
        self.assertTrue(validate_record(r))
        c['verification']['basis'] = 'direct-source'
        self.assertEqual(validate_record(r), [])

    def test_review_history_does_not_gate(self):
        r = executed()
        for value in ('human-reviewed', 'needs-review', None, []):
            r['review_status'] = value
            self.assertEqual(validate_record(r), [])

    def test_malformed_json_values_never_crash(self):
        values = [None, True, 1, [], {}, ['nested'], '']
        self.assertTrue(validate_record(None))
        for value in values:
            for top in ('hypotheses', 'cycles', 'question', 'schema'):
                r = executed(); r[top] = value; validate_record(r)
            for key in ('id', 'parent', 'novelty', 'disposition'):
                r = executed(); r['hypotheses'][0][key] = value; validate_record(r)
            for key in ('id', 'hypothesis_id', 'outcome', 'action', 'evidence', 'verification', 'validation', 'absent_companion', 'independent_lineages_claimed'):
                r = executed(); r['cycles'][0][key] = value; validate_record(r)
            for key in validation():
                r = executed(); r['cycles'][0]['validation'] = validation()
                r['cycles'][0]['validation'][key] = value; validate_record(r)


class CliTests(unittest.TestCase):
    def run_cli(self, root, *paths):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = main(['--root', str(root), *map(str, paths)])
        return code, json.loads(output.getvalue())

    def test_paths_and_multiple_blocks(self):
        with tempfile.TemporaryDirectory() as folder, tempfile.TemporaryDirectory() as outside:
            root = Path(folder); (root/'knowledge').mkdir()
            good = root/'knowledge/good.json'; good.write_text(json.dumps(planned()))
            self.assertEqual(self.run_cli(root, good)[0], 0)
            self.assertEqual(self.run_cli(root, 'knowledge/good.json')[0], 0)
            escape = Path(outside)/'escape.json'; escape.write_text(json.dumps(planned()))
            (root/'knowledge/link.json').symlink_to(escape)
            for p in (escape, 'knowledge/link.json', '../escape.json', root):
                self.assertEqual(self.run_cli(root, p)[0], 1)
            for content in ('{', '# no block', '```research-cycle\n{\n```'):
                bad = root/'knowledge/bad.md'; bad.write_text(content)
                self.assertEqual(self.run_cli(root, bad)[0], 1)
            multi = root/'knowledge/multi.md'
            block = '```research-cycle\n'+json.dumps(planned())+'\n```\n'
            multi.write_text(block+block)
            code, report = self.run_cli(root, multi)
            self.assertEqual(code, 0); self.assertEqual(report['reports'][0]['records'], 2)


class GitMetadataTests(unittest.TestCase):
    def test_ordinary_and_linked_checkout(self):
        with tempfile.TemporaryDirectory() as folder:
            repo = Path(folder)/'repo'; linked = Path(folder)/'linked'
            def git(*args):
                return subprocess.run(['git', *args], check=True, capture_output=True, text=True).stdout.strip()
            git('init', str(repo))
            git('-C', str(repo), '-c', 'user.name=Test', '-c', 'user.email=test@example.invalid', 'commit', '--allow-empty', '-m', 'fixture')
            git('-C', str(repo), 'worktree', 'add', '-b', 'test-linked', str(linked))
            self.assertEqual(git_directories(repo), [(repo/'.git').resolve()])
            dirs = git_directories(linked)
            self.assertEqual(len(dirs), 2)
            self.assertIn((repo/'.git').resolve(), dirs)
            self.assertTrue((linked/'.git').is_file())
            for directory in dirs:
                result = probe(directory, 'research-cycle-test')
                self.assertTrue(all(result[key] for key in ('created', 'read_back', 'deleted')), result)


if __name__ == '__main__':
    unittest.main()
