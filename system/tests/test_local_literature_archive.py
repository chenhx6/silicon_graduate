"""Offline library fixtures: identity, recovery boundaries and real PDF reading."""
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import local_literature_archive as library


class LibraryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "knowledge/sources").mkdir(parents=True)
        (self.root / "raw/papers").mkdir(parents=True)

    def pdf(self, name, text="A study of nuclear shapes\nAlice Author\nAbstract\nResults"):
        import pymupdf
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        with pymupdf.open() as doc:
            page = doc.new_page()
            page.insert_text((30, 50), text)
            doc.save(path)
        return path

    def source(self, slug, raw, **meta):
        import yaml
        data = dict(type="source", title_original="A study of nuclear shapes",
                    authors=["Alice Author"], year=2020, raw_file=raw,
                    reading_depth="skimmed")
        data.update(meta)
        p = self.root / "knowledge/sources" / (slug + ".md")
        p.write_text("---\n" + yaml.safe_dump(data) + "---\n## Covered scope\np.1\n")
        return p

    def test_publication_preprint_and_supplement_grouped_with_preference(self):
        pub = self.pdf("raw/papers/published.pdf")
        self.pdf("raw/papers/arxiv2001.12345.pdf", "Preprint title\nAlice\nAbstract")
        self.pdf("raw/papers/supplement.pdf", "Supplement\nAdditional data")
        self.source("paper", "raw/papers/published.pdf", doi="10.1234/test",
                    arxiv="2001.12345", journal="Journal",
                    raw_sha256=library.digest(pub))
        home = self.root / library.HOME
        home.mkdir(parents=True)
        (home / "overrides.json").write_text(json.dumps({"artifacts": {
            "raw/papers/supplement.pdf": {
                "role": "supplement", "parent_work_key": "doi:10.1234/test",
                "basis": "Fixture supplementary material explicitly identifies the main paper."}}}))
        library.inventory(self.root)
        result = library.find(self.root, doi="10.1234/test")
        self.assertEqual(result["status"], "found-usable")
        work = result["results"][0]
        self.assertEqual(len(work["artifacts"]), 3)
        self.assertEqual(work["preferred_artifact"], "raw/papers/published.pdf")
        self.assertEqual(len(work["sources"]), 1)
        self.assertEqual(work["sources"][0]["reading_depth"], "skimmed")

    def test_reference_doi_does_not_identify_unregistered_paper(self):
        self.pdf("raw/papers/unknown.pdf", "A different title\nBob Author\nAbstract\n"
                 "Text\nReferences\nDOI: 10.9999/cited")
        library.inventory(self.root)
        result = library.find(self.root, doi="10.9999/cited")
        self.assertEqual(result["status"], "candidate-needs-identification")
        self.assertIsNone(result["results"][0]["preferred_artifact"])
        self.assertNotIn("doi:10.9999/cited", result["results"][0]["identity_keys"])

    def test_same_title_different_authors_are_not_merged(self):
        for i, author in enumerate(["Alice", "Bob"]):
            self.pdf(f"raw/papers/{i}.pdf", f"Shared title\n{author}\nAbstract")
            self.source(str(i), f"raw/papers/{i}.pdf", authors=[author])
        library.inventory(self.root)
        self.assertEqual(library.stats(self.root)["works"], 2)

    def test_missing_path_needs_identification_and_does_not_become_fulltext(self):
        self.source("missing", "raw/papers/absent.pdf", doi="10.1234/absent")
        library.inventory(self.root)
        result = library.find(self.root, doi="10.1234/absent")
        self.assertEqual(result["status"], "metadata-only")
        self.assertIsNone(result["results"][0]["preferred_artifact"])

    def test_bad_pdf_yaml_and_private_symlinks_do_not_block_other_files(self):
        self.pdf("raw/papers/good.pdf")
        (self.root / "raw/papers/bad.pdf").write_text("not a PDF")
        (self.root / "knowledge/sources/bad.md").write_text(
            '---\ntype: source\ntitle: "\\gamma"\nraw_file: raw/papers/bad.pdf\n---\n')
        outside = self.root / "raw/personal"
        outside.mkdir()
        (outside / "secret.pdf").write_text("secret")
        (self.root / "raw/papers/leak.pdf").symlink_to(outside / "secret.pdf")
        data = library.inventory(self.root)
        paths = {a["path"] for w in data["works"] for a in w["artifacts"]}
        self.assertNotIn("raw/papers/leak.pdf", paths)
        self.assertTrue(data["warnings"])
        self.assertTrue(library.find(self.root, query="good")["results"])

    def test_incremental_stable_id_and_deleted_file_detection(self):
        p = self.pdf("raw/papers/original.pdf")
        first = library.inventory(self.root)
        second = library.inventory(self.root)
        self.assertEqual(first["works"][0]["id"], second["works"][0]["id"])
        self.assertEqual(second["refresh"]["files_reextracted"], 0)
        p.unlink()
        self.assertNotEqual(library.find(self.root, query="original")["status"],
                            "found-usable")

    def test_absent_index_and_lock_have_explicit_states(self):
        self.assertEqual(library.find(self.root, doi="10.1/x")["status"],
                         "index-incomplete")
        home = self.root / library.HOME
        home.mkdir(parents=True)
        (home / "write.lock").write_text("another writer")
        with self.assertRaisesRegex(RuntimeError, "locked"):
            library.inventory(self.root)

    def test_manifest_maps_multiple_artifacts_without_reading_upgrade(self):
        p = self.pdf("raw/papers/main.pdf")
        q = self.pdf("raw/papers/extra.pdf", "Supplement")
        manifest = self.root / "raw/papers/manifest.json"
        manifest.write_text(json.dumps({"files": [
            {"path": str(x.relative_to(self.root)), "sha256": library.digest(x),
             "role": role} for x, role in [(p, "main"), (q, "supplement")]]}))
        self.source("collection", "raw/papers/manifest.json", doi="10.12/collection")
        library.inventory(self.root)
        result = library.find(self.root, doi="10.12/collection")["results"][0]
        self.assertEqual(len(result["artifacts"]), 2)
        self.assertEqual(result["sources"][0]["reading_depth"], "skimmed")

    def test_same_bytes_different_paths_and_fulltext_search(self):
        p = self.pdf("raw/papers/one.pdf")
        q = self.root / "raw/papers/two.pdf"
        q.write_bytes(p.read_bytes())
        data = library.inventory(self.root)
        self.assertEqual(len(data["works"]), 1)
        self.assertEqual(len(data["works"][0]["artifacts"]), 2)
        library.index_text(self.root, "raw/papers/one.pdf")
        self.assertTrue(library.find(self.root, query="Results")["results"])
        self.assertEqual(p.read_bytes(), q.read_bytes())

    def test_changed_bytes_require_identity_recheck(self):
        p = self.pdf("raw/papers/a.pdf")
        self.source("a", "raw/papers/a.pdf", doi="10.1/a",
                    raw_sha256=library.digest(p))
        library.inventory(self.root)
        p.write_bytes(b"changed")
        self.assertNotEqual(library.find(self.root, doi="10.1/a")["status"],
                            "found-usable")

    def test_chinese_substring_and_identifier_query(self):
        self.pdf("raw/papers/a.pdf")
        self.source("a", "raw/papers/a.pdf", title_original="三轴形变与集体运动研究",
                    doi="10.1234/triaxial")
        library.inventory(self.root)
        self.assertTrue(library.find(self.root, query="三轴形变")["results"])
        self.assertEqual(library.find(self.root, query="10.1234/triaxial")["status"],
                         "found-usable")

    def test_erratum_retains_identifier_and_explicit_parent_relation(self):
        self.pdf("raw/papers/main.pdf")
        self.pdf("raw/papers/erratum.pdf", "Correction\nAlice\nAbstract")
        self.source("main", "raw/papers/main.pdf", doi="10.1234/main", journal="J")
        self.source("erratum", "raw/papers/erratum.pdf", doi="10.1234/correction",
                    source_type="journal-erratum")
        home = self.root / library.HOME
        home.mkdir(parents=True)
        (home / "overrides.json").write_text(json.dumps({"artifacts": {
            "raw/papers/erratum.pdf": {"role": "erratum",
                "parent_work_key": "doi:10.1234/main",
                "basis": "Fixture correction explicitly names the main paper."}}}))
        library.inventory(self.root)
        work = library.find(self.root, doi="10.1234/main")["results"][0]
        self.assertEqual(len(work["artifacts"]), 2)
        self.assertEqual(work["preferred_artifact"], "raw/papers/main.pdf")
        self.assertIn("doi:10.1234/correction", work["identity_keys"])
        self.assertTrue(any(s["doi"] == "10.1234/correction" for s in work["sources"]))
        self.assertEqual(library.find(self.root, doi="10.1234/correction")["results"][0]
                         ["preferred_artifact"], "raw/papers/erratum.pdf")

    def test_access_failure_page_is_not_fulltext_and_disappeared_copy_is_retained(self):
        path = self.root / "raw/papers/blocked.html"
        path.write_text("<html><title>403 Forbidden</title>Access denied</html>")
        self.source("blocked", "raw/papers/blocked.html", doi="10.1234/blocked")
        self.pdf("raw/papers/removed.pdf")
        library.inventory(self.root)
        self.assertEqual(library.find(self.root, doi="10.1234/blocked")["status"], "metadata-only")
        (self.root / "raw/papers/removed.pdf").unlink()
        library.inventory(self.root)
        self.assertGreater(library.stats(self.root)["missing_paths"], 0)

    def test_tampered_manifest_cannot_rebind_itself_via_standalone_scan(self):
        p = self.pdf("raw/papers/a.pdf")
        manifest = self.root / "raw/papers/manifest.json"
        manifest.write_text(json.dumps({"files": [{"path": "raw/papers/a.pdf",
            "source_page": "knowledge/sources/a.md", "sha256": library.digest(p)}]}))
        self.source("a", "raw/papers/manifest.json", doi="10.1234/a",
                    raw_sha256="0" * 64)
        library.inventory(self.root)
        self.assertNotEqual(library.find(self.root, doi="10.1234/a")["status"], "found-usable")

    def test_collection_does_not_merge_independent_papers(self):
        a = self.pdf("raw/papers/a.pdf", "Paper A\nAlice\nAbstract")
        b = self.pdf("raw/papers/b.pdf", "Paper B\nBob\nAbstract")
        manifest = self.root / "raw/papers/manifest.json"
        manifest.write_text(json.dumps({"files": [{"path": str(p.relative_to(self.root)),
            "sha256": library.digest(p)} for p in [a, b]]}))
        self.source("collection", "raw/papers/manifest.json")
        data = library.inventory(self.root)
        wa = next(w for w in data["works"] if any(x["path"].endswith("a.pdf") for x in w["artifacts"]))
        wb = next(w for w in data["works"] if any(x["path"].endswith("b.pdf") for x in w["artifacts"]))
        self.assertNotEqual(wa["id"], wb["id"])

    def test_split_groups_keep_unique_accessions(self):
        p = self.pdf("raw/papers/a.pdf")
        q = self.root / "raw/papers/b.pdf"
        q.write_bytes(p.read_bytes())
        library.inventory(self.root)
        p.unlink()
        self.pdf("raw/papers/a.pdf", "Different paper\nBob\nAbstract")
        data = library.inventory(self.root)
        ids = [w["id"] for w in data["works"]]
        self.assertEqual(len(set(ids)), len(ids))

    def test_journal_metadata_does_not_prove_local_edition(self):
        self.pdf("raw/papers/neutral.pdf")
        self.source("a", "raw/papers/neutral.pdf", journal="Journal",
                    doi="10.1234/a", arxiv="2001.12345")
        library.inventory(self.root)
        work = library.find(self.root, doi="10.1234/a")["results"][0]
        self.assertEqual(work["canonical_edition"], "published")
        self.assertEqual(work["actual_edition"], "unknown")

    def test_source_symlinks_do_not_import_metadata(self):
        private = self.root / "raw/personal"
        private.mkdir()
        secret = private / "private.md"
        secret.write_text("---\ntype: source\ntitle_original: TOPSECRET\n---\n")
        (self.root / "knowledge/sources/leak.md").symlink_to(secret)
        data = library.inventory(self.root)
        self.assertFalse(any("TOPSECRET" in w["search_text"] for w in data["works"]))


if __name__ == "__main__":
    unittest.main()
