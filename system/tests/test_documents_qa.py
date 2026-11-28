"""Document QA regressions, including a real temporary Git worktree for hooks."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))
import documents_qa as qa
import documents_qa_hook as hook


def issues(text, name='knowledge/sample.md'):
    data = text.encode('utf-8') if isinstance(text, str) else text
    return [(i.line, i.code) for i in qa.check_bytes(name, data)]


class TextQA(unittest.TestCase):
    def test_literal_a_not_valid_commands(self):
        self.assertEqual(issues(r'$r_0 \a1.07$'), [(1, 'TEX_FRAGMENT_A')])
        self.assertEqual(issues(r'$\alpha + \beta + \rho \approx \frac{\text{a}}{\mathrm{b}}$'), [])

    def test_encoding_and_control(self):
        self.assertEqual(issues('汉字\r\n题目'), [])
        self.assertEqual(issues(b'good\n\xff'), [(2, 'ENCODING')])
        self.assertEqual(issues('some \a data'), [(1, 'BEL')])
        self.assertEqual(issues(b'x\x00'), [(1, 'CONTROL_CHAR')])

    def test_missing_math_delimiters(self):
        self.assertEqual(issues('Paragraph.\n\n$$\n' + r'\rho_0 \approx 1' + '\n'), [(3, 'MATH_UNCLOSED')])
        self.assertEqual(issues(r'Value $\alpha.'), [(1, 'MATH_UNCLOSED')])
        self.assertEqual(issues('Budget: $20.'), [])

    def test_math_in_list(self):
        doc = '- Example\n\n  $$\n  ' + r'\rho_0 \approx 0.16' + '\n  $$\n\n- Next item.\n'
        self.assertEqual(issues(doc), [])

    def test_math_braces_and_nested_dollar(self):
        self.assertEqual(issues(r'$$a_$C_{\text{sym}}$ = 2$$'), [(1, 'MATH_NESTED_DOLLAR')])
        self.assertEqual(issues(r'$\frac{a}{b$'), [(1, 'MATH_BRACE')])
        self.assertEqual(issues('$\\frac{a}{\n b}$'), [])
        self.assertEqual(issues(r'$t_m_{\max}$'), [(1, 'TEX_DOUBLE_SUBSCRIPT')])
        self.assertEqual(issues('$' + '\text{lost slash}' + '$'), [(1, 'TEX_TAB_ESCAPE')])

    def test_plain_code_excluded(self):
        code = r'`bad $ \a`' + '\n\n```tex\n' + r'\a $$' + '\n```\n<!-- $$ \\a -->\n'
        self.assertEqual(issues(code), [])
        self.assertEqual(issues('~~~math\n' + r'\a' + '\n~~~'), [(2, 'TEX_FRAGMENT_A')])
        self.assertEqual(issues(r'$`\a`$'), [(1, 'TEX_FRAGMENT_A')])

    def test_table_header(self):
        self.assertEqual(issues('| a | b | c |\n| --- | --- |\n| a | b | c |\n'), [(2, 'TABLE_HEADER')])
        self.assertEqual(issues('| a | b |\n|----|---|\n| 1 |\n'), [(3, 'TABLE_ROW')])

    def test_table_math_code_and_alias_pipes(self):
        header = '| Label | Value |\n| --- | --- |\n'
        for cell in (r'$|x|$', '`x|y`', '[[page|name]]'):
            with self.subTest(cell=cell):
                self.assertEqual(issues(header + f'| A | {cell} |\n'), [(3, 'TABLE_ROW')])
        for cell in (r'$\lvert x\rvert$', r'$x\mid y$', r'`x\|y`', r'[[page\|name]]'):
            with self.subTest(cell=cell):
                self.assertEqual(issues(header + f'| A | {cell} |\n'), [])

    def test_tex_comments_verbatim_and_environment(self):
        tex = '\n'.join((r'\begin{verbatim}', r'\a $$', r'\end{verbatim}', r'% \a $$',
                          r'\begin{align}', r'\rho &\approx 1 \\', r'\end{align}'))
        self.assertEqual(issues(tex, 'system/paper.tex'), [])
        self.assertIn((5, 'MATH_UNCLOSED'), issues(tex.rsplit('\n', 1)[0], 'system/paper.tex'))
        self.assertEqual(issues(r'$\begin{pmatrix}x&b\\a&y\end{pmatrix}$'), [])

    @unittest.skipUnless(shutil.which('pandoc'), 'Pandoc unavailable')
    def test_render_reports_unrecognized_tex_at_source_line(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'paper.md').write_text('# Title\n\n' + r'Valid $\alpha$. Bad $\badtex$.' + '\n', encoding='utf-8')
            self.assertEqual([(i.line, i.code) for i in qa.check_render(root, ['paper.md'])], [(3, 'MATH_RENDER')])


class GitHookQA(unittest.TestCase):
    def setUp(self):
        self.directory = TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name).resolve()
        self.run_git('init', '-q')
        self.write('kept.md', 'stable\n')
        self.write('already.md', 'stable\n')
        self.write('.gitignore', 'tmp/\n')
        self.commit()
        self.payload = {'session_id': 'fixture', 'turn_id': 'turn1'}

    def run_git(self, *args):
        subprocess.run(['git', '-C', str(self.root), *args], check=True, capture_output=True)

    def commit(self):
        self.run_git('add', '--', 'kept.md', 'already.md', '.gitignore')
        self.run_git('-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid', 'commit', '-qm', 'fixture')

    def write(self, relative, text):
        file = self.root / relative
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(text, encoding='utf-8')

    def run_event(self, event, active=False):
        return hook.handle(self.root, {**self.payload, 'hook_event_name': event, 'stop_hook_active': active})

    def test_nothing_changed_ignores_existing_dirty_docs(self):
        self.write('already.md', '$$\n')
        self.assertEqual(self.run_event('UserPromptSubmit'), {})
        with patch.object(hook, 'scan', side_effect=AssertionError('no file should be linted')):
            self.assertEqual(self.run_event('Stop'), {})

    def test_two_retries_then_checklist(self):
        self.run_event('UserPromptSubmit')
        self.write('kept.md', '$$\n')
        self.assertEqual(self.run_event('Stop')['decision'], 'block')
        self.assertIn('pass 2/2', self.run_event('Stop', active=True)['reason'])
        self.assertIn('stopped automatic retries', self.run_event('Stop', active=True)['systemMessage'])
        self.assertNotIn('decision', self.run_event('Stop', active=True))
        saved = list((self.root / 'tmp' / 'documents-qa' / 'hooks').glob('*-issues.json'))
        self.assertEqual(len(saved), 1)
        self.assertEqual(json.loads(saved[0].read_text())['issues'][0]['path'], 'kept.md')

    def test_repair_passes_and_preexisting_dirty_preserved(self):
        self.write('already.md', '$$\n')
        self.run_event('UserPromptSubmit')
        self.write('kept.md', r'$r_0 \a1.07$')
        self.assertNotIn('already.md', self.run_event('Stop')['reason'])
        self.write('kept.md', r'$r_0 \approx 1.07$')
        self.assertEqual(self.run_event('Stop', active=True), {})
        self.assertEqual((self.root / 'already.md').read_text(), '$$\n')

    def test_detects_committed_during_turn_and_nonrepo_skips(self):
        self.run_event('UserPromptSubmit')
        self.write('kept.md', '$$\n')
        self.commit()
        self.write('raw/paper.md', '$$\n')
        res = self.run_event('Stop')['reason']
        self.assertIn('kept.md:1', res)
        self.assertNotIn('raw/paper.md', res)

    def test_scope(self):
        self.write('outputs/report.md', 'content')
        self.write('outputs/generated-report.md', '<!-- auto-generated -->\n$$\n')
        self.write('outputs/generated/run.md', '$$\n')
        self.write('.agents/skills/demo/SKILL.md', 'content')
        self.write('tmp/unchecked.md', '$$\n')
        result = qa.scan(self.root, qa.all_paths(self.root))
        self.assertIn('outputs/report.md', result['files'])
        self.assertIn('.agents/skills/demo/SKILL.md', result['files'])
        self.assertIn('outputs/generated-report.md', result['generated_skipped'])
        self.assertNotIn('outputs/generated/run.md', result['files'])
        self.assertNotIn('tmp/unchecked.md', result['files'])
        self.assertEqual(result['issues'], [])


if __name__ == '__main__':
    unittest.main()
