import React from "react";
import { GOLD, INK, PINK } from "../theme";

export const MIRROR = { width: 560, height: 760 };

// Ornate arched mirror. `variant` switches between the haunted gold frame
// and the clean branded frame used once the lights come on.
export const Mirror: React.FC<{
  variant: "haunted" | "clean";
  top: number;
  scale?: number;
  children?: React.ReactNode;
}> = ({ variant, top, scale = 1, children }) => {
  const haunted = variant === "haunted";
  const radius = `${MIRROR.width / 2}px ${MIRROR.width / 2}px 40px 40px`;
  const border = haunted ? 26 : 14;
  return (
    <div
      style={{
        position: "absolute",
        top,
        left: "50%",
        width: MIRROR.width,
        height: MIRROR.height,
        marginLeft: -MIRROR.width / 2 - 45,
        transform: `scale(${scale})`,
        transformOrigin: "center center",
      }}
    >
      <div
        style={{
          position: "absolute",
          inset: 0,
          borderRadius: radius,
          background: haunted
            ? `linear-gradient(135deg, #6b4e1e, ${GOLD} 30%, #f3dc9c 50%, ${GOLD} 70%, #5a3f14)`
            : INK,
          boxShadow: haunted
            ? "0 0 80px rgba(255,160,60,0.25), inset 0 0 20px rgba(0,0,0,0.6)"
            : "0 30px 80px rgba(0,0,0,0.18)",
        }}
      />
      <div
        style={{
          position: "absolute",
          inset: border,
          borderRadius: `${MIRROR.width / 2 - border}px ${MIRROR.width / 2 - border}px 28px 28px`,
          overflow: "hidden",
          background: haunted
            ? "linear-gradient(160deg, #2b3138 0%, #101418 55%, #1d232a 100%)"
            : "linear-gradient(160deg, #ffffff 0%, #f1f1f1 100%)",
          boxShadow: haunted ? "inset 0 0 60px rgba(0,0,0,0.9)" : `inset 0 0 0 4px ${PINK}`,
        }}
      >
        {children}
        <div
          style={{
            position: "absolute",
            inset: 0,
            background:
              "linear-gradient(115deg, rgba(255,255,255,0) 35%, rgba(255,255,255,0.12) 45%, rgba(255,255,255,0) 55%)",
          }}
        />
      </div>
      {haunted ? (
        <div
          style={{
            position: "absolute",
            top: -34,
            left: "50%",
            width: 70,
            height: 70,
            marginLeft: -35,
            borderRadius: "50%",
            background: `radial-gradient(circle, #f3dc9c, ${GOLD} 60%, #5a3f14)`,
          }}
        />
      ) : null}
    </div>
  );
};
