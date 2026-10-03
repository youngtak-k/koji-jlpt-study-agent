"""Regression tests for packaging boundaries, not a measure of teaching quality."""

from pathlib import Path
import tempfile
import subprocess
import unittest

from scripts.check_release import REQUIRED, index_matches_worktree, link_errors, manifest_errors, validate


class ReleaseBoundaryTests(unittest.TestCase):
    def test_forced_private_file_is_rejected(self):
        for extra in ["local/CURRENT.md", "local/sessions/one.md", "docs/PRODUCT_REQUIREMENTS.md", ".env"]:
            with self.subTest(extra=extra):
                self.assertTrue(manifest_errors(REQUIRED | {extra}))

    def test_incomplete_distribution_is_rejected(self):
        self.assertTrue(manifest_errors(REQUIRED - {"agent/COACH.md"}))

    def test_existing_private_target_is_not_a_public_link(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "local").mkdir()
            (root / "local/note.md").write_text("Private")
            self.assertTrue(link_errors(root, "README.md", "[note](local/note.md)", {"README.md"}))

    def test_traversal_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertTrue(link_errors(Path(directory), "README.md", "[escape](../private.md)", {"README.md"}))

    def test_locale_link_resolves_inside_package(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual([], link_errors(Path(directory), "readme/README.ko.md", "[Guide](../agent/COACH.md)", {"agent/COACH.md"}))

    def test_external_and_fragment_links_are_not_local_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual([], link_errors(Path(directory), "README.md", "[Web](https://example.com) [Part](#start)", {"README.md"}))

    def test_symlink_cannot_publish_an_external_file(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").symlink_to("/tmp/other.md")
            self.assertTrue(any("ordinary file" in e for e in validate(root, {"README.md"})))

    def test_manual_packet_cannot_drift_from_workspace_template(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "agent").mkdir()
            (root / "templates").mkdir()
            (root / "agent/COACH.md").write_text("```markdown\nschema_version: 1\n```")
            (root / "templates/CURRENT.md").write_text("schema_version: 2\n")
            self.assertIn("The portable packet and workspace template differ.", validate(root, set()))

    def test_staged_contents_cannot_differ_from_checked_working_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            path = root / "README.md"
            path.write_text("Content in the index\n")
            subprocess.run(["git", "add", "README.md"], cwd=root, check=True)
            self.assertTrue(index_matches_worktree(root))
            path.write_text("Different content in the working tree\n")
            self.assertFalse(index_matches_worktree(root))


if __name__ == "__main__":
    unittest.main()
