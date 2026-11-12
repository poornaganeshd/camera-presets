# Presets

Canonical machine list: `presets.json`. This file is the same data, readable.

Distances are meters in a full-size room. Scale them all by the same factor if the set is a miniature. Angles are degrees. Time is frames at 30 fps.

The character is a flat card. That is why the only orbit is 22 degrees and why sliders stay short.

# prop-macro

**Prop macro.** Open on the object, or return to it when the mechanism is named.

| | |
|---|---|
| frames | 40 at 30 fps (1.33s) |
| move has arrived by | frame 32 |
| then hold | 8 frames |
| lens | 85mm |
| aperture | f/2.8 |
| focus | prop surface, a real detail (edge, notch, stamp), not the center of a blur |
| easing | cubic-out |

## Path

Slow dolly back 0.20m and rise 0.07m. No yaw. No roll. No lens zoom.

Start: `{"distance_m": 0.28, "height_m": 1.05, "pitch_deg": -8, "yaw_deg": 0, "prop_frame_height": 0.46}`

End: `{"distance_m": 0.48, "height_m": 1.12, "pitch_deg": -6, "yaw_deg": 0, "prop_frame_height": 0.3}`

## Parallax check

The prop's near edge moves more than its far edge. If it scales like a sticker, you zoomed. Redo as a dolly.

## Allowed with

Nothing. This preset is the whole shot.

Cut in from: cold-open, snap-inset, answer-drift.

Cut out to: consequence-pull, quiet-push, table-arc-22.

Never directly after: rival-whip.

## Do not

- Do not put a title card in front of this shot.
- Do not orbit. At 85mm an arc turns into a smear.
- Do not let the prop touch the caption band.

## One line, if a video model needs it

85mm macro of one small object on a table, camera dollies back 20 centimeters and rises slightly over 1.3 seconds, cubic ease-out, no zoom, no orbit, shallow focus on a real surface detail, vertical 9:16.


---

# quiet-push

**Quiet push.** Default listening shot while a fact is said. Use this when unsure.

| | |
|---|---|
| frames | 66 at 30 fps (2.20s) |
| move has arrived by | frame 58 |
| then hold | 8 frames |
| lens | 35mm |
| aperture | f/5.6 |
| focus | character card eyes, or the prop if the line is about the prop |
| easing | cubic-in-out |

## Path

Dolly in 0.35m on a straight line. Height locked. No pan.

Start: `{"distance_m": 2.4, "height_m": 1.45, "pitch_deg": 0, "yaw_deg": 0, "subject": "waist-up, headroom 12% of frame"}`

End: `{"distance_m": 2.05, "height_m": 1.45, "pitch_deg": 0, "yaw_deg": 0, "subject": "chest-up"}`

## Parallax check

A foreground mug, post, or door edge must slide a little. If nothing nearer than the character exists, the push looks like a zoom. Add one foreground piece.

## Allowed with

impact-lock

Cut in from: any.

Cut out to: any.

No hard ban on the previous shot.

## Do not

- Do not push more than 0.35m. Bigger reads as comedy.
- Do not add handheld noise.
- Do not use this twice in a row with the same framing size. Change size or change preset.

## One line, if a video model needs it

35mm, eye height, slow straight dolly in of 35 centimeters over 2.2 seconds, cubic ease in and out, no pan, no zoom, no shake, a nearer object slides against the back wall, vertical 9:16.


---

# consequence-pull

**Consequence pull.** Prove the small object sits inside a result big enough to matter.

| | |
|---|---|
| frames | 54 at 30 fps (1.80s) |
| move has arrived by | frame 46 |
| then hold | 8 frames |
| lens | 24mm |
| aperture | f/5.6 |
| focus | start on the prop, widen so the room is readable by the end. Do not blur the prop away. |
| easing | cubic-out |

## Path

Dolly back 1.7m and pedestal up 0.65m. Counter-tilt only enough to keep the prop planted on the lower third. Yaw 0. Roll 0. Lens stays 24mm.

Start: `{"distance_m": 0.9, "height_m": 1.2, "pitch_deg": -4, "prop_on": "lower third"}`

End: `{"distance_m": 2.6, "height_m": 1.85, "pitch_deg": -8, "prop_on": "lower third, still fully visible"}`

## Parallax check

Floorboards and ceiling must both enter frame. That is the proof of height.

## Allowed with

Nothing. This preset is the whole shot.

Cut in from: prop-macro, snap-inset.

Cut out to: quiet-push, parallax-slider, boot-crane.

Never directly after: consequence-pull, overhead-settle.

## Do not

- Do not lose the prop.
- Do not zoom out.
- Do not crane so high the character becomes a circle with no feet.

## One line, if a video model needs it

24mm camera dollies back 1.7 meters and rises 0.65 meters over 1.8 seconds, ease-out, no zoom, no yaw, the small prop stays on the lower third while the full room opens around it, vertical 9:16.


---

# parallax-slider

**Parallax slider.** Cross a place while a sentence of context plays. The move is the geography.

| | |
|---|---|
| frames | 60 at 30 fps (2.00s) |
| move has arrived by | frame 52 |
| then hold | 8 frames |
| lens | 35mm |
| aperture | f/4 |
| focus | the character or the work surface, not the passing foreground |
| easing | linear for the middle 70%, cubic ease both ends |

## Path

Truck 0.8m sideways. Counter-yaw about 10 degrees so the subject stays near the same screen position. One foreground shape (post, wheel, jar) crosses at least 30% of the frame width.

Start: `{"truck_m": 0.0, "height_m": 1.4, "yaw_deg": 6}`

End: `{"truck_m": 0.8, "height_m": 1.4, "yaw_deg": -4}`

## Parallax check

Three speeds: foreground fast, character medium, back wall slow. Two speeds means a missing layer.

## Allowed with

impact-lock

Cut in from: quiet-push, boot-crane, arch-pass.

Cut out to: quiet-push, hand-track, occluder-clear.

Never directly after: parallax-slider, table-arc-22.

## Do not

- Do not truck far enough to see the edge of the character card. 0.8m at 2.2m subject distance stays card-safe.
- Do not pan instead of truck. A pan has no parallax.

## One line, if a video model needs it

35mm lateral truck of 0.8 meters over 2 seconds, slight counter-pan so the subject stays put, a foreground post crosses the frame, three distinct parallax speeds, no roll, vertical 9:16.


---

# boot-crane

**Boot crane.** Bring a person in from the ground they stand on. Use on an entrance or a status change.

| | |
|---|---|
| frames | 48 at 30 fps (1.60s) |
| move has arrived by | frame 40 |
| then hold | 8 frames |
| lens | 35mm |
| aperture | f/4 |
| focus | feet at frame 0, eyes by the end |
| easing | cubic-out |

## Path

Pedestal up 1.1m while dollying out 0.3m so the head does not clip. Tilt follows. No yaw.

Start: `{"height_m": 0.35, "distance_m": 1.6, "pitch_deg": 12, "subject": "boots and the floor contact shadow"}`

End: `{"height_m": 1.45, "distance_m": 1.9, "pitch_deg": 0, "subject": "head and shoulders, feet may leave"}`

## Parallax check

The floor drops out of frame. The ceiling or the top of a door arrives.

## Allowed with

impact-lock

Cut in from: consequence-pull, arch-pass.

Cut out to: quiet-push, hand-track.

Never directly after: boot-crane, overhead-settle.

## Do not

- Do not start above the knees. The shot is about contact with the ground.
- Do not shoot so low the card's chin breaks into a crescent for the whole shot. Leave the low angle by frame 20.

## One line, if a video model needs it

Camera starts at boot height looking slightly up, then rises to eye height over 1.6 seconds while easing back a little, tilt follows the body, no yaw, contact shadow visible at the start, vertical 9:16.


---

# arch-pass

**Arch pass.** Enter a room. The doorway, wheel, or window is a wipe made of scenery.

| | |
|---|---|
| frames | 50 at 30 fps (1.67s) |
| move has arrived by | frame 42 |
| then hold | 8 frames |
| lens | 24mm |
| aperture | f/4 |
| focus | rack from the near frame (frame 0-10) to the subject (by frame 24) |
| easing | cubic-in-out |

## Path

Dolly forward through the opening, about 1.1m of travel. A soft rack focus. No yaw beyond 5 degrees of correction.

Start: `{"distance_to_arch_m": 0.4, "arch_covers": 0.55, "height_m": 1.4}`

End: `{"past_arch_m": 0.7, "arch_covers": 0.0, "height_m": 1.45, "subject": "readable, not centered under a beam"}`

## Parallax check

The arch leaves frame at the edges while the room inside grows. That edge-exit is the cut's motivation.

## Allowed with

Nothing. This preset is the whole shot.

Cut in from: quiet-push, parallax-slider.

Cut out to: quiet-push, boot-crane, overhead-settle.

Never directly after: arch-pass.

## Do not

- Do not fly through a solid wall.
- Do not rack focus so late the subject is mush at the landing.

## One line, if a video model needs it

24mm camera moves forward through a doorway or wheel, the near frame slides off the edges, focus racks from that frame to the person inside, 1.7 seconds, no orbit, vertical 9:16.


---

# table-arc-22

**Table arc 22.** Inspect an object with some ceremony. The only orbit in the pack, and it is small on purpose.

| | |
|---|---|
| frames | 72 at 30 fps (2.40s) |
| move has arrived by | frame 64 |
| then hold | 8 frames |
| lens | 50mm |
| aperture | f/2.8 |
| focus | prop, held for the whole arc |
| easing | cubic-in-out |

## Path

Orbit 22 degrees total around the prop at a fixed radius and height. Subject stays screen-center. Character cards in this shot must face within 15 degrees of the START camera, or be absent. A 22 degree arc will not show the card edge if they face the middle of the arc.

Start: `{"radius_m": 1.15, "height_m": 1.25, "yaw_deg": -11, "pitch_deg": -12}`

End: `{"radius_m": 1.15, "height_m": 1.25, "yaw_deg": 11, "pitch_deg": -12}`

## Parallax check

The far side of the table and the near lip travel in opposite screen directions. If they travel together, the camera panned instead of orbiting.

## Allowed with

Nothing. This preset is the whole shot.

Cut in from: prop-macro, quiet-push, snap-inset.

Cut out to: snap-inset, quiet-push, hand-track.

Never directly after: table-arc-22, parallax-slider, rival-whip.

## Do not

- Do not exceed 22 degrees.
- Do not change radius. A spiral reads as dizziness on a phone.
- Do not put a flat character on the far side of this arc.

## One line, if a video model needs it

50mm orbit of only 22 degrees around a tabletop object, radius and height locked, 2.4 seconds, ease in and out, object stays centered, no zoom, vertical 9:16.


---

# overhead-settle

**Overhead settle.** A plan, track, or tabletop diagram becomes a place you could stand in.

| | |
|---|---|
| frames | 54 at 30 fps (1.80s) |
| move has arrived by | frame 46 |
| then hold | 8 frames |
| lens | 24mm |
| aperture | f/8 |
| focus | deep. The diagram and the nearest person both readable at the end. |
| easing | cubic-in-out |

## Path

Pitch opens from a steep top view toward a three-quarter view while the camera drops and eases back. Not a flat 2D zoom on a map.

Start: `{"height_m": 4.5, "pitch_deg": -62, "distance_m": 0.4}`

End: `{"height_m": 2.1, "pitch_deg": -20, "distance_m": 2.2}`

## Parallax check

Parallel lines on the floor stop being parallel. That convergence is the whole point.

## Allowed with

Nothing. This preset is the whole shot.

Cut in from: quiet-push, arch-pass.

Cut out to: quiet-push, hand-track, snap-inset.

Never directly after: overhead-settle, consequence-pull, boot-crane.

## Do not

- Do not go to a perfect 90 degree top-down and stay there. Phone viewers lose the room.
- Do not include a flat character face in the steep first half. Show the set, the path, the prop. Faces return on the next shot.

## One line, if a video model needs it

Start steeply above a floor plan or table, 24mm, then drop and tilt toward a three-quarter view over 1.8 seconds so parallel lines converge, deep focus, no zoom, vertical 9:16.


---

# hand-track

**Hand track.** Show the cause being done. The hand is the verb.

| | |
|---|---|
| frames | 48 at 30 fps (1.60s) |
| move has arrived by | frame 40 |
| then hold | 8 frames |
| lens | 50mm |
| aperture | f/2.8 |
| focus | the hand and the prop, together |
| easing | match the hand. Do not ease a motion the hand did not ease. |

## Path

Truck or short dolly locked to the hand's path, never more than 0.45m. Camera leads the hand by about 4 frames, then stops when the hand stops. If you need the stop to feel like a hit, add impact-lock on the contact frame.

Start: `{"follows": "hand", "lead_frames": 4, "height_m": 1.15}`

End: `{"follows": "hand has stopped", "height_m": 1.15}`

## Parallax check

The tabletop texture slides under the hand. The hand stays almost pinned on screen.

## Allowed with

impact-lock

Cut in from: table-arc-22, quiet-push, occluder-clear.

Cut out to: snap-inset, impact-lock shot, quiet-push.

Never directly after: hand-track.

## Do not

- Do not orbit the hand.
- Do not keep drifting after the hand has finished. The leftover drift looks like a mistake.

## One line, if a video model needs it

50mm camera tracks a hand placing or cutting a small object, hand stays near the same spot on screen, table slides under it, camera stops when the hand stops, shallow focus, no orbit, vertical 9:16.


---

# occluder-clear

**Occluder clear.** Withhold the look for half a second, then pay it. A person, a wheel, a jar blocks the subject.

| | |
|---|---|
| frames | 42 at 30 fps (1.40s) |
| move has arrived by | frame 34 |
| then hold | 8 frames |
| lens | 50mm |
| aperture | f/2.8 |
| focus | the hidden subject, already. The occluder can be soft. |
| easing | cubic-out |

## Path

Short truck, 0.25 to 0.4m, just enough for the subject to clear the occluder. Stop as soon as the face or prop is readable. Do not keep traveling.

Start: `{"subject_visible": 0.25, "height_m": 1.4}`

End: `{"subject_visible": 0.9, "height_m": 1.4}`

## Parallax check

Occluder and subject must be on different planes or the clear never happens.

## Allowed with

Nothing. This preset is the whole shot.

Cut in from: parallax-slider, quiet-push.

Cut out to: snap-inset, quiet-push, hand-track.

Never directly after: occluder-clear, rival-whip.

## Do not

- Do not fully hide the subject at frame 0. The viewer should know something is there.
- Do not use a foreground blur blob with no shape. The occluder is a real object in the set.

## One line, if a video model needs it

50mm, a real foreground object hides most of a face or prop, camera trucks just far enough to clear it over 1.4 seconds and then holds, focus already on the hidden subject, vertical 9:16.


---

# rival-whip

**Rival whip.** Jump from one side of an argument to the other inside the SAME set. This is a transition, not a scene.

| | |
|---|---|
| frames | 8 at 30 fps (0.27s) |
| move has arrived by | frame 8 |
| then hold | 0 frames |
| lens | 35mm |
| aperture | f/5.6 |
| focus | match both sides. Do not rack during the whip. |
| easing | linear blur, not an ease. Eased whips look like a mistake. |

## Path

Eight frames of directional motion blur along a pan of roughly 40 to 70 degrees. Do not try to render a readable character during these 8 frames. The shots on either side are ordinary quiet-push or parallax-slider shots with an 8-frame hold.

Start: `{"note": "last frame of the outgoing shot, already composed"}`

End: `{"note": "first frame of the incoming shot, already composed"}`

## Parallax check

None. This is a smear. Parallax belongs to the shots it connects.

## Allowed with

Nothing. This preset is the whole shot.

Cut in from: quiet-push, parallax-slider.

Cut out to: quiet-push, parallax-slider.

Never directly after: rival-whip, table-arc-22, snap-inset.

## Do not

- Do not whip to a different set. If the place changes, it is a cut, not a whip.
- Do not whip more than once a film.
- Do not put text on the whip frames.

## One line, if a video model needs it

Eight frames of horizontal motion blur whipping from one framed person to another person in the same room, no readable face during the blur, no zoom, vertical 9:16.


---

# snap-inset

**Snap inset.** The one detail that makes the cause fair. A notch, a stamp, a gap, a reflection.

| | |
|---|---|
| frames | 28 at 30 fps (0.93s) |
| move has arrived by | frame 12 |
| then hold | 16 frames |
| lens | 85mm |
| aperture | f/2.8 |
| focus | the detail, already sharp at frame 0 |
| easing | overshoot then settle, then lock |

## Path

Fast dolly in of 0.22m over 6 frames, 8% overshoot, settle by frame 12, then HOLD. No zoom. The hold is the shot. Cutting on the overshoot feels cheap.

Start: `{"distance_m": 0.7, "detail_frame_height": 0.18}`

End: `{"distance_m": 0.48, "detail_frame_height": 0.34}`

## Parallax check

Tiny, because the move is short. The detail must be a real 3D edge, not a drawn circle that scales.

## Allowed with

Nothing. This preset is the whole shot.

Cut in from: hand-track, table-arc-22, quiet-push, occluder-clear.

Cut out to: quiet-push, consequence-pull, answer-drift.

Never directly after: snap-inset, prop-macro.

## Do not

- Do not punch in on a face for emphasis. This preset is for the mechanism.
- Do not animate the detail itself more than the camera. The camera is the emphasis.
- Do not use more than three snap-insets in one film.

## One line, if a video model needs it

85mm, a small mechanical detail is already sharp, camera dollies in fast over 6 frames with a slight overshoot, settles, and holds dead still, no zoom, no shake, vertical 9:16.


---

# answer-drift

**Answer drift.** Last shot. The viewer restates the cause. Almost still.

| | |
|---|---|
| frames | 75 at 30 fps (2.50s) |
| move has arrived by | frame 67 |
| then hold | 8 frames |
| lens | 35mm |
| aperture | f/5.6 |
| focus | the prop AND the result in the same deep-enough frame |
| easing | linear, very slow |

## Path

Dolly in 8 centimeters over the whole shot. That is all. If you can see the move without looking for it, it is too big.

Start: `{"distance_m": 2.3, "height_m": 1.5, "pitch_deg": -3}`

End: `{"distance_m": 2.22, "height_m": 1.5, "pitch_deg": -3}`

## Parallax check

Barely. Enough that the frame is not a freeze, not enough to distract.

## Allowed with

Nothing. This preset is the whole shot.

Cut in from: quiet-push, snap-inset, consequence-pull.

Cut out to: end.

No hard ban on the previous shot.

## Do not

- Do not end on a snap, a whip, or a black card.
- Do not cover the prop with the last caption.
- Do not introduce a new fact in this shot.

## One line, if a video model needs it

35mm almost-locked shot, camera creeps forward only 8 centimeters over 2.5 seconds, the prop and its result both visible, no pan, no zoom, no music sting camera move, vertical 9:16.


---
