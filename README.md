# Maple House English — AI Story Building

**One complete planned story at a time.** An original 3D animated American-English family comedy with six recurring family characters: Dan, Maya, Nina, Leo, Ella and Max.

## Episode folders

| Folder | Status |
|---|---|
| [Episode_01](Episode_01/) | **Current production:** 20-minute story-only screenplay, 80 shot prompts, 12 selected storyboard images, dialogue subtitles and visual references |
| [Episode_02](Episode_02/) | **Story and visual preproduction draft:** fruit-shop/picnic screenplay, 80 prompts and matching subtitles, 20 four-panel storyboard PNGs illustrating all 80 concepts, 14 shared cast previews, five environment references and editable overlays; creator approval, motion first frames, voices and video pending |
| Episode_03–Episode_10 | Empty placeholders — create content one at a time; do not prefill with scripts or art |

Read [EPISODE_IDEAS.md](EPISODE_IDEAS.md) for the planned first ten stories. Episodes 01 and 02 have written story packages; Episodes 03–10 remain ideas.

**Important new format:** Every episode begins with an approximately **20-minute full animated story**: comedy, gentle drama and natural learning through entertaining conversation. **No separate English-practice slots, no documentary recap blocks, no forced repeat pauses or quiz overlays** are included in that story runtime. The creator will design and add optional practice content **after** the 20-minute story; uploads may then be 25, 30 or more minutes in total. This is not a requirement that the finished upload must be 20 minutes.

**Episode 01:** [Full script](Episode_01/STORY.md) · [Final storyboards](Episode_01/STORYBOARD_INDEX.md) · [All story video prompts](Episode_01/VIDEO_PROMPTS.md) · [Dialogue-only subtitles](Episode_01/SUBTITLES.srt) · [Character gallery](Episode_01/assets/characters/) · [Continuity](Episode_01/CONTINUITY.md) · [22-step/Task 5–6 readiness](Episode_01/PRODUCTION_READINESS.md) · [character-populated scene plan](Episode_01/SCENE_REFERENCE_PLAN.md)

**Episode 02 — Dad Bought the Sourest Fruit!:** [Storyboard gallery](Episode_02/STORYBOARD_GALLERY.md) · [HTML gallery](Episode_02/assets/storyboards/index.html) · [Full script](Episode_02/STORY.md) · [All story video prompts](Episode_02/VIDEO_PROMPTS.md) · [Dialogue-only subtitles](Episode_02/SUBTITLES.srt) · [Continuity](Episode_02/CONTINUITY.md) · [Shot/board index](Episode_02/STORYBOARD_INDEX.md) · [Cast gallery](Episode_02/assets/characters/) · [Environment references](Episode_02/assets/environments/) · [Production readiness](Episode_02/PRODUCTION_READINESS.md). Uses the same six original character references; Episode 01's vegetable boards are not counted as Episode 02 artwork.

## Scope and production status

- Episode 01 contains 48 retained original visual beats plus 32 additional story beats (80 × 15 seconds = 1,200 seconds). The 12 selected storyboard sheets illustrate the **48 retained beats only**; the new 32 shots need visuals before actual animation.
- Episode 02 has 20 new four-panel storyboard sheets illustrating all 80 planned shots, plus four newly generated clean fruit-shop/garden environment PNG drafts. Its 14 cast-preview JPGs and kitchen JPG are unchanged copies of Episode 01 references. See the [storyboard generation notes](Episode_02/assets/storyboards/GENERATION_NOTES.md) and [environment generation notes](Episode_02/assets/environments/GENERATION_NOTES.md) for provenance and known limits. These visual drafts need creator review; no individual motion first frame is approved.
- There are no other active script versions or board v1/v2/v3 files. Older material remains recoverable from **Git commit history** or the owner's original production ZIP; deleting it from current tree does not erase historical commits.
- Original full-resolution 3D character/environment PNG masters remain in the owner-controlled ZIP. Shared JPGs are viewing previews; the new Episode 02 environment PNGs are generated visual drafts, not recovered archive masters.
- **Task 5 actual video and audio generation is deferred.** No finished movie, recorded voices, or generated animation is claimed. Episode 01's selected studies and Episode 02's new illustrated drafts are distinct from creator-approved motion first frames.

## Quality check

Run `python Episode_01/check.py` and `python Episode_02/check.py`. Episode 01 checks its existing story/assets and the remaining empty folders; Episode 02 checks all 80 shot slots, exact screenplay/prompt/subtitle dialogue alignment, subtitle timing, local document links, storyboard coverage/image assets and editable SVGs. Run `python Episode_02/sync.py --check` to detect stale derived Episode 02 draft documents and `python -m unittest discover -s tests -v` for validation failure cases. GitHub Actions runs all four commands. File/source checks do not certify visual likeness, per-panel fruit inventory or creator approval.

## Clarification on environment images and project tasks

Episode 01's five environment pictures and Episode 02's five environment references intentionally show **locations without people**. Clean backgrounds stay separate from populated storyboard compositions and checked individual first frames. See the [Episode 01 briefs](Episode_01/SCENE_REFERENCE_PLAN.md) and [Episode 02 reference/review plan](Episode_02/SCENE_REFERENCE_PLAN.md). Do not overwrite clean backgrounds or treat a generated actor likeness as accepted without review. Exact list/receipt/title graphics live in each episode's `assets/overlays/`; do not recreate the obsolete `assets/props/` directory.

The [original 22-section guide mapping and Tasks 5/6 readiness](Episode_01/PRODUCTION_READINESS.md) use the **current 80-shot / 20-minute story-only** canon, not the obsolete 48-shot + 24 teaching recaps.
