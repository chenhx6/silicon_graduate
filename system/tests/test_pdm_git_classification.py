from __future__ import annotations

import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class PdmGitClassificationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory(prefix="pdm-git-classification-", dir=ROOT / "tmp")
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        subprocess.run(["git", "init", "--quiet", str(self.root)], check=True, capture_output=True)
        shutil.copyfile(ROOT / ".gitignore", self.root / ".gitignore")

    def assert_ignored(self, paths: list[str], expected: bool) -> None:
        result = subprocess.run(
            ["git", "-C", str(self.root), "check-ignore", "--no-index", "--stdin", "-z"],
            input="\0".join(paths).encode() + b"\0", capture_output=True, check=False,
        )
        self.assertIn(result.returncode, (0, 1), result.stderr.decode())
        ignored = {path.decode() for path in result.stdout.split(b"\0") if path}
        self.assertEqual(ignored, set(paths) if expected else set())

    def test_maintained_software_is_publishable(self) -> None:
        self.assert_ignored([
            "raw/code/PDM/GUI/pyproject.toml", "raw/code/PDM/GUI/LICENSE",
            "raw/code/PDM/GUI/MANIFEST.in", "raw/code/PDM/GUI/README.md",
            "raw/code/PDM/GUI/src/multipolepdm/pdm/statistics.py",
            "raw/code/PDM/GUI/src/multipolepdm/examples/example.json",
            "raw/code/PDM/GUI/src/multipolepdm/examples/README.md",
            "raw/code/PDM/GUI/tests/reference/angular_correlation.py",
            "raw/code/PDM/GUI/scripts/build_release.py",
            "raw/code/PDM/GUI/docs/response-reference.md",
            "raw/code/PDM/GUI/docs/p-ado-input.png",
            "raw/code/PDM/analysis/README.md",
            "raw/code/PDM/analysis/01_results_and_intervals.ipynb",
            "raw/code/PDM/analysis/scripts/run_benchmarks.py",
            "raw/code/PDM/analysis/research/grid_resolution/study.py",
            "raw/code/PDM/analysis/research/grid_resolution/README.md",
            "outputs/plans/20261120-pdm-three-mode-rewrite/delivery/0.1.1/git-publication.json",
        ], False)

    def test_results_originals_snapshots_and_caches_stay_local(self) -> None:
        self.assert_ignored([
            "raw/code/PDM/GUI/dist/multipolepdm-0.1.1.whl",
            "raw/code/PDM/GUI/src/multipolepdm.egg-info/PKG-INFO",
            "raw/code/PDM/GUI/src/multipolepdm/__pycache__/grid.pyc",
            "raw/code/PDM/GUI/.pytest_cache/README.md",
            "raw/code/PDM/GUI/.ruff_cache/CACHEDIR.TAG",
            "raw/code/PDM/GUI/src/multipolepdm/private.json",
            "raw/code/PDM/GUI/docs/private.png",
            "raw/code/PDM/analysis/research/grid_resolution/marginals.npz",
            "raw/code/PDM/analysis/research/grid_resolution/results.json",
            "raw/code/PDM/analysis/benchmarks/manifest.json",
            "raw/code/PDM/analysis/cases/source_evidence.json",
            "raw/code/PDM/archives/20261124-code-inputs/manifest.json",
            "raw/code/another-program/main.py", "raw/papers/original.pdf",
            "raw/writing/pado/20261029_review_v1/PDM/main.pdf",
            "raw/zotero/wiki-inbox.bib",
            "outputs/plans/20261120-pdm-three-mode-rewrite/delivery/0.1.1/pypi-upload.log",
        ], True)


if __name__ == "__main__":
    unittest.main()
