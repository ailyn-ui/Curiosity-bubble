import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { PINK, SAFE, SERIF } from "../theme";

export type Word = { text: string; pink?: boolean };

// Headline in the brand style: bold serif capitals, pink bar on the left,
// one highlighted word in pink. Lines rise in one after another.
export const Headline: React.FC<{
  lines: Word[][];
  color: string;
  top?: number;
  size?: number;
}> = ({ lines, color, top = SAFE.top + 10, size = 96 }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return (
    <div
      style={{
        position: "absolute",
        top,
        left: SAFE.left,
        right: SAFE.right,
        borderLeft: `12px solid ${PINK}`,
        paddingLeft: 32,
        fontFamily: "Playfair, serif",
        fontWeight: 900,
        fontSize: size,
        lineHeight: 1.05,
        color,
        textTransform: "uppercase",
      }}
    >
      {lines.map((line, i) => {
        const p = spring({ frame: frame - i * 5, fps, config: { damping: 200 } });
        return (
          <div
            key={i}
            style={{
              opacity: p,
              transform: `translateY(${interpolate(p, [0, 1], [40, 0])}px)`,
            }}
          >
            {line.map((w, j) => (
              <span key={j} style={{ color: w.pink ? PINK : color }}>
                {w.text}
                {j < line.length - 1 ? " " : ""}
              </span>
            ))}
          </div>
        );
      })}
    </div>
  );
};

// Burned-in subtitle for the spoken line, for people watching muted.
export const Subtitle: React.FC<{ text: string; dark: boolean }> = ({ text, dark }) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 6], [0, 1], { extrapolateRight: "clamp" });
  return (
    <div
      style={{
        position: "absolute",
        top: 1420 - 110,
        left: SAFE.left,
        right: SAFE.right,
        display: "flex",
        justifyContent: "center",
        opacity,
      }}
    >
      <div
        style={{
          fontFamily: `${SERIF}, serif`,
          fontWeight: 700,
          fontSize: 44,
          lineHeight: 1.25,
          textAlign: "center",
          color: dark ? "#fff" : "#0B0B0B",
          background: dark ? "rgba(0,0,0,0.8)" : "rgba(255,255,255,0.95)",
          padding: "12px 24px",
          borderRadius: 14,
        }}
      >
        {text}
      </div>
    </div>
  );
};

export const Card: React.FC<{
  text: string;
  style?: React.CSSProperties;
  textStyle?: React.CSSProperties;
}> = ({ text, style, textStyle }) => (
  <div
    style={{
      position: "absolute",
      background: "#fbf8f1",
      borderRadius: 10,
      padding: "26px 30px",
      boxShadow: "0 18px 40px rgba(0,0,0,0.5)",
      ...style,
    }}
  >
    <div
      style={{
        fontFamily: `${SERIF}, serif`,
        fontWeight: 700,
        fontSize: 42,
        color: "#0B0B0B",
        whiteSpace: "nowrap",
        ...textStyle,
      }}
    >
      {text}
    </div>
  </div>
);

export const Pumpkin: React.FC<{ size: number }> = ({ size }) => (
  <svg width={size} height={size} viewBox="0 0 100 100" style={{ display: "inline-block", verticalAlign: "middle" }}>
    <path d="M50 22 C 48 12, 54 6, 60 4" stroke="#2f5d1e" strokeWidth={6} fill="none" strokeLinecap="round" />
    <ellipse cx={30} cy={60} rx={22} ry={30} fill="#e8670c" />
    <ellipse cx={70} cy={60} rx={22} ry={30} fill="#e8670c" />
    <ellipse cx={50} cy={60} rx={24} ry={33} fill="#ff7f1a" />
    <path d="M36 52 L44 44 L46 56 Z M64 52 L56 44 L54 56 Z" fill="#2a1200" />
    <path d="M32 68 Q50 84 68 68 L62 70 L58 66 L54 72 L50 67 L46 72 L42 66 L38 70 Z" fill="#2a1200" />
  </svg>
);
