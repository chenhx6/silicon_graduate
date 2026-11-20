import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from system.scripts import literature_learning as learning


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.root = Path(folder.name)
        self.raw = self.root / "raw"
        self.raw.mkdir()
        self.pdf = self.raw / "archive.pdf"
        self.pdf.write_bytes(b"test original")
        self.path = "raw/archive.pdf"

    def test_hits_keep_pdf_pages_and_link_followup_to_the_prior_receipt(self):
        pages = [
            "The commissioning run used a calibration source.",
            "The σ/I curve assumes a fixed alignment of 0.3.\nThe transition has mixing ratio δ.",
            "",
            "The fit profiles alignment jointly with the mixing ratio.",
        ]
        with patch.object(learning, "pdf_pages", return_value=pages):
            first = learning.evidence(self.root, [self.path], "σ/I fixed alignment 0.3", 1)
            receipt = self.root / "round.json"
            receipt.write_text(json.dumps(first))
            second = learning.evidence(
                self.root, [], "jointly profiles alignment mixing ratio", 3,
                gap="Does the fit vary alignment independently of the reference curve?", prior=receipt,
            )
        self.assertEqual(first["corpus"][0]["pages_without_searchable_text"], [3])
        self.assertEqual(first["hits"][0]["pdf_page"], 2)
        self.assertIn("sigma", first["hits"][0]["matched_terms"])
        self.assertEqual(second["round"], 2)
        self.assertEqual(second["parent_receipt_sha256"], hashlib.sha256(receipt.read_bytes()).hexdigest())
        self.assertEqual(second["hits"][0]["pdf_page"], 4)
        self.assertFalse(second["hits"][0]["page_in_earlier_results"])
        self.assertTrue(next(hit for hit in second["hits"] if hit["pdf_page"] == 2)["page_in_earlier_results"])

    def test_followup_rejects_changed_original_even_when_a_cache_exists(self):
        with patch.object(learning, "pdf_pages", return_value=["mixing ratio"]):
            first = learning.evidence(self.root, [self.path], "ratio", 2)
        receipt = self.root / "round.json"
        receipt.write_text(json.dumps(first))
        self.pdf.write_bytes(b"different original at the same path")
        with patch.object(learning, "pdf_pages") as extract:
            with self.assertRaisesRegex(ValueError, "differs from the earlier receipt"):
                learning.evidence(self.root, [], "ratio", 2, gap="uncertainty", prior=receipt)
            extract.assert_not_called()

    def test_extraction_cache_preserves_empty_pages_and_reuses_content(self):
        cache = self.root / "tmp" / "cache"
        digest = learning.file_hash(self.pdf)
        result = subprocess.CompletedProcess(
            args=["pdftotext"], returncode=0, stdout=b"page one\n\f\fpage three\n\f", stderr=b"",
        )
        with patch.object(learning.subprocess, "run", return_value=result) as execute:
            first = learning.pdf_pages(self.pdf, digest, cache)
            second = learning.pdf_pages(self.pdf, digest, cache)
        execute.assert_called_once()
        self.assertEqual(first, ["page one\n", "", "page three\n"])
        self.assertEqual(first, second)

    def test_path_outside_raw_is_rejected_before_extraction(self):
        report = self.root / "notes.pdf"
        report.write_bytes(b"local report")
        with patch.object(learning, "pdf_pages") as extract:
            with self.assertRaisesRegex(ValueError, "under raw"):
                learning.evidence(self.root, [str(report)], "report", 3)
            extract.assert_not_called()

    def test_page_layout_keeps_coordinates_and_physical_page_identity(self):
        fixture = b"""<html xmlns="http://www.w3.org/1999/xhtml"><body><doc>
        <page width="612" height="792"><flow>
        <block xMin="72" yMin="80" xMax="200" yMax="92">
        <line><word>systematic</word><word>uncertainty</word></line>
        </block></flow></page></doc></body></html>"""
        with patch.object(learning, "extract_pdf", return_value=fixture) as extract:
            result = learning.pdf_layout(self.root, self.path, 12)
        extract.assert_called_once_with(self.pdf, ["-f", "12", "-l", "12", "-bbox-layout"])
        self.assertEqual(result["pdf_page"], 12)
        self.assertEqual(result["sha256"], learning.file_hash(self.pdf))
        self.assertEqual(result["blocks"], [{
            "bbox_pt": [72.0, 80.0, 200.0, 92.0], "lines": ["systematic uncertainty"],
        }])


class ScreeningTests(unittest.TestCase):
    def setUp(self):
        self.records = [
            {"doi": "seed-positive", "title": "Doppler shift attenuation lifetime spectroscopy", "label": "relevant"},
            {"doi": "seed-negative", "title": "Optical photometry atmosphere survey", "label": "irrelevant"},
            {"doi": "first", "title": "Optical photometry observations", "label": "irrelevant"},
            {"doi": "second", "title": "Doppler shift attenuation spectroscopy", "label": "relevant"},
            {"doi": "third", "title": "Optical photometry of stars", "label": "irrelevant"},
            {"doi": "fourth", "title": "Doppler lifetime from attenuation spectroscopy", "label": "relevant"},
        ]

    def test_get_paper_manifest_uses_explicit_labels_and_excludes_labeled_records(self):
        records = [{key: value for key, value in record.items() if key != "label"} for record in self.records]
        pool = learning.read_candidates(
            {"results": records}, {"seed-positive": "relevant", "seed-negative": "irrelevant"},
        )
        ranked = learning.screen(pool)["ranking"]
        self.assertEqual({item["screen_id"] for item in ranked[:2]}, {"second", "fourth"})
        self.assertEqual(len(ranked), 4)
        self.assertEqual(ranked[0]["record"], records[3])

    def test_single_class_cold_start_preserves_input_order(self):
        pool = learning.read_candidates(
            [{"id": "seen", "title": "positive paper", "label": "relevant"},
             {"id": "low", "title": "new study"}, {"id": "high", "title": "positive paper later"}], {},
        )
        ranked = learning.screen(pool)["ranking"]
        self.assertEqual([(hit["screen_id"], hit["screen_score"]) for hit in ranked], [("low", None), ("high", None)])

    def test_replay_withholds_each_label_until_selected(self):
        pool = learning.read_candidates(self.records, {})
        result = learning.replay(pool, ["seed-positive", "seed-negative"])
        self.assertEqual(result["held_out_relevant"], 2)
        self.assertEqual(result["baseline"][-1], {"reviewed": 4, "found": 2, "recall": 1.0})
        self.assertEqual(result["adaptive"][-1], {"reviewed": 2, "found": 2, "recall": 1.0})
        self.assertEqual(set(result["adaptive_order"]), {"first", "second", "third", "fourth"})

    def test_replay_rejects_an_unlabeled_pool(self):
        records = [*self.records, {"id": "unlabeled", "title": "An unseen record"}]
        with self.assertRaisesRegex(ValueError, "known labels"):
            learning.replay(learning.read_candidates(records, {}), ["seed-positive", "seed-negative"])
