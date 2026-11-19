import base64
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import github_learning as learning


COMMIT = "1" * 40
TREE = "2" * 40
REPO = "example/agent-toolkit"
SOURCE_PATH = "skills/review/SKILL.md"
CONTENTS = b"---\nname: review\n---\n"


def blob_entry(path=SOURCE_PATH, mode="100644"):
    header = f"blob {len(CONTENTS)}\0".encode()
    return {
        "path": path, "mode": mode, "type": "blob", "size": len(CONTENTS),
        "sha": hashlib.sha1(header + CONTENTS).hexdigest(),
    }


class GitHubLearningTests(unittest.TestCase):
    def test_review_snapshot_preserves_bytes_without_activating_a_skill(self):
        entry = blob_entry(mode="100755")
        response = {"sha": entry["sha"], "encoding": "base64", "content": base64.b64encode(CONTENTS).decode()}
        info = {"repository": REPO, "commit": COMMIT, "tree_truncated": False}
        with tempfile.TemporaryDirectory() as folder, patch.object(learning, "read_tree", return_value=(info, [entry])):
            with patch.object(learning, "get_json", return_value=response):
                result = learning.fetch(REPO, COMMIT, [SOURCE_PATH], Path(folder))
            manifest = Path(result["manifest"])
            recorded = json.loads(manifest.read_text())["files"][0]
            self.assertEqual(recorded["path"], SOURCE_PATH)
            self.assertEqual(recorded["sha256"], hashlib.sha256(CONTENTS).hexdigest())
            self.assertIn(COMMIT, recorded["url"])
            sample = manifest.parent / recorded["local_file"]
            self.assertEqual(sample.read_bytes(), CONTENTS)
            self.assertEqual(sample.suffix, ".blob")
            self.assertEqual(sample.stat().st_mode & 0o111, 0)

    def test_symlink_is_rejected_before_downloading_or_writing(self):
        info = {"tree_truncated": False}
        with tempfile.TemporaryDirectory() as folder, patch.object(learning, "read_tree", return_value=(info, [blob_entry(mode="120000")])):
            with patch.object(learning, "get_json") as request:
                with self.assertRaisesRegex(learning.GitHubError, "regular Git files"):
                    learning.fetch(REPO, COMMIT, [SOURCE_PATH], Path(folder))
                request.assert_not_called()
            self.assertEqual(list(Path(folder).iterdir()), [])

    def test_blob_hash_mismatch_leaves_no_sample(self):
        entry = blob_entry()
        response = {"sha": entry["sha"], "encoding": "base64", "content": base64.b64encode(b"X" * len(CONTENTS)).decode()}
        info = {"tree_truncated": False}
        with tempfile.TemporaryDirectory() as folder, patch.object(learning, "read_tree", return_value=(info, [entry])):
            with patch.object(learning, "get_json", return_value=response):
                with self.assertRaisesRegex(learning.GitHubError, "hash mismatch"):
                    learning.fetch(REPO, COMMIT, [SOURCE_PATH], Path(folder))
            self.assertEqual(list(Path(folder).iterdir()), [])

    def test_pinned_ref_must_match_the_returned_commit(self):
        repo = {"full_name": REPO, "default_branch": "main"}
        commit = {"sha": "3" * 40, "commit": {"tree": {"sha": TREE}}}
        with patch.object(learning, "get_json", side_effect=[repo, commit]) as request:
            with self.assertRaisesRegex(learning.GitHubError, "different commit"):
                learning.read_tree(REPO, COMMIT)
            self.assertEqual(request.call_count, 2)
