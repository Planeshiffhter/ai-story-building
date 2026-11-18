# Maple House English · Episodes 01–10 production audit

The audit starts at fork commit `09063a73430ed9dbe0a7a5cf46074cb4e3fb16c2`. The ten episode directories contain 800 authored 15-second shots and 200 selected storyboard PNGs. Use the episode's STORY.md and CONTINUITY.md as the joint editorial source. Each episode also has a generated shot index, video prompts, provisional subtitles, reference art and exact overlays. The original full-resolution family masters remain with the owner.

## Cleanup decisions and recovery

[Baseline file ledger](qa/baseline-files.tsv) · [Archive member SHA-256 checksums](qa/archive.sha256)

The ledger covers all 960 tracked paths at the starting revision. Each row gives a decision, use, byte count, SHA-256, Git blob, file read check and matching paths where applicable. Images were decoded. All 960 paths were regular tracked files. No application secrets or external services are required for these checks. ARCHIVE means retain the existing historical location. REVIEW means the raw image's selection history is uncertain. No directories were moved.

| Baseline area | Finding | Action |
|---|---|---|
| `production_work/generated_images/` | 169 paths. 136 exactly match selected episode assets, seven match previous active versions, four have explicit design/correction histories, and 21 have no established selection history. One was empty. | Retain all 168 nonempty sources. Two documented initial garden designs were unselected. The other two are original designs before localized park and porch edits. |
| `MERGE_ARCHIVE/` | 66 paths. Sixteen match current active files byte for byte. The ledger lists known historical paths for recoverable variants. | Keep historical directory structure and its unique material intact. |
| `production_work/resume/` | 33 scripts, source maps and records from earlier generation sessions. | Keep for provenance. Use current episode tools for production. |
| `Episode_01…10/assets/characters/` | Each episode carries the 14 canonical JPGs. The series audit compares them to Episode 01. | Keep portable episode paths and links. Git already shares identical blobs. |

**Removed paths.** The ledger's eight DELETE rows give the exact paths. The seven zero-byte `.gitkeep` files in Episodes 04–10 held directories open before commissioning. Each directory now contains a full tracked package. Historical reviews mention these markers collectively. No active process requires them. The eighth was `production_work/generated_images/episode04_board09_correction_from_returned_image.png`, an empty failed save. No baseline text references its filename. Its real replacement is `Episode_04/assets/storyboards/BOARD_09.png`, with identical original bytes in `production_work/generated_images/exec-1cf2161c-c77b-46ce-80a8-1e204230a930.png`. All eight removals are low risk and recoverable with `git restore --source=09063a7 -- <path>`. The strict episode checks and file inventory verify the active packages after removal.

**External archive procedure.** Create the tar from the stated baseline to include its exact 268 historical members, including the empty attempt. Restore into an empty directory and run the checksum check there. Upload the tar and manifest to owner-controlled storage, record the destination and object version, and independently restore and verify both the path set and every member digest before considering relocation. The working fork retains the originals.

```sh
git archive -o /tmp/maple-recovery-09063a7.tar 09063a7 -- MERGE_ARCHIVE production_work/generated_images production_work/resume
restore_dir=$(mktemp -d)
tar -xf /tmp/maple-recovery-09063a7.tar -C "$restore_dir"
manifest="$PWD/docs/qa/archive.sha256"
(cd "$restore_dir" && sha256sum --check --quiet "$manifest")
```

## Review in progress

The cleanup ledger describes the starting revision. Current visual findings, repairs and verification will be recorded separately from the baseline data. Creator approval remains pending.
