"""A still-polish deferral must never silently hide an unrelated video defect."""
from pathlib import Path
import tempfile
import unittest

from tools.video_constraints import family_appearance, read_deferrals


class VideoDeferralTests(unittest.TestCase):
    def test_family_wardrobe_is_read_from_the_current_canon(self):
        root = Path(__file__).resolve().parents[1]
        appearance = family_appearance(root)
        self.assertEqual(set(appearance), {"DAN", "MAYA", "NINA", "LEO", "ELLA", "MAX"})
        self.assertIn("Plum blouse", appearance["MAYA"])
        self.assertIn("full-length", appearance["ELLA"])

    def read(self, text, findings):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "deferrals.tsv"
            path.write_text(text, encoding="utf-8")
            return read_deferrals(path, findings)

    def test_only_explicit_deferrals_for_existing_failures_are_accepted(self):
        findings = {("01", "SHOT_024"): {"status": "FAIL", "correction": "Left wrist."}}
        result = self.read("episode\tshot\tcorrection\treason\n01\tSHOT_024\tLeft wrist.\tWatch wrist is cosmetic.\n", findings)
        self.assertEqual(result, {("01", "SHOT_024"): "Watch wrist is cosmetic."})
        self.assertEqual(findings[("01", "SHOT_024")]["status"], "FAIL")

    def test_duplicate_unknown_and_repaired_deferrals_are_rejected(self):
        text = "episode\tshot\tcorrection\treason\n01\tSHOT_024\tLeft wrist.\tCosmetic.\n"
        for findings, value in (
            ({}, text),
            ({("01", "SHOT_024"): {"status": "NEEDS_HUMAN_REVIEW"}}, text),
            ({("01", "SHOT_024"): {"status": "FAIL", "correction": "Left wrist."}},
             text + "01\tSHOT_024\tLeft wrist.\tAgain.\n"),
        ):
            with self.subTest(findings=findings, value=value):
                with self.assertRaisesRegex(ValueError, "invalid, duplicate or stale"):
                    self.read(value, findings)

    def test_blank_reason_and_wrong_columns_are_rejected(self):
        findings = {("01", "SHOT_024"): {"status": "FAIL", "correction": "Left wrist."}}
        with self.assertRaisesRegex(ValueError, "explicit reason"):
            self.read("episode\tshot\tcorrection\treason\n01\tSHOT_024\tLeft wrist.\t\n", findings)
        with self.assertRaisesRegex(ValueError, "columns"):
            self.read("episode\tshot\n01\tSHOT_024\n", findings)

    def test_a_new_defect_cannot_inherit_an_old_cosmetic_deferral(self):
        findings = {("01", "SHOT_024"): {"status": "FAIL", "correction": "Remove a duplicated child."}}
        with self.assertRaisesRegex(ValueError, "QA correction changed"):
            self.read("episode\tshot\tcorrection\treason\n01\tSHOT_024\tLeft wrist.\tCosmetic.\n", findings)

    def test_authored_supporting_hands_are_allowed_but_phone_actors_stay_unseen(self):
        from tools.production_handoff import build_records
        records = {(row["episode"], row["shot_id"]): row for row in build_records()}
        for key, actor in ((('01', 'SHOT_057'), 'VENDOR'),
                           (('06', 'SHOT_010'), 'SERVER'),
                           (('10', 'SHOT_056'), 'NEIGHBOR')):
            row = records[key]
            prompt = row["video_preparation"]["prompt"]
            self.assertIn(row["action"], prompt)
            self.assertIn(f"Off-screen supporting roles: {actor}.", prompt)
            self.assertIn("Hands/forearms may enter only when explicitly described", prompt)
            self.assertIn("Unseen phone voices: NONE.", prompt)
        for key, actor in ((('01', 'SHOT_045'), 'MAYA'), (('07', 'SHOT_029'), 'ED')):
            prompt = records[key]["video_preparation"]["prompt"]
            self.assertIn(f"Unseen phone voices: {actor}. Keep these actors entirely off-screen", prompt)


if __name__ == "__main__":
    unittest.main()
