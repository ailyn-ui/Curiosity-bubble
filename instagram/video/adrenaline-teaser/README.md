# Adrenaline teaser (Motion Studio)

Every frame is drawn on a canvas in `piece.html` (open it in a browser for a live preview).
30 s, 1080×1920, 30 fps, with a synthesized soundtrack.

- Text cards and timing: the `T` object at the top of `piece.html`
- Layout: `LAYOUTS.C` ("one bloom"); A and B are the other options that were tried
- Elements: `el/*.png`, cut from Ailyn's ink brush sheet (bird split from its branch)
- Stills: `npm ci && node render.mjs piece.html --stills 2.6 12 17.5 23.6 29`
- Video: `node render.mjs piece.html out.mp4` (uses the pre-installed Chromium in a cloud session; change `exe` in `render.mjs` on your own computer)
- Sound: `node score.mjs score.wav`, then combine:
  `ffmpeg -i out.mp4 -i score.wav -c:v libx264 -crf 20 -pix_fmt yuv420p -af "loudnorm=I=-15:TP=-1.5:LRA=11,alimiter=limit=0.84:level=false" -c:a aac -b:a 256k -shortest -movflags +faststart final.mp4`
