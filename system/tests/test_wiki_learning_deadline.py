#!/usr/bin/env python3
"""Unit tests for wiki_learning_deadline pure resolver."""

from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from datetime import datetime, timedelta
from pathlib import Path

from system.scripts import wiki_learning_deadline as wld


def install_override(run_dir: Path, receipt: dict, *, hour: int = 17) -> dict:
    """Create an explicit hash-bound fixture, never a real run sidecar."""
    snapshot = run_dir / "before-user-extension.json"
    snapshot.write_text(json.dumps(receipt))
    original = wld.aware_datetime(receipt["overnight_until"])
    effective = original.replace(hour=hour)
    sidecar = {
        "schema_version": 1, "run_id": receipt["run_id"], "session_id": receipt["session_id"],
        "recorded_at": (original - timedelta(hours=1)).isoformat(),
        "authorization_kind": "explicit-current-user-instruction", "user_instruction": "Extend this run to 17:00.",
        "original_research_deadline": original.isoformat(),
        "effective_research_deadline": effective.isoformat(),
        "effective_closeout_window_ends_at": (effective + timedelta(hours=1)).isoformat(),
        "original_receipt_snapshot": snapshot.name,
        "original_receipt_snapshot_sha256": hashlib.sha256(snapshot.read_bytes()).hexdigest(),
    }
    path = run_dir / "user-override.json"
    path.write_text(json.dumps(sidecar))
    receipt.update(
        original_overnight_until=original.isoformat(), effective_overnight_until=effective.isoformat(),
        effective_closeout_window_ends_at=(effective + timedelta(hours=1)).isoformat(),
        deadline_override_receipt=path.name, deadline_override_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
    )
    return sidecar


class WikiLearningDeadlineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory(prefix="wld-test-")
        self.addCleanup(self.temp_dir.cleanup)
        self.root = Path(self.temp_dir.name)
        self.daily_root = self.root / "outputs" / "learning-daily"
        self.run_dir = self.daily_root / "20261025-DAY23-test-run-01"
        self.run_dir.mkdir(parents=True)
        self.receipt_path = self.run_dir / "run.json"
        self.run_date = "2026-10-25"
        self.default_deadline = wld.planned_closeout_for_run_date(self.run_date)
        self.receipt = {
            "run_id": "2026-10-25-day-23-01",
            "run_date": self.run_date,
            "day_index": 23,
            "session_id": "01a172fd-cbfb-7a13-b715-cfa0c479e08e",
            "overnight_until": self.default_deadline.isoformat(),
            "closeout_window_ends_at": (self.default_deadline + timedelta(hours=1)).isoformat(),
            "status": "running",
            "session_mode": "new-session-per-run",
            "project_root": str(self.root), "schedule_id": "wiki-daily-learning",
            "report": str(self.daily_root / "20261025-DAY23-test.md"),
        }
        self.write_receipt()

    def write_receipt(self) -> None:
        self.receipt_path.write_text(json.dumps(self.receipt, ensure_ascii=False, indent=2), encoding="utf-8")

    def test_default_deadline_without_override(self) -> None:
        info = wld.resolve_deadline_info(self.receipt_path, self.receipt, self.root)
        self.assertFalse(info["is_override"])
        self.assertEqual(info["original_deadline"], self.default_deadline)
        self.assertEqual(info["effective_deadline"], self.default_deadline)
        self.assertEqual(info["effective_closeout_end"], self.default_deadline + timedelta(hours=1))

    def test_rejects_unauthorized_deadline_mismatch_without_override(self) -> None:
        self.receipt["overnight_until"] = "2026-10-26T17:00:00+08:00"
        self.write_receipt()
        with self.assertRaisesRegex(RuntimeError, "without explicit override"):
            wld.resolve_deadline_info(self.receipt_path, self.receipt, self.root)

    def test_explicit_override_with_valid_sidecar_and_snapshot(self) -> None:
        snapshot_data = dict(self.receipt)
        snap_file = self.run_dir / "run-before-extension.json"
        snap_file.write_text(json.dumps(snapshot_data), encoding="utf-8")
        snap_sha = hashlib.sha256(snap_file.read_bytes()).hexdigest()

        eff_deadline = datetime(2026, 10, 26, 17, 0, tzinfo=wld.TIMEZONE)
        eff_end = datetime(2026, 10, 26, 18, 0, tzinfo=wld.TIMEZONE)
        override_data = {
            "schema_version": 1,
            "run_id": self.receipt["run_id"],
            "session_id": self.receipt["session_id"],
            "original_research_deadline": self.default_deadline.isoformat(),
            "effective_research_deadline": eff_deadline.isoformat(),
            "effective_closeout_window_ends_at": eff_end.isoformat(),
            "original_receipt_snapshot": snap_file.name,
            "original_receipt_snapshot_sha256": snap_sha,
            "authorization_kind": "explicit-current-user-instruction",
            "user_instruction": "extend to 17:00",
            "recorded_at": "2026-10-26T14:00:00+08:00",
        }
        override_file = self.run_dir / "user-override.json"
        override_file.write_text(json.dumps(override_data), encoding="utf-8")
        ov_sha = hashlib.sha256(override_file.read_bytes()).hexdigest()

        self.receipt.update({
            "original_overnight_until": self.default_deadline.isoformat(),
            "effective_overnight_until": eff_deadline.isoformat(),
            "effective_closeout_window_ends_at": eff_end.isoformat(),
            "deadline_override_receipt": override_file.name,
            "deadline_override_sha256": ov_sha,
        })
        self.write_receipt()

        info = wld.resolve_deadline_info(self.receipt_path, self.receipt, self.root)
        self.assertTrue(info["is_override"])
        self.assertEqual(info["original_deadline"], self.default_deadline)
        self.assertEqual(info["effective_deadline"], eff_deadline)
        self.assertEqual(info["effective_closeout_end"], eff_end)
        self.assertEqual(info["authorization"], "extend to 17:00")

    def test_override_rejects_tampered_sha(self) -> None:
        override_data = {
            "schema_version": 1,
            "run_id": self.receipt["run_id"],
            "session_id": self.receipt["session_id"],
            "original_research_deadline": self.default_deadline.isoformat(),
            "effective_research_deadline": "2026-10-26T17:00:00+08:00",
            "effective_closeout_window_ends_at": "2026-10-26T18:00:00+08:00",
        }
        override_file = self.run_dir / "user-override.json"
        override_file.write_text(json.dumps(override_data), encoding="utf-8")

        self.receipt["deadline_override_receipt"] = override_file.name
        self.receipt["deadline_override_sha256"] = "0" * 64
        self.write_receipt()
        with self.assertRaisesRegex(RuntimeError, "sha256 mismatch"):
            wld.resolve_deadline_info(self.receipt_path, self.receipt, self.root)

    def test_standard_baseline_resolution(self) -> None:
        baseline = {
            "run_id": self.receipt["run_id"],
            "day_index": self.receipt["day_index"],
            "report_existed_before": False,
            "knowledge_sha256_before": {"knowledge/index.md": "0" * 64},
        }
        (self.run_dir / "baseline.json").write_text(json.dumps(baseline), encoding="utf-8")
        kb, meta = wld.resolve_baseline_knowledge(self.run_dir, self.receipt, self.root)
        self.assertEqual(meta["kind"], "standard-baseline")
        self.assertEqual(kb, {"knowledge/index.md": "0" * 64})

    def test_reconstructed_entry_witness_baseline_resolution(self) -> None:
        source_bl = {"head": "1" * 40, "observed_at": "2026-10-25T12:00:00Z", "status_porcelain": "?? unrelated.txt\n",
                     "knowledge_sha256": {"knowledge/index.md": "0" * 64}}
        src_file = self.run_dir / "baseline-001.json"
        src_file.write_text(json.dumps(source_bl), encoding="utf-8")
        src_sha = hashlib.sha256(src_file.read_bytes()).hexdigest()

        evidence = {
            "head": "1" * 40,
            "source_path": src_file.relative_to(self.root).as_posix(),
            "observed_at": source_bl["observed_at"],
            "source_sha256": src_sha,
            "baseline_knowledge_count": 1, "head_tree_knowledge_md_count": 1,
            "baseline_vs_head_blob_mismatches": [], "mismatch_EOL_followup": [],
            "head_tree_report_entries": [], "report_status_entries": [], "knowledge_status_entries": [],
            "all_717_head_content_matches_after_explained_EOL": True,
            "report_absence_witness": {
                "report_relative_path": Path(self.receipt["report"]).relative_to(self.root).as_posix(),
                "head_tree_absent": True,
                "captured_porcelain_has_exact_path": False,
                "captured_porcelain_untracked_ancestor_collapsing_report": [],
                "current_check_ignore_no_index_exit": 1, "head_gitignore_sha256": "2" * 64,
                "boundary": "Reconstructed HEAD/status witness; historical external excludes not directly observed.",
            },
        }
        ev_file = self.run_dir / "evidence.json"
        ev_file.write_text(json.dumps(evidence), encoding="utf-8")
        ev_sha = hashlib.sha256(ev_file.read_bytes()).hexdigest()

        rec_data = {
            "kind": "reconstructed-entry-witness",
            "run_id": self.receipt["run_id"],
            "day_index": self.receipt["day_index"],
            "session_id": self.receipt["session_id"],
            "run_date": self.run_date, "recorded_at": "2026-10-26T14:00:00+08:00",
            "source_baseline": src_file.name,
            "source_baseline_sha256": src_sha,
            "source_head": "1" * 40,
            "source_observed_at": "2026-10-25T12:00:00Z",
            "evidence_file": ev_file.name,
            "evidence_sha256": ev_sha,
        }
        rec_file = self.run_dir / "baseline-reconstruction.json"
        rec_file.write_text(json.dumps(rec_data), encoding="utf-8")
        rec_sha = hashlib.sha256(rec_file.read_bytes()).hexdigest()

        self.receipt["baseline_reconstruction_receipt"] = rec_file.name
        self.receipt["baseline_reconstruction_sha256"] = rec_sha
        self.write_receipt()

        kb, meta = wld.resolve_baseline_knowledge(self.run_dir, self.receipt, self.root)
        self.assertEqual(meta["kind"], "reconstructed-entry-witness")
        self.assertEqual(kb, {"knowledge/index.md": "0" * 64})

    def test_find_active_learning_receipt_detects_running_session_within_window(self) -> None:
        now = datetime(2026, 10, 26, 10, 0, tzinfo=wld.TIMEZONE)
        active = wld.find_active_learning_receipt(self.daily_root, self.root, now=now)
        self.assertIsNotNone(active)
        self.assertEqual(active["receipt"]["run_id"], self.receipt["run_id"])

    def test_find_active_learning_receipt_ignores_completed_or_closed_window(self) -> None:
        self.receipt["status"] = "completed"
        self.write_receipt()
        now = datetime(2026, 10, 26, 10, 0, tzinfo=wld.TIMEZONE)
        self.assertIsNone(wld.find_active_learning_receipt(self.daily_root, self.root, now=now))

    def test_override_rejects_missing_binding_authorization_and_snapshot(self) -> None:
        sidecar = install_override(self.run_dir, self.receipt)
        original = dict(self.receipt)
        for field in ("deadline_override_sha256", "effective_overnight_until", "original_overnight_until"):
            with self.subTest(field=field):
                self.receipt = dict(original)
                self.receipt.pop(field)
                with self.assertRaises((RuntimeError, ValueError)):
                    wld.resolve_deadline_info(self.receipt_path, self.receipt, self.root)
        self.receipt = dict(original)
        path = self.run_dir / self.receipt["deadline_override_receipt"]
        for key, value in (("authorization_kind", "inferred"), ("user_instruction", ""),
                           ("session_id", "wrong-thread"), ("original_receipt_snapshot", "../outside.json"),
                           ("original_receipt_snapshot_sha256", "0" * 64),
                           ("recorded_at", "2026-10-26T17:01:00+08:00"),
                           ("effective_research_deadline", "2026-10-27T17:00:00+08:00")):
            bad = {**sidecar, key: value}
            path.write_text(json.dumps(bad))
            self.receipt["deadline_override_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
            with self.subTest(key=key), self.assertRaises((RuntimeError, ValueError)):
                wld.resolve_deadline_info(self.receipt_path, self.receipt, self.root)

    def test_override_does_not_allow_rewriting_original_timing_or_snapshot_identity(self) -> None:
        install_override(self.run_dir, self.receipt)
        self.receipt["overnight_until"] = self.receipt["effective_overnight_until"]
        with self.assertRaisesRegex(RuntimeError, "preserve original"):
            wld.resolve_deadline_info(self.receipt_path, self.receipt, self.root)
        self.receipt["overnight_until"] = self.default_deadline.isoformat()
        snapshot = self.run_dir / "before-user-extension.json"
        original = json.loads(snapshot.read_text())
        for key, value in (("run_date", "2026-10-24"), ("day_index", 24), ("run_id", "other-run")):
            snapshot.write_text(json.dumps({**original, key: value}))
            sidecar_path = self.run_dir / "user-override.json"
            sidecar = json.loads(sidecar_path.read_text())
            sidecar["original_receipt_snapshot_sha256"] = hashlib.sha256(snapshot.read_bytes()).hexdigest()
            sidecar_path.write_text(json.dumps(sidecar))
            self.receipt["deadline_override_sha256"] = hashlib.sha256(sidecar_path.read_bytes()).hexdigest()
            with self.subTest(key=key), self.assertRaisesRegex(RuntimeError, "snapshot"):
                wld.resolve_deadline_info(self.receipt_path, self.receipt, self.root)

    def test_effective_fields_alone_do_not_authorize_extension_and_symlinks_rejected(self) -> None:
        self.receipt["effective_overnight_until"] = "2026-10-26T17:00:00+08:00"
        with self.assertRaisesRegex(RuntimeError, "explicit override"):
            wld.resolve_deadline_info(self.receipt_path, self.receipt, self.root)
        self.receipt.pop("effective_overnight_until")
        install_override(self.run_dir, self.receipt)
        p = self.run_dir / "user-override.json"
        target = self.run_dir / "other.json"
        p.rename(target)
        p.symlink_to(target)
        with self.assertRaisesRegex(RuntimeError, "symlink"):
            wld.resolve_deadline_info(self.receipt_path, self.receipt, self.root)

    def test_override_accepts_equivalent_utc_and_keeps_next_trigger_at_1600(self) -> None:
        install_override(self.run_dir, self.receipt)
        self.receipt["effective_overnight_until"] = "2026-10-26T09:00:00Z"
        self.receipt["effective_closeout_window_ends_at"] = "2026-10-26T10:00:00Z"
        info = wld.resolve_deadline_info(self.receipt_path, self.receipt, self.root)
        self.assertEqual(info["effective_deadline"].hour, 17)
        self.assertEqual(wld.next_scheduled_start_for_run_date(self.run_date).hour, 16)
        self.assertEqual(self.receipt["overnight_until"], self.default_deadline.isoformat())

    def test_reconstruction_cannot_omit_or_tamper_evidence(self) -> None:
        self.test_reconstructed_entry_witness_baseline_resolution()
        rec_path = self.run_dir / self.receipt["baseline_reconstruction_receipt"]
        original = json.loads(rec_path.read_text())
        for key, value in (("evidence_file", None), ("evidence_sha256", None), ("source_baseline_sha256", "0" * 64),
                           ("source_head", "2" * 40), ("run_date", "2026-10-24"), ("session_id", "wrong")):
            rec_path.write_text(json.dumps({**original, key: value}))
            self.receipt["baseline_reconstruction_sha256"] = hashlib.sha256(rec_path.read_bytes()).hexdigest()
            with self.subTest(key=key), self.assertRaises((RuntimeError, ValueError)):
                wld.resolve_baseline_knowledge(self.run_dir, self.receipt, self.root)

    def test_reconstruction_rejects_report_or_unexplained_knowledge_changes(self) -> None:
        self.test_reconstructed_entry_witness_baseline_resolution()
        rec_path = self.run_dir / self.receipt["baseline_reconstruction_receipt"]
        rec = json.loads(rec_path.read_text())
        proof_path = self.run_dir / rec["evidence_file"]
        original = json.loads(proof_path.read_text())
        for change in ({"source_sha256": "3" * 64}, {"head_tree_report_entries": ["report.md"]},
                       {"all_717_head_content_matches_after_explained_EOL": False},
                       {"baseline_vs_head_blob_mismatches": [{"path": "knowledge/index.md"}]},
                       {"report_absence_witness": {**original["report_absence_witness"], "head_tree_absent": False}}):
            proof_path.write_text(json.dumps({**original, **change}))
            rec["evidence_sha256"] = hashlib.sha256(proof_path.read_bytes()).hexdigest()
            rec_path.write_text(json.dumps(rec))
            self.receipt["baseline_reconstruction_sha256"] = hashlib.sha256(rec_path.read_bytes()).hexdigest()
            with self.subTest(change=change), self.assertRaises((RuntimeError, ValueError)):
                wld.resolve_baseline_knowledge(self.run_dir, self.receipt, self.root)

    def test_reconstruction_rejects_future_recorded_at(self) -> None:
        self.test_reconstructed_entry_witness_baseline_resolution()
        at=datetime(2026,10,26,13,tzinfo=wld.TIMEZONE)
        with self.assertRaisesRegex(RuntimeError,"recorded_at cannot be in the future"):
            wld.resolve_baseline_knowledge(self.run_dir,self.receipt,self.root,now=at)

    def test_running_override_blocks_until_effective_hour_end_and_invalid_override_fails_closed(self) -> None:
        install_override(self.run_dir, self.receipt)
        self.receipt["status"] = "failed-verification"
        self.write_receipt()
        for hour in (16, 17):
            self.assertIsNotNone(wld.find_active_learning_receipt(self.daily_root, self.root, datetime(2026,10,26,hour,tzinfo=wld.TIMEZONE)))
        self.assertIsNone(wld.find_active_learning_receipt(self.daily_root, self.root, datetime(2026,10,26,18,tzinfo=wld.TIMEZONE)))
        self.receipt["deadline_override_sha256"] = "0" * 64
        self.write_receipt()
        with self.assertRaisesRegex(RuntimeError, "sha256 mismatch"):
            wld.find_active_learning_receipt(self.daily_root, self.root, datetime(2026,10,26,16,tzinfo=wld.TIMEZONE))

    def test_old_incomplete_receipts_do_not_hide_current_run_or_block_new_schedule_forever(self) -> None:
        old_dir=self.daily_root/'20260923-legacy-run-01'
        old_dir.mkdir()
        old={**self.receipt,"run_date":"2026-09-23","run_id":"legacy","overnight_until":None,"session_id":None}
        (old_dir/'run.json').write_text(json.dumps(old))
        now=datetime(2026,10,26,14,tzinfo=wld.TIMEZONE)
        self.assertEqual(wld.find_active_learning_receipt(self.daily_root,self.root,now)["receipt"]["run_id"],self.receipt["run_id"])
        self.receipt['status']='completed'
        self.write_receipt()
        self.assertIsNone(wld.find_active_learning_receipt(self.daily_root,self.root,now))

    def test_completed_manual_closeout_sidecar_ignores_stale_identityless_receipt(self) -> None:
        self.receipt["session_id"] = None
        self.write_receipt()
        (self.run_dir / "final-session-receipt-23.json").write_text(
            json.dumps(
                {
                    "run_id": self.receipt["run_id"],
                    "day_index": self.receipt["day_index"],
                    "status": "completed-content-final-not-pushed",
                    "closed_at": "2026-10-26T15:47:00+08:00",
                }
            ),
            encoding="utf-8",
        )
        now = datetime(2026, 10, 26, 16, 0, tzinfo=wld.TIMEZONE)
        self.assertIsNone(wld.find_active_learning_receipt(self.daily_root, self.root, now))


if __name__ == "__main__":
    unittest.main()
