#!/usr/bin/env python3
"""Write the Prop Room camera preset pack. Numbers are the source of truth."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

PACK = {
    "pack": "prop-room-cameras",
    "version": "1.0.0",
    "not": "Not a copy of any channel, character, set, title, or script. A camera grammar for original 9:16 diorama explainers: a flat illustrated character standing in a lit 3D room.",
    "format": {
        "width": 1080,
        "height": 1920,
        "fps": 30,
        "shot_seconds": [1.4, 2.6],
        "film_seconds": [55, 70],
        "sets_per_film": [3, 5],
        "unit": "meters in a full-size room. If the set is a miniature, multiply every distance by the same scale. Never mix scales.",
        "eye_line_m": 1.45,
        "hold_before_cut_frames": 8,
    },
    "why_these_numbers": [
        "A flat character card breaks past about 25 degrees of orbit: the ellipse of the head and the contact shadow give it away. Arcs stop at 22 degrees.",
        "A phone cut during acceleration reads as a glitch. Every move arrives, then holds 8 frames.",
        "Lens zoom flattens the room, so the small prop never feels like it is inside a big consequence. Dolly unless a preset says otherwise.",
        "Shake, 360 spins, and constant bouncing hide the prop. Violence is a camera that STOPS, not a camera that shakes.",
    ],
    "hard_rules": [
        "One primary preset per shot. A second behavior only if it is listed in that preset's compounds.",
        "If no preset fits, use quiet-push. Do not invent a move, an orbit, a zoom, or a shake.",
        "No animated roll. Dutch is not in this pack.",
        "No fade-in as a shot. Picture is already framed. A 4-frame dip from black is allowed only on shot 1.",
        "Captions never cover the prop the sentence is about.",
        "The 2D character is unshaded. Do not relight the card to sell the camera move. Light the room.",
        "Contact shadow stays under the feet for the whole move.",
        "Screen direction stays the same until a character actually turns around.",
        "New information earns a new shot. A new shot does not earn a new set.",
        "Land the camera 8 frames before the cut.",
    ],
    "lenses": [
        {"id": "geography", "mm": 24, "use": "The room is the sentence."},
        {"id": "room", "mm": 35, "use": "Default. Person plus the place."},
        {"id": "person", "mm": 50, "use": "A face or a pair of hands."},
        {"id": "secret", "mm": 85, "use": "The prop is the sentence. Background compresses."},
    ],
    "modifiers": [
        {
            "id": "impact-lock",
            "kind": "modifier",
            "apply_to": ["quiet-push", "hand-track", "parallax-slider", "boot-crane"],
            "behavior": "On the contact frame, camera velocity reaches 0 in 2 frames and stays 0 through the cut hold. Do not add shake, flash, or roll.",
            "why": "The hit reads because everything else stops.",
        }
    ],
    "presets": [],
}

PRESETS = [
    {
        "id": "prop-macro",
        "name": "Prop macro",
        "job": "Open on the object, or return to it when the mechanism is named.",
        "frames": 40,
        "arrive_by_frame": 32,
        "lens_mm": 85,
        "aperture": 2.8,
        "focus": "prop surface, a real detail (edge, notch, stamp), not the center of a blur",
        "start": {"distance_m": 0.28, "height_m": 1.05, "pitch_deg": -8, "yaw_deg": 0, "prop_frame_height": 0.46},
        "end": {"distance_m": 0.48, "height_m": 1.12, "pitch_deg": -6, "yaw_deg": 0, "prop_frame_height": 0.30},
        "path": "Slow dolly back 0.20m and rise 0.07m. No yaw. No roll. No lens zoom.",
        "easing": "cubic-out",
        "parallax": "The prop's near edge moves more than its far edge. If it scales like a sticker, you zoomed. Redo as a dolly.",
        "compounds": [],
        "cut_in_from": ["cold-open", "snap-inset", "answer-drift"],
        "cut_out_to": ["consequence-pull", "quiet-push", "table-arc-22"],
        "never_after": ["rival-whip"],
        "do_not": [
            "Do not put a title card in front of this shot.",
            "Do not orbit. At 85mm an arc turns into a smear.",
            "Do not let the prop touch the caption band.",
        ],
        "video_model_line": "85mm macro of one small object on a table, camera dollies back 20 centimeters and rises slightly over 1.3 seconds, cubic ease-out, no zoom, no orbit, shallow focus on a real surface detail, vertical 9:16.",
    },
    {
        "id": "quiet-push",
        "name": "Quiet push",
        "job": "Default listening shot while a fact is said. Use this when unsure.",
        "frames": 66,
        "arrive_by_frame": 58,
        "lens_mm": 35,
        "aperture": 5.6,
        "focus": "character card eyes, or the prop if the line is about the prop",
        "start": {"distance_m": 2.4, "height_m": 1.45, "pitch_deg": 0, "yaw_deg": 0, "subject": "waist-up, headroom 12% of frame"},
        "end": {"distance_m": 2.05, "height_m": 1.45, "pitch_deg": 0, "yaw_deg": 0, "subject": "chest-up"},
        "path": "Dolly in 0.35m on a straight line. Height locked. No pan.",
        "easing": "cubic-in-out",
        "parallax": "A foreground mug, post, or door edge must slide a little. If nothing nearer than the character exists, the push looks like a zoom. Add one foreground piece.",
        "compounds": ["impact-lock"],
        "cut_in_from": ["any"],
        "cut_out_to": ["any"],
        "never_after": [],
        "do_not": [
            "Do not push more than 0.35m. Bigger reads as comedy.",
            "Do not add handheld noise.",
            "Do not use this twice in a row with the same framing size. Change size or change preset.",
        ],
        "video_model_line": "35mm, eye height, slow straight dolly in of 35 centimeters over 2.2 seconds, cubic ease in and out, no pan, no zoom, no shake, a nearer object slides against the back wall, vertical 9:16.",
    },
    {
        "id": "consequence-pull",
        "name": "Consequence pull",
        "job": "Prove the small object sits inside a result big enough to matter.",
        "frames": 54,
        "arrive_by_frame": 46,
        "lens_mm": 24,
        "aperture": 5.6,
        "focus": "start on the prop, widen so the room is readable by the end. Do not blur the prop away.",
        "start": {"distance_m": 0.9, "height_m": 1.2, "pitch_deg": -4, "prop_on": "lower third"},
        "end": {"distance_m": 2.6, "height_m": 1.85, "pitch_deg": -8, "prop_on": "lower third, still fully visible"},
        "path": "Dolly back 1.7m and pedestal up 0.65m. Counter-tilt only enough to keep the prop planted on the lower third. Yaw 0. Roll 0. Lens stays 24mm.",
        "easing": "cubic-out",
        "parallax": "Floorboards and ceiling must both enter frame. That is the proof of height.",
        "compounds": [],
        "cut_in_from": ["prop-macro", "snap-inset"],
        "cut_out_to": ["quiet-push", "parallax-slider", "boot-crane"],
        "never_after": ["consequence-pull", "overhead-settle"],
        "do_not": [
            "Do not lose the prop.",
            "Do not zoom out.",
            "Do not crane so high the character becomes a circle with no feet.",
        ],
        "video_model_line": "24mm camera dollies back 1.7 meters and rises 0.65 meters over 1.8 seconds, ease-out, no zoom, no yaw, the small prop stays on the lower third while the full room opens around it, vertical 9:16.",
    },
    {
        "id": "parallax-slider",
        "name": "Parallax slider",
        "job": "Cross a place while a sentence of context plays. The move is the geography.",
        "frames": 60,
        "arrive_by_frame": 52,
        "lens_mm": 35,
        "aperture": 4,
        "focus": "the character or the work surface, not the passing foreground",
        "start": {"truck_m": 0.0, "height_m": 1.4, "yaw_deg": 6},
        "end": {"truck_m": 0.8, "height_m": 1.4, "yaw_deg": -4},
        "path": "Truck 0.8m sideways. Counter-yaw about 10 degrees so the subject stays near the same screen position. One foreground shape (post, wheel, jar) crosses at least 30% of the frame width.",
        "easing": "linear for the middle 70%, cubic ease both ends",
        "parallax": "Three speeds: foreground fast, character medium, back wall slow. Two speeds means a missing layer.",
        "compounds": ["impact-lock"],
        "cut_in_from": ["quiet-push", "boot-crane", "arch-pass"],
        "cut_out_to": ["quiet-push", "hand-track", "occluder-clear"],
        "never_after": ["parallax-slider", "table-arc-22"],
        "do_not": [
            "Do not truck far enough to see the edge of the character card. 0.8m at 2.2m subject distance stays card-safe.",
            "Do not pan instead of truck. A pan has no parallax.",
        ],
        "video_model_line": "35mm lateral truck of 0.8 meters over 2 seconds, slight counter-pan so the subject stays put, a foreground post crosses the frame, three distinct parallax speeds, no roll, vertical 9:16.",
    },
    {
        "id": "boot-crane",
        "name": "Boot crane",
        "job": "Bring a person in from the ground they stand on. Use on an entrance or a status change.",
        "frames": 48,
        "arrive_by_frame": 40,
        "lens_mm": 35,
        "aperture": 4,
        "focus": "feet at frame 0, eyes by the end",
        "start": {"height_m": 0.35, "distance_m": 1.6, "pitch_deg": 12, "subject": "boots and the floor contact shadow"},
        "end": {"height_m": 1.45, "distance_m": 1.9, "pitch_deg": 0, "subject": "head and shoulders, feet may leave"},
        "path": "Pedestal up 1.1m while dollying out 0.3m so the head does not clip. Tilt follows. No yaw.",
        "easing": "cubic-out",
        "parallax": "The floor drops out of frame. The ceiling or the top of a door arrives.",
        "compounds": ["impact-lock"],
        "cut_in_from": ["consequence-pull", "arch-pass"],
        "cut_out_to": ["quiet-push", "hand-track"],
        "never_after": ["boot-crane", "overhead-settle"],
        "do_not": [
            "Do not start above the knees. The shot is about contact with the ground.",
            "Do not shoot so low the card's chin breaks into a crescent for the whole shot. Leave the low angle by frame 20.",
        ],
        "video_model_line": "Camera starts at boot height looking slightly up, then rises to eye height over 1.6 seconds while easing back a little, tilt follows the body, no yaw, contact shadow visible at the start, vertical 9:16.",
    },
    {
        "id": "arch-pass",
        "name": "Arch pass",
        "job": "Enter a room. The doorway, wheel, or window is a wipe made of scenery.",
        "frames": 50,
        "arrive_by_frame": 42,
        "lens_mm": 24,
        "aperture": 4,
        "focus": "rack from the near frame (frame 0-10) to the subject (by frame 24)",
        "start": {"distance_to_arch_m": 0.4, "arch_covers": 0.55, "height_m": 1.4},
        "end": {"past_arch_m": 0.7, "arch_covers": 0.0, "height_m": 1.45, "subject": "readable, not centered under a beam"},
        "path": "Dolly forward through the opening, about 1.1m of travel. A soft rack focus. No yaw beyond 5 degrees of correction.",
        "easing": "cubic-in-out",
        "parallax": "The arch leaves frame at the edges while the room inside grows. That edge-exit is the cut's motivation.",
        "compounds": [],
        "cut_in_from": ["quiet-push", "parallax-slider"],
        "cut_out_to": ["quiet-push", "boot-crane", "overhead-settle"],
        "never_after": ["arch-pass"],
        "do_not": [
            "Do not fly through a solid wall.",
            "Do not rack focus so late the subject is mush at the landing.",
        ],
        "video_model_line": "24mm camera moves forward through a doorway or wheel, the near frame slides off the edges, focus racks from that frame to the person inside, 1.7 seconds, no orbit, vertical 9:16.",
    },
    {
        "id": "table-arc-22",
        "name": "Table arc 22",
        "job": "Inspect an object with some ceremony. The only orbit in the pack, and it is small on purpose.",
        "frames": 72,
        "arrive_by_frame": 64,
        "lens_mm": 50,
        "aperture": 2.8,
        "focus": "prop, held for the whole arc",
        "start": {"radius_m": 1.15, "height_m": 1.25, "yaw_deg": -11, "pitch_deg": -12},
        "end": {"radius_m": 1.15, "height_m": 1.25, "yaw_deg": 11, "pitch_deg": -12},
        "path": "Orbit 22 degrees total around the prop at a fixed radius and height. Subject stays screen-center. Character cards in this shot must face within 15 degrees of the START camera, or be absent. A 22 degree arc will not show the card edge if they face the middle of the arc.",
        "easing": "cubic-in-out",
        "parallax": "The far side of the table and the near lip travel in opposite screen directions. If they travel together, the camera panned instead of orbiting.",
        "compounds": [],
        "cut_in_from": ["prop-macro", "quiet-push", "snap-inset"],
        "cut_out_to": ["snap-inset", "quiet-push", "hand-track"],
        "never_after": ["table-arc-22", "parallax-slider", "rival-whip"],
        "do_not": [
            "Do not exceed 22 degrees.",
            "Do not change radius. A spiral reads as dizziness on a phone.",
            "Do not put a flat character on the far side of this arc.",
        ],
        "video_model_line": "50mm orbit of only 22 degrees around a tabletop object, radius and height locked, 2.4 seconds, ease in and out, object stays centered, no zoom, vertical 9:16.",
    },
    {
        "id": "overhead-settle",
        "name": "Overhead settle",
        "job": "A plan, track, or tabletop diagram becomes a place you could stand in.",
        "frames": 54,
        "arrive_by_frame": 46,
        "lens_mm": 24,
        "aperture": 8,
        "focus": "deep. The diagram and the nearest person both readable at the end.",
        "start": {"height_m": 4.5, "pitch_deg": -62, "distance_m": 0.4},
        "end": {"height_m": 2.1, "pitch_deg": -20, "distance_m": 2.2},
        "path": "Pitch opens from a steep top view toward a three-quarter view while the camera drops and eases back. Not a flat 2D zoom on a map.",
        "easing": "cubic-in-out",
        "parallax": "Parallel lines on the floor stop being parallel. That convergence is the whole point.",
        "compounds": [],
        "cut_in_from": ["quiet-push", "arch-pass"],
        "cut_out_to": ["quiet-push", "hand-track", "snap-inset"],
        "never_after": ["overhead-settle", "consequence-pull", "boot-crane"],
        "do_not": [
            "Do not go to a perfect 90 degree top-down and stay there. Phone viewers lose the room.",
            "Do not include a flat character face in the steep first half. Show the set, the path, the prop. Faces return on the next shot.",
        ],
        "video_model_line": "Start steeply above a floor plan or table, 24mm, then drop and tilt toward a three-quarter view over 1.8 seconds so parallel lines converge, deep focus, no zoom, vertical 9:16.",
    },
    {
        "id": "hand-track",
        "name": "Hand track",
        "job": "Show the cause being done. The hand is the verb.",
        "frames": 48,
        "arrive_by_frame": 40,
        "lens_mm": 50,
        "aperture": 2.8,
        "focus": "the hand and the prop, together",
        "start": {"follows": "hand", "lead_frames": 4, "height_m": 1.15},
        "end": {"follows": "hand has stopped", "height_m": 1.15},
        "path": "Truck or short dolly locked to the hand's path, never more than 0.45m. Camera leads the hand by about 4 frames, then stops when the hand stops. If you need the stop to feel like a hit, add impact-lock on the contact frame.",
        "easing": "match the hand. Do not ease a motion the hand did not ease.",
        "parallax": "The tabletop texture slides under the hand. The hand stays almost pinned on screen.",
        "compounds": ["impact-lock"],
        "cut_in_from": ["table-arc-22", "quiet-push", "occluder-clear"],
        "cut_out_to": ["snap-inset", "impact-lock shot", "quiet-push"],
        "never_after": ["hand-track"],
        "do_not": [
            "Do not orbit the hand.",
            "Do not keep drifting after the hand has finished. The leftover drift looks like a mistake.",
        ],
        "video_model_line": "50mm camera tracks a hand placing or cutting a small object, hand stays near the same spot on screen, table slides under it, camera stops when the hand stops, shallow focus, no orbit, vertical 9:16.",
    },
    {
        "id": "occluder-clear",
        "name": "Occluder clear",
        "job": "Withhold the look for half a second, then pay it. A person, a wheel, a jar blocks the subject.",
        "frames": 42,
        "arrive_by_frame": 34,
        "lens_mm": 50,
        "aperture": 2.8,
        "focus": "the hidden subject, already. The occluder can be soft.",
        "start": {"subject_visible": 0.25, "height_m": 1.4},
        "end": {"subject_visible": 0.9, "height_m": 1.4},
        "path": "Short truck, 0.25 to 0.4m, just enough for the subject to clear the occluder. Stop as soon as the face or prop is readable. Do not keep traveling.",
        "easing": "cubic-out",
        "parallax": "Occluder and subject must be on different planes or the clear never happens.",
        "compounds": [],
        "cut_in_from": ["parallax-slider", "quiet-push"],
        "cut_out_to": ["snap-inset", "quiet-push", "hand-track"],
        "never_after": ["occluder-clear", "rival-whip"],
        "do_not": [
            "Do not fully hide the subject at frame 0. The viewer should know something is there.",
            "Do not use a foreground blur blob with no shape. The occluder is a real object in the set.",
        ],
        "video_model_line": "50mm, a real foreground object hides most of a face or prop, camera trucks just far enough to clear it over 1.4 seconds and then holds, focus already on the hidden subject, vertical 9:16.",
    },
    {
        "id": "rival-whip",
        "name": "Rival whip",
        "job": "Jump from one side of an argument to the other inside the SAME set. This is a transition, not a scene.",
        "frames": 8,
        "arrive_by_frame": 8,
        "lens_mm": 35,
        "aperture": 5.6,
        "focus": "match both sides. Do not rack during the whip.",
        "start": {"note": "last frame of the outgoing shot, already composed"},
        "end": {"note": "first frame of the incoming shot, already composed"},
        "path": "Eight frames of directional motion blur along a pan of roughly 40 to 70 degrees. Do not try to render a readable character during these 8 frames. The shots on either side are ordinary quiet-push or parallax-slider shots with an 8-frame hold.",
        "easing": "linear blur, not an ease. Eased whips look like a mistake.",
        "parallax": "None. This is a smear. Parallax belongs to the shots it connects.",
        "compounds": [],
        "cut_in_from": ["quiet-push", "parallax-slider"],
        "cut_out_to": ["quiet-push", "parallax-slider"],
        "never_after": ["rival-whip", "table-arc-22", "snap-inset"],
        "do_not": [
            "Do not whip to a different set. If the place changes, it is a cut, not a whip.",
            "Do not whip more than once a film.",
            "Do not put text on the whip frames.",
        ],
        "video_model_line": "Eight frames of horizontal motion blur whipping from one framed person to another person in the same room, no readable face during the blur, no zoom, vertical 9:16.",
    },
    {
        "id": "snap-inset",
        "name": "Snap inset",
        "job": "The one detail that makes the cause fair. A notch, a stamp, a gap, a reflection.",
        "frames": 28,
        "arrive_by_frame": 12,
        "lens_mm": 85,
        "aperture": 2.8,
        "focus": "the detail, already sharp at frame 0",
        "start": {"distance_m": 0.7, "detail_frame_height": 0.18},
        "end": {"distance_m": 0.48, "detail_frame_height": 0.34},
        "path": "Fast dolly in of 0.22m over 6 frames, 8% overshoot, settle by frame 12, then HOLD. No zoom. The hold is the shot. Cutting on the overshoot feels cheap.",
        "easing": "overshoot then settle, then lock",
        "parallax": "Tiny, because the move is short. The detail must be a real 3D edge, not a drawn circle that scales.",
        "compounds": [],
        "cut_in_from": ["hand-track", "table-arc-22", "quiet-push", "occluder-clear"],
        "cut_out_to": ["quiet-push", "consequence-pull", "answer-drift"],
        "never_after": ["snap-inset", "prop-macro"],
        "do_not": [
            "Do not punch in on a face for emphasis. This preset is for the mechanism.",
            "Do not animate the detail itself more than the camera. The camera is the emphasis.",
            "Do not use more than three snap-insets in one film.",
        ],
        "video_model_line": "85mm, a small mechanical detail is already sharp, camera dollies in fast over 6 frames with a slight overshoot, settles, and holds dead still, no zoom, no shake, vertical 9:16.",
    },
    {
        "id": "answer-drift",
        "name": "Answer drift",
        "job": "Last shot. The viewer restates the cause. Almost still.",
        "frames": 75,
        "arrive_by_frame": 67,
        "lens_mm": 35,
        "aperture": 5.6,
        "focus": "the prop AND the result in the same deep-enough frame",
        "start": {"distance_m": 2.3, "height_m": 1.5, "pitch_deg": -3},
        "end": {"distance_m": 2.22, "height_m": 1.5, "pitch_deg": -3},
        "path": "Dolly in 8 centimeters over the whole shot. That is all. If you can see the move without looking for it, it is too big.",
        "easing": "linear, very slow",
        "parallax": "Barely. Enough that the frame is not a freeze, not enough to distract.",
        "compounds": [],
        "cut_in_from": ["quiet-push", "snap-inset", "consequence-pull"],
        "cut_out_to": ["end"],
        "never_after": [],
        "do_not": [
            "Do not end on a snap, a whip, or a black card.",
            "Do not cover the prop with the last caption.",
            "Do not introduce a new fact in this shot.",
        ],
        "video_model_line": "35mm almost-locked shot, camera creeps forward only 8 centimeters over 2.5 seconds, the prop and its result both visible, no pan, no zoom, no music sting camera move, vertical 9:16.",
    },
]


def md_preset(p: dict) -> str:
    s, e = p["start"], p["end"]
    lines = [
        f"# {p['id']}",
        "",
        f"**{p['name']}.** {p['job']}",
        "",
        "| | |",
        "|---|---|",
        f"| frames | {p['frames']} at 30 fps ({p['frames']/30:.2f}s) |",
        f"| move has arrived by | frame {p['arrive_by_frame']} |",
        f"| then hold | {p['frames'] - p['arrive_by_frame']} frames |",
        f"| lens | {p['lens_mm']}mm |",
        f"| aperture | f/{p['aperture']} |",
        f"| focus | {p['focus']} |",
        f"| easing | {p['easing']} |",
        "",
        "## Path",
        "",
        p["path"],
        "",
        "Start: `" + json.dumps(s) + "`",
        "",
        "End: `" + json.dumps(e) + "`",
        "",
        "## Parallax check",
        "",
        p["parallax"],
        "",
        "## Allowed with",
        "",
        (", ".join(p["compounds"]) if p["compounds"] else "Nothing. This preset is the whole shot."),
        "",
        f"Cut in from: {', '.join(p['cut_in_from'])}.",
        "",
        f"Cut out to: {', '.join(p['cut_out_to'])}.",
        "",
        (f"Never directly after: {', '.join(p['never_after'])}." if p["never_after"] else "No hard ban on the previous shot."),
        "",
        "## Do not",
        "",
    ]
    for d in p["do_not"]:
        lines.append(f"- {d}")
    lines += [
        "",
        "## One line, if a video model needs it",
        "",
        p["video_model_line"],
        "",
    ]
    return "\n".join(lines)


def presets_md() -> str:
    parts = [
        "# Presets",
        "",
        "Canonical machine list: `presets.json`. This file is the same data, readable.",
        "",
        "Distances are meters in a full-size room. Scale them all by the same factor if the set is a miniature. Angles are degrees. Time is frames at 30 fps.",
        "",
        "The character is a flat card. That is why the only orbit is 22 degrees and why sliders stay short.",
        "",
    ]
    for p in PRESETS:
        parts.append(md_preset(p))
        parts.append("\n---\n")
    return "\n".join(parts)


CLAUDE = """# Camera director

You are cutting an original 9:16 explainer. Illustrated flat characters stand in a lit 3D room. You do not copy any channel's characters, sets, titles, scripts, thumbnails, or voice.

Read `presets.json` before you assign a camera. It is the source of truth. `PRESETS.md` is the same data in prose. `grammar.md` is why the numbers exist.

## What you output

For each shot, a card with only these fields:

- id
- preset (one id from presets.json)
- modifier (`none` or `impact-lock`, and only if that preset allows it)
- frames
- set (reuse; 3 to 5 sets in the whole film)
- lens_mm (use the preset's lens)
- what is in focus
- the prop, and whether captions clear it
- one sentence of action

Do not output a new camera style. Do not say "cinematic", "dynamic", or "subtle Ken Burns" instead of a preset id.

## Assignment

1. Cut when the sentence says something new, not when a timer fires. Most shots land between 40 and 72 frames. `rival-whip` is 8. `snap-inset` is 28. `answer-drift` is 75.
2. First shot is `prop-macro` or `consequence-pull`. Last shot is `answer-drift`.
3. If you are unsure, `quiet-push`.
4. Check `never_after` before you lock the list.
5. The move arrives, then holds 8 frames. Do not cut on the way in.
6. Dolly means the camera moves. Do not substitute a zoom.
7. A flat character card faces the middle of the shot's arc. Do not schedule `table-arc-22` on a card that would be seen edge-on.
8. Same set, new preset, when the place has not changed.
9. `rival-whip` once per film, and only inside one set.
10. `snap-inset` at most three times, and only on the mechanism, never on a face for emphasis.

## Timing rail

Use this as a clock, not as a plot. The story itself must be original and sourced if you claim it is true.

| beat | seconds | allowed presets |
|---|---|---|
| cold open | 0–3 | prop-macro, consequence-pull |
| stake | 3–12 | boot-crane, quiet-push, parallax-slider, arch-pass |
| attempt | 12–28 | hand-track, table-arc-22, quiet-push, arch-pass |
| pressure | 28–40 | parallax-slider, occluder-clear, rival-whip, impact-lock |
| mechanism | 40–52 | snap-inset, prop-macro, table-arc-22, hand-track |
| payoff | 52–58 | consequence-pull, overhead-settle, quiet-push |
| rest | 58–65 | answer-drift only |

## If you are also building the picture

- 1080×1920, 30 fps.
- Light the room from a practical source. Do not shade the flat character like a 3D person.
- Contact shadow under the feet in every shot where the feet are in frame.
- Three depth layers whenever the preset's parallax check requires it.
- Captions: one or two words, lower third, never over the prop.
- No whoosh on every cut. Sound belongs to contact, not to camera moves.

## If a human asks you to copy a specific video

Refuse the copy. Offer to assign these presets to their original script instead.
"""

GRAMMAR = """# Grammar

These presets exist so a short on a phone feels directed without turning into a camera demo.

## The card problem

The person is a drawing on a plane standing in a modeled room. Two failures follow from that, and most "cinematic" defaults hit both.

1. An orbit past about 25 degrees shows the card's edge, breaks the head's ellipse, and slides the contact shadow off the feet.
2. A lens zoom changes scale but not parallax, so the room and the card move as one sticker. The prop never feels small inside a large result.

So: the only orbit is 22 degrees, at a locked radius. Everything else is a dolly, a truck, a pedestal, or a tilt. Zoom is not a preset.

## Land, then cut

At 30 fps, an 8-frame hold is a quarter of a second. That is enough for the eye to understand the framing before the next shot. Cutting while the camera is still speeding up feels like a dropped frame. Every preset names the frame by which the move has arrived. The remaining frames are the hold. Do not eat the hold.

## One move

A shot can truck, or push, or crane. It does not truck while it orbits while it zooms. The allowed pairings are in each preset under compounds. The only compound in this pack is `impact-lock`: on the frame of a physical contact, velocity goes to zero in two frames. No shake. Stopping is the accent.

## What the phone can read

- Moves under about 0.2 meters at normal room distance do not read, except `answer-drift`, where that is the point.
- Moves over about 2 meters inside a 2 second shot smear a vertical frame. `consequence-pull` is the exception, and it is mostly a rise-and-reveal with the prop pinned.
- Foreground crossing the frame is worth more than a bigger move. `parallax-slider` and `occluder-clear` and `arch-pass` are built on that.

## Set economy

Three to five rooms. A new angle is cheaper and clearer than a new place. `overhead-settle` and `consequence-pull` are how a room you already saw becomes new information.

## What this pack refuses

- 360 degree orbits and "dynamic camera"
- handheld noise as a style
- dutch angles
- animated roll
- Ken Burns on a flat illustration
- a title card as shot 1
- a black card as the ending
- whip pans between different places
- punch-ins on faces
- covering the prop with type

## Scale

Numbers assume a real-size room: eyes at 1.45 m, a table near 0.75 m, a person near 1.7 m. If you build a tabletop miniature, multiply every meter by the same scale and leave degrees, lenses, and frames alone.
"""

README = """# Prop Room Cameras

A preset pack for original vertical explainers: a flat illustrated person in a lit 3D room, 1080×1920, 30 fps, about a minute long.

It is not a remake kit. It does not contain another channel's characters, sets, titles, or scripts. The moves are original numbers for a format where the camera has to stay card-safe and the cut has to land.

## Upload this folder

Claude Project, Claude Code, or any tool that takes files:

1. Upload the whole folder, or the zip.
2. First message: `Read CLAUDE.md and presets.json. Assign cameras to my script. Do not invent moves.`
3. Paste or upload your own script after that.

If the tool only accepts one file, upload `PRESETS.md`. The rules are repeated at the top of `CLAUDE.md`.

## Files

| file | what it is |
|---|---|
| `CLAUDE.md` | Instructions for the model that will direct. |
| `presets.json` | Source of truth. Ids, frames, meters, lenses, bans. |
| `PRESETS.md` | The same presets, readable. |
| `grammar.md` | Why the numbers exist. |
| `examples/shotlist.sample.json` | A fictional minute, already assigned, so the model can see the shape. Not a story to publish. |

## The dozen moves

| id | what you feel |
|---|---|
| `prop-macro` | The object, too close, eases wider. |
| `quiet-push` | The default. A short straight push. Use when unsure. |
| `consequence-pull` | Dolly back and up. The small thing stays, the room arrives. |
| `parallax-slider` | Sideways. A foreground piece crosses. |
| `boot-crane` | From the shoes to the eyes. |
| `arch-pass` | Through a door, a wheel, a window. |
| `table-arc-22` | The only orbit. Twenty-two degrees. On purpose. |
| `overhead-settle` | A plan tilts into a place. |
| `hand-track` | Follows the hand, stops when the hand stops. |
| `occluder-clear` | Something in front slides off the subject. |
| `rival-whip` | Eight blur frames inside one room. Once a film. |
| `snap-inset` | A fast dolly onto the mechanism, then a hold. |
| `answer-drift` | The last shot. Almost still. |

`impact-lock` is not a shot. It is a stop you can add to a moving shot on the frame something hits.

## Keep it original

Use the grammar on a story you have the right to tell. Check facts if you present them as facts. Do not trace another creator's designs, narration, or edit.
"""

SAMPLE = {
    "label": "FICTION. Camera demo only. Do not publish as history or as a true story.",
    "format": {"w": 1080, "h": 1920, "fps": 30},
    "sets": ["bakery-dawn", "market-stall", "guild-table"],
    "prop": "a single knife-notch in the heel of a loaf",
    "line": "The town taxed bread by the cut slice. A notch was how a loaf admitted it had been opened. A second notch dried a different color, and that color was the lie.",
    "shots": [
        {"id": "s01", "preset": "prop-macro", "modifier": "none", "frames": 40, "set": "bakery-dawn", "focus": "the pale notch in the crust", "action": "The notch fills the frame, then the loaf eases back onto a floured board."},
        {"id": "s02", "preset": "consequence-pull", "modifier": "none", "frames": 54, "set": "bakery-dawn", "focus": "loaf, then the whole bench", "action": "Oven, bench, and a waiting crate open up behind one loaf."},
        {"id": "s03", "preset": "boot-crane", "modifier": "none", "frames": 48, "set": "bakery-dawn", "focus": "feet, then eyes", "action": "The baker steps in. Camera rises from floury shoes to the face."},
        {"id": "s04", "preset": "parallax-slider", "modifier": "none", "frames": 60, "set": "bakery-dawn", "focus": "the bench", "action": "A flour sack in the foreground crosses as the line names the tax."},
        {"id": "s05", "preset": "quiet-push", "modifier": "none", "frames": 66, "set": "bakery-dawn", "focus": "eyes", "action": "Sliced bread is taxed. A whole loaf is not."},
        {"id": "s06", "preset": "hand-track", "modifier": "none", "frames": 48, "set": "bakery-dawn", "focus": "knife and the heel of the loaf", "action": "One notch, cut, and the hand stops."},
        {"id": "s07", "preset": "snap-inset", "modifier": "none", "frames": 28, "set": "bakery-dawn", "focus": "a pale fresh cut", "action": "The crumb at the notch is still soft."},
        {"id": "s08", "preset": "quiet-push", "modifier": "none", "frames": 66, "set": "bakery-dawn", "focus": "loaf in the baker's hands", "action": "An honest loaf is one notch. Said too early, on purpose."},
        {"id": "s09", "preset": "parallax-slider", "modifier": "none", "frames": 60, "set": "bakery-dawn", "focus": "loaves on the peel", "action": "The peel crosses frame. Every loaf on it carries a single notch."},
        {"id": "s10", "preset": "arch-pass", "modifier": "none", "frames": 50, "set": "market-stall", "focus": "rack from the doorpost to the stall", "action": "Through the shop door into the morning market."},
        {"id": "s11", "preset": "parallax-slider", "modifier": "none", "frames": 60, "set": "market-stall", "focus": "two loaves", "action": "A post crosses. One loaf has one notch. The next has two."},
        {"id": "s12", "preset": "quiet-push", "modifier": "none", "frames": 66, "set": "market-stall", "focus": "the twice-cut loaf", "action": "A buyer treats the second notch as a baker's mark, not a lie."},
        {"id": "s13", "preset": "hand-track", "modifier": "impact-lock", "frames": 48, "set": "market-stall", "focus": "knife entering the crust", "action": "Someone adds a second notch at the stall. The camera stops on the cut."},
        {"id": "s14", "preset": "snap-inset", "modifier": "none", "frames": 28, "set": "market-stall", "focus": "two cuts, two colors", "action": "The new cut is pale. The older one has dried darker."},
        {"id": "s15", "preset": "occluder-clear", "modifier": "none", "frames": 42, "set": "market-stall", "focus": "a watching face behind a loaf", "action": "A loaf in front clears off a face that has already understood."},
        {"id": "s16", "preset": "quiet-push", "modifier": "none", "frames": 66, "set": "market-stall", "focus": "that face", "action": "They don't speak. The color is the evidence."},
        {"id": "s17", "preset": "boot-crane", "modifier": "none", "frames": 48, "set": "market-stall", "focus": "boots in market mud, then the face", "action": "The watcher stands. We rise with them."},
        {"id": "s18", "preset": "quiet-push", "modifier": "none", "frames": 66, "set": "market-stall", "focus": "the twice-cut loaf, held out", "action": "The loaf is the accusation. No new prop."},
        {"id": "s19", "preset": "arch-pass", "modifier": "none", "frames": 50, "set": "guild-table", "focus": "rack from a doorframe to a table", "action": "Into the guild room. Same morning, harder light."},
        {"id": "s20", "preset": "overhead-settle", "modifier": "none", "frames": 54, "set": "guild-table", "focus": "deep, ledger and loaf", "action": "A top-down ledger tilts into a room with the loaf on it."},
        {"id": "s21", "preset": "quiet-push", "modifier": "none", "frames": 66, "set": "guild-table", "focus": "inspector's hands on the page", "action": "The count is by the slice. The page has no column for color."},
        {"id": "s22", "preset": "parallax-slider", "modifier": "none", "frames": 60, "set": "guild-table", "focus": "baker on one side, inspector on the other", "action": "The table edge crosses as we slide from one seat to the other."},
        {"id": "s23", "preset": "quiet-push", "modifier": "impact-lock", "frames": 66, "set": "guild-table", "focus": "loaf set down on wood", "action": "The loaf lands. Camera velocity dies on the thud."},
        {"id": "s24", "preset": "rival-whip", "modifier": "none", "frames": 8, "set": "guild-table", "focus": "matched both sides", "action": "Eight blur frames from inspector to baker. Same room."},
        {"id": "s25", "preset": "quiet-push", "modifier": "none", "frames": 66, "set": "guild-table", "focus": "baker", "action": "The baker says nothing. The loaf stays in frame."},
        {"id": "s26", "preset": "table-arc-22", "modifier": "none", "frames": 72, "set": "guild-table", "focus": "both notches", "action": "Twenty-two degrees around the loaf. No face on the far side of the turn."},
        {"id": "s27", "preset": "hand-track", "modifier": "none", "frames": 48, "set": "guild-table", "focus": "a finger on the darker notch", "action": "A finger finds the dried cut and stops."},
        {"id": "s28", "preset": "snap-inset", "modifier": "none", "frames": 28, "set": "guild-table", "focus": "the darker crumb", "action": "Third and last punch. The lie is a color, not a shape."},
        {"id": "s29", "preset": "quiet-push", "modifier": "none", "frames": 66, "set": "guild-table", "focus": "both people, loaf between", "action": "The rule finally fits the object."},
        {"id": "s30", "preset": "occluder-clear", "modifier": "none", "frames": 42, "set": "guild-table", "focus": "the notch, revealed past a ledger", "action": "The standing ledger slides off the heel of the loaf."},
        {"id": "s31", "preset": "quiet-push", "modifier": "none", "frames": 66, "set": "guild-table", "focus": "the single idea, held", "action": "Hold the explanation. Do not add a fact."},
        {"id": "s32", "preset": "consequence-pull", "modifier": "none", "frames": 54, "set": "bakery-dawn", "focus": "one loaf, then the oven behind it", "action": "Back in the bakery. The notch stays low in frame while the oven returns."},
        {"id": "s33", "preset": "answer-drift", "modifier": "none", "frames": 75, "set": "bakery-dawn", "focus": "the single honest notch", "action": "Almost still. One notch. No new fact."},
    ],
}


def sample_md() -> str:
    frames = sum(s["frames"] for s in SAMPLE["shots"])
    lines = [
        "# Sample assignment",
        "",
        SAMPLE["label"],
        "",
        f"Prop: {SAMPLE['prop']}",
        "",
        SAMPLE["line"],
        "",
        f"Total {frames} frames, {frames/30:.1f}s at 30 fps. Sets: {', '.join(SAMPLE['sets'])}.",
        "",
        "| shot | preset | mod | frames | set | action |",
        "|---|---|---|---|---|---|",
    ]
    for s in SAMPLE["shots"]:
        lines.append(
            f"| {s['id']} | {s['preset']} | {s['modifier']} | {s['frames']} | {s['set']} | {s['action']} |"
        )
    lines += [
        "",
        "Notice the bans it respects: one whip, and not into the arc; arc only after a quiet shot; three snap-insets, all on the cut in the bread; impact-lock only on presets that allow it; ending on answer-drift in a room already built.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    PACK["presets"] = PRESETS
    (ROOT / "presets.json").write_text(json.dumps(PACK, indent=2) + "\n", encoding="utf-8")
    (ROOT / "PRESETS.md").write_text(presets_md(), encoding="utf-8")
    (ROOT / "CLAUDE.md").write_text(CLAUDE, encoding="utf-8")
    (ROOT / "grammar.md").write_text(GRAMMAR, encoding="utf-8")
    (ROOT / "README.md").write_text(README, encoding="utf-8")
    ex = ROOT / "examples"
    ex.mkdir(exist_ok=True)
    (ex / "shotlist.sample.json").write_text(json.dumps(SAMPLE, indent=2) + "\n", encoding="utf-8")
    (ex / "shotlist.sample.md").write_text(sample_md(), encoding="utf-8")
    # sanity
    ids = [p["id"] for p in PRESETS]
    assert len(ids) == len(set(ids))
    allowed = set(ids)
    for p in PRESETS:
        for key in ("cut_out_to", "never_after"):
            for ref in p[key]:
                if ref in ("any", "end", "impact-lock shot"):
                    continue
                assert ref in allowed or ref in ("cold-open",), (p["id"], key, ref)
    frames = sum(s["frames"] for s in SAMPLE["shots"])
    assert 58 <= frames / 30 <= 70, frames / 30
    by_id = {p["id"]: p for p in PRESETS}
    snaps = 0
    whips = 0
    for i, shot in enumerate(SAMPLE["shots"]):
        preset = by_id[shot["preset"]]
        assert shot["frames"] == preset["frames"], (shot["id"], shot["frames"], preset["frames"])
        if shot["modifier"] != "none":
            assert shot["modifier"] in preset["compounds"], shot["id"]
        if i:
            prev = SAMPLE["shots"][i - 1]["preset"]
            assert prev not in preset["never_after"], (shot["id"], prev, preset["never_after"])
        if shot["preset"] == "snap-inset":
            snaps += 1
        if shot["preset"] == "rival-whip":
            whips += 1
            assert SAMPLE["shots"][i - 1]["set"] == shot["set"]
            assert SAMPLE["shots"][i + 1]["set"] == shot["set"]
    assert snaps <= 3
    assert whips <= 1
    assert SAMPLE["shots"][0]["preset"] in ("prop-macro", "consequence-pull")
    assert SAMPLE["shots"][-1]["preset"] == "answer-drift"
    print(f"presets {len(ids)} sample {frames/30:.2f}s shots {len(SAMPLE['shots'])}")


if __name__ == "__main__":
    main()
