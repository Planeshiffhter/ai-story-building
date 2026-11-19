"""Prepare essential video corrections from the audited source; never render media.

The audit remains the record of selected still pixels. Video preparation carries
required corrections forward without treating a written prompt as a repaired take.
"""
from __future__ import annotations

import csv
import hashlib
from pathlib import Path

from tools.check_audit_qa import audit_issues
from tools.episode_package import FAMILY


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def family_appearance(root: Path) -> dict[str, str]:
    presentation = {}
    for line in (root / "SERIES_CANON.md").read_text(encoding="utf-8").splitlines():
        cells = [cell.strip().replace("**", "") for cell in line.strip("|").split("|")]
        if len(cells) == 3 and cells[0].endswith(" Brooks"):
            actor = cells[0].split()[0].upper()
            if actor in FAMILY:
                presentation[actor] = cells[2]
    if set(presentation) != FAMILY:
        raise ValueError("series canon must define all six original family appearances")
    return presentation


def read_deferrals(path: Path, findings: dict) -> dict:
    result = {}
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        if reader.fieldnames != ["episode", "shot", "correction", "reason"]:
            raise ValueError("video deferrals need episode, shot, correction and reason columns")
        for row in reader:
            key = row["episode"], row["shot"]
            if key in result or key not in findings or findings[key]["status"] != "FAIL":
                raise ValueError(f"invalid, duplicate or stale video deferral: {key}")
            if row["correction"] != findings[key]["correction"]:
                raise ValueError(f"stale video deferral: QA correction changed for {key}")
            if (set(row) != {"episode", "shot", "correction", "reason"}
                    or not isinstance(row["reason"], str) or not row["reason"].strip()):
                raise ValueError(f"video deferral needs an explicit reason: {key}")
            result[key] = row["reason"]
    return result


def motion_prompt(record: dict, preparation: dict) -> str:
    """Use positive source actions and exact correction; keep observed defects out of prompts."""
    inputs = preparation["reference_inputs"]
    visible = ", ".join(record["visible_cast"])
    phone = ", ".join(actor for actor in record["offscreen_cast"] if actor in FAMILY or actor == "ED") or "NONE"
    supporting = ", ".join(actor for actor in record["offscreen_cast"] if actor not in FAMILY and actor != "ED") or "NONE"
    lines = [
        f"{record['shot_id']}: {record['title']}",
        "Create one 16:9 animated story shot using the original family identities and W01 wardrobe; preserve any authored time ellipses.",
        f"Editorial slot: {record['editorial_start']}–{record['editorial_end']} (15 seconds). "
        "Confirm the chosen service's supported clip duration before rendering; preserve the complete action and dialogue in the edit.",
        f"Visible cast: {visible}. Show each named actor once; retain original faces, relative ages and heights. Only these actors may have visible faces or full bodies.",
        *[f"{actor} appearance: {description}" for actor, description in preparation["family_appearance"].items()],
        f"Unseen phone voices: {phone}. Keep these actors entirely off-screen, including insets, reflections and phone screens.",
        f"Off-screen supporting roles: {supporting}. Their faces and full bodies remain unseen. Hands/forearms may enter only when explicitly described by the source action.",
        f"Location: {record['location']}. Camera: {record['camera']}",
        f"Starting state: {record['opening_state']}",
        f"Action: {record['action']}",
        f"Ending state: {record['ending_state']}",
        f"Continuity: {record['continuity']}",
    ]
    if preparation["required_correction"]:
        lines.append(f"Mandatory correction for this video take: {preparation['required_correction']}")
    lines.extend([
        "Keep each owned object and food portion continuous through the shot; transfers happen visibly and consumed food does not reset.",
        "Use the episode's exact editable overlays for readable story text, prices, maps and labels during editing; verify their values in the finished video.",
        "Render this single shot without storyboard grids, printed shot badges, captions or unplanned title cards.",
        "Character reference inputs: " + (", ".join(inputs["visible_characters"] + inputs["supporting_cast"]) or "no visible actor reference"),
        f"Clean location reference: {inputs['environment']}",
        f"Episode continuity source: {preparation['continuity_source']}",
        "Storyboard usage: composition guidance only. Use character and location references to establish the shot; an unapproved panel is not a literal first-frame input.",
        "Exact dialogue, in order (observe the role visibility rules above):",
        *[f"{turn['speaker']}: {turn['text']}" for turn in record["dialogue"]],
        "Acceptance: check the generated take's cast, action, quantities, safety, readable plot text, and starting/ending state before keeping it.",
    ])
    return "\n".join(lines)


def attach_video_preparation(records: list[dict], root: Path) -> list[dict]:
    errors, _ = audit_issues(root)
    if errors:
        raise ValueError("video preparation requires current QA evidence: " + "; ".join(errors[:5]))
    findings = {}
    for number in range(1, 11):
        episode = f"{number:02}"
        path = root / "docs/qa" / f"Episode_{episode}.tsv"
        with path.open(encoding="utf-8", newline="") as stream:
            for row in csv.DictReader(stream, delimiter="\t"):
                findings[episode, row["shot"]] = row
    deferrals = read_deferrals(root / "docs/qa/video-deferrals.tsv", findings)
    appearance = family_appearance(root)
    hashes = {}
    for record in records:
        key = record["episode"], record["shot_id"]
        finding = findings[key]
        deferred = deferrals.get(key, "")
        required = finding["status"] == "FAIL" and not deferred
        episode_dir = f"Episode_{record['episode']}"
        qa_source = f"docs/qa/{episode_dir}.tsv"
        continuity_source = f"{episode_dir}/CONTINUITY.md"
        for path in (qa_source, continuity_source):
            if path not in hashes:
                hashes[path] = digest(root / path)
        actor_refs = [f"{episode_dir}/assets/characters/{actor}_sheet.jpg"
                      for actor in record["visible_cast"] if actor in FAMILY]
        for path in actor_refs:
            if not (root / path).is_file():
                raise ValueError(f"missing visible-cast reference: {path}")
        prep = {
            "priority": "must_fix_in_video" if required else (
                "defer_still_polish" if deferred else "review_generated_take"),
            "required_correction": finding["correction"] if required else "",
            "deferred_note": deferred,
            "board_input_policy": "composition_only",
            "use_board_as_first_frame": False,
            "visual_qa": {
                **{name: finding[name] for name in ("status", "observed", "correction", "evidence")},
                "source_tsv": qa_source, "source_tsv_sha256": hashes[qa_source],
            },
            "reference_inputs": {
                "visible_characters": actor_refs,
                "environment": record["references"]["environment"],
                "supporting_cast": record["references"]["supporting_cast_refs"],
            },
            "continuity_source": continuity_source,
            "continuity_sha256": hashes[continuity_source],
            "family_appearance": {actor: appearance[actor] for actor in record["visible_cast"] if actor in FAMILY},
        }
        prep["prompt"] = motion_prompt(record, prep)
        record["video_preparation"] = prep
    return records


def export_video_preparation(records: list[dict], output_dir: Path) -> None:
    rows = []
    for record in records:
        prep = record["video_preparation"]
        rows.append({
            "episode": record["episode"], "shot": record["shot_id"],
            "priority": prep["priority"], "required_correction": prep["required_correction"],
            "deferred_note": prep["deferred_note"],
            "qa_status": prep["visual_qa"]["status"],
            "board_input_policy": prep["board_input_policy"],
            "use_board_as_first_frame": "false",
            "qa_source": prep["visual_qa"]["source_tsv"],
        })
    for filename, selected in (
        ("video-preparation.tsv", rows),
        ("video-must-fix.tsv", [row for row in rows if row["priority"] == "must_fix_in_video"]),
    ):
        with (output_dir / filename).open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0]), delimiter="\t")
            writer.writeheader()
            writer.writerows(selected)
    prompt_dir = output_dir / "video-prompts"
    prompt_dir.mkdir(exist_ok=True)
    for number in range(1, 11):
        episode = f"{number:02}"
        selected = [r for r in records if r["episode"] == episode]
        lines = [
            f"# Episode {episode} — video preparation", "",
            "Corrected instructions for generation and take review. No rendered media or creator approval is claimed.",
            "Use visible-character references and the clean location. All storyboard panels remain composition guidance only.",
            "Readable plot text must use the exact episode overlays in editing. Cosmetic still repairs can wait.", "",
        ]
        for record in selected:
            prep = record["video_preparation"]
            lines.extend([
                f"## {record['shot_id']} · {record['title']}", "",
                f"Priority: `{prep['priority']}`. Image QA remains `{prep['visual_qa']['status']}`.", "",
                "```text", prep["prompt"], "```", "",
                "Overlay candidates: " + ", ".join(record["references"]["overlay_candidates"]), "",
            ])
            if prep["deferred_note"]:
                lines.extend(["Deferred still polish: " + prep["deferred_note"], ""])
        (prompt_dir / f"Episode_{episode}.md").write_text("\n".join(lines), encoding="utf-8")
