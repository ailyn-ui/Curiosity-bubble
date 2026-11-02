// The reel, scene by scene. Lines come from the essay "Putting the weight down".
// `big` is the bold capitals line, `small` the quieter line under it.
// `pink` is the one word in `big` that turns pink.
export type Scene = {
  element: string;
  big?: string;
  small?: string;
  pink?: string;
  // Direction the ink paints in from.
  from: "left" | "right" | "top" | "bottom";
};

export const SCENES: Scene[] = [
  { element: "enso", big: "You don't have a discipline problem.", pink: "discipline", from: "left" },
  { element: "mountain", small: "Even on the days opening your laptop feels harder than lifting a boulder.", from: "bottom" },
  { element: "cloud", small: "You eat. You scroll. You start that other idea. Just to get some dopamine in.", from: "left" },
  { element: "strokes", big: "Be more consistent. Fix your mindset. Push through.", small: "The standard advice.", from: "top" },
  { element: "butterfly", small: "And RSD makes it easy to assume it's all on you.", from: "right" },
  { element: "swoosh", big: "You're running your business on adrenaline and cortisol.", pink: "cortisol", from: "left" },
  { element: "cosmos", big: "Your brain runs a body budget.", pink: "body", small: "Ask it for high energy every morning just to keep revenue moving, and it treats that as a crisis.", from: "bottom" },
  { element: "palm", small: "Your ideas, your framework, your track record", big: "need a home outside your head.", pink: "outside", from: "right" },
  { element: "peony", big: "An external structure that holds the weight,", small: "so your body and your brain don't have to.", from: "bottom" },
  { element: "bird", big: "Put the weight down.", pink: "down", small: "Ailyn Eida", from: "left" },
];

const FPS = 30;
const words = (s?: string) => (s ? s.split(/\s+/).length : 0);

// Long enough to read: about 3.3 words a second plus a beat to look.
export const sceneFrames = (s: Scene) =>
  Math.round(FPS * Math.min(6, Math.max(2.6, 1.4 + (words(s.big) + words(s.small)) * 0.3)));

export const FADE = 10;
export const totalFrames = SCENES.reduce((t, s) => t + sceneFrames(s), 0) - FADE * (SCENES.length - 1);
