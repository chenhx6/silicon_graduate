"""Publication path boundaries, using isolated local repositories only."""
import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/git/git20260905.py'
spec = importlib.util.spec_from_file_location('manifest_helper', SCRIPT)
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)


class ManifestPaths(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.git('init', '-q')
        self.git('-c', 'user.name=Test', '-c', 'user.email=test@example.invalid',
                 'commit', '--allow-empty', '-qm', 'baseline')

    def tearDown(self):
        self.tmp.cleanup()

    def git(self, *args):
        return subprocess.check_output(['git', '-C', str(self.root), *args])

    def test_unicode_quotes_and_whitespace(self):
        names = ['knowledge/中文 "引号".md', 'knowledge/ trailing .md', 'knowledge/a\nb.md']
        for name in names:
            p = self.root / name
            p.parent.mkdir(exist_ok=True)
            p.write_text('x')
        self.assertEqual(helper.changed_paths(self.root), set(names))

    def test_literal_metacharacter_filename(self):
        name = 'knowledge/[abc]*.md'
        p = self.root / name
        p.parent.mkdir()
        p.write_text('x')
        helper.validate_stage_path(self.root, name)
        self.assertIn(name, helper.changed_paths(self.root))

    def test_reject_directory_dot_traversal_and_protected(self):
        (self.root / 'knowledge').mkdir()
        for name in ['.', 'knowledge', '../escape', 'knowledge/../PLAN.md',
                     '/absolute', 'raw/test.pdf', 'PLAN.md', '.git/config']:
            with self.subTest(name=name), self.assertRaises(ValueError):
                helper.validate_stage_path(self.root, name)

    def test_reject_symlink_to_protected_file(self):
        (self.root / 'PLAN.md').write_text('protected')
        (self.root / 'knowledge').mkdir()
        (self.root / 'knowledge/link.md').symlink_to('../PLAN.md')
        with self.assertRaises(ValueError):
            helper.validate_stage_path(self.root, 'knowledge/link.md')

    def test_rename_rejected_without_mutating_index(self):
        (self.root / 'before').write_text('x')
        self.git('add', '--', 'before')
        self.git('-c', 'user.name=Test', '-c', 'user.email=test@example.invalid',
                 'commit', '-qm', 'file')
        self.git('mv', 'before', 'after')
        before = self.git('diff', '--cached', '--raw')
        with self.assertRaises(ValueError):
            helper.changed_paths(self.root)
        self.assertEqual(before, self.git('diff', '--cached', '--raw'))

    def test_root_accepts_worktree_git_file(self):
        (self.root / 'nested').mkdir()
        self.assertEqual(helper.repository_root(self.root / 'nested'), self.root)
        other = self.root / 'worktree'
        other.mkdir()
        (other / '.git').write_text('gitdir: ../.git/worktrees/example\n')
        self.assertEqual(helper.repository_root(other), other)


if __name__ == '__main__':
    unittest.main()
