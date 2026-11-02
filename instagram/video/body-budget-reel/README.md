# Body Budget Reel (Remotion)

1080×1920, 30fps, ~45s, silent (add music in Instagram or CapCut).
Rendered output: `../../reels/2026-11-02-body-budget/body-budget-reel.mp4`

- Script (scenes, lines, pink words, paint direction): `src/script.ts`
- Animation: `src/Reel.tsx` · brand colours, fonts, safe zone: `src/theme.ts`
- Ink elements: `public/elements/*.png`, cut from Ailyn's brush sheet (12 elements; 10 used)
- Preview: `npm ci && npx remotion studio`
- Render: `npx remotion render BodyBudgetReel out/reel.mp4`
  (in a cloud session add `--browser-executable=/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell`)

Remotion is free for individuals and teams of up to 3 (https://remotion.pro/license).
