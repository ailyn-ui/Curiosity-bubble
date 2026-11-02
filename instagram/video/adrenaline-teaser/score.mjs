// node score.mjs score.wav — 30 s, 48 kHz stereo, synthesized. Events match piece.html's timeline.
import fs from 'fs';
const SR = 48000, DUR = 30.5, N = Math.floor(SR * DUR);
const L = new Float32Array(N), R = new Float32Array(N);
const sendL = new Float32Array(N), sendR = new Float32Array(N);
let seed = 12345; const rnd = () => (seed = (seed * 1664525 + 1013904223) >>> 0) / 4294967296;
const NOTE = { C: 0, 'C#': 1, D: 2, 'D#': 3, E: 4, F: 5, 'F#': 6, G: 7, 'G#': 8, A: 9, 'A#': 10, B: 11 };
function hz(n) { const m = n.match(/^([A-G]#?)(\d)$/); if (!m) throw new Error('bad note ' + n); return 440 * Math.pow(2, (NOTE[m[1]] + (+m[2] + 1) * 12 - 69) / 12); }
function add(i, l, r, send = 0.3) { if (i < 0 || i >= N) return; L[i] += l; R[i] += r; sendL[i] += l * send; sendR[i] += r * send; }

// ---- pad: detuned sines with slow attack/release ----
function pad(t0, t1, notes, gain = 0.05, att = 1.6, rel = 2.2) {
  const fs_ = notes.map(hz);
  for (let i = Math.floor(t0 * SR); i < Math.min(N, Math.floor((t1 + rel) * SR)); i++) {
    const t = i / SR, e = Math.min(1, (t - t0) / att) * (t > t1 ? Math.max(0, 1 - (t - t1) / rel) : 1);
    let l = 0, r = 0;
    fs_.forEach((f, k) => { for (const d of [-0.12, 0.12]) { const s = Math.sin(2 * Math.PI * f * (1 + d / 100) * t + k); if (d < 0) l += s; else r += s; } });
    const trem = 1 + 0.08 * Math.sin(2 * Math.PI * 0.2 * t);
    add(i, l * gain * e * trem / fs_.length, r * gain * e * trem / fs_.length, 0.5);
  }
}
// ---- Karplus-Strong pluck ----
function pluck(t0, n, gain = 0.25, pan = 0, decay = 0.996) {
  const f = hz(n), len = Math.round(SR / f), buf = new Float32Array(len);
  for (let k = 0; k < len; k++) buf[k] = rnd() * 2 - 1;
  let idx = 0; const i0 = Math.floor(t0 * SR);
  for (let k = 0; k < SR * 3; k++) {
    const a = buf[idx], b = buf[(idx + 1) % len]; buf[idx] = decay * 0.5 * (a + b);
    const s = a * gain; add(i0 + k, s * (1 - pan) * 0.7, s * (1 + pan) * 0.7, 0.45); idx = (idx + 1) % len;
  }
}
// ---- bell: inharmonic partials ----
function bell(t0, n, gain = 0.08, pan = 0) {
  const f = hz(n), parts = [[1, 1], [2.76, 0.5], [5.4, 0.25], [8.9, 0.12]], i0 = Math.floor(t0 * SR);
  for (let k = 0; k < SR * 4; k++) {
    const t = k / SR; let s = 0; parts.forEach(([m, a], j) => { s += a * Math.sin(2 * Math.PI * f * m * t) * Math.exp(-t * (1.2 + j * 1.5)); });
    s *= gain * Math.min(1, t * 400); add(i0 + k, s * (1 - pan), s * (1 + pan), 0.6);
  }
}
// ---- filtered noise with gliding cutoff (state-variable band-pass) ----
function noise(t0, dur, f0, f1, gain, pan0 = 0, pan1 = 0, shape = 'swell', am = 0) {
  let low = 0, band = 0; const i0 = Math.floor(t0 * SR), n = Math.floor(dur * SR);
  for (let k = 0; k < n; k++) {
    const p = k / n, fc = f0 * Math.pow(f1 / f0, p), F = 2 * Math.sin(Math.PI * Math.min(fc, SR / 6) / SR), q = 0.7;
    const x = rnd() * 2 - 1; low += F * band; const high = x - low - q * band; band += F * high;
    let env = shape === 'swell' ? Math.sin(Math.PI * p) ** 2 : shape === 'rise' ? p * p * (1 - Math.max(0, (p - 0.92) / 0.08)) : Math.exp(-p * 6);
    if (am) env *= 0.55 + 0.45 * Math.sin(2 * Math.PI * am * k / SR);
    const pan = pan0 + (pan1 - pan0) * p, s = band * gain * env;
    add(i0 + k, s * (1 - pan), s * (1 + pan), 0.35);
  }
}
// ---- chirp: short sine sweeps ----
function chirp(t0, f0, f1, dur, gain = 0.05, pan = 0.5) {
  const i0 = Math.floor(t0 * SR), n = Math.floor(dur * SR); let ph = 0;
  for (let k = 0; k < n; k++) { const p = k / n, f = f0 + (f1 - f0) * p; ph += 2 * Math.PI * f / SR; const s = Math.sin(ph) * gain * Math.sin(Math.PI * p); add(i0 + k, s * (1 - pan), s * (1 + pan), 0.5); }
}

// ================= the score (times from piece.html) =================
// Pad harmony: D major, calm. Changes where the picture changes.
pad(0.0, 4.4, ['D3', 'A3', 'E4', 'F#4'], 0.055, 0.8);
pad(4.4, 9.3, ['B2', 'F#3', 'D4', 'A4'], 0.055);
pad(9.3, 13.4, ['G2', 'D3', 'B3', 'F#4'], 0.055);
pad(13.4, 18.3, ['E3', 'B3', 'D4', 'G4'], 0.045);          // ideas leave: thinner
pad(18.3, 25.3, ['D3', 'A3', 'F#4'], 0.04, 2.5);           // the breath: the bloom
pad(25.3, 30.0, ['G2', 'D3', 'A3', 'B3', 'F#4'], 0.055, 1.2, 1.2);

// Ideas leave one by one (6.0, 7.4, 8.8, 10.2): a soft rising note for each, like letting go
[[6.0, 'D5', -0.6], [7.6, 'F#5', -0.4], [9.2, 'A5', 0.6]].forEach(([t, n, pn]) => pluck(t + 0.5, n, 0.14, pn, 0.997));

// Text cards appear: a soft pluck each time
[[0.4, 'A4'], [4.5, 'F#4'], [9.4, 'B4'], [13.7, 'D5'], [19.7, 'A4'], [25.5, 'F#5']].forEach(([t, n], k) => pluck(t, n, 0.22, k % 2 ? 0.25 : -0.25));
// Pink key words land a little later: bell
[[1.2, 'D6'], [11.2, 'A5'], [15.3, 'F#5'], [21.2, 'D6'], [25.8, 'A5']].forEach(([t, n]) => bell(t, n, 0.05, 0.1));

// The peony grows (18.4–22.6): a slow rising breath, then a chime as it opens
bell(22.6, 'D5', 0.07, -0.1); bell(22.65, 'A5', 0.05, 0.1);

// The bird flies in (22.7–24.6): wing flutter, landing tick, two chirps
noise(24.6, 0.12, 3000, 3000, 0.2, 0.5, 0.5, 'hit');
chirp(24.95, 3200, 4200, 0.07, 0.035, 0.6); chirp(25.08, 3400, 4600, 0.06, 0.03, 0.6);
chirp(26.4, 3000, 4400, 0.08, 0.03, 0.6);
// Take-off (26.0–28.8) and the butterfly following (26.4–29.4)
// End: final pluck resolves
pluck(28.6, 'D4', 0.18, 0); pluck(28.62, 'A4', 0.12, 0.2);

// ================= mix: Schroeder reverb + soft clip =================
function comb(x, d, fb) { const y = new Float32Array(x.length), b = new Float32Array(d); let i = 0, lp = 0; for (let n = 0; n < x.length; n++) { const o = b[i]; lp = o * 0.8 + lp * 0.2; b[i] = x[n] + lp * fb; y[n] = o; i = (i + 1) % d; } return y; }
function allp(x, d, g) { const y = new Float32Array(x.length), b = new Float32Array(d); let i = 0; for (let n = 0; n < x.length; n++) { const o = b[i], v = x[n] + o * g; b[i] = v; y[n] = o - v * g; i = (i + 1) % d; } return y; }
function verb(x, off) { let s = new Float32Array(x.length); for (const d of [1557, 1617, 1491, 1422, 1277, 1356]) { const c = comb(x, d + off, 0.86); for (let n = 0; n < x.length; n++) s[n] += c[n] / 6; } for (const d of [225, 556, 441]) s = allp(s, d + off, 0.5); return s; }
const vL = verb(sendL, 0), vR = verb(sendR, 23);
const out = Buffer.alloc(44 + N * 4); let peak = 0;
const mix = new Float32Array(N * 2);
for (let n = 0; n < N; n++) { const l = Math.tanh((L[n] + vL[n] * 0.9) * 1.4), r = Math.tanh((R[n] + vR[n] * 0.9) * 1.4); mix[2 * n] = l; mix[2 * n + 1] = r; peak = Math.max(peak, Math.abs(l), Math.abs(r)); if (Number.isNaN(l + r)) throw new Error('NaN at ' + n); }
if (peak < 1e-4) throw new Error('silence');
const g = 0.9 / peak;
out.write('RIFF', 0); out.writeUInt32LE(36 + N * 4, 4); out.write('WAVEfmt ', 8); out.writeUInt32LE(16, 16); out.writeUInt16LE(1, 20); out.writeUInt16LE(2, 22);
out.writeUInt32LE(SR, 24); out.writeUInt32LE(SR * 4, 28); out.writeUInt16LE(4, 32); out.writeUInt16LE(16, 34); out.write('data', 36); out.writeUInt32LE(N * 4, 40);
for (let k = 0; k < N * 2; k++) out.writeInt16LE(Math.round(Math.max(-1, Math.min(1, mix[k] * g)) * 32767), 44 + k * 2);
fs.writeFileSync(process.argv[2] || 'score.wav', out); console.log('peak', peak.toFixed(3));
