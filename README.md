# GHOST FREQUENCY / GF—808

Created by [@ChainZenit](https://x.com/ChainZenit).

[Play GHOST FREQUENCY](https://podzemniytip.github.io/ghost-frequency/)


Playable drum machine: original local MP3 samples, 8 pads, a 16-step sequencer, swing, tone, volume, presets, browser storage, animated exploded assembly, and sound-reactive native WebGL.


## Run locally


Run `python -m http.server 8080` in this folder and open http://localhost:8080. No build or npm dependencies. Use an HTTP server: browser audio fetching does not work from `file://`.


## Play


- Pads: A S D F J K L ; (physical keys also work with Russian keyboard layout).
- Space: play / stop; click the grid to edit steps.
- РАЗОБРАТЬ: explode the chassis, board and front panel. The pads remain playable.
- СОХРАНИТЬ: save pattern, tempo and swing in this browser's local storage.
- Playback stops when the tab is hidden to prevent timing drift.


## GitHub Pages


Push to the `main` branch. In repository Settings → Pages → Build and deployment, select **GitHub Actions**. The included workflow deploys only the website files and audio. Relative paths support both repository and custom-domain Pages sites.


## Audio


Eight original synthesized percussion recordings are committed as MP3 under `assets/audio`. No external sample licenses or API services required. Regenerate with Python and FFmpeg: `python scripts/generate_audio.py`.


Google Fonts is optional: system fallback fonts work if offline. WebGL is decorative; the instrument remains functional when WebGL is unavailable. Reduced-motion preferences disable decorative motion.

