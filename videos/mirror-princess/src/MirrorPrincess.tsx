import React from "react";
import {
  AbsoluteFill,
  Easing,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { loadFont } from "@remotion/google-fonts/Caveat";

const { fontFamily } = loadFont("normal", { weights: ["700"], subsets: ["latin"] });

const INK = "#1d1d1f";
const GOLD = "#e0a922";
const PINK = "#f7a1c4";
const PAPER = "#f5f1e8";

// Scene timing, in frames at 30fps
const T = {
  ground: 0,
  mirror: 15,
  walkStart: 40,
  walkEnd: 130,
  textOneDay: 120,
  reflection: 160,
  magic: 205,
  princess: 215,
  castle: 225,
  rainbow: 260,
  likes: 290,
  girlCrown: 375,
  textEnd: 395,
};

const easeOut = Easing.bezier(0.33, 1, 0.68, 1);

const progress = (frame: number, start: number, dur: number) =>
  interpolate(frame, [start, start + dur], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: easeOut,
  });

const usePop = (start: number, damping = 11) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return spring({ frame: frame - start, fps, config: { damping } });
};

const ellipsePath = (cx: number, cy: number, rx: number, ry: number) =>
  `M ${cx - rx} ${cy} A ${rx} ${ry} 0 1 1 ${cx + rx} ${cy} A ${rx} ${ry} 0 1 1 ${cx - rx} ${cy}`;

const starPath = (r: number, inner = 0.45, points = 5) => {
  let d = "";
  for (let i = 0; i < points * 2; i++) {
    const rad = i % 2 === 0 ? r : r * inner;
    const a = (Math.PI / points) * i - Math.PI / 2;
    d += `${i === 0 ? "M" : "L"} ${Math.cos(a) * rad} ${Math.sin(a) * rad} `;
  }
  return d + "Z";
};

const SPARKLE = "M 0 -1 Q 0.12 -0.12 1 0 Q 0.12 0.12 0 1 Q -0.12 0.12 -1 0 Q -0.12 -0.12 0 -1 Z";

/** A stroke that draws itself on, optionally filling in once drawn. */
const Draw: React.FC<{
  d: string;
  start: number;
  dur: number;
  stroke?: string;
  width?: number;
  fill?: string;
  opacity?: number;
}> = ({ d, start, dur, stroke = INK, width = 6, fill, opacity = 1 }) => {
  const frame = useCurrentFrame();
  const p = progress(frame, start, dur);
  const fillOpacity = progress(frame, start + dur * 0.7, dur * 0.5);
  return (
    <g opacity={opacity}>
      {fill ? <path d={d} fill={fill} opacity={fillOpacity} /> : null}
      <path
        d={d}
        pathLength={1}
        strokeDasharray="1 1"
        strokeDashoffset={1 - p}
        fill="none"
        stroke={stroke}
        strokeWidth={width}
        strokeLinecap="round"
        strokeLinejoin="round"
        opacity={p > 0 ? 1 : 0}
      />
    </g>
  );
};

/** Crumpled paper made from lit noise, like the reference clip. */
const Paper: React.FC = () => (
  <svg width={1080} height={1920} style={{ position: "absolute" }}>
    <defs>
      <filter id="crumple" x="0" y="0" width="100%" height="100%">
        <feTurbulence type="fractalNoise" baseFrequency="0.009" numOctaves="5" seed="11" result="noise" />
        <feDiffuseLighting in="noise" lightingColor="#ffffff" surfaceScale="4">
          <feDistantLight azimuth="235" elevation="58" />
        </feDiffuseLighting>
      </filter>
      <radialGradient id="vignette" cx="50%" cy="50%" r="75%">
        <stop offset="60%" stopColor="#000" stopOpacity="0" />
        <stop offset="100%" stopColor="#3b2f1e" stopOpacity="0.28" />
      </radialGradient>
    </defs>
    <rect width={1080} height={1920} filter="url(#crumple)" />
    <rect width={1080} height={1920} fill={PAPER} opacity={0.42} />
    <rect width={1080} height={1920} fill="url(#vignette)" />
  </svg>
);

/** Re-seeded displacement every few frames gives the "boiling" hand-drawn line. */
const InkFilter: React.FC = () => {
  const frame = useCurrentFrame();
  const seed = Math.floor(frame / 4) % 3;
  return (
    <filter id="ink" x="-5%" y="-5%" width="110%" height="110%">
      <feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed={seed} />
      <feDisplacementMap in="SourceGraphic" scale="4.5" />
    </filter>
  );
};

const Face: React.FC<{ y: number }> = ({ y }) => (
  <>
    <circle cx={-14} cy={y + 3} r={4.5} fill={INK} />
    <circle cx={14} cy={y + 3} r={4.5} fill={INK} />
    <circle cx={-24} cy={y + 15} r={6.5} fill="#f48aa8" opacity={0.6} />
    <circle cx={24} cy={y + 15} r={6.5} fill="#f48aa8" opacity={0.6} />
    <path d={`M -11 ${y + 18} Q 0 ${y + 28} 11 ${y + 18}`} stroke={INK} strokeWidth={4} fill="none" strokeLinecap="round" />
  </>
);

const Crown: React.FC<{ y: number; size?: number; scale: number }> = ({ y, size = 1, scale }) => (
  <g transform={`translate(0 ${y}) scale(${size * scale})`}>
    <path d="M -26 0 L -28 -28 L -13 -12 L 0 -34 L 13 -12 L 28 -28 L 26 0 Z" fill="#f5c518" stroke={INK} strokeWidth={4} strokeLinejoin="round" />
    <circle cx={0} cy={-8} r={4.5} fill="#e5484d" />
  </g>
);

/** The little girl. Feet at the origin, about 340 units tall. */
const Girl: React.FC<{
  phase: number;
  walking: number;
  crown?: number;
  hop?: number;
  armUp?: number;
}> = ({ phase, walking, crown = 0, hop = 0, armUp = 0 }) => {
  const swing = Math.sin(phase) * 24 * walking;
  const bob = -Math.abs(Math.sin(phase)) * 6 * walking - hop;

  const leg = (hipX: number, deg: number) => {
    const r = (deg * Math.PI) / 180;
    const ex = hipX + Math.sin(r) * 115;
    const ey = -120 + Math.cos(r) * 115;
    return `M ${hipX} -120 L ${ex} ${ey + hop} L ${ex + 14} ${ey + hop}`;
  };
  const arm = (side: number, deg: number) => {
    const r = (deg * Math.PI) / 180;
    return `M ${side * 10} -222 L ${side * 10 + Math.sin(r) * 82} ${-222 + Math.cos(r) * 82}`;
  };
  const rightArmDeg = interpolate(armUp, [0, 1], [28 - swing * 0.8, 150]);

  return (
    <g strokeLinecap="round" strokeLinejoin="round">
      <ellipse cx={0} cy={4} rx={60} ry={9} fill={INK} opacity={0.12} />
      <g transform={`translate(0 ${bob})`}>
        <path d={leg(-12, swing)} stroke={INK} strokeWidth={7} fill="none" />
        <path d={leg(12, -swing)} stroke={INK} strokeWidth={7} fill="none" />
        <path d={arm(-1, -28 + swing * 0.8)} stroke={INK} strokeWidth={7} fill="none" />
        <path d={arm(1, rightArmDeg)} stroke={INK} strokeWidth={7} fill="none" />
        <path d="M -14 -238 L 14 -238 L 62 -118 Q 0 -106 -62 -118 Z" fill={PINK} stroke={INK} strokeWidth={5} />
        <line x1={0} y1={-256} x2={0} y2={-238} stroke={INK} strokeWidth={7} />
        <circle cx={0} cy={-295} r={40} fill="#fffaf3" stroke={INK} strokeWidth={6} />
        <path
          d="M -44 -292 C -52 -352, 52 -352, 44 -292 L 47 -258 Q 32 -262 30 -286 Q 0 -300 -30 -286 Q -32 -262 -47 -258 Z"
          fill={INK}
        />
        <Face y={-296} />
        {crown > 0 ? <Crown y={-330} scale={crown} /> : null}
      </g>
    </g>
  );
};

/** The grown-up princess she sees in the mirror. Feet at the origin. */
const Princess: React.FC = () => {
  const frame = useCurrentFrame();
  const sway = Math.sin(frame / 14) * 2.5;
  const twinkle = 1 + Math.sin(frame / 4) * 0.15;
  return (
    <g strokeLinecap="round" strokeLinejoin="round" transform={`rotate(${sway * 0.3})`}>
      <path
        d="M -42 -470 C -52 -532, 52 -532, 42 -470 C 52 -420, 62 -380, 54 -338 L 30 -350 C 34 -392, 30 -432, 26 -462 Q 0 -478 -26 -462 C -30 -432, -34 -392, -30 -350 L -54 -338 C -62 -380, -52 -420, -42 -470 Z"
        fill={INK}
      />
      <path d={`M -16 -340 C -40 -220, -110 -80, ${-152 - sway} 0 Q 0 22 ${152 + sway} 0 C 110 -80, 40 -220, 16 -340 Z`} fill={PINK} stroke={INK} strokeWidth={5} />
      <path d="M -122 -48 Q -61 -26 0 -48 Q 61 -26 122 -48" stroke={INK} strokeWidth={4} fill="none" />
      <path d="M -82 -150 Q -41 -132 0 -150 Q 41 -132 82 -150" stroke={INK} strokeWidth={3} fill="none" opacity={0.6} />
      <path d="M -22 -416 L 22 -416 L 16 -340 L -16 -340 Z" fill="#ee7fae" stroke={INK} strokeWidth={5} />
      <path d="M -20 -404 L -58 -330 L -40 -296" stroke={INK} strokeWidth={7} fill="none" />
      <path d="M 20 -404 L 78 -470" stroke={INK} strokeWidth={7} fill="none" />
      <line x1={78} y1={-470} x2={98} y2={-548} stroke={INK} strokeWidth={5} />
      <g transform={`translate(100 -562) scale(${twinkle})`}>
        <path d={starPath(20)} fill="#f5c518" stroke={INK} strokeWidth={3} />
      </g>
      <line x1={0} y1={-432} x2={0} y2={-416} stroke={INK} strokeWidth={7} />
      <circle cx={0} cy={-470} r={38} fill="#fffaf3" stroke={INK} strokeWidth={6} />
      <path d="M -40 -470 C -48 -522, 48 -522, 40 -470 Q 20 -500 -2 -488 Q -22 -500 -40 -470 Z" fill={INK} />
      <Face y={-472} />
      <Crown y={-506} size={1.25} scale={1} />
    </g>
  );
};

const Mirror = { cx: 640, cy: 1000, rx: 250, ry: 370 };

const MirrorStand: React.FC = () => {
  const { cx, cy, rx } = Mirror;
  const s = T.mirror;
  return (
    <>
      <Draw d={`M ${cx - rx - 22} 1500 L ${cx - rx - 22} ${cy}`} start={s} dur={22} width={9} />
      <Draw d={`M ${cx + rx + 22} 1500 L ${cx + rx + 22} ${cy}`} start={s} dur={22} width={9} />
      <Draw d={`M ${cx - rx - 50} 1500 L ${cx - rx + 6} 1500`} start={s + 10} dur={10} width={9} />
      <Draw d={`M ${cx + rx - 6} 1500 L ${cx + rx + 50} 1500`} start={s + 10} dur={10} width={9} />
    </>
  );
};

const MirrorFrame: React.FC = () => {
  const { cx, cy, rx, ry } = Mirror;
  const s = T.mirror + 15;
  return (
    <>
      <Draw d={ellipsePath(cx, cy, rx + 12, ry + 12)} start={s} dur={40} stroke={GOLD} width={18} />
      <Draw d={ellipsePath(cx, cy, rx + 12, ry + 12)} start={s + 4} dur={40} width={4} opacity={0.8} />
      <Draw d={ellipsePath(cx, cy, rx - 4, ry - 4)} start={s + 8} dur={40} width={3} opacity={0.7} />
      <Draw
        d={`M ${cx} ${cy - ry - 18} C ${cx - 40} ${cy - ry - 70}, ${cx - 80} ${cy - ry - 20}, ${cx} ${cy - ry - 18} C ${cx + 80} ${cy - ry - 20}, ${cx + 40} ${cy - ry - 70}, ${cx} ${cy - ry - 18}`}
        start={s + 35}
        dur={18}
        stroke={GOLD}
        width={8}
        fill="#f5c518"
      />
      <Draw d={`M ${cx - rx - 22} ${cy} L ${cx - rx - 10} ${cy}`} start={s + 30} dur={6} width={9} />
      <Draw d={`M ${cx + rx + 10} ${cy} L ${cx + rx + 22} ${cy}`} start={s + 30} dur={6} width={9} />
    </>
  );
};

const Castle: React.FC = () => {
  const s = T.castle;
  const c = "#8b7fc7";
  return (
    <g opacity={0.85}>
      <Draw d="M 520 880 L 520 760 L 545 760 L 545 740 L 560 740 L 560 760 L 580 760 L 580 880" start={s} dur={25} stroke={c} width={5} fill="#e9e4fb" />
      <Draw d="M 700 880 L 700 760 L 720 760 L 720 740 L 735 740 L 735 760 L 760 760 L 760 880" start={s + 6} dur={25} stroke={c} width={5} fill="#e9e4fb" />
      <Draw d="M 580 880 L 580 790 L 700 790 L 700 880" start={s + 12} dur={25} stroke={c} width={5} fill="#f1edfd" />
      <Draw d="M 600 790 L 640 700 L 680 790" start={s + 18} dur={20} stroke={c} width={5} fill="#d8cff7" />
      <Draw d="M 640 700 L 640 665 L 668 676 L 640 686" start={s + 30} dur={12} stroke={c} width={4} fill="#f48aa8" />
      <Draw d="M 520 760 L 550 715 L 580 760 M 700 760 L 730 715 L 760 760" start={s + 24} dur={18} stroke={c} width={5} />
    </g>
  );
};

const Reflection: React.FC = () => {
  const frame = useCurrentFrame();
  const { cx, cy, rx, ry } = Mirror;
  const littleOpacity =
    interpolate(frame, [T.reflection, T.reflection + 30], [0, 0.85], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }) *
    interpolate(frame, [T.magic, T.magic + 20], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const princess = usePop(T.princess, 14);
  const flash = interpolate(frame, [T.magic - 5, T.magic + 8, T.magic + 35], [0, 0.95, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const shimmer = interpolate(frame, [T.reflection - 10, T.reflection + 30], [-500, 500], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const glass = progress(frame, T.mirror + 40, 30);

  return (
    <g>
      <clipPath id="glass">
        <path d={ellipsePath(cx, cy, rx, ry)} />
      </clipPath>
      <g clipPath="url(#glass)">
        <rect x={cx - rx} y={cy - ry} width={rx * 2} height={ry * 2} fill="#dcecf3" opacity={glass * 0.75} />
        <Castle />
        <g transform={`translate(${cx} 1300) scale(-1 1)`} opacity={littleOpacity}>
          <Girl phase={0} walking={0} />
        </g>
        <g transform={`translate(${cx} 1325) scale(${0.85 * princess})`} opacity={Math.min(1, princess * 1.4)}>
          <Princess />
        </g>
        <rect x={cx + shimmer - 40} y={cy - ry - 100} width={60} height={ry * 2 + 200} fill="#fff" opacity={0.7} transform={`rotate(20 ${cx} ${cy})`} />
        <rect x={cx + shimmer + 40} y={cy - ry - 100} width={18} height={ry * 2 + 200} fill="#fff" opacity={0.6} transform={`rotate(20 ${cx} ${cy})`} />
        <rect x={cx - rx} y={cy - ry} width={rx * 2} height={ry * 2} fill="#fff" opacity={flash} />
      </g>
    </g>
  );
};

const Sparkle: React.FC<{ x: number; y: number; start: number; size?: number; color?: string }> = ({
  x,
  y,
  start,
  size = 26,
  color = "#f5c518",
}) => {
  const frame = useCurrentFrame();
  const life = interpolate(frame, [start, start + 10, start + 26], [0, 1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  if (life <= 0) return null;
  return (
    <g transform={`translate(${x} ${y}) rotate(${(frame - start) * 4}) scale(${size * life})`}>
      <path d={SPARKLE} fill={color} stroke={INK} strokeWidth={0.08} />
    </g>
  );
};

const MagicBurst: React.FC = () => {
  const pts = Array.from({ length: 14 }, (_, i) => {
    const a = (i / 14) * Math.PI * 2;
    const r = 300 + (i % 3) * 70;
    return { x: Mirror.cx + Math.cos(a) * r, y: Mirror.cy + Math.sin(a) * r * 1.25, d: (i * 3) % 14 };
  });
  return (
    <>
      {pts.map((p, i) => (
        <Sparkle key={i} x={p.x} y={p.y} start={T.magic + p.d} size={18 + (i % 3) * 8} />
      ))}
    </>
  );
};

const Rainbow: React.FC = () => {
  const colors = ["#e5484d", "#f5a524", "#f5d90a", "#46a758", "#3e9fd8", "#8e4ec6"];
  const cx = 640;
  const cy = 720;
  return (
    <g opacity={0.75}>
      {colors.map((c, i) => {
        const r = 400 - i * 18;
        return (
          <Draw key={c} d={`M ${cx - r} ${cy} A ${r} ${r} 0 0 1 ${cx + r} ${cy}`} start={T.rainbow + i * 3} dur={40} stroke={c} width={20} />
        );
      })}
    </g>
  );
};

const Cloud: React.FC<{ x: number; y: number; start: number }> = ({ x, y, start }) => {
  const pop = usePop(start);
  return (
    <g transform={`translate(${x} ${y}) scale(${pop})`}>
      <path
        d="M -70 20 Q -90 -10 -55 -20 Q -50 -55 -10 -45 Q 15 -70 45 -40 Q 85 -40 75 0 Q 90 25 55 28 L -50 28 Q -80 30 -70 20 Z"
        fill="#ffffff"
        stroke={INK}
        strokeWidth={5}
        strokeLinejoin="round"
      />
    </g>
  );
};

const Flower: React.FC<{ x: number; start: number; h: number; color: string }> = ({ x, start, h, color }) => {
  const bloom = usePop(start + 18, 9);
  const frame = useCurrentFrame();
  const sway = Math.sin((frame + x) / 16) * 3;
  return (
    <g>
      <Draw d={`M ${x} 1500 Q ${x - 12} ${1500 - h / 2} ${x} ${1500 - h}`} start={start} dur={20} width={5} />
      <Draw d={`M ${x - 2} ${1500 - h * 0.4} q -30 -10 -36 -30 q 26 0 36 26`} start={start + 10} dur={12} width={4} fill="#6cbf5f" />
      <g transform={`translate(${x} ${1500 - h}) rotate(${sway}) scale(${bloom})`}>
        {[0, 72, 144, 216, 288].map((a) => (
          <ellipse key={a} cx={0} cy={-18} rx={13} ry={20} fill={color} stroke={INK} strokeWidth={4} transform={`rotate(${a})`} />
        ))}
        <circle r={12} fill="#f5c518" stroke={INK} strokeWidth={4} />
      </g>
    </g>
  );
};

const Star: React.FC<{ x: number; y: number; start: number; r?: number }> = ({ x, y, start, r = 26 }) => {
  const frame = useCurrentFrame();
  const pop = usePop(start, 8);
  const twinkle = 1 + Math.sin((frame + x) / 6) * 0.1;
  return (
    <g transform={`translate(${x} ${y}) rotate(${Math.sin((frame + y) / 20) * 10}) scale(${pop * twinkle})`}>
      <path d={starPath(r)} fill="#f5c518" stroke={INK} strokeWidth={4} strokeLinejoin="round" />
    </g>
  );
};

const Butterfly: React.FC<{ start: number; from: [number, number]; to: [number, number]; color: string }> = ({
  start,
  from,
  to,
  color,
}) => {
  const frame = useCurrentFrame();
  const t = interpolate(frame, [start, start + 120], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.inOut(Easing.quad),
  });
  if (frame < start) return null;
  const x = interpolate(t, [0, 1], [from[0], to[0]]) + Math.sin(t * Math.PI * 3) * 40;
  const y = interpolate(t, [0, 1], [from[1], to[1]]) - Math.sin(t * Math.PI) * 120;
  const flap = 0.25 + Math.abs(Math.sin(frame / 2.2)) * 0.75;
  const appear = Math.min(1, (frame - start) / 8);
  return (
    <g transform={`translate(${x} ${y}) scale(${appear})`}>
      <g transform={`scale(${flap} 1)`}>
        <path d="M 0 0 C -40 -50, -70 -10, -40 10 C -60 30, -30 50, 0 10 Z" fill={color} stroke={INK} strokeWidth={4} />
        <path d="M 0 0 C 40 -50, 70 -10, 40 10 C 60 30, 30 50, 0 10 Z" fill={color} stroke={INK} strokeWidth={4} />
      </g>
      <line x1={0} y1={-14} x2={0} y2={22} stroke={INK} strokeWidth={5} strokeLinecap="round" />
    </g>
  );
};

const Heart: React.FC<{ x: number; start: number }> = ({ x, start }) => {
  const frame = useCurrentFrame();
  const t = frame - start;
  if (t < 0) return null;
  const y = 1150 - t * 4.5;
  const opacity = interpolate(t, [0, 10, 80, 110], [0, 1, 1, 0], { extrapolateRight: "clamp" });
  return (
    <g transform={`translate(${x + Math.sin(t / 10) * 22} ${y}) scale(1.1)`} opacity={opacity}>
      <path d="M 0 12 C -30 -8, -24 -32, 0 -18 C 24 -32, 30 -8, 0 12 Z" fill="#e5484d" stroke={INK} strokeWidth={3.5} strokeLinejoin="round" />
    </g>
  );
};

const Books: React.FC = () => {
  const b = [
    { c: "#3e9fd8", w: 120, s: T.likes + 10 },
    { c: "#e5484d", w: 104, s: T.likes + 16 },
    { c: "#46a758", w: 112, s: T.likes + 22 },
  ];
  return (
    <>
      {b.map((book, i) => (
        <BookItem key={i} {...book} y={1500 - (i + 1) * 30} />
      ))}
    </>
  );
};

const BookItem: React.FC<{ c: string; w: number; s: number; y: number }> = ({ c, w, s, y }) => {
  const pop = usePop(s, 10);
  return (
    <g transform={`translate(80 ${y + (1 - pop) * -120})`} opacity={Math.min(1, pop * 2)}>
      <rect x={-w / 2} y={0} width={w} height={30} rx={4} fill={c} stroke={INK} strokeWidth={4} />
      <line x1={w / 2 - 14} y1={4} x2={w / 2 - 14} y2={26} stroke="#fff" strokeWidth={4} />
    </g>
  );
};

const Cat: React.FC = () => {
  const frame = useCurrentFrame();
  const pop = usePop(T.likes + 40, 10);
  const tail = Math.sin(frame / 9) * 14;
  return (
    <g transform={`translate(985 1500) scale(${pop})`}>
      <path d="M 30 -20 C 70 -30, 80 -80, 60 -100" stroke={INK} strokeWidth={9} fill="none" strokeLinecap="round" transform={`rotate(${tail} 30 -20)`} />
      <ellipse cx={0} cy={-38} rx={45} ry={40} fill={INK} />
      <circle cx={-22} cy={-92} r={30} fill={INK} />
      <path d="M -48 -108 L -46 -140 L -26 -118 Z M 4 -108 L 2 -140 L -18 -118 Z" fill={INK} />
      <circle cx={-32} cy={-95} r={4} fill="#f5d90a" />
      <circle cx={-12} cy={-95} r={4} fill="#f5d90a" />
    </g>
  );
};

const Caption: React.FC<{ text: string; start: number; end: number; y: number; size?: number }> = ({
  text,
  start,
  end,
  y,
  size = 110,
}) => {
  const frame = useCurrentFrame();
  const reveal = progress(frame, start, 30);
  const out = interpolate(frame, [end - 15, end], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  if (frame < start || frame > end) return null;
  return (
    <g opacity={out}>
      <clipPath id={`clip-${start}`}>
        <rect x={0} y={y - size} width={1080 * reveal} height={size * 1.5} />
      </clipPath>
      <text x={540} y={y} textAnchor="middle" fontFamily={fontFamily} fontWeight={700} fontSize={size} fill={INK} clipPath={`url(#clip-${start})`}>
        {text}
      </text>
    </g>
  );
};

const LittleGirl: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const x = interpolate(frame, [T.walkStart, T.walkEnd], [-120, 230], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.quad),
  });
  const walking = interpolate(frame, [T.walkStart, T.walkStart + 8, T.walkEnd - 12, T.walkEnd], [0, 1, 1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const crown = spring({ frame: frame - T.girlCrown, fps, config: { damping: 9 } });
  const hopT = frame - (T.girlCrown + 8);
  const hop = hopT > 0 && hopT < 36 ? Math.abs(Math.sin((hopT / 18) * Math.PI)) * 40 : 0;
  const armUp = interpolate(frame, [T.girlCrown + 5, T.girlCrown + 15], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  return (
    <g transform={`translate(${x} 1500)`}>
      <Girl phase={frame / 4.2} walking={walking} crown={crown} hop={hop} armUp={armUp} />
    </g>
  );
};

export const MirrorPrincess: React.FC = () => {
  return (
    <AbsoluteFill style={{ backgroundColor: PAPER }}>
      <Paper />
      <svg width={1080} height={1920} viewBox="0 0 1080 1920" style={{ position: "absolute" }}>
        <defs>
          <InkFilter />
        </defs>
        <g filter="url(#ink)">
          <Draw d="M 20 1500 C 300 1492, 700 1508, 1060 1498" start={T.ground} dur={35} width={6} />
          <Draw d="M 150 1500 l -6 -22 M 160 1500 l 4 -26 M 900 1500 l -6 -20 M 910 1500 l 5 -24" start={T.ground + 20} dur={15} width={4} />

          <Rainbow />
          <Cloud x={300} y={712} start={T.rainbow + 30} />
          <Cloud x={980} y={712} start={T.rainbow + 36} />

          <MirrorStand />
          <Reflection />
          <MirrorFrame />

          <Flower x={430} start={T.likes} h={110} color="#f48aa8" />
          <Flower x={850} start={T.likes + 8} h={140} color="#8e4ec6" />
          <Flower x={330} start={T.likes + 16} h={90} color="#3e9fd8" />
          <Flower x={1040} start={T.likes + 24} h={120} color="#e5484d" />
          <Books />
          <Cat />

          <LittleGirl />

          <Star x={130} y={330} start={T.likes + 5} />
          <Star x={950} y={300} start={T.likes + 12} r={32} />
          <Star x={90} y={1030} start={T.likes + 20} r={20} />
          <Star x={1000} y={1060} start={T.likes + 26} r={22} />
          <Star x={300} y={480} start={T.likes + 32} r={18} />
          <Star x={790} y={470} start={T.likes + 38} r={18} />

          <Butterfly start={T.likes + 10} from={[420, 900]} to={[130, 760]} color="#f5a524" />
          <Butterfly start={T.likes + 30} from={[880, 1100]} to={[960, 560]} color="#3e9fd8" />

          {[560, 700, 620, 760, 520].map((x, i) => (
            <Heart key={i} x={x} start={T.likes + 20 + i * 14} />
          ))}

          <MagicBurst />
          <Sparkle x={230} y={1140} start={T.girlCrown - 4} size={34} />
          <Sparkle x={180} y={1190} start={T.girlCrown + 2} size={22} />
          <Sparkle x={290} y={1180} start={T.girlCrown + 6} size={24} />

          <Caption text="One day..." start={T.textOneDay} end={T.rainbow} y={190} />
          <Caption text="Dream it. Become it." start={T.textEnd} end={9999} y={190} size={100} />
        </g>
      </svg>
    </AbsoluteFill>
  );
};
