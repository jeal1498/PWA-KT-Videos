#!/bin/bash
# Uso: armar.sh <trabajo> [--vistazo [cada_s]]
# Arma el video de punta a punta. Correrlo con run_in_background (el render tarda 6 a 9 min): no hace falta esperar con pgrep.
#   --vistazo   solo build + hoja de cuadros cada 2 s (vistazo.jpg) para buscar huecos y textos encimados; sin render.
# Sin --vistazo: build.py (si existe; con cara, componer.py ya dejó public/index.html) → render → voz (v2: voz.mp3 con
# la cola de 0.6 s del aviso) → portada como primer cuadro → final.mp4 (≤60 MB) y prueba-720.mp4 (para SendUserFile).
set -e
SK="$(cd "$(dirname "$0")/.." && pwd)"; W="$(realpath "$1")"; HF="npx --yes hyperframes@0.8.163"
cd "$W"
[ -f build.py ] && python3 build.py
DUR=$(python3 -c "import re;print(re.search(r'data-duration=\"([0-9.]+)\"',open('public/index.html').read()).group(1))")
if [ "$2" = "--vistazo" ]; then
  T=$(python3 -c "import sys;d=float(sys.argv[1]);s=float(sys.argv[2]);print(','.join(f'{x*s:.1f}' for x in range(int(d/s)+1)))" "$DUR" "${3:-2}")
  $HF snapshot public --at "$T" 2>&1 | tail -2
  D=$(ls -td public/.hyperframes/artifacts/snapshots/*/ | head -1); rm -f vistazo-*.jpg
  for f in "$D"contact-sheet-*.jpg; do cp "$f" "vistazo-${f##*-}"; done; ls "$W"/vistazo-*.jpg
  exit 0
fi
[ -f portada.png ] || { echo "✗ falta portada.png (portada.sh o portada.py)"; exit 1; }
echo "render ($DUR s)…"
PRODUCER_BROWSER_GPU_MODE=software $HF render public --fps 30 -o render.mp4 > render.log 2>&1 || { tail -20 render.log; exit 1; }
if [ -f voz.mp3 ]; then
  ffmpeg -v error -y -i render.mp4 -i voz.mp3 -map 0:v -map 1:a -af apad -t "$DUR" -c:v copy -c:a aac -b:a 160k master.mp4
else
  mv -f render.mp4 master.mp4
fi
bash "$SK/scripts/portada_primer_cuadro.sh" master.mp4 portada.png final.mp4
if [ $(stat -c %s final.mp4) -gt 62914560 ]; then  # >60 MB: recomprimir (el de 1080p con foto sale ≈87 MB)
  ffmpeg -v error -y -i final.mp4 -c:v libx264 -preset medium -crf 28 -c:a copy -movflags +faststart final-l.mp4 && mv final-l.mp4 final.mp4
fi
ffmpeg -v error -y -i final.mp4 -vf scale=720:-2 -c:v libx264 -preset fast -crf 27 -c:a aac -b:a 128k -movflags +faststart prueba-720.mp4
for f in final.mp4 prueba-720.mp4; do echo "$f: $(ffprobe -v error -show_entries format=duration -of csv=p=0 $f) s, $(( $(stat -c %s $f) / 1048576 )) MB"; done
