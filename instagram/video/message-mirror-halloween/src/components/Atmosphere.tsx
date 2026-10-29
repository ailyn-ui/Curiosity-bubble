import React from "react";
import { AbsoluteFill, useCurrentFrame } from "remotion";

// Deterministic candle flicker: a few incommensurate sines.
export const flicker = (frame: number) =>
  0.82 +
  0.1 * Math.sin(frame * 0.9) +
  0.05 * Math.sin(frame * 2.3 + 1) +
  0.03 * Math.sin(frame * 5.1 + 2);

export const DarkRoom: React.FC = () => {
  const frame = useCurrentFrame();
  const f = flicker(frame);
  return (
    <AbsoluteFill style={{ backgroundColor: "#050404" }}>
      <AbsoluteFill
        style={{
          background: `radial-gradient(ellipse 70% 45% at 50% 62%, rgba(255,150,60,${0.28 * f}) 0%, rgba(120,40,10,${0.12 * f}) 45%, rgba(0,0,0,0) 75%)`,
        }}
      />
      <AbsoluteFill
        style={{
          background:
            "radial-gradient(ellipse 90% 70% at 50% 50%, rgba(0,0,0,0) 55%, rgba(0,0,0,0.85) 100%)",
        }}
      />
      <Candle x={70} y={1500} scale={1} phase={0} />
      <Candle x={1000} y={1530} scale={0.8} phase={3} />
      <Cobweb />
    </AbsoluteFill>
  );
};

const Candle: React.FC<{ x: number; y: number; scale: number; phase: number }> = ({
  x,
  y,
  scale,
  phase,
}) => {
  const frame = useCurrentFrame();
  const f = flicker(frame + phase * 7);
  const sway = Math.sin((frame + phase * 10) * 0.35) * 4;
  return (
    <div
      style={{
        position: "absolute",
        left: x - 40 * scale,
        top: y - 140 * scale,
        width: 80 * scale,
        height: 260 * scale,
      }}
    >
      <div
        style={{
          position: "absolute",
          left: "50%",
          top: 0,
          width: 120 * scale,
          height: 120 * scale,
          marginLeft: -60 * scale,
          borderRadius: "50%",
          background: `radial-gradient(circle, rgba(255,200,120,${0.55 * f}) 0%, rgba(255,140,40,0) 70%)`,
        }}
      />
      <div
        style={{
          position: "absolute",
          left: "50%",
          top: 30 * scale,
          width: 22 * scale,
          height: 46 * scale,
          marginLeft: -11 * scale,
          borderRadius: "50% 50% 50% 50% / 65% 65% 35% 35%",
          background: "linear-gradient(#fff6d0, #ffb347 60%, #ff7a1a)",
          transform: `translateX(${sway}px) scaleY(${0.9 + 0.15 * f})`,
          transformOrigin: "bottom center",
        }}
      />
      <div
        style={{
          position: "absolute",
          left: "50%",
          top: 80 * scale,
          width: 50 * scale,
          height: 170 * scale,
          marginLeft: -25 * scale,
          borderRadius: 6 * scale,
          background: "linear-gradient(90deg, #d9d2c4, #f4efe4 45%, #b8ae9c)",
        }}
      />
    </div>
  );
};

const Cobweb: React.FC = () => (
  <svg
    width={260}
    height={260}
    viewBox="0 0 100 100"
    style={{ position: "absolute", left: 0, top: 0, opacity: 0.35 }}
  >
    <g stroke="#ddd" strokeWidth={0.5} fill="none">
      {[0, 22, 45, 68, 90].map((a) => {
        const r = (a * Math.PI) / 180;
        return <line key={a} x1={0} y1={0} x2={100 * Math.cos(r)} y2={100 * Math.sin(r)} />;
      })}
      {[25, 45, 65, 85].map((d) => (
        <path key={d} d={`M ${d} 0 Q ${d * 0.75} ${d * 0.3} ${d * 0.7} ${d * 0.7} Q ${d * 0.3} ${d * 0.75} 0 ${d}`} />
      ))}
    </g>
  </svg>
);

export const Bats: React.FC = () => {
  const frame = useCurrentFrame();
  const bats = [
    { start: -200, y: 320, speed: 13, size: 70, delay: 0 },
    { start: -500, y: 420, speed: 10, size: 50, delay: 8 },
    { start: -900, y: 260, speed: 15, size: 40, delay: 4 },
  ];
  return (
    <AbsoluteFill>
      {bats.map((b, i) => {
        const x = b.start + (frame + b.delay) * b.speed;
        const y = b.y + Math.sin((frame + i * 9) * 0.25) * 30;
        const flap = Math.abs(Math.sin((frame + i * 3) * 0.8));
        return (
          <svg
            key={i}
            width={b.size}
            height={b.size * 0.5}
            viewBox="0 0 100 50"
            style={{ position: "absolute", left: x, top: y, opacity: 0.85 }}
          >
            <path
              d={`M50 20 C 40 ${10 - flap * 10}, 20 ${5 - flap * 5}, 0 ${15 + flap * 10} C 15 22, 25 30, 35 28 C 40 35, 45 32, 50 38 C 55 32, 60 35, 65 28 C 75 30, 85 22, 100 ${15 + flap * 10} C 80 ${5 - flap * 5}, 60 ${10 - flap * 10}, 50 20 Z`}
              fill="#000"
              stroke="#3a2a2a"
              strokeWidth={1}
            />
          </svg>
        );
      })}
    </AbsoluteFill>
  );
};

export const Fog: React.FC<{ opacity?: number }> = ({ opacity = 1 }) => {
  const frame = useCurrentFrame();
  const a = Math.sin(frame * 0.05) * 20;
  const b = Math.cos(frame * 0.04) * 25;
  return (
    <AbsoluteFill
      style={{
        opacity,
        background: `radial-gradient(ellipse 60% 30% at ${40 + a * 0.5}% ${60 + b * 0.3}%, rgba(200,200,220,0.25), rgba(0,0,0,0) 70%), radial-gradient(ellipse 50% 25% at ${60 - b * 0.4}% ${40 + a * 0.3}%, rgba(180,180,200,0.2), rgba(0,0,0,0) 70%)`,
      }}
    />
  );
};
