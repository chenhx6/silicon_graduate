import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from system.scripts.wiki_archive_gate import changed_archive_scope, changed_paths, main, run_check, sha256
from system.scripts import wiki_hook


class ArchiveGateTests(unittest.TestCase):
    def make_repo(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        (root / "knowledge/sources").mkdir(parents=True)
        (root / "raw/figures/gpt/learning-daily/example").mkdir(parents=True)
        return root

    def make_manifest(self, root):
        artifact = root / "raw/figures/gpt/learning-daily/example/figure.png"
        artifact.write_bytes(b"figure")
        manifest = artifact.parent / "manifest.json"
        manifest.write_text(json.dumps({
            "retrieved_at": "2026-11-01T13:00:00+08:00",
            "files": [{
                "path": str(artifact.relative_to(root)),
                "sha256": sha256(artifact),
                "size": artifact.stat().st_size,
                "url": "https://example.org/figure.png",
            }],
        }), encoding="utf-8")
        return artifact, manifest

    def test_source_hash_and_manifest_pass(self):
        root = self.make_repo()
        _, manifest = self.make_manifest(root)
        source = root / "knowledge/sources/example.md"
        source.write_text(
            "---\nraw_file: \"raw/figures/gpt/learning-daily/example/manifest.json\"\n"
            f"raw_sha256: {sha256(manifest)}\n---\n",
            encoding="utf-8",
        )
        result = run_check(root, [str(source), str(manifest)], full=False)
        self.assertTrue(result["ok"], result)

    def test_missing_source_artifact_fails(self):
        root = self.make_repo()
        source = root / "knowledge/sources/example.md"
        source.write_text(
            "---\nraw_file: \"raw/papers/missing.pdf\"\n---\n",
            encoding="utf-8",
        )
        result = run_check(root, [str(source)], full=False)
        self.assertFalse(result["ok"])
        self.assertEqual(result["failures"][0]["kind"], "source-missing")

    def test_manifest_hash_mismatch_fails(self):
        root = self.make_repo()
        artifact, manifest = self.make_manifest(root)
        artifact.write_bytes(b"changed")
        result = run_check(root, [str(manifest)], full=False)
        self.assertFalse(result["ok"])
        self.assertIn("hash", {failure["kind"] for failure in result["failures"]})

    def test_url_only_source_fails(self):
        root = self.make_repo()
        source = root / "knowledge/sources/new.md"
        source.write_text("---\nsource_url: https://example.org/paper\n---\n", encoding="utf-8")
        result = run_check(root, [str(source)], full=False)
        self.assertFalse(result["ok"])
        self.assertEqual(result["failures"][0]["kind"], "source-unarchived")

    def test_single_file_requires_hash(self):
        root = self.make_repo()
        artifact, _ = self.make_manifest(root)
        source = root / "knowledge/sources/new.md"
        source.write_text(f'---\nraw_file: "{artifact.relative_to(root)}"\n---\n', encoding="utf-8")
        result = run_check(root, [str(source)], full=False)
        self.assertFalse(result["ok"])
        self.assertEqual(result["failures"][0]["kind"], "source-hash-missing")

    def test_typo_in_requested_source_is_not_silently_skipped(self):
        root = self.make_repo()
        result = run_check(root, ["knowledge/sources/typo.md"], full=False)
        self.assertFalse(result["ok"])
        self.assertEqual(result["failures"][0]["kind"], "requested-missing")

    def test_manifest_rejects_missing_provenance_empty_files_and_bad_hash(self):
        for mutation in ("provenance", "empty", "hash", "time", "duplicate"):
            with self.subTest(mutation=mutation):
                root = self.make_repo()
                _, manifest = self.make_manifest(root)
                payload = json.loads(manifest.read_text())
                if mutation == "provenance":
                    del payload["files"][0]["url"]
                elif mutation == "empty":
                    payload["files"] = []
                elif mutation == "hash":
                    payload["files"][0]["sha256"] = "not-a-hash"
                elif mutation == "time":
                    payload["retrieved_at"] = "2026-11-01T13:00:00"
                else:
                    payload["files"].append(payload["files"][0])
                manifest.write_text(json.dumps(payload))
                result = run_check(root, [str(manifest)], full=False)
                self.assertFalse(result["ok"])
                self.assertEqual(result["failures"][0]["kind"], "manifest")

    def test_manifest_rejects_repository_nonraw_artifacts(self):
        root = self.make_repo()
        _, manifest = self.make_manifest(root)
        artifact = root / "knowledge/copied.png"
        artifact.write_bytes(b"figure")
        payload = json.loads(manifest.read_text())
        payload["files"][0]["path"] = str(artifact.relative_to(root))
        manifest.write_text(json.dumps(payload))
        result = run_check(root, [str(manifest)], full=False)
        self.assertFalse(result["ok"])
        self.assertEqual(result["failures"][0]["kind"], "path")

    def test_source_rejects_outside_symlink(self):
        root = self.make_repo()
        outside_dir = tempfile.TemporaryDirectory()
        self.addCleanup(outside_dir.cleanup)
        outside = Path(outside_dir.name) / "private.pdf"
        outside.write_bytes(b"private")
        link = root / "raw/private.pdf"
        link.symlink_to(outside)
        source = root / "knowledge/sources/new.md"
        source.write_text("---\nraw_file: raw/private.pdf\n---\n", encoding="utf-8")
        result = run_check(root, [str(source)], full=False)
        self.assertFalse(result["ok"])
        self.assertEqual(result["failures"][0]["kind"], "source-path")

    def test_cli_interspersed_options_and_separator(self):
        root = self.make_repo()
        _, manifest = self.make_manifest(root)
        with patch("builtins.print"):
            self.assertEqual(main(["check", "--root", str(root), "--", str(manifest)]), 0)

    def test_changed_scope_handles_unicode_spaces_and_new_sources(self):
        root = self.make_repo()
        subprocess.run(["git", "init", "-q", str(root)], check=True, capture_output=True)
        path = root / "knowledge/sources/学位 论文.md"
        path.write_text("---\ntype: source\n---\n", encoding="utf-8")
        self.assertIn("knowledge/sources/学位 论文.md", changed_paths(root))
        script = Path(__file__).resolve().parents[1] / "scripts/wiki_archive_gate.py"
        result = subprocess.run(
            [sys.executable, str(script), "check", "--root", str(root), "--changed"],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("source-unarchived", result.stdout)

    def test_registered_manifest_rechecked_when_raw_is_git_ignored(self):
        root = self.make_repo()
        subprocess.run(["git", "init", "-q", str(root)], check=True, capture_output=True)
        (root / ".gitignore").write_text("raw/**\n")
        artifact, _ = self.make_manifest(root)
        artifact.unlink()
        script = Path(__file__).resolve().parents[1] / "scripts/wiki_archive_gate.py"
        result = subprocess.run(
            [sys.executable, str(script), "check", "--root", str(root), "--changed"],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("archived file is missing", result.stdout)

    def test_enrolled_source_checked_without_a_git_change(self):
        root = self.make_repo()
        artifact, _ = self.make_manifest(root)
        source = root / "knowledge/sources/enrolled.md"
        source.write_text(
            f"---\narchive_required: true\nraw_file: {artifact.relative_to(root)}\n"
            f"raw_sha256: {sha256(artifact)}\n---\n", encoding="utf-8",
        )
        artifact.write_bytes(b"replaced")
        with patch("system.scripts.wiki_archive_gate.changed_paths", return_value=[]):
            selected = changed_archive_scope(root)
        self.assertIn(str(source), selected)
        result = run_check(root, selected, full=False)
        self.assertIn("source-hash", {failure["kind"] for failure in result["failures"]})

    def test_library_and_historical_staging_paths_are_not_archive_files(self):
        root = self.make_repo()
        artifact, _ = self.make_manifest(root)
        source = root / "knowledge/sources/history.md"
        source.write_text(
            f"---\nraw_file: {artifact.relative_to(root)}\nraw_sha256: {sha256(artifact)}\n"
            'library_file: "E:/Zotero/paper.pdf"\n'
            "actual_body_file: tmp/old-download.pdf\n"
            "public_staging_file: tmp/public-download.pdf\n"
            "staging_file: tmp/transient-download.pdf\n---\n", encoding="utf-8",
        )
        self.assertTrue(run_check(root, [str(source)], full=False)["ok"])

    def test_companion_archive_is_required_and_hashed(self):
        root = self.make_repo()
        artifact, _ = self.make_manifest(root)
        source = root / "knowledge/sources/companion.md"
        source.write_text(
            f"---\nraw_file: {artifact.relative_to(root)}\nraw_sha256: {sha256(artifact)}\n"
            "supplement_file: raw/papers/missing-supplement.pdf\n"
            f"supplement_sha256: {'0' * 64}\n---\n", encoding="utf-8",
        )
        result = run_check(root, [str(source)], full=False)
        self.assertFalse(result["ok"])
        self.assertEqual(result["failures"][0]["kind"], "companion-archive")

    def test_companion_manifest_checks_its_registered_files(self):
        root = self.make_repo()
        artifact, manifest = self.make_manifest(root)
        source = root / "knowledge/sources/collection.md"
        source.write_text(
            f"---\nraw_file: {artifact.relative_to(root)}\nraw_sha256: {sha256(artifact)}\n"
            f"response_file: {manifest.relative_to(root)}\nresponse_sha256: {sha256(manifest)}\n---\n",
            encoding="utf-8",
        )
        artifact.unlink()
        replacement = root / "raw/anchor.txt"
        replacement.write_text("anchor", encoding="utf-8")
        source.write_text(
            f"---\nraw_file: {replacement.relative_to(root)}\nraw_sha256: {sha256(replacement)}\n"
            f"response_file: {manifest.relative_to(root)}\nresponse_sha256: {sha256(manifest)}\n---\n",
            encoding="utf-8",
        )
        result = run_check(root, [str(source)], full=False)
        self.assertFalse(result["ok"])
        self.assertIn("missing", {failure["kind"] for failure in result["failures"]})

    def test_legacy_download_receipt_is_reported_without_becoming_an_archive(self):
        root = self.make_repo()
        subprocess.run(["git", "init", "-q", str(root)], check=True, capture_output=True)
        (root / ".gitignore").write_text("raw/**\n")
        receipt = root / "raw/figures/gpt/learning-daily/example/manifest.json"
        receipt.write_text(json.dumps({"version": 1, "results": [{"status": "failed"}]}))
        script = Path(__file__).resolve().parents[1] / "scripts/wiki_archive_gate.py"
        result = subprocess.run(
            [sys.executable, str(script), "check", "--root", str(root), "--changed"],
            capture_output=True, text=True, check=False,
        )
        payload = json.loads(result.stdout)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertEqual(payload["checked_manifests"], [])
        self.assertEqual(payload["legacy_receipts_not_archive_validated"], [str(receipt)])
        self.assertFalse(run_check(root, [str(receipt)], full=False)["ok"])

    def test_after_edit_cannot_pass_with_failed_archive_gate(self):
        root = self.make_repo()
        successful_diff = subprocess.CompletedProcess([], 0, "", "")
        with patch.object(wiki_hook, "changed_paths", return_value=[]), \
                patch.object(wiki_hook, "archive_gate", return_value={"ok": False}), \
                patch.object(wiki_hook.subprocess, "run", return_value=successful_diff):
            self.assertFalse(wiki_hook.after_edit(root)["ok"])

    def test_session_summary_returns_failure_for_failed_archive_gate(self):
        root = self.make_repo()
        with patch.object(wiki_hook, "status_payload", return_value={"status_ok": True}), \
                patch.object(wiki_hook, "after_edit", return_value={"ok": False}), \
                patch("builtins.print"):
            result = wiki_hook.main(["session-summary", "--root", str(root)])
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
