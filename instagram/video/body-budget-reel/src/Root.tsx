import React from "react";
import { Composition, delayRender, continueRender } from "remotion";
import { Reel } from "./Reel";
import { fontsReady } from "./theme";
import { totalFrames } from "./script";

const handle = delayRender("Loading Playfair Display");
fontsReady.then(() => continueRender(handle));

export const RemotionRoot: React.FC = () => (
  <Composition id="BodyBudgetReel" component={Reel} durationInFrames={totalFrames} fps={30} width={1080} height={1920} />
);
