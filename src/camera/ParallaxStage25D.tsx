import React, { useEffect, useMemo, useRef, useState } from 'react';
import { continueRender, delayRender, staticFile, useCurrentFrame } from 'remotion';
import { useFrame, useThree } from '@react-three/fiber';
import * as THREE from 'three';

/**
 * 1. Canonical 5-Plane Z-Depth Bucket Spec
 * Reference Camera sits at Z = +5.0 looking toward -Z.
 * Reference Subject Plane sits at Z = 0.0 (Scale Multiplier = 1.00x).
 */
export const Z_DEPTH_BUCKETS = {
  FG_EXTREME: { z: 3.5, defaultScale: 0.30, overscan: 1.35 },
  MID_SUBJECT: { z: 0.0, defaultScale: 1.00, overscan: 1.15 },
  MID_ENV: { z: -4.0, defaultScale: 1.80, overscan: 1.25 },
  BG_NEAR: { z: -10.0, defaultScale: 3.00, overscan: 1.50 },
  BG_SKY: { z: -25.0, defaultScale: 6.00, overscan: 2.20 },
} as const;

export type DepthBucketKey = keyof typeof Z_DEPTH_BUCKETS;

/**
 * 2. Declarative JSON Layer Schema
 */
export interface StageLayerSpec {
  id: string;
  /** Path relative to public/ (e.g., "animated-shorts/v1/art/char_inspector.png") or full URL */
  textureUrl: string;
  depthBucket: DepthBucketKey;
  /** Fine Z offset relative to the bucket's base Z plane (prevents Z-fighting within same bucket) */
  zOffset?: number;
  /**
   * [X, Y] position in world meters as composed at the Z=0 reference plane.
   * Y=0 represents the ground floor; if anchorBottom is true (default), the plane's bottom edge sits at Y.
   */
  position?: [number, number];
  /** Uncompensated height in world meters at Z=0 reference plane (default: 2.0) */
  baseHeight?: number;
  /** Width / Height aspect ratio. If omitted, auto-detected from the loaded PNG dimensions */
  aspectRatio?: number;
  /** Automatically compensates scale and X/Y screen-space alignment across Z-depth (default: true) */
  autoFrustumScale?: boolean;
  /** Rotates plane around vertical Y-axis to face camera during wide pans/trucks (default: false) */
  cylindricalBillboard?: boolean;
  /** Anchors the bottom of the PNG cut-out to position[1] instead of its center (default: true) */
  anchorBottom?: boolean;
  /** Flip PNG horizontally (useful for reusing character pose assets) */
  flipX?: boolean;
  /** Opacity [0..1] (default: 1.0) */
  opacity?: number;
  /** Optional subtle stepped stop-motion idle bobbing for characters */
  idleBob?: {
    enabled: boolean;
    amplitudeY?: number;
    frequencyHz?: number;
  };
}

export interface ParallaxStage25DProps {
  layers: StageLayerSpec[];
  /** Reference camera Z distance used for 1:1 frustum scale compensation (default: 5.0) */
  referenceCameraZ?: number;
  /** Reference focal plane Z (default: 0.0) */
  referencePlaneZ?: number;
  /** Alpha cutout threshold for crisp retro edges without depth-sorting halos (default: 0.05) */
  alphaTest?: number;
}

/**
 * 3. Core Mathematical Helpers
 * S(z) = |Z_cam - z| / |Z_cam - Z_ref|
 */
export function computeFrustumScaleFactor(
  layerZ: number,
  cameraZ: number = 5.0,
  referenceZ: number = 0.0
): number {
  const refDistance = Math.abs(cameraZ - referenceZ);
  if (refDistance < 1e-5) return 1.0;
  const layerDistance = Math.abs(cameraZ - layerZ);
  return layerDistance / refDistance;
}

export function computeCylindricalBillboardY(
  planeWorldPos: THREE.Vector3,
  cameraWorldPos: THREE.Vector3
): number {
  const dx = cameraWorldPos.x - planeWorldPos.x;
  const dz = cameraWorldPos.z - planeWorldPos.z;
  return Math.atan2(dx, dz);
}

/**
 * Resolver for Remotion public/ paths vs external URLs
 */
function resolveAssetPath(url: string): string {
  if (url.startsWith('http://') || url.startsWith('https://') || url.startsWith('data:')) {
    return url;
  }
  const cleanPath = url.startsWith('/') ? url.slice(1) : url;
  try {
    return staticFile(cleanPath);
  } catch {
    return url;
  }
}

/**
 * 4. Individual 2.5D Plane Sub-Component
 */
interface CutoutPlaneProps {
  layer: StageLayerSpec;
  texture: THREE.Texture;
  referenceCameraZ: number;
  referencePlaneZ: number;
  alphaTest: number;
}

const CutoutPlane: React.FC<CutoutPlaneProps> = ({
  layer,
  texture,
  referenceCameraZ,
  referencePlaneZ,
  alphaTest,
}) => {
  const meshRef = useRef<THREE.Mesh>(null);
  const frame = useCurrentFrame();
  const { camera } = useThree();

  // Compute exact Z position and frustum scale factor
  const bucket = Z_DEPTH_BUCKETS[layer.depthBucket];
  const finalZ = bucket.z + (layer.zOffset ?? 0);

  const scaleFactor =
    layer.autoFrustumScale !== false
      ? computeFrustumScaleFactor(finalZ, referenceCameraZ, referencePlaneZ)
      : 1.0;

  // Auto-detect aspect ratio from loaded PNG if not explicitly set in JSON
  const img = texture.image as HTMLImageElement | undefined;
  const detectedAspect =
    img && img.width && img.height ? img.width / img.height : 1.0;
  const aspect = layer.aspectRatio ?? detectedAspect;

  const baseHeight = layer.baseHeight ?? 2.0;
  const compensatedHeight = baseHeight * scaleFactor;
  const compensatedWidth = baseHeight * aspect * scaleFactor;

  const [rawX, rawY] = layer.position ?? [0, 0];
  const anchorBottom = layer.anchorBottom !== false;

  // Deterministic stepped idle bobbing (quantized to 12fps steps at 60fps for stop-motion feel)
  let bobOffsetY = 0;
  if (layer.idleBob?.enabled) {
    const steppedFrame = Math.floor(frame / 5) * 5;
    const freq = layer.idleBob.frequencyHz ?? 1.5;
    const amp = layer.idleBob.amplitudeY ?? 0.015;
    bobOffsetY = Math.sin((steppedFrame / 60) * freq * Math.PI * 2) * amp;
  }

  // Compensate X & Y so an asset placed at [x, y] stays in the exact same screen-space
  // quadrant from the reference camera viewpoint regardless of which Z bucket it is dropped into.
  const worldX = rawX * scaleFactor;
  const worldY =
    (rawY + bobOffsetY) * scaleFactor +
    (anchorBottom ? compensatedHeight * 0.5 : 0);

  // Clone texture adjustments if horizontal flip is requested
  const configuredTexture = useMemo(() => {
    const tex = texture.clone();
    tex.colorSpace = THREE.SRGBColorSpace;
    tex.minFilter = THREE.LinearFilter;
    tex.magFilter = THREE.LinearFilter;
    if (layer.flipX) {
      tex.wrapS = THREE.RepeatWrapping;
      tex.repeat.x = -1;
      tex.offset.x = 1;
    }
    tex.needsUpdate = true;
    return tex;
  }, [texture, layer.flipX]);

  // Apply Cylindrical Y-Axis Billboarding on every frame render if enabled
  useFrame(() => {
    if (!meshRef.current) return;
    if (layer.cylindricalBillboard) {
      const camPos = new THREE.Vector3();
      camera.getWorldPosition(camPos);
      const planePos = new THREE.Vector3(worldX, worldY, finalZ);
      meshRef.current.rotation.y = computeCylindricalBillboardY(planePos, camPos);
    } else {
      meshRef.current.rotation.y = 0;
    }
  });

  return (
    <mesh
      ref={meshRef}
      name={`layer-${layer.id}`}
      position={[worldX, worldY, finalZ]}
      renderOrder={Math.round((finalZ + 50) * 10)}
    >
      <planeGeometry args={[compensatedWidth, compensatedHeight]} />
      <meshBasicMaterial
        map={configuredTexture}
        transparent={true}
        opacity={layer.opacity ?? 1.0}
        alphaTest={alphaTest}
        side={THREE.DoubleSide}
        depthWrite={true}
      />
    </mesh>
  );
};

/**
 * 5. Main Drop-In Component: ParallaxStage25D
 * Blocks Remotion frame capture until every PNG layer texture is loaded in memory.
 */
export const ParallaxStage25D: React.FC<ParallaxStage25DProps> = ({
  layers,
  referenceCameraZ = 5.0,
  referencePlaneZ = 0.0,
  alphaTest = 0.05,
}) => {
  const [texturesMap, setTexturesMap] = useState<Record<string, THREE.Texture>>({});
  const [handle] = useState(() =>
    delayRender(`Loading ${layers.length} 2.5D PNG layers for ParallaxStage25D`)
  );

  useEffect(() => {
    let isMounted = true;
    const loader = new THREE.TextureLoader();

    Promise.all(
      layers.map(
        (layer) =>
          new Promise<[string, THREE.Texture]>((resolve, reject) => {
            const resolvedUrl = resolveAssetPath(layer.textureUrl);
            loader.load(
              resolvedUrl,
              (tex) => resolve([layer.id, tex]),
              undefined,
              (err) =>
                reject(
                  new Error(
                    `Failed to load layer "${layer.id}" (${resolvedUrl}): ${err}`
                  )
                )
            );
          })
      )
    )
      .then((entries) => {
        if (!isMounted) return;
        setTexturesMap(Object.fromEntries(entries));
        continueRender(handle);
      })
      .catch((err) => {
        console.error(err);
        if (isMounted) continueRender(handle);
      });

    return () => {
      isMounted = false;
    };
  }, [layers, handle]);

  // Do not mount meshes until all PNGs are ready so Remotion never renders blank white planes
  if (Object.keys(texturesMap).length < layers.length) {
    return null;
  }

  return (
    <group name="ParallaxStage25D">
      {layers.map((layer) => {
        const tex = texturesMap[layer.id];
        if (!tex) return null;
        return (
          <CutoutPlane
            key={layer.id}
            layer={layer}
            texture={tex}
            referenceCameraZ={referenceCameraZ}
            referencePlaneZ={referencePlaneZ}
            alphaTest={alphaTest}
          />
        );
      })}
    </group>
  );
};
