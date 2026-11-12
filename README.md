# Camera Presets — 2.5D Deadpan & Uncanny Cinema

Deterministic, frame-accurate **camera rig + preset system** and a **5-plane 2.5D parallax stage** for **Three.js + Remotion** (60 fps) pipelines.

Built for a rigid, paper-cutout diorama look: uncomfortable stillness, mechanical transitions, and locked Z-depth buckets so perspective never breaks the layout.

## What’s included

| Path | Description |
|------|-------------|
| [`src/camera/cameraPresets.ts`](src/camera/cameraPresets.ts) | Pure TypeScript camera evaluator: 6 named presets, easing, gate-weave, vertigo math |
| [`src/camera/KnoxCameraRig.tsx`](src/camera/KnoxCameraRig.tsx) | Two-node R3F + Remotion camera hierarchy driven by `evaluateCameraRig` |
| [`src/camera/ParallaxStage25D.tsx`](src/camera/ParallaxStage25D.tsx) | Remotion + R3F component that loads PNG cutouts onto 5 Z-buckets with frustum compensation |
| [`src/camera/SuburbanSceneComposition.tsx`](src/camera/SuburbanSceneComposition.tsx) | Drop-in Remotion composition wiring camera + stage from JSON |
| [`src/camera/index.ts`](src/camera/index.ts) | Barrel exports |
| [`docs/2.5d-deadpan-uncanny-cinema-spec.md`](docs/2.5d-deadpan-uncanny-cinema-spec.md) | Full architectural & visual-grammar specification |
| [`examples/scene-timeline.json`](examples/scene-timeline.json) | Shots-only timeline |
| [`examples/scene-shotlist.json`](examples/scene-shotlist.json) | Shots **+** layers for `SuburbanSceneComposition` |

## Camera presets (visual grammar)

1. **`deadpan-lock`** — Locked tripod stillness with optional micro gate-weave  
2. **`tension-push`** — Linear Z push (no ease-out); cuts while still moving  
3. **`parallax-slide`** — Lateral dolly that exposes depth between Z-planes  
4. **`whip-pan-snap`** — Fast X snap with overshoot + damped settle  
5. **`vertigo-creep`** — Dolly-out + FOV zoom that freezes subject scale at Z=0  
6. **`pedestal-reveal`** — Pure Y elevator move, no pitch  

All transforms are evaluated as a function of frame + config so results are deterministic and frame-accurate.

## Two-node camera hierarchy

Do **not** animate `THREE.PerspectiveCamera` in world space directly:

1. **`CameraTrackNode`** (`THREE.Group`) — world X/Y/Z + look-at  
2. **`CameraBodyNode`** (`THREE.PerspectiveCamera`, child) — FOV, Dutch roll, micro-jitter  

`KnoxCameraRig` implements this hierarchy and applies `evaluateCameraRig()` every frame.

## Quick start (Remotion)

```tsx
import { SuburbanSceneComposition } from './camera/SuburbanSceneComposition';

// Register in Root.tsx / composition registry:
// <Composition id="SuburbanScene" component={SuburbanSceneComposition} ... />
```

Or wire pieces yourself:

```tsx
import { ThreeCanvas } from '@remotion/three';
import { KnoxCameraRig } from './camera/KnoxCameraRig';
import { ParallaxStage25D } from './camera/ParallaxStage25D';
import sceneData from '../examples/scene-shotlist.json';

<ThreeCanvas width={width} height={height}>
  <color attach="background" args={['#d8d2c5']} />
  <KnoxCameraRig shots={sceneData.shots}>
    <ParallaxStage25D layers={sceneData.layers} referenceCameraZ={5} />
  </KnoxCameraRig>
</ThreeCanvas>
```

### Peer dependencies

These modules expect:

- `three`
- `@react-three/fiber`
- `remotion`
- `@remotion/three`

Install them in a Remotion project that consumes this code:

```bash
npm install three @react-three/fiber remotion @remotion/three
```

Place PNG cutouts under `public/art/...` (paths in `scene-shotlist.json` are relative to `public/` via Remotion `staticFile`).

## Spec & timeline

- Full design doc: [docs/2.5d-deadpan-uncanny-cinema-spec.md](docs/2.5d-deadpan-uncanny-cinema-spec.md)  
- Example shot + layer list: [examples/scene-shotlist.json](examples/scene-shotlist.json)

## License

Use and adapt freely within this project. Add an explicit license file if you publish the camera modules as a standalone package.
