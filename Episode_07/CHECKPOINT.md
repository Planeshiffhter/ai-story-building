# Episode 07 — saved checkpoint and resume work

The complete written package has **80 shots / 20:00** and **234 matching dialogue/SRT cues**, with matching prompts, 80 shot briefs, a 20-sheet index, Markdown/HTML galleries, continuity, scene plan and the same 22-section production handoff used by Episodes02/03.

Actual assets saved: **10/20 four-panel storyboard PNGs** (BOARD_01–10, SHOT_001–040), **5/5 clean environment views** (unchanged home JPG +4 newly generated PNGs), **14/14 byte-identical original cast JPGs**, **6 editable overlays** and **1 bus seating SVG**. Source paths and image inspections are in [SHEET_REVIEW.md](assets/storyboards/SHEET_REVIEW.md) and the [environment notes](assets/environments/GENERATION_NOTES.md).

The visual package is **incomplete**. BOARD_11–20 (SHOT_041–080) and localized corrections remain. Image generation returned `429 usage_limit_reached`, a daily1,440-minute quota window, about65,625seconds until reset when observed. Requests stopped after that confirmed external blocker. No replacement art or false completion was created.

Resume after image service access resets:

1. Correct BOARD_01's generated title banner; BOARD_02 SHOT_006 visible Dan receiving edge; BOARD_03 SHOT_009 full-length Ella overalls; BOARD_05's invented Route36 on leaflet; BOARD_08 phone/bag state; BOARD_09 walking direction/bag ownership; BOARD_10 starting crossing side and bag ownership. Inspect all detailed targets in the review record.
2. Generate real BOARD_11–20 from STORY.md, with actual cast references and CORRECT_STOP/BUS_INTERIOR/LIBRARY_FOYER designs as appropriate. Do not relabel earlier artwork. Preserve original output paths, inspect each image and record corrections honestly.
3. Update STORY.md Picture fields from illustration-pending to actual generated-draft status only when those images exist. Run `python Episode_07/sync.py`, then `python Episode_07/sync.py --check` and `python Episode_07/check.py`.
4. Full check must still reject the missing ten sheets until they exist; written-only passing does not certify artwork. Run repository regression checks before root's next GitHub push.

Grandpa Ed is Nina's father, unseen in SHOT_029–032 only. Fictional Route7 NORTHBOUND—LIBRARY, six prepaid one-way tickets/$9, safe supervised crossing and three-return/three-new-book ledger remain unchanged. No performed voices, animation, approved individual motion first frames or creator visual acceptance exist. Root manages checkpoint commits and pushes.

Verified at this checkpoint: `sync.py --check` passes; `check.py --written-only` passes234matchedcues. Existing-asset checks pass14PNGstructural/checksum validations,14cast+home byte-equality checks,7SVGnamespace/exact-text checks and249existinglocal links. The only missing local targets are BOARD_11.png through BOARD_20.png. Full `check.py` correctly fails because twenty ordered sheets are required. Visual correction targets remain manual and unresolved.
