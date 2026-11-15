"""Root documentation link and historical status regression checks."""
from pathlib import Path
import tempfile
import unittest

from tools.check_root_docs import root_link_issues, MARKDOWN_LINK, ROOT


class RootDocsTests(unittest.TestCase):
    def test_real_root_docs_have_no_broken_links_or_stale_agent_guidance(self):
        self.assertEqual(root_link_issues(ROOT), [])

    def test_local_broken_link_is_reported(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)
            (path / "README.md").write_text("[bad](missing.txt)")
            self.assertTrue(any("missing.txt" in item for item in root_link_issues(path)))

    def test_external_urls_and_section_links_are_ignored(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)
            (path / "README.md").write_text("[external](https://example.com/file)\n[section](#intro)")
            issues = root_link_issues(path)
            self.assertFalse(any("external" in item or "intro" in item for item in issues))


if __name__ == "__main__":
    unittest.main()
