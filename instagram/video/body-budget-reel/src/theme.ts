import { loadFont } from "@remotion/fonts";
import { staticFile } from "remotion";

export const PINK = "#E6005C";
export const INK = "#0B0B0B";
export const PAPER = "#FFFFFF";
export const SERIF = "Playfair";

// Instagram Reels safe zone on a 1080x1920 frame.
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
