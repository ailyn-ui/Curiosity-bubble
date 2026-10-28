import React from "react";
import { Composition, delayRender, continueRender } from "remotion";
import { MessageMirrorReel } from "./MessageMirrorReel";
import { fontsReady } from "./theme";

const handle = delayRender("Loading Playfair Display");
fontsReady.then(() => continueRender(handle));

// 6 scenes (426 frames) minus 5 fade overlaps of 8 frames = 386 frames, ~12.9s.
export const RemotionRoot: React.FC = () => (
  <Composition
    id="MessageMirrorHalloween"
    component={MessageMirrorReel}
    durationInFrames={386}
    fps={30}
    width={1080}
    height={1920}
  />
);
