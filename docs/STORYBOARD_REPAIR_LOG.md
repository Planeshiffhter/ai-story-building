# Storyboard image corrections — 2026-11-20

The active request is to fix the selected storyboard PNGs themselves. Video-prompt workarounds and still-polish deferrals have been removed. All recorded visual defects remain repair targets; no image is considered corrected solely because its instructions are correct.

## Selected corrections

| Episode / sheet | Verified image change | Recovery and evidence |
|---|---|---|
| 01 / BOARD_04 | SHOT_013 now shows Ella raising four fingers for the four carrots. All four panels and printed shot badges were rechecked. | [Selected sheet](../Episode_01/assets/storyboards/BOARD_04.png) · [Correction record](../artwork_qa/records/ep01-board04-counting-correction.json) |

Current QA inventory: **324 shots with major visual defects; 476 awaiting human review**. The counting repair removes one documented major discrepancy. Creator acceptance and individual motion-frame approval remain pending. Other storyboard defects have not been declared fixed.

Each selected edit preserves the prior image through its parent Git commit, retains the returned ImageGen source, updates all four panel evidence hashes and records what was visually confirmed. The Episode 01 printed-label audit is refreshed against the new pixels. Corrections are committed and pushed as checkpoints before requesting the next image.
