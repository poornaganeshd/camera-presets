import * as THREE from 'three';

export type CameraPresetType =
  | 'deadpan-lock'
  | 'tension-push'
  | 'parallax-slide'
  | 'whip-pan-snap'
  | 'vertigo-creep'
  | 'pedestal-reveal';

export interface CameraShotConfig {
  preset: CameraPresetType;
  startFrame: number;
  durationInFrames: number;
  fps?: number;
  params?: {
    startX?: number;
    endX?: number;
    startY?: number;
    endY?: number;
    startZ?: number;
    endZ?: number;
    baseFov?: number;
    whipTriggerFrame?: number; // Relative to startFrame
    dutchAngleDeg?: number;
    quantizeFps?: number; // Set to 12 or 24 for stop-motion stutter on camera
  };
}

export interface EvaluatedCameraState {
  position: [number, number, number];
  lookAt: [number, number, number];
  fov: number;
  rollRad: number;
}

// --- Deterministic Easing Helpers ---
const clamp01 = (v: number) => Math.max(0, Math.min(1, v));

const easeInOutCubic = (t: number): number =>
  t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;

const easeWhipSnap = (t: number): number => {
  const c = clamp01(t);
  return c < 0.5
    ? 8 * c * c * c * c
    : 1 - Math.pow(-2 * c + 2, 4) / 2;
};

// Deterministic pseudo-noise for subtle analog gate weave
const gateWeave = (frame: number, seed: number): number => {
  return Math.sin(frame * 0.37 + seed) * Math.cos(frame * 0.83 - seed) * 0.008;
};

export function evaluateCameraRig(
  currentFrame: number,
  config: CameraShotConfig
): EvaluatedCameraState {
  const fps = config.fps ?? 60;
  const p = config.params ?? {};

  // Optional frame quantization (e.g., 24fps feel inside a 60fps composition)
  let localFrame = Math.max(0, currentFrame - config.startFrame);
  if (p.quantizeFps && p.quantizeFps < fps) {
    const step = Math.round(fps / p.quantizeFps);
    localFrame = Math.floor(localFrame / step) * step;
  }

  const progress = clamp01(localFrame / Math.max(1, config.durationInFrames));

  let x = p.startX ?? 0;
  let y = p.startY ?? 0;
  let z = p.startZ ?? 10;
  let fov = p.baseFov ?? 38;
  const rollRad = THREE.MathUtils.degToRad(p.dutchAngleDeg ?? 0);

  switch (config.preset) {
    case 'deadpan-lock': {
      fov = p.baseFov ?? 35;
      x = (p.startX ?? 0) + gateWeave(localFrame, 1.1);
      y = (p.startY ?? 0) + gateWeave(localFrame, 2.7);
      z = p.startZ ?? 10;
      break;
    }

    case 'tension-push': {
      fov = p.baseFov ?? 40;
      const sZ = p.startZ ?? 10.0;
      const eZ = p.endZ ?? 6.8;
      // Strictly linear push — never eases out before the cut
      z = sZ + (eZ - sZ) * progress;
      x = (p.startX ?? 0) + gateWeave(localFrame, 3.4) * 0.5;
      y = (p.startY ?? 0) + gateWeave(localFrame, 5.1) * 0.5;
      break;
    }

    case 'parallax-slide': {
      fov = p.baseFov ?? 45;
      const sX = p.startX ?? -2.2;
      const eX = p.endX ?? 2.2;
      const eased = easeInOutCubic(progress);
      x = sX + (eX - sX) * eased;
      y = p.startY ?? 0;
      z = p.startZ ?? 10;
      break;
    }

    case 'whip-pan-snap': {
      fov = p.baseFov ?? 42;
      const trigger = p.whipTriggerFrame ?? Math.floor(config.durationInFrames * 0.5);
      const whipDuration = 9; // 9 frames at 60fps = 150ms snap
      const sX = p.startX ?? 0;
      const eX = p.endX ?? 6.5;

      if (localFrame < trigger) {
        x = sX + gateWeave(localFrame, 1.0);
      } else if (localFrame <= trigger + whipDuration) {
        const whipT = (localFrame - trigger) / whipDuration;
        // Add slight mechanical overshoot on the final frame of the whip
        const overshoot = Math.sin(whipT * Math.PI) * 0.12;
        x = sX + (eX - sX) * easeWhipSnap(whipT) + overshoot;
      } else {
        const settleFrames = localFrame - (trigger + whipDuration);
        const damped = Math.exp(-settleFrames * 0.45) * Math.cos(settleFrames * 1.8) * 0.08;
        x = eX + damped + gateWeave(localFrame, 2.0);
      }
      break;
    }

    case 'vertigo-creep': {
      const sZ = p.startZ ?? 7.5;
      const eZ = p.endZ ?? 14.5;
      const startFov = p.baseFov ?? 52;

      // Calculate locked frustum width at Z=0 reference plane
      const halfFovRad = THREE.MathUtils.degToRad(startFov / 2);
      const lockedWidth = 2 * sZ * Math.tan(halfFovRad);

      const eased = easeInOutCubic(progress);
      z = sZ + (eZ - sZ) * eased;
      // Recompute FOV so Z=0 plane scale stays completely frozen while background warps
      fov = THREE.MathUtils.radToDeg(2 * Math.atan(lockedWidth / (2 * z)));
      break;
    }

    case 'pedestal-reveal': {
      fov = p.baseFov ?? 38;
      const sY = p.startY ?? -3.5;
      const eY = p.endY ?? 0;
      y = sY + (eY - sY) * easeInOutCubic(progress);
      break;
    }
  }

  return {
    position: [x, y, z],
    lookAt: [x, y, 0], // Strictly parallel camera plane for authentic 2.5D diorama look
    fov,
    rollRad,
  };
}

/**
 * Utility to compute exact mesh scale for a 2D cutout placed at `layerZ`
 * so its visual size matches the Z=0 reference plane from `cameraDefaultZ`.
 */
export function getFrustumCompensationScale(
  layerZ: number,
  cameraDefaultZ = 10,
  referenceZ = 0
): number {
  return (cameraDefaultZ - layerZ) / (cameraDefaultZ - referenceZ);
}
