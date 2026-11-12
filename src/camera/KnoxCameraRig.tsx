import React, { useMemo, useRef } from 'react';
import { useCurrentFrame, useVideoConfig } from 'remotion';
import { useFrame, useThree } from '@react-three/fiber';
import * as THREE from 'three';
import {
  evaluateCameraRig,
  type CameraPresetType,
  type CameraShotConfig,
} from './cameraPresets';

/**
 * Shot segment used by KnoxCameraRig / declarative scene JSON.
 * Maps cleanly onto CameraShotConfig.
 */
export interface CameraShotSegment {
  id?: string;
  preset: CameraPresetType;
  startFrame: number;
  durationInFrames: number;
  params?: CameraShotConfig['params'];
}

export interface KnoxCameraRigProps {
  shots: CameraShotSegment[];
  children?: React.ReactNode;
  /** Default FOV when a shot does not specify baseFov */
  defaultFov?: number;
}

/**
 * Two-node camera hierarchy for 2.5D deadpan / uncanny cinema:
 * - Track node: world translation + look-at
 * - Body node: PerspectiveCamera (FOV, Dutch roll)
 *
 * Never animates the PerspectiveCamera in world space directly.
 * Drives from evaluateCameraRig() so motion stays frame-accurate and deterministic.
 */
export const KnoxCameraRig: React.FC<KnoxCameraRigProps> = ({
  shots,
  children,
  defaultFov = 38,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const { set } = useThree();

  const trackRef = useRef<THREE.Group>(null);
  const bodyRef = useRef<THREE.PerspectiveCamera>(null);

  // Pick the active shot for the current frame (last matching startFrame wins)
  const activeConfig: CameraShotConfig = useMemo(() => {
    let active: CameraShotSegment | undefined;
    for (const shot of shots) {
      if (frame >= shot.startFrame) {
        active = shot;
      }
    }
    if (!active && shots.length > 0) {
      active = shots[0];
    }
    if (!active) {
      return {
        preset: 'deadpan-lock',
        startFrame: 0,
        durationInFrames: 1,
        fps,
        params: { baseFov: defaultFov },
      };
    }
    return {
      preset: active.preset,
      startFrame: active.startFrame,
      durationInFrames: active.durationInFrames,
      fps,
      params: {
        baseFov: defaultFov,
        ...active.params,
      },
    };
  }, [shots, frame, fps, defaultFov]);

  // Register this camera as the R3F default so materials / useThree().camera work
  React.useLayoutEffect(() => {
    if (bodyRef.current) {
      set({ camera: bodyRef.current });
    }
  }, [set]);

  useFrame(() => {
    const track = trackRef.current;
    const body = bodyRef.current;
    if (!track || !body) return;

    const state = evaluateCameraRig(frame, activeConfig);

    track.position.set(state.position[0], state.position[1], state.position[2]);
    track.lookAt(state.lookAt[0], state.lookAt[1], state.lookAt[2]);

    body.fov = state.fov;
    body.rotation.z = state.rollRad;
    body.updateProjectionMatrix();
  });

  return (
    <group name="KnoxCameraTrack" ref={trackRef}>
      <perspectiveCamera
        ref={bodyRef}
        name="KnoxCameraBody"
        makeDefault
        fov={defaultFov}
        near={0.1}
        far={200}
      />
      {children}
    </group>
  );
};
