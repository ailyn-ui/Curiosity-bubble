import { Composition } from "remotion";
import { MirrorPrincess } from "./MirrorPrincess";

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="MirrorPrincess"
      component={MirrorPrincess}
      durationInFrames={480}
      fps={30}
      width={1080}
      height={1920}
    />
  );
};
