import { loadFont } from "@remotion/fonts";
import { staticFile } from "remotion";

export const PINK = "#E6005C";
export const INK = "#0B0B0B";
export const PAPER = "#FFFFFF";
export const GOLD = "#C9A45C";
export const SERIF = "Playfair";

// Instagram Reels safe zone on a 1080x1920 frame: keep clear of the top bar,
// the caption/audio strip at the bottom and the action rail on the right.
export const SAFE = { top: 250, bottom: 500, left: 110, right: 230 };

export const fontsReady = Promise.all(
  ["400", "700", "900"].map((weight) =>
    loadFont({
      family: SERIF,
      url: staticFile(`Playfair-${weight}.woff2`),
      weight,
    }),
  ),
);
