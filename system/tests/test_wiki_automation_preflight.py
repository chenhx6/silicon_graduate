from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "system" / "scripts" / "wiki_automation_preflight.py"


class WikiAutomationPreflightTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="wiki-preflight-", dir=ROOT / "tmp"))
        (self.tmp / ".git").mkdir()
        (self.tmp / ".codex").mkdir()
        (self.tmp / ".codex" / "config.toml").write_text(
            '# Docker supplies sandboxing\n', encoding="utf-8"
        )
        bib = self.tmp / "raw" / "zotero"
        bib.mkdir(parents=True)
        self.bib = bib / "wiki-inbox.bib"
        self.bib.write_text("@article{probe}\n", encoding="utf-8")

    def tearDown(self) -> None:
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def invoke(self, *extra: str):
        env = os.environ.copy()
        env.pop("CODEX_PERMISSION_PROFILE", None)
        p = subprocess.run([sys.executable, str(SCRIPT), "--root", str(self.tmp), *extra],
                           text=True, capture_output=True, env=env, check=False)
        return p, json.loads(p.stdout)

    def test_success_and_probes_are_cleaned(self) -> None:
        p, payload = self.invoke()
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertTrue(payload["ok"])
        self.assertIsNone(payload["config_default"])
        self.assertTrue(all(x["deleted"] for x in payload["write_probes"]))
        self.assertFalse(list(self.tmp.glob(".codex-write-probe-*.tmp")))
        self.assertFalse(list((self.tmp / ".git").glob(".codex-write-probe-*.tmp")))

    def test_baseline_mismatch_fails(self) -> None:
        p, payload = self.invoke("--baseline-bib-hash", "0" * 64)
        self.assertEqual(p.returncode, 1)
        self.assertFalse(payload["ok"])
        self.assertEqual(payload["protected_bib"]["status"], "mismatch")

    def test_missing_bib_is_allowed_for_public_clone(self) -> None:
        self.bib.unlink()
        p, payload = self.invoke()
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertEqual(payload["protected_bib"]["status"], "absent")


if __name__ == "__main__":
    unittest.main()
