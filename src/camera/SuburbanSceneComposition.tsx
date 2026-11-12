import React from 'react';
import { useVideoConfig } from 'remotion';
import { ThreeCanvas } from '@remotion/three';
import { KnoxCameraRig, type CameraShotSegment } from './KnoxCameraRig';
import { ParallaxStage25D, type StageLayerSpec } from './ParallaxStage25D';
import sceneData from '../../examples/scene-shotlist.json';

export const SuburbanSceneComposition: React.FC = () => {
  const { width, height } = useVideoConfig();

  return (
    <ThreeCanvas
      width={width}
      height={height}
      gl={{ antialias: true, alpha: false }}
    >
      <color attach="background" args={['#d8d2c5']} />
      <KnoxCameraRig shots={sceneData.shots as CameraShotSegment[]}>
        <ParallaxStage25D
          layers={sceneData.layers as StageLayerSpec[]}
          referenceCameraZ={5.0}
        />
      </KnoxCameraRig>
    </ThreeCanvas>
  );
};
