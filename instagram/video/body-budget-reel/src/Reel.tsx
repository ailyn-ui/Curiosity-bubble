import React from "react";
import {
  AbsoluteFill,
  Easing,
  Img,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { TransitionSeries, linearTiming } from "@remotion/transitions";
import { fade } from "@remotion/transitions/fade";
import { FADE, SCENES, Scene, sceneFrames } from "./script";
import { INK, PAPER, PINK, SAFE } from "./theme";

const DIRS = { left: "to right", right: "to left", top: "to bottom", bottom: "to top" } as const;

// The ink paints in along a soft-edged mask, then breathes slowly.
const Ink: React.FC<{ scene: Scene; dur: number }> = ({ scene, dur }) => {
  const frame = useCurrentFrame();
  const p = interpolate(frame, [0, 26], [0, 1], {
    extrapolateRight: "clamp",
    easing: Easing.bezier(0.33, 0, 0.2, 1),
  });
  const edge = p * 130 - 15;
  const mask = `linear-gradient(${DIRS[scene.from]}, black ${edge - 15}%, transparent ${edge + 15}%)`;
  const scale = interpolate(frame, [0, dur], [1.06, 1.0]);
  const drift = interpolate(frame, [0, dur], [10, -10]);
  return (
    <div
      style={{
        position: "absolute",
        top: SAFE.top - 40,
        left: 140,
        right: 140,
        height: 760,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        transform: `translateY(${drift}px) scale(${scale})`,
      }}
    >
      <Img
        src={staticFile(`elements/${scene.element}.png`)}
        style={{
          maxWidth: "100%",
          maxHeight: "100%",
          objectFit: "contain",
          WebkitMaskImage: mask,
          maskImage: mask,
        }}
      />
    </div>
  );
};

const Big: React.FC<{ text: string; pink?: string; delay: number }> = ({ text, pink, delay }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const ws = text.split(" ");
  return (
    <div
      style={{
        fontFamily: "Playfair, serif",
        fontWeight: 900,
        fontSize: ws.length > 6 ? 70 : 84,
        lineHeight: 1.08,
        textTransform: "uppercase",
        color: INK,
      }}
    >
      {ws.map((w, i) => {
        const s = spring({ frame: frame - delay - i * 2, fps, config: { damping: 200 } });
        const isPink = pink && w.toLowerCase().replace(/[^a-z']/g, "") === pink.toLowerCase();
        return (
          <span
            key={i}
            style={{
              display: "inline-block",
              marginRight: "0.25em",
              opacity: s,
              transform: `translateY(${interpolate(s, [0, 1], [24, 0])}px)`,
              color: isPink ? PINK : INK,
            }}
          >
            {w}
          </span>
        );
      })}
    </div>
  );
};

const Small: React.FC<{ text: string; delay: number; byline?: boolean; solo?: boolean }> = ({ text, delay, byline, solo }) => {
  const frame = useCurrentFrame();
  const o = interpolate(frame, [delay, delay + 12], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  return (
    <div
      style={{
        fontFamily: "Playfair, serif",
        fontWeight: byline ? 700 : 400,
        fontSize: byline ? 40 : solo ? 64 : 52,
        letterSpacing: byline ? "0.18em" : 0,
        textTransform: byline ? "uppercase" : "none",
        lineHeight: 1.3,
        color: byline ? PINK : INK,
        opacity: o,
        transform: `translateY(${interpolate(o, [0, 1], [14, 0])}px)`,
      }}
    >
      {text}
    </div>
  );
};

const SceneView: React.FC<{ scene: Scene; dur: number; last: boolean }> = ({ scene, dur, last }) => {
  const frame = useCurrentFrame();
  const bar = interpolate(frame, [8, 22], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const smallFirst = scene.element === "palm";
  const bigDelay = smallFirst ? 18 : 10;
  const smallDelay = smallFirst ? 8 : scene.big ? 10 + scene.big.split(" ").length * 2 + 8 : 10;
  return (
    <AbsoluteFill style={{ backgroundColor: PAPER }}>
      <Ink scene={scene} dur={dur} />
      <div
        style={{
          position: "absolute",
          top: 1060,
          left: SAFE.left,
          right: SAFE.right - 60,
          bottom: SAFE.bottom - 80,
          display: "flex",
          flexDirection: "column",
          justifyContent: "flex-start",
        }}
      >
        <div style={{ position: "relative", display: "flex", flexDirection: "column", gap: 28, paddingLeft: 32 }}>
          <div
            style={{
              position: "absolute",
              left: 0,
              top: 4,
              bottom: 4,
              width: 10,
              backgroundColor: PINK,
              transformOrigin: "top",
              transform: `scaleY(${bar})`,
            }}
          />
          {smallFirst && scene.small ? <Small text={scene.small} delay={smallDelay} /> : null}
          {scene.big ? <Big text={scene.big} pink={scene.pink} delay={bigDelay} /> : null}
          {!smallFirst && scene.small ? (
            <Small text={scene.small} delay={smallDelay} byline={last} solo={!scene.big} />
          ) : null}
        </div>
      </div>
    </AbsoluteFill>
  );
};

export const Reel: React.FC = () => (
  <AbsoluteFill style={{ backgroundColor: PAPER }}>
    <TransitionSeries>
      {SCENES.map((s, i) => {
        const dur = sceneFrames(s);
        return (
          <React.Fragment key={s.element}>
            <TransitionSeries.Sequence durationInFrames={dur}>
              <SceneView scene={s} dur={dur} last={i === SCENES.length - 1} />
            </TransitionSeries.Sequence>
            {i < SCENES.length - 1 ? (
              <TransitionSeries.Transition presentation={fade()} timing={linearTiming({ durationInFrames: FADE })} />
            ) : null}
          </React.Fragment>
        );
      })}
    </TransitionSeries>
  </AbsoluteFill>
);
