# Essential corrections for video — 2026-11-20

The production goal is video. Separate still-image polishing can wait. The current screenplays already specify the essential actions correctly; this pass carries the audit's corrections into individual video briefs and selects character/location inputs that do not embed the known storyboard defects.

The prepared handoff contains **309 required shot corrections**, **16 explicitly deferred still-polish findings**, and **475 shots awaiting generated-take review**. These are preparation priorities. Existing image findings remain 325 FAIL and 475 NEEDS_HUMAN_REVIEW until actual selected pixels change; no rendered take has been checked or approved.

## Use the corrected video briefs

From the repository root:

```sh
python tools/production_handoff.py --output-dir /tmp/maple-video-handoff
```

Open `video-prompts/Episode_01.md` in that output directory to start Episode 01. The other nine episode files follow the same naming pattern. Each contains 80 independent briefs with the exact visible cast, off-screen speakers, appearance/wardrobe from the series canon, camera, action, starting/ending states, continuity, dialogue and any mandatory correction. They include reference paths for the actors actually visible in that shot, the clean location, supporting roles where scripted, and editable overlay candidates.

Phone-only Maya, Nina and Ed remain completely unseen. Vendor, clerk, server and neighbor faces/full bodies remain off-screen, while source-scripted hands or forearms may perform receipt, service and sealed-box transfers.

`video-must-fix.tsv` is the essential correction queue. `video-preparation.tsv` covers all 800 shots. The richer `shot-production.jsonl` includes each brief, its QA evidence and source checksums. The normal CI artifact includes these outputs alongside the existing production handoff.

Upload the named character/location references using the chosen video service's supported reference controls. The existing JPGs are identity previews; owner-controlled original masters and supporting-design acceptance remain separate production prerequisites. No video provider, account capability or cost is assumed. The 15-second values are editorial story slots; supported native clip lengths must be checked before rendering.

Unapproved storyboard panels are marked **composition guidance only** and excluded from the prepared first-frame inputs. A video model can preserve the defects in a supplied starting frame. Use the source action and character/location references to establish the correct shot; if the chosen workflow requires a first frame, review that individual input before rendering. A four-panel sheet must never become one animated frame.

## Essential video checks

| Episode | Required corrections | Deferred still polish | Essential story facts to verify in takes |
|---|---:|---:|---|
| 01 | 26 | 1 | Correct BLUE salad/YELLOW soup lists, purchased quantities, $18.50/$20/$1.50, rear-right stove, six places, off-screen phone voices. |
| 02 | 27 | 11 | Individual prepared samples; adult grape quartering before serving Max; net weights; $16 budget, $15.50 purchase, $4.50 cash change versus $0.50 budget remainder. |
| 03 | 17 | 0 | One half-teaspoon of salt, one recipe, twelve pancakes in six pairs, adult stove zone, raw/cooked separation and stove OFF. |
| 04 | 17 | 4 | Safe fitting; both trial shoes returned before closing boxes; one purchased navy size-2 pair boxed and bagged; original green shoes worn home; Max stands on floor. |
| 05 | 43 | 0 | Map rotates as one graphic; fixed park geography; one basket/cooler; six sandwiches, plates and waters; eaten portions never replenish. |
| 06 | 52 | 0 | Six fixed seats and meals, six glasses, Nina's food-temperature check before Max eats, persistent consumed portions, $80 payment/$16.20 change/$10 tip/$6.20 retained. |
| 07 | 20 | 0 | One closed bag with Leo; active phone call; supervised crossing and handhold; correct bus lane and boarding order; six tickets used once. |
| 08 | 38 | 0 | Six fabric cubes, six separate tags, twelve socks; lavender pouch stays private; correct one-owner cube and final two-row storage map. |
| 09 | 42 | 0 | Three pots/saucers/seeds; three 100 mL pours; drain saucers while pots stay upright; adult lifts, outdoor soil/tools, handwashing, no instant growth. |
| 10 | 27 | 0 | Home 14 versus neighbor 18; order MHE-10-C; one phone/box/berry; seal and refrigeration continuity; six portions. |
| **Total** | **309** | **16** | All generated takes still require visual and continuity review. |

Start by validating the most consequential actions: Episode 02 SHOT_060 grape preparation, Episode 03 SHOT_028 salt and SHOT_049–055 cooking, Episode 06 SHOT_048 food-temperature check, Episode 07 SHOT_034–041 crossing, Episode 09 SHOT_057 saucer drainage, and Episode 10 SHOT_021/053–060 delivery evidence and sealed-box transfer. The full essential queue also covers duplicated/missing cast, prop ownership, impossible counts and broken action geography.

Readable story information—prices, receipts, route/map labels, addresses, order IDs, owner names and planting records—must be correct in the finished edit. Use the existing exact SVG overlays rather than spending still-generation attempts on invented lettering. Keep plot text distinct from decorative title polish.

## What can wait

The [explicit deferral list](qa/video-deferrals.tsv) covers watch wrist, basket carry side/handle shape, blanket fabric and shoe lace color. Canonical versions stay in the video instructions, but these observations do not require another still-image repair pass. The list binds each decision to the exact audited correction, so a different future defect cannot silently inherit a cosmetic deferral.

Fine earrings, textures, subtle pose differences and other pending likeness/anatomy concerns can be assessed on generated takes. A clear identity change, duplicate person, malformed limb, unsafe action or story contradiction in the actual video still requires rejection or correction. Still-image QA is preserved as evidence; written instructions alone cannot resolve it.

The stories, dialogue, timings and subtitle drafts are unchanged. This pass creates preparation files only. Video rendering, performed voices, service costs and creator acceptance remain unverified.

Validation: 123 local regression tests, both strict series checks, QA evidence validation, root-document checks, all ten sync checks and production-handoff export pass. The export contains ten 80-shot briefs and the 309-row mandatory queue. These checks validate the preparation, not future rendered footage.
