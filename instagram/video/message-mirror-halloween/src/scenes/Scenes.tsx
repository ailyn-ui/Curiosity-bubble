import React from "react";
import {
  AbsoluteFill,
  Img,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { Bats, DarkRoom, Fog } from "../components/Atmosphere";
import { MIRROR, Mirror } from "../components/Mirror";
import { Card, Headline, Pumpkin, Subtitle } from "../components/Text";
import { INK, PAPER, PINK, SERIF } from "../theme";

const MIRROR_TOP = 560;
const MIRROR_SCALE = 0.92;
const glassW = MIRROR.width - 52;

const CoverInGlass: React.FC<{ blur: number; opacity: number; scale: number }> = ({
  blur,
  opacity,
  scale,
}) => (
  <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
    <Img
      src={staticFile("cover.png")}
      style={{
        width: glassW * 0.86,
        filter: `blur(${blur}px)`,
        opacity,
        transform: `scale(${scale})`,
        boxShadow: "0 10px 30px rgba(0,0,0,0.25)",
      }}
    />
  </AbsoluteFill>
);

// 1. Hook: "What if it wasn't you?"
export const HookScene: React.FC = () => {
  const frame = useCurrentFrame();
  const push = interpolate(frame, [0, 60], [1, 1.05]);
  const ghost = interpolate(frame, [0, 20, 60], [0, 0.55, 0.35]);
  return (
    <AbsoluteFill>
      <DarkRoom />
      <Mirror variant="haunted" top={MIRROR_TOP} scale={MIRROR_SCALE * push}>
        <Fog />
        <AbsoluteFill style={{ justifyContent: "flex-end", alignItems: "center" }}>
          <Silhouette opacity={ghost} lag={Math.sin(frame * 0.2) * 8} />
        </AbsoluteFill>
      </Mirror>
      <Bats />
      <Headline
        color={PAPER}
        size={84}
        lines={[[{ text: "Mirror, mirror…" }], [{ text: "is it" }, { text: "me?", pink: true }]]}
      />
      <Subtitle dark text="What if it wasn't you?" />
    </AbsoluteFill>
  );
};

const Silhouette: React.FC<{ opacity: number; lag: number }> = ({ opacity, lag }) => (
  <svg
    width={340}
    height={520}
    viewBox="0 0 100 150"
    style={{ opacity, transform: `translateX(${lag}px)`, filter: "blur(2px)" }}
  >
    <ellipse cx={50} cy={38} rx={20} ry={24} fill="#c9d3dd" />
    <path d="M10 150 C 12 95, 30 72, 50 70 C 70 72, 88 95, 90 150 Z" fill="#c9d3dd" />
  </svg>
);

// 2. "Maybe there's a gap"
export const GapScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const crack = interpolate(frame, [8, 40], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const cardIn = spring({ frame: frame - 10, fps, config: { damping: 14 } });
  return (
    <AbsoluteFill>
      <DarkRoom />
      <Mirror variant="haunted" top={MIRROR_TOP} scale={MIRROR_SCALE}>
        <Fog />
        <svg viewBox="0 0 100 140" style={{ position: "absolute", inset: 0, width: "100%", height: "100%" }}>
          <path
            d="M48 0 L52 22 L45 38 L55 58 L47 80 L54 100 L49 140"
            stroke="#e8eef5"
            strokeWidth={0.9}
            fill="none"
            pathLength={1}
            strokeDasharray={1}
            strokeDashoffset={1 - crack}
          />
        </svg>
      </Mirror>
      <Card
        text="Full brand + structure"
        style={{
          left: 90,
          top: 1120,
          transform: `translateX(${interpolate(cardIn, [0, 1], [-500, 0])}px) rotate(-4deg)`,
        }}
      />
      <Bats />
      <Headline color={PAPER} lines={[[{ text: "There's a" }], [{ text: "gap", pink: true }]]} />
      <Subtitle dark text="Maybe there's a gap" />
    </AbsoluteFill>
  );
};

// 3. "between what you say and what is heard."
export const HeardScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const wobble = Math.sin(frame * 0.4);
  const reflIn = spring({ frame: frame - 8, fps, config: { damping: 200 } });
  return (
    <AbsoluteFill>
      <DarkRoom />
      <Mirror variant="haunted" top={MIRROR_TOP} scale={MIRROR_SCALE}>
        <Fog />
        <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
          <div
            style={{
              opacity: reflIn,
              transform: `skewX(${wobble * 8}deg) scale(${0.85 + wobble * 0.04}) rotate(${wobble * 3}deg)`,
              filter: `blur(${1.5 + Math.abs(wobble) * 1.5}px) hue-rotate(60deg)`,
            }}
          >
            <div
              style={{
                background: "#d8e6d0",
                padding: "30px 44px",
                borderRadius: 10,
                fontFamily: `${SERIF}, serif`,
                fontWeight: 900,
                fontSize: 68,
                color: "#3b6b1f",
                textShadow: "0 8px 0 rgba(59,107,31,0.5), 0 16px 2px rgba(59,107,31,0.25)",
                fontStyle: "italic",
              }}
            >
              a logo?
            </div>
          </div>
        </AbsoluteFill>
      </Mirror>
      <Card text="Full brand + structure" style={{ left: 90, top: 1120, transform: "rotate(-4deg)" }} />
      <Bats />
      <Headline
        color={PAPER}
        size={84}
        lines={[[{ text: "What you say" }], [{ text: "≠", pink: true }, { text: "what" }], [{ text: "they hear" }]]}
      />
      <Subtitle dark text="between what you say and what is heard." />
    </AbsoluteFill>
  );
};

// 4. "So I made The Message Mirror."
export const RevealScene: React.FC = () => {
  const frame = useCurrentFrame();
  const clear = interpolate(frame, [6, 40], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const shimmer = interpolate(frame, [0, 30], [-60, 160]);
  return (
    <AbsoluteFill>
      <DarkRoom />
      <Mirror variant="haunted" top={MIRROR_TOP - 180} scale={1.05}>
        <Fog opacity={1 - clear} />
        <CoverInGlass blur={interpolate(clear, [0, 1], [24, 0])} opacity={clear} scale={0.95 + clear * 0.05} />
        <AbsoluteFill
          style={{
            background: `linear-gradient(115deg, rgba(255,255,255,0) ${shimmer - 20}%, rgba(255,240,200,0.55) ${shimmer}%, rgba(255,255,255,0) ${shimmer + 20}%)`,
          }}
        />
      </Mirror>
      <Subtitle dark text="So I made The Message Mirror." />
    </AbsoluteFill>
  );
};

// 5. "A quick tool to get clear." Lights on.
export const ClarityScene: React.FC = () => {
  const frame = useCurrentFrame();
  const flash = interpolate(frame, [0, 10], [0.9, 0], { extrapolateRight: "clamp" });
  return (
    <AbsoluteFill style={{ backgroundColor: PAPER }}>
      <Mirror variant="clean" top={MIRROR_TOP} scale={MIRROR_SCALE}>
        <CoverInGlass blur={0} opacity={1} scale={1} />
      </Mirror>
      <Headline color={INK} lines={[[{ text: "A tool for" }], [{ text: "clarity", pink: true }]]} />
      <Subtitle dark={false} text="A quick tool to get clear." />
      <AbsoluteFill style={{ backgroundColor: "#fff", opacity: flash }} />
    </AbsoluteFill>
  );
};

// 6. "Comment 'mirror.'"
export const CtaScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const bounce = Math.abs(Math.sin(frame * 0.25)) * 26;
  const pop = spring({ frame: frame - 6, fps, config: { damping: 10 } });
  return (
    <AbsoluteFill style={{ backgroundColor: PAPER }}>
      <Mirror variant="clean" top={MIRROR_TOP + 40} scale={0.78}>
        <CoverInGlass blur={0} opacity={1} scale={1} />
      </Mirror>
      <Headline
        color={INK}
        lines={[[{ text: "Comment" }], [{ text: "“mirror”", pink: true }]]}
      />
      <div style={{ position: "absolute", left: 640, top: 380, transform: `scale(${pop})` }}>
        <Pumpkin size={150} />
      </div>
      <svg
        width={90}
        height={120}
        viewBox="0 0 30 40"
        style={{ position: "absolute", left: 790, top: 1160 + bounce }}
      >
        <path d="M15 0 V30 M4 20 L15 34 L26 20" stroke={PINK} strokeWidth={4} fill="none" strokeLinecap="round" strokeLinejoin="round" />
      </svg>
      <Subtitle dark={false} text="Comment “mirror.”" />
    </AbsoluteFill>
  );
};
