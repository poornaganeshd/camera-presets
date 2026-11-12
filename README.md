# Camera Presets — 2.5D Deadpan & Uncanny Cinema

Deterministic, frame-accurate **camera rig + preset system** and a **5-plane 2.5D parallax stage** for **Three.js + Remotion** (60 fps) pipelines.

Built for a rigid, paper-cutout diorama look: uncomfortable stillness, mechanical transitions, and locked Z-depth buckets so perspective never breaks the layout.

## What’s included

| Path | Description |
|------|-------------|
| [`src/camera/cameraPresets.ts`](src/camera/cameraPresets.ts) | Pure TypeScript camera evaluator: 6 named presets, easing, gate-weave, vertigo math |
| [`src/camera/ParallaxStage25D.tsx`](src/camera/ParallaxStage25D.tsx) | Remotion + R3F component that loads PNG cutouts onto 5 Z-buckets with frustum compensation |
| [`docs/2.5d-deadpan-uncanny-cinema-spec.md`](docs/2.5d-deadpan-uncanny-cinema-spec.md) | Full architectural & visual-grammar specification |
| [`examples/scene-timeline.json`](examples/scene-timeline.json) | Declarative shot list you can drive from a composition |

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

`evaluateCameraRig()` returns `{ position, lookAt, fov, rollRad }` for you to apply to that hierarchy.

## 5-plane Z-depth buckets

Assets live on discrete Z planes. Frustum compensation keeps apparent size stable when the camera moves:

```ts
S = (Z_cam - Z_layer) / (Z_cam - Z_ref)
```

See the [spec](docs/2.5d-deadpan-uncanny-cinema-spec.md) for default bucket coordinates and overscan margins.  
`ParallaxStage25D` ships its own bucket table (`FG_EXTREME` … `BG_SKY`) tuned for a reference camera at Z ≈ 5.

## Quick start (Remotion + R3F)

```ts
import { evaluateCameraRig, type CameraShotConfig } from './camera/cameraPresets';
import { ParallaxStage25D } from './camera/ParallaxStage25D';

// Inside a Remotion frame:
const config: CameraShotConfig = {
  preset: 'tension-push',
  startFrame: 0,
  durationInFrames: 150,
  params: { startZ: 10, endZ: 6.5, baseFov: 40 },
};

const state = evaluateCameraRig(frame, config);
// Apply state.position / state.lookAt / state.fov / state.rollRad to your two-node rig
```

```tsx
<ParallaxStage25D
  layers={[
    {
      id: 'hero',
      textureUrl: 'art/char.png',
      depthBucket: 'MID_SUBJECT',
      position: [0, 0],
      baseHeight: 2.2,
      idleBob: { enabled: true },
    },
    // … more layers
  ]}
/>
```

### Peer dependencies

These modules expect (not yet declared in this workspace’s root `package.json`):

- `three`
- `@react-three/fiber`
- `remotion` (for `ParallaxStage25D`)

Install them in a Remotion project that consumes this code, or add them to this repo if you wire the stage into the existing app.

## Spec & timeline

- Full design doc: [docs/2.5d-deadpan-uncanny-cinema-spec.md](docs/2.5d-deadpan-uncanny-cinema-spec.md)  
- Example shot list: [examples/scene-timeline.json](examples/scene-timeline.json)

## License

Use and adapt freely within this project. Add an explicit license file if you publish the camera modules as a standalone package.
